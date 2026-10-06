"""Actual-runtime, offline tests. All projects/approvals/observations are SYNTHETIC."""
import copy, json, os, subprocess, sys, unittest
from pathlib import Path
from support import Fixture, bh, write, approval, git, PACKAGE

class RuntimeTests(unittest.TestCase):
 def setUp(self):self.f=Fixture();self.addCleanup(self.f.close);self.h=self.f.h;self.r=self.f.root
 def ready(self):return self.f.ready()
 def check_bad_handoff(self,mutator):
  mutator(self.f.handoff);self.f.refresh_handoff()
  with self.assertRaises(bh.BHError):self.h.handoff('Handoff/handoff.json')
 def test_roundtrip_human_pending(self):
  self.ready();self.f.verify();scores,_,gaps=self.h.audit_results(self.h.state());self.assertEqual(scores,{'AC-01':'PASS','AC-HUMAN':'HUMAN_PENDING'});self.assertFalse(gaps)
  with self.h.lock():self.h.return_report()
  ret=bh.load_json(self.r/'.bh/exports/task-01/RETURN.json');self.assertEqual(ret['human_acceptance'],'PENDING');self.assertTrue(ret['synthetic'])
 def test_structural_approval_not_authentication(self):
  self.ready();self.f.verify();out=self.f.accept();self.assertEqual(out['phase'],'ACCEPTED');self.assertIn('not authentication',out['authentication'])
 def test_missing_human_acceptance(self):
  self.ready();self.f.verify();s=self.h.state();snap=bh.snapshot(self.r)
  a=approval(self.f.pid,self.f.task,'acceptance',bh.digest({'snapshot':snap['sha256'],'plan':s['plan']['sha256'],'handoff':s['handoff']['sha256']}));write(self.r,'.bh/tasks/task-01/nohuman.json',a)
  with self.assertRaises(bh.BHError),self.h.lock():self.h.accept('.bh/tasks/task-01/nohuman.json')
 def test_no_self_certification(self):
  a=approval(self.f.pid,self.f.task,'plan','0'*64);a['actor']='executor'
  with self.assertRaises(bh.BHError):self.h.approval(a,'plan','0'*64,self.f.task)
 def test_missing_design_approval(self):
  self.f.refresh_handoff(False)
  with self.assertRaises(bh.BHError):self.h.handoff('Handoff/handoff.json')
 def test_draft_is_not_execution(self):
  self.f.handoff['status']='DRAFT';self.f.refresh_handoff(False);self.h.handoff('Handoff/handoff.json',False)
  with self.assertRaises(bh.BHError):self.h.initialize('Handoff/handoff.json')
 def test_wrong_version(self):self.check_bad_handoff(lambda h:h.update(version='2.0.0'))
 def test_wrong_harness_version(self):self.check_bad_handoff(lambda h:h.update(harness_version='9.0.0'))
 def test_wrong_design_method(self):self.check_bad_handoff(lambda h:h.update(design_method_version='3.0.0'))
 def test_dropped_acceptance(self):self.check_bad_handoff(lambda h:h.update(acceptance_ids=['AC-01']))
 def test_dropped_invariant(self):self.check_bad_handoff(lambda h:h.update(invariant_ids=[]))
 def test_manifest_mismatch(self):
  write(self.r,'Handoff/DESIGN.md','changed')
  with self.assertRaises(bh.BHError):self.h.handoff('Handoff/handoff.json')
 def test_missing_artifact(self):
  (self.r/'Handoff/DESIGN.md').unlink()
  with self.assertRaises(bh.BHError):self.h.handoff('Handoff/handoff.json')
 def test_missing_reference(self):self.check_bad_handoff(lambda h:h.update(architecture_refs=['Handoff/missing.md']))
 def test_duplicate_check_id(self):self.check_bad_handoff(lambda h:h['checks'].append(copy.deepcopy(h['checks'][0])))
 def test_dropped_check(self):self.check_bad_handoff(lambda h:h.update(checks=[h['checks'][1]]))
 def test_required_na_rejected(self):self.check_bad_handoff(lambda h:h['checks'][0].update(not_applicable_reason='skip'))
 def test_required_above_profile(self):self.check_bad_handoff(lambda h:h['checks'][0].update(profile='milestone'))
 def test_human_automation_rejected(self):self.check_bad_handoff(lambda h:h['checks'][0].update(ac_ids=['AC-HUMAN']))
 def test_manual_not_automated(self):self.check_bad_handoff(lambda h:h['checks'][1].update(ac_ids=['AC-01']))
 def test_nunit_requires_names(self):self.check_bad_handoff(lambda h:h['checks'][0].update(test_names=[]))
 def test_nunit_requires_positive_count(self):self.check_bad_handoff(lambda h:h['checks'][0].update(minimum_tests=0))
 def test_blocking_question(self):self.check_bad_handoff(lambda h:h['questions'].append({'id':'Q1','class':'BLOCKING','question':'What is approved?','owner':'human','revisit':'before design approval'}))
 def test_open_overlay_decision(self):
  o=self.f.overlay;o['open_decisions']=['Unresolved pipeline'];write(self.r,'Handoff/overlay.json',o);self.f.refresh_handoff()
  with self.assertRaises(bh.BHError):self.h.handoff('Handoff/handoff.json')
 def test_unreconciled_overlay(self):
  o=self.f.overlay;o['status']='SOURCE_DERIVED_UNRECONCILED';write(self.r,'Handoff/overlay.json',o);self.f.refresh_handoff()
  with self.assertRaises(bh.BHError):self.h.handoff('Handoff/handoff.json')
 def test_approval_subject(self):
  self.f.handoff['approval']['subject_sha256']='0'*64;write(self.r,'Handoff/handoff.json',self.f.handoff)
  with self.assertRaises(bh.BHError):self.h.handoff('Handoff/handoff.json')
 def test_synthetic_boundary(self):self.check_bad_handoff(lambda h:h.update(synthetic=False))
 def test_preflight_no_writes(self):
  before={p.relative_to(self.r):bh.file_hash(p) for p in self.r.rglob('*') if p.is_file()};out=self.h.preflight();after={p.relative_to(self.r):bh.file_hash(p) for p in self.r.rglob('*') if p.is_file()};self.assertEqual(before,after);self.assertEqual(out['status'],'PREFLIGHT_ONLY')
 def test_duplicate_json_keys(self):
  p=write(self.r,'duplicate.json','{"a":1,"a":2}')
  with self.assertRaises(bh.BHError):bh.load_json(p)
 def test_nonfinite_json(self):
  p=write(self.r,'nonfinite.json','{"a":NaN}')
  with self.assertRaises(bh.BHError):bh.load_json(p)
 def test_missing_configuration(self):
  (self.r/'.bh/project.json').unlink()
  with self.assertRaises((bh.BHError,OSError)):bh.Harness(self.r)
 def test_unknown_configuration_field(self):
  v=bh.load_json(self.r/'.bh/project.json');v['ignore_failures']=True;write(self.r,'.bh/project.json',v)
  with self.assertRaises(bh.BHError):bh.Harness(self.r)
 def test_illegal_transition(self):
  with self.h.lock():self.h.initialize('Handoff/handoff.json')
  with self.assertRaises(bh.BHError):self.h.move(self.h.state(),'ACCEPTED','skip approval')
 def test_lock_serializes_writers(self):
  with self.h.lock():
   with self.assertRaises(bh.BHError),self.h.lock():pass
 def test_concurrent_state_revision(self):
  with self.h.lock():self.h.initialize('Handoff/handoff.json')
  s=self.h.state()
  with self.h.lock():self.h.save(s,s['revision'])
  with self.assertRaises(bh.BHError),self.h.lock():self.h.save(s,0)
 def test_repeated_init_unchanged(self):
  with self.h.lock():self.h.initialize('Handoff/handoff.json');self.assertEqual(self.h.initialize('Handoff/handoff.json')['status'],'UNCHANGED')
 def test_resume_discovery(self):
  with self.h.lock():self.h.initialize('Handoff/handoff.json');self.assertEqual(self.h.resume()['phase'],'DISCOVERY')
 def test_begin_without_plan(self):
  with self.h.lock():self.h.initialize('Handoff/handoff.json')
  with self.assertRaises(bh.BHError),self.h.lock():self.h.begin()
 def test_begin_without_approval(self):
  with self.h.lock():self.h.initialize('Handoff/handoff.json');self.h.make_plan('.bh/tasks/task-01/proposal.json')
  with self.assertRaises(bh.BHError),self.h.lock():self.h.begin()
 def test_dirty_after_plan_before_approval(self):
  with self.h.lock():self.h.initialize('Handoff/handoff.json');self.h.make_plan('.bh/tasks/task-01/proposal.json')
  s=self.h.state();a=approval(self.f.pid,self.f.task,'plan',bh.digest(bh.load_json(self.h.artifact(s['plan']))));write(self.r,'.bh/tasks/task-01/approval.json',a);write(self.r,'Source/value.json',{'value':2})
  with self.assertRaises(bh.BHError),self.h.lock():self.h.approve('.bh/tasks/task-01/approval.json')
 def test_protected_mutation_blocks(self):
  self.ready();write(self.r,'Tests/fixture_driver.py','changed')
  with self.assertRaises(bh.BHError),self.h.lock():self.h.verification('slice')
 def test_out_of_scope_mutation_blocks(self):
  self.ready();write(self.r,'Other/new.txt','changed')
  with self.assertRaises(bh.BHError),self.h.lock():self.h.verification('slice')
 def test_stale_dirty_evidence(self):
  self.ready();self.f.verify();write(self.r,'Source/value.json',{'value':2})
  with self.h.lock():self.h.resume()
  self.assertEqual(self.h.state()['ac_status']['AC-01'],'NOT_RUN');self.assertEqual(self.h.state()['phase'],'EXECUTING')
 def test_stale_human_acceptance(self):
  self.ready();self.f.verify();self.f.accept();write(self.r,'Source/value.json',{'value':2})
  with self.h.lock():self.h.return_report()
  self.assertEqual(bh.load_json(self.r/'.bh/exports/task-01/RETURN.json')['human_acceptance'],'PENDING')
 def test_new_commit_invalidates(self):
  self.ready();self.f.verify();git(self.r,'commit','--allow-empty','-qm','Synthetic changed revision')
  scores,_,gaps=self.h.audit_results(self.h.state());self.assertNotEqual(scores['AC-01'],'PASS')
 def test_missing_receipt(self):
  self.ready();self.f.verify();(self.r/self.h.state()['runs'][0]).unlink();scores,_,gaps=self.h.audit_results(self.h.state());self.assertTrue(gaps);self.assertNotEqual(scores['AC-01'],'PASS')
 def test_wrong_project_receipt(self):
  self.ready();self.f.verify();p=self.h.state()['runs'][0];v=bh.load_json(self.r/p);v['project_id']='another';write(self.r,p,v);self.assertTrue(self.h.audit_results(self.h.state())[2])
 def test_missing_raw_artifact(self):
  self.ready();self.f.verify();v=bh.load_json(self.r/self.h.state()['runs'][0]);(self.r/v['results'][0]['artifacts'][0]['path']).unlink();self.assertTrue(self.h.audit_results(self.h.state())[2])
 def test_duplicate_receipt_check(self):
  self.ready();self.f.verify();p=self.h.state()['runs'][0];v=bh.load_json(self.r/p);v['results'].append(copy.deepcopy(v['results'][0]));write(self.r,p,v);self.assertTrue(self.h.audit_results(self.h.state())[2])
 def test_raw_output_reparsed_not_green_wrapper(self):
  self.ready();write(self.r,'Source/value.json',{'value':2});self.f.verify();p=self.h.state()['runs'][0];v=bh.load_json(self.r/p);v['results'][0]['status']='PASS';write(self.r,p,v);scores,_,gaps=self.h.audit_results(self.h.state());self.assertNotEqual(scores['AC-01'],'PASS');self.assertTrue(gaps)
 def test_interrupted_run_resume(self):
  self.ready();s=self.h.state()
  with self.h.lock():self.h.move(s,'VERIFYING','synthetic interruption');s['pending_run']='.bh/runs/run-interrupted';self.h.save(s,s['revision']);self.h.resume()
  self.assertEqual(self.h.state()['phase'],'PAUSED');self.assertTrue((self.r/'.bh/runs/run-interrupted/interrupted.json').is_file())
 def test_recovery_budget(self):
  self.ready();s=self.h.state()
  with self.h.lock():self.h.move(s,'PAUSED','synthetic pause');self.h.save(s,s['revision']);self.h.recovery('Inspect observed fixture output and retry one bounded action');s=self.h.state();self.h.move(s,'PAUSED','second pause');self.h.save(s,s['revision'])
  with self.assertRaises(bh.BHError),self.h.lock():self.h.recovery('Another attempt beyond the configured recovery budget')
 def test_unbound_required_check_blocks_plan(self):
  write(self.r,'.bh/bindings.json',{'version':'1.0.0','project_id':self.f.pid,'checks':[]});h=bh.Harness(self.r)
  with h.lock():h.initialize('Handoff/handoff.json');h.make_plan('.bh/tasks/task-01/proposal.json')
  self.assertEqual(h.state()['phase'],'BLOCKED')
 def test_duplicate_skills_block(self):
  write(self.r,'.agents/skills/duplicate/SKILL.md','---\nname: bh-unity-preflight\ndescription: synthetic duplicate\n---\n')
  with self.assertRaises(bh.BHError):self.h.preflight()
 def test_nested_instruction_conflict(self):
  write(self.r,'Source/AGENTS.md','Synthetic conflicting rule');self.assertEqual(self.h.preflight()['status'],'BLOCKED')
 def test_override_instruction_conflict(self):
  write(self.r,'AGENTS.override.md','Synthetic conflicting rule');self.assertEqual(self.h.preflight()['status'],'BLOCKED')
 def test_path_traversal(self):
  for name in ('../escape','/absolute','C:/escape','a\\b','CON','foo.','a/../b','a//b'):
   with self.subTest(name=name),self.assertRaises(bh.BHError):bh.portable(name)
 def test_symlink_escape(self):
  (self.r/'escape').symlink_to(self.r.parent,target_is_directory=True)
  with self.assertRaises(bh.BHError):bh.safe(self.r,'escape/file')
 def test_case_collision(self):
  write(self.r,'Source/Case.txt','1');write(self.r,'Source/case.txt','2')
  with self.assertRaises(bh.BHError):bh.snapshot(self.r)
 def test_lfs_pointer_blocks(self):
  write(self.r,'Source/pointer','version https://git-lfs.github.com/spec/v1\noid sha256:fake\n')
  with self.assertRaises(bh.BHError):bh.snapshot(self.r)
 def test_unknown_schema_keyword(self):
  with self.assertRaises(bh.BHError):bh.validate('test',{'type':'string','madeUp':True},self.h.schema)
 def test_archive_and_no_task_reuse(self):
  self.ready();self.f.verify();self.f.accept();s=self.h.state()
  with self.h.lock():self.h.archive(s['task_id'],bh.digest(s))
  self.assertFalse((self.r/'.bh/state.json').exists())
  with self.assertRaises(bh.BHError),self.h.lock():self.h.initialize('Handoff/handoff.json')
 def test_unlock_cannot_terminate_live_owner(self):
  with self.h.lock():
   token=bh.load_json(self.r/'.bh/locks/writer.json')['token']
   with self.assertRaises(bh.BHError):self.h.unlock(token,True)
 def test_real_cli_preflight(self):
  p=subprocess.run([sys.executable,str(self.r/'Tools/BH/bh.py'),'--root',str(self.r),'preflight'],capture_output=True,text=True);self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(json.loads(p.stdout)['status'],'PREFLIGHT_ONLY')
 def test_failed_then_pass_preserves_history(self):
  self.ready();write(self.r,'Source/value.json',{'value':2});self.f.verify()
  with self.h.lock():self.h.recovery('Observed incorrect value; change only the approved counter input')
  write(self.r,'Source/value.json',{'value':1});self.f.verify();self.assertEqual(len(self.h.state()['runs']),2);self.assertEqual(bh.load_json(self.r/self.h.state()['runs'][0])['results'][0]['status'],'FAIL');self.assertEqual(self.h.state()['ac_status']['AC-01'],'PASS')
 def test_named_suite_failure_not_leaf_pass(self):
  p=write(self.r,'suite.xml','<test-run result="Failed" total="1" passed="1" failed="0"><test-suite result="Failed"><test-case fullname="T" result="Passed"/></test-suite></test-run>')
  self.assertEqual(bh.parse_nunit(p,{'test_names':['T'],'minimum_tests':1})['status'],'FAIL')
 def test_root_count_mismatch(self):
  p=write(self.r,'counts.xml','<test-run result="Passed" total="2"><test-case fullname="T" result="Passed"/></test-run>')
  with self.assertRaises(bh.BHError):bh.parse_nunit(p,{'test_names':['T'],'minimum_tests':1})

class ProcessTests(unittest.TestCase):
 def run_mode(self,mode,value=1):
  f=Fixture(mode);self.addCleanup(f.close);f.ready()
  if value!=1:write(f.root,'Source/value.json',{'value':value})
  out=f.verify();receipt=bh.load_json(f.root/f.h.state()['runs'][-1]);return out,receipt['results'][0],f
 def test_zero_tests(self):self.assertNotEqual(self.run_mode('zero')[1]['status'],'PASS')
 def test_missing_artifact(self):self.assertEqual(self.run_mode('missing')[1]['status'],'ERROR')
 def test_timeout(self):self.assertEqual(self.run_mode('timeout')[1]['status'],'ERROR')
 def test_nonzero_exit(self):self.assertNotEqual(self.run_mode('nonzero')[1]['status'],'PASS')
 def test_compile_error(self):self.assertEqual(self.run_mode('compile')[1]['status'],'FAIL')
 def test_skipped_required(self):self.assertNotEqual(self.run_mode('skip')[1]['status'],'PASS')
 def test_wrong_test_name(self):self.assertNotEqual(self.run_mode('wrong-test')[1]['status'],'PASS')
 def test_xml_entities(self):self.assertEqual(self.run_mode('entity')[1]['status'],'ERROR')
 def test_audit_detects_mutation(self):self.assertEqual(self.run_mode('mutate')[1]['status'],'ERROR')
 def test_facts_match(self):self.assertEqual(self.run_mode('facts')[1]['status'],'PASS')
 def test_facts_disagree(self):self.assertEqual(self.run_mode('facts',2)[1]['status'],'FAIL')
 def test_wrong_run_identity(self):self.assertEqual(self.run_mode('wrong-run')[1]['status'],'ERROR')
 def test_diagnostics_clean(self):self.assertEqual(self.run_mode('diagnostics')[1]['status'],'PASS')
 def test_diagnostics_new(self):self.assertEqual(self.run_mode('diagnostics',2)[1]['status'],'FAIL')
 def test_build_failure(self):self.assertEqual(self.run_mode('build')[1]['status'],'FAIL')
 def test_two_materially_different_profiles(self):
  a=Fixture(pipeline='URP');b=Fixture(pipeline='HDRP');self.addCleanup(a.close);self.addCleanup(b.close);a.ready();b.ready();a.verify();b.verify();self.assertNotEqual(a.pid,b.pid);self.assertNotEqual(a.h.config['engine']['render_pipeline'],b.h.config['engine']['render_pipeline'])
 def test_reviewed_narrow_dependencies(self):
  f=Fixture(narrow=True);self.addCleanup(f.close);f.ready();f.verify();write(f.root,'Source/unrelated.txt','changed unrelated');self.assertEqual(f.h.audit_results(f.h.state())[0]['AC-01'],'PASS')

if __name__=='__main__':unittest.main()
