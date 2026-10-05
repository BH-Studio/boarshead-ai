"""Bounded Unity observation reducers. Provider data is evidence, never authority.

Original BH code; no vendor runtime or skill code is embedded. These reducers do
not invoke Unity, infer coverage from zero findings, or grant human acceptance.
"""
from __future__ import annotations
import csv
import io
import math
from collections import Counter
from pathlib import Path
import bh

MAX_BYTES = 1024 * 1024
CSV_COLUMNS = ('Category', 'Severity', 'Areas', 'Description', 'RelativePath',
               'Line', 'DescriptorId', 'Recommendation')


def fields(value, names, label):
    bh.require(type(value) is dict and set(value) == set(names), label + ': wrong fields')
    return value


def text(value, label, limit=2048, empty=False):
    bh.require(type(value) is str and len(value) <= limit and (empty or value.strip()),
               label + ': invalid text')
    bh.require('\x00' not in value, label + ': NUL rejected')
    return value


def integer(value, label, minimum=0, maximum=1000000):
    bh.require(type(value) is int and minimum <= value <= maximum, label + ': invalid integer')
    return value


def boolean(value, label):
    bh.require(type(value) is bool, label + ': expected boolean')
    return value


def strings(value, label, minimum=0, maximum=256):
    bh.require(type(value) is list and minimum <= len(value) <= maximum, label + ': invalid list')
    for item in value:
        text(item, label)
    bh.require(len(value) == len(set(value)), label + ': duplicate entry')
    return value


def primitive(value):
    bh.require(type(value) in (str, bool, int, float, type(None)), 'Only scalar properties are supported')
    if isinstance(value, str):
        text(value, 'property', empty=True)
    if type(value) in (float, int):
        bh.require(math.isfinite(value), 'Nonfinite property')
    return value


def run_file(root, directory, name, expected_hash=None, max_bytes=MAX_BYTES):
    """Only a regular, current-run direct child; never a provider-chosen absolute path."""
    text(name, 'artifact name', 200)
    bh.require(Path(name).name == name, 'Artifact must be a simple current-run filename')
    rel = (directory.relative_to(root) / name).as_posix()
    path = bh.safe(root, rel)
    bh.require(path.is_file() and 0 < path.stat().st_size <= max_bytes, 'Missing/empty/oversized artifact')
    if expected_hash is not None:
        bh.require(bh.file_hash(path) == expected_hash, 'Artifact digest mismatch')
    return path


def read_auditor_csv(path):
    bh.no_links(path)
    bh.require(Path(path).is_file() and Path(path).stat().st_size <= MAX_BYTES, 'CSV missing or too large')
    raw = Path(path).read_text(encoding='utf-8-sig')
    reader = csv.reader(io.StringIO(raw), strict=True)
    header = next(reader, None)
    bh.require(header is not None and len(header) == len(set(header))
               and set(header) == set(CSV_COLUMNS), 'Auditor CSV header mismatch')
    rows = []
    for row in reader:
        bh.require(len(rows) < 10000 and len(row) == len(header), 'CSV row/count mismatch')
        item = dict(zip(header, row))
        for key in CSV_COLUMNS:
            text(item[key], 'CSV ' + key, empty=key in ('Areas', 'RelativePath', 'Line', 'Recommendation'))
        if item['RelativePath']:
            bh.portable(item['RelativePath'])
        bh.require(not item['Line'] or item['Line'].isdigit(), 'Invalid CSV line')
        rows.append(tuple(item[key] for key in CSV_COLUMNS))
    return rows


def audit_report(spec, value, root, outdir):
    fields(spec, ('categories', 'scope_paths', 'rules_fingerprint', 'baseline'), 'audit spec')
    fields(value, ('csv_file', 'issue_count', 'categories', 'scope_paths', 'rules_fingerprint',
                   'rules_present', 'coverage_complete', 'analyzed_count'), 'audit result')
    strings(spec['categories'], 'categories', 1)
    strings(spec['scope_paths'], 'scope', 1)
    for path in spec['scope_paths']:
        bh.portable(path)
    text(spec['rules_fingerprint'], 'rules fingerprint')
    for key in ('categories', 'scope_paths', 'rules_fingerprint'):
        bh.require(value[key] == spec[key], 'Audit scope/rules differ: ' + key)
    bh.require(boolean(value['rules_present'], 'rules') and
               boolean(value['coverage_complete'], 'coverage'), 'Audit rules or coverage unavailable')
    integer(value['analyzed_count'], 'analyzed count', 1)
    rows = read_auditor_csv(run_file(root, outdir, value['csv_file']))
    bh.require(len(rows) == integer(value['issue_count'], 'issue count'), 'Audit issue count mismatch')
    bh.require(all(row[0] in spec['categories'] for row in rows), 'Undeclared audit category')
    baseline_ref = spec['baseline']
    fields(baseline_ref, ('path', 'sha256'), 'baseline reference')
    baseline_path = bh.safe(root, baseline_ref['path'])
    bh.require(bh.file_hash(baseline_path) == baseline_ref['sha256'], 'Baseline manifest changed')
    baseline = bh.load_json(baseline_path)
    fields(baseline, ('source', 'categories', 'scope_paths', 'rules_fingerprint', 'analyzed_count',
                      'coverage_complete', 'report'), 'baseline')
    bh.require(baseline['source'] == 'unity-project-auditor', 'Wrong baseline source')
    for key in ('categories', 'scope_paths', 'rules_fingerprint'):
        bh.require(baseline[key] == spec[key], 'Baseline coverage/rules differ')
    integer(baseline['analyzed_count'], 'baseline analyzed count', 1)
    bh.require(baseline['coverage_complete'] is True, 'Baseline coverage incomplete')
    fields(baseline['report'], ('path', 'sha256'), 'baseline CSV reference')
    old_path = bh.safe(root, baseline['report']['path'])
    bh.require(bh.file_hash(old_path) == baseline['report']['sha256'], 'Baseline CSV changed')
    old_rows = read_auditor_csv(old_path)
    bh.require(all(row[0] in spec['categories'] for row in old_rows), 'Undeclared baseline category')
    old, now = Counter(old_rows), Counter(rows)
    added, removed = now - old, old - now
    groups = Counter((row[0], row[6], row[1]) for row in rows)
    return ({'coverage_complete': True, 'analyzed_count': value['analyzed_count'],
             'current_findings': len(rows), 'new_findings': sum(added.values()),
             'resolved_findings': sum(removed.values())},
            {'groups': [{'category': k[0], 'descriptor': k[1], 'severity': k[2], 'count': v}
                        for k, v in groups.most_common(10)],
             'group_count': len(groups), 'new_examples': [dict(zip(CSV_COLUMNS, r))
                                                        for r in list(added)[:10]],
             'raw_csv': {'path': value['csv_file'], 'sha256': bh.file_hash(outdir / value['csv_file'])},
             'limitation': 'Grouped summary is not all rows. Original CSV retained; findings do not authorize repairs.'})


def search_report(spec, value, root, outdir):
    fields(spec, ('query', 'provider', 'scope_paths', 'properties', 'max_items'), 'search spec')
    fields(value, ('query', 'provider', 'scope_paths', 'complete', 'total_count', 'items'), 'search result')
    text(spec['query'], 'query'); text(spec['provider'], 'provider')
    strings(spec['scope_paths'], 'scope paths', 1); strings(spec['properties'], 'properties')
    maximum = integer(spec['max_items'], 'maximum items', 1, 200)
    for path in spec['scope_paths']:
        bh.portable(path)
    for key in ('query', 'provider', 'scope_paths'):
        bh.require(value[key] == spec[key], 'Search identity/scope mismatch: ' + key)
    total = integer(value['total_count'], 'total count')
    complete = boolean(value['complete'], 'search completeness')
    bh.require(type(value['items']) is list and len(value['items']) <= maximum, 'Search result cap exceeded')
    bh.require(total >= len(value['items']) and (not complete or total == len(value['items'])),
               'Search completeness/count conflict')
    identities = set()
    for item in value['items']:
        fields(item, ('id', 'kind', 'path', 'properties'), 'search item')
        text(item['id'], 'object id'); text(item['kind'], 'object kind')
        bh.portable(item['path'])
        bh.require(any(bh.below(item['path'], p) for p in spec['scope_paths']), 'Object outside search scope')
        bh.require(item['id'] not in identities, 'Duplicate object identity'); identities.add(item['id'])
        bh.require(type(item['properties']) is dict and set(item['properties']) == set(spec['properties']),
                   'Missing or extra requested property')
        for val in item['properties'].values():
            primitive(val)
    return ({'coverage_complete': complete, 'match_count': total, 'returned_count': len(value['items'])},
            {'query': spec['query'], 'provider': spec['provider'], 'scope_paths': spec['scope_paths'],
             'examples': value['items'][:10], 'summary_truncated': len(value['items']) > 10,
             'limitation': 'No matches only means absence within the completed declared search, not a dependency audit.'})


def smoke_report(spec, value, root, outdir):
    fields(spec, ('condition_ids', 'capture_source', 'minimum_frame_advance'), 'smoke spec')
    fields(value, ('frame_before', 'frame_after', 'conditions', 'error_count', 'capture'), 'smoke result')
    ids = strings(spec['condition_ids'], 'condition ids', 1, 64)
    step = integer(spec['minimum_frame_advance'], 'minimum advance', 1)
    before = integer(value['frame_before'], 'frame before', 0, 2**63-1)
    after = integer(value['frame_after'], 'frame after', 0, 2**63-1)
    fields(value['conditions'], ids, 'observed conditions')
    for val in value['conditions'].values():
        boolean(val, 'condition')
    errors = integer(value['error_count'], 'error count')
    bh.require(spec['capture_source'] in ('screen', 'camera', 'none'), 'Unknown capture source')
    if spec['capture_source'] == 'none':
        bh.require(value['capture'] is None, 'Unrequested capture')
    else:
        fields(value['capture'], ('path', 'sha256', 'source'), 'capture')
        bh.require(value['capture']['source'] == spec['capture_source'], 'Wrong capture source')
        run_file(root, outdir, value['capture']['path'], value['capture']['sha256'], 8 * MAX_BYTES)
    return ({'frames_advanced': after - before >= step,
             'conditions_met': all(value['conditions'].values()), 'error_count': errors},
            {'conditions': value['conditions'], 'capture': value['capture'],
             'limitation': 'Frame advancement and a capture do not certify game feel or human acceptance.'})


def asset_report(spec, value, root, outdir):
    fields(spec, ('assets',), 'asset spec'); fields(value, ('assets',), 'asset result')
    bh.require(type(spec['assets']) is list and 0 < len(spec['assets']) <= 100, 'Empty/large asset roster')
    bh.require(type(value['assets']) is list and len(value['assets']) <= 100, 'Invalid observed assets')
    expected = {}
    for asset in spec['assets']:
        fields(asset, ('path', 'subassets', 'bindings', 'behavior_ids'), 'asset requirement')
        bh.portable(asset['path']); strings(asset['subassets'], 'subassets'); strings(asset['behavior_ids'], 'behaviors')
        bh.require(type(asset['bindings']) is dict, 'Binding requirements must be a mapping')
        for key, binding in asset['bindings'].items():
            text(key, 'binding id'); fields(binding, ('target', 'method', 'call_state'), 'binding requirement')
            for val in binding.values(): text(val, 'binding property')
        bh.require(asset['path'] not in expected, 'Duplicate asset requirement'); expected[asset['path']] = asset
    observed = {}
    for asset in value['assets']:
        fields(asset, ('path', 'persisted', 'reloaded', 'subassets', 'bindings', 'behaviors', 'duplicate_count'), 'asset observation')
        bh.require(asset['path'] in expected and asset['path'] not in observed, 'Unknown/duplicate observed asset')
        observed[asset['path']] = asset
        boolean(asset['persisted'], 'persisted'); boolean(asset['reloaded'], 'reloaded')
        strings(asset['subassets'], 'observed subassets'); integer(asset['duplicate_count'], 'duplicate count')
        bh.require(type(asset['bindings']) is dict and type(asset['behaviors']) is dict, 'Invalid behavior/binding result')
        for binding in asset['bindings'].values():
            fields(binding, ('target', 'method', 'call_state', 'observed'), 'binding observation')
            for key in ('target', 'method', 'call_state'): text(binding[key], key, empty=True)
            boolean(binding['observed'], 'binding observed')
        for val in asset['behaviors'].values(): boolean(val, 'behavior')
    failures = []
    for path, requirement in expected.items():
        asset = observed.get(path)
        ok = asset is not None
        if ok:
            ok = (asset['persisted'] and asset['reloaded'] and not asset['duplicate_count']
                  and set(requirement['subassets']) <= set(asset['subassets']))
            for key, binding in requirement['bindings'].items():
                actual = asset['bindings'].get(key, {})
                ok = ok and actual.get('observed') is True and all(actual.get(k) == v for k, v in binding.items())
            ok = ok and all(asset['behaviors'].get(key) is True for key in requirement['behavior_ids'])
        if not ok: failures.append(path)
    return ({'required_assets': len(expected), 'observed_assets': len(observed), 'asset_failures': len(failures)},
            {'failed_assets': failures, 'limitation': 'Requires a reviewed provider measuring persisted/reloaded state, not in-memory assertions alone.'})


def localization_report(spec, value, root, outdir):
    fields(spec, ('keys', 'locales', 'code_sites'), 'localization spec')
    fields(value, ('entries', 'converted_code_sites'), 'localization result')
    keys = strings(spec['keys'], 'keys', 1); locales = strings(spec['locales'], 'locales', 1, 64)
    sites = strings(spec['code_sites'], 'code sites')
    converted = strings(value['converted_code_sites'], 'converted code sites')
    bh.require(set(converted) <= set(sites), 'Unknown converted code site')
    bh.require(type(value['entries']) is list and len(value['entries']) <= 16384, 'Invalid/large entry list')
    expected = {(key, locale) for key in keys for locale in locales}
    observed = {}
    for entry in value['entries']:
        fields(entry, ('key', 'locale', 'value'), 'localized entry')
        pair = (text(entry['key'], 'key'), text(entry['locale'], 'locale'))
        bh.require(pair in expected and pair not in observed, 'Unknown/duplicate localization entry')
        observed[pair] = text(entry['value'], 'translation', 8000, empty=True)
    gaps = sorted(pair for pair in expected if not observed.get(pair, '').strip())
    return ({'required_entries': len(expected), 'observed_entries': len(observed),
             'missing_or_empty_entries': len(gaps), 'unconverted_code_sites': len(set(sites) - set(converted))},
            {'gap_count': len(gaps), 'gap_examples': gaps[:10],
             'unconverted_code_sites': sorted(set(sites) - set(converted)),
             'limitation': 'Completeness is not translation quality, glyph coverage, or visual layout acceptance.'})


REDUCERS = {'search': search_report, 'audit': audit_report, 'smoke': smoke_report,
            'assets': asset_report, 'localization': localization_report}


def reduce_result(operation, spec, value, root, outdir):
    bh.require(operation in REDUCERS, 'Unsupported Unity observation')
    return REDUCERS[operation](spec, value, Path(root), Path(outdir))
