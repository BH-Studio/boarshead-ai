import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
data = json.loads((BASE / 'b05e2-input.json').read_text(encoding='utf-8'))
out = BASE / 'b05e2-work'
out.mkdir(exist_ok=True)
dep = data['prior_dependencies']
batch = next(x for x in dep['follow_up_batches'] if x['id'] == 'B05e2')
assert [x['path'] for x in data['files']] == batch['paths']
assert len(data['files']) == 7
records = []
for item in data['files']:
    path = item['path']
    assert item['encoding'] == 'utf-8'
    raw = item['content'].encode('utf-8')
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    prior = next(x for x in batch['tree_metadata'] if x['path'] == path)
    tree = item['tree']
    assert tree['type'] == 'blob'
    assert blob == item['sha'] == tree['sha'] == prior['git_blob_sha']
    assert len(raw) == tree['size'] == prior['bytes']
    knowledge = [x for x in dep['knowledge_files'] if x['path'] == path]
    preserved = [x for x in dep['preserved_references'] if x['path'] == path]
    assert len(preserved) == 1
    checks = []
    for role, entries in [('selected_knowledge', knowledge), ('preserved_reference', preserved)]:
        for entry in entries:
            if entry.get('expected_sha256'):
                assert sha256 == entry['expected_sha256']
                checks.append({'role': role, 'algorithm': 'sha256', 'expected': entry['expected_sha256'], 'matched': True})
            if entry.get('expected_git_blob_sha'):
                assert blob == entry['expected_git_blob_sha']
                checks.append({'role': role, 'algorithm': 'git_blob_sha1', 'expected': entry['expected_git_blob_sha'], 'matched': True})
    assert checks
    dest = out / 'BH-Unity-Harness' / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    assert dest.read_bytes() == raw
    records.append({'path': path, 'git_blob_sha': blob, 'sha256': sha256, 'bytes': len(raw), 'selected_knowledge': bool(knowledge), 'preserved_reference': True, 'selected_role': knowledge[0]['role'] if knowledge else None, 'original_source_path': preserved[0]['source_path'], 'manifest_checks': checks, 'matched': True})
    print(f'PASS {path}: {len(raw)} bytes; blob {blob}; sha256 {sha256}; applicable manifest identities matched')

assert sum(x['preserved_reference'] for x in records) == 7
assert sum(x['selected_knowledge'] for x in records) == 6
assert records[-1]['path'] == 'design-gpt/evaluation/SOURCE_V3_ACCEPTANCE_TESTS.md'
assert not records[-1]['selected_knowledge']
assert 'evaluation/SOURCE_V3_ACCEPTANCE_TESTS.md' in dep['evaluation_files_not_knowledge']
sources = {'task': 'B05e2', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'files': records}
findings = {
    'task': 'B05e2', 'review_type': 'bounded identity and retained/selected scope reconciliation',
    'scope_counts': {'selected_knowledge': 6, 'preserved_references': 7, 'evaluation_only': 1},
    'retention': 'K05-K10 match the declared original Git blobs in both selected and preserved records. The evaluation file matches its declared original acceptance-test blob. This is exact byte retention against recorded identities, not repeated framework research.',
    'evaluation_boundary': {'path': records[-1]['path'], 'finding': 'Preserved source evaluation material; excluded from selected knowledge. Its opening instructions specify GPT Preview after configuration and evaluate behavior. Example prompts are evaluation inputs, not project defaults. No preview prompt was executed and no configured-host pass is claimed.'},
    'limits': ['Framework contents were not researched again or activated.', 'No source-game defaults imported.', 'No candidate source content changed.', 'No tests, discovery, package checker, assembler, runner or installer ran.', 'B05f1 and later content batches NOT_STARTED.', 'Not full-package validation, configured-host testing or human adoption.']
}
result = {'task': 'B05e2', 'input_head': data['head'], 'status': 'PASS', 'assigned': 7, 'reconciled': 7, 'missing': [], 'mismatched': [], 'tests': 'NOT_RUN', 'command_exit_status': 0, 'later_batches': 'NOT_STARTED', 'candidate_implementation_changes': False}
fetch = {'task': 'B05e2', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'checkpoint_blob': data['checkpoint_sha'], 'incorporation_status_blob': data['status_sha'], 'B05c_dependency_blob': data['dependency_sha'], 'B05c_dependency_input_head': dep['input_head'], 'content_reads': [{'path': x['path'], 'encoding': x['encoding'], 'returned_blob': x['sha'], 'url': x['display_url'], 'tree': x['tree']} for x in data['files']], 'next_batch_metadata_only': next(x for x in dep['follow_up_batches'] if x['id'] == 'B05f1'), 'tree_truncated': False}
for name, value in [('SOURCES.json', sources), ('RESULT.json', result), ('FINDINGS.json', findings), ('FETCH_METADATA.json', fetch)]:
    (out / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
print('PASS retained/selected scope: 6 selected knowledge inputs; 7 preserved references; evaluation excluded from knowledge')
print('B05e2 PASS: 7/7 identities. Tests NOT_RUN; later batches NOT_STARTED.')
