#!/usr/bin/env python3
"""Assemble the additions and exact preserved references, offline, into a NEW directory.
Never changes the clone, installs into a game, runs repository scripts or fetches data.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode=True
PACKAGE=Path(__file__).resolve().parents[1]

def blob_sha(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def assemble(clone, output, package=PACKAGE):
    clone=Path(clone).resolve(); output=Path(output).absolute(); package=Path(package).resolve()
    if output.exists() or output.is_symlink(): raise ValueError('Output must not exist; no overwrite')
    for p in [output, *output.parents]:
        if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()): raise ValueError('Linked destination rejected')
    if output.is_relative_to(clone) or output.is_relative_to(package): raise ValueError('Output must be outside source clone and additions')
    git=shutil.which('git')
    if not git: raise ValueError('Git is required; no automatic installation')
    def run(*args):
        return subprocess.run([git,'-c','core.fsmonitor=false','-C',str(clone),*args],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30).stdout
    run('rev-parse','--git-dir')
    manifest=json.loads((package/'PRESERVED_REFERENCES.json').read_text(encoding='utf-8'))
    recovered={}
    for entry in manifest['files']:
        name=entry['path']; sha=entry['git_blob_sha']; rel=Path(name)
        if not re.fullmatch('[0-9a-f]{40}',sha) or rel.is_absolute() or '..' in rel.parts or '\\' in name or not name.startswith('design-gpt/'):
            raise ValueError('Unsafe reference manifest')
        data=run('cat-file','blob',sha)
        if blob_sha(data)!=sha: raise ValueError('Git blob mismatch: '+name)
        recovered[name]=data
    output.parent.mkdir(parents=True,exist_ok=True)
    stage=Path(tempfile.mkdtemp(prefix='.bh-assembly-',dir=output.parent))
    try:
        for src in package.rglob('*'):
            if src.is_symlink() or (hasattr(src,'is_junction') and src.is_junction()): raise ValueError('Linked source rejected')
            if not src.is_file() or '__pycache__' in src.parts: continue
            dest=stage/src.relative_to(package);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
        for name,data in recovered.items():
            dest=stage/name
            if dest.exists() and dest.read_bytes()!=data: raise ValueError('Conflicting preserved file: '+name)
            dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        if output.exists(): raise ValueError('Concurrent destination creation')
        stage.rename(output)
    finally:
        if stage.exists(): shutil.rmtree(stage)
    return {'status':'ASSEMBLED_NOT_ADOPTED','output':str(output),'preserved_files':len(recovered),'next':'Run tools/check_package.py and the actual suite; review before any pilot.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--clone',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    try: print(json.dumps(assemble(a.clone,a.output),indent=2));return 0
    except (OSError,ValueError,KeyError,subprocess.SubprocessError) as exc: print(json.dumps({'status':'BLOCKED','error':str(exc)}),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
