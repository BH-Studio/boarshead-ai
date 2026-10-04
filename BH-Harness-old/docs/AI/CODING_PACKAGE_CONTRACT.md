# Detailed coding-package contract and compiler

Package: B1-CODEX-OPS | Version: 0.1.0 | Prepared: 2026-09-08
Status: CANDIDATE workflow; effective only after human adoption.

## Purpose

Codex should receive an executable specification of authorized work, not a transcript and not a
list of feature names. "Executable" here means sufficiently precise to implement and test; it
does not authorize executing documents or uninspected scripts. This contract governs future
packages after system/milestone approval. All files in `templates/` are unapproved forms. [B1-K12]

## Required package shape

Each substantial package has one ID/revision and a manifest. The minimum is a manifest,
`M##_SPEC.md`, and `M##_CODEX_PROMPT.md`. Add a separate test plan when validation complexity
warrants it. Add exact contracts, schemas, fixtures, experiment definitions and authoring/setup
instructions only when required. Work state and completion reports are outputs, not invented
pre-existing evidence. Use actual milestone IDs; `M##` here is notation only.

| Artifact | What must be complete before affected implementation |
|---|---|
| Manifest | Source revisions/approval records, read order, checkout binding, instruction-pack compatibility, writable paths, execution permissions, evidence outputs and unresolved gates |
| Milestone spec | Purpose, dependencies, scope/exclusions, locked decisions, exact behavior and failure states, deliverables, acceptance matrix and definition of done |
| Codex prompt | One outcome; required reads; inspection; phased implementation; stop conditions; exact validation references; authorized documentation and return contract |
| Contract/schema/fixtures | Actual owner, inputs/outputs, units/IDs, state transitions, timing/order, failure semantics, persistence/compatibility and examples as needed |
| Test plan | Actual command registry bindings, expected discovery, test workload/thresholds, manual gates, artifact paths and evidence mapping |
| Experiment plan | Approved variants, control conditions, resets, metrics, falsification, participant/analysis plan, toggle/default/removal policy and production exclusion |
| Authoring/setup | Exact assets/references/editor steps or inspected builder, source ownership, reproducibility, safe rerun/undo and verification |

## Compiler procedure

1. Verify human system and milestone approvals or a clearly bounded expedited exception. Pin
   exact versions/IDs, relevant ADRs, current-state revision and supplied evidence. Do not compile
   final implementation authorization out of "settled discussion" alone.
2. Resolve the read-only repository audit: actual source owners, integration seams, paths,
   packages, test harnesses, existing behavior and dirty baseline. Unknown facts stay unknown.
   A candidate package may be drafted before audit but must not claim verified path/API bindings.
3. Trace each requirement to a decision/contract, milestone AC, validation method and evidence.
   Use IDs where they add traceability. Consolidate duplicated rules; link shared policies rather
   than repeating all AGENTS text.
4. Copy approved meaning without changing behavior, schema, authority, scale, budget or scope.
   Fill units, defaults, permitted tuning ranges and error cases from inputs; never choose them
   merely to make a prompt look complete. Escalate missing semantic fields.
5. Describe implementation order and owning areas. Allow private low-level choices within the
   contract; pin external/serialized contracts exactly. Every named API must exist, be a documented
   approved new deliverable, or remain an explicit blocked assumption.
6. Bind test/build commands to inspected harnesses and actual versions. Define manual/player
   evidence and what happens if the environment cannot run it. Do not claim those checks occurred.
7. Run a compilation review: conflicting sources, broken links, unresolved required placeholders,
   unauthorized dependencies, inactive prototype flags, migration gaps, missing authoring work,
   invalid evidence retention, and unowned shared-state writes.
8. Mark COMPILED FROM APPROVED INPUTS only when the inputs and affected bindings are complete.
   Otherwise issue a DRAFT/BLOCKED package plus consolidated material questions. Compilation
   can improve clarity and order, not confer approval. Preserve exact version and supersession.

## Specification detail standard

A meaningful behavior specifies trigger/preconditions; authorized actor/owner; state transition;
outputs and semantic feedback; timing/order/reentrancy; invalid/repeated/canceled requests; reset,
scene unload and disconnect behavior when relevant; and how tests observe it. A save-dependent
feature also specifies schema/version, compatibility window, migrations, unknown content and
failure recovery. A networked transaction needs explicitly defined authority and replay/duplicate
behavior; "exactly once" is not a magic property supplied by a transport.

Example of insufficient detail: "Add revive and test it." Necessary contract questions include
who owns downed state/timer, which actions are allowed, revive eligibility/interruption, simultaneous
completion/expiry precedence, retry cleanup, solo/bot behavior, player feedback and persistence.
This pack asks for those answers; it deliberately supplies no invented revive rules.

## Scope and resources

Record nominal/target/stress/guardrail axes only where relevant: active AI, simultaneous attacks,
projectiles, VFX/audio, path requests, player count, save size and duration. Record frame/CPU/GPU,
allocation/memory, network and I/O budgets with measurement method. The supplied 60-FPS product
target is not a verified per-system budget. Do not divide it arbitrarily across middleware.

Future feasibility is not future implementation. Preserve explicit seams for the intended two-player
product, but do not add unapproved networking to an early solo proof. Claim framework reuse only
with an actual named second consumer and conformance evidence. [B1-K08; B1-CONTEXT]

## Review return and change control

A package specifies writable work/completion paths and proposed shared-state deltas. Codex returns
READY FOR REVIEW/BLOCKED. Verification uses the approved review verdicts and a focused iteration
for unresolved criteria only. Human approval is required for closure and any acceptance deferral.
