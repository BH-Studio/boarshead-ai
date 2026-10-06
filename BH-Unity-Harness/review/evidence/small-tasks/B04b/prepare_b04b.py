import datetime
import hashlib
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / 'b04b-input.json').read_text())
assert data['harness_tree']['truncated'] is False
tree = {e['path']: e for e in data['harness_tree']['tree']}
work = here / 'b04b-work'
package = work / 'BH-Unity-Harness'
manifest = json.loads(data['files']['PACKAGE_FILES.json']['content'])
paths = ['project-template/' + f['path'] for f in manifest['files']]
paths += ['PACKAGE_FILES.json', 'installer/install.py', 'tests/support.py',
          'tests/fixture_driver.py', 'tests/test_efficiency_runtime.py']
assert len(paths) == len(set(paths)) == 30
assert {p for p in tree if p.startswith('project-template/') and tree[p]['type'] == 'blob'} == {p for p in paths if p.startswith('project-template/')}
rows = []
for path in sorted(paths):
    if path in data['files']:
        fetched = data['files'][path]
        assert fetched['encoding'] == 'utf-8'
        raw = fetched['content'].encode('utf-8')
        assert fetched['sha'] == tree[path]['sha'], path
        origin = 'Pinned GitHub file retrieval at input_head; bytes verified against current Git tree'
    else:
        raw = (here / 'b04a-work/BH-Unity-Harness' / path).read_bytes()
        origin = 'Existing local bytes; independently rehashed against current pinned Git tree before reuse'
    git_sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    assert git_sha == tree[path]['sha'] and len(raw) == tree[path]['size'], path
    dest = package / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    rows.append({'path': path, 'git_blob_sha': git_sha, 'sha256': sha256, 'bytes': len(raw), 'origin': origin})
    print('MATCH ' + path + ' sha256=' + sha256 + ' git_blob=' + git_sha)
for f in manifest['files']:
    assert hashlib.sha256((package / 'project-template' / f['path']).read_bytes()).hexdigest() == f['sha256'], f['path']
sources = {'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree']['sha'], 'files': rows}
(work / 'SOURCES.json').write_text(json.dumps(sources, indent=2) + '\n')
report = {'task': 'B04b', 'input_head': data['head'], 'reconciled_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'command': 'python3 prepare_b04b.py > b04b-reconciliation.log 2>&1',
          'source_count': len(rows), 'matched_count': len(rows), 'installed_file_count': len(manifest['files']),
          'manifest_roster_and_hashes_match': True, 'git_tree_truncated': False,
          'root_tree': data['root_tree'], 'harness_tree': data['harness_tree']['sha'],
          'tree_url': 'https://api.github.com/repos/BH-Studio/boarshead-ai/git/trees/' + data['harness_tree']['sha'] + '?recursive=1',
          'dependency_scope': ['efficiency runtime module imports support and exercises bh.py, including its real CLI', 'support imports bh.py and installer/install.py',
                               'Fixture copies the entire 25-file template and executes tests/fixture_driver.py for selected evidence cases',
                               'PACKAGE_FILES.json included as independent installation-roster integrity evidence'],
          'tests_executed': 0, 'exit_status': 0, 'result': 'PASS'}
(work / 'RECONCILIATION.json').write_text(json.dumps(report, indent=2) + '\n')
print('PASS: 30/30 current source identities; 25-file installation roster and manifest hashes matched.')
print('No tests executed during reconciliation.')
