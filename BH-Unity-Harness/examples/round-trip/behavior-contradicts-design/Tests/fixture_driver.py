#!/usr/bin/env python3
"""SYNTHETIC test process. Writes observations, never harness receipts."""
import argparse, json, sys, time
from pathlib import Path
p=argparse.ArgumentParser()
for x in ('root','result','project','task','run','mode'): p.add_argument('--'+x,required=True)
a=p.parse_args(); root=Path(a.root); out=Path(a.result)
value=json.loads((root/'Source/value.json').read_text())['value']
if a.mode=='timeout': time.sleep(20)
if a.mode=='nonzero': print('Synthetic process failure',file=sys.stderr);sys.exit(7)
if a.mode=='compile': print('error CS1002: Synthetic compile failure',file=sys.stderr);sys.exit(1)
if a.mode=='missing': sys.exit(0)
if a.mode=='mutate': (root/'Source/value.json').write_text('{"value":999}')
if a.mode in ('facts','wrong-run','diagnostics','build'):
 v={'project_id':a.project,'task_id':a.task,'run_id':a.run,'observations':{'value':value}}
 if a.mode=='wrong-run':v['run_id']='stale-run'
 if a.mode=='diagnostics':
  v.update(source='sonarqube',analysis_complete=True,issues=[] if value==1 else [{'path':'Source/value.json','line':1,'rule':'SYNTHETIC','message':'Synthetic new diagnostic','severity':'warning'}])
 if a.mode=='build':v.update(build_result='Failed',errors=1,target='Synthetic-Windows',outputs=[])
 out.write_text(json.dumps(v));sys.exit(0)
if a.mode=='zero':out.write_text('<test-run total="0" passed="0" failed="0" skipped="0" inconclusive="0" result="Passed"/>');sys.exit(0)
if a.mode=='entity':out.write_text('<!DOCTYPE x [<!ENTITY e SYSTEM "file:///etc/passwd">]><test-run>&e;</test-run>');sys.exit(0)
name='Fixture.Other' if a.mode=='wrong-test' else 'Fixture.CounterChanges'
status='Skipped' if a.mode=='skip' else ('Passed' if value==1 else 'Failed')
c={'Passed':(1,0,0),'Failed':(0,1,0),'Skipped':(0,0,1)}[status]
out.write_text(f'<test-run total="1" passed="{c[0]}" failed="{c[1]}" skipped="{c[2]}" inconclusive="0" result="{status}"><test-suite result="{status}"><test-case fullname="{name}" result="{status}"/></test-suite></test-run>')
