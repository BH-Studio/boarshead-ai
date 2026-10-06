# BH design / execution interface 1.0.0

Owned by `contracts/schema.json`. The copies named `BH_CONTRACT_SCHEMA.json` in design knowledge and `.bh/schema.json` in the installed game must be byte-identical. This document is likewise copied unchanged to the two consumers. The small local validator supports only the schema vocabulary used here, rejects unknown fields/keywords, and never resolves remote schema references. It is not a general JSON Schema implementation.

## Compatible pair and authority

| Producer | Interface | Execution harness | Disposition |
|---|---|---|---|
| BH Game Systems Design Team v3 method 3.1.0 candidate | 1.0.0 | BH Unity Harness 1.0.0 candidate | Eligible for pilot after local validation and human adoption |
| Legacy project-specific package | Legacy contract | Prior harness | Preserve current slice; migrate deliberately, never relabel old evidence |
| Any other version combination | Any | Any | Reject; review an explicit migration before compilation/execution |

The design method owns proposals, specifications, requirements and design review. The human owns decisions and approvals. The harness owns execution state, verified observations and receipt freshness. Native Codex instruction precedence is not this policy's authority hierarchy and can bypass it; host permissions and genuine human review remain necessary.

## Required design resources — producer only

This section governs the design host. Codex consumes the approved handoff and `Docs/Harness/CODEX_CONSUMER.md`; it does not retrieve producer personas or frameworks to execute a task. Compact views from `Tools/BH/views.py` are derived reading aids, not replacement wire contracts. Full records and approval subjects remain authoritative and retrievable.

For full system/foundation work retrieve `01_GPT_INSTRUCTIONS_FULL.md` and `K01_PERSONAS_AND_ROUTING.md`. The retained full file preserves the design workflow; only its older compiler procedure is replaced by current K12 and this interface. Full/reference documents do not acquire higher instruction priority by being uploaded.

| Procedure | Exact knowledge filename |
|---|---|
| Personas / routing | K01_PERSONAS_AND_ROUTING.md |
| Player experience / dynamics / mechanics | K02_FRAMEWORK_MDA.txt |
| Repeated activity / time scales | K03_FRAMEWORK_CORE_AND_NESTED_GAMEPLAY_LOOPS.txt |
| Causal relationships / feedback | K04_FRAMEWORK_SYSTEMS_THINKING_AND_FEEDBACK_LOOPS.txt |
| Resources / economy | K05_FRAMEWORK_MACHINATIONS_RESOURCE_FLOW.txt |
| Player skills / difficulty / parameters | K06_FRAMEWORK_RATIONAL_GAME_DESIGN.txt |
| Current evidence / comparables / sentiment | K07_RESEARCH_AND_PLAYER_EVIDENCE.md |
| Architecture / scale / reuse | K08_ARCHITECTURE_SCALING_REUSE_AND_INTEGRATION.md |
| Validation / red team / quality gates | K09_VALIDATION_RED_TEAM_TESTING_AND_QUALITY_GATES.md |
| Durable artifacts / decisions | K10_ARTIFACTS_DECISIONS_CONTEXT_AND_TRACEABILITY.md |
| Applicable procedural / persistence lessons | K11_GENERALIZED_DELIVERY_LESSONS.md |
| Milestones / compilation / return / closure | K12_MILESTONES_CODEX_COMPILER_AND_COMPLETION.md |
| Shared interface rules | BH_INTERFACE.md |
| Exact structured contracts | BH_CONTRACT_SCHEMA.json |

Retrieve only applicable framework procedures, not every document every turn. Before compiling or reviewing a handoff retrieve K12, this interface and the relevant schema definitions. Record missing/partial retrieval and stop that dependent operation rather than fabricating a resource. Continue independent design work only where it does not need the missing authority.

## Producer: a complete bounded package

The package contains an approved design/milestone specification; applicable architecture/data contracts; stable requirement-to-acceptance mapping; a project overlay; a handoff JSON; a standard-distribution reference; and one startup prompt. The standard distribution is the reviewed, pinned `BH-Unity-Harness` package, including `PACKAGE_FILES.json`, its installer and `project-template`. A moving default-branch URL or an instruction to recreate the standard is not a distribution.

Use the schema definitions `criteria`, `overlay`, `handoff`, `approval`, `proposal`. All fields in each definition are required unless the schema explicitly says otherwise. An unavailable value is not permission to invent it. IDs are portable, case-sensitive, unique, at most 64 characters; paths are relative to the actual game root, with `/` separators, no traversal, drives, UNC paths or symlink/junction escape. Data is UTF-8 JSON with no duplicate keys or nonfinite numbers.

`handoff` binds `version`, `harness_version`, `design_method_version`, `project_id`, `task_id`, `milestone_id`, `synthetic`, `status`, objectives/non-goals/assumptions, `source_commit`, artifact hashes, design/criteria/overlay paths, `read_order`, acceptance/invariant IDs, allowed/protected paths and allowed actions. It also carries architecture/data references, dependencies, migration impact, risk controls, questions, checks, required verification profile, stop conditions, startup, return format and design approval. All referenced design inputs must be in `artifacts` with actual SHA-256 hashes. `source_commit=null` explicitly means not yet pinned; actual technical reconciliation still has to establish the repository baseline.

The overlay preserves project invariants with source references, protected paths, optional capabilities, known facts, open decisions and provenance. `SOURCE_DERIVED_UNRECONCILED` cannot execute; `RECONCILED` requires real repository/human review. `SYNTHETIC` is only for visibly marked disposable fixtures. Source projects and synthetic fixtures never supply another project's defaults. The standard selects no game, genre, mechanics, lore, player count, middleware or rendering pipeline; current approved project inputs own those choices.

Every acceptance criterion has stable `id`, `requirement_ids`, `expected` and `kind` (`automated` or `human`). Each criterion needs at least one required check. Every check has `id`, mapped `ac_ids`, required flag, adapter, profile, observable expectation, named tests/minimum count where applicable, and an optional N/A reason. Required checks cannot become N/A; automation cannot certify human criteria. Named NUnit tests and a positive discovery count are required. Dropping an acceptance ID, invariant, required check or artifact fails validation.

A `DRAFT` is structurally inspectable using `validate-handoff --draft`; it is not executable. A `COMPILED` handoff requires no blocking/design-shaping questions, a reconciled overlay and a matching human design-approval record. It becomes eligible for technical reconciliation, not approved for game mutation. Do not independently regenerate common AGENTS.md, skills, schema or safety policy. Project-specific test/design guidance belongs in the approved task artifacts, not a second conflicting common harness.

## Approval subjects and writes

Canonical hashes use sorted-key compact UTF-8 JSON, finite numbers only. File hashes use exact bytes. Do not confuse the two.

Design approval subject: canonical hash of the complete handoff excluding its `approval` field. Plan approval subject: canonical hash of the exact generated plan. Acceptance subject: canonical hash of `{snapshot: current_snapshot.sha256, plan: state.plan.sha256, handoff: state.handoff.sha256}`. These different subjects prevent design approval being silently reused for execution or acceptance.

`approval` records specify identity, kind, actor=human, source kind, genuine source reference, name, UTC timestamp, subject hash, scope/limits, synthetic status and human-criterion observations. Empty or fabricated approval records never create authorization. The runtime validates structure and correlation, not whether a person really wrote or understood the approval. The human/session must inspect that original source. There is no signing service or separate trust boundary.

Preflight and draft validation are nonmutating. The user may explicitly permit installation/configuration and task/plan/evidence writes before code approval. `init`, `plan`, `approve`, `begin`, `verify`, `resume`, `return`, `pause`, `claim`, `recover`, `checkpoint`, `cancel`, `accept`, `archive` write designated `.bh` records; they are not read-only just because they do not edit gameplay. Verification processes can also write Unity-generated directories and must be reviewed for their actual effects.

## Consumer: reconcile, plan, approve, execute

Run preflight at the real Git root, validate the handoff, initialize unique task state and prepare the `proposal`. Inspect actual code/tests, Unity patch, packages, targets, render pipeline, asset ownership, nested/global instructions, diagnostics bridge and tool versions. Unavailable required tools block the plan/check. Preserve source facts rather than swapping a middleware package to get a green result.

The `plan` captures proposal, handoff/configuration/harness hashes, full tested-input baseline, scope, protected paths, allowed actions and required checks/profile. It cannot silently widen the handoff. Review it and obtain genuine approval of the exact subject. Ordinary authorized edits then proceed without repeated approval, but material design/architecture/dependency/persistence changes stop. Unity launching additionally requires `launch-unity` in approved actions.

## Return and practical transport

`return` produces `.bh/exports/<task>/RETURN.json` and `RETURN.md`, format `BH-RETURN-1.0.0`. It includes current source snapshot (commit, dirty status and file hashes), claims, criterion statuses, receipt references, deviations, design questions, human acceptance, independence limits and next action. Logs are separate, not pasted wholesale into the summary.

Upload the return together with the pinned handoff/design and only the referenced receipts/raw results needed for the current questions; alternatively publish those reviewed/redacted files to a human-authorized branch and give the design GPT the immutable commit and paths. A local `C:\...` or `.bh/runs/...` string is not remotely accessible. Until the files are actually retrieved, the GPT records evidence unavailable. Hashes correlate inputs/artifacts; same-workspace writers can forge both, so they are not independent attestation.

The design review checks scope, contracts, build/static, focused correctness, integration/regression, performance/scale, design behavior and durable state. Preserve `PASS`, `FAIL`, `ERROR`, `NOT_RUN`, `BLOCKED`, `NOT_APPLICABLE`, `HUMAN_PENDING` and explicit human deferrals. Only current matching evidence can support a claim. A passing code test does not prove onboarding, accessibility, narrative, usability or game feel.

## Change and closure

Emit a schema-valid `change_request`: old/new decision, reason, alternatives, affected acceptance/check IDs, impacts, evidence references, prior-handoff hash, `invalidates_plan_approval=true` and approval only when genuinely supplied. `PROPOSED` is not executable. The human approves the decision; a new bounded handoff/task is compiled and reconciled. Cancel/archive the old task explicitly before adopting a new active task; do not rewrite its approvals or receipts. Changes to configuration/core/handoff or Git baseline require replan/reapproval. Input edits invalidate affected verification. The safe default is whole-input dependency binding; narrow dependencies require a recorded review and always retain common-core dependencies.

`READY_FOR_HUMAN_REVIEW` is automation's limit. A human-only criterion remains pending or receives a real recorded PASS/ACCEPTED_DEFERRED with evidence, reason and revisit trigger. The separate `accept` operation records acceptance of the exact snapshot. Later edits invalidate that acceptance claim even when the historic state says ACCEPTED. Human Git integration is separate; the wrapper never merges or publishes.

## Efficiency reading aids and final evidence
The installed views.py can emit BH-CONTEXT-VIEW-1 and BH-RETURN-VIEW-1. These are derived projections, not replacement handoff/approval/return schemas. For routine returned-evidence review prefer AGENT_RETURN.json, its complete criterion/deviation list and current supporting receipts. The hashed full_return and history_index are retrievable references; fetch their full contents only for questions requiring them. Missing underlying required evidence still blocks the claim. Do not regenerate the entire path/hash roster in a model response.

Consumer verification may select approved check IDs and reuse validated original results for intermediate work. Completion still requires all required checks from one complete fresh profile run; reused or mixed partial runs cannot substitute. Ordinary FAILED repair below thresholds consumes no exceptional recovery cycle. Strict commit, executable binding, scope and approval boundaries are unchanged. See the owned CODEX_CONSUMER.md for actual commands and remaining prerequisite/checkpoint limitations.
