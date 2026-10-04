"""Game-agnostic distribution checks and synthetic cross-profile negatives.
Historical names below are scan counterexamples, not operational instructions.
This bounded lexical check does not prove semantic neutrality or model compliance.
"""
import copy, hashlib, importlib.util, re, shutil, tempfile, unittest
from pathlib import Path
from support import PACKAGE, Fixture, bh, write, git

SOURCE_NAMES=re.compile(r'breach[ _-]?one|iron[ _-]?meridian|vector[ _-]?rift|ashfall[ _-]?raiders|\bronin\b|\bwardens\b|galaxy[ _-]?generator|\bb1-',re.I)

def load_tool(name):
    spec=importlib.util.spec_from_file_location(name,PACKAGE/'tools'/f'{name}.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

class GameAgnosticTests(unittest.TestCase):
    def profiles(self):
        return [bh.load_json(p) for p in sorted((PACKAGE/'examples/profiles').glob('*.json'))]
    def test_active_policy_and_knowledge_have_no_source_game_names(self):
        km=bh.load_json(PACKAGE/'design-gpt/KNOWLEDGE_MANIFEST.json')
        paths={PACKAGE/'design-gpt'/r['path'] for r in km['knowledge_files']}
        paths.update(PACKAGE/'design-gpt'/p for p in ('01C_GPT_INSTRUCTIONS_OFFICIAL.md','02_NAME_DESCRIPTION_STARTERS.md','evaluation/REGRESSION_CASES.md'))
        for root in ('project-template','contracts','optional','installer','examples/profiles'):
            paths.update(p for p in (PACKAGE/root).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
        for p in sorted(paths):
            with self.subTest(path=str(p.relative_to(PACKAGE))):
                self.assertTrue(p.is_file(),f'Missing active resource: {p}')
                self.assertIsNone(SOURCE_NAMES.search(p.relative_to(PACKAGE).as_posix()))
                self.assertIsNone(SOURCE_NAMES.search(p.read_text(encoding='utf-8')))
    def test_scanner_rejects_name_variants(self):
        for text in ('Breach One','breach-one','BreachOne','VECTOR_RIFT','Galaxy Generator','K11_GALAXY_GENERATOR'):
            self.assertIsNotNone(SOURCE_NAMES.search(text))
        self.assertIsNone(SOURCE_NAMES.search('SYNTHETIC discrete-state profile'))
    def test_profiles_are_distinct_synthetic_contracts(self):
        profiles=self.profiles();self.assertEqual(len(profiles),2)
        self.assertEqual(len({p['project_id'] for p in profiles}),2)
        text=' '.join(i['text'] for p in profiles for i in p['invariants'])
        self.assertIn('elapsed-time',text);self.assertIn('explicit authorized step',text)
        self.assertFalse(any(p['optional_capabilities'] for p in profiles))
    def test_real_seed_does_not_select_game_configuration(self):
        seed=bh.load_json(PACKAGE/'project-template/.bh/project.json')
        self.assertEqual(seed['project_id'],'UNCONFIGURED');self.assertFalse(seed['synthetic'])
        self.assertIsNone(seed['engine']['version']);self.assertEqual(seed['engine']['render_pipeline'],'UNRECONCILED')
        self.assertEqual(seed['engine']['targets'],['UNCONFIGURED']);self.assertEqual(seed['enabled_capabilities'],[])
        self.assertEqual(seed['telemetry'],'none')
    def test_reference_only_lesson_is_not_a_knowledge_selection(self):
        refs=bh.load_json(PACKAGE/'PRESERVED_REFERENCES.json')
        row=next(r for r in refs['files'] if r['path']=='review/reference-only/K11_SOURCE_LESSONS.md')
        b=(PACKAGE/row['path']).read_bytes()
        self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),row['git_blob_sha'])
        km=bh.load_json(PACKAGE/'design-gpt/KNOWLEDGE_MANIFEST.json')
        self.assertTrue(all('GALAXY' not in r['path'] and 'reference-only' not in r['path'] for r in km['knowledge_files']))
    def test_generic_lesson_preserves_fifteen_responsibilities(self):
        text=(PACKAGE/'design-gpt/Knowledge/K11_GENERALIZED_DELIVERY_LESSONS.md').read_text()
        self.assertEqual([int(x) for x in re.findall(r'^# (\d+)\.',text,re.M)],list(range(1,16)))
        self.assertIn('claim',text);self.assertIn('current project',text);self.assertIsNone(SOURCE_NAMES.search(text))
    def test_shipped_profiles_block_execution_until_reconciled(self):
        for overlay in self.profiles():
            f=Fixture('facts');self.addCleanup(f.close);o=copy.deepcopy(overlay);o['project_id']=f.pid
            write(f.root,'Handoff/overlay.json',o);f.handoff['invariant_ids']=[r['id'] for r in o['invariants']];f.refresh_handoff()
            with self.assertRaisesRegex(bh.BHError,'unresolved decisions'):f.h.handoff('Handoff/handoff.json')
    def test_foreign_profile_invariants_are_rejected(self):
        profiles=self.profiles()
        for index,overlay in enumerate(profiles):
            f=Fixture('facts');self.addCleanup(f.close);o=copy.deepcopy(overlay);o['project_id']=f.pid;o['open_decisions']=[]
            # Only this synthetic test binds its synthetic facts. This is not a real project approval.
            write(f.root,'Handoff/overlay.json',o);f.handoff['invariant_ids']=[r['id'] for r in o['invariants']];f.refresh_handoff()
            f.h.handoff('Handoff/handoff.json')
            f.handoff['invariant_ids']=[r['id'] for r in profiles[1-index]['invariants']];f.refresh_handoff()
            with self.assertRaisesRegex(bh.BHError,'invariant'):f.h.handoff('Handoff/handoff.json')
    def test_assembler_accepts_only_declared_review_reference_path(self):
        assembler=load_tool('assemble_candidate')
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);repo=root/'repo';repo.mkdir();git(repo,'init','-q')
            data=b'SYNTHETIC review provenance only\n';(repo/'src').write_bytes(data);sha=git(repo,'hash-object','-w','src').decode().strip()
            package=root/'package';package.mkdir();write(package,'PRESERVED_REFERENCES.json',{'files':[{'path':'review/reference-only/source.md','git_blob_sha':sha}]})
            out=root/'assembled';assembler.assemble(repo,out,package);self.assertEqual((out/'review/reference-only/source.md').read_bytes(),data)
            write(package,'PRESERVED_REFERENCES.json',{'files':[{'path':'review/../../outside','git_blob_sha':sha}]})
            with self.assertRaises(ValueError):assembler.assemble(repo,root/'bad',package)
    def test_test_receipts_include_markdown_inputs_not_generated_evidence(self):
        runner=load_tool('run_tests')
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);write(root,'instructions.md','first');write(root,'evidence/run.json',{'status':'SYNTHETIC'})
            first=runner.source_hashes(root);write(root,'instructions.md','changed');second=runner.source_hashes(root)
            self.assertIn('instructions.md',first);self.assertNotEqual(first['instructions.md'],second['instructions.md'])
            self.assertNotIn('evidence/run.json',first)

    def test_arbitrary_unreviewed_skill_blocks_without_a_game_prefix(self):
        f=Fixture('facts');self.addCleanup(f.close)
        write(f.root,'.agents/skills/foreign-workflow/SKILL.md','---\nname: foreign-workflow\ndescription: SYNTHETIC unrelated workflow\n---\n')
        result=f.h.preflight();self.assertEqual(result['status'],'BLOCKED')
        self.assertTrue(any('Unreviewed local skill' in x for x in result['issues']))
    def test_unregistered_skill_cannot_hide_behind_studio_prefix(self):
        f=Fixture('facts');self.addCleanup(f.close)
        write(f.root,'.agents/skills/bh-unregistered/SKILL.md','---\nname: bh-unregistered\ndescription: SYNTHETIC unreviewed skill\n---\n')
        self.assertEqual(f.h.preflight()['status'],'BLOCKED')
    def test_explicitly_reviewed_extra_skill_is_preserved(self):
        f=Fixture('facts');self.addCleanup(f.close);name='.agents/skills/custom-local/SKILL.md'
        write(f.root,name,'---\nname: custom-local\ndescription: SYNTHETIC reviewed local procedure\n---\n')
        config=bh.load_json(f.root/'.bh/project.json');config['instruction_review']['paths'].append(name);write(f.root,'.bh/project.json',config)
        result=bh.Harness(f.root).preflight();self.assertEqual(result['status'],'PREFLIGHT_ONLY');self.assertTrue((f.root/name).is_file())
    def test_malformed_skill_registry_fails_explicitly(self):
        f=Fixture('facts');self.addCleanup(f.close);write(f.root,'.bh/skill-registry.json',{'version':'1.0.0','skills':'not a list'})
        with self.assertRaises(bh.BHError):f.h.preflight()

    def test_missing_nonpreserved_knowledge_cannot_pass_package_check(self):
        checker=load_tool('check_package')
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'package'
            shutil.copytree(PACKAGE,root,ignore=shutil.ignore_patterns('__pycache__','evidence'))
            (root/'design-gpt/Knowledge/K11_GENERALIZED_DELIVERY_LESSONS.md').unlink()
            checker.P=root
            for allow_partial in (False,True):
                out=checker.check(allow_partial)
                self.assertEqual(out['status'],'FAIL')
                self.assertTrue(any('knowledge file' in x for x in out['problems']))
