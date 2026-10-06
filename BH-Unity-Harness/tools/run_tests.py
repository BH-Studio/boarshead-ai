#!/usr/bin/env python3
"""Portable deterministic test partitions; all parts are required for a suite pass."""
from pathlib import Path
import argparse, datetime, hashlib, io, json, platform, sys, time, unittest
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[1]
def flatten(suite):
    for item in suite:
        if isinstance(item,unittest.TestSuite):yield from flatten(item)
        else:yield item
def source_hashes(root=P):
    """Bind all source/document/manifest bytes, not only executable extensions."""
    root=Path(root)
    return {f.relative_to(root).as_posix():hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted(root.rglob('*')) if f.is_file()
            and not any(part in ('__pycache__','evidence','.git') for part in f.relative_to(root).parts)}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--part',type=int,default=0);p.add_argument('--parts',type=int,default=1);p.add_argument('--output',required=True);a=p.parse_args()
    if not 0<=a.part<a.parts:p.error('Require 0 <= part < parts')
    sys.path.insert(0,str(P/'tests'));cases=sorted(flatten(unittest.defaultTestLoader.discover(str(P/'tests'))),key=lambda t:t.id());selected=cases[a.part::a.parts]
    out=Path(a.output);out.mkdir(parents=True,exist_ok=True);prefix=out/f'part-{a.part}-of-{a.parts}'
    if prefix.with_suffix('.json').exists():p.error('Evidence exists; choose a new output directory, do not overwrite prior attempts')
    hashes=source_hashes(P)
    start=time.time()
    with prefix.with_suffix('.log').open('w',encoding='utf-8') as log:r=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.TestSuite(selected))
    v={'status':'PASS_PART' if r.wasSuccessful() and r.testsRun else 'FAIL','part':a.part,'parts':a.parts,'discovered_total':len(cases),'tests':r.testsRun,'failures':len(r.failures),'errors':len(r.errors),'skipped':len(r.skipped),'seconds':round(time.time()-start,3),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'platform':platform.platform(),'python':sys.version,'case_ids':[c.id() for c in selected],'source_sha256':hashes}
    prefix.with_suffix('.json').write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v[k] for k in ('status','part','parts','discovered_total','tests','failures','errors','skipped','seconds')}));sys.exit(0 if r.wasSuccessful() and r.testsRun else 1)
