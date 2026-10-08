"""Actual installer tests; synthetic Git destinations, never a real game."""
from pathlib import Path
import hashlib, io, json, shutil, sys, tempfile, unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from support import PACKAGE, bh, install, git, write
class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='BH install synthetic ');self.root=Path(self.tmp.name)
        git(self.root,'init','-q');write(self.root,'.bh/SYNTHETIC_FIXTURE','SYNTHETIC installer test\n')
    def tearDown(self):self.tmp.cleanup()
    def preview(self):return install.preview(self.root)
    def apply(self,preserve=()):
        p=install.preview(self.root,preserve);return install.apply(self.root,bh.digest(p),preserve)
    def test_preview_no_writes(self):
        before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()};self.preview();after={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()};self.assertEqual(before,after)
    def test_fresh_install_actual_manifest(self):
        self.assertEqual(self.apply()['status'],'APPLIED')
        for x in install.distribution()['files']:self.assertEqual(bh.file_hash(self.root/x['path']),x['sha256'])
    def test_target_only_installs_without_validation(self):
        with tempfile.TemporaryDirectory(prefix='BH distribution ') as folder:
            package=Path(folder)
            write(package,'project-template/AGENTS.md','# Local instructions\n')
            write(package,'project-template/.bh/project.json','Local seed\n')
            write(package,'PACKAGE_FILES.json','Not a valid manifest')
            write(self.root,'AGENTS.md','Old instructions\n')
            write(self.root,'.bh/project.json','Old seed\n')
            write(self.root,'.bh/state.json',{'phase':'EXECUTING'})
            write(self.root,'.bh/install/writer.lock','Existing lock\n')
            write(self.root,'HumanNotes.txt','Keep\n')
            (self.root/'.bh/SYNTHETIC_FIXTURE').unlink()
            output=io.StringIO()
            with patch.object(install,'PACKAGE',package), patch.object(sys,'argv',['install.py','--target',str(self.root)]), \
                 patch.object(install,'target_root',side_effect=AssertionError('No destination validation')), \
                 patch.object(install,'distribution',side_effect=AssertionError('No manifest validation')), \
                 patch.object(install.bh,'git',side_effect=AssertionError('No Git commands')), redirect_stdout(output):
                self.assertEqual(install.main(),0)
            self.assertEqual(json.loads(output.getvalue())['mode'],'direct')
            self.assertEqual((self.root/'AGENTS.md').read_bytes(),(package/'project-template/AGENTS.md').read_bytes())
            self.assertEqual((self.root/'.bh/project.json').read_bytes(),(package/'project-template/.bh/project.json').read_bytes())
            self.assertEqual((self.root/'HumanNotes.txt').read_text(),'Keep\n')
            self.assertEqual(json.loads((self.root/'.bh/state.json').read_text())['phase'],'EXECUTING')
            self.assertEqual((self.root/'.bh/install/writer.lock').read_text(),'Existing lock\n')
    def test_direct_install_creates_plain_target_with_exact_bytes(self):
        with tempfile.TemporaryDirectory(prefix='BH distribution ') as folder:
            package=Path(folder)
            source=write(package,'project-template/.agents/local.md','')
            source.write_bytes(b'# Local instructions\r\n')
            target=self.root/'NewProject'
            with patch.object(install,'PACKAGE',package):
                self.assertEqual(install.direct_install(target)['status'],'APPLIED')
            self.assertEqual((target/'.agents/local.md').read_bytes(),source.read_bytes())
            self.assertFalse((target/'.git').exists())
    def test_release_line_endings_install_exact_local_bytes(self):
        for data in (b'# Instructions\nLocal files\n', b'# Instructions\r\nLocal files\r\n'):
            with self.subTest(data=data), tempfile.TemporaryDirectory(prefix='BH distribution ') as folder:
                package=Path(folder)
                source=write(package,'project-template/AGENTS.md','')
                source.write_bytes(data)
                expected=hashlib.sha256(data.replace(b'\r\n',b'\n')).hexdigest()
                manifest=write(package,'PACKAGE_FILES.json',{'version':'1.0.0','files':[{'path':'AGENTS.md','sha256':expected,'ownership':'managed'}]})
                manifest_before=manifest.read_bytes()
                with patch.object(install,'PACKAGE',package):
                    p=self.preview()
                    self.assertEqual(p['rows'][0]['after'],hashlib.sha256(data).hexdigest())
                    result=install.apply(self.root,bh.digest(p))
                    self.assertEqual((self.root/'AGENTS.md').read_bytes(),data)
                    self.assertEqual(self.apply()['status'],'UNCHANGED')
                    install.rollback(self.root,result['transaction'],True)
                self.assertEqual(source.read_bytes(),data)
                self.assertEqual(manifest.read_bytes(),manifest_before)
    def test_distribution_content_change_still_rejected(self):
        with tempfile.TemporaryDirectory(prefix='BH distribution ') as folder:
            package=Path(folder)
            write(package,'project-template/AGENTS.md','# Changed instructions\n')
            write(package,'PACKAGE_FILES.json',{'version':'1.0.0','files':[{'path':'AGENTS.md','sha256':hashlib.sha256(b'# Original instructions\n').hexdigest(),'ownership':'managed'}]})
            with patch.object(install,'PACKAGE',package), self.assertRaisesRegex(install.bh.BHError,'Distribution changed: AGENTS.md'):
                self.preview()
    def test_source_line_ending_change_invalidates_preview(self):
        with tempfile.TemporaryDirectory(prefix='BH distribution ') as folder:
            package=Path(folder)
            source=write(package,'project-template/AGENTS.md','')
            source.write_bytes(b'# Instructions\n')
            write(package,'PACKAGE_FILES.json',{'version':'1.0.0','files':[{'path':'AGENTS.md','sha256':bh.file_hash(source),'ownership':'managed'}]})
            with patch.object(install,'PACKAGE',package):
                p=self.preview()
                source.write_bytes(b'# Instructions\r\n')
                with self.assertRaisesRegex(install.bh.BHError,'Preview changed'):
                    install.apply(self.root,bh.digest(p))
                self.assertFalse((self.root/'AGENTS.md').exists())
    def test_non_repo_install_and_rollback_without_git(self):
        shutil.rmtree(self.root/'.git')
        with patch.object(install.bh, 'git', side_effect=AssertionError('Git must not run without repository metadata')):
            before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
            self.preview()
            self.assertEqual(before,{str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
            result=self.apply()
            self.assertEqual(result['status'],'APPLIED')
            for entry in install.distribution()['files']:
                self.assertEqual(bh.file_hash(self.root/entry['path']),entry['sha256'])
            self.assertEqual(self.apply()['status'],'UNCHANGED')
            self.assertEqual(install.rollback(self.root,result['transaction'])['status'],'ROLLBACK_PREVIEW')
            self.assertEqual(install.rollback(self.root,result['transaction'],True)['status'],'ROLLED_BACK')
            self.assertFalse((self.root/'AGENTS.md').exists())
    def test_repository_subdirectory_still_rejected(self):
        nested=self.root/'NestedProject'
        write(nested,'.bh/SYNTHETIC_FIXTURE','SYNTHETIC installer test\n')
        with self.assertRaisesRegex(install.bh.BHError,'Destination must be Git root'):
            install.preview(nested)
    def test_invalid_repository_metadata_still_rejected(self):
        shutil.rmtree(self.root/'.git')
        write(self.root,'.git','gitdir: missing-repository\n')
        with self.assertRaisesRegex(install.bh.BHError,'Git read failed'):
            self.preview()
    def test_repeat_unchanged(self):self.apply();self.assertEqual(self.apply()['status'],'UNCHANGED')
    def test_bad_approval_no_install(self):
        with self.assertRaises(install.bh.BHError):install.apply(self.root,'0'*64)
        self.assertFalse((self.root/'AGENTS.md').exists())
    def test_conflicting_agents_preserved(self):
        write(self.root,'AGENTS.md','Human policy\n')
        with self.assertRaises(install.bh.BHError):self.apply()
        self.assertEqual((self.root/'AGENTS.md').read_text(),'Human policy\n')
    def test_explicit_manual_merge(self):
        write(self.root,'AGENTS.md','Human policy\n');r=self.apply(['AGENTS.md']);self.assertTrue(r['manual_merge_required']);self.assertEqual((self.root/'AGENTS.md').read_text(),'Human policy\n')
    def test_seed_local_edits_preserved(self):
        self.apply();write(self.root,'.bh/project.json','Human project decisions\n');self.apply();self.assertEqual((self.root/'.bh/project.json').read_text(),'Human project decisions\n')
    def test_managed_edits_conflict(self):
        self.apply();write(self.root,'Tools/BH/bh.py','Local edit\n')
        with self.assertRaises(install.bh.BHError):self.apply()
    def test_stale_preview(self):
        p=self.preview();write(self.root,'AGENTS.md','Concurrent edit\n')
        with self.assertRaises(install.bh.BHError):install.apply(self.root,bh.digest(p))
    def test_rollback_preview_read_only(self):
        r=self.apply();before=(self.root/'AGENTS.md').read_bytes();v=install.rollback(self.root,r['transaction']);self.assertEqual(v['status'],'ROLLBACK_PREVIEW');self.assertEqual(before,(self.root/'AGENTS.md').read_bytes())
    def test_rollback_managed_only(self):
        r=self.apply();write(self.root,'HumanNotes.txt','Keep');install.rollback(self.root,r['transaction'],True);self.assertFalse((self.root/'AGENTS.md').exists());self.assertTrue((self.root/'HumanNotes.txt').exists());self.assertEqual(install.rollback(self.root,r['transaction'],True)['status'],'UNCHANGED')
    def test_rollback_preserves_edited_seed(self):
        r=self.apply();write(self.root,'.bh/project.json','Human decisions');install.rollback(self.root,r['transaction'],True);self.assertEqual((self.root/'.bh/project.json').read_text(),'Human decisions')
    def test_rollback_refuses_managed_edit(self):
        r=self.apply();write(self.root,'AGENTS.md','Human change')
        with self.assertRaises(install.bh.BHError):install.rollback(self.root,r['transaction'],True)
        self.assertEqual((self.root/'AGENTS.md').read_text(),'Human change')
    def test_active_task_blocks(self):
        write(self.root,'.bh/state.json',{'phase':'EXECUTING'})
        with self.assertRaises(install.bh.BHError):self.preview()
    def test_rollback_active_record_blocks(self):
        r=self.apply();write(self.root,'.bh/state.json',{'phase':'ACCEPTED'})
        with self.assertRaises(install.bh.BHError):install.rollback(self.root,r['transaction'],True)
    def test_lock_blocks(self):
        write(self.root,'.bh/install/writer.lock','active')
        with self.assertRaises(install.bh.BHError):self.apply()
    def test_wrong_destination(self):
        with self.assertRaises(install.bh.BHError):install.preview(PACKAGE)
    def test_destination_requires_marker(self):
        (self.root/'.bh/SYNTHETIC_FIXTURE').unlink()
        with self.assertRaises(install.bh.BHError):self.preview()
    def test_traversal_transaction(self):
        with self.assertRaises(install.bh.BHError):install.rollback(self.root,'../../other')
    def test_preserve_not_blanket_override(self):
        with self.assertRaises(install.bh.BHError):install.preview(self.root,['Tools/BH/bh.py'])
