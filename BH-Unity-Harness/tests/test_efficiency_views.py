"""Actual compact-view checks, not measured Codex consumption."""
import contextlib
import importlib.util
import io
import json
import sys
import unittest
from unittest.mock import patch
from support import Fixture, PACKAGE, bh, write

spec = importlib.util.spec_from_file_location('views', PACKAGE/'project-template/Tools/BH/views.py')
views = importlib.util.module_from_spec(spec)
with patch.dict(sys.modules, {'bh': bh}):
    spec.loader.exec_module(views)

class EfficiencyViewTests(unittest.TestCase):
    def setUp(self):
        self.f = Fixture(narrow=True)
        self.addCleanup(self.f.close)
        self.h = self.f.ready()

    def test_all_decision_fields_present_without_source_roster(self):
        view = views.context_view(self.h)
        plan = bh.load_json(self.h.artifact(self.h.state()['plan']))
        self.assertEqual(view['plan']['proposal'], plan['proposal'])
        self.assertEqual(view['plan_approval_subject'], bh.digest(plan))
        self.assertEqual(view['handoff']['checks'], self.f.handoff['checks'])
        self.assertEqual(view['overlay'], self.f.overlay)
        self.assertEqual({x['id'] for x in view['acceptance']}, {'AC-01','AC-HUMAN'})
        self.assertNotIn('files', view['plan']['baseline'])
        self.assertNotIn('files', view['current_source'])

    def test_context_does_not_write_workspace(self):
        before = bh.snapshot(self.f.root)
        state = self.h.state()
        views.context_view(self.h)
        self.assertEqual(state, self.h.state())
        self.assertEqual(before['files'], bh.snapshot(self.f.root)['files'])

    def test_context_size_not_proportional_to_irrelevant_source_roster(self):
        small = len(json.dumps(views.context_view(self.h)))
        for i in range(1000):
            write(self.f.root, f'Source/irrelevant/{i:04}.txt', 'synthetic')
        large = len(json.dumps(views.context_view(self.h)))
        self.assertLess(large-small, 200)

    def test_tampered_plan_is_not_projected_as_valid(self):
        s = self.h.state()
        path = self.f.root/s['plan']['path']
        path.write_bytes(path.read_bytes()+b' ')
        with self.assertRaises(bh.BHError):
            views.context_view(self.h)

    def test_changed_handoff_is_blocked(self):
        write(self.f.root, 'Handoff/DESIGN.md', 'tampered')
        with self.assertRaises(bh.BHError):
            views.context_view(self.h)

    def test_unrelated_edit_keeps_evidence_and_relevant_edit_invalidates(self):
        self.f.verify()
        write(self.f.root, 'Source/unrelated.txt', 'changed')
        v = views.context_view(self.h)
        self.assertEqual(v['acceptance'][0]['current_status'], 'PASS')
        write(self.f.root, 'Source/value.json', {'value': 2})
        self.assertEqual(views.context_view(self.h)['acceptance'][0]['current_status'], 'NOT_RUN')

    def test_missing_raw_artifact_visible(self):
        self.f.verify()
        receipt = bh.load_json(self.f.root/self.h.state()['runs'][-1])
        (self.f.root/receipt['results'][0]['artifacts'][0]['path']).unlink()
        self.assertTrue(views.context_view(self.h)['current_evidence_gaps'])

    def test_schema_transitive_closure_and_unknown_rejection(self):
        out = views.schema_view(self.h.schema, 'plan')
        self.assertIn('snapshot', out['$defs'])
        self.assertIn('proposal', out['$defs'])
        self.assertNotIn('return', out['$defs'])
        plan = self.h.load_plan(self.h.state())
        bh.validate(plan, 'plan', out)
        with self.assertRaises(bh.BHError):
            views.schema_view(self.h.schema, 'absent')

    def test_generated_draft_has_no_approval_and_blocks_execution_plan(self):
        value = views.draft_proposal(self.h, 'Handoff/handoff.json')
        self.assertTrue(value['scope_conflicts'])
        self.assertNotIn('approval', value)
        write(self.f.root, '.bh/tasks/task-01/draft.json', value)
        with self.h.lock(), self.assertRaises(bh.BHError):
            self.h.make_plan('.bh/tasks/task-01/draft.json')

    def test_return_keeps_full_evidence_and_every_criterion(self):
        self.f.verify()
        with self.h.lock():
            out = views.return_view(self.h)
        self.assertEqual(out['human_acceptance'], 'PENDING')
        full = bh.load_json(self.h.artifact(out['full_return']))
        self.assertIn('files', full['source_snapshot'])
        self.assertNotIn('files', out['source_snapshot'])
        self.assertEqual(full['acceptance'], out['acceptance'])
        self.assertTrue(self.h.artifact(out['history_index']).exists())

    def test_context_cli_emits_valid_json(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = views.main(['--root', str(self.f.root), 'context'])
        self.assertEqual(code, 2)  # Required final evidence has not yet run.
        self.assertEqual(json.loads(output.getvalue())['format'], 'BH-CONTEXT-VIEW-1')

if __name__ == '__main__':
    unittest.main()
