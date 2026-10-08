#!/usr/bin/env python3
"""Install local template files directly, or preview/apply/roll back managed files.

With only --target, copy files as-is without validation, overwriting matching files.
Explicit preview/apply/rollback operations retain their validation and approval checks.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import uuid
sys.dont_write_bytecode = True
PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bh_runtime', PACKAGE / 'project-template/Tools/BH/bh.py')
bh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bh)


def direct_install(target):
    root = Path(target).absolute()
    shutil.copytree(PACKAGE / 'project-template', root, dirs_exist_ok=True)
    return {'status': 'APPLIED', 'destination': str(root), 'mode': 'direct'}


def distribution():
    value = bh.load_json(PACKAGE / 'PACKAGE_FILES.json')
    bh.require(value.get('version') == '1.0.0', 'Unsupported distribution version')
    entries = bh.unique(value['files'], 'path', 'distribution file paths')
    bh.require(len({n.casefold() for n in entries}) == len(entries), 'Case-colliding distribution')
    for name, entry in entries.items():
        source = bh.safe(PACKAGE / 'project-template', name)
        bh.require(source.is_file(), 'Distribution changed: ' + name)
        data = source.read_bytes()
        actual = hashlib.sha256(data).hexdigest()
        # Windows checkouts may convert release LF files to CRLF. Validate
        # their content, then bind the preview and copies to the local bytes.
        bh.require(actual == entry['sha256'] or
                   hashlib.sha256(data.replace(b'\r\n', b'\n')).hexdigest() == entry['sha256'],
                   'Distribution changed: ' + name)
        entry['sha256'] = actual
        bh.require(entry.get('ownership') in ('managed', 'project-seed'), 'Undeclared file ownership: ' + name)
    return value


def target_root(target):
    p = Path(target).absolute()
    bh.no_links(p)
    p = p.resolve()
    bh.require(p.is_dir(), 'Destination must exist; no guessed game creation')
    bh.require(not p.is_relative_to(PACKAGE) and not PACKAGE.is_relative_to(p), 'Do not install into the source collection or its ancestor')
    # Archives and copied projects can be installed without Git. A .git file
    # also counts as repository metadata (for example, in a linked worktree).
    if any((parent / '.git').exists() for parent in (p, *p.parents)):
        bh.require(Path(bh.git(p, 'rev-parse', '--show-toplevel').decode().strip()).resolve() == p, 'Destination must be Git root')
    bh.require(bh.safe(p, 'ProjectSettings/ProjectVersion.txt').is_file() or bh.safe(p, '.bh/SYNTHETIC_FIXTURE').is_file(), 'Destination is not a Unity project or visibly synthetic fixture')
    return p


def preview(target, preserve=()):
    root = target_root(target)
    dist = distribution()
    bh.require(set(preserve) <= {'AGENTS.md'}, 'Only AGENTS.md supports explicit project-owned preservation')
    state_path = bh.safe(root, '.bh/state.json')
    if state_path.exists():
        state = bh.load_json(state_path)
        bh.require(state.get('phase') in ('ACCEPTED', 'CANCELLED'), 'Finish/cancel and archive active task before harness migration')
    manifest = bh.safe(root, '.bh/install/managed.json')
    old = bh.load_json(manifest) if manifest.exists() else {'files': {}}
    rows = []
    for entry in dist['files']:
        name = entry['path']
        dest = bh.safe(root, name)
        prior = bh.file_hash(dest) if dest.is_file() else None
        bh.require(not dest.exists() or dest.is_file(), 'Directory/file conflict: ' + name)
        if prior == entry['sha256']:
            action = 'UNCHANGED'
        elif entry['ownership'] == 'project-seed' and prior is not None:
            action = 'PRESERVE_PROJECT_OWNED'
        elif name in preserve and prior is not None:
            action = 'PRESERVE_REQUIRES_MANUAL_MERGE'
        elif prior is None:
            action = 'ADD'
        elif old.get('files', {}).get(name) == prior:
            action = 'UPDATE'
        else:
            action = 'CONFLICT'
        rows.append({'path': name, 'action': action, 'before': prior, 'after': entry['sha256'], 'ownership': entry['ownership']})
    retired = sorted(set(old.get('files', {})) - {r['path'] for r in rows})
    return {'version': '1.0.0', 'destination': str(root), 'distribution_sha256': bh.digest(dist), 'rows': rows,
            'retired_preserved': retired, 'preserve': sorted(preserve),
            'manual_merge_required': any(r['action'] == 'PRESERVE_REQUIRES_MANUAL_MERGE' for r in rows)}


def apply(target, approved, preserve=()):
    root = target_root(target)
    before = preview(root, preserve)
    bh.require(bh.digest(before) == approved, 'Preview changed or approval hash does not match; no writes made')
    bh.require(not any(x['action'] == 'CONFLICT' for x in before['rows']), 'Unresolved conflicts; backup does not authorize overwrite')
    lock = bh.safe(root, '.bh/install/writer.lock')
    lock.parent.mkdir(parents=True, exist_ok=True)
    try:
        lock.open('x').close()
    except FileExistsError as exc:
        raise bh.BHError('Installation writer lock exists; inspect interrupted transaction') from exc
    try:
        bh.require(bh.digest(preview(root, preserve)) == approved, 'Destination changed before apply')
        prior_manifest = bh.safe(root, '.bh/install/managed.json')
        prior = bh.load_json(prior_manifest) if prior_manifest.exists() else None
        changes = [r for r in before['rows'] if r['action'] in ('ADD', 'UPDATE')]
        if not changes:
            return {'status': 'UNCHANGED', 'manual_merge_required': before['manual_merge_required']}
        tx = 'install-' + uuid.uuid4().hex
        journal = {'version': '1.0.0', 'id': tx, 'status': 'APPLYING', 'approved_preview_sha256': approved,
                   'prior_manifest': prior, 'changes': [], 'manual_merge_required': before['manual_merge_required']}
        journal_path = bh.safe(root, f'.bh/install/{tx}/journal.json')
        bh.atomic_json(journal_path, journal)
        for row in changes:
            dest = bh.safe(root, row['path'])
            source = bh.safe(PACKAGE / 'project-template', row['path'])
            bh.require((bh.file_hash(dest) if dest.exists() else None) == row['before'], 'Concurrent destination change: ' + row['path'])
            bh.require(bh.file_hash(source) == row['after'], 'Distribution changed during apply')
            backup = None
            if dest.exists():
                backup = f'.bh/install/{tx}/backup/{row["path"]}'
                b = bh.safe(root, backup)
                b.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(dest, b)
            change = {**row, 'backup': backup, 'written': False}
            journal['changes'].append(change)
            bh.atomic_json(journal_path, journal)
            dest.parent.mkdir(parents=True, exist_ok=True)
            temp = dest.with_name(dest.name + '.bh-install-' + uuid.uuid4().hex)
            try:
                shutil.copyfile(source, temp)
                bh.require((bh.file_hash(dest) if dest.exists() else None) == row['before'], 'Concurrent destination change before replacement')
                temp.replace(dest)
            finally:
                if temp.exists():
                    temp.unlink()
            change['written'] = True
            bh.atomic_json(journal_path, journal)
        managed = {r['path']: r['after'] for r in before['rows'] if r['ownership'] == 'managed' and not r['action'].startswith('PRESERVE')}
        bh.atomic_json(prior_manifest, {'version': '1.0.0', 'transaction': tx, 'files': managed,
                                      'manual_merge_required': before['manual_merge_required']})
        journal['status'] = 'APPLIED'
        bh.atomic_json(journal_path, journal)
        return {'status': 'APPLIED', 'transaction': tx, 'manual_merge_required': before['manual_merge_required'],
                'next': 'Reconcile project/local bindings and all instructions. Installation does not approve a game task.'}
    finally:
        if lock.exists():
            lock.unlink()


def rollback(target, transaction, execute=False):
    root = target_root(target)
    bh.portable(transaction)
    bh.require('/' not in transaction, 'Transaction ID must be a single name')
    journal_path = bh.safe(root, f'.bh/install/{transaction}/journal.json')
    journal = bh.load_json(journal_path)
    bh.require(journal['id'] == transaction and journal['status'] in ('APPLIED', 'APPLYING', 'ROLLED_BACK'), 'Invalid rollback transaction')
    if journal['status'] == 'ROLLED_BACK':
        return {'status': 'UNCHANGED'}
    state = bh.safe(root, '.bh/state.json')
    bh.require(not state.exists(), 'Archive the active task before rollback; state must not outlive its harness')
    managed_path = bh.safe(root, '.bh/install/managed.json')
    active = bh.load_json(managed_path) if managed_path.exists() else None
    if active is not None:
        allowed = {transaction}
        if journal['status'] == 'APPLYING' and journal['prior_manifest']:
            allowed.add(journal['prior_manifest'].get('transaction'))
        bh.require(active.get('transaction') in allowed, 'Roll back newest transaction first')
    conflicts = []
    retained = []
    for row in journal['changes']:
        dest = bh.safe(root, row['path'])
        current = bh.file_hash(dest) if dest.is_file() else None
        if row.get('ownership') == 'project-seed' and current not in (row['after'], row['before']):
            retained.append(row['path'])
            continue
        if current not in (row['after'], row['before']):
            conflicts.append(row['path'])
        if row['backup']:
            b = bh.safe(root, row['backup'])
            bh.require(b.is_file() and bh.file_hash(b) == row['before'], 'Backup missing/changed')
    bh.require(not conflicts, 'Local changes preserved; rollback blocked: ' + ', '.join(conflicts))
    if not execute:
        return {'status': 'ROLLBACK_PREVIEW', 'transaction': transaction, 'managed_files': len(journal['changes']),
                'retained_project_owned': retained, 'will_remove_only_unmodified_additions': True}
    lock = bh.safe(root, '.bh/install/writer.lock')
    try:
        lock.open('x').close()
    except FileExistsError as exc:
        raise bh.BHError('Installation writer lock exists') from exc
    try:
        bh.require(bh.load_json(journal_path) == journal, 'Concurrent transaction change')
        bh.require((bh.load_json(managed_path) if managed_path.exists() else None) == active, 'Concurrent managed manifest change')
        for row in reversed(journal['changes']):
            if row['path'] in retained:
                continue
            dest = bh.safe(root, row['path'])
            current = bh.file_hash(dest) if dest.is_file() else None
            bh.require(current in (row['after'], row['before']), 'Concurrent edit during rollback')
            if row['backup']:
                temp = dest.with_name(dest.name + '.bh-rollback-' + uuid.uuid4().hex)
                shutil.copyfile(bh.safe(root, row['backup']), temp)
                temp.replace(dest)
            elif current == row['after']:
                dest.unlink()
        if journal['prior_manifest'] is None:
            if managed_path.exists():
                managed_path.unlink()
        else:
            bh.atomic_json(managed_path, journal['prior_manifest'])
        journal['status'] = 'ROLLED_BACK'
        bh.atomic_json(journal_path, journal)
        return {'status': 'ROLLED_BACK', 'retained_project_owned': retained,
                'retained': 'Backups, journal, unrelated files, user-edited configuration and empty directories'}
    finally:
        if lock.exists():
            lock.unlink()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('operation', nargs='?', choices=('preview', 'apply', 'rollback'),
                   help='Omit to copy local files directly without validation')
    p.add_argument('--target', required=True)
    p.add_argument('--preserve', action='append', default=[])
    p.add_argument('--approved-preview')
    p.add_argument('--transaction')
    p.add_argument('--execute', action='store_true')
    a = p.parse_args()
    if a.operation is None and (a.preserve or a.approved_preview or a.transaction or a.execute):
        p.error('--preserve, --approved-preview, --transaction and --execute require an explicit operation')
    try:
        if a.operation is None:
            out = direct_install(a.target)
        elif a.operation == 'preview':
            value = preview(a.target, a.preserve)
            out = {'preview': value, 'approval_sha256': bh.digest(value)}
        elif a.operation == 'apply':
            bh.require(a.approved_preview, 'Apply requires exact --approved-preview hash')
            out = apply(a.target, a.approved_preview, a.preserve)
        else:
            bh.require(a.transaction, 'Rollback requires transaction ID')
            out = rollback(a.target, a.transaction, a.execute)
        print(json.dumps(out, indent=2))
        return 0
    except (bh.BHError, OSError, ValueError, KeyError) as exc:
        print(json.dumps({'status': 'BLOCKED', 'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
