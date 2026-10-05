#!/usr/bin/env python3
"""Reproducible offline efficiency observations; no model/credit accounting."""
import argparse,importlib.util,json,sys,hashlib
from pathlib import Path
from unittest.mock import patch
p=argparse.ArgumentParser();p.add_argument('--package',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
if a.output.exists():raise SystemExit('Refusing to overwrite existing evidence')
sys.dont_write_bytecode=True
sys.path.insert(0,str(a.package.resolve()/'tests'))
from support import Fixture,bh,write
spec=importlib.util.spec_from_file_location('views',a.package/'project-template/Tools/BH/views.py');views=importlib.util.module_from_spec(spec)
with patch.dict(sys.modules,{'bh':bh}):spec.loader.exec_module(views)
result={'kind':'offline-efficiency-observations','runtime_sha256':hashlib.sha256((a.package/'project-template/Tools/BH/bh.py').read_bytes()).hexdigest(),'limitations':['No native Codex or billed credits measured','Linux synthetic projects, not Windows/Unity','Byte and operation counts are not token or credit counts']}
f=Fixture(narrow=True)
try:
 f.ready();small=views.context_view(f.h)
 for i in range(1000):write(f.root,f'Source/irrelevant/{i:04}.txt','synthetic')
 large=views.context_view(f.h)
 result['context_small_bytes']=len(json.dumps(small).encode());result['context_1000_more_files_bytes']=len(json.dumps(large).encode())
 with patch.object(bh,'snapshot',wraps=bh.snapshot) as snap:
  f.verify()
 result['one_automated_one_manual_snapshot_calls']=snap.call_count
 with f.h.lock():v=views.return_view(f.h)
 result['return_full_bytes']=(f.root/v['full_return']['path']).stat().st_size
 result['return_view_bytes']=len(json.dumps(v,ensure_ascii=False,indent=2).encode())
finally:f.close()
f=Fixture()
try:
 f.handoff['checks'][0]['profile']='fast';f.refresh_handoff();f.ready()
 for _ in range(8):
  with f.h.lock():f.h.verification('fast')
 with patch.object(bh,'parse_nunit',wraps=bh.parse_nunit) as parse,patch.object(f.h,'harness_hash',wraps=f.h.harness_hash) as hh:
  f.h.audit_results(f.h.state())
 result['status_after_8_runs']={'nunit_reparses':parse.call_count,'harness_hash_calls':hh.call_count}
 with patch.object(f.h,'run_check',wraps=f.h.run_check) as check,f.h.lock():o=f.h.verification('slice',reuse=True)
 result['unchanged_fast_to_slice_reuse']={'executed_check_calls':check.call_count,'reused_checks':o['reused_checks'],'new_receipt_created':len(f.h.state()['runs'])!=8,'final_gate_still_required':bool(o['blockers'])}
finally:f.close()
for n in (100,500):
 f=Fixture()
 try:
  for i in range(n):write(f.root,f'Source/dense/{i:04}.txt','synthetic')
  old=Path.iterdir;counter=[0,0]
  def visit(path):
   counter[0]+=1
   for item in old(path):counter[1]+=1;yield item
  with patch.object(Path,'iterdir',visit):bh.snapshot(f.root)
  result['dense_'+str(n)]={'directory_enumerations':counter[0],'directory_entries_visited':counter[1]}
 finally:f.close()
a.output.parent.mkdir(parents=True,exist_ok=True)
a.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
