import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
data = json.loads((BASE / 'b05d-input.json').read_text(encoding='utf-8'))
out = BASE / 'b05d-work'
out.mkdir(exist_ok=True)
dep = data['prior_dependencies']
batch = next(x for x in dep['follow_up_batches'] if x['id'] == 'B05d')
assert [x['path'] for x in data['files']] == batch['paths']
assert len(data['files']) == 3
records = []
for item in data['files']:
    path = item['path']
    assert item['encoding'] == 'utf-8'
    raw = item['content'].encode('utf-8')
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    tree = item['tree']
    prior = next(x for x in batch['tree_metadata'] if x['path'] == path)
    assert tree['type'] == 'blob'
    assert blob == item['sha'] == tree['sha'] == prior['git_blob_sha']
    assert len(raw) == tree['size'] == prior['bytes']
    knowledge = [x for x in dep['knowledge_files'] if x['path'] == path]
    preserved = [x for x in dep['preserved_references'] if x['path'] == path]
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
    records.append({'path': path, 'git_blob_sha': blob, 'sha256': sha256, 'bytes': len(raw), 'selected_knowledge': bool(knowledge), 'preserved_reference': bool(preserved), 'manifest_checks': checks, 'matched': True})
    print(f'PASS {path}: {len(raw)} bytes; blob {blob}; sha256 {sha256}; applicable manifest identities matched')

sources = {'task': 'B05d', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'files': records}
findings = {
    'task': 'B05d', 'review_type': 'bounded identity and source-retention scope review; not original design/framework research',
    'historical_K11': {'path': records[0]['path'], 'role': 'preserved reference only; excluded from selected knowledge', 'observed_sections': ['Purpose', '7. Resource envelopes must be explicit and project-specific', '8. Representative-scale tests change architectural confidence'], 'finding': 'Retains historical project examples and expressly prohibits copying their implementation details or CPU percentage into unrelated projects. No historical requirement was imported.'},
    'generalized_K11': {'path': records[1]['path'], 'role': 'selected knowledge', 'observed_sections': ['Purpose', '7. Resource envelopes must be explicit and project-specific', '8. Representative-scale tests change architectural confidence', '13. Design authority and implementation authority should remain distinct'], 'finding': 'Retains fifteen generalized lessons; purpose rejects source names/mechanics/genre/player-count/middleware/pipeline/numerical defaults. Scale counts and budgets derive from current project artifacts.'},
    'K12': {'path': records[2]['path'], 'role': 'selected compiler/handoff/returned-evidence knowledge', 'observed_sections': ['3. Milestone question and approval gates', '4. Implementation Package Compiler', '7. Returned-results review order and verdicts', '10. Change request and feedback transport', '11. Source-retained detail checks (retrieve only when applicable)', '12. Game-agnostic compilation boundary'], 'finding': 'Preserves v3 design method and human authority, separate milestone/plan approval, design versus implementation, pinned package/handoff, retrieved raw evidence and human closure. Source-retained detail checks are conditional; historical records are outside Instructions/knowledge uploads and current approved artifacts supply project defaults.'},
    'limits': ['No source content changed.', 'No tests, runtime discovery, package checker, assembler, runner, installer or game process ran.', 'No later batch content retrieved.', 'No configured host, Unity, adoption or full-package validation claim.']
}
assert not records[0]['selected_knowledge'] and records[0]['preserved_reference']
assert all(x['selected_knowledge'] and not x['preserved_reference'] for x in records[1:])
result = {'task': 'B05d', 'input_head': data['head'], 'status': 'PASS', 'assigned': 3, 'reconciled': 3, 'missing': [], 'mismatched': [], 'tests': 'NOT_RUN', 'command_exit_status': 0, 'later_batches': 'NOT_STARTED', 'candidate_implementation_changes': False}
fetch = {'task': 'B05d', 'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree'], 'checkpoint_blob': data['checkpoint_sha'], 'incorporation_status_blob': data['status_sha'], 'B05c_dependency_blob': data['dependency_sha'], 'B05c_dependency_input_head': dep['input_head'], 'content_reads': [{'path': x['path'], 'encoding': x['encoding'], 'returned_blob': x['sha'], 'url': x['display_url'], 'tree': x['tree']} for x in data['files']], 'next_batch_metadata_only': next(x for x in dep['follow_up_batches'] if x['id'] == 'B05e1'), 'tree_truncated': False}
for name, value in [('SOURCES.json', sources), ('RESULT.json', result), ('FINDINGS.json', findings), ('FETCH_METADATA.json', fetch)]:
    (out / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
print('PASS reference-only / selected-knowledge scope reconciliation; no source-game defaults imported')
print('B05d PASS: 3/3 identities. Tests NOT_RUN; later batches NOT_STARTED.')
