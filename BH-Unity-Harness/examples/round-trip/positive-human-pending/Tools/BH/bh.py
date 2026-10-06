#!/usr/bin/env python3
"""BH Unity Harness 1.0.0 candidate: deterministic checks, not a sandbox.

Human approval records are structurally checked, never authenticated here.
No model/API calls, package installation, or automatic Git mutation are performed.
"""
from __future__ import annotations
import argparse
import contextlib
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import signal
import subprocess
import sys
import time
import uuid
import xml.etree.ElementTree as ET

sys.dont_write_bytecode = True
VERSION = '1.0.0'
TIERS = {'fast': 0, 'slice': 1, 'milestone': 2}
VOLATILE = ('.git', 'Library', 'Temp', 'Logs', 'obj', 'UserSettings',
            '.bh/runs', '.bh/tasks', '.bh/exports', '.bh/install', '.bh/locks',
            '.bh/state.json', '.bh/CHECKPOINT.md')
CORE = ('AGENTS.md', '.agents/skills', 'Tools/BH', '.bh/schema.json',
        '.bh/project.json', '.bh/local.json', '.bh/bindings.json')
TRANSITIONS = {
    'DISCOVERY': {'PLANNED', 'BLOCKED', 'PAUSED', 'CANCELLED'},
    'PLANNED': {'AWAITING_APPROVAL', 'BLOCKED', 'PAUSED', 'CANCELLED'},
    'AWAITING_APPROVAL': {'APPROVED', 'PLANNED', 'BLOCKED', 'PAUSED', 'CANCELLED'},
    'APPROVED': {'EXECUTING', 'PLANNED', 'BLOCKED', 'PAUSED', 'CANCELLED'},
    'EXECUTING': {'VERIFYING', 'PLANNED', 'BLOCKED', 'PAUSED', 'CANCELLED'},
    'VERIFYING': {'EXECUTING', 'READY_FOR_HUMAN_REVIEW', 'FAILED', 'BLOCKED', 'PAUSED'},
    'READY_FOR_HUMAN_REVIEW': {'ACCEPTED', 'EXECUTING', 'PLANNED', 'BLOCKED', 'PAUSED', 'CANCELLED'},
    'FAILED': {'EXECUTING', 'PLANNED', 'BLOCKED', 'PAUSED', 'CANCELLED'},
    'BLOCKED': {'DISCOVERY', 'PLANNED', 'EXECUTING', 'PAUSED', 'CANCELLED'},
    'PAUSED': {'DISCOVERY', 'PLANNED', 'EXECUTING', 'BLOCKED', 'CANCELLED'},
    'ACCEPTED': set(), 'CANCELLED': set(),
}

class BHError(Exception):
    """An explicit blocked, invalid, or failed operation."""


def require(condition, message):
    if not condition:
        raise BHError(message)


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00', 'Z')


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      allow_nan=False).encode('utf-8')


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def load_json(path):
    p = Path(path)
    require(p.is_file(), f'Missing required file: {p}')
    require(p.stat().st_size <= 16 * 1024 * 1024, f'JSON exceeds 16 MiB: {p}')
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f'Duplicate JSON key: {key}')
            result[key] = value
        return result
    try:
        return json.loads(p.read_text(encoding='utf-8-sig'), object_pairs_hook=pairs,
                          parse_constant=lambda x: (_ for _ in ()).throw(BHError('Nonfinite JSON number')))
    except (ValueError, UnicodeError) as exc:
        raise BHError(f'Malformed JSON in {p}: {exc}') from exc


def portable(name, allow_dot=False):
    require(isinstance(name, str) and bool(name), 'Empty path')
    if allow_dot and name == '.':
        return name
    require(not name.startswith(('/', '\\')) and '\\' not in name and ':' not in name,
            f'Absolute, drive, UNC, or backslash path rejected: {name}')
    require(not any(ord(c) < 32 for c in name), 'Control character in path')
    for part in name.split('/'):
        require(part not in ('', '.', '..') and not part.endswith(('.', ' ')), f'Unsafe path: {name}')
        require(not re.match(r'^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)', part, re.I),
                f'Windows reserved path: {name}')
        require(not any(c in part for c in '<>"|?*'), f'Unsafe filename: {name}')
    return name


def no_links(path):
    path = Path(path)
    for part in [path, *path.parents]:
        if part.exists() or part.is_symlink():
            require(not part.is_symlink(), f'Symlink rejected: {part}')
            require(not (getattr(part.lstat(), 'st_file_attributes', 0) & 0x400),
                    f'Junction/reparse point rejected: {part}')


def safe(root, name, allow_dot=False):
    portable(name, allow_dot)
    p = Path(root) / name
    no_links(p)
    require(p.resolve().is_relative_to(Path(root).resolve()), f'Path escapes workspace: {name}')
    current = Path(root)
    for part in ([] if name == '.' else name.split('/')):
        if current.is_dir():
            matches = [x.name for x in current.iterdir() if x.name.casefold() == part.casefold()]
            require(not matches or matches == [part], f'Case collision: {name}: {matches}')
        current /= part
    return p


def below(name, prefix):
    return name == prefix or name.startswith(prefix.rstrip('/') + '/')


def atomic_json(path, value):
    p = Path(path)
    no_links(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    temp = p.with_name(p.name + '.tmp-' + uuid.uuid4().hex)
    try:
        with temp.open('x', encoding='utf-8', newline='\n') as stream:
            stream.write(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, p)
    finally:
        if temp.exists():
            temp.unlink()


def validate(value, definition, schema, loc='$'):
    """Validate the deliberately restricted, local BH schema vocabulary; fail closed."""
    s = schema['$defs'][definition] if isinstance(definition, str) else definition
    supported = {'$ref', 'type', 'const', 'enum', 'anyOf', 'properties', 'required',
                 'additionalProperties', 'items', 'minItems', 'maxItems', 'uniqueItems',
                 'minLength', 'maxLength', 'pattern', 'format', 'minimum', 'maximum'}
    require(not set(s) - supported, f'Unsupported schema keywords at {loc}: {set(s) - supported}')
    if '$ref' in s:
        require(s['$ref'].startswith('#/$defs/'), 'Remote schema references are forbidden')
        return validate(value, s['$ref'].split('/')[-1], schema, loc)
    if 'anyOf' in s:
        for choice in s['anyOf']:
            try:
                validate(value, choice, schema, loc)
                return
            except BHError:
                pass
        raise BHError(f'{loc}: no schema alternative matches')
    if 'const' in s:
        require(type(value) is type(s['const']) and value == s['const'], f'{loc}: wrong constant')
    if 'enum' in s:
        require(any(type(value) is type(x) and value == x for x in s['enum']), f'{loc}: unsupported value {value}')
    t = s.get('type')
    types = {'object': dict, 'array': list, 'string': str, 'integer': int, 'boolean': bool, 'null': type(None)}
    if t == 'number':
        require(type(value) in (int, float) and math.isfinite(value), f'{loc}: expected finite number')
    elif t:
        require(t in types and type(value) is types[t], f'{loc}: expected {t}')
    if isinstance(value, dict):
        props = s.get('properties', {})
        require(not set(s.get('required', [])) - value.keys(), f'{loc}: missing {set(s.get("required", [])) - value.keys()}')
        for key, item in value.items():
            if key in props:
                validate(item, props[key], schema, loc + '.' + key)
            elif s.get('additionalProperties') is False:
                raise BHError(f'{loc}: unknown field {key}')
            elif isinstance(s.get('additionalProperties'), dict):
                validate(item, s['additionalProperties'], schema, loc + '.' + key)
    elif isinstance(value, list):
        require(s.get('minItems', 0) <= len(value) <= s.get('maxItems', 1000000), f'{loc}: array size')
        if s.get('uniqueItems'):
            require(len({canonical(x) for x in value}) == len(value), f'{loc}: duplicate items')
        for i, item in enumerate(value):
            validate(item, s.get('items', {}), schema, f'{loc}[{i}]')
    elif isinstance(value, str):
        require(s.get('minLength', 0) <= len(value) <= s.get('maxLength', 10000000), f'{loc}: string size')
        if 'pattern' in s:
            require(re.search(s['pattern'], value) is not None, f'{loc}: pattern mismatch')
        if 'format' in s:
            require(s['format'] == 'date-time', f'{loc}: unsupported format')
            try:
                parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
                require(parsed.utcoffset() == dt.timedelta(0), f'{loc}: UTC required')
            except ValueError as exc:
                raise BHError(f'{loc}: invalid timestamp') from exc
    elif type(value) in (int, float):
        require(math.isfinite(value), f'{loc}: nonfinite number')
        require(s.get('minimum', -math.inf) <= value <= s.get('maximum', math.inf), f'{loc}: numeric range')


def unique(items, key, label):
    result = {x[key]: x for x in items}
    require(len(result) == len(items), f'Duplicate {label}')
    return result


def git(root, *args):
    executable = shutil.which('git')
    require(executable is not None, 'Git executable unavailable')
    executable = str(Path(executable).resolve())
    no_links(executable)
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0')
    result = subprocess.run([executable, '-c', 'core.fsmonitor=false', '-C', str(root), *args],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30, env=env)
    require(result.returncode == 0, 'Git read failed: ' + result.stderr.decode('utf-8', 'replace')[:500])
    return result.stdout


def snapshot(root):
    root = Path(root).resolve()
    require(Path(git(root, 'rev-parse', '--show-toplevel').decode().strip()).resolve() == root,
            'Select the Git repository root, not a subdirectory')
    commit = git(root, 'rev-parse', 'HEAD').decode().strip()
    for entry in git(root, 'ls-files', '--stage', '-z').split(b'\0'):
        if entry:
            mode = entry.split(b' ', 1)[0]
            require(mode not in (b'120000', b'160000'), 'Symlink/submodule requires a separately reviewed workspace')
    names = sorted(set(x.decode('utf-8') for x in git(root, 'ls-files', '--cached', '--others', '--exclude-standard', '-z').split(b'\0') if x))
    require(len({x.casefold() for x in names}) == len(names), 'Case-colliding Git paths')
    files = {}
    total = 0
    for name in names:
        if any(below(name, p) for p in VOLATILE):
            continue
        p = safe(root, name)
        if not p.exists():
            continue
        require(p.is_file(), f'Non-file source: {name}')
        with p.open('rb') as stream:
            require(not stream.read(128).startswith(b'version https://git-lfs.github.com/spec/v1'),
                    f'Unmaterialized LFS pointer: {name}')
        files[name] = file_hash(p)
        total += p.stat().st_size
    status = git(root, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
    return {'commit': commit, 'dirty': bool(status), 'status_sha256': hashlib.sha256(status).hexdigest(),
            'files': files, 'sha256': digest({'commit': commit, 'files': files}),
            'file_count': len(files), 'bytes_hashed': total}


def changed(a, b):
    return sorted(k for k in a.keys() | b.keys() if a.get(k) != b.get(k))


class Harness:
    def __init__(self, root):
        p = Path(root).absolute()
        no_links(p)
        self.root = p.resolve()
        self.schema = load_json(safe(self.root, '.bh/schema.json'))
        self.config = self.read('.bh/project.json', 'project')
        self.local = self.read('.bh/local.json', 'local')
        self.bindings = self.read('.bh/bindings.json', 'bindings')
        for value in (self.local, self.bindings):
            self.identity(value)
        self.tools = unique(self.local['tools'], 'key', 'tool keys')
        self.bound = unique(self.bindings['checks'], 'check_id', 'check bindings')
        if self.config['synthetic']:
            require(safe(self.root, '.bh/SYNTHETIC_FIXTURE').is_file(), 'Synthetic mode requires visible fixture marker')
        else:
            require(self.config['engine']['name'] == 'Unity', 'Non-synthetic project must declare Unity')
        for name in self.config['protected_paths']:
            portable(name)

    def read(self, name, kind):
        v = load_json(safe(self.root, name))
        validate(v, kind, self.schema)
        return v

    def identity(self, value, task=None):
        require(value['project_id'] == self.config['project_id'], 'Wrong project identity')
        if task is not None:
            require(value['task_id'] == task, 'Wrong task identity')
        if 'synthetic' in value:
            require(value['synthetic'] == self.config['synthetic'], 'Synthetic/real boundary mismatch')

    def artifact(self, entry):
        p = safe(self.root, entry['path'])
        require(p.is_file() and file_hash(p) == entry['sha256'], f'Missing or changed artifact: {entry["path"]}')
        return p

    def config_hash(self):
        return digest([file_hash(safe(self.root, x)) for x in ('.bh/project.json', '.bh/local.json', '.bh/bindings.json')])

    def harness_hash(self):
        files = {}
        for prefix in ('Tools/BH', '.agents/skills'):
            p = safe(self.root, prefix)
            if p.exists():
                for f in sorted(p.rglob('*')):
                    no_links(f)
                    if f.is_file() and '__pycache__' not in f.parts:
                        files[f.relative_to(self.root).as_posix()] = file_hash(f)
        for name in ('AGENTS.md', '.bh/schema.json'):
            p = safe(self.root, name)
            require(p.is_file(), f'Missing core: {name}')
            files[name] = file_hash(p)
        return digest(files)

    def approval(self, record, kind, subject, task):
        validate(record, 'approval', self.schema)
        self.identity(record, task)
        require(record['kind'] == kind and record['subject_sha256'] == subject, 'Approval subject/kind mismatch')
        require(record['actor'] == 'human', 'Executor cannot self-certify')
        # Source authenticity must be inspected by the human/session; these fields are not credentials.

    def handoff(self, name, executable=True):
        h = self.read(name, 'handoff')
        self.identity(h, h['task_id'])
        manifest = unique(h['artifacts'], 'path', 'artifact paths')
        for entry in h['artifacts']:
            self.artifact(entry)
        required = [h['design_path'], h['criteria_path'], h['overlay_path'], *h['read_order'],
                    *h['architecture_refs'], *h['data_contract_refs']]
        require(set(required) <= manifest.keys(), 'Reference missing from pinned artifact manifest')
        c = self.read(h['criteria_path'], 'criteria')
        self.identity(c, h['task_id'])
        o = self.read(h['overlay_path'], 'overlay')
        self.identity(o)
        criteria = unique(c['criteria'], 'id', 'acceptance IDs')
        invariants = unique(o['invariants'], 'id', 'invariants')
        require(set(h['acceptance_ids']) == criteria.keys(), 'Dropped or extra acceptance criterion')
        require(set(h['invariant_ids']) == invariants.keys(), 'Dropped or extra project invariant')
        checks = unique(h['checks'], 'id', 'check IDs')
        for check in checks.values():
            require(set(check['ac_ids']) <= criteria.keys(), 'Check refers to unknown acceptance criterion')
            if check['adapter'] == 'manual':
                require(all(criteria[x]['kind'] == 'human' for x in check['ac_ids']), 'Manual check cannot replace automated criterion')
            else:
                require(all(criteria[x]['kind'] == 'automated' for x in check['ac_ids']), 'Automation cannot certify human judgment')
            if check['adapter'] == 'nunit':
                require(check['minimum_tests'] > 0 and bool(check['test_names']), 'NUnit requires positive count and named tests')
            if check['required']:
                require(check['not_applicable_reason'] is None, 'Required checks cannot be downgraded to N/A')
                require(TIERS[check['profile']] <= TIERS[h['required_profile']], 'Required check lies above required profile')
        for criterion in criteria.values():
            require(any(x['required'] and criterion['id'] in x['ac_ids'] for x in checks.values()),
                    f'Acceptance criterion lacks required verification: {criterion["id"]}')
        for p in h['allowed_paths'] + h['protected_paths'] + o['protected_paths']:
            portable(p)
        if executable:
            require(h['status'] == 'COMPILED', 'Handoff is not compiled from approved inputs')
            require(not any(q['class'] in ('BLOCKING', 'DESIGN-SHAPING') for q in h['questions']), 'Unresolved blocking/design-shaping decision')
            require(o['status'] in ('RECONCILED', 'SYNTHETIC'), 'Project overlay requires repository/human reconciliation')
            require(not o['open_decisions'], 'Project overlay retains unresolved decisions')
            require(h['approval'] is not None, 'Missing design approval')
            subject = digest({k: v for k, v in h.items() if k != 'approval'})
            self.approval(h['approval'], 'design', subject, h['task_id'])
        return h, criteria, o

    def state(self):
        s = self.read('.bh/state.json', 'state')
        self.identity(s, s['task_id'])
        return s

    @contextlib.contextmanager
    def lock(self):
        p = safe(self.root, '.bh/locks/writer.json')
        p.parent.mkdir(parents=True, exist_ok=True)
        token = uuid.uuid4().hex
        try:
            with p.open('x', encoding='utf-8') as f:
                json.dump({'pid': os.getpid(), 'host': platform.node(), 'token': token, 'created': utc()}, f)
        except FileExistsError as exc:
            raise BHError('Writer lock exists; inspect owner/process and recover explicitly; no automatic unlock') from exc
        try:
            yield
        finally:
            if p.exists() and load_json(p).get('token') == token:
                p.unlink()

    def checkpoint(self, s):
        baseline = 'No technical plan yet.'
        if s['plan']:
            try:
                p = self.read(s['plan']['path'], 'plan')
                b = p['baseline']
                baseline = f'{b["commit"]}; dirty={b["dirty"]}; inputs={b["sha256"]}'
            except (BHError, OSError):
                baseline = 'UNAVAILABLE; do not trust previous execution context.'
        lines = ['# BH checkpoint (generated; edit state through commands)',
                 f'State revision: {s["revision"]}; SHA-256: {digest(s)}',
                 f'Project/task: {s["project_id"]}/{s["task_id"]}; phase: {s["phase"]}',
                 f'Handoff: {s["handoff"]["path"]}', f'Plan: {s["plan"]}',
                 f'Planned baseline: {baseline}', f'Latest runs: {s["runs"][-3:]}',
                 f'Acceptance: {s["ac_status"]}', f'Claims (not evidence): {s["claims"]}',
                 f'Blockers: {s["blockers"]}',
                 f'Attempts used: {s["counters"]}; configured budgets: {self.config["budgets"]}',
                 f'Next exact action: {s["next_action"]}',
                 'Run resume to check freshness against the workspace. Human acceptance requires genuine source review.']
        p = safe(self.root, '.bh/CHECKPOINT.md')
        temp = p.with_suffix('.tmp-' + uuid.uuid4().hex)
        try:
            temp.write_text('\n\n'.join(lines) + '\n', encoding='utf-8')
            os.replace(temp, p)
        finally:
            if temp.exists():
                temp.unlink()

    def save(self, s, expected):
        p = safe(self.root, '.bh/state.json')
        require((self.state()['revision'] if p.exists() else None) == expected, 'Concurrent state change')
        s['revision'] = 0 if expected is None else expected + 1
        s['updated_utc'] = utc()
        validate(s, 'state', self.schema)
        atomic_json(p, s)
        self.checkpoint(s)

    def move(self, s, target, reason):
        require(target in TRANSITIONS[s['phase']], f'Illegal transition {s["phase"]} -> {target}')
        require(len(s['events']) < 256, 'Task event limit reached; preserve records and explicitly split/archive task')
        s['events'].append({'from': s['phase'], 'to': target, 'at': utc(), 'reason': reason})
        s['phase'] = target

    def save_record(self, name, value, kind):
        validate(value, kind, self.schema)
        p = safe(self.root, name)
        if p.exists():
            require(load_json(p) == value, 'Immutable record conflict: ' + name)
        else:
            atomic_json(p, value)
        return {'path': name, 'sha256': file_hash(p)}

    def load_plan(self, s):
        require(s['plan'] is not None, 'No technical plan')
        self.artifact(s['plan'])
        p = self.read(s['plan']['path'], 'plan')
        self.identity(p, s['task_id'])
        self.artifact(s['handoff'])
        require(p['handoff_sha256'] == s['handoff']['sha256'], 'Plan/handoff mismatch')
        require(p['config_sha256'] == self.config_hash() and p['harness_sha256'] == self.harness_hash(), 'Configuration/core changed; replan and reapprove')
        return p

    def scope(self, plan, now):
        require(now['commit'] == plan['baseline']['commit'], 'Git revision changed; reconcile/replan explicitly')
        for name in changed(plan['baseline']['files'], now['files']):
            require(any(below(name, p) for p in plan['allowed_paths']), 'Out-of-scope mutation: ' + name)
            require(not any(below(name, p) for p in plan['protected_paths']), 'Protected-path mutation: ' + name)

    def dependency_hash(self, spec, snap):
        binding = self.bound.get(spec['id'], {})
        deps = binding.get('dependency_paths', [])
        require(not deps or binding.get('dependency_review_ref'), 'Narrow dependencies require explicit review reference')
        files = {p: h for p, h in snap['files'].items() if not deps or any(below(p, d) for d in deps) or any(below(p, d) for d in CORE)}
        return digest({'commit': snap['commit'], 'files': files, 'config': self.config_hash(), 'harness': self.harness_hash()})

    def binding_ready(self, spec):
        if spec['adapter'] == 'manual':
            return
        require(spec['id'] in self.bound, 'Unbound required check: ' + spec['id'])
        b = self.bound[spec['id']]
        require(b['tool_key'] in self.tools, 'Unbound executable')
        t = self.tools[b['tool_key']]
        p = Path(t['path'])
        no_links(p)
        require(p.is_absolute() and p.is_file() and file_hash(p) == t['sha256'], 'Executable missing or changed: ' + t['key'])
        require(p.stem.lower() not in ('cmd', 'powershell', 'pwsh', 'bash', 'sh', 'zsh', 'wscript', 'cscript'), 'Shell interpreters are not supported adapters')
        require(b['result_file'] == Path(b['result_file']).name, 'Result file must be a simple run-local name')
        portable(b['result_file'])
        safe(self.root, b['working_directory'], True)
        for dep in b['dependency_paths']:
            portable(dep)
        for entry in b['input_files']:
            self.artifact(entry)
        if t['kind'] == 'python':
            require(b['arguments'] and not b['arguments'][0].startswith('-'), 'Python must invoke a reviewed file, not -c/-m')
            require(any(b['arguments'][0] == '{project}/' + a['path'] for a in b['input_files']), 'Python entry script must be pinned in input_files')
        if spec['adapter'] in ('facts', 'build'):
            require(bool(b['expectations']), 'Facts/build checks require approved observable expectations')
            require(set(spec['ac_ids']) <= {x for e in b['expectations'] for x in e['ac_ids']}, 'Expectation coverage incomplete')
        if spec['adapter'] == 'build':
            require(bool(b['build_target']), 'Build target is not configured')
        if spec['adapter'] == 'diagnostics':
            require(b['diagnostics_baseline'] is not None and b['diagnostic_source'], 'Diagnostics baseline/source missing')
            self.artifact(b['diagnostics_baseline'])
        if t['kind'] == 'unity':
            require(self.local['editor_route'] == 'batch', 'This executable adapter supports batch only; use separately reviewed Editor route')
            require(self.local['batch_closed_confirmation_ref'], 'Human confirmation of closed project is required')
            require(not safe(self.root, 'Temp/UnityLockfile').exists(), 'Editor/project ownership detected; never start a second batch Editor')
            require(self.config['engine']['version'] and self.config['engine']['render_pipeline'] != 'UNRECONCILED', 'Unity facts unreconciled')
            actual = safe(self.root, 'ProjectSettings/ProjectVersion.txt').read_text(encoding='utf-8')
            require(re.search(r'^m_EditorVersion:\s*' + re.escape(self.config['engine']['version']) + r'\s*$', actual, re.M), 'Unity project version mismatch')
            require(t['observed_version'] == self.config['engine']['version'], 'Editor tool version does not match project')
            args = b['arguments']
            require('-projectPath' in args and args.index('-projectPath') + 1 < len(args)
                    and args[args.index('-projectPath') + 1] == '{project}', 'Explicit Unity project targeting required')
            if spec['adapter'] == 'nunit':
                require('-runTests' in args and '-testResults' in args and '-quit' not in args, 'Use documented test runner arguments without premature -quit')
        for arg in b['arguments']:
            require(not any(c in arg for c in ('\x00', '\n', '\r')), 'Unsafe control character in argument')
            require(set(re.findall(r'\{([^{}]+)\}', arg)) <= {'project', 'run_dir', 'result', 'log', 'project_id', 'task_id', 'run_id'}, 'Unknown command placeholder')
        return b, t

    def preflight(self):
        snap = snapshot(self.root)
        issues = []
        skills = []
        # Use known Git input paths instead of traversing Library/assets caches.
        known = self.config['instruction_review']['paths']
        for name in snap['files']:
            if Path(name).name == 'AGENTS.override.md':
                issues.append('Instruction override requires review: ' + name)
            if Path(name).name == 'AGENTS.md' and name not in known:
                issues.append('Unreviewed nested instructions: ' + name)
        names = []
        base = safe(self.root, '.agents/skills')
        for p in sorted(base.glob('*/SKILL.md')):
            no_links(p)
            text = p.read_text(encoding='utf-8')
            m = re.search(r'^name:\s*(\S+)', text, re.M)
            require(m is not None, 'Skill missing name: ' + str(p))
            names.append(m.group(1))
            skills.append(p.parent.name)
        require(len(names) == len(set(names)), 'Duplicate local skill names')
        if any(x.startswith('b1-') for x in skills):
            issues.append('Legacy B1 skills remain active; human must resolve duplicate policy before adoption')
        if not self.config['synthetic']:
            if (self.config['engine']['version'] is None or self.config['engine']['render_pipeline'] == 'UNRECONCILED'
                    or any(t.startswith('UNCONFIGURED') for t in self.config['engine']['targets'])):
                issues.append('Unity version/render pipeline requires reconciliation')
            if self.config['adoption_ref'].startswith('UNCONFIGURED'):
                issues.append('Project adoption is not recorded')
        return {'status': 'BLOCKED' if issues else 'PREFLIGHT_ONLY', 'snapshot': {k: v for k, v in snap.items() if k != 'files'},
                'issues': issues, 'skills': skills, 'tools': [{'key': t['key'], 'version': t['observed_version']} for t in self.tools.values()],
                'limits': ['No Unity/MCP execution occurred.', 'Global/ancestor or ignored host instructions and actual approval authenticity require session review.']}

    def initialize(self, name):
        h, criteria, _ = self.handoff(name)
        require('write-task-state' in h['allowed_actions'], 'Task/state writes not declared')
        p = safe(self.root, '.bh/state.json')
        if p.exists():
            s = self.state()
            require(s['task_id'] == h['task_id'] and s['handoff']['sha256'] == file_hash(safe(self.root, name)), 'Existing task must be explicitly archived/migrated; not overwritten')
            return {'status': 'UNCHANGED', 'phase': s['phase']}
        closed = safe(self.root, f'.bh/tasks/{h["task_id"]}/closed')
        require(not closed.exists(), 'Archived task ID cannot be reused; assign a new task ID')
        s = {'version': VERSION, 'harness_version': VERSION, 'project_id': h['project_id'], 'task_id': h['task_id'],
             'revision': 0, 'phase': 'DISCOVERY', 'synthetic': h['synthetic'], 'updated_utc': utc(),
             'handoff': {'path': name, 'sha256': file_hash(safe(self.root, name))}, 'plan': None, 'approval': None,
             'acceptance_record': None, 'claims': [], 'ac_status': {x: 'HUMAN_PENDING' if c['kind'] == 'human' else 'NOT_RUN' for x, c in criteria.items()},
             'runs': [], 'pending_run': None, 'blockers': [], 'next_action': 'Read handoff inputs; prepare bounded technical proposal, then run plan.',
             'counters': dict.fromkeys(('failed_rounds', 'repeat_failures', 'no_progress_rounds', 'infrastructure_failures', 'recovery_cycles'), 0),
             'last_fingerprint': None, 'last_passed_ids': [], 'events': []}
        self.save(s, None)
        return {'phase': s['phase'], 'next_action': s['next_action']}

    def make_plan(self, proposal_path):
        s = self.state()
        rev = s['revision']
        self.artifact(s['handoff'])
        h, criteria, overlay = self.handoff(s['handoff']['path'])
        proposal = self.read(proposal_path, 'proposal')
        self.identity(proposal, s['task_id'])
        require(set(criteria) <= {x for step in proposal['steps'] for x in step['ac_ids']}, 'Plan drops acceptance criteria')
        require(not proposal['scope_conflicts'], 'Unresolved technical scope conflict')
        for step in proposal['steps']:
            require(set(step['ac_ids']) <= criteria.keys(), 'Plan refers to unknown AC')
            for p in step['paths']:
                portable(p)
                require(any(below(p, a) for a in h['allowed_paths']), 'Plan exceeds design envelope')
        snap = snapshot(self.root)
        blockers = self.preflight()['issues']
        if h['source_commit'] and h['source_commit'] != snap['commit']:
            blockers.append('Handoff repository baseline differs; obtain corrected design/reconciliation input')
        for spec in h['checks']:
            try:
                self.binding_ready(spec)
            except BHError as exc:
                if spec['required']:
                    blockers.append(str(exc))
        protected = (*CORE, '.git', *self.config['protected_paths'], *h['protected_paths'],
                     *overlay['protected_paths'], s['handoff']['path'], *(a['path'] for a in h['artifacts']))
        plan = {'version': VERSION, 'project_id': s['project_id'], 'task_id': s['task_id'], 'created_utc': utc(),
                'handoff_sha256': s['handoff']['sha256'], 'config_sha256': self.config_hash(), 'harness_sha256': self.harness_hash(),
                'baseline': snap, 'proposal': proposal, 'blockers': blockers, 'allowed_paths': h['allowed_paths'],
                'protected_paths': sorted(set(protected)), 'allowed_actions': h['allowed_actions'],
                'check_ids': [x['id'] for x in h['checks']], 'required_profile': h['required_profile']}
        s['plan'] = self.save_record(f'.bh/tasks/{s["task_id"]}/plans/{digest(plan)}.json', plan, 'plan')
        s['approval'] = None
        s['acceptance_record'] = None
        self.move(s, 'PLANNED', 'Bound technical proposal to current repository/configuration')
        self.move(s, 'BLOCKED' if blockers else 'AWAITING_APPROVAL', 'Capability checks and reconciliation complete')
        s['blockers'] = blockers
        s['ac_status'] = {x: 'HUMAN_PENDING' if c['kind'] == 'human' else 'NOT_RUN' for x, c in criteria.items()}
        s['next_action'] = 'Resolve blockers and replan.' if blockers else 'Human reviews exact plan; record real approval of its canonical hash.'
        self.save(s, rev)
        return {'phase': s['phase'], 'plan': s['plan'], 'approval_subject_sha256': digest(plan), 'blockers': blockers}

    def approve(self, name):
        s = self.state()
        rev = s['revision']
        p = self.load_plan(s)
        require(s['phase'] == 'AWAITING_APPROVAL' and not p['blockers'], 'Plan is not eligible for approval')
        require(snapshot(self.root)['sha256'] == p['baseline']['sha256'], 'Workspace changed after planning')
        r = self.read(name, 'approval')
        self.approval(r, 'plan', digest(p), s['task_id'])
        s['approval'] = self.save_record(f'.bh/tasks/{s["task_id"]}/approvals/{digest(r)}.json', r, 'approval')
        self.move(s, 'APPROVED', 'Recorded structurally valid human approval; authenticity remains external')
        s['next_action'] = 'Confirm genuine approval in session, then run begin.'
        self.save(s, rev)
        return {'phase': s['phase'], 'authentication': 'NOT PROVIDED by shared writable records'}

    def authorized(self, s):
        p = self.load_plan(s)
        require(s['approval'] is not None, 'Missing technical-plan approval')
        self.artifact(s['approval'])
        self.approval(self.read(s['approval']['path'], 'approval'), 'plan', digest(p), s['task_id'])
        self.handoff(s['handoff']['path'])
        self.scope(p, snapshot(self.root))
        return p

    def begin(self):
        s = self.state()
        rev = s['revision']
        p = self.authorized(s)
        require(snapshot(self.root)['sha256'] == p['baseline']['sha256'], 'Initial execution baseline changed')
        self.move(s, 'EXECUTING', 'Begin only the approved bounded plan')
        s['next_action'] = p['proposal']['next_action']
        self.save(s, rev)
        return {'phase': s['phase']}

    def run_check(self, spec, snap, run_name, run_id, task):
        result = {'id': spec['id'], 'ac_ids': spec['ac_ids'], 'required': spec['required'], 'adapter': spec['adapter'],
                  'status': 'NOT_RUN', 'reason': 'Not executed', 'dependency_sha256': self.dependency_hash(spec, snap),
                  'command': [], 'working_directory': '.', 'tool_version': 'unavailable', 'exit_code': None,
                  'duration_seconds': 0.0, 'counts': dict.fromkeys(('discovered', 'passed', 'failed', 'skipped', 'inconclusive'), 0),
                  'failed_names': [], 'observations': [], 'artifacts': []}
        if spec['adapter'] == 'manual':
            result['reason'] = 'Human-only judgment remains pending; automation cannot perform it.'
            return result
        if not spec['required'] and spec['not_applicable_reason']:
            result.update(status='NOT_APPLICABLE', reason=spec['not_applicable_reason'])
            return result
        start = time.monotonic()
        process = None
        stopped = False
        outdir = safe(self.root, run_name + '/' + spec['id'])
        outdir.mkdir(parents=True, exist_ok=False)
        log = outdir / 'process.log'
        try:
            b, tool = self.binding_ready(spec)
            output = outdir / b['result_file']
            require(not output.exists(), 'Result path is not fresh')
            replacements = {'project': str(self.root), 'run_dir': str(outdir), 'result': str(output),
                            'log': str(outdir / 'unity.log'), 'project_id': self.config['project_id'],
                            'task_id': task, 'run_id': run_id}
            args = [str(tool['path'])] + [a.format_map(replacements) for a in b['arguments']]
            result.update(command=args, working_directory=b['working_directory'], tool_version=tool['observed_version'])
            allowed_env = ('PATH', 'SystemRoot', 'WINDIR', 'COMSPEC', 'TEMP', 'TMP', 'HOME', 'USERPROFILE',
                           'APPDATA', 'LOCALAPPDATA', 'ProgramFiles', 'ProgramFiles(x86)', 'DISPLAY')
            env = {k: v for k, v in os.environ.items() if k in allowed_env}
            env.update(PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
            with log.open('xb') as stream:
                process = subprocess.Popen(args, cwd=safe(self.root, b['working_directory'], True), stdout=stream,
                                           stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, shell=False, env=env,
                                           start_new_session=os.name != 'nt')
                while process.poll() is None:
                    if time.monotonic() - start > b['timeout_seconds']:
                        stopped = True
                        terminate_owned(process)
                        raise BHError('TIMEOUT: owned process stopped; inspect Windows child processes manually')
                    if log.stat().st_size > 16 * 1024 * 1024:
                        stopped = True
                        terminate_owned(process)
                        raise BHError('Log exceeded 16 MiB; process stopped, evidence retained')
                    time.sleep(0.025)
            result['exit_code'] = process.returncode
            if process.returncode != 0:
                tail = log.read_bytes()[-8192:].decode('utf-8', 'replace')
                unity_log = outdir / 'unity.log'
                if unity_log.is_file():
                    no_links(unity_log)
                    with unity_log.open('rb') as stream:
                        stream.seek(max(0, unity_log.stat().st_size - 8192))
                        tail += stream.read().decode('utf-8', 'replace')
                compile_failure = bool(re.search(r'error CS\d+|compilation failed|scripts have compiler errors', tail, re.I))
                result.update(status='FAIL' if output.is_file() or compile_failure else 'ERROR',
                              reason=('Compilation error; ' if compile_failure else '') + f'Process exited {process.returncode}; cannot pass')
            else:
                require(output.is_file(), 'MISSING_ARTIFACT: process returned zero without result')
                no_links(output)
                require(output.stat().st_size <= 16 * 1024 * 1024, 'Result exceeds size cap')
                parsed = parse_nunit(output, spec) if spec['adapter'] == 'nunit' else self.parse_observations(output, spec, b, task, run_id, outdir)
                result.update(parsed)
        except KeyboardInterrupt:
            stopped = True
            if process is not None and process.poll() is None:
                terminate_owned(process)
            result.update(status='ERROR', reason='CANCELLED by user; process evidence preserved; no retry')
        except (BHError, OSError, ValueError, ET.ParseError) as exc:
            result.update(status='BLOCKED' if process is None else 'ERROR', reason=str(exc))
        finally:
            if process is not None and process.poll() is None:
                terminate_owned(process)
            if process is not None:
                result['exit_code'] = process.poll()
            result['duration_seconds'] = round(time.monotonic() - start, 6)
            # Preserve logs even when parsing fails. Never follow a process-created link.
            for path in sorted(outdir.iterdir()):
                try:
                    no_links(path)
                    if path.is_file():
                        result['artifacts'].append({'path': path.relative_to(self.root).as_posix(), 'sha256': file_hash(path)})
                except (BHError, OSError) as exc:
                    result.update(status='ERROR', reason='Unsafe/unreadable output: ' + str(exc))
            if stopped:
                result['observations'].append('Only this wrapper-owned process was terminated; no existing Unity Editor was killed.')
        return result

    def parse_observations(self, output, spec, binding, task, run_id, outdir):
        value = load_json(output)
        require(isinstance(value, dict), 'Observation object required')
        self.identity(value, task)
        require(value.get('run_id') == run_id, 'Wrong/stale result run identity')
        if spec['adapter'] == 'diagnostics':
            require(value.get('source') == binding['diagnostic_source'] and value.get('analysis_complete') is True,
                    'Diagnostics incomplete or wrong source; a clean empty response is not proof')
            require(isinstance(value.get('issues'), list), 'Diagnostics issues array missing')
            baseline = load_json(self.artifact(binding['diagnostics_baseline']))
            require(baseline.get('source') == binding['diagnostic_source'], 'Wrong diagnostics baseline source')
            require(isinstance(baseline.get('issues'), list), 'Diagnostics baseline issues missing')
            def normalize(issue):
                require(isinstance(issue, dict) and all(k in issue for k in ('path', 'line', 'rule', 'message', 'severity')), 'Malformed diagnostic')
                portable(issue['path'])
                require(type(issue['line']) is int and issue['line'] >= 0, 'Invalid diagnostic line')
                require(all(isinstance(issue[x], str) for x in ('rule', 'message', 'severity')), 'Invalid diagnostic metadata')
                return (issue['path'], issue['line'], issue['rule'], issue['message'], issue['severity'])
            previous = {normalize(x) for x in baseline['issues']}
            new = [normalize(x) for x in value['issues'] if normalize(x) not in previous]
            return {'status': 'FAIL' if new else 'PASS', 'reason': f'{len(new)} new diagnostics against pinned baseline',
                    'observations': [f'Existing: {len(previous)}; current: {len(value["issues"])}; source: {value["source"]}'],
                    'failed_names': [str(x)[:1000] for x in new]}
        observed = value.get('observations')
        require(isinstance(observed, dict), 'Missing observed facts')
        failures = []
        notes = []
        for item in binding['expectations']:
            key = item['key']
            require(key in observed, f'Missing observed value: {key}')
            actual, expected = observed[key], item['value']
            if item['operator'] == 'equals':
                ok = type(actual) is type(expected) and actual == expected
            else:
                require(type(actual) in (int, float) and type(expected) in (int, float)
                        and math.isfinite(actual) and math.isfinite(expected), 'Numeric comparison requires actual finite numbers')
                ok = actual <= expected if item['operator'] == 'at_most' else actual >= expected
            notes.append(f'{key}: observed={actual!r}; expected {item["operator"]} {expected!r}; units={item["units"]}')
            if not ok:
                failures.append(key)
        if spec['adapter'] == 'build':
            require(value.get('build_result') in ('Succeeded', 'Failed', 'Cancelled', 'Unknown')
                    and type(value.get('errors')) is int and value['errors'] >= 0,
                    'Malformed Unity build result/errors')
            require(value.get('target') == binding['build_target'], 'Wrong Unity build target')
            if value['build_result'] == 'Failed' or value['errors'] > 0:
                return {'status': 'FAIL', 'reason': 'Unity reported build failure/errors',
                        'observations': notes, 'failed_names': ['Unity.BuildReport']}
            require(value['build_result'] == 'Succeeded', 'Unity build cancelled or outcome unknown')
            require(isinstance(value.get('outputs'), list) and bool(value['outputs']), 'Build report has no output artifacts')
            for entry in value['outputs']:
                validate(entry, 'artifact', self.schema)
                p = self.artifact(entry)
                require(p.resolve().is_relative_to(outdir.resolve()), 'Build outputs must be fresh in this run directory')
                require(p.stat().st_size > 0, 'Empty build output cannot prove a successful build')
        return {'status': 'FAIL' if failures else 'PASS',
                'reason': 'Observed values contradict approved expectation' if failures else 'Observed values match approved expectations',
                'observations': notes, 'failed_names': failures}

    def verification(self, profile):
        require(profile in TIERS, 'Unknown verification profile')
        s = self.state()
        rev = s['revision']
        plan = self.authorized(s)
        require(s['phase'] == 'EXECUTING', 'Verification requires EXECUTING; use explicit begin/recovery/resume')
        require('run-checks' in plan['allowed_actions'], 'Check execution not authorized')
        h, criteria, _ = self.handoff(s['handoff']['path'])
        selected = [x for x in h['checks'] if TIERS[x['profile']] <= TIERS[profile]]
        require(bool(selected), 'No checks selected; no verification receipt can pass')
        require(len(s['runs']) < 256, 'Run limit reached; preserve history and split/archive task explicitly')
        for spec in selected:
            tool = self.tools.get(self.bound.get(spec['id'], {}).get('tool_key'), {})
            if tool.get('kind') == 'unity':
                require('launch-unity' in plan['allowed_actions'], 'Unity launch is not authorized')
        run_id = 'run-' + uuid.uuid4().hex
        run_name = '.bh/runs/' + run_id
        start = utc()
        self.move(s, 'VERIFYING', 'Run approved verification; code/fixtures are not repaired during audit')
        s['pending_run'] = run_name
        s['next_action'] = 'Await current owned check result; interrupted runs require resume.'
        self.save(s, rev)
        rev = s['revision']
        snap = snapshot(self.root)
        results = []
        mutations = []
        atomic_json(safe(self.root, run_name + '/pending.json'), {'run_id': run_id, 'project_id': s['project_id'], 'task_id': s['task_id'], 'started': start})
        # The pending state deliberately survives an unexpected interruption before receipt persistence.
        for spec in selected:
            results.append(self.run_check(spec, snap, run_name, run_id, s['task_id']))
            after = snapshot(self.root)
            mutations = changed(snap['files'], after['files'])
            if mutations or snap['commit'] != after['commit']:
                results[-1].update(status='ERROR', reason='Audit changed tested inputs; no auto-repair/restore performed')
                break
            if 'CANCELLED' in results[-1]['reason'] or 'TIMEOUT' in results[-1]['reason']:
                break
        after = snapshot(self.root)
        receipt = {'version': VERSION, 'harness_version': VERSION, 'project_id': s['project_id'], 'task_id': s['task_id'],
                   'run_id': run_id, 'synthetic': s['synthetic'], 'started_utc': start, 'finished_utc': utc(),
                   'harness_sha256': self.harness_hash(), 'config_sha256': self.config_hash(), 'plan_sha256': s['plan']['sha256'],
                   'snapshot': snap, 'after_snapshot_sha256': after['sha256'],
                   'environment': {'os': platform.platform(), 'python': platform.python_version(), 'git': git(self.root, '--version').decode().strip()},
                   'profile': profile, 'results': results, 'audit_mutations': mutations,
                   'independence': 'deterministic-wrapper-same-workspace',
                   'limitations': ['Synthetic results are not Unity evidence.' if s['synthetic'] else 'Bound adapters ran; other live-host integration is not implied.',
                                   'Same user can edit code and evidence; no independent attestation.',
                                   'Human playtest/design quality remains unverified by automation.']}
        receipt_ref = self.save_record(run_name + '/receipt.json', receipt, 'receipt')
        s['runs'].append(receipt_ref['path'])
        s['pending_run'] = None
        scores, refs, gaps = self.audit_results(s, after)
        s['ac_status'], s['blockers'] = scores, gaps
        failed = [r for r in results if r['status'] == 'FAIL']
        infra = [r for r in results if r['status'] in ('ERROR', 'BLOCKED')]
        passed = sorted(k for k, v in scores.items() if v == 'PASS')
        if failed:
            fingerprint = digest([(r['id'], r['failed_names'], r['reason']) for r in failed])
            s['counters']['failed_rounds'] += 1
            s['counters']['repeat_failures'] = s['counters']['repeat_failures'] + 1 if s['last_fingerprint'] == fingerprint else 1
            s['counters']['no_progress_rounds'] = 0 if set(passed) - set(s['last_passed_ids']) else s['counters']['no_progress_rounds'] + 1
            s['last_fingerprint'] = fingerprint
        if infra:
            s['counters']['infrastructure_failures'] += 1
        s['last_passed_ids'] = passed
        threshold = any(s['counters'][k] >= self.config['budgets'][k]
                        for k in ('failed_rounds', 'repeat_failures', 'no_progress_rounds', 'infrastructure_failures'))
        ready = all(scores[c['id']] == 'PASS' for c in criteria.values() if c['kind'] == 'automated') and not gaps
        cancelled = any('CANCELLED' in r['reason'] for r in results)
        target = ('PAUSED' if threshold or cancelled else 'BLOCKED' if infra else 'FAILED' if failed
                  else 'READY_FOR_HUMAN_REVIEW' if ready else 'EXECUTING')
        self.move(s, target, 'Verification receipts evaluated; human acceptance remains separate')
        s['next_action'] = ('Human reviews return/evidence and performs pending playtest.' if ready else
                            'Inspect exact failed/not-run criteria; use bounded recovery or request missing binding/approval.')
        self.save(s, rev)
        return {'phase': s['phase'], 'receipt': receipt_ref, 'acceptance': scores, 'blockers': gaps}

    def audit_results(self, s, snap=None):
        snap = snap or snapshot(self.root)
        self.artifact(s['handoff'])
        h, criteria, _ = self.handoff(s['handoff']['path'])
        specs = {x['id']: x for x in h['checks']}
        latest = {}
        gaps = []
        current_profile = False
        for name in s['runs']:
            try:
                require(below(name, '.bh/runs') and Path(name).name == 'receipt.json', 'Receipt must be in the designated run tree')
                r = self.read(name, 'receipt')
                self.identity(r, s['task_id'])
                if s['plan'] is None or r['plan_sha256'] != s['plan']['sha256']:
                    continue  # Preserve superseded-plan history without treating it as current.
                require(r['harness_sha256'] == self.harness_hash() and r['config_sha256'] == self.config_hash(), 'Receipt core/configuration mismatch')
                require(r['run_id'] == Path(name).parent.name, 'Receipt path/run mismatch')
                require(r['snapshot']['sha256'] == digest({'commit': r['snapshot']['commit'], 'files': r['snapshot']['files']}), 'Receipt source snapshot hash is inconsistent')
                require(not r['audit_mutations'] and r['snapshot']['sha256'] == r['after_snapshot_sha256'], 'Audit mutation invalidates receipt')
                require(r['finished_utc'] >= r['started_utc'], 'Receipt timestamps reversed')
                current_profile = current_profile or TIERS[r['profile']] >= TIERS[h['required_profile']]
                unique(r['results'], 'id', 'receipt check IDs')
                for result in r['results']:
                    require(result['id'] in specs, 'Unknown receipt check')
                    spec = specs[result['id']]
                    require(result['ac_ids'] == spec['ac_ids'] and result['required'] == spec['required'] and result['adapter'] == spec['adapter'], 'Receipt changed requirement mapping')
                    require(result['dependency_sha256'] == self.dependency_hash(spec, r['snapshot']), 'Receipt dependency claim contradicts its source snapshot')
                    if result['dependency_sha256'] != self.dependency_hash(spec, snap):
                        latest[result['id']] = ('NOT_RUN', name, 'Stale tested-input dependencies')
                        continue
                    for artifact in result['artifacts']:
                        require(below(artifact['path'], str(Path(name).parent).replace('\\', '/')), 'Raw artifact outside its recorded run')
                        self.artifact(artifact)
                    require(result['status'] != 'PASS' or bool(result['artifacts']), 'Passing check has no raw artifacts')
                    if result['status'] == 'PASS':
                        require(result['exit_code'] == 0, 'Passing receipt has nonzero/missing process status')
                        binding = self.bound.get(spec['id'])
                        require(binding is not None, 'Passing receipt has no binding')
                        result_name = (Path(name).parent / spec['id'] / binding['result_file']).as_posix()
                        require(result_name in {a['path'] for a in result['artifacts']}, 'Receipt omits bound raw result')
                        output = safe(self.root, result_name)
                        parsed = parse_nunit(output, spec) if spec['adapter'] == 'nunit' else self.parse_observations(output, spec, binding, s['task_id'], r['run_id'], output.parent)
                        require(parsed['status'] == 'PASS', 'Raw artifact contradicts passing receipt')
                        if spec['adapter'] == 'nunit':
                            require(result['counts'] == parsed['counts'], 'Receipt test counts contradict raw result')
                    latest[result['id']] = (result['status'], name, result['reason'])
            except (BHError, OSError, ValueError, KeyError, ET.ParseError) as exc:
                gaps.append(f'Invalid receipt {name}: {exc}')
        if s['plan'] is not None and not current_profile:
            gaps.append('Required final verification profile has not run for this plan')
        scores, refs = {}, {}
        for ac, criterion in criteria.items():
            if criterion['kind'] == 'human':
                scores[ac], refs[ac] = 'HUMAN_PENDING', []
                continue
            needed = [spec for spec in specs.values() if spec['required'] and ac in spec['ac_ids']]
            entries = [latest.get(spec['id'], ('NOT_RUN', '', 'Required check has not run')) for spec in needed]
            statuses = [e[0] for e in entries]
            scores[ac] = ('PASS' if statuses and all(x == 'PASS' for x in statuses) else
                          next((x for x in ('ERROR', 'BLOCKED', 'FAIL', 'NOT_RUN') if x in statuses), 'BLOCKED'))
            refs[ac] = sorted({x[1] for x in entries if x[1]})
        return scores, refs, gaps

    def resume(self):
        s = self.state()
        rev = s['revision']
        self.artifact(s['handoff'])
        snap = snapshot(self.root)
        if s['plan'] is not None:
            self.scope(self.load_plan(s), snap)
        interrupted_note = []
        if s['pending_run']:
            interrupted = s['pending_run']
            require(below(interrupted, '.bh/runs'), 'Invalid pending run location')
            interrupted_note = [f'Interrupted run {interrupted}: no completed receipt; NOT_RUN. Inspect owned processes before retry.']
            atomic_json(safe(self.root, interrupted + '/interrupted.json'), {'status': 'ERROR', 'reason': 'Interrupted before complete receipt', 'at': utc()})
            s['pending_run'] = None
            if s['phase'] == 'VERIFYING':
                self.move(s, 'PAUSED', 'Recovered interrupted run without re-execution')
        scores, refs, gaps = self.audit_results(s, snap)
        s['ac_status'] = scores
        if s['phase'] == 'READY_FOR_HUMAN_REVIEW' and (gaps or any(v not in ('PASS', 'HUMAN_PENDING') for v in scores.values())):
            self.move(s, 'EXECUTING', 'Relevant edits invalidated prior verification')
        s['blockers'] = interrupted_note + gaps
        s['next_action'] = ('Read current plan, exact diff and checkpoint; do not re-execute completed work. Use explicit recover when paused/failed.'
                            if s['plan'] else 'Read pinned design inputs and prepare the bounded technical proposal; no game edits authorized.')
        self.save(s, rev)
        return {'phase': s['phase'], 'acceptance': scores, 'blockers': s['blockers']}

    def recovery(self, diagnosis):
        s = self.state()
        rev = s['revision']
        self.authorized(s)
        require(s['phase'] in ('FAILED', 'BLOCKED', 'PAUSED'), 'Recovery requires a failed, blocked, or paused task')
        require(len(diagnosis.strip()) >= 20, 'Supply a concrete diagnosis/evidence and one bounded next action')
        require(s['counters']['recovery_cycles'] < self.config['budgets']['recovery_cycles'], 'Recovery budget exhausted; human must revise scope/plan, not loop')
        s['counters']['recovery_cycles'] += 1
        self.move(s, 'EXECUTING', 'Bounded recovery: ' + diagnosis[:1500])
        s['next_action'] = diagnosis[:1500]
        self.save(s, rev)
        return {'phase': s['phase'], 'recovery_cycles': s['counters']['recovery_cycles']}

    def return_report(self):
        s = self.state()
        self.artifact(s['handoff'])
        h, criteria, _ = self.handoff(s['handoff']['path'])
        snap = snapshot(self.root)
        scores, refs, gaps = self.audit_results(s, snap)
        accepted = False
        if s['acceptance_record'] and s['plan']:
            self.artifact(s['acceptance_record'])
            r = self.read(s['acceptance_record']['path'], 'approval')
            subject = digest({'snapshot': snap['sha256'], 'plan': s['plan']['sha256'], 'handoff': s['handoff']['sha256']})
            accepted = (not gaps and r['subject_sha256'] == subject
                        and all(scores[k] == 'PASS' for k, c in criteria.items() if c['kind'] == 'automated'))
            if accepted:
                self.approval(r, 'acceptance', subject, s['task_id'])
                for c in r['human_criteria']:
                    scores[c['id']] = c['status']
        receipts = []
        for n in s['runs']:
            p = safe(self.root, n)
            if p.is_file():
                receipts.append({'path': n, 'sha256': file_hash(p)})
            else:
                gaps.append('Missing receipt: ' + n)
        value = {'version': VERSION, 'format': 'BH-RETURN-1.0.0', 'project_id': s['project_id'], 'task_id': s['task_id'],
                 'synthetic': s['synthetic'], 'created_utc': utc(), 'handoff_sha256': s['handoff']['sha256'],
                 'plan_sha256': s['plan']['sha256'] if s['plan'] else None, 'source_snapshot': snap,
                 'implementation_claims': s['claims'],
                 'acceptance': [{'id': k, 'expected': v['expected'], 'status': scores[k], 'receipt_refs': refs[k],
                                 'limitations': ['Human observation required'] if v['kind'] == 'human' and not accepted else []} for k, v in criteria.items()],
                 'receipts': receipts, 'deviations': list(dict.fromkeys(s['blockers'] + gaps)),
                 'design_questions': [q['question'] for q in h['questions']],
                 'human_acceptance': 'ACCEPTED_FOR_RECORDED_SNAPSHOT' if accepted else 'PENDING',
                 'evidence_transport': 'LOCAL_ONLY_UNTIL_UPLOADED_OR_PUBLISHED',
                 'review_independence': 'same-session-or-not-established', 'next_action': s['next_action']}
        validate(value, 'return', self.schema)
        name = f'.bh/exports/{s["task_id"]}/RETURN.json'
        atomic_json(safe(self.root, name), value)
        md = '# Implementation return\n\n' + ('SYNTHETIC FIXTURE — not game evidence.\n\n' if s['synthetic'] else '')
        md += f'Project/task: {s["project_id"]}/{s["task_id"]}\n\nHuman acceptance: {value["human_acceptance"]}\n\n'
        md += 'Claims: ' + '; '.join(s['claims']) + '\n\n'
        for c in value['acceptance']:
            md += f'- {c["id"]}: {c["status"]}; {c["expected"]}; receipts: {c["receipt_refs"]}\n'
        md += '\nEvidence is unavailable to the design GPT until the referenced files are actually uploaded or retrieved from a pinned repository revision. Local paths are not links.\n'
        if value['deviations']:
            md += '\nLimitations: ' + '; '.join(value['deviations']) + '\n'
        md += '\nNext: ' + s['next_action'] + '\n'
        safe(self.root, f'.bh/exports/{s["task_id"]}/RETURN.md').write_text(md, encoding='utf-8')
        return {'return': name, 'acceptance': scores, 'human_acceptance': value['human_acceptance'],
                'acceptance_subject_sha256': digest({'snapshot': snap['sha256'], 'plan': s['plan']['sha256'], 'handoff': s['handoff']['sha256']}) if s['plan'] else None}

    def accept(self, name):
        s = self.state()
        rev = s['revision']
        self.authorized(s)
        require(s['phase'] == 'READY_FOR_HUMAN_REVIEW', 'Automated readiness is required before acceptance')
        h, criteria, _ = self.handoff(s['handoff']['path'])
        snap = snapshot(self.root)
        scores, refs, gaps = self.audit_results(s, snap)
        require(not gaps and all(scores[k] == 'PASS' for k, c in criteria.items() if c['kind'] == 'automated'), 'Required automated verification is not passing/current')
        record = self.read(name, 'approval')
        subject = digest({'snapshot': snap['sha256'], 'plan': s['plan']['sha256'], 'handoff': s['handoff']['sha256']})
        self.approval(record, 'acceptance', subject, s['task_id'])
        humans = unique(record['human_criteria'], 'id', 'human criteria')
        require(humans.keys() == {k for k, c in criteria.items() if c['kind'] == 'human'}, 'Human playtest/deferral evidence is incomplete')
        for k, c in humans.items():
            scores[k] = c['status']
        s['acceptance_record'] = self.save_record(f'.bh/tasks/{s["task_id"]}/acceptance/{digest(record)}.json', record, 'approval')
        s['ac_status'] = scores
        self.move(s, 'ACCEPTED', 'Recorded human acceptance for exact tested snapshot only')
        s['next_action'] = 'Human controls Git integration; acceptance does not authorize merge/publish.'
        self.save(s, rev)
        return {'phase': s['phase'], 'authentication': 'External human source must be verified; record alone is not authentication'}

    def archive(self, task, expected_state_hash):
        s = self.state()
        require(s['phase'] in ('ACCEPTED', 'CANCELLED'), 'Only accepted/cancelled tasks can be archived')
        require(s['task_id'] == task and digest(s) == expected_state_hash, 'Archive subject changed; review current state')
        ref = self.save_record(f'.bh/tasks/{task}/closed/{expected_state_hash}.json', s, 'state')
        require(digest(self.state()) == expected_state_hash, 'Concurrent state change before archive')
        safe(self.root, '.bh/state.json').unlink()
        safe(self.root, '.bh/CHECKPOINT.md').write_text('# BH checkpoint\n\nNo active task. Closed task history remains at ' + ref['path'] + '.\n', encoding='utf-8')
        return {'status': 'ARCHIVED', 'closed_state': ref, 'next_action': 'Use a new unique task ID; prior evidence and approvals remain archived.'}

    def unlock(self, token, confirm_owner_stopped):
        require(confirm_owner_stopped, 'Explicit owner-stopped confirmation required')
        p = safe(self.root, '.bh/locks/writer.json')
        r = load_json(p)
        require(r.get('token') == token and r.get('host') == platform.node(), 'Wrong token or different host; manual owner investigation required')
        require(os.name != 'nt', 'Automatic PID probing is disabled on Windows; inspect lock owner manually without terminating processes')
        pid = r.get('pid')
        require(type(pid) is int and pid > 0, 'Invalid lock PID')
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            pass
        except PermissionError as exc:
            raise BHError('Lock owner status unknown; cannot unlock') from exc
        else:
            raise BHError('Lock owner process is still present; no unlock or process termination permitted')
        require(load_json(p) == r, 'Lock changed during recovery')
        p.unlink()
        return {'status': 'UNLOCKED', 'next_action': 'Inspect pending run/owned children, then resume explicitly.'}


def terminate_owned(process):
    if process.poll() is not None:
        return
    try:
        if os.name != 'nt':
            os.killpg(process.pid, signal.SIGTERM)
        else:
            process.terminate()
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            if os.name != 'nt':
                os.killpg(process.pid, signal.SIGKILL)
            else:
                process.kill()
            process.wait(timeout=3)
    except ProcessLookupError:
        pass


def parse_nunit(path, spec):
    raw = Path(path).read_bytes()
    require(len(raw) <= 16 * 1024 * 1024, 'NUnit artifact too large')
    require(b'<!DOCTYPE' not in raw.upper() and b'<!ENTITY' not in raw.upper(), 'DTD/entity XML rejected')
    root = ET.fromstring(raw)
    require(root.tag in ('test-run', 'test-results'), 'Unknown NUnit root')
    cases = list(root.iter('test-case'))
    require(bool(cases), 'ZERO_TESTS: no test-case elements')
    names = []
    counts = dict.fromkeys(('discovered', 'passed', 'failed', 'skipped', 'inconclusive'), 0)
    failed = []
    for case in cases:
        name = case.get('fullname') or case.get('name')
        require(bool(name), 'Unnamed test case')
        names.append(name)
        status = (case.get('result') or '').lower()
        if not status and case.get('executed') == 'False':
            status = 'skipped'
        if not status and case.get('success') is not None:
            status = 'passed' if case.get('success') == 'True' else 'failed'
        mapping = {'passed': 'passed', 'success': 'passed', 'failed': 'failed', 'failure': 'failed', 'error': 'failed',
                   'skipped': 'skipped', 'ignored': 'skipped', 'notrunnable': 'skipped', 'inconclusive': 'inconclusive'}
        require(status in mapping, f'Unknown NUnit outcome: {status}')
        counts['discovered'] += 1
        counts[mapping[status]] += 1
        if mapping[status] != 'passed':
            failed.append(name)
    require(len(names) == len(set(names)), 'Duplicate test-case names; ambiguous evidence')
    if root.get('total') is not None:
        require(int(root.get('total')) == len(cases), 'NUnit total disagrees with actual test cases')
    for key in ('passed', 'failed', 'skipped', 'inconclusive'):
        if root.get(key) is not None:
            require(int(root.get(key)) == counts[key], f'NUnit {key} count disagrees with cases')
    require(set(spec['test_names']) <= set(names), 'Required named tests were not discovered')
    require(counts['discovered'] >= spec['minimum_tests'], 'Too few discovered tests')
    failed_suites = [node.get('fullname') or node.get('name') or node.tag
                     for node in root.iter() if node.tag in ('test-run', 'test-suite', 'test-results')
                     and ((node.get('result') or '').lower() in ('failed', 'failure', 'error', 'inconclusive')
                          or (node.get('success') or '').lower() == 'false')]
    ok = counts['passed'] == counts['discovered'] and not failed_suites
    return {'status': 'PASS' if ok else 'FAIL',
            'reason': 'All required discovered tests passed' if ok else 'Failures/skips/inconclusive tests or suite failures prevent a pass',
            'counts': counts, 'failed_names': failed + failed_suites,
            'observations': [f'Parsed {len(cases)} actual NUnit test-case elements']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='.')
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('preflight', 'begin', 'resume', 'status', 'checkpoint', 'return'):
        sub.add_parser(name)
    p = sub.add_parser('validate-handoff')
    p.add_argument('path')
    p.add_argument('--draft', action='store_true')
    for name in ('init', 'plan', 'approve', 'accept'):
        p = sub.add_parser(name)
        p.add_argument('path')
    p = sub.add_parser('verify')
    p.add_argument('--profile', choices=TIERS, required=True)
    for name in ('pause', 'cancel', 'recover', 'claim'):
        p = sub.add_parser(name)
        p.add_argument('reason')
    p = sub.add_parser('archive')
    p.add_argument('--task', required=True)
    p.add_argument('--expected-state-hash', required=True)
    p = sub.add_parser('unlock')
    p.add_argument('--token', required=True)
    p.add_argument('--confirm-owner-stopped', action='store_true')
    args = parser.parse_args(argv)
    try:
        require(sys.version_info >= (3, 11), 'Python 3.11+ required; no automatic install')
        h = Harness(args.root)
        if args.command == 'preflight':
            out = h.preflight()
        elif args.command == 'validate-handoff':
            h.handoff(args.path, not args.draft)
            out = {'status': 'STRUCTURALLY_VALID_DRAFT' if args.draft else 'ELIGIBLE_FOR_RECONCILIATION',
                   'limitations': 'Not authentication, execution authorization, or design-quality proof'}
        elif args.command == 'status':
            s = h.state()
            scores, refs, gaps = h.audit_results(s)
            out = {'phase': s['phase'], 'acceptance': scores, 'gaps': gaps, 'next_action': s['next_action'], 'state_sha256': digest(s)}
        elif args.command == 'unlock':
            out = h.unlock(args.token, args.confirm_owner_stopped)
        else:
            with h.lock():
                if args.command == 'init':
                    out = h.initialize(args.path)
                elif args.command == 'plan':
                    out = h.make_plan(args.path)
                elif args.command == 'approve':
                    out = h.approve(args.path)
                elif args.command == 'begin':
                    out = h.begin()
                elif args.command == 'verify':
                    out = h.verification(args.profile)
                elif args.command == 'resume':
                    out = h.resume()
                elif args.command == 'return':
                    out = h.return_report()
                elif args.command == 'accept':
                    out = h.accept(args.path)
                elif args.command == 'recover':
                    out = h.recovery(args.reason)
                elif args.command == 'archive':
                    out = h.archive(args.task, args.expected_state_hash)
                else:
                    s = h.state()
                    rev = s['revision']
                    if args.command == 'checkpoint':
                        h.checkpoint(s)
                        out = {'status': 'REGENERATED_FROM_STATE'}
                    else:
                        if args.command == 'claim':
                            require(s['phase'] == 'EXECUTING', 'Claims can only be recorded during execution')
                            h.authorized(s)
                            s['claims'].append(args.reason)
                        else:
                            h.move(s, 'PAUSED' if args.command == 'pause' else 'CANCELLED', args.reason)
                        s['next_action'] = args.reason
                        h.save(s, rev)
                        out = {'phase': s['phase']}
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 2 if out.get('status') == 'BLOCKED' or out.get('phase') in ('BLOCKED', 'FAILED', 'PAUSED') or out.get('gaps') else 0
    except (BHError, OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(json.dumps({'status': 'BLOCKED', 'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
