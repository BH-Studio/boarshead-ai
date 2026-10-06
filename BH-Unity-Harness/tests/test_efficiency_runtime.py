"""Efficiency changes exercise real runtime paths; no credits or live Unity measured."""
import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from support import Fixture, bh, write

DIAG = 'Observed counter mismatch; test one bounded correction in Source/value.json'

class EfficiencyRuntimeTests(unittest.TestCase):
    def make(self, **kw):
        f=Fixture(**kw); self.addCleanup(f.close); return f

    def fast_fixture(self, **kw):
        f=self.make(**kw)
        f.handoff['checks'][0]['profile']='fast'
        f.refresh_handoff();f.ready()
        return f

    def test_unchanged_fast_reused_but_final_gate_still_missing(self):
        f=self.fast_fixture()
        with f.h.lock(): f.h.verification('fast')
        old=f.h.state()['runs'][-1]
        with patch.object(f.h, 'run_check', wraps=f.h.run_check) as check, f.h.lock():
            out=f.h.verification('slice', reuse=True)
        self.assertEqual(check.call_count,0)
        self.assertEqual(out['reused_checks'][0]['receipt'],old)
        self.assertTrue(out['blockers'])
        self.assertEqual(f.h.state()['phase'],'EXECUTING')
        self.assertEqual(len(f.h.state()['runs']),1)
        with f.h.lock(): out=f.h.verification('slice')
        self.assertEqual(out['phase'],'READY_FOR_HUMAN_REVIEW')

    def test_relevant_change_is_executed_not_reused(self):
        f=self.fast_fixture(narrow=True)
        with f.h.lock(): f.h.verification('fast')
        write(f.root,'Source/value.json',{'value':2})
        with patch.object(f.h,'run_check',wraps=f.h.run_check) as check, f.h.lock():
            out=f.h.verification('slice',reuse=True)
        self.assertEqual(check.call_count,1)
        self.assertFalse(out['reused_checks'])
        self.assertEqual(out['acceptance']['AC-01'],'FAIL')

    def test_reviewed_unrelated_change_reuses(self):
        f=self.fast_fixture(narrow=True)
        with f.h.lock(): f.h.verification('fast')
        write(f.root,'Source/unrelated.txt','unrelated edit')
        with patch.object(f.h,'run_check',wraps=f.h.run_check) as check, f.h.lock():
            out=f.h.verification('slice',reuse=True)
        self.assertEqual(check.call_count,0)
        self.assertEqual(out['acceptance']['AC-01'],'PASS')

    def test_default_whole_dependency_fallback_stays_conservative(self):
        f=self.fast_fixture()
        with f.h.lock(): f.h.verification('fast')
        write(f.root,'Source/unrelated.txt','new unrelated bytes')
        with patch.object(f.h,'run_check',wraps=f.h.run_check) as check, f.h.lock():
            f.h.verification('slice',reuse=True)
        self.assertEqual(check.call_count,1)

    def test_invalid_selection_fails_before_writes(self):
        f=self.make();f.ready();before=f.h.state()
        for ids in ([],['unknown'],['CHECK-01','CHECK-01'],['../escape']):
            with self.subTest(ids=ids), f.h.lock(), self.assertRaises(bh.BHError):
                f.h.verification('slice',check_ids=ids)
        self.assertEqual(before,f.h.state())

    def test_selected_profile_cannot_claim_fresh_full_gate(self):
        f=self.make();f.ready()
        with f.h.lock(): out=f.h.verification('slice',check_ids=['CHECK-01'])
        self.assertEqual(out['acceptance']['AC-01'],'PASS')
        self.assertEqual(out['phase'],'EXECUTING')
        self.assertTrue(out['blockers'])

    def test_missing_current_artifact_blocks_reuse(self):
        f=self.fast_fixture()
        with f.h.lock(): f.h.verification('fast')
        r=bh.load_json(f.root/f.h.state()['runs'][-1])
        (f.root/r['results'][0]['artifacts'][0]['path']).unlink()
        with f.h.lock(), self.assertRaises(bh.BHError): f.h.verification('slice',reuse=True)

    def test_unchanged_final_reuse_is_noop_and_keeps_original_time(self):
        f=self.make();f.ready();f.verify();old=f.h.state()
        with f.h.lock():out=f.h.verification('slice',reuse=True)
        self.assertEqual(old,f.h.state())
        self.assertFalse(out['fresh_final_gate'])
        self.assertEqual(out['reused_checks'][0]['receipt'],old['runs'][-1])
        self.assertFalse(out['blockers'])

    def two_checks(self):
        f=self.make(mode='facts')
        c=copy.deepcopy(f.handoff['checks'][0]);c['id']='CHECK-02'
        f.handoff['checks'].insert(1,c)
        b=bh.load_json(f.root/'.bh/bindings.json')
        second=copy.deepcopy(b['checks'][0]);second['check_id']='CHECK-02'
        b['checks'].append(second);write(f.root,'.bh/bindings.json',b)
        f.refresh_handoff();f.h=bh.Harness(f.root);f.ready();return f

    def test_fail_fast_leaves_following_checks_unrun(self):
        f=self.two_checks();write(f.root,'Source/value.json',{'value':2})
        with f.h.lock():out=f.h.verification('slice',fail_fast=True)
        r=bh.load_json(f.root/f.h.state()['runs'][-1])
        self.assertEqual([x['id'] for x in r['results']],['CHECK-01'])
        self.assertNotEqual(out['phase'],'READY_FOR_HUMAN_REVIEW')

    def test_selected_second_does_not_hide_first_failure(self):
        f=self.two_checks();write(f.root,'Source/value.json',{'value':2})
        with f.h.lock():f.h.verification('slice',fail_fast=True);f.h.repair(DIAG)
        with f.h.lock():out=f.h.verification('slice',check_ids=['CHECK-02'])
        self.assertEqual(out['acceptance']['AC-01'],'FAIL')
        self.assertNotEqual(out['phase'],'READY_FOR_HUMAN_REVIEW')

    def test_two_ordinary_repairs_do_not_consume_exception_budget(self):
        f=self.make();f.ready();write(f.root,'Source/value.json',{'value':2})
        for i in range(2):
            f.verify()
            with f.h.lock():out=f.h.repair(DIAG)
            self.assertEqual(out['recovery_cycles'],0)
            self.assertEqual(out['counters']['failed_rounds'],i+1)
        write(f.root,'Source/value.json',{'value':1});f.verify()
        self.assertEqual(f.h.state()['phase'],'READY_FOR_HUMAN_REVIEW')

    def test_threshold_pause_cannot_use_ordinary_repair(self):
        f=self.make();f.ready();write(f.root,'Source/value.json',{'value':2})
        for i in range(3):
            f.verify()
            if i<2:
                with f.h.lock():f.h.repair(DIAG)
        self.assertEqual(f.h.state()['phase'],'PAUSED')
        with f.h.lock(),self.assertRaises(bh.BHError):f.h.repair(DIAG)
        with f.h.lock():f.h.recovery(DIAG)
        self.assertEqual(f.h.state()['counters']['recovery_cycles'],1)
        write(f.root,'Source/value.json',{'value':1});f.verify()
        self.assertEqual(f.h.state()['phase'],'READY_FOR_HUMAN_REVIEW')

    def test_user_pause_not_bypassed_by_repair(self):
        f=self.make();f.ready();s=f.h.state()
        with f.h.lock():f.h.move(s,'PAUSED','user stopped');f.h.save(s,s['revision'])
        with f.h.lock(),self.assertRaises(bh.BHError):f.h.repair(DIAG)

    def test_repair_cannot_expand_approved_scope(self):
        f=self.make();f.ready();write(f.root,'Source/value.json',{'value':2});f.verify()
        write(f.root,'Outside/evil.txt','not allowed')
        with f.h.lock(),self.assertRaises(bh.BHError):f.h.repair(DIAG)

    def test_status_parses_only_latest_supporting_result_history_can_deep_audit(self):
        f=self.fast_fixture()
        for _ in range(8):
            with f.h.lock():f.h.verification('fast')
        with patch.object(bh,'parse_nunit',wraps=bh.parse_nunit) as parse:
            f.h.audit_results(f.h.state())
        self.assertEqual(parse.call_count,1)
        with patch.object(bh,'parse_nunit',wraps=bh.parse_nunit) as parse:
            f.h.audit_results(f.h.state(),full_history=True)
        self.assertEqual(parse.call_count,8)

    def test_corrupt_latest_never_falls_back_silently(self):
        f=self.fast_fixture()
        for _ in range(2):
            with f.h.lock():f.h.verification('fast')
        path=f.root/f.h.state()['runs'][-1]
        r=bh.load_json(path);r['results'][0]['exit_code']=8
        write(f.root,path.relative_to(f.root),r)
        self.assertTrue(f.h.audit_results(f.h.state())[2])
        with f.h.lock(),self.assertRaises(bh.BHError):f.h.verification('slice',reuse=True)

    def test_old_corruption_only_deep_history_but_stays_accessible(self):
        f=self.fast_fixture()
        for _ in range(2):
            with f.h.lock():f.h.verification('fast')
        r=bh.load_json(f.root/f.h.state()['runs'][0])
        (f.root/r['results'][0]['artifacts'][0]['path']).unlink()
        # Add full final run so there is no missing-profile gap.
        with f.h.lock():f.h.verification('slice')
        self.assertFalse(f.h.audit_results(f.h.state())[2])
        self.assertTrue(f.h.audit_results(f.h.state(),full_history=True)[2])

    def test_one_automated_plus_manual_uses_two_snapshots(self):
        f=self.make();f.ready()
        with patch.object(bh,'snapshot',wraps=bh.snapshot) as snap:
            f.verify()
        self.assertEqual(snap.call_count,2)

    def test_dense_directory_enumerated_once_per_snapshot(self):
        f=self.make()
        for i in range(500):write(f.root,f'Source/dense/{i:04}.txt','synthetic')
        old=Path.iterdir;counts={}
        def visit(path):
            counts[path]=counts.get(path,0)+1
            return old(path)
        with patch.object(Path,'iterdir',visit):bh.snapshot(f.root)
        self.assertEqual(counts[f.root/'Source/dense'],1)

    def test_case_index_not_retained_across_snapshots(self):
        f=self.make();bh.snapshot(f.root)
        write(f.root,'Source/Case.txt','1');write(f.root,'Source/case.txt','2')
        with self.assertRaises(bh.BHError):bh.snapshot(f.root)

    def test_real_cli_selection_and_history(self):
        f=self.make();f.ready()
        args=[sys.executable,str(f.root/'Tools/BH/bh.py'),'--root',str(f.root)]
        proc=subprocess.run(args+['verify','--profile','slice','--check','CHECK-01'],capture_output=True,text=True)
        self.assertEqual(json.loads(proc.stdout)['executed_checks'],['CHECK-01'])
        proc=subprocess.run(args+['status','--history'],capture_output=True,text=True)
        self.assertTrue(json.loads(proc.stdout)['gaps'])

if __name__=='__main__':unittest.main()
