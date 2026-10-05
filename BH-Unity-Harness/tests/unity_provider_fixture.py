#!/usr/bin/env python3
"""SYNTHETIC provider process for the BH protocol, not a Unity integration.

Writes raw observations only. The real harness creates and judges receipts.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys
import time

p = argparse.ArgumentParser(description=__doc__)
for name in ('action', 'request', 'project', 'job-id', 'mode'):
    p.add_argument('--' + name, required=True)
a = p.parse_args()
r = json.loads(Path(a.request).read_text(encoding='utf-8'))
root = Path(a.project)
assert r['project_path'] == str(root)
assert (root / '.bh/SYNTHETIC_FIXTURE').is_file()
outdir = Path(r['artifact_directory'])
trace = outdir / 'provider-calls.json'
calls = json.loads(trace.read_text()) if trace.exists() else []
calls.append(a.action)
trace.write_text(json.dumps(calls))
result = None
state, job = ('ready', None) if a.action == 'probe' else ('accepted', 'SYNTHETIC-JOB')
if a.mode == 'probe-unavailable' and a.action == 'probe':
    state = 'unavailable'
if a.action == 'submit' and a.mode == 'lost-submit':
    sys.exit(7)
if a.action == 'status':
    assert a.job_id == 'SYNTHETIC-JOB'
    state = 'completed'
    if a.mode in ('busy', 'unavailable', 'interrupted', 'failed', 'cancelled', 'running'):
        state = a.mode
    elif a.mode == 'timeout':
        time.sleep(3)
    elif a.mode == 'nonzero':
        sys.exit(7)
    elif a.mode == 'oversized':
        print('x' * 10000)
        sys.exit(0)
    elif a.mode == 'malformed':
        print('{not json}')
        sys.exit(0)
    if state == 'completed':
        s = r['spec']
        operation = r['operation']
        if operation == 'search':
            result = {'query': s['query'], 'provider': s['provider'], 'scope_paths': s['scope_paths'],
                      'complete': a.mode != 'partial', 'total_count': 2 if a.mode == 'partial' else 1,
                      'items': [{'id': 'SYNTHETIC-OBJECT', 'kind': 'fixture', 'path': 'Source/value.json',
                                 'properties': {key: 1 for key in s['properties']}}]}
        elif operation == 'audit':
            header = ['Category', 'Severity', 'Areas', 'Description', 'RelativePath', 'Line', 'DescriptorId', 'Recommendation']
            rows = [['Code', 'Warning', 'SYNTHETIC', 'Synthetic finding', 'Source/value.json', '1', 'SYN-01', 'Review']]
            if a.mode != 'new-finding':
                rows = []
            with (outdir / 'audit.csv').open('w', newline='', encoding='utf-8') as stream:
                writer = csv.writer(stream); writer.writerow(header); writer.writerows(rows)
            result = {key: s[key] for key in ('categories', 'scope_paths', 'rules_fingerprint')}
            result.update(csv_file='audit.csv', issue_count=len(rows), rules_present=True,
                          coverage_complete=True, analyzed_count=1)
        elif operation == 'smoke':
            capture = None
            if s['capture_source'] != 'none':
                payload = b'SYNTHETIC capture bytes, not a real screenshot'
                (outdir / 'capture.bin').write_bytes(payload)
                capture = {'path': 'capture.bin', 'sha256': hashlib.sha256(payload).hexdigest(), 'source': s['capture_source']}
            result = {'frame_before': 1, 'frame_after': 1 if a.mode == 'frozen' else 2,
                      'conditions': {key: True for key in s['condition_ids']}, 'error_count': 0, 'capture': capture}
        elif operation == 'assets':
            result = {'assets': [{'path': asset['path'], 'persisted': True, 'reloaded': a.mode != 'unsaved',
                                 'subassets': asset['subassets'], 'duplicate_count': 0,
                                 'bindings': {key: {**value, 'observed': True} for key, value in asset['bindings'].items()},
                                 'behaviors': {key: True for key in asset['behavior_ids']}} for asset in s['assets']]}
        else:
            result = {'entries': [{'key': key, 'locale': locale, 'value': 'SYNTHETIC translation'}
                                  for key in s['keys'] for locale in s['locales']],
                      'converted_code_sites': s['code_sites']}
            if a.mode == 'missing-locale':
                result['entries'].pop()
        if a.mode == 'mutate':
            (root / 'Source/value.json').write_text('{"value":2}')
v = {'protocol': 'BH-UNITY-PROVIDER-1', 'project_id': r['project_id'], 'project_path': r['project_path'],
     'run_id': r['run_id'], 'request_sha256': r['request_sha256'], 'session_id': r['session_id'],
     'capabilities_sha256': r['capabilities_sha256'], 'capabilities': ['observe'],
     'job_id': job, 'state': state, 'result': result}
if a.action == 'status':
    for mode, key in [('wrong-job', 'job_id'), ('wrong-session', 'session_id'),
                      ('wrong-project', 'project_id'), ('wrong-run', 'run_id'),
                      ('wrong-request', 'request_sha256'), ('wrong-capabilities', 'capabilities_sha256')]:
        if a.mode == mode:
            v[key] = 'SYNTHETIC-WRONG'
if a.mode == 'missing-capability':
    v['capabilities'] = []
print(json.dumps(v))
