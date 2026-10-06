import ast
import datetime
import hashlib
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent
data = json.loads((root / 'b05a-input.json').read_text())
assert data['harness_tree']['truncated'] is False
tree = {e['path']: e for e in data['harness_tree']['tree']}
paths = ['tests/test_package.py', 'tests/test_game_agnostic.py', 'tests/test_review_amendments.py']
assert sorted(data['files']) == sorted(paths)
work = root / 'b05a-work'
work.mkdir(exist_ok=True)
rows, facts = [], []
for path in paths:
    fetched = data['files'][path]
    assert fetched['encoding'] == 'utf-8'
    raw = fetched['content'].encode('utf-8')
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()
    assert blob == fetched['sha'] == tree[path]['sha'], path
    assert len(raw) == tree[path]['size'], path
    dest = work / 'BH-Unity-Harness' / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    rows.append({'path': path, 'git_blob_sha': blob, 'sha256': sha256, 'bytes': len(raw),
                 'origin': 'Pinned GitHub UTF-8 retrieval; exact bytes checked against immutable Git tree'})
    parsed = ast.parse(raw, filename=path)
    imports = [{'line': n.lineno, 'statement': ast.get_source_segment(fetched['content'], n)}
               for n in ast.walk(parsed) if isinstance(n, (ast.Import, ast.ImportFrom))]
    cases = []
    for cls in parsed.body:
        if isinstance(cls, ast.ClassDef):
            for fn in cls.body:
                if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and fn.name.startswith('test_'):
                    cases.append({'candidate_id': pathlib.Path(path).stem + '.' + cls.name + '.' + fn.name, 'line': fn.lineno})
    calls = []
    interesting = {'read_text', 'read_bytes', 'load_json', 'glob', 'rglob', 'copytree', 'spec_from_file_location', 'module', 'load_tool', 'distribution', 'check', 'assemble', 'source_hashes'}
    for n in ast.walk(parsed):
        if isinstance(n, ast.Call):
            name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id if isinstance(n.func, ast.Name) else ''
            if name in interesting:
                calls.append({'line': n.lineno, 'expression': ast.get_source_segment(fetched['content'], n)})
    facts.append({'path': path, 'imports': sorted(imports, key=lambda r: r['line']),
                  'declared_test_method_count': len(cases), 'static_case_candidates': sorted(cases, key=lambda r: r['candidate_id']),
                  'file_and_tool_calls': sorted(calls, key=lambda r: r['line'])})
    print('MATCH ' + path + ' bytes=' + str(len(raw)) + ' git_blob=' + blob + ' sha256=' + sha256)
    print('AST ONLY: ' + str(len(cases)) + ' declared test methods; module not imported or executed.')
sources = {'input_head': data['head'], 'root_tree': data['root_tree'], 'harness_tree': data['harness_tree']['sha'], 'files': rows}
(work / 'SOURCES.json').write_text(json.dumps(sources, indent=2) + '\n')
(work / 'SOURCE_FACTS.json').write_text(json.dumps({'task': 'B05a', 'input_head': data['head'], 'method': 'ast.parse only; no module import or unittest discovery', 'modules': facts}, indent=2) + '\n')
total = sum(m['declared_test_method_count'] for m in facts)
report = {'task': 'B05a', 'result': 'PASS_SOURCE_RECONCILIATION', 'input_head': data['head'],
          'command': 'python3 b05a_reconcile.py > b05a-reconciliation.log 2>&1', 'working_directory': str(root),
          'finished_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'exit_status': 0,
          'source_count': len(rows), 'matched_count': len(rows), 'missing_sources': [], 'mismatched_sources': [],
          'static_declared_test_methods': total, 'historical_recorded_total': 44, 'static_total_differs_from_history': total != 44,
          'runtime_discovery': 'NOT_RUN', 'tests_executed': 0, 'follow_up_byte_reconciliation': 'NOT_STARTED',
          'environment': {'python': sys.version}, 'scope': 'Only three requested test source files reconciled; AST inventory is not a test pass or transitive input verification.'}
(work / 'RESULT.json').write_text(json.dumps(report, indent=2) + '\n')
print('PASS: 3/3 source identities; ' + str(total) + ' declared methods versus historical 44; runtime discovery/tests NOT_RUN.')
