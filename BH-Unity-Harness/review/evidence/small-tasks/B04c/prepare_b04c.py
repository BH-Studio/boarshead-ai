import datetime
import hashlib
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / 'b04c-input.json').read_text())
assert data['harness_tree']['truncated'] is False
tree = {e['path']: e for e in data['harness_tree']['tree']}
prior = data['prior_sources']
assert len(prior['files']) == 30
assert len({r['path'] for r in prior['files']}) == 30
work = here / 'b04c-work'
package = work / 'BH-Unity-Harness'
rows = []
for old in prior['files']:
    path = old['path']
    if path in data['files']:
        fetched = data['files'][path]
        assert fetched['encoding'] == 'utf-8' and fetched['sha'] == tree[path]['sha'], path
        raw = fetched['content'].encode('utf-8')
        origin = 'Pinned GitHub file retrieval at input_head; bytes checked against current Git tree and committed B04b ledger'
    else:
        raw = (here / 'b04b-work/BH-Unity-Harness' / path).read_bytes()
        origin = 'Existing local bytes; independently rehashed against current Git tree and committed B04b ledger before reuse'
    git_sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    assert git_sha == tree[path]['sha'] == old['git_blob_sha'], path
    assert len(raw) == tree[path]['size'] == old['bytes'], path
    assert sha256 == old['sha256'], path
    dest = package / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    rows.append({'path': path, 'git_blob_sha': git_sha, 'sha256': sha256, 'bytes': len(raw), 'origin': origin})
    print('MATCH current tree and B04b: ' + path + ' sha256=' + sha256 + ' git_blob=' + git_sha)
manifest = json.loads((package / 'PACKAGE_FILES.json').read_text())
installed = {r['path'] for r in rows if r['path'].startswith('project-template/')}
assert len(installed) == len(manifest['files']) == 25
assert installed == {'project-template/' + f['path'] for f in manifest['files']}
assert installed == {p for p in tree if p.startswith('project-template/') and tree[p]['type'] == 'blob'}
for f in manifest['files']:
    assert hashlib.sha256((package / 'project-template' / f['path']).read_bytes()).hexdigest() == f['sha256'], f['path']
sources = {'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree']['sha'], 'files': rows}
(work / 'SOURCES.json').write_text(json.dumps(sources, indent=2) + '\n')
(work / 'PRIOR_PARTITIONS.json').write_text(json.dumps(data['prior_partitions'], indent=2) + '\n')
prior_path = 'review/evidence/small-tasks/B04b/SOURCES.json'
report = {'task': 'B04c', 'input_head': data['head'], 'reconciled_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'command': 'python3 prepare_b04c.py > b04c-reconciliation.log 2>&1',
          'source_count': len(rows), 'matched_count': len(rows), 'installed_file_count': 25,
          'manifest_roster_and_hashes_match': True, 'git_tree_truncated': False,
          'root_tree': data['root_tree'], 'harness_tree': data['harness_tree']['sha'],
          'tree_url': 'https://api.github.com/repos/BH-Studio/boarshead-ai/git/trees/' + data['harness_tree']['sha'] + '?recursive=1',
          'prior_ledger_path': prior_path, 'prior_ledger_git_blob_sha': tree[prior_path]['sha'],
          'prior_input_head': prior['input_head'], 'prior_ledger_matched_count': len(rows), 'changed_inputs': [],
          'dependency_scope': ['efficiency runtime module imports support and exercises bh.py', 'support imports bh.py and installer/install.py',
                               'Fixture copies the entire 25-file template and reads tests/fixture_driver.py',
                               'PACKAGE_FILES.json included as independent installation-roster integrity evidence'],
          'tests_executed': 0, 'exit_status': 0, 'result': 'PASS'}
(work / 'RECONCILIATION.json').write_text(json.dumps(report, indent=2) + '\n')
print('PASS: 30/30 current source identities also match committed B04b ledger; 25-file manifest roster/hashes matched.')
print('No tests executed during reconciliation.')
