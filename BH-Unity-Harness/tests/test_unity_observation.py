"""Test the actual optional reducers and subprocess job runner in isolated fixtures."""
import copy
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
from support import PACKAGE, Fixture, bh, write

# The existing suite imports its own module instance; share it with the optional code.
sys.modules['bh'] = bh
OPTION = PACKAGE / 'optional/unity-observation'
def module(name):
    spec = importlib.util.spec_from_file_location(name, OPTION / (name + '.py'))
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    return m
evidence = module('unity_evidence')
jobs = module('unity_jobs')

def expectation(key, value, operator='equals'):
    return {'key': key, 'value': value, 'operator': operator, 'ac_ids': ['AC-01'], 'units': 'SYNTHETIC'}

def case(operation):
    if operation == 'search':
        return ({'query': 'synthetic', 'provider': 'SYNTHETIC', 'scope_paths': ['Source'],
                 'properties': ['value'], 'max_items': 10},
                [expectation('coverage_complete', True), expectation('match_count', 1)])
    if operation == 'smoke':
        return ({'condition_ids': ['behavior'], 'capture_source': 'screen', 'minimum_frame_advance': 1},
                [expectation('frames_advanced', True), expectation('conditions_met', True), expectation('error_count', 0)])
    if operation == 'assets':
        return ({'assets': [{'path': 'Source/value.json', 'subassets': ['Material'],
                            'bindings': {'label': {'target': 'SYNTHETIC-ID', 'method': 'set_text', 'call_state': 'RuntimeOnly'}},
                            'behavior_ids': ['updates']}]}, [expectation('asset_failures', 0)])
    if operation == 'localization':
        return ({'keys': ['label'], 'locales': ['en', 'ja'], 'code_sites': ['Source/value.json:1']},
                [expectation('missing_or_empty_entries', 0), expectation('unconverted_code_sites', 0)])
    return ({'categories': ['Code'], 'scope_paths': ['Source'], 'rules_fingerprint': 'SYNTHETIC-RULES',
             'baseline': None}, [expectation('coverage_complete', True), expectation('new_findings', 0)])

class JobFixture(Fixture):
    def __init__(self, operation='search', mode='ok', change=None):
        super().__init__('facts')
        for name in ('unity_evidence.py', 'unity_jobs.py'):
            shutil.copyfile(OPTION / name, self.root / 'Tools/BH' / name)
        shutil.copyfile(PACKAGE / 'tests/unity_provider_fixture.py', self.root / 'Tests/unity_provider_fixture.py')
        config = bh.load_json(self.root / '.bh/project.json')
        config['enabled_capabilities'] = ['unity-observation']; write(self.root, '.bh/project.json', config)
        spec, expectations = case(operation)
        if operation == 'audit':
            csv_path = write(self.root, 'Tests/baseline.csv', ','.join(evidence.CSV_COLUMNS) + '\n')
            baseline = {'source': 'unity-project-auditor', **{k: spec[k] for k in ('categories', 'scope_paths', 'rules_fingerprint')},
                        'analyzed_count': 1, 'coverage_complete': True,
                        'report': {'path': 'Tests/baseline.csv', 'sha256': bh.file_hash(csv_path)}}
            path = write(self.root, 'Tests/baseline.json', baseline)
            spec['baseline'] = {'path': 'Tests/baseline.json', 'sha256': bh.file_hash(path)}
        provider_path = 'Tests/unity_provider_fixture.py'
        config = {'version': '1.0.0', 'enabled': True, 'project_id': self.pid, 'operation': operation,
                  'session_id': 'SYNTHETIC-SESSION', 'capabilities_sha256': 'a' * 64,
                  'required_capabilities': ['observe'], 'provider_tool': 'python',
                  'provider_arguments': ['{project}/' + provider_path, '--action', '{action}', '--request', '{request}',
                                         '--project', '{project}', '--job-id', '{job_id}', '--mode', mode],
                  'provider_inputs': [{'path': provider_path, 'sha256': bh.file_hash(self.root / provider_path)}],
                  'deadline_seconds': 1 if mode == 'timeout' else 5, 'poll_interval_seconds': 0.05,
                  'max_polls': 2, 'max_response_bytes': 4096, 'spec': spec}
        if change:
            change(config)
        write(self.root, '.bh/unity-operation.json', config)
        bindings = bh.load_json(self.root / '.bh/bindings.json'); binding = bindings['checks'][0]
        binding.update(arguments=['{project}/Tools/BH/unity_jobs.py', '--root', '{project}', '--config', '.bh/unity-operation.json',
                                  '--check', 'CHECK-01', '--run', '{run_id}', '--task', '{task_id}',
                                  '--project', '{project_id}', '--result', '{result}'], timeout_seconds=20,
                       expectations=expectations, reuse_policy='never')
        paths = ['Tools/BH/unity_jobs.py', 'Tools/BH/unity_evidence.py', '.bh/unity-operation.json', provider_path]
        if operation == 'audit': paths += ['Tests/baseline.json', 'Tests/baseline.csv']
        binding['input_files'] = [{'path': path, 'sha256': bh.file_hash(self.root / path)} for path in paths]
        write(self.root, '.bh/bindings.json', bindings)
        self.h = bh.Harness(self.root)
    def journals(self):
        return sorted(self.root.glob('.bh/runs/*/CHECK-01/unity-job.json'))
    def calls(self):
        paths = sorted(self.root.glob('.bh/runs/*/CHECK-01/provider-calls.json'))
        return [json.loads(p.read_text()) for p in paths]
    def owned(self):
        return (self.root / '.bh/locks/unity-job.json').exists()

class UnityJobTests(unittest.TestCase):
    def make(self, operation='search', mode='ok', change=None):
        f = JobFixture(operation, mode, change); self.addCleanup(f.close); f.ready(); return f
    def assert_incomplete(self, f, owned=True):
        result = f.verify()
        self.assertNotEqual(result['acceptance']['AC-01'], 'PASS')
        self.assertEqual(f.owned(), owned)
        return result
    def test_success_one_submit_local_poll_and_human_pending(self):
        f = self.make(); result = f.verify()
        self.assertEqual(result['phase'], 'READY_FOR_HUMAN_REVIEW')
        self.assertEqual(result['acceptance']['AC-HUMAN'], 'HUMAN_PENDING')
        self.assertEqual(f.calls(), [['probe', 'submit', 'status']]); self.assertFalse(f.owned())
        self.assertEqual(json.loads(f.journals()[0].read_text())['state'], 'COMPLETED')
    def test_every_operation_runs_actual_provider_and_parser(self):
        for operation in ('audit', 'smoke', 'assets', 'localization'):
            with self.subTest(operation=operation):
                f = self.make(operation); self.assertEqual(f.verify()['acceptance']['AC-01'], 'PASS')
    def test_never_reuse_live_observation(self):
        f = self.make(); f.verify()
        with f.h.lock(): result = f.h.verification('slice', reuse=True)
        self.assertEqual(result['executed_checks'], ['CHECK-01']); self.assertFalse(result['reused_checks'])
        self.assertEqual(len(f.calls()), 2)
    def test_explicit_fresh_verification_from_ready(self):
        f = self.make(); f.verify(); result = f.verify()
        self.assertEqual(result['phase'], 'READY_FOR_HUMAN_REVIEW'); self.assertEqual(len(f.calls()), 2)
    def test_disabled_config_never_starts_provider(self):
        f = self.make(change=lambda c: c.update(enabled=False)); self.assert_incomplete(f, False)
        self.assertFalse(f.calls()); self.assertFalse(f.journals())
    def test_invalid_spec_never_starts_provider(self):
        f = self.make(change=lambda c: c['spec'].update(max_items=0)); self.assert_incomplete(f, False)
        self.assertFalse(f.calls()); self.assertFalse(f.journals())
    def test_missing_capability_never_submits(self):
        f = self.make(mode='missing-capability'); self.assert_incomplete(f, False)
        self.assertEqual(f.calls(), [['probe']])
    def test_probe_not_ready_never_submits(self):
        f = self.make(mode='probe-unavailable'); self.assert_incomplete(f, False)
        self.assertEqual(f.calls(), [['probe']])
    def test_identity_changes_rejected_and_ownership_retained(self):
        for mode in ('wrong-job', 'wrong-session', 'wrong-project', 'wrong-run', 'wrong-request', 'wrong-capabilities'):
            with self.subTest(mode=mode): self.assert_incomplete(self.make(mode=mode))
    def test_lost_submit_retains_ownership_and_blocks_resubmit(self):
        f = self.make(mode='lost-submit'); self.assert_incomplete(f)
        with f.h.lock(): f.h.recovery('SYNTHETIC inspect lost response; test no automatic resubmission')
        self.assert_incomplete(f)
        self.assertEqual(f.calls(), [['probe', 'submit']])
    def test_uncertain_terminal_states_retain_ownership(self):
        for mode in ('busy', 'unavailable', 'interrupted'):
            with self.subTest(mode=mode): self.assert_incomplete(self.make(mode=mode))
    def test_confirmed_stopped_states_release_ownership_without_pass(self):
        for mode in ('failed', 'cancelled'):
            with self.subTest(mode=mode): self.assert_incomplete(self.make(mode=mode), False)
    def test_poll_budget_stops_without_claiming_cancellation(self):
        f = self.make(mode='running'); self.assert_incomplete(f)
        self.assertEqual(f.calls(), [['probe', 'submit', 'status', 'status']])
        journal = json.loads(f.journals()[0].read_text())
        self.assertFalse(journal['cancellation_requested']); self.assertTrue(journal['server_may_be_running'])
    def test_timeout_is_not_server_cancellation(self):
        f = self.make(mode='timeout'); self.assert_incomplete(f)
        self.assertFalse(json.loads(f.journals()[0].read_text())['cancellation_requested'])
    def test_bad_process_output_is_not_evidence(self):
        for mode in ('nonzero', 'oversized', 'malformed'):
            with self.subTest(mode=mode): self.assert_incomplete(self.make(mode=mode))
    def test_partial_search_fails_coverage_expectation(self):
        f = self.make(mode='partial'); result = f.verify()
        self.assertEqual(result['acceptance']['AC-01'], 'FAIL'); self.assertFalse(f.owned())
    def test_frozen_smoke_fails_despite_capture(self):
        f = self.make('smoke', 'frozen'); self.assertEqual(f.verify()['acceptance']['AC-01'], 'FAIL')
    def test_persistence_and_localization_failures_propagate(self):
        for op, mode in (('assets', 'unsaved'), ('localization', 'missing-locale'), ('audit', 'new-finding')):
            with self.subTest(operation=op): self.assertEqual(self.make(op, mode).verify()['acceptance']['AC-01'], 'FAIL')
    def test_source_mutation_during_observation_invalidates_run(self):
        f = self.make(mode='mutate'); result = f.verify()
        self.assertEqual(result['acceptance']['AC-01'], 'NOT_RUN')
        self.assertTrue(any('Invalid receipt' in b for b in result['blockers']))
    def test_changed_provider_executable_input_blocks_before_submit(self):
        f = self.make(); (f.root / 'Tests/unity_provider_fixture.py').write_text('changed')
        with self.assertRaises(bh.BHError): f.verify()
        self.assertFalse(f.calls())
    def test_missing_coverage_expectation_blocks_before_submit(self):
        f = JobFixture(); self.addCleanup(f.close)
        b = bh.load_json(f.root / '.bh/bindings.json'); b['checks'][0]['expectations'] = [expectation('match_count', 1)]
        write(f.root, '.bh/bindings.json', b); f.h = bh.Harness(f.root); f.ready()
        self.assert_incomplete(f, False); self.assertFalse(f.calls())
    def test_unknown_reuse_policy_rejected(self):
        f = JobFixture(); self.addCleanup(f.close)
        b = bh.load_json(f.root / '.bh/bindings.json'); b['checks'][0]['reuse_policy'] = 'always'
        write(f.root, '.bh/bindings.json', b)
        with self.assertRaises(bh.BHError): bh.Harness(f.root)

class UnityReducerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.out = self.root / '.bh/runs/SYNTHETIC/CHECK'; self.out.mkdir(parents=True)
    def search(self):
        s, _ = case('search')
        v = {'query': s['query'], 'provider': s['provider'], 'scope_paths': s['scope_paths'], 'complete': True,
             'total_count': 1, 'items': [{'id': 'one', 'kind': 'fixture', 'path': 'Source/value.json', 'properties': {'value': 1}}]}
        return s, v
    def reduce(self, op, s, v): return evidence.reduce_result(op, s, v, self.root, self.out)
    def test_search_counts_and_scoped_properties(self):
        s, v = self.search(); obs, _ = self.reduce('search', s, v)
        self.assertEqual(obs, {'coverage_complete': True, 'match_count': 1, 'returned_count': 1})
    def test_incomplete_search_is_never_labeled_complete(self):
        s, v = self.search(); v.update(complete=False, total_count=2)
        self.assertFalse(self.reduce('search', s, v)[0]['coverage_complete'])
    def test_outside_scope_duplicate_and_missing_properties_rejected(self):
        s, original = self.search()
        for alter in (lambda v: v['items'][0].update(path='Outside/value'),
                      lambda v: v['items'].append(copy.deepcopy(v['items'][0])),
                      lambda v: v['items'][0].update(properties={}),
                      lambda v: v.update(total_count=0)):
            v = copy.deepcopy(original); alter(v)
            with self.assertRaises(bh.BHError): self.reduce('search', s, v)
    def test_unknown_fields_nonfinite_and_oversize_rejected(self):
        s, v = self.search(); v['extra'] = 1
        with self.assertRaises(bh.BHError): self.reduce('search', s, v)
        s, v = self.search(); v['items'][0]['properties']['value'] = float('nan')
        with self.assertRaises(bh.BHError): self.reduce('search', s, v)
        s, v = self.search(); v['items'][0]['properties']['value'] = 'x' * 3000
        with self.assertRaises(bh.BHError): self.reduce('search', s, v)
    def test_no_result_is_not_universal_absence(self):
        s, v = self.search(); v.update(total_count=0, items=[])
        obs, summary = self.reduce('search', s, v)
        self.assertTrue(obs['coverage_complete']); self.assertIn('declared search', summary['limitation'])
    def test_capture_digest_and_source_and_paths(self):
        s, _ = case('smoke'); data = b'SYNTHETIC'; (self.out / 'capture.bin').write_bytes(data)
        v = {'frame_before': 1, 'frame_after': 2, 'conditions': {'behavior': True}, 'error_count': 0,
             'capture': {'path': 'capture.bin', 'source': 'screen', 'sha256': hashlib.sha256(data).hexdigest()}}
        self.assertTrue(self.reduce('smoke', s, v)[0]['frames_advanced'])
        for field, value in (('path', '../capture.bin'), ('source', 'camera'), ('sha256', '0' * 64)):
            bad = copy.deepcopy(v); bad['capture'][field] = value
            with self.assertRaises(bh.BHError): self.reduce('smoke', s, bad)
    def test_frozen_and_failed_conditions_are_observed_not_invented(self):
        s, _ = case('smoke'); s['capture_source'] = 'none'
        v = {'frame_before': 1, 'frame_after': 1, 'conditions': {'behavior': False}, 'error_count': 2, 'capture': None}
        obs, _ = self.reduce('smoke', s, v)
        self.assertFalse(obs['frames_advanced']); self.assertFalse(obs['conditions_met']); self.assertEqual(obs['error_count'], 2)
    def test_empty_rosters_rejected_before_execution(self):
        for op, s in [('assets', {'assets': []}), ('localization', {'keys': [], 'locales': ['en'], 'code_sites': []}),
                      ('smoke', {'condition_ids': [], 'capture_source': 'none', 'minimum_frame_advance': 1})]:
            with self.subTest(operation=op), self.assertRaises(bh.BHError): evidence.validate_spec(op, s, self.root)
    def test_missing_asset_or_unsaved_binding_is_failure(self):
        s, _ = case('assets')
        obs, _ = self.reduce('assets', s, {'assets': []}); self.assertEqual(obs['asset_failures'], 1)
        a = s['assets'][0]; observed = {'path': a['path'], 'persisted': True, 'reloaded': True,
           'subassets': ['Material'], 'bindings': {'label': {**a['bindings']['label'], 'observed': False}},
           'behaviors': {'updates': True}, 'duplicate_count': 0}
        self.assertEqual(self.reduce('assets', s, {'assets': [observed]})[0]['asset_failures'], 1)
    def test_missing_locale_empty_translation_and_code_site(self):
        s, _ = case('localization'); v = {'entries': [{'key': 'label', 'locale': 'en', 'value': ' '}], 'converted_code_sites': []}
        obs, _ = self.reduce('localization', s, v)
        self.assertEqual(obs['missing_or_empty_entries'], 2); self.assertEqual(obs['unconverted_code_sites'], 1)
    def test_unknown_locale_duplicate_pair_and_unknown_code_site_rejected(self):
        s, _ = case('localization')
        for v in ({'entries': [{'key': 'label', 'locale': 'xx', 'value': 'text'}], 'converted_code_sites': []},
                  {'entries': [{'key': 'label', 'locale': 'en', 'value': 'text'}] * 2, 'converted_code_sites': []},
                  {'entries': [], 'converted_code_sites': ['unknown']}):
            with self.assertRaises(bh.BHError): self.reduce('localization', s, v)
    def test_csv_quoted_fields_and_header_validation(self):
        p = self.out / 'audit.csv'
        with p.open('w', newline='') as stream:
            w = csv.writer(stream); w.writerow(evidence.CSV_COLUMNS)
            w.writerow(['Code', 'Warning', '', 'comma, newline\ntext', 'Source/a.cs', '1', 'RULE', 'Review'])
        self.assertEqual(len(evidence.read_auditor_csv(p)), 1)
        p.write_text('Category,Category\nCode,Code\n')
        with self.assertRaises(bh.BHError): evidence.read_auditor_csv(p)
    def test_run_file_rejects_symlink(self):
        actual = self.root / 'outside'; actual.write_text('data'); (self.out / 'link').symlink_to(actual)
        with self.assertRaises(bh.BHError): evidence.run_file(self.root, self.out, 'link')
    def test_reducers_never_mark_human_accepted(self):
        s, v = self.search(); obs, summary = self.reduce('search', s, v)
        self.assertNotIn('acceptance', obs); self.assertNotIn('human_acceptance', summary)
    def test_mandatory_expectations_and_type_checks(self):
        for op in evidence.REDUCERS:
            with self.subTest(op=op), self.assertRaises(bh.BHError): evidence.validate_expectations(op, {'expectations': []})
        with self.assertRaises(bh.BHError): evidence.boolean(1, 'flag')
        with self.assertRaises(bh.BHError): evidence.integer(True, 'count')

if __name__ == '__main__': unittest.main()
