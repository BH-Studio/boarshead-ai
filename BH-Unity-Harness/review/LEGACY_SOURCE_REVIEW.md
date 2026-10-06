# Legacy source review — continuation 2026-10-04

Status: completed review batch; corrections identified below are not claimed implemented by this document. No adoption or game implementation.
Source repository: BH-Studio/boarshead-ai. All source reads pinned to 0cffc7e090eccb2d0b453c2c2c5a0db4631650c8. Source prefix below: BH-Harness-old/docs/AI/. Full UTF-8 content was read through the GitHub connector for all 31 files in the tables. The source pack is B1-CODEX-OPS 0.1.0 candidate dated September 8; compact baseline documents retain their actual September 2 dates and mixed statuses.

## Exact read coverage

| Policy (complete file) | Git blob SHA |
|---|---|
| AI_WORKFLOW.md | 4cf38ddd032c70434a418a2e180f919b6251dd55 |
| AUTHORITY_AND_CHANGE_CONTROL.md | e9e3f526eb61af21d98d58118a9740d008f151d1 |
| CODING_PACKAGE_CONTRACT.md | 577d511ce5d014952608d1e98a3b8e28ed94ef19 |
| CONTEXT_AND_ROUTING.md | abd5d078c1eef77781f44023ab39e512ae4dcd84 |
| SECURITY_AND_EXECUTION.md | 89b3766c3b8adedc6d356c2a15873d133961a4cf |
| UNITY_AND_MIDDLEWARE_POLICY.md | f898fcffb02eb7fc45b426041dde1ba359e81249 |
| VALIDATION_AND_EVIDENCE.md | 668f95d20d7ffca8560a3ce69889f16441fdee1c |
| BASELINE_INDEX.md | 77e475c3bb8a948c1ee1ffa4e4b4e2dbb5f05374 |
| REPOSITORY_MAP.md | 79992b18c0aa403b1a6e62805b51ffe45ba2f572 |
| PROMPT_CARDS.md | 20f06d7f814c6fc6830bbca031b08e9773c41e7b |
| SKILL_CATALOG.md | 56e38666f746af277fc592165f079e463c7bd924 |
| SOURCES.md | 6085b183f88e64eb90bce09dfa2a0a80f6fbb1ea |

| Template (under templates/, complete file) | Git blob SHA |
|---|---|
| ADOPTION_RECORD.template.md | e61d3b5df0b75887ef05564ff4c65b0c07292d9c |
| AUTHORING_SETUP.template.md | f4729e709e9210ee18a43a1e7afd2dadbc7a3f39 |
| CHANGE_REQUEST.template.md | 86a47bea3f0697d55ff476d9200074754e58d123 |
| CODEX_PROMPT.template.md | 7199af0203add5369e7141a232c2a6fbcf26460f |
| COMPLETION_REPORT.template.md | 24d6d8ebb3beeac7c500515fb05d8f5d221af8cd |
| CONTRACT.template.md | f811938aea3923d00b0004eff4b19d6d40c31d34 |
| EXPERIMENT_PLAN.template.md | 812f00c9fbfe85a98e648df314d1a0125e8fad4a |
| ITERATION_PROMPT.template.md | 0df93f1acee69ebd8381e657217ba60bd012e29d |
| MILESTONE_SPEC.template.md | d388379d0865a35a100a7dc4445ad46eb0570394 |
| PACKAGE_MANIFEST.template.md | b8504a0337300c88731afe0a55d60e322e5c16c7 |
| REPOSITORY_AUDIT.template.md | d0780c0205c2e535d9abc62854ccd364e54422c1 |
| REVIEW_AND_INTEGRATION.template.md | 97557008c6c971042bddb47081942e3868b53830 |
| STATE_DELTA.template.md | 83c36c0acd732e663c70bde7d397dc3d94c20ba3 |
| TEST_PLAN.template.md | d48bd353e2f5585f3d00573ae080b8ff5c387081 |
| WORK_STATE.template.md | 5c136e5d143d9c3bb51ba86ea4af9032ea3f00fb |

| Baseline (under baselines/2026-09-08/, complete file) | Git blob SHA |
|---|---|
| PROJECT_CONTEXT.md | aa0e7c6042afdc0472a2dfad17f4a9a58fd31bc2 |
| CURRENT_STATE.md | 243cc32b8470df564b5c87636a8e931f951ab9c2 |
| DECISION_REGISTER.md | 4cdf9e27777c524c5566d5162e5ad46d5251fc24 |
| TECHNICAL_STACK_AND_ASSET_REGISTER.md | c22abec8e9848ffdb3d10babfe285064efe7c805 |

The larger narrative snapshot 06_BREACH_ONE_MERIDIAN_OPENING_ARC_v1.0.md (blob cf42dbae9bfc8bdf8154989e5563a0e88052d3aa, 77269 bytes) is inventoried, not fully reread in this batch. BASELINE_INDEX's interpretation is not a substitute for its complete narrative source. Individual 13 skill bodies/metadata, VS Code files, and original design knowledge still require the remaining coverage work recorded in SOURCE_INVENTORY. SOURCES mentions earlier distribution manuals, AGENTS.zip and ARCHIVE_INVENTORY.md that have not been established as present here; those historical citations are not newly retrieved evidence.

## Source-to-candidate decisions

| ID | Source locator / requirement | Owner and disposition | Enforcement / verification |
|---|---|---|---|
| LEG-01 | AI_WORKFLOW task table; AUTHORITY approval provenance: proportional tasks, no repeated ordinary-edit approval | Preserve in design method and bounded task workflow. User's current assignment explicitly adds repository reconciliation and technical-plan approval where required. An existing genuine approval of the exact proposal may satisfy the gate; do not demand a second ceremonial decision or per-edit approval. | Runtime exact-plan checks; human provenance is not authenticated by a writable JSON file. Existing approval/dirty-plan tests. |
| LEG-02 | AUTHORITY shared records; STATE_DELTA template | M's shared game canon is distinct from .bh machine task state. Default return is proposed canonical deltas; direct game-context/ADR/roadmap editing requires exact delegated paths and limits. | Scope wrapper plus advisory producer/consumer rule; review returned diff. Clarify this in the next targeted K12 update. |
| LEG-03 | SECURITY execution envelope; REPOSITORY_AUDIT | Preserve read-only versus explicit execution/state writes. Reading scripts does not authorize Unity launch, package import, tests, credential/network changes or publication. This candidate task has explicit branch publication permission only within its output. | Host permissions + reviewed bindings + scope checks; no claim of universal interception. |
| LEG-04 | CODING_PACKAGE specification detail; CONTRACT and MILESTONE templates | Preserve actor, trigger, units, clocks, owners, public contract, semantic output, invalid/repeated/cancelled requests, ordering, lifecycle and failure meaning. Fill from approved sources, not code-agent invention. | Compiler checklist + AC/test review, not automatic semantic proof. Next targeted K12 detail amendment justified. |
| LEG-05 | UNITY content deliverables; AUTHORING_SETUP | Feature completeness includes scene/prefab/reference/input/animation/configuration, reproducible reset, inspected builder, idempotency/conflict/undo and manual Editor gaps. No fabricated GUIDs or unverified setup. | Producer checklist + Unity/manual validation; real Editor NOT_RUN. Next targeted K12 amendment justified. |
| LEG-06 | EXPERIMENT_PLAN; TEST_PLAN | Control variants and confounds, order/practice effects, participant/input/accessibility segments, privacy/consent, neutral observation, falsification, production exclusion, default/removal policy. Experiment approval is not production adoption. | Design/QA checklist and human protocol; not a claim of statistical evidence. Next targeted K12 amendment justified. |
| LEG-07 | VALIDATION; COMPLETION/REVIEW templates | Preserve separate design, architecture and implementation claims, exact command/count/workload evidence, fresh output, failed history, human-only pending judgments, comparable baseline for pre-existing/improvement claims. | Existing parsers, receipts, stale-input/zero-test tests; software tests do not prove enjoyment. |
| LEG-08 | CONTEXT; ITERATION/WORK_STATE | Small named read set, exact next action, preserve valid evidence, focused correction not full prompt/history regeneration. Optional read-only roles are not mandatory crews. | Five focused skills, checkpoints, bounded recovery; real allowance savings NOT_MEASURED. |
| LEG-09 | UNITY ownership and metadata | Preserve .meta/GUID, serialization/assembly migration, definitions versus runtime state, event cleanup, pooling/re-enable/reload tests; one final motor writer; no blanket wrapper/ECS/event-bus prescription. | Scope/paths partly deterministic; Unity engineering review and real tests required. |
| LEG-10 | Baseline DEC-PROD-002..006; PROJECT_CONTEXT §§2,5,9,11,12 | Keep combat-first, satisfying baseline, temporary-power rather than vehicle requirement, bounded/horizontal progression, one/two route choices, three source invariants, rejected VECTOR RIFT canon and exact proof order in Breach One overlay. Current overlay captures only part of these. Add compact source-located invariants without canonizing future choices. | Overlay invariant-set checks; actual behavior manual/game tests. Overlay remains SOURCE_DERIVED_UNRECONCILED. |
| LEG-11 | Baseline DEC-SESSION/PLATFORM/INPUT/ENGINE/RENDER | Preserve solo/exactly-two online target, both input families, Windows-first/URP/Unity 6.3 intent, short proof stages and operation target; Xbox conditional, mobile/four-player/replay deferred. These are not universal studio defaults or evidence of installed versions. | Project-specific overlay and human reconciliation; never add early networking simply because it is a product target. |
| LEG-12 | TECHNICAL_STACK §§3..8; DEC-UCC/AI/NAV/STATE | Retain owned/available/candidate/validation/approved-bounded distinctions. UCC final character execution; project-owned operation/shared economy/save/network meaning; BD3 validation; A*/Rewired/network remain candidates. State Designer/UIS/terrain/optimization deferred until justified. | Refer to exact asset register, not copy catalog into every task. Six asset acceptance gates retained: compatibility, ownership, testability, production value, representative behavior, exit path. |
| LEG-13 | BASELINE_INDEX reconciliation table | Dated perspective, revive, bot, narrative and four-player differences remain unresolved until current exact human decisions are retrieved. Do not infer approval from numbered replies or newer filenames. | Open decisions remain blocking for affected work, not unrelated documentation. |

## Consolidation without lost obligations

The fifteen templates need not become fifteen always-loaded Codex files. Their responsibilities map to K12's milestone/compiler/iteration/return/change workflow, the canonical shared schema, .bh generated state, operating/installation guide and project overlay. Authoring and experiment details should be additional on-demand K12 checklist sections, not a new orchestrator, state store or mandatory skill catalog. Return construction progress separately from game task state.

No copied vendor source, purchased asset, game code or original directory was changed in this review. No upstream maintenance/compatibility claim follows from the historical asset register. No current source-derived build, player test or statistical result was executed.

## Durable continuation

Next: preserve the remaining skill/VS Code source coverage, then apply the three bounded K12 clarifications (semantic detail, authoring/experiment completeness, shared-state deltas) and compact Breach One overlay expansion. Refresh affected knowledge/current distribution manifests and static tests. Keep official instruction count and all native runtime behavior unchanged unless an independently identified defect justifies an edit. Commit each batch before external-reference review. Raw 127-test outcomes are already published at review/evidence/resume-20261004.log (commit edb60c00dfda4819afce61118ee7259583414f64); the historical 125-test report is not the current rerun.
