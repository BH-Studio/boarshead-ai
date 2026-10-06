"""Additional offline tests of shipped package tools, parsers and release scan."""
import importlib.util, json, sys, tempfile, unittest
from pathlib import Path
from support import PACKAGE, Fixture, bh, install, write, git

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
check=module('check_package',PACKAGE/'tools/check_package.py')
assemble=module('assemble_candidate',PACKAGE/'tools/assemble_candidate.py')
sys.path.insert(0,str(PACKAGE/'project-template/Tools/BH'))
release=module('release',PACKAGE/'project-template/Tools/BH/check_release_profile.py')
class PackageTests(unittest.TestCase):
    def test_package_additions_no_false_full_pass(self):
        out=check.check(True);self.assertFalse(out['problems']);self.assertIn(out['status'],('PASS_STATIC_PACKAGE','PARTIAL_UNASSEMBLED'))
    def test_missing_preserved_blocks_full_validation(self):
        out=check.check(False)
        if out['missing_preserved']:self.assertEqual(out['status'],'FAIL')
        else:self.assertEqual(out['status'],'PASS_STATIC_PACKAGE')
    def test_budget_metrics(self):
        text=(PACKAGE/'design-gpt/01C_GPT_INSTRUCTIONS_OFFICIAL.md').read_text();self.assertLessEqual(len(text),8000);self.assertGreaterEqual(8000-len(text),200)
    def test_canonical_copies(self):self.assertEqual((PACKAGE/'contracts/schema.json').read_bytes(),(PACKAGE/'project-template/.bh/schema.json').read_bytes())
    def test_distribution_nonempty(self):self.assertGreater(len(install.distribution()['files']),20)
    def test_no_design_in_game(self):self.assertFalse((PACKAGE/'project-template/design-gpt').exists())
    def test_seed_project_schema_valid(self):bh.validate(bh.load_json(PACKAGE/'project-template/.bh/project.json'),'project',bh.load_json(PACKAGE/'contracts/schema.json'))
    def test_assembler_real_git_blob(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);repo=root/'repo';repo.mkdir();git(repo,'init','-q');data=b'SYNTHETIC reference, not preserved studio content\n';f=repo/'source.md';f.write_bytes(data);sha=git(repo,'hash-object','-w','source.md').decode().strip();package=root/'additions';package.mkdir();write(package,'PRESERVED_REFERENCES.json',{'files':[{'path':'design-gpt/reference.md','git_blob_sha':sha}]});out=root/'assembled';assemble.assemble(repo,out,package);self.assertEqual((out/'design-gpt/reference.md').read_bytes(),data)
            with self.assertRaises(ValueError):assemble.assemble(repo,out,package)
    def test_assembler_accepts_crlf_checkout_of_preserved_blob(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);repo=root/'repo';repo.mkdir();git(repo,'init','-q');data=b'SYNTHETIC reference\nsecond line\n';source=repo/'source.md';source.write_bytes(data);sha=git(repo,'hash-object','-w','source.md').decode().strip();package=root/'additions';package.mkdir();write(package,'PRESERVED_REFERENCES.json',{'files':[{'path':'design-gpt/reference.md','git_blob_sha':sha}]});existing=package/'design-gpt/reference.md';existing.parent.mkdir();existing.write_bytes(data.replace(b'\n',b'\r\n'));out=root/'assembled';assemble.assemble(repo,out,package);self.assertEqual((out/'design-gpt/reference.md').read_bytes(),data)
    def test_assembler_rejects_real_preserved_content_conflict(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);repo=root/'repo';repo.mkdir();git(repo,'init','-q');data=b'SYNTHETIC reference\n';source=repo/'source.md';source.write_bytes(data);sha=git(repo,'hash-object','-w','source.md').decode().strip();package=root/'additions';package.mkdir();write(package,'PRESERVED_REFERENCES.json',{'files':[{'path':'design-gpt/reference.md','git_blob_sha':sha}]});existing=package/'design-gpt/reference.md';existing.parent.mkdir();existing.write_bytes(b'DIFFERENT reference\r\n')
            with self.assertRaisesRegex(ValueError,'Conflicting preserved file'):assemble.assemble(repo,root/'assembled',package)
    def test_assembler_rejects_unsafe_reference(self):
        with tempfile.TemporaryDirectory() as td:
            r=Path(td);repo=r/'repo';repo.mkdir();git(repo,'init','-q');package=r/'p';package.mkdir();write(package,'PRESERVED_REFERENCES.json',{'files':[{'path':'../escape','git_blob_sha':'0'*40}]})
            with self.assertRaises(ValueError):assemble.assemble(repo,r/'out',package)
    def test_release_actual_match(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td);write(p,'Plugins/DebugBridge.dll','synthetic');facts,paths=release.scan(p,{'version':'1.0.0','review_ref':'SYNTHETIC','forbidden_filename_patterns':['*DebugBridge*']});self.assertEqual(facts['forbidden_matches'],1);self.assertEqual(paths,['Plugins/DebugBridge.dll'])
    def test_release_no_match_narrow_only(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td);write(p,'Player.exe','synthetic');facts,_=release.scan(p,{'version':'1.0.0','review_ref':'SYNTHETIC','forbidden_filename_patterns':['*DebugBridge*']});self.assertEqual(facts['forbidden_matches'],0)
    def test_release_empty_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(release.bh.BHError):release.scan(td,{'version':'1.0.0','review_ref':'SYNTHETIC','forbidden_filename_patterns':['*DebugBridge*']})
    def test_release_empty_policy_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(release.bh.BHError):release.scan(td,{'version':'1.0.0','review_ref':'SYNTHETIC','forbidden_filename_patterns':[]})

class BuildParserTests(unittest.TestCase):
    def setUp(self):
        self.f=Fixture('build');self.addCleanup(self.f.close);self.r=self.f.root;self.out=self.r/'.bh/runs/run-synthetic/CHECK-01';self.out.mkdir(parents=True);self.spec=self.f.handoff['checks'][0];self.binding=bh.load_json(self.r/'.bh/bindings.json')['checks'][0]
        f=write(self.r,'.bh/runs/run-synthetic/CHECK-01/player.bin','SYNTHETIC build output')
        self.value={'project_id':self.f.pid,'task_id':self.f.task,'run_id':'run-synthetic','observations':{'value':1},'build_result':'Succeeded','errors':0,'target':'Synthetic-Windows','outputs':[{'path':f.relative_to(self.r).as_posix(),'sha256':bh.file_hash(f)}]}
    def parse(self):
        f=write(self.r,'.bh/runs/run-synthetic/CHECK-01/result.json',self.value);return self.f.h.parse_observations(f,self.spec,self.binding,self.f.task,'run-synthetic',self.out)
    def test_success_actual_hashed_output(self):self.assertEqual(self.parse()['status'],'PASS')
    def test_failed_is_fail_not_error(self):self.value.update(build_result='Failed',errors=1,outputs=[]);self.assertEqual(self.parse()['status'],'FAIL')
    def test_missing_result_is_malformed(self):
        self.value.pop('build_result')
        with self.assertRaises(bh.BHError):self.parse()
    def test_cancelled_not_pass(self):
        self.value['build_result']='Cancelled'
        with self.assertRaises(bh.BHError):self.parse()
    def test_wrong_target(self):
        self.value['target']='Other'
        with self.assertRaises(bh.BHError):self.parse()
    def test_no_outputs(self):
        self.value['outputs']=[]
        with self.assertRaises(bh.BHError):self.parse()
    def test_output_digest_mismatch(self):
        self.value['outputs'][0]['sha256']='0'*64
        with self.assertRaises(bh.BHError):self.parse()
    def test_stale_output_directory(self):
        f=write(self.r,'.bh/runs/older/player.bin','old');self.value['outputs']=[{'path':f.relative_to(self.r).as_posix(),'sha256':bh.file_hash(f)}]
        with self.assertRaises(bh.BHError):self.parse()
