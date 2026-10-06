import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
data = json.loads((BASE / 'b05f1-input.json').read_text(encoding='utf-8'))
out = BASE / 'b05f1-work'
out.mkdir(exist_ok=True)
dep = data['prior_dependencies']
batch = next(x for x in dep['follow_up_batches'] if x['id'] == 'B05f1')
assert [x['path'] for x in data['files']] == batch['paths']
assert len(data['files']) == 10
records = []
profiles = []
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
    dest = out / 'BH-Unity-Harness' / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    assert dest.read_bytes() == raw
    role = 'shared contract guidance' if path.startswith('contracts/') else 'synthetic example' if path.startswith('examples/') else 'optional resource outside installed template'
    records.append({'path': path, 'git_blob_sha': blob, 'sha256': sha256, 'bytes': len(raw), 'expected_B05c_blob': prior['git_blob_sha'], 'expected_B05c_bytes': prior['bytes'], 'role': role, 'matched': True})
    if path.endswith('.json'):
        profile = json.loads(item['content'])
        assert profile['synthetic'] is True and profile['status'] == 'SYNTHETIC'
        assert profile['optional_capabilities'] == []
        profiles.append({'path': path, 'project_id': profile['project_id'], 'synthetic': profile['synthetic'], 'status': profile['status'], 'optional_capabilities': profile['optional_capabilities'], 'open_decisions': profile['open_decisions']})
    print(f'PASS {path}: {len(raw)} bytes; blob {blob}; sha256 {sha256}; current tree and B05c identities matched')

assert len(profiles) == 2
sources = {'task': 'B05f1', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'files': records}
findings = {
    'task': 'B05f1', 'review_type': 'bounded identity and contract/optional/profile scope reading',
    'synthetic_profiles': profiles,
    'contract_boundary': 'Consumer opening specifies execution guidance with approved project inputs, not design defaults; producer personas/frameworks remain design-host references. Shared interface remains canonical paired guidance; no contract was changed or executed.',
    'optional_boundary': 'Procedural regression and Auditor procedures require actual project scope and separately approved optional adoption. Auditor agent policy disables implicit invocation. Build README labels the Windows64 C# producer optional and NOT_RUN in Unity, with approval and actual project/patch/compiler requirements. None was installed, invoked or treated as a universal default.',
    'limits': ['JSON parsing and synthetic-label checks only; no schema/runtime validation claim.', 'C# and YAML byte identities checked; neither compiled nor executed.', 'No tests, discovery, package checker, assembler, runner or installer ran.', 'No source-game defaults imported or source research repeated.', 'No candidate implementation/design content changed.', 'B05f2 and later content batches NOT_STARTED; no full-package/host/adoption claim.']
}
result = {'task': 'B05f1', 'input_head': data['head'], 'status': 'PASS', 'assigned': 10, 'reconciled': 10, 'missing': [], 'mismatched': [], 'synthetic_profiles_parsed': 2, 'tests': 'NOT_RUN', 'command_exit_status': 0, 'later_batches': 'NOT_STARTED', 'candidate_implementation_changes': False}
fetch = {'task': 'B05f1', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'checkpoint_blob': data['checkpoint_sha'], 'incorporation_status_blob': data['status_sha'], 'B05c_dependency_blob': data['dependency_sha'], 'B05c_dependency_input_head': dep['input_head'], 'content_reads': [{'path': x['path'], 'encoding': x['encoding'], 'returned_blob': x['sha'], 'url': x['display_url'], 'tree': x['tree']} for x in data['files']], 'next_batch_metadata_only': next(x for x in dep['follow_up_batches'] if x['id'] == 'B05f2'), 'tree_truncated': False}
for name, value in [('SOURCES.json', sources), ('RESULT.json', result), ('FINDINGS.json', findings), ('FETCH_METADATA.json', fetch)]:
    (out / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
print('PASS synthetic profile labels: 2 parsed; SYNTHETIC true; no enabled optional capabilities')
print('B05f1 PASS: 10/10 identities. Tests NOT_RUN; optional installation/activation NOT_RUN; later batches NOT_STARTED.')
