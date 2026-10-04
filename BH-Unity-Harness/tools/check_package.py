#!/usr/bin/env python3
"""Check actual distribution, shared copies, GPT budget, preserved references and discovery.
--allow-unassembled reports PARTIAL, never a complete-package pass.
"""
from pathlib import Path
import argparse, ast, hashlib, importlib.util, json, sys
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def check(allow_unassembled=False):
    problems=[];missing=[];checks=[]
    def test(condition,message):
        checks.append(message)
        if not condition:problems.append(message)
    for src,targets in [('contracts/schema.json',['project-template/.bh/schema.json','design-gpt/Knowledge/BH_CONTRACT_SCHEMA.json']),('contracts/INTERFACE.md',['project-template/Docs/Harness/INTERFACE.md','design-gpt/Knowledge/BH_INTERFACE.md'])]:
        for target in targets:test((P/src).read_bytes()==(P/target).read_bytes(),'Byte-identical shared copy: '+target)
    text=(P/'design-gpt/01C_GPT_INSTRUCTIONS_OFFICIAL.md').read_text(encoding='utf-8')
    metrics=json.loads((P/'design-gpt/INSTRUCTION_METRICS.json').read_text())
    test(len(text)<=8000 and len(text)==metrics['characters'] and 8000-len(text)==metrics['headroom'],'Exact instruction character budget')
    test(sha(P/'design-gpt/01C_GPT_INSTRUCTIONS_OFFICIAL.md')==metrics['sha256'],'Instruction digest')
    test(len(text.encode('utf-8'))==len((P/'design-gpt/01C_GPT_INSTRUCTIONS_OFFICIAL.md').read_bytes()),'UTF-8/LF instruction encoding')
    manifest=json.loads((P/'PACKAGE_FILES.json').read_text())
    files=manifest['files'];test(len({f['path'].casefold() for f in files})==len(files),'Unique portable managed paths')
    actual={x.relative_to(P/'project-template').as_posix() for x in (P/'project-template').rglob('*') if x.is_file() and '__pycache__' not in x.parts}
    test(actual=={x['path'] for x in files},'Exact game-installable manifest coverage')
    for row in files:
        p=P/'project-template'/row['path'];test(p.is_file() and sha(p)==row['sha256'],'Installable file hash: '+row['path'])
    km=json.loads((P/'design-gpt/KNOWLEDGE_MANIFEST.json').read_text())
    test(len(km['knowledge_files'])==km['knowledge_count']==15,'Fifteen exact knowledge files')
    test(len({Path(x['path']).name.casefold() for x in km['knowledge_files']})==15,'Knowledge basenames unambiguous')
    refs=json.loads((P/'PRESERVED_REFERENCES.json').read_text())
    for row in refs['files']:
        p=P/row['path']
        if not p.is_file():missing.append(row['path'])
        else:test(blob(p)==row['git_blob_sha'],'Preserved exact Git blob: '+row['path'])
    for row in km['knowledge_files']:
        p=P/'design-gpt'/row['path']
        if not p.exists():continue
        test(sha(p)==row['sha256'] if 'sha256' in row else blob(p)==row['git_blob_sha'],'Knowledge manifest hash: '+row['path'])
    skills=list((P/'project-template/.agents/skills').glob('*/SKILL.md'))
    test(len(skills)==5,'Five active-discovery skills only')
    for p in skills:
        s=p.read_text();test(s.startswith('---\n') and 'name:' in s.split('---')[1] and 'description:' in s.split('---')[1],'Native skill metadata: '+p.parent.name)
        test('allow_implicit_invocation: false' in (p.parent/'agents/openai.yaml').read_text(),'Explicit invocation: '+p.parent.name)
    test(not (P/'project-template/.agents/skills/bh-procedural-regression').exists(),'Optional procedural skill outside discovery')
    for p in P.rglob('*.py'):
        if '__pycache__' not in p.parts:ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
    for name in ['QUICKSTART.md','review/VERIFICATION_REPORT.md','review/ASSURANCE.md','review/REQUIREMENTS_AND_MIGRATION.md','review/SOURCE_INVENTORY.json','review/EXTERNAL_SOURCES.md','design-gpt/REVIEW_AND_SETUP.md','design-gpt/evaluation/REGRESSION_CASES.md','tools/export_examples.py','tests/test_installer.py','tests/test_package.py','project-template/Docs/Harness/OPERATING_GUIDE.md']:
        test((P/name).is_file(),'Required package artifact: '+name)
    if missing and not allow_unassembled:problems.append('Missing preserved source files; assemble from exact Git blobs first')
    return {'status':'FAIL' if problems else ('PARTIAL_UNASSEMBLED' if missing else 'PASS_STATIC_PACKAGE'),'checks':len(checks),'instruction_characters':len(text),'managed_files':len(files),'missing_preserved':missing,'problems':problems,'limitations':'Static package checks are not live GPT, Codex, Unity or Windows validation.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--allow-unassembled',action='store_true');a=p.parse_args()
    try:r=check(a.allow_unassembled);print(json.dumps(r,indent=2));return 2 if r['problems'] else (3 if r['missing_preserved'] else 0)
    except (OSError,ValueError,KeyError,SyntaxError) as exc:print(json.dumps({'status':'FAIL','error':str(exc)}));return 2
if __name__=='__main__':sys.exit(main())
