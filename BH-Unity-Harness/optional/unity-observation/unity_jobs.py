#!/usr/bin/env python3
"""Run one explicitly configured Unity observation through a reviewed provider.

The BH-UNITY-PROVIDER-1 protocol is a BH interface, NOT a Unity CLI command claim.
A project must supply a verified local mapping/provider. No provider is enabled
or installed by this module. One submit, bounded local polling, no auto restart.
"""
from __future__ import annotations
import argparse
import csv
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import uuid
import bh
import unity_evidence as evidence

PROTOCOL = 'BH-UNITY-PROVIDER-1'
STATES = {'ready', 'accepted', 'running', 'completed', 'busy', 'unavailable',
          'interrupted', 'failed', 'cancelled'}
CONFIG_FIELDS = ('version', 'enabled', 'project_id', 'operation', 'session_id',
                 'capabilities_sha256', 'required_capabilities', 'provider_tool',
                 'provider_arguments', 'provider_inputs', 'deadline_seconds',
                 'poll_interval_seconds', 'max_polls', 'max_response_bytes', 'spec')
ENVELOPE_FIELDS = ('protocol', 'project_id', 'project_path', 'run_id', 'request_sha256',
                   'session_id', 'capabilities_sha256', 'capabilities', 'job_id', 'state', 'result')


def configure(h, path, check, run_id, task, project, result):
    """Validate the real parent verification context; do not invent authorization."""
    config = bh.load_json(bh.safe(h.root, path))
    evidence.fields(config, CONFIG_FIELDS, 'Unity operation config')
    bh.require(config['version'] == '1.0.0' and config['enabled'] is True, 'Unity provider disabled/unconfigured')
    bh.require(config['project_id'] == project == h.config['project_id'], 'Wrong project')
    bh.require('unity-observation' in h.config['enabled_capabilities'], 'Unity observation capability not adopted')
    bh.require(config['operation'] in evidence.REDUCERS, 'Unsupported observation')
    evidence.text(config['session_id'], 'session id', 256)
    bh.require(re.fullmatch('[0-9a-f]{64}', config['capabilities_sha256']) is not None, 'Unpinned capability schema')
    evidence.strings(config['required_capabilities'], 'required capabilities', 1, 32)
    evidence.integer(config['deadline_seconds'], 'deadline', 1, 1800)
    evidence.integer(config['max_polls'], 'poll count', 1, 200)
    evidence.integer(config['max_response_bytes'], 'response cap', 256, evidence.MAX_BYTES)
    interval = config['poll_interval_seconds']
    bh.require(type(interval) in (float, int) and 0.05 <= interval <= 30, 'Invalid polling interval')
    bh.require(bh.safe(h.root, '.bh/locks/writer.json').is_file(), 'Parent writer lock is required')
    state = h.state()
    bh.require(state['phase'] == 'VERIFYING' and state['pending_run'] == '.bh/runs/' + run_id,
               'Only a current parent verification may run an observation')
    bh.require(state['task_id'] == task, 'Wrong task')
    # The parent checks scope before and after its child. Revalidate the immutable
    # authority records here, without repeating a whole-project asset snapshot.
    plan = h.load_plan(state)
    bh.require(state['approval'] is not None, 'Parent plan approval missing')
    h.artifact(state['approval'])
    h.approval(h.read(state['approval']['path'], 'approval'), 'plan', bh.digest(plan), task)
    bh.require('run-checks' in plan['allowed_actions'] and check in plan['check_ids'], 'Unapproved check')
    handoff, _, _ = h.handoff(state['handoff']['path'])
    spec = next(item for item in handoff['checks'] if item['id'] == check)
    bh.require(spec['adapter'] == 'facts', 'Observation adapter must use the facts contract')
    binding, _ = h.binding_ready(spec)
    bh.require(binding.get('reuse_policy') == 'never', 'Live observations require reuse_policy=never')
    bh.require(config['deadline_seconds'] + 5 <= binding['timeout_seconds'], 'Parent timeout needs journal grace')
    pinned = {entry['path']: entry['sha256'] for entry in binding['input_files']}
    bh.require(pinned.get(path) == bh.file_hash(bh.safe(h.root, path)), 'Operation configuration is not pinned')
    bh.require(type(config['provider_inputs']) is list and len(config['provider_inputs']) <= 32, 'Invalid provider inputs')
    for entry in config['provider_inputs']:
        evidence.fields(entry, ('path', 'sha256'), 'provider input')
        bh.require(pinned.get(entry['path']) == entry['sha256'], 'Provider input is not in parent reviewed inputs')
        h.artifact(entry)
    bh.require(config['provider_tool'] in h.tools, 'Provider executable unconfigured')
    tool = h.tools[config['provider_tool']]
    exe = Path(tool['path'])
    bh.no_links(exe)
    bh.require(exe.is_absolute() and exe.is_file() and bh.file_hash(exe) == tool['sha256'], 'Provider executable changed')
    bh.require(tool['kind'] in ('native', 'python'), 'Provider must not launch a batch Editor')
    bh.require(exe.stem.lower() not in ('cmd', 'pwsh', 'powershell', 'sh', 'bash', 'zsh', 'wscript', 'cscript'),
               'Shell providers unsupported')
    args = config['provider_arguments']
    bh.require(type(args) is list and 0 < len(args) <= 64, 'Provider arguments required')
    for arg in args:
        evidence.text(arg, 'argument', 2000)
        bh.require(not any(c in arg for c in ('\n', '\r', '\x00')), 'Argument control character')
        bh.require(set(re.findall(r'\{([^{}]+)\}', arg)) <= {'action', 'request', 'job_id', 'project'}, 'Unknown provider placeholder')
    bh.require('{action}' in args and '{request}' in args and '{project}' in args and '{job_id}' in args, 'Explicit action/request/project required')
    if tool['kind'] == 'python':
        bh.require(args[0] in ['{project}/' + item['path'] for item in config['provider_inputs']],
                   'Python provider entry must be pinned; -c/-m are not supported')
    output = Path(result).absolute()
    expected = bh.safe(h.root, f'.bh/runs/{run_id}/{check}/{binding["result_file"]}')
    bh.require(output == expected and not expected.exists(), 'Wrong or occupied result path')
    return config, tool, expected


def envelope(value, config, request, job=None, probe=False):
    evidence.fields(value, ENVELOPE_FIELDS, 'provider response')
    for key in ('project_id', 'run_id', 'request_sha256'):
        bh.require(value[key] == request[key], 'Provider identity mismatch: ' + key)
    bh.require(value['protocol'] == PROTOCOL and value['project_path'] == request['project_path'], 'Wrong protocol/project path')
    bh.require(value['session_id'] == config['session_id'] and
               value['capabilities_sha256'] == config['capabilities_sha256'], 'Editor session/capabilities changed')
    capabilities = evidence.strings(value['capabilities'], 'capabilities', 0, 128)
    bh.require(set(config['required_capabilities']) <= set(capabilities), 'Required capability unavailable')
    bh.require(value['state'] in STATES, 'Unknown provider state')
    if probe:
        bh.require(value['state'] == 'ready' and value['job_id'] is None and value['result'] is None,
                   'Editor not ready; no operation submitted')
    elif job is not None:
        bh.require(value['job_id'] == job, 'Wrong job identity')
    elif value['state'] not in ('busy', 'unavailable', 'failed', 'interrupted', 'cancelled'):
        evidence.text(value['job_id'], 'job id', 256)
    if value['state'] != 'completed':
        bh.require(value['result'] is None, 'Nonterminal response contains premature result')
    return value


def invoke(root, config, tool, action, request_path, job, outdir, index, deadline):
    """Each child has bounded output and wall time; no model participates in polling."""
    remaining = deadline - time.monotonic()
    bh.require(remaining > 0, 'Operation deadline reached')
    replacements = {'action': action, 'request': str(request_path), 'job_id': job or '', 'project': str(root)}
    args = [tool['path']] + [arg.format_map(replacements) for arg in config['provider_arguments']]
    # Recheck execution inputs across every process boundary.
    bh.require(bh.file_hash(tool['path']) == tool['sha256'], 'Provider executable changed during job')
    for item in config['provider_inputs']:
        bh.require(bh.file_hash(bh.safe(root, item['path'])) == item['sha256'], 'Provider helper changed during job')
    stdout = bh.safe(root, (outdir / f'provider-{index:03d}.json').relative_to(root).as_posix())
    stderr = bh.safe(root, (outdir / f'provider-{index:03d}.log').relative_to(root).as_posix())
    process = None
    env = {key: value for key, value in os.environ.items() if key in
           ('PATH', 'SystemRoot', 'WINDIR', 'TEMP', 'TMP', 'HOME', 'USERPROFILE', 'APPDATA', 'LOCALAPPDATA')}
    env.update(PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
    try:
        with stdout.open('xb') as out, stderr.open('xb') as err:
            process = subprocess.Popen(args, cwd=root, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                       env=env, shell=False, start_new_session=os.name != 'nt')
            while process.poll() is None:
                bh.require(time.monotonic() < deadline, 'Provider operation timed out; server cancellation NOT established')
                bh.require(stdout.stat().st_size <= config['max_response_bytes'] and
                           stderr.stat().st_size <= config['max_response_bytes'], 'Provider output exceeded cap')
                time.sleep(0.02)
        bh.no_links(stdout); bh.no_links(stderr)
        bh.require(stdout.stat().st_size <= config['max_response_bytes'] and
                   stderr.stat().st_size <= config['max_response_bytes'], 'Provider output exceeded cap')
        bh.require(time.monotonic() <= deadline, 'Late provider result')
        bh.require(process.returncode == 0, f'Provider exited {process.returncode}; inspect retained log')
        return bh.load_json(stdout)
    finally:
        if process is not None and process.poll() is None:
            bh.terminate_owned(process)


def run(h, config_path, check, run_id, task, project, result):
    config, tool, output = configure(h, config_path, check, run_id, task, project, result)
    directory = output.parent
    journal_path = bh.safe(h.root, (directory / 'unity-job.json').relative_to(h.root).as_posix())
    bh.require(not journal_path.exists(), 'Job journal already exists; inspect it, never resubmit blindly')
    request_path = bh.safe(h.root, (directory / 'unity-request.json').relative_to(h.root).as_posix())
    bh.require(not request_path.exists(), 'Request path occupied')
    request = {'protocol': PROTOCOL, 'project_id': project, 'project_path': str(h.root), 'task_id': task,
               'run_id': run_id, 'operation': config['operation'], 'session_id': config['session_id'],
               'capabilities_sha256': config['capabilities_sha256'], 'spec': config['spec'],
               'artifact_directory': str(directory)}
    request['request_sha256'] = bh.digest(request)
    bh.atomic_json(request_path, request)
    journal = {'protocol': PROTOCOL, 'project_id': project, 'run_id': run_id, 'check_id': check,
               'request_sha256': request['request_sha256'], 'session_id': config['session_id'],
               'state': 'PROBING', 'job_id': None, 'polls': 0, 'started_utc': bh.utc(),
               'deadline_seconds': config['deadline_seconds'], 'cancellation_requested': False,
               'server_may_be_running': False}
    deadline = time.monotonic() + config['deadline_seconds']
    bh.atomic_json(journal_path, journal)
    owner_path = bh.safe(h.root, '.bh/locks/unity-job.json')
    token = uuid.uuid4().hex
    owner = {'token': token, 'project_id': project, 'task_id': task, 'run_id': run_id,
             'session_id': config['session_id'], 'journal': journal_path.relative_to(h.root).as_posix()}
    try:
        with owner_path.open('x', encoding='utf-8') as stream:
            json.dump(owner, stream)
    except FileExistsError as exc:
        raise bh.BHError('An earlier Unity job has unresolved ownership; inspect its journal before any new submit') from exc
    try:
        envelope(invoke(h.root, config, tool, 'probe', request_path, None, directory, 0, deadline), config, request, probe=True)
        journal.update(state='SUBMITTING', server_may_be_running=True)
        bh.atomic_json(journal_path, journal)  # Survives an uncertain submit or lost response.
        value = envelope(invoke(h.root, config, tool, 'submit', request_path, None, directory, 1, deadline), config, request)
        job = value['job_id']; journal.update(job_id=job, state=value['state'])
        bh.atomic_json(journal_path, journal)
        while value['state'] in ('accepted', 'running'):
            bh.require(journal['polls'] < config['max_polls'], 'Polling budget exhausted; server cancellation NOT established')
            remaining = deadline - time.monotonic()
            bh.require(remaining > config['poll_interval_seconds'], 'Operation deadline reached; server may still run')
            time.sleep(config['poll_interval_seconds'])
            journal['polls'] += 1
            value = envelope(invoke(h.root, config, tool, 'status', request_path, job, directory,
                                    journal['polls'] + 1, deadline), config, request, job=job)
            journal['state'] = value['state']; bh.atomic_json(journal_path, journal)
        if value['state'] in ('completed', 'failed', 'cancelled'):
            journal['server_may_be_running'] = False
        bh.require(value['state'] == 'completed', 'Operation ended without completed evidence: ' + value['state'])
        observations, summary = evidence.reduce_result(config['operation'], config['spec'], value['result'], h.root, directory)
        bh.atomic_json(directory / 'unity-summary.json', summary)
        # Configuration and immutable operation inputs must still be the approved bytes.
        configure(h, config_path, check, run_id, task, project, result)
        bh.atomic_json(output, {'project_id': project, 'task_id': task, 'run_id': run_id,
                                'observations': observations})
        journal.update(state='COMPLETED', server_may_be_running=False, finished_utc=bh.utc())
        bh.atomic_json(journal_path, journal)
        return observations
    except BaseException as exc:
        journal.update(state='INCOMPLETE', finished_utc=bh.utc(), error=str(exc)[:1000])
        bh.atomic_json(journal_path, journal)
        raise
    finally:
        if not journal['server_may_be_running'] and owner_path.exists():
            bh.require(bh.load_json(owner_path).get('token') == token, 'Unity ownership record changed')
            owner_path.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('root', 'config', 'check', 'run', 'task', 'project', 'result'):
        parser.add_argument('--' + key, required=True)
    args = parser.parse_args(argv)
    try:
        result = run(bh.Harness(args.root), args.config, args.check, args.run, args.task, args.project, args.result)
        print(json.dumps({'status': 'OBSERVED', 'observations': result}))
        return 0
    except (bh.BHError, OSError, ValueError, KeyError, TypeError, csv.Error, subprocess.SubprocessError) as exc:
        print(json.dumps({'status': 'INCOMPLETE', 'error': str(exc)[:1000],
                          'server_cancellation': 'NOT_REQUESTED_OR_ESTABLISHED'}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
