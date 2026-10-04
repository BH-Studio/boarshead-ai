# <actual milestone ID> — <title>

Status: TEMPLATE — NOT AUTHORIZED
Revision/date: <actual>
Parent approved system and approval: <exact artifact/revision/record>
Milestone human approval: NOT RECORDED
Owner / dependencies / supersedes: <actual>

## 1. Purpose, player/developer outcome and risk retired

Describe the observable capability and why this is the next coherent proof. State relevant
experience → repeated behavior → mechanic relation without claiming it is already validated.

## 2. Starting baseline and prerequisites

Pin actual checkout, Unity/packages, existing capabilities, contracts and prerequisite evidence.
Separate reported state from directly observed implementation and missing evidence.

## 3. In scope / explicit exclusions

Name delivered behavior and required code/configuration/content/tooling/tests/docs. Name adjacent
systems that must not be implemented. Future-feasibility boundaries are not future features.

## 4. Locked decisions and bounded implementation choices

| Decision/contract | Exact approved meaning | Rationale | Source/approval | Tunables with approved range |
|---|---|---|---|---|
| <ID> | <actual> | <brief> | <locator> | <range/units or none> |

## 5. Required behavior and invariants

For each behavior, supply actor/preconditions, trigger, authoritative owner, validated inputs,
transition, outputs, semantic feedback, time unit/clock, ordering/concurrency, and invariants.
Specify repeated/invalid/stale/canceled requests, reset/retry/unload, simultaneous outcomes and
failure/recovery. Do not leave Codex to choose design behavior to complete these fields.

## 6. Ownership and contracts

List each state category: definitions, runtime instance, campaign/session, participant knowledge,
presentation/cache. Identify canonical owner, permitted writers/readers, lifecycle and dependency
direction. Reference exact APIs/events/schemas or explicitly approved new deliverables. State
what remains UCC-local and what remains project policy where relevant.

## 7. Data, save and compatibility impact

Record stable IDs/units, old/new versions, semantic or byte equality, migration/old-data window,
unknown/missing definition and corruption behavior, atomicity/recovery and unchanged boundaries.
Use NO CHANGE/NOT APPLICABLE with reasons instead of speculative persistence architecture.

## 8. Integration, session and presentation

Specify affected neighbors and allowed interactions. For network scope, include validated owner,
request/result/idempotency/failure behavior and process tests. For UI/audio/input, specify what
players must perceive, accessibility/feedback and control transitions. Do not select a backend
or alter narrative reveal/consent rules from an open recommendation.

## 9. Content and authoring

List exact scenes/prefabs/assets/definitions, component/reference ownership, setup or inspected
builder, reproducible reset/rerun, invalid-data feedback and manual checks. State when a human
Editor step is still required and what gate remains open until it is verified.

## 10. Scale and resource envelope

| Axis/workload | Nominal | Target | Stress | Guardrail behavior | Measurement/units | Source/approval |
|---|---|---|---|---|---|---|
| <relevant axis> | NOT SET | NOT SET | NOT SET | <specified> | <method> | <locator> |

Specify environment/settings, relevant frame/CPU/GPU/memory/network/I/O budgets, or reason for
not applicable. No copied galaxy counts or arbitrary allocation of the whole frame budget.

## 11. Deliverables and acceptance criteria

| AC | Required observable result | Requirement/contract | Validation | Required evidence | Blocker |
|---|---|---|---|---|---|
| <AC-ID> | <precise pass/fail rule> | <reference> | <method> | <artifact/locator> | <yes/no> |

## 12. Validation matrix and human checks

Reference the bound test plan or include it here. Cover relevant static, focused, contract,
PlayMode, player, persistence, co-op, scale/stress, regression, content and playtest claims.
Distinguish planned from executed; human checks cannot be silently replaced by automation.

## 13. Risks and unresolved question gate

List severity, evidence, failure scenario, smallest validation, owner and revisit trigger.
Group unresolved questions as BLOCKING / DESIGN-SHAPING / TUNING / DEFERRED. No self-approval.

## 14. Durable records and definition of done

Name allowed work/completion outputs and shared-state delta proposals. Done requires delivered
scope, required evidence, reviewed deviations and actual human acceptance, not only successful
compilation. Record explicitly accepted deferrals; leave the milestone open otherwise.
