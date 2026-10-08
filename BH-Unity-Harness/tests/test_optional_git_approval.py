"""Real local workflows in synthetic projects; no Unity or human authentication."""
import io
import shutil
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from support import Fixture, bh, install, git, write


class OptionalGitApprovalTests(unittest.TestCase):
    def fixture(self, git_enabled=False):
        f = Fixture(git_enabled=git_enabled)
        self.addCleanup(f.close)
        return f

    def plan(self, f):
        with f.h.lock():
            f.h.initialize('Handoff/handoff.json')
            return f.h.make_plan('.bh/tasks/task-01/proposal.json')

    def approve(self, f):
        with f.h.lock():
            return f.h.approve(by='SYNTHETIC reviewer', source='SYNTHETIC explicit approval message')

    def ready(self, f):
        self.plan(f)
        self.approve(f)
        with f.h.lock():
            f.h.begin()

    def test_full_workflow_without_git_executable_or_repository(self):
        f = self.fixture()
        which = bh.shutil.which
        with patch.object(bh.shutil, 'which', side_effect=lambda name: None if name == 'git' else which(name)), \
                patch.object(bh, 'git', side_effect=AssertionError('Git must not be invoked')):
            self.assertEqual(f.h.preflight()['status'], 'PREFLIGHT_ONLY')
            self.ready(f)
            result = f.verify()
            self.assertEqual(f.h.state()['ac_status']['AC-01'], 'PASS', result)
            receipt = bh.load_json(f.root / f.h.state()['runs'][-1])
            self.assertIsNone(receipt['snapshot']['commit'])
            self.assertIn('UNAVAILABLE', receipt['environment']['git'])
            with f.h.lock():
                f.h.return_report()
            self.assertEqual(f.accept()['phase'], 'ACCEPTED')
            with f.h.lock():
                self.assertEqual(f.h.resume()['phase'], 'ACCEPTED')

    def test_existing_repository_works_when_git_is_missing(self):
        f = self.fixture(True)
        with patch.object(bh.shutil, 'which', return_value=None), patch.object(bh, 'git', side_effect=AssertionError('No Git')):
            self.ready(f)
            f.verify()
            self.assertEqual(f.h.state()['ac_status']['AC-01'], 'PASS')

    def test_unborn_repository_uses_file_snapshot(self):
        f = self.fixture()
        git(f.root, 'init', '-q')
        self.ready(f)
        self.assertIsNone(bh.snapshot(f.root)['commit'])
        f.verify()
        self.assertEqual(f.h.state()['ac_status']['AC-01'], 'PASS')

    def test_project_inside_parent_repository_uses_own_root(self):
        f = self.fixture(True)
        nested = f.root / 'Nested'
        write(nested, 'ProjectSettings/ProjectVersion.txt', 'SYNTHETIC fixture')
        write(nested, 'Assets/value.txt', 'one')
        snap = bh.snapshot(nested)
        self.assertIsNone(snap['commit'])
        self.assertEqual(set(snap['files']), {'ProjectSettings/ProjectVersion.txt', 'Assets/value.txt'})

    def test_broken_metadata_or_git_read_failure_does_not_block(self):
        f = self.fixture()
        write(f.root, '.git', 'gitdir: missing-repository\n')
        for error in (bh.BHError('Git read failed'), OSError('unavailable')):
            with patch.object(bh, 'git', side_effect=error):
                self.assertIsNone(bh.snapshot(f.root)['commit'])
                self.assertEqual(f.h.preflight()['status'], 'PREFLIGHT_ONLY')

    def test_file_snapshot_prunes_caches_and_journals_before_traversal(self):
        f = self.fixture()
        for name in ('Library', 'Temp', 'Logs', '.bh/runs'):
            write(f.root, name + '/bad-name.', 'ignored volatile input')
        original = bh.Path.iterdir
        def visit(path):
            self.assertNotIn(path, [f.root / n for n in ('Library', 'Temp', 'Logs', '.bh/runs')])
            return original(path)
        with patch.object(bh.Path, 'iterdir', visit):
            first = bh.snapshot(f.root)
            second = bh.snapshot(f.root)
        self.assertEqual(first, second)
        self.assertTrue(first['dirty'])
        self.assertFalse(any(p.startswith(('Library/', 'Temp/', 'Logs/', '.bh/runs/')) for p in first['files']))

    def test_no_git_snapshot_detects_add_edit_delete(self):
        f = self.fixture()
        first = bh.snapshot(f.root)
        write(f.root, 'Source/new.txt', 'new')
        write(f.root, 'Source/value.json', {'value': 2})
        (f.root / 'Source/unrelated.txt').unlink()
        second = bh.snapshot(f.root)
        self.assertEqual(bh.changed(first['files'], second['files']), ['Source/new.txt', 'Source/unrelated.txt', 'Source/value.json'])
        self.assertNotEqual(first['sha256'], second['sha256'])

    def test_no_git_stale_plan_cannot_be_approved(self):
        f = self.fixture()
        self.plan(f)
        write(f.root, 'Source/value.json', {'value': 2})
        with self.assertRaisesRegex(bh.BHError, 'Workspace changed'):
            self.approve(f)
        self.assertIsNone(f.h.state()['approval'])

    def test_no_git_stale_verification_is_not_reused(self):
        f = self.fixture()
        self.ready(f)
        f.verify()
        write(f.root, 'Source/value.json', {'value': 2})
        with f.h.lock():
            f.h.resume()
        self.assertEqual(f.h.state()['ac_status']['AC-01'], 'NOT_RUN')

    def test_no_git_protected_and_out_of_scope_changes_block(self):
        for path in ('Other/new.txt', 'Tests/fixture_driver.py'):
            with self.subTest(path=path):
                f = self.fixture()
                self.ready(f)
                write(f.root, path, 'changed')
                with self.assertRaises(bh.BHError), f.h.lock():
                    f.h.verification('slice')

    def test_no_git_case_collisions_and_lfs_pointers_block(self):
        f = self.fixture()
        write(f.root, 'Source/Case.txt', 'one')
        write(f.root, 'Source/case.txt', 'two')
        if (f.root / 'Source/Case.txt').read_text() != 'one':
            self.skipTest('Host filesystem is case-insensitive')
        with self.assertRaisesRegex(bh.BHError, 'Case-colliding'):
            bh.snapshot(f.root)
        (f.root / 'Source/case.txt').unlink()
        write(f.root, 'Source/pointer', 'version https://git-lfs.github.com/spec/v1\noid sha256:fake\n')
        with self.assertRaisesRegex(bh.BHError, 'LFS pointer'):
            bh.snapshot(f.root)

    def test_no_git_symlink_is_rejected_without_following_it(self):
        f = self.fixture()
        try:
            (f.root / 'Source/link').symlink_to(f.root / 'Source/value.json')
        except OSError:
            self.skipTest('Host cannot create symlink')
        with self.assertRaises(bh.BHError):
            bh.snapshot(f.root)

    def test_cli_approval_needs_no_hash_or_record_file(self):
        f = self.fixture()
        self.plan(f)
        output = io.StringIO()
        with redirect_stdout(output):
            code = bh.main(['--root', str(f.root), 'approve', '--by', 'SYNTHETIC reviewer', '--source', 'SYNTHETIC human message'])
        self.assertEqual(code, 0, output.getvalue())
        s = f.h.state()
        self.assertEqual(s['phase'], 'APPROVED')
        record = f.h.read(s['approval']['path'], 'approval')
        self.assertEqual(record['subject_sha256'], bh.digest(f.h.load_plan(s)))
        self.assertEqual(record['source_ref'], 'SYNTHETIC human message')

    def test_approval_requires_explicit_human_and_source(self):
        f = self.fixture()
        self.plan(f)
        for kwargs in ({}, {'by': 'reviewer'}, {'source': 'message'}, {'by': ' ', 'source': 'message'}):
            with self.subTest(kwargs=kwargs), self.assertRaises(bh.BHError), f.h.lock():
                f.h.approve(**kwargs)
        self.assertEqual(f.h.state()['phase'], 'AWAITING_APPROVAL')

    def test_approval_cannot_bypass_blocked_plan(self):
        f = self.fixture()
        write(f.root, '.bh/bindings.json', {'version': '1.0.0', 'project_id': f.pid, 'checks': []})
        f.h = bh.Harness(f.root)
        self.plan(f)
        self.assertEqual(f.h.state()['phase'], 'BLOCKED')
        with self.assertRaisesRegex(bh.BHError, 'not eligible'):
            self.approve(f)

    def test_no_implicit_approval_at_plan_or_begin(self):
        f = self.fixture()
        self.plan(f)
        self.assertIsNone(f.h.state()['approval'])
        with self.assertRaises(bh.BHError), f.h.lock():
            f.h.begin()

    def test_changed_plan_record_or_core_invalidates_approval(self):
        for path in ('plan', 'AGENTS.md'):
            with self.subTest(path=path):
                f = self.fixture()
                self.plan(f)
                self.approve(f)
                target = f.h.state()['plan']['path'] if path == 'plan' else path
                write(f.root, target, 'changed')
                with self.assertRaises(bh.BHError), f.h.lock():
                    f.h.begin()

    def test_legacy_record_and_git_identity_checks_remain_supported(self):
        f = self.fixture(True)
        f.ready()
        f.verify()
        git(f.root, 'commit', '--allow-empty', '-qm', 'SYNTHETIC changed revision')
        self.assertNotEqual(f.h.audit_results(f.h.state())[0]['AC-01'], 'PASS')

    def test_managed_install_and_rollback_with_metadata_but_no_git(self):
        f = self.fixture()
        # Installed files in this fixture are deliberately configured; use a
        # separate disposable target for the default installer distribution.
        target = f.root / 'InstallTarget'
        write(target, 'ProjectSettings/ProjectVersion.txt', 'SYNTHETIC fixture')
        write(target, '.git', 'gitdir: nonexistent\n')
        with patch.object(install.bh, 'git', side_effect=AssertionError('Git must remain optional')):
            preview = install.preview(target)
            result = install.apply(target, bh.digest(preview))
            self.assertEqual(result['status'], 'APPLIED')
            self.assertEqual(install.rollback(target, result['transaction'], True)['status'], 'ROLLED_BACK')


if __name__ == '__main__':
    unittest.main()
