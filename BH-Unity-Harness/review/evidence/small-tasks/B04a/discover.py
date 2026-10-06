import json
import pathlib
import sys
import unittest

root = pathlib.Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(root / 'BH-Unity-Harness/tests'))
import test_efficiency_views

def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item.id()

ids = sorted(flatten(unittest.defaultTestLoader.loadTestsFromModule(test_efficiency_views)))
assert len(ids) == len(set(ids)), 'Duplicate case IDs'
parts = [{'id': 'B04a' if len(ids) <= 20 else 'B04a' + chr(ord('a') + i // 20),
          'case_ids': ids[i:i+20]} for i in range(0, len(ids), 20)]
plan = {'module': 'tests/test_efficiency_views.py', 'order': 'Unicode lexical order of full unittest case ID',
        'observed_count': len(ids), 'historical_count': 11, 'count_changed': len(ids) != 11,
        'partition_limit': 20, 'partitions': parts}
(root / 'PARTITIONS.json').write_text(json.dumps(plan, indent=2) + '\n')
print('Discovery only; no tests executed.')
print('Observed efficiency views cases:', len(ids), '; historical count: 11; changed:', plan['count_changed'])
for part in parts:
    print(part['id'] + ' (' + str(len(part['case_ids'])) + ' cases)')
    for case_id in part['case_ids']:
        print('  ' + case_id)
