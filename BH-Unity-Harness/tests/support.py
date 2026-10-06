"""SYNTHETIC consumer fixtures exercising the actual installed implementation."""
from pathlib import Path
import copy, importlib.util, json, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode=True
PACKAGE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bh',PACKAGE/'project-template/Tools/BH/bh.py');bh=importlib.util.module_from_spec(spec);spec.loader.exec_module(bh)
spec=importlib.util.spec_from_file_location('install',PACKAGE/'installer/install.py');install=importlib.util.module_from_spec(spec);spec.loader.exec_module(install)
def write(root,name,value):
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(value,indent=2)+'\n' if not isinstance(value,str) else value,encoding='utf-8')
 return p

def approval(project,task,kind,subject):
 return {'version':'1.0.0','project_id':project,'task_id':task,'kind':kind,'actor':'human','name':'SYNTHETIC fixture actor; not authenticated','source_kind':'manual-record','source_ref':'SYNTHETIC test record, not real human approval','timestamp':bh.utc(),'subject_sha256':subject,'scope':'Synthetic fixture scope only','limits':[],'synthetic':True,'human_criteria':[]}

def git(root,*args):
 return subprocess.run(['git','-c','core.hooksPath=/dev/null','-C',str(root),*args],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout

class Fixture:
 def __init__(self,mode='nunit',pipeline='URP',narrow=False):
  self.temp=tempfile.TemporaryDirectory(prefix='BH synthetic project ');self.root=Path(self.temp.name)
  shutil.copytree(PACKAGE/'project-template',self.root,dirs_exist_ok=True)
  r=self.root;self.pid='synthetic-'+pipeline.lower();self.task='task-01'
  write(r,'.bh/SYNTHETIC_FIXTURE','SYNTHETIC — not a Unity game.\n')
  write(r,'.gitignore','.bh/runs/\n.bh/tasks/\n.bh/exports/\n.bh/locks/\n.bh/install/\n.bh/state.json\n.bh/CHECKPOINT.md\n**/__pycache__/\n')
  write(r,'Source/value.json',{'value':1});write(r,'Source/unrelated.txt','SYNTHETIC unrelated file\n')
  driver=Path(__file__).with_name('fixture_driver.py').read_text();write(r,'Tests/fixture_driver.py',driver)
  config=bh.load_json(r/'.bh/project.json');config.update(project_id=self.pid,synthetic=True,adoption_ref='SYNTHETIC approved installation fixture')
  config['engine']={'name':'Synthetic','version':'synthetic-1','render_pipeline':pipeline,'targets':['Synthetic-Windows']}
  config['protected_paths']=['Tests'];config['instruction_review']={'source_ref':'SYNTHETIC reviewed instructions','paths':['AGENTS.md']}
  write(r,'.bh/project.json',config)
  exe=Path(sys.executable).resolve()
  local={'version':'1.0.0','project_id':self.pid,'tools':[{'key':'python','path':str(exe),'sha256':bh.file_hash(exe),'observed_version':sys.version.split()[0],'kind':'python','review_ref':'SYNTHETIC pinned test interpreter'}],'editor_route':'disabled','batch_closed_confirmation_ref':None}
  write(r,'.bh/local.json',local)
  adapter={'facts':'facts','wrong-run':'facts','diagnostics':'diagnostics','build':'build'}.get(mode,'nunit')
  binding={'check_id':'CHECK-01','tool_key':'python','arguments':['{project}/Tests/fixture_driver.py','--root','{project}','--result','{result}','--project','{project_id}','--task','{task_id}','--run','{run_id}','--mode',mode],'working_directory':'.','result_file':'result.xml' if adapter=='nunit' else 'result.json','timeout_seconds':1 if mode=='timeout' else 5,'input_files':[{'path':'Tests/fixture_driver.py','sha256':bh.file_hash(r/'Tests/fixture_driver.py')}],'dependency_paths':['Source/value.json','Tests'] if narrow else [],'dependency_review_ref':'SYNTHETIC reviewed dependency boundary' if narrow else None,'expectations':[{'key':'value','ac_ids':['AC-01'],'operator':'equals','value':1,'units':'counter units'}] if adapter in ('facts','build') else [],'diagnostics_baseline':None,'diagnostic_source':None,'build_target':'Synthetic-Windows' if adapter=='build' else None,'review_ref':'SYNTHETIC reviewed process adapter'}
  if adapter=='diagnostics':
   write(r,'Tests/diagnostics-baseline.json',{'source':'sonarqube','issues':[]})
   binding['diagnostics_baseline']={'path':'Tests/diagnostics-baseline.json','sha256':bh.file_hash(r/'Tests/diagnostics-baseline.json')};binding['diagnostic_source']='sonarqube'
  write(r,'.bh/bindings.json',{'version':'1.0.0','project_id':self.pid,'checks':[binding]})
  write(r,'Handoff/DESIGN.md','# SYNTHETIC counter slice\nCounter equals one; clarity requires human playtest. No procedural architecture.\n')
  self.criteria={'version':'1.0.0','project_id':self.pid,'task_id':self.task,'criteria':[{'id':'AC-01','requirement_ids':['REQ-01'],'expected':'Counter value is exactly one','kind':'automated'},{'id':'AC-HUMAN','requirement_ids':['REQ-02'],'expected':'A human can understand the first-use counter','kind':'human'}]}
  self.overlay={'version':'1.0.0','project_id':self.pid,'synthetic':True,'status':'SYNTHETIC','invariants':[{'id':'INV-01','text':'No procedural generation is assumed','source_ref':'SYNTHETIC approved design'}],'protected_paths':['Tests'],'optional_capabilities':[],'open_decisions':[],'facts':['Synthetic fixture, no Unity Editor'],'source_refs':['SYNTHETIC source']}
  write(r,'Handoff/criteria.json',self.criteria);write(r,'Handoff/overlay.json',self.overlay)
  check={'id':'CHECK-01','ac_ids':['AC-01'],'required':True,'adapter':adapter,'profile':'slice','expected':'Actual observations match approved counter behavior','test_names':['Fixture.CounterChanges'] if adapter=='nunit' else [],'minimum_tests':1 if adapter=='nunit' else 0,'not_applicable_reason':None}
  manual={'id':'HUMAN-01','ac_ids':['AC-HUMAN'],'required':True,'adapter':'manual','profile':'slice','expected':'Human first-use playtest','test_names':[],'minimum_tests':0,'not_applicable_reason':None}
  paths=['Handoff/DESIGN.md','Handoff/criteria.json','Handoff/overlay.json']
  self.handoff={'version':'1.0.0','harness_version':'1.0.0','design_method_version':'3.1.0','project_id':self.pid,'task_id':self.task,'milestone_id':'M-SYNTHETIC','synthetic':True,'status':'COMPILED','objectives':['Verify synthetic counter'],'non_goals':['A real game or Unity integration test'],'assumptions':['Synthetic only'],'source_commit':None,'artifacts':[{'path':p,'sha256':bh.file_hash(r/p)} for p in paths],'design_path':paths[0],'criteria_path':paths[1],'overlay_path':paths[2],'read_order':paths,'acceptance_ids':['AC-01','AC-HUMAN'],'invariant_ids':['INV-01'],'allowed_paths':['Source'],'protected_paths':['Tests'],'allowed_actions':['edit-source','write-task-state','run-checks'],'architecture_refs':[paths[0]],'data_contract_refs':[paths[0]],'dependencies':[],'migration_impact':'No persistent game state','risk_controls':['Synthetic boundaries and human-only clarity criterion'],'questions':[],'checks':[check,manual],'required_profile':'slice','stop_conditions':['Scope or approval mismatch'],'startup':'Validate, reconcile, plan and obtain genuine technical approval before begin','return_format':'BH-RETURN-1.0.0','approval':None}
  self.refresh_handoff()
  self.proposal={'version':'1.0.0','project_id':self.pid,'task_id':self.task,'steps':[{'id':'STEP-01','description':'Bounded synthetic counter change and human review','paths':['Source/value.json'],'ac_ids':['AC-01','AC-HUMAN']}],'risks':['Synthetic only'],'reconciliation':['Actual fixture paths and Python tool pinned'],'tool_review_ref':'SYNTHETIC tool review','scope_conflicts':[],'next_action':'Obtain genuine approval of the exact generated plan'}
  write(r,'.bh/tasks/task-01/proposal.json',self.proposal)
  git(r,'init','-q');git(r,'config','user.name','BH Synthetic Tests');git(r,'config','user.email','synthetic@example.invalid');git(r,'add','.');git(r,'commit','-qm','Synthetic baseline')
  self.h=bh.Harness(r)
 def refresh_handoff(self,approve=True):
  for a in self.handoff['artifacts']:a['sha256']=bh.file_hash(self.root/a['path'])
  self.handoff['approval']=approval(self.pid,self.task,'design',bh.digest({k:v for k,v in self.handoff.items() if k!='approval'})) if approve else None
  write(self.root,'Handoff/handoff.json',self.handoff)
 def ready(self):
  h=self.h
  with h.lock():
   h.initialize('Handoff/handoff.json');result=h.make_plan('.bh/tasks/task-01/proposal.json')
   if h.state()['phase']!='AWAITING_APPROVAL':raise AssertionError(result)
   s=h.state();plan=bh.load_json(h.artifact(s['plan']))
   write(self.root,'.bh/tasks/task-01/approve.json',approval(self.pid,self.task,'plan',bh.digest(plan)))
   h.approve('.bh/tasks/task-01/approve.json');h.begin()
  return h
 def verify(self):
  with self.h.lock():return self.h.verification('slice')
 def accept(self):
  h=self.h;s=h.state();snap=bh.snapshot(self.root)
  a=approval(self.pid,self.task,'acceptance',bh.digest({'snapshot':snap['sha256'],'plan':s['plan']['sha256'],'handoff':s['handoff']['sha256']}))
  a['human_criteria']=[{'id':'AC-HUMAN','status':'PASS','evidence_ref':'SYNTHETIC observation; not real playtest','reason':'Synthetic fixture acceptance path','revisit':'Not applicable to any game'}]
  write(self.root,'.bh/tasks/task-01/accept.json',a)
  with h.lock():return h.accept('.bh/tasks/task-01/accept.json')
 def close(self):self.temp.cleanup()
