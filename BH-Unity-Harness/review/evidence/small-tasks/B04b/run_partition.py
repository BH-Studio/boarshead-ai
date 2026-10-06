import datetime
import hashlib
import json
import pathlib
import platform
import subprocess
import sys
import time
import unittest

root = pathlib.Path(__file__).resolve().parent
sources = json.loads((root / 'SOURCES.json').read_text())
plan = json.loads((root / 'PARTITIONS.json').read_text())
part = next(p for p in plan['partitions'] if p['id'] == 'B04b')
assert 1 <= len(part['case_ids']) <= 20
sys.dont_write_bytecode = True

def fingerprint():
    rows = []
    for item in sources['files']:
        raw = (root / 'BH-Unity-Harness' / item['path']).read_bytes()
        observed = {'path': item['path'], 'sha256': hashlib.sha256(raw).hexdigest(),
                    'git_blob_sha': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest(),
                    'bytes': len(raw)}
        assert all(observed[k] == item[k] for k in ('sha256', 'git_blob_sha', 'bytes')), item['path']
        rows.append(observed)
    return rows

before = fingerprint()
sys.path.insert(0, str(root / 'BH-Unity-Harness/tests'))
suite = unittest.defaultTestLoader.loadTestsFromNames(part['case_ids'])
assert suite.countTestCases() == len(part['case_ids'])
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
print('B04b pinned head: ' + sources['input_head'], flush=True)
print('Selected partition: 20 or fewer exact cases from PARTITIONS.json', flush=True)
for case_id in part['case_ids']:
    print('CASE ' + case_id, flush=True)
clock = time.monotonic()
result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
elapsed = time.monotonic() - clock
after = fingerprint()
assert before == after, 'Source mutation'
exit_status = 0 if result.wasSuccessful() and not result.skipped and result.testsRun == len(part['case_ids']) else 1
report = {'task': 'B04b', 'result': 'PASS' if exit_status == 0 else 'FAIL',
          'input_head': sources['input_head'], 'command': 'python3 run_partition.py > RAW.log 2>&1',
          'working_directory': str(root), 'started_at_utc': started,
          'finished_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'elapsed_seconds': elapsed, 'exit_status': exit_status,
          'selected_case_ids': part['case_ids'], 'discovered_count': plan['observed_count'],
          'tests_run': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors),
          'skips': len(result.skipped), 'expected_failures': len(result.expectedFailures),
          'unexpected_successes': len(result.unexpectedSuccesses),
          'source_before': before, 'source_after': after, 'sources_unchanged': before == after,
          'environment': {'python': sys.version, 'interpreter': str(pathlib.Path(sys.executable).resolve()),
                          'interpreter_sha256': hashlib.sha256(pathlib.Path(sys.executable).read_bytes()).hexdigest(),
                          'platform': platform.platform(),
                          'git_version': subprocess.check_output(['git', '--version'], text=True).strip()},
          'scope': 'Offline synthetic efficiency runtime fixtures; only the first lexical partition. B04c and other modules NOT_RUN. Native Unity/Windows/adoption NOT_RUN.'}
(root / 'RESULT.json').write_text(json.dumps(report, indent=2) + '\n')
print('B04b result: ' + report['result'] + '; source hashes unchanged; exit status: ' + str(exit_status), flush=True)
sys.exit(exit_status)
