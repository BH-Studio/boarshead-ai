"""B01 only: hash retrieved installed bytes; never import or execute the harness."""
import base64
import hashlib
import json
import pathlib
import sys

src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
data = json.loads(src.read_text(encoding='utf-8'))

def blob_sha(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()

manifest_raw = base64.b64decode(data['manifest']['content'])
manifest = json.loads(manifest_raw)
entries = {e['path']: e for e in data['template_tree']['tree'] if e['type'] == 'blob'}
retrieved = {f['path']: f for f in data['files']}
paths = [f['path'] for f in manifest['files']]
missing = sorted(set(paths) - set(entries))
extra = sorted(set(entries) - set(paths))
duplicates = sorted({p for p in paths if paths.count(p) > 1})
rows = []
for f in manifest['files']:
    p = f['path']
    e = entries.get(p)
    r = retrieved.get(p)
    if e is None or r is None or 'content' not in r:
        rows.append({'path': p, 'status': 'MISSING', 'expected_sha256': f['sha256']})
        continue
    raw = r['content'].encode('utf-8')
    sha256 = hashlib.sha256(raw).hexdigest()
    git_sha = blob_sha(raw)
    matches = sha256 == f['sha256'] and git_sha == e['sha'] and len(raw) == e['size'] and e['mode'] == '100644'
    rows.append({'path': p, 'repository_path': 'BH-Unity-Harness/project-template/' + p,
                 'ownership': f['ownership'], 'bytes': len(raw), 'expected_sha256': f['sha256'],
                 'actual_sha256': sha256, 'expected_git_blob_sha': e['sha'],
                 'actual_git_blob_sha': git_sha, 'expected_bytes': e['size'], 'mode': e['mode'],
                 'status': 'MATCH' if matches else 'MISMATCH'})
manifest_ok = blob_sha(manifest_raw) == data['manifest']['sha'] and len(manifest_raw) == data['manifest']['reported_size']
checkpoint_raw = data['checkpoint']['content'].encode('utf-8')
checkpoint_ok = blob_sha(checkpoint_raw) == data['checkpoint']['sha']
valid = (len(paths) == 25 and not missing and not extra and not duplicates
         and manifest_ok and checkpoint_ok and not data['template_tree']['truncated']
         and all(r['status'] == 'MATCH' for r in rows))
command = 'python3 b01_validate.py b01-input.json b01-evidence'
result = {'task': 'B01', 'result': 'PASS' if valid else 'FAIL', 'repository': data['repository'],
          'branch': data['branch'], 'input_head': data['head'],
          'input_root_tree': data['git_commit']['tree']['sha'],
          'installed_tree': data['template_tree']['sha'],
          'manifest': {'path': 'BH-Unity-Harness/PACKAGE_FILES.json', 'git_blob_sha': data['manifest']['sha'],
                       'computed_git_blob_sha': blob_sha(manifest_raw), 'sha256': hashlib.sha256(manifest_raw).hexdigest(),
                       'bytes': len(manifest_raw), 'identity_match': manifest_ok},
          'checkpoint_input': {'git_blob_sha': data['checkpoint']['sha'], 'identity_match': checkpoint_ok},
          'counts': {'manifest_files': len(paths), 'installed_tree_files': len(entries),
                     'matched': sum(r['status'] == 'MATCH' for r in rows)},
          'missing_paths': missing, 'extra_paths': extra, 'duplicate_paths': duplicates,
          'mismatched_paths': [r['path'] for r in rows if r['status'] != 'MATCH'],
          'retrieval': 'Immutable GitHub tree at pinned commit; fetch_blob for each declared blob; UTF-8 re-encoding accepted only after Git blob SHA and byte-size checks. Manifest retrieved as base64.',
          'retrieval_note': data['retrieval_note'], 'pr_before': data['pr'],
          'command': command, 'exit_status': 0 if valid else 1,
          'scope': 'Installed-file identity validation only; no runtime tests, harness execution, live installation, design edits or B02 work.',
          'files': rows}
(out / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('B01 input head: ' + data['head'])
print('PACKAGE_FILES.json Git blob identity: ' + ('MATCH' if manifest_ok else 'MISMATCH'))
print('BUILD_CHECKPOINT.md input Git blob identity: ' + ('MATCH' if checkpoint_ok else 'MISMATCH'))
for r in rows:
    print(r['status'] + ' ' + r['path'] + ' sha256=' + r.get('actual_sha256', 'UNAVAILABLE') + ' git_blob=' + r.get('actual_git_blob_sha', 'UNAVAILABLE'))
print('Missing paths: ' + json.dumps(missing))
print('Extra installed paths: ' + json.dumps(extra))
print('Duplicate manifest paths: ' + json.dumps(duplicates))
print('Mismatched paths: ' + json.dumps(result['mismatched_paths']))
print('RESULT ' + result['result'] + ': ' + str(result['counts']['matched']) + '/' + str(len(paths)) + ' installed files matched')
print('Runtime tests: NOT_RUN; B02: NOT_STARTED')
sys.exit(result['exit_status'])
