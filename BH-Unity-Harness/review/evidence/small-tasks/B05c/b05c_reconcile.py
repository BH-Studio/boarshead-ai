import datetime
import hashlib
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent
data = json.loads((root / 'b05c-input.json').read_text())
assert data['harness_tree']['truncated'] is False
tree = {e['path']: e for e in data['harness_tree']['tree']}
batch = next(b for b in data['prior_dependencies']['follow_up_batches'] if b['id'] == 'B05c')
assert sorted(data['files']) == sorted(batch['paths']) and len(data['files']) == 8
prior = {r['path']: r for r in batch['tree_metadata']}
work = root / 'b05c-work'
work.mkdir(exist_ok=True)
rows = []
for path in batch['paths']:
    fetched = data['files'][path]
    assert fetched['encoding'] == 'utf-8'
    raw = fetched['content'].encode('utf-8')
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    assert blob == fetched['sha'] == tree[path]['sha'] == prior[path]['git_blob_sha'], path
    assert len(raw) == tree[path]['size'] == prior[path]['bytes'], path
    dest = work / 'BH-Unity-Harness' / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    rows.append({'path': path, 'git_blob_sha': blob, 'sha256': sha256, 'bytes': len(raw),
                 'origin': 'Pinned GitHub retrieval; checked against current immutable tree and B05b batch metadata'})
    print('MATCH ' + path + ' bytes=' + str(len(raw)) + ' git_blob=' + blob + ' sha256=' + sha256)
def value(path):
    return json.loads(data['files'][path]['content'])
package = value('PACKAGE_FILES.json')
refs = value('PRESERVED_REFERENCES.json')
knowledge = value('design-gpt/KNOWLEDGE_MANIFEST.json')
metrics = value('design-gpt/INSTRUCTION_METRICS.json')
schema = value('contracts/schema.json')
text = data['files']['design-gpt/01C_GPT_INSTRUCTIONS_OFFICIAL.md']['content']
assert len(text) == metrics['characters'] == 7798
assert metrics['budget'] == 8000 and metrics['headroom'] == 8000-len(text) == 202
assert hashlib.sha256(text.encode('utf-8')).hexdigest() == metrics['sha256']
assert '\r' not in text and text.endswith('\n')
assert package['version'] == '1.0.0' and len(package['files']) == 25
installed = {'project-template/' + f['path'] for f in package['files']}
assert len(installed) == 25
assert installed == {p for p, e in tree.items() if p.startswith('project-template/') and e['type'] == 'blob'}
assert knowledge['knowledge_count'] == len(knowledge['knowledge_files']) == 15
selected = ['design-gpt/' + f['path'] for f in knowledge['knowledge_files']]
assert len(set(selected)) == len({pathlib.Path(p).name.casefold() for p in selected}) == 15
assert len(refs['files']) == len({f['path'] for f in refs['files']}) == 13
for row in refs['files']:
    assert tree[row['path']]['sha'] == row['git_blob_sha'], row['path']
for row in knowledge['knowledge_files']:
    path = 'design-gpt/' + row['path']
    assert tree[path]['type'] == 'blob', path
    if 'git_blob_sha' in row:
        assert tree[path]['sha'] == row['git_blob_sha'], path
assert 'review/reference-only/K11_SOURCE_LESSONS.md' not in selected
assert schema['$id'] == 'urn:bh:contracts:1.0.0'
schema_refs = []
def walk(v):
    if isinstance(v, dict):
        if '$ref' in v: schema_refs.append(v['$ref'])
        for item in v.values(): walk(item)
    elif isinstance(v, list):
        for item in v: walk(item)
walk(schema)
assert all(r.startswith('#/$defs/') and r.removeprefix('#/$defs/') in schema['$defs'] for r in schema_refs)
(work / 'SOURCES.json').write_text(json.dumps({'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree']['sha'], 'files': rows}, indent=2) + '\n')
findings = {'task': 'B05c', 'input_head': data['head'], 'installed_count': 25, 'installed_path_roster_matches_tree': True,
            'installed_content_hash_verification': 'NOT_RUN_IN_B05c', 'knowledge_count': 15, 'preserved_count': 13,
            'preserved_declared_git_blobs_match_tree_metadata': True, 'knowledge_declared_git_blobs_match_tree_metadata': True,
            'downstream_resource_bytes': 'NOT_RETRIEVED_IN_B05c', 'instruction_characters': len(text), 'instruction_headroom': 202,
            'instruction_metrics_hash_and_encoding_match': True, 'schema_id': schema['$id'], 'schema_definition_count': len(schema['$defs']),
            'schema_refs_local_and_resolved': True, 'schema_runtime_validation': 'NOT_RUN',
            'reference_only_K11_is_not_knowledge_selection': True,
            'authority_review': 'Official policy retains human approval, game neutrality, design/implementation separation, thin pinned handoffs, returned-evidence review and no guessed savings. Evaluation rows remain NOT_RUN host scenarios; read examples are not executed or adopted.'}
(work / 'MANIFEST_FINDINGS.json').write_text(json.dumps(findings, indent=2) + '\n')
report = {'task': 'B05c', 'result': 'PASS_SOURCE_RECONCILIATION', 'input_head': data['head'],
          'command': 'python3 b05c_reconcile.py > b05c-reconciliation.log 2>&1', 'working_directory': str(root),
          'finished_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'exit_status': 0,
          'source_count': 8, 'matched_count': 8, 'missing_sources': [], 'mismatched_sources': [],
          'json_documents_parsed': 5, 'tests_executed': 0, 'package_checker_assembler_runner': 'NOT_RUN',
          'B05d_or_other_resource_content': 'NOT_RETRIEVED', 'environment': {'python': sys.version},
          'scope': 'Eight assigned input bytes and intra-batch metrics/schema/manifest structure only; downstream identities are tree metadata, not resource byte verification or full suite proof.'}
(work / 'RESULT.json').write_text(json.dumps(report, indent=2) + '\n')
print('PASS: 8/8 input identities; five JSON documents parsed; instruction metrics 7798 characters / 202 headroom matched.')
print('ROSTERS: 25 installed, 15 selected knowledge, 13 preserved references; downstream tree metadata only.')
print('Tests, package checker, assembler, runner and B05d/other content retrieval NOT_RUN.')
