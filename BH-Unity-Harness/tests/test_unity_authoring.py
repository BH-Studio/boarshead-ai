"""BH metadata/reference negatives; no live Editor or skill activation implied."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from support import PACKAGE

spec = importlib.util.spec_from_file_location('unity_authoring', PACKAGE / 'tools/check_unity_authoring.py')
check = importlib.util.module_from_spec(spec); spec.loader.exec_module(check)

class UnityAuthoringTests(unittest.TestCase):
    def test_current_authored_subset(self):
        result = check.check(PACKAGE)
        self.assertEqual(result['status'], 'PASS_UNITY_AUTHORING_SUBSET', result['problems'])
    def test_plain_and_quoted_metadata(self):
        for description in ('Clear text.', '"A colon: is permitted when quoted."'):
            self.assertEqual(check.frontmatter('---\nname: example\ndescription: '+description+'\n---\n')['name'], 'example')
    def test_invalid_frontmatter_never_silently_disappears(self):
        for text in ('name: x', '---\nname: x\n---\n', '---\nname: x\nname: y\ndescription: z\n---\n',
                     '---\nname: x\ndescription: bad: value\n---\n', '---\nname: x\ndescription: [x]\n---\n',
                     '---\nname: X\ndescription: x\n---\n', '---\nname: x\ndescription: ""\n---\n'):
            with self.subTest(text=text), self.assertRaises(ValueError): check.frontmatter(text)
    def test_nonstring_yaml_scalars_rejected(self):
        for scalar in ('true', 'False', 'null', '~', 'yes', '12', '1.2', '1e3'):
            with self.subTest(scalar=scalar), self.assertRaises(ValueError):
                check.frontmatter('---\nname: example\ndescription: '+scalar+'\n---\n')
    def test_malformed_activation_metadata_rejected(self):
        base='interface:\n  display_name: "example"\n  short_description: "Description"\npolicy:\n  allow_implicit_invocation: false\n'
        self.assertEqual(check.activation_metadata(base), ['example','Description'])
        for value in (base.replace('false','true'), base+'policy:\n', base.replace('interface:', 'interface'), base.replace('"Description"','[]')):
            with self.subTest(value=value), self.assertRaises(ValueError): check.activation_metadata(value)
    def test_missing_and_escaping_references(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); p = root / 'SKILL.md'
            for link in ('missing.md', '../escape.md'):
                p.write_text('[reference]('+link+')')
                self.assertTrue(check.reference_errors(p, root))
    def test_existing_reference_and_external_link(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); (root/'guide.md').write_text('guide');p=root/'SKILL.md'
            p.write_text('[reference](guide.md#anchor) [source](https://example.org/docs)')
            self.assertFalse(check.reference_errors(p, root))
    def test_symlink_reference_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);(root/'target').write_text('x');(root/'link').symlink_to(root/'target')
            p=root/'SKILL.md';p.write_text('[reference](link)')
            self.assertTrue(check.reference_errors(p,root))
    def copy(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);root=Path(temp.name)
        for name in ('project-template','optional'):shutil.copytree(PACKAGE/name,root/name)
        shutil.copyfile(PACKAGE/'PACKAGE_FILES.json',root/'PACKAGE_FILES.json');return root
    def test_enabled_example_rejected(self):
        root=self.copy();p=root/'optional/unity-observation/provider.disabled.json';c=json.loads(p.read_text());c['enabled']=True;p.write_text(json.dumps(c))
        self.assertIn('Provider example cannot silently activate',check.check(root)['problems'])
    def test_missing_reference_rejected(self):
        root=self.copy();(root/'optional/unity-observation/README.md').unlink()
        self.assertEqual(check.check(root)['status'],'FAIL')
    def test_implicit_activation_rejected(self):
        root=self.copy();p=root/'project-template/.agents/skills/bh-unity-verify/agents/openai.yaml'
        p.write_text(p.read_text().replace('false','true'))
        self.assertTrue(any('Explicit invocation' in x for x in check.check(root)['problems']))
    def test_missing_default_manifest_file_rejected(self):
        root=self.copy();(root/'project-template/Docs/Harness/UNITY_PROCEDURES.md').unlink()
        self.assertEqual(check.check(root)['status'],'FAIL')
    def test_changed_core_hash_rejected(self):
        root=self.copy();p=root/'project-template/Tools/BH/bh.py';p.write_text(p.read_text()+'\n# altered\n')
        self.assertIn('Installed hash: Tools/BH/bh.py',check.check(root)['problems'])

if __name__ == '__main__': unittest.main()
