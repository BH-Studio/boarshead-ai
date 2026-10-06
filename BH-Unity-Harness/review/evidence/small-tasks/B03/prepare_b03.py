import hashlib
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / 'b03-input.json').read_text())
assert not data['harness_tree']['truncated']
tree = {e['path']: e for e in data['harness_tree']['tree']}
work = here / 'b03-work'
sources = json.loads((work / 'SOURCES.json').read_text())
assert sources['input_head'] == data['head']
assert len(sources['files']) == 29
for item in sources['files']:
    raw = (work / 'BH-Unity-Harness' / item['path']).read_bytes()
    git_sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    entry = tree[item['path']]
    assert git_sha == item['git_blob_sha'] == entry['sha'], item['path']
    assert len(raw) == item['bytes'] == entry['size'], item['path']
    assert sha256 == item['sha256'], item['path']
    print('MATCH ' + item['path'] + ' sha256=' + sha256 + ' git_blob=' + git_sha)
manifest = json.loads((work / 'BH-Unity-Harness/PACKAGE_FILES.json').read_text())
installed = {f['path'].removeprefix('project-template/') for f in sources['files'] if f['path'].startswith('project-template/')}
assert installed == {f['path'] for f in manifest['files']}
for f in manifest['files']:
    assert hashlib.sha256((work / 'BH-Unity-Harness/project-template' / f['path']).read_bytes()).hexdigest() == f['sha256']
report = json.loads((work / 'RECONCILIATION.json').read_text())
report['command'] = 'python3 prepare_b03.py > b03-reconciliation.log 2>&1'
report['installed_file_count'] = len(installed)
report['manifest_roster_and_hashes_match'] = True
(work / 'RECONCILIATION.json').write_text(json.dumps(report, indent=2) + '\n')
print('PASS: 29/29 current source identities; 25-file installation roster and manifest hashes matched.')
print('No tests executed during reconciliation.')
