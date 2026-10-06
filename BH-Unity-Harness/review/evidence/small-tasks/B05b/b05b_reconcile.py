import ast
import datetime
import hashlib
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent
data = json.loads((root / 'b05b-input.json').read_text())
assert data['harness_tree']['truncated'] is False
tree = {e['path']: e for e in data['harness_tree']['tree']}
prior = next(b for b in data['prior_inventory']['follow_up_batches'] if b['id'] == 'B05b')
assert sorted(data['files']) == sorted(prior['paths']) and len(data['files']) == 8
old = {r['path']: r for r in prior['tree_metadata']}
work = root / 'b05b-work'
work.mkdir(exist_ok=True)
rows, facts = [], []
for path in prior['paths']:
    fetched = data['files'][path]
    assert fetched['encoding'] == 'utf-8'
    raw = fetched['content'].encode('utf-8')
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    assert blob == fetched['sha'] == tree[path]['sha'] == old[path]['git_blob_sha'], path
    assert len(raw) == tree[path]['size'] == old[path]['bytes'], path
    dest = work / 'BH-Unity-Harness' / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    rows.append({'path': path, 'git_blob_sha': blob, 'sha256': sha256, 'bytes': len(raw),
                 'origin': 'Pinned GitHub retrieval; bytes checked against current immutable tree and B05a batch metadata'})
    parsed = ast.parse(raw, filename=path)
    imports = [{'line': n.lineno, 'statement': ast.get_source_segment(fetched['content'], n)}
               for n in ast.walk(parsed) if isinstance(n, (ast.Import, ast.ImportFrom))]
    interesting = {'read_text', 'read_bytes', 'load_json', 'glob', 'rglob', 'copytree', 'copyfile', 'spec_from_file_location', 'open', 'is_file', 'exists', 'read', 'safe', 'file_hash', 'parse', 'snapshot', 'source_hashes'}
    calls = []
    for n in ast.walk(parsed):
        if isinstance(n, ast.Call):
            name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id if isinstance(n.func, ast.Name) else ''
            if name in interesting:
                calls.append({'line': n.lineno, 'expression': ast.get_source_segment(fetched['content'], n)})
    facts.append({'path': path, 'imports': sorted(imports, key=lambda r: r['line']),
                  'file_and_tool_calls': sorted(calls, key=lambda r: r['line'])})
    print('MATCH ' + path + ' bytes=' + str(len(raw)) + ' git_blob=' + blob + ' sha256=' + sha256)
    print('AST ONLY: source parsed; module not imported or executed.')
sources = {'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree']['sha'], 'files': rows}
(work / 'SOURCES.json').write_text(json.dumps(sources, indent=2) + '\n')
(work / 'SOURCE_FACTS.json').write_text(json.dumps({'task': 'B05b', 'input_head': data['head'], 'method': 'ast.parse only; no module import or invocation', 'modules': facts}, indent=2) + '\n')
report = {'task': 'B05b', 'result': 'PASS_SOURCE_RECONCILIATION', 'input_head': data['head'],
          'command': 'python3 b05b_reconcile.py > b05b-reconciliation.log 2>&1', 'working_directory': str(root),
          'finished_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'exit_status': 0,
          'source_count': len(rows), 'matched_count': len(rows), 'prior_batch_metadata_matches': len(rows),
          'missing_sources': [], 'mismatched_sources': [], 'ast_parsed_sources': len(facts),
          'runtime_discovery': 'NOT_RUN', 'tests_executed': 0, 'package_checker': 'NOT_RUN', 'assembler': 'NOT_RUN', 'run_tests': 'NOT_RUN',
          'follow_up_byte_reconciliation': 'NOT_STARTED', 'environment': {'python': sys.version},
          'scope': 'Only eight requested support/tool source files reconciled and statically reviewed; no complete package-byte closure or test pass claim.'}
(work / 'RESULT.json').write_text(json.dumps(report, indent=2) + '\n')
print('PASS: 8/8 source identities match current tree and B05a metadata; all eight AST-parsed without import.')
print('Tests, package checker, assembler, runner and next input batch NOT_RUN.')
