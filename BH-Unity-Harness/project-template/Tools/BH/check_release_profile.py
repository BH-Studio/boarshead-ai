#!/usr/bin/env python3
"""Bounded filename scan of actual build output using an approved, pinned policy.
This does not inspect assembly IL, bundled assets, network behavior or dynamic loading.
It writes observations, not a harness receipt. Absence of matches has only this scope.
"""
import argparse, fnmatch, json, sys
from pathlib import Path
sys.dont_write_bytecode=True
import bh

def scan(build_dir, policy):
    root=Path(build_dir).absolute();bh.no_links(root);root=root.resolve()
    bh.require(root.is_dir(),'Build directory missing')
    bh.require(isinstance(policy,dict) and policy.get('version')=='1.0.0','Unsupported release-scan policy')
    patterns=policy.get('forbidden_filename_patterns')
    bh.require(isinstance(patterns,list) and bool(patterns) and all(isinstance(x,str) and x.strip() and '/' not in x and '\\' not in x for x in patterns),'Explicit reviewed nonempty filename patterns required')
    bh.require(isinstance(policy.get('review_ref'),str) and bool(policy['review_ref'].strip()),'Policy review reference required')
    files=[];matches=[]
    # Do not traverse links/reparse points. Inspect directories before recursing.
    def walk(directory):
        for p in sorted(directory.iterdir()):
            bh.no_links(p)
            if p.is_dir():walk(p)
            elif p.is_file():
                bh.require(len(files)<100000,'Build inventory exceeds 100,000 files; scope it explicitly')
                name=p.relative_to(root).as_posix();files.append(name)
                if any(fnmatch.fnmatchcase(p.name.casefold(),x.casefold()) for x in patterns):matches.append(name)
    walk(root);bh.require(bool(files),'Empty build is not a successful release scan')
    return {'files_scanned':len(files),'forbidden_matches':len(matches)},matches

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('build-dir','policy','result','project','task','run'):p.add_argument('--'+name,required=True)
    a=p.parse_args()
    try:
        facts,matches=scan(a.build_dir,bh.load_json(a.policy));out=Path(a.result).absolute();bh.no_links(out)
        bh.require(not out.exists(),'Result must be fresh; no overwrite')
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open('x',encoding='utf-8') as f:json.dump({'project_id':a.project,'task_id':a.task,'run_id':a.run,'observations':facts,'matches':matches,'limitations':['Filename-only scan of declared output directory; not proof of absence of development capabilities.']},f,indent=2)
        return 0 # Wrapper compares actual forbidden_matches to approved zero expectation.
    except (bh.BHError,OSError,ValueError) as e:print(str(e),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
