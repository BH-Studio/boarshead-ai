#!/usr/bin/env python3
"""Export actual synthetic subprocess round trips and negative inputs to a NEW directory.
Every approval and game here is synthetic; none can approve a real game or live GPT.
"""
from pathlib import Path
import argparse, copy, json, shutil, sys
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P/'tests'))
from support import Fixture,bh,write

def export(output):
    dest=Path(output).absolute();bh.no_links(dest);bh.require(not dest.exists(),'Output must not exist')
    bh.require(not dest.is_relative_to(P) or dest.is_relative_to(P/'examples'),'Export only into a separate directory or authoring examples, never game-template')
    dest.mkdir(parents=True)
    results=[]
    for name,pipeline,mode,value in [('positive-human-pending','URP','facts',1),('behavior-contradicts-design','HDRP','facts',99)]:
        f=Fixture(mode,pipeline)
        try:
            f.ready()
            if value!=1:write(f.root,'Source/value.json',{'value':value})
            f.verify()
            with f.h.lock():f.h.return_report()
            out=dest/name
            shutil.copytree(f.root,out,ignore=shutil.ignore_patterns('.git','__pycache__'))
            ret=bh.load_json(out/'.bh/exports/task-01/RETURN.json')
            results.append({'case':name,'synthetic':True,'acceptance':ret['acceptance'],'human_acceptance':ret['human_acceptance'],'phase':f.h.state()['phase'],'source_path_original':str(f.root),'portable_note':'Raw receipt commands refer to original temporary execution path; captured bytes/hashes remain the evidence. Copied snapshots are review fixtures, not executable approvals. Re-run exporter for fresh evidence.'})
        finally:f.close()
    f=Fixture()
    try:
        negatives={}
        mutations={'missing-design-approval':lambda h:h.update(approval=None),'unsupported-version':lambda h:h.update(version='99.0.0'),'dropped-acceptance':lambda h:h.update(acceptance_ids=['AC-01']),'lost-project-invariant':lambda h:h.update(invariant_ids=[]),'source-manifest-mismatch':lambda h:h['artifacts'][0].update(sha256='0'*64)}
        for name,fn in mutations.items():
            value=copy.deepcopy(f.handoff);fn(value);write(dest,'negative-inputs/'+name+'.json',value)
            write(f.root,'Handoff/bad.json',value)
            try:f.h.handoff('Handoff/bad.json');negatives[name]='UNEXPECTED_ACCEPT'
            except bh.BHError as exc:negatives[name]={'expected':'REJECT','actual':str(exc)}
        # Demonstrate real stale-evidence rejection after an initially passing run.
        f.ready();f.verify();write(f.root,'Source/value.json',{'value':7});scores,_,gaps=f.h.audit_results(f.h.state());negatives['stale-evidence-after-edit']={'acceptance':scores,'gaps':gaps}
        negatives['missing-knowledge-file']={'expected':'Design host must block dependent procedure; tools/check_package.py rejects missing preserved files','live_gpt':'NOT_RUN'}
        write(dest,'negative-inputs/OBSERVED_RESULTS.json',negatives)
    finally:f.close()
    write(dest,'ROUNDTRIP_RESULTS.json',results)
    write(dest,'README.md','# SYNTHETIC round-trip examples\n\nThese records were produced by actual fixture subprocesses and the shipped runtime, not by writing successful receipts. The two projects are materially different synthetic render-pipeline profiles, not claimed Boar\'s Head games. Positive automated evidence leaves human acceptance PENDING. Contrary behavior fails the approved numeric expectation. Negative inputs and the stale-after-edit observation demonstrate rejection. The original temporary command paths are retained as provenance; they do not make archived evidence automatically valid for a new checkout. No Unity, Windows, Codex or configured-GPT test is implied.\n')
    return results
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args()
    try:print(json.dumps(export(a.output),indent=2))
    except (OSError,bh.BHError,ValueError) as e:print(str(e),file=sys.stderr);sys.exit(2)
