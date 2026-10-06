#!/usr/bin/env python3
"""Compact projections of BH records; never an alternative approval authority.

context/schema/draft-proposal write nothing. return uses the existing authorized
record writer under its lock, then writes a derived view and a history index.
"""
from __future__ import annotations
import argparse
import copy
import json
import sys
import bh

sys.dont_write_bytecode = True


def schema_view(schema: dict, name: str) -> dict:
    """Return a definition and the complete transitive local reference closure."""
    bh.require(name in schema['$defs'], 'Unknown schema definition: ' + name)
    found = {}
    def visit(value):
        if isinstance(value, dict):
            ref = value.get('$ref')
            if ref:
                bh.require(ref.startswith('#/$defs/'), 'Nonlocal schema reference')
                key = ref[len('#/$defs/'):]
                bh.require(key in schema['$defs'], 'Missing referenced definition: ' + key)
                if key not in found:
                    found[key] = schema['$defs'][key]
                    visit(found[key])
            for key, child in value.items():
                if key != '$ref':
                    visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit({'$ref': '#/$defs/' + name})
    return {'$ref': '#/$defs/' + name, '$defs': dict(sorted(found.items()))}


def snapshot_summary(snapshot: dict) -> dict:
    return {key: value for key, value in snapshot.items() if key != 'files'}


def context_view(h) -> dict:
    """All decision-bearing fields remain; the bulk path/hash roster does not."""
    state = h.state()
    h.artifact(state['handoff'])
    handoff, criteria, overlay = h.handoff(state['handoff']['path'])
    snap = bh.snapshot(h.root)
    plan = h.load_plan(state) if state['plan'] else None
    if plan:
        h.scope(plan, snap)
    approval = None
    if state['approval']:
        bh.require(plan is not None, 'Approval without a plan')
        h.artifact(state['approval'])
        approval = h.read(state['approval']['path'], 'approval')
        h.approval(approval, 'plan', bh.digest(plan), state['task_id'])
    scores, refs, gaps = h.audit_results(state, snap)
    projected_plan = copy.deepcopy(plan)
    if projected_plan:
        projected_plan['baseline'] = snapshot_summary(projected_plan['baseline'])
    return {
        'format': 'BH-CONTEXT-VIEW-1', 'authority': 'DERIVED_VIEW_NOT_AUTHORIZATION',
        'project_id': state['project_id'], 'task_id': state['task_id'],
        'synthetic': state['synthetic'], 'recorded_phase': state['phase'],
        'state_sha256': bh.digest(state), 'current_source': snapshot_summary(snap),
        'handoff_ref': state['handoff'],
        'handoff': {k: v for k, v in handoff.items() if k != 'artifacts'},
        'artifact_manifest': {'count': len(handoff['artifacts']), 'ref': state['handoff']},
        'overlay': overlay, 'plan_ref': state['plan'], 'plan': projected_plan,
        'plan_approval_subject': bh.digest(plan) if plan else None,
        'plan_approval': approval,
        'acceptance': [{**criterion, 'current_status': scores[key], 'receipt_refs': refs[key]}
                       for key, criterion in criteria.items()],
        'claims_not_evidence': state['claims'], 'recorded_blockers': state['blockers'],
        'current_evidence_gaps': gaps, 'pending_run': state['pending_run'],
        'attempts_used': state['counters'], 'budgets': h.config['budgets'],
        'next_action': state['next_action'],
        'limits': ['Inspect genuine approval sources; records do not authenticate a human.',
                   'Human acceptance is not evaluated by this context projection.',
                   'Full immutable records remain available by the exact references above.']}


def draft_proposal(h, path: str) -> dict:
    """Generate mechanical fields only; unresolved content deliberately blocks plan."""
    handoff, criteria, _ = h.handoff(path, executable=False)
    value = {
        'version': bh.VERSION, 'project_id': handoff['project_id'],
        'task_id': handoff['task_id'],
        'steps': [{'id': 'STEP-01', 'description': 'UNRESOLVED: supply actual bounded implementation steps',
                   'paths': handoff['allowed_paths'], 'ac_ids': list(criteria)}],
        'risks': handoff['risk_controls'],
        'reconciliation': ['UNRESOLVED: inspect current code, test dependencies and tool bindings'],
        'tool_review_ref': 'UNRESOLVED',
        'scope_conflicts': ['Generated draft only; reconcile every placeholder before requesting plan approval'],
        'next_action': 'Supply substantive decisions, validate, plan, then request genuine human approval'}
    bh.validate(value, 'proposal', h.schema)
    return value


def return_view(h) -> dict:
    """Write the original return plus a bounded view; keep history separately."""
    result = h.return_report()
    value = h.read(result['return'], 'return')
    current = {name for ac in value['acceptance'] for name in ac['receipt_refs']}
    history_path = f'.bh/exports/{value["task_id"]}/HISTORY_INDEX.json'
    bh.atomic_json(bh.safe(h.root, history_path), {
        'format': 'BH-HISTORY-INDEX-1', 'project_id': value['project_id'],
        'task_id': value['task_id'], 'receipts': value['receipts']})
    view = {**value, 'format': 'BH-RETURN-VIEW-1',
            'source_snapshot': snapshot_summary(value['source_snapshot']),
            'receipts': [r for r in value['receipts'] if r['path'] in current],
            'full_return': {'path': result['return'],
                            'sha256': bh.file_hash(bh.safe(h.root, result['return']))},
            'history_index': {'path': history_path,
                              'sha256': bh.file_hash(bh.safe(h.root, history_path))},
            'authority': 'DERIVED_VIEW_NOT_A_REPLACEMENT_FOR_EVIDENCE'}
    bh.atomic_json(bh.safe(h.root, f'.bh/exports/{value["task_id"]}/AGENT_RETURN.json'), view)
    return view


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', default='.')
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('context')
    sub.add_parser('return')
    sub.add_parser('schema').add_argument('definition')
    sub.add_parser('draft-proposal').add_argument('path')
    a = p.parse_args(argv)
    try:
        h = bh.Harness(a.root)
        if a.command == 'schema':
            value = schema_view(h.schema, a.definition)
        elif a.command == 'context':
            value = context_view(h)
        elif a.command == 'draft-proposal':
            value = draft_proposal(h, a.path)
        else:
            with h.lock():
                value = return_view(h)
        print(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False))
        return 2 if value.get('current_evidence_gaps') or value.get('deviations') else 0
    except (bh.BHError, OSError, ValueError, KeyError) as exc:
        print(json.dumps({'status': 'BLOCKED', 'reason': str(exc)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
