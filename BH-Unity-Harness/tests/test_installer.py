"""Actual installer tests; synthetic Git destinations, never a real game."""
from pathlib import Path
import json, tempfile, unittest
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
