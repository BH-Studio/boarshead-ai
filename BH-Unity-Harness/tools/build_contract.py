"""Authoring-only generator. Canonical contract is contracts/schema.json."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
S={'type':'string','minLength':1,'maxLength':8000}
ID={'type':'string','pattern':r'^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$'}
HASH={'type':'string','pattern':r'^[0-9a-f]{64}$'}
B={'type':'boolean'}; N={'type':'integer','minimum':0}; V={'const':'1.0.0','type':'string'}
TIME={'type':'string','format':'date-time'}; NULL={'type':'null'}; D={}
def ref(n): return {'$ref':'#/$defs/'+n}
def arr(v=S,low=0,high=256): return {'type':'array','items':v,'minItems':low,'maxItems':high}
def enum(*v): return {'type':'string','enum':list(v)}
def obj(p,optional=()): return {'type':'object','properties':p,'required':[x for x in p if x not in optional],'additionalProperties':False}
def nullable(v): return {'anyOf':[v,NULL]}
def strings(low=0,high=256): return arr(S,low,high)
def ids(low=0,high=64): return {**arr(ID,low,high),'uniqueItems':True}
D['artifact']=obj({'path':S,'sha256':HASH})
D['approval']=obj({'version':V,'project_id':ID,'task_id':ID,'kind':enum('design','plan','acceptance','adoption','exception'),
 'actor':enum('human'),'name':S,'source_kind':enum('human-message','manual-record'),'source_ref':S,'timestamp':TIME,
 'subject_sha256':HASH,'scope':S,'limits':strings(),'synthetic':B,
 'human_criteria':arr(obj({'id':ID,'status':enum('PASS','ACCEPTED_DEFERRED'),'evidence_ref':S,'reason':S,'revisit':S}),0,64)})
D['criterion']=obj({'id':ID,'requirement_ids':ids(1),'expected':S,'kind':enum('automated','human')})
D['criteria']=obj({'version':V,'project_id':ID,'task_id':ID,'criteria':arr(ref('criterion'),1,64)})
D['invariant']=obj({'id':ID,'text':S,'source_ref':S})
D['overlay']=obj({'version':V,'project_id':ID,'synthetic':B,'status':enum('SOURCE_DERIVED_UNRECONCILED','RECONCILED','SYNTHETIC'),
 'invariants':arr(ref('invariant'),1,128),'protected_paths':strings(),'optional_capabilities':ids(),'open_decisions':strings(),'facts':strings(),'source_refs':strings(1)})
D['check_spec']=obj({'id':ID,'ac_ids':ids(1),'required':B,'adapter':enum('nunit','facts','diagnostics','build','manual'),
 'profile':enum('fast','slice','milestone'),'expected':S,'test_names':strings(),'minimum_tests':N,'not_applicable_reason':nullable(S)})
D['handoff']=obj({'version':V,'harness_version':V,'design_method_version':{'const':'3.1.0'},'project_id':ID,'task_id':ID,'milestone_id':ID,
 'synthetic':B,'status':enum('DRAFT','BLOCKED','COMPILED'),'objectives':strings(1),'non_goals':strings(1),'assumptions':strings(),
 'source_commit':nullable({'type':'string','pattern':r'^[0-9a-f]{40}$'}),'artifacts':arr(ref('artifact'),3,128),
 'design_path':S,'criteria_path':S,'overlay_path':S,'read_order':strings(3,128),'acceptance_ids':ids(1),'invariant_ids':ids(1,128),
 'allowed_paths':strings(1),'protected_paths':strings(),
 'allowed_actions':arr(enum('edit-source','edit-tests','edit-assets','write-task-state','run-checks','launch-unity','git-commit'),1,7),
 'architecture_refs':strings(1),'data_contract_refs':strings(1),'dependencies':strings(),'migration_impact':S,'risk_controls':strings(1),
 'questions':arr(obj({'id':ID,'class':enum('BLOCKING','DESIGN-SHAPING','TUNING','DEFERRED'),'question':S,'owner':S,'revisit':S})),
 'checks':arr(ref('check_spec'),1,64),'required_profile':enum('fast','slice','milestone'),'stop_conditions':strings(1),
 'startup':S,'return_format':{'const':'BH-RETURN-1.0.0'},'approval':nullable(ref('approval'))})
D['project']=obj({'version':V,'harness_version':V,'project_id':ID,'synthetic':B,
 'engine':obj({'name':enum('Unity','Synthetic'),'version':nullable(S),'render_pipeline':enum('UNRECONCILED','BuiltIn','URP','HDRP','Synthetic'),'targets':strings(1)}),
 'protected_paths':strings(),'enabled_capabilities':ids(),
 'budgets':obj({'failed_rounds':{'type':'integer','minimum':1,'maximum':20},'repeat_failures':{'type':'integer','minimum':1,'maximum':10},
 'no_progress_rounds':{'type':'integer','minimum':1,'maximum':20},'recovery_cycles':{'type':'integer','minimum':0,'maximum':3},
 'infrastructure_failures':{'type':'integer','minimum':1,'maximum':10}}),
 'adoption_ref':S,'instruction_review':obj({'source_ref':S,'paths':strings(1)}),'telemetry':{'const':'none'}})
D['tool']=obj({'key':ID,'path':S,'sha256':HASH,'observed_version':S,'kind':enum('unity','python','native'),'review_ref':S})
D['local']=obj({'version':V,'project_id':ID,'tools':arr(ref('tool')),'editor_route':enum('disabled','batch','external-mcp','unity-cli'),
 'batch_closed_confirmation_ref':nullable(S)})
D['expectation']=obj({'key':S,'ac_ids':ids(1),'operator':enum('equals','at_most','at_least'),'value':{'anyOf':[S,{'type':'number'},B]},'units':S})
D['binding']=obj({'check_id':ID,'tool_key':ID,'arguments':strings(1,128),'working_directory':S,'result_file':S,
 'timeout_seconds':{'type':'integer','minimum':1,'maximum':3600},'input_files':arr(ref('artifact')),'dependency_paths':strings(),
 'dependency_review_ref':nullable(S),'expectations':arr(ref('expectation'),0,64),'diagnostics_baseline':nullable(ref('artifact')),
 'diagnostic_source':nullable(S),'build_target':nullable(S),'review_ref':S,
 'reuse_policy':enum('source-bound','never')}, optional=('reuse_policy',))
D['bindings']=obj({'version':V,'project_id':ID,'checks':arr(ref('binding'),0,64)})
D['proposal']=obj({'version':V,'project_id':ID,'task_id':ID,'steps':arr(obj({'id':ID,'description':S,'paths':strings(1),'ac_ids':ids(1)}),1,64),
 'risks':strings(),'reconciliation':strings(1),'tool_review_ref':S,'scope_conflicts':strings(),'next_action':S})
D['snapshot']=obj({'commit':{'type':'string','pattern':r'^[0-9a-f]{40}$'},'dirty':B,'status_sha256':HASH,
 'files':{'type':'object','additionalProperties':HASH},'sha256':HASH,'file_count':N,'bytes_hashed':N})
D['plan']=obj({'version':V,'project_id':ID,'task_id':ID,'created_utc':TIME,'handoff_sha256':HASH,'config_sha256':HASH,'harness_sha256':HASH,
 'baseline':ref('snapshot'),'proposal':ref('proposal'),'blockers':strings(),'allowed_paths':strings(1),'protected_paths':strings(),
 'allowed_actions':strings(1),'check_ids':ids(1),'required_profile':enum('fast','slice','milestone')})
D['phase']=enum('DISCOVERY','PLANNED','AWAITING_APPROVAL','APPROVED','EXECUTING','VERIFYING','READY_FOR_HUMAN_REVIEW','ACCEPTED','BLOCKED','FAILED','PAUSED','CANCELLED')
D['result_status']=enum('PASS','FAIL','ERROR','NOT_RUN','BLOCKED','NOT_APPLICABLE')
D['ac_status']=enum('PASS','FAIL','ERROR','NOT_RUN','BLOCKED','HUMAN_PENDING','ACCEPTED_DEFERRED')
D['state']=obj({'version':V,'harness_version':V,'project_id':ID,'task_id':ID,'revision':N,'phase':ref('phase'),'synthetic':B,'updated_utc':TIME,
 'handoff':ref('artifact'),'plan':nullable(ref('artifact')),'approval':nullable(ref('artifact')),'acceptance_record':nullable(ref('artifact')),
 'claims':strings(),'ac_status':{'type':'object','additionalProperties':ref('ac_status')},'runs':strings(),'pending_run':nullable(S),
 'blockers':strings(),'next_action':S,'counters':obj({'failed_rounds':N,'repeat_failures':N,'no_progress_rounds':N,'infrastructure_failures':N,'recovery_cycles':N}),
 'last_fingerprint':nullable(HASH),'last_passed_ids':ids(),'events':arr(obj({'from':ref('phase'),'to':ref('phase'),'at':TIME,'reason':S}))})
D['check_result']=obj({'id':ID,'ac_ids':ids(1),'required':B,'adapter':S,'status':ref('result_status'),'reason':S,'dependency_sha256':HASH,
 'command':strings(),'working_directory':S,'tool_version':S,'exit_code':nullable({'type':'integer'}),'duration_seconds':{'type':'number','minimum':0},
 'counts':obj({'discovered':N,'passed':N,'failed':N,'skipped':N,'inconclusive':N}),'failed_names':strings(),'observations':strings(),'artifacts':arr(ref('artifact'))})
D['receipt']=obj({'version':V,'harness_version':V,'project_id':ID,'task_id':ID,'run_id':ID,'synthetic':B,'started_utc':TIME,'finished_utc':TIME,
 'harness_sha256':HASH,'config_sha256':HASH,'plan_sha256':HASH,'snapshot':ref('snapshot'),'after_snapshot_sha256':HASH,
 'environment':obj({'os':S,'python':S,'git':S}),'profile':enum('fast','slice','milestone'),'results':arr(ref('check_result'),1,64),
 'audit_mutations':strings(),'independence':enum('deterministic-wrapper-same-workspace'),'limitations':strings(1)})
D['return']=obj({'version':V,'format':{'const':'BH-RETURN-1.0.0'},'project_id':ID,'task_id':ID,'synthetic':B,'created_utc':TIME,
 'handoff_sha256':HASH,'plan_sha256':nullable(HASH),'source_snapshot':ref('snapshot'),'implementation_claims':strings(),
 'acceptance':arr(obj({'id':ID,'expected':S,'status':ref('ac_status'),'receipt_refs':strings(),'limitations':strings()}),1,64),
 'receipts':arr(ref('artifact')),'deviations':strings(),'design_questions':strings(),'human_acceptance':enum('PENDING','ACCEPTED_FOR_RECORDED_SNAPSHOT'),
 'evidence_transport':enum('LOCAL_ONLY_UNTIL_UPLOADED_OR_PUBLISHED'),'review_independence':enum('same-session-or-not-established'),'next_action':S})
D['change_request']=obj({'version':V,'project_id':ID,'task_id':ID,'change_id':ID,'status':enum('PROPOSED','HUMAN_APPROVED'),
 'prior_handoff_sha256':HASH,'previous_decision':S,'proposed_decision':S,'reason':S,'alternatives':strings(1),
 'affected_acceptance_ids':ids(1),'affected_check_ids':ids(1),'impacts':strings(1),'invalidates_plan_approval':{'const':True},
 'evidence_refs':arr(ref('artifact')),'approval':nullable(ref('approval'))})
SCHEMA={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:bh:contracts:1.0.0','title':'BH design/execution interface 1.0.0','$defs':D}
if __name__=='__main__':
 data=json.dumps(SCHEMA,ensure_ascii=False,indent=2)+'\n'
 for dest in ('contracts/schema.json','project-template/.bh/schema.json','design-gpt/Knowledge/BH_CONTRACT_SCHEMA.json'):
  p=ROOT/dest;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data,encoding='utf-8')
 print(len(D),'definitions;',len(data.encode()),'bytes; three byte-matched copies')
