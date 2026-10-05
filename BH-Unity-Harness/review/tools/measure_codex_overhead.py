#!/usr/bin/env python3
"""Measure a pinned BH candidate in disposable SYNTHETIC projects, not live games.
No API/model calls. No changes to the supplied package. Counts are not billed credits.
"""
from __future__ import annotations
import argparse, contextlib, copy, hashlib, importlib, io, json, platform, sys, time
from pathlib import Path
from unittest.mock import patch

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--package',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
P=args.package.resolve()
sys.dont_write_bytecode=True
sys.path.insert(0,str(P/'tests'))
from support import Fixture, write, git, approval, bh

EXPECTED='5dff7bef67a6ee750918e190ce635ac1cddf2857'
def blob(path):
 b=path.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert blob(P/'project-template/Tools/BH/bh.py')==EXPECTED, 'This probe is bound to the reviewed runtime; review before use on another version.'

@contextlib.contextmanager
def fixture(*a,**kw):
 f=Fixture(*a,**kw)
 try:yield f
 finally:f.close()

def instrument(fn):
 counts={'snapshot_calls':0,'git_calls':0,'file_hash_calls':0,'file_hash_bytes':0,'harness_hash_calls':0,'config_hash_calls':0,'parse_nunit_calls':0,'directory_entries_visited':0,'run_check_calls':[]}
 def wrap(key,original):
  def call(*a,**k):
   counts[key]+=1
   return original(*a,**k)
  return call
 old_hash=bh.file_hash;old_dir=Path.iterdir;old_check=bh.Harness.run_check
 def h(path):
  counts['file_hash_calls']+=1;counts['file_hash_bytes']+=Path(path).stat().st_size
  return old_hash(path)
 def dirs(path):
  for item in old_dir(path):
   counts['directory_entries_visited']+=1;yield item
 def check(self,spec,*a,**k):
  counts['run_check_calls'].append({'id':spec['id'],'adapter':spec['adapter']});return old_check(self,spec,*a,**k)
 started=time.perf_counter()
 with patch.object(bh,'snapshot',wrap('snapshot_calls',bh.snapshot)),patch.object(bh,'git',wrap('git_calls',bh.git)),patch.object(bh,'file_hash',h),patch.object(bh.Harness,'harness_hash',wrap('harness_hash_calls',bh.Harness.harness_hash)),patch.object(bh.Harness,'config_hash',wrap('config_hash_calls',bh.Harness.config_hash)),patch.object(bh,'parse_nunit',wrap('parse_nunit_calls',bh.parse_nunit)),patch.object(Path,'iterdir',dirs),patch.object(bh.Harness,'run_check',check):
  value=fn()
 counts['elapsed_seconds']=round(time.perf_counter()-started,6)
 return value,counts

def phase_error(fn):
 try:fn();return None
 except bh.BHError as exc:return str(exc)

out={'kind':'synthetic-efficiency-observations','reviewed_commit':'b002e3cc0b2134868c36ea93dadc83aaa7333739','runtime_git_blob':EXPECTED,'environment':{'os':platform.system(),'python':platform.python_version()},'limitations':['No Codex model or credits were measured.','No Windows/Unity/real game run.','Timing is one local sample per observation, not a production benchmark.','Fixtures create and remove only their own temporary projects.'],'probes':{}}
R=out['probes']
with fixture() as f:
 f.handoff['checks'][0]['profile']='fast';f.refresh_handoff();f.h=bh.Harness(f.root);f.ready()
 a,ca=instrument(lambda:f.h.verification('fast'))
 b,cb=instrument(lambda:f.h.verification('slice'))
 assert ca['run_check_calls']==[{'id':'CHECK-01','adapter':'nunit'}]
 assert cb['run_check_calls']==[{'id':'CHECK-01','adapter':'nunit'},{'id':'HUMAN-01','adapter':'manual'}]
 assert a['phase']=='EXECUTING' and b['phase']=='READY_FOR_HUMAN_REVIEW'
 R['cumulative_rerun']={'first_phase':a['phase'],'second_phase':b['phase'],'fast':ca,'slice_after_unchanged_fast':cb}

for narrow in (False,True):
 with fixture(narrow=narrow) as f:
  f.ready();f.verify();before=f.h.state()['ac_status'];write(f.root,'Source/unrelated.txt','SYNTHETIC unrelated edit\n')
  after=f.h.resume()
  assert after['acceptance']['AC-01']==('PASS' if narrow else 'NOT_RUN')
  R['unrelated_edit_'+('reviewed_narrow' if narrow else 'default')]={'before':before,'after':after['acceptance'],'phase':after['phase']}

with fixture(narrow=True) as f:
 f.ready();f.verify();before=bh.snapshot(f.root)
 git(f.root,'commit','--allow-empty','-qm','Synthetic content-preserving checkpoint')
 after=bh.snapshot(f.root);err=phase_error(f.h.resume)
 assert before['files']==after['files'] and err and 'revision changed' in err
 R['content_identical_new_commit']={'input_files_identical':True,'resume_error':err}

with fixture(mode='facts') as f:
 f.ready();write(f.root,'Source/value.json',{'value':2});a=f.verify();f.h.recovery('SYNTHETIC diagnosis: recheck unchanged observed counter failure.');b=f.verify();err=phase_error(lambda:f.h.recovery('SYNTHETIC diagnosis: a second bounded correction is needed.'))
 assert a['phase']=='FAILED' and b['phase']=='FAILED' and 'Recovery budget exhausted' in err
 R['recovery_budget']={'first_phase':a['phase'],'second_phase':b['phase'],'counters':f.h.state()['counters'],'configured_budgets':f.h.config['budgets'],'second_recovery_error':err}

with fixture() as f:
 f.handoff['checks'][0]['profile']='fast';f.refresh_handoff();f.h=bh.Harness(f.root);f.ready()
 for _ in range(7):f.h.verification('fast')
 f.h.verification('slice')
 capture=io.StringIO()
 def status():
  with contextlib.redirect_stdout(capture): return bh.main(['--root',str(f.root),'status'])
 code,c=instrument(status)
 assert code==0 and c['parse_nunit_calls']==8
 ret=f.h.return_report();v=bh.load_json(f.root/ret['return'])
 R['status_after_8_runs']={'exit_code':code,'stdout_bytes':len(capture.getvalue().encode()),'counts':c,'return_receipt_count':len(v['receipts']),'current_AC_receipt_count':len(v['acceptance'][0]['receipt_refs'])}

with fixture(mode='facts') as f:
 config=bh.load_json(f.root/'.bh/project.json');config['protected_paths']=[];write(f.root,'.bh/project.json',config)
 f.handoff['allowed_paths']=['Source','Tests'];f.handoff['protected_paths']=[]
 f.overlay['protected_paths']=[];write(f.root,'Handoff/overlay.json',f.overlay);f.refresh_handoff();f.h=bh.Harness(f.root);f.ready()
 driver=f.root/'Tests/fixture_driver.py';driver.write_text(driver.read_text()+'\n# SYNTHETIC authorized helper edit\n')
 result,c=instrument(f.verify)
 assert result['phase']=='BLOCKED'
 receipt=bh.load_json(f.root/result['receipt']['path'])
 R['authorized_helper_edit']={'test_directory_in_allowed_scope':True,'phase':result['phase'],'check_reason':receipt['results'][0]['reason'],'exit_code':receipt['results'][0]['exit_code']}

with fixture(mode='facts') as f:
 check=copy.deepcopy(f.handoff['checks'][0]);check['id']='CHECK-02';f.handoff['checks'].insert(1,check)
 bindings=bh.load_json(f.root/'.bh/bindings.json');binding=copy.deepcopy(bindings['checks'][0]);binding['check_id']='CHECK-02';binding['expectations'][0]['value']=2;bindings['checks'].append(binding);write(f.root,'.bh/bindings.json',bindings)
 f.refresh_handoff();f.h=bh.Harness(f.root);f.ready();write(f.root,'Source/value.json',{'value':2})
 result,c=instrument(f.verify);receipt=bh.load_json(f.root/result['receipt']['path'])
 assert [r['status'] for r in receipt['results']][:2]==['FAIL','PASS']
 R['runs_after_normal_failure']={'results':[{'id':r['id'],'status':r['status']} for r in receipt['results']],'counts':c,'note':'No prerequisite/dependency relation is represented by this fixture. The runtime has no check-level dependency scheduler.'}

for size in (100,500):
 with fixture() as f:
  for i in range(size):write(f.root,f'Source/Dense/asset-{i:04d}.txt','SYNTHETIC\n')
  snap,c=instrument(lambda:bh.snapshot(f.root))
  R[f'dense_snapshot_{size}']={'synthetic_extra_files':size,'snapshot_file_count':snap['file_count'],'snapshot_bytes':len(json.dumps(snap,ensure_ascii=False,indent=2).encode()),'counts':c}

with fixture() as f:
 for i in range(1000):write(f.root,f'Source/Sharded/g{i//50:02d}/asset-{i:04d}.txt','SYNTHETIC\n')
 f.ready();f.verify();ret=f.h.return_report();s=f.h.state();plan=bh.load_json(f.root/s['plan']['path']);receipt=bh.load_json(f.root/s['runs'][0]);returned=bh.load_json(f.root/ret['return'])
 R['actual_1000_extra_file_payloads']={'snapshot_file_count':plan['baseline']['file_count'],'plan_bytes':(f.root/s['plan']['path']).stat().st_size,'receipt_bytes':(f.root/s['runs'][0]).stat().st_size,'return_json_bytes':(f.root/ret['return']).stat().st_size,'return_markdown_bytes':(f.root/ret['return']).with_suffix('.md').stat().st_size,'full_path_hash_maps_in_plan_receipt_return':3}

S=bh.load_json(P/'project-template/.bh/schema.json')
R['source_sizes']={'AGENTS_bytes':(P/'project-template/AGENTS.md').stat().st_size,'schema_bytes':(P/'project-template/.bh/schema.json').stat().st_size,'schema_lines':len((P/'project-template/.bh/schema.json').read_text().splitlines()),'interface_bytes':(P/'project-template/Docs/Harness/INTERFACE.md').stat().st_size,'operating_guide_bytes':(P/'project-template/Docs/Harness/OPERATING_GUIDE.md').stat().st_size,'all_five_skill_body_bytes':sum(p.stat().st_size for p in (P/'project-template/.agents/skills').glob('*/SKILL.md')),'proposal_definition_serialized_bytes':len(json.dumps(S['$defs']['proposal'],indent=2).encode()),'note':'Definition-only size excludes transitive referenced definitions. Byte counts are not token or credit counts.'}
out['assertions']='All probe assertions passed. This is not a rerun or replacement of the 148-test candidate suite.'
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
