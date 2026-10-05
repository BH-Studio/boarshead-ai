#!/usr/bin/env python3
"""Validate BH-authored Unity procedure metadata/references, not live host behavior.

This accepts BH's restricted flat name/description frontmatter, not arbitrary YAML.
No parser dependency or vendor script is installed or executed.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import re
import sys


def frontmatter(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError('Missing closed frontmatter')
    fields = {}
    for line in match.group(1).splitlines():
        m = re.fullmatch(r'(name|description): (.+)', line)
        if not m or m[1] in fields:
            raise ValueError('Unsupported or duplicate BH frontmatter field')
        raw = m[2]
        if raw.startswith('"'):
            value = json.loads(raw)
        else:
            if (raw[0] in "[]{}'&*!#?:>|%@`" or ': ' in raw or ' #' in raw
                    or raw.casefold() in ('true', 'false', 'yes', 'no', 'on', 'off', 'null', '~')
                    or re.fullmatch(r'[+-]?(?:[0-9][0-9_.]*(?:[eE][+-]?[0-9]+)?|0[xob][0-9a-fA-F]+)', raw)):
                raise ValueError('Unsupported YAML construct; use a JSON-quoted scalar')
            value = raw
        if not isinstance(value, str) or not value.strip() or '\x00' in value:
            raise ValueError('Empty or invalid metadata scalar')
        fields[m[1]] = value
    if set(fields) != {'name', 'description'} or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', fields['name']):
        raise ValueError('Invalid BH name/description')
    return fields


def activation_metadata(text):
    """Accept the complete five-line BH activation profile, not arbitrary YAML."""
    quoted = r'("(?:[^"\\\n]|\\.)*")'
    pattern = (r'interface:\r?\n  display_name: ' + quoted
               + r'\r?\n  short_description: ' + quoted
               + r'\r?\npolicy:\r?\n  allow_implicit_invocation: false\r?\n?')
    match = re.fullmatch(pattern, text)
    if not match:
        raise ValueError('Invalid BH activation metadata or implicit invocation')
    return [json.loads(value) for value in match.groups()]


def reference_errors(path, root):
    errors = []
    for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        ref = ref.split('#', 1)[0]
        if not ref or re.match(r'https?://', ref):
            continue
        target = path.parent / ref
        if not target.resolve().is_relative_to(root.resolve()):
            errors.append('Reference escapes package: ' + ref)
        elif any(p.is_symlink() for p in (target, *target.parents)) or not target.is_file():
            errors.append('Missing or linked reference: ' + ref)
    return errors


def check(package):
    root = Path(package).resolve()
    errors, checked = [], []
    def test(ok, label):
        checked.append(label)
        if not ok:
            errors.append(label)
    core = root / 'project-template/.agents/skills'
    skills = sorted(core.glob('*/SKILL.md'))
    test(len(skills) == 5, 'Exactly five core skills')
    optional = root / 'optional/bh-unity-project-audit/SKILL.md'
    skills += [optional, root / 'optional/bh-procedural-regression/SKILL.md']
    names = []
    for path in skills:
        try:
            data = frontmatter(path.read_text(encoding='utf-8'))
            names.append(data['name'])
            test(data['name'] == path.parent.name, 'Skill name matches folder: ' + path.parent.name)
            if path.is_relative_to(core) or path == optional:
                meta = (path.parent / 'agents/openai.yaml').read_text(encoding='utf-8')
                try:
                    display, description = activation_metadata(meta)
                    valid = display == data['name'] and bool(description.strip())
                except ValueError:
                    valid = False
                test(valid, 'Explicit invocation metadata: ' + path.parent.name)
            problems = reference_errors(path, root)
            test(not problems, 'Complete local skill references: ' + path.parent.name)
            errors.extend(problems)
        except (OSError, ValueError) as exc:
            errors.append(str(path.relative_to(root)) + ': ' + str(exc))
    test(len(names) == len(set(names)), 'No duplicate BH skill names')
    try:
        directory = root / 'optional/unity-observation'
        source = ast.parse((directory / 'unity_jobs.py').read_text(encoding='utf-8'))
        constants = {n.targets[0].id: ast.literal_eval(n.value) for n in source.body
                     if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name)
                     and n.targets[0].id in ('CONFIG_FIELDS', 'ENVELOPE_FIELDS')}
        config = json.loads((directory / 'provider.disabled.json').read_text(encoding='utf-8'))
        test(set(config) == set(constants['CONFIG_FIELDS']), 'Disabled config uses actual protocol fields')
        test(config['enabled'] is False and config['provider_tool'] == 'UNCONFIGURED'
             and not config['required_capabilities'] and not config['provider_arguments']
             and not config['provider_inputs'], 'Provider example cannot silently activate')
        for name in ('README.md', 'PROVIDER_PROTOCOL.md'):
            path = directory / name
            test(path.is_file() and not reference_errors(path, root), 'Optional document references: ' + name)
        protocol = (directory / 'PROVIDER_PROTOCOL.md').read_text(encoding='utf-8')
        test(all(name in protocol for name in constants['ENVELOPE_FIELDS']), 'Documented response field coverage')
        schema = json.loads((root / 'project-template/.bh/schema.json').read_text())
        test(schema['$defs']['binding']['properties']['reuse_policy']['enum'] == ['source-bound', 'never'],
             'Explicit fresh-observation binding support')
        manifest = json.loads((root / 'PACKAGE_FILES.json').read_text())
        paths = {row['path'] for row in manifest['files']}
        actual = {p.relative_to(root / 'project-template').as_posix() for p in (root / 'project-template').rglob('*')
                  if p.is_file() and '__pycache__' not in p.parts}
        test(paths == actual and len(paths) == len(manifest['files']), 'Exact default-install path coverage')
        for row in manifest['files']:
            path = root / 'project-template' / row['path']
            test(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == row['sha256'],
                 'Installed hash: ' + row['path'])
        test(not any('unity_jobs.py' in p or 'unity_evidence.py' in p or 'project-audit/SKILL.md' in p for p in paths),
             'Optional runner/audit excluded from default discovery')
        guide = root / 'project-template/Docs/Harness/UNITY_PROCEDURES.md'
        test(guide.is_file() and not reference_errors(guide, root), 'Conditional Unity guide available')
    except (OSError, ValueError, KeyError, SyntaxError) as exc:
        errors.append('Unity authoring metadata: ' + str(exc))
    return {'status': 'FAIL' if errors else 'PASS_UNITY_AUTHORING_SUBSET', 'checks': len(checked),
            'problems': errors, 'limits': ['Restricted BH metadata/reference checks, not a general YAML validator.',
                                         'Not a complete design/package validation or native Codex/Unity test.']}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package', type=Path, default=Path(__file__).resolve().parents[1])
    result = check(p.parse_args().package)
    print(json.dumps(result, indent=2))
    sys.exit(1 if result['problems'] else 0)
