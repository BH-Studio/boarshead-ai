import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
data = json.loads((BASE / 'b05e1-input.json').read_text(encoding='utf-8'))
out = BASE / 'b05e1-work'
out.mkdir(exist_ok=True)
dep = data['prior_dependencies']
batch = next(x for x in dep['follow_up_batches'] if x['id'] == 'B05e1')
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
    assert len(knowledge) == 1
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
    records.append({'path': path, 'git_blob_sha': blob, 'sha256': sha256, 'bytes': len(raw), 'selected_knowledge': True, 'preserved_reference': bool(preserved), 'selected_role': knowledge[0]['role'], 'original_source_path': preserved[0]['source_path'] if preserved else None, 'manifest_checks': checks, 'matched': True})
    print(f'PASS {path}: {len(raw)} bytes; blob {blob}; sha256 {sha256}; applicable manifest identities matched')

assert sum(x['preserved_reference'] for x in records) == 5
assert sum(x['selected_knowledge'] for x in records) == 7
sources = {'task': 'B05e1', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'files': records}
findings = {
    'task': 'B05e1', 'review_type': 'bounded identity and retained/selected scope reconciliation',
    'scope_counts': {'selected_knowledge': 7, 'also_preserved_references': 5, 'shared_interface_resources': 2},
    'retention': 'Full v3 method, persona routing and K02-K04 framework inputs match the recorded original Git blobs in both selected and preserved manifests. This proves byte retention against those declared identities, without repeating original research or executing their instructions.',
    'shared_contracts': 'Knowledge schema and interface match the selected manifest SHA-256 identities. Other consumer copies were not fetched in this batch; current all-copy equality remains a later closure check.',
    'authority_reading': {'paths': ['design-gpt/01_GPT_INSTRUCTIONS_FULL.md', 'design-gpt/Knowledge/K01_PERSONAS_AND_ROUTING.md', 'design-gpt/Knowledge/BH_INTERFACE.md'], 'finding': 'Read only opening authority/routing and producer-resource boundary passages. Full method keeps human final authority and uses expert lenses within one model. Interface assigns design proposals/review, human decisions/approvals and harness verified execution; producer retrieval is distinct from Codex consumption. No file is installed or activated by this reconciliation.'},
    'limits': ['No original framework/design research repeated.', 'No source-game defaults imported.', 'No candidate source content changed.', 'No tests, discovery, package checker, assembler, runner or installer ran.', 'B05e2 and all later content batches NOT_STARTED.', 'Not full-package validation, host activation or human adoption.']
}
result = {'task': 'B05e1', 'input_head': data['head'], 'status': 'PASS', 'assigned': 7, 'reconciled': 7, 'missing': [], 'mismatched': [], 'tests': 'NOT_RUN', 'command_exit_status': 0, 'later_batches': 'NOT_STARTED', 'candidate_implementation_changes': False}
fetch = {'task': 'B05e1', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'checkpoint_blob': data['checkpoint_sha'], 'incorporation_status_blob': data['status_sha'], 'B05c_dependency_blob': data['dependency_sha'], 'B05c_dependency_input_head': dep['input_head'], 'content_reads': [{'path': x['path'], 'encoding': x['encoding'], 'returned_blob': x['sha'], 'url': x['display_url'], 'tree': x['tree']} for x in data['files']], 'next_batch_metadata_only': next(x for x in dep['follow_up_batches'] if x['id'] == 'B05e2'), 'tree_truncated': False}
for name, value in [('SOURCES.json', sources), ('RESULT.json', result), ('FINDINGS.json', findings), ('FETCH_METADATA.json', fetch)]:
    (out / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
print('PASS retained/selected scope: 7 selected inputs; 5 also preserved references; 2 shared contract inputs')
print('B05e1 PASS: 7/7 identities. Tests NOT_RUN; later batches NOT_STARTED.')
