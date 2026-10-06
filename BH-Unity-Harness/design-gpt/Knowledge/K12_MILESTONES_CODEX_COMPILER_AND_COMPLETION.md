# Milestones, Implementation Package Compiler, Codex Handoff, and Completion

BH Game Systems Design Team v3 — method 3.1.0 candidate. Paired interface 1.0.0 / BH Unity Harness 1.0.0. This replaces the original K12's compiler mechanics, not the v3 design method or human authority. Retrieve `BH_INTERFACE.md` and relevant `BH_CONTRACT_SCHEMA.json` definitions before compiling, accepting returned evidence or proposing a change request.

## 1. Milestone design principles
After system approval, create a coherent, reviewable frontier. Prefer risk-first proof, contract-first dependencies, thin vertical slices and independently observable criteria. Avoid a giant batch with unlocalizable failures and micro-steps without durable value. Design exploration remains on the ChatGPT side; bounded implementation does not remove alternatives, research, specialist review or red-team analysis before approval.

## 2. Milestone spec template
```markdown
# M## — Milestone name
Status: DRAFT / QUESTION GATE / READY FOR APPROVAL / APPROVED / IN PROGRESS / READY FOR REVIEW / COMPLETE
Project and parent system:
Dependencies and authoritative versions:
## Purpose and intended player experience
## Why now / risk retired
## In scope / out of scope
## Locked decisions, assumptions and open questions
## Required behavior, rules, formulas and invariants
## State ownership and architecture / interfaces
## Data/schema, persistence and migration impact
## Integration points and purchased-asset boundaries
## Nominal, target, stress and failure scale/resource budgets
## Reuse/extension and clean-consumer expectation
## Failure, recovery and observability
## Content/authoring, UX/audio/accessibility requirements
## Deliverables and exact file/contract ownership
## Acceptance criteria
REQ-... → AC-... → observable expectation → automated or human
## Verification matrix
CHECK-... → AC-... → profile/adapter → expected output/test names/count
## Documentation and durable state updates
## Definition of done, deferred items and revisit triggers
```

## 3. Milestone question and approval gates
Before finalization inspect behavior, contracts, compatibility, scale, testing, scope and missing facts. Consolidate BLOCKING / DESIGN-SHAPING / TUNING / DEFERRED questions. Do not re-ask settled system decisions. Delegation must be recorded; it does not authenticate subsequent approval. Present the exact milestone version READY FOR APPROVAL. An approved overall system is not automatic milestone or technical-plan approval.

## 4. Implementation Package Compiler
After genuine milestone approval STOP DESIGNING. Compile the approved system, milestone, ADRs/contracts, current state and validation requirements. Clarity, ordering, cross-reference checks and test mapping are permitted; changing behavior, schema, architecture, scope, scale targets or acceptance expectations is not. Conflicts return to the human/design boundary.

Require the actual pinned BH Unity Harness distribution with manifest. Never replace it with a moving URL, independently generated core policies or an instruction for Codex to invent the missing package. The human's practical handoff contains:

1. The reviewed standard package or a resolvable immutable distribution reference, manifest and safe install/merge instructions.
2. Only the current approved design/milestone and relevant contracts/ADRs, criteria, overlay and actual artifact hashes.
3. A versioned `handoff` object and one startup prompt; genuine design approval is correlated to the exact canonical subject.
4. Test specifications, observable expectations, human-only criteria, stop conditions and the required return format.

Use schema `criteria`, `overlay`, `handoff` and `approval`; do not maintain competing field definitions here. Preserve source names such as PROJECT_CONTEXT and CURRENT_STATE as design artifacts, not competing machine task state. A DRAFT may be validated structurally but cannot initialize execution. A missing standard/knowledge file/approval, unmatched hash, lost invariant, dropped criterion or unresolved material decision blocks compilation/execution. Never manufacture facts to make a sample look ready.

Project policies and narrative remain project-owned. Common AGENTS.md and skills are versioned standard files; game-specific constraints belong in the thin overlay and approved task documents. Review existing policies and nested instructions before installation; an installer backup is not consent to overwrite them. Existing game tool/asset inventory must distinguish owned, installed, validated and approved.

## 5. Codex startup template
```text
Use the installed BH Unity Harness 1.0.0 and $bh-review-handoff.
Read applicable AGENTS.md and the handoff at <actual game-relative path>.
Validate the complete pinned manifest, criteria, invariants and genuine approval source.
Reconcile actual repository, Unity, package, target, pipeline and tool facts.
Preflight is nonmutating. I authorize the declared task/plan records in .bh only.
Prepare the bounded technical proposal and exact approval subject; do not edit game code.
Report conflicts, unavailable required checks and the next decision. Do not replace the
standard, add dependencies, infer approval or use API credits.
```
Replace the path only after the actual artifact exists. After separate plan approval use the approved-slice prompt in the harness operating guide. Unresolved configuration is an explicit block, not a reason to relax required tests.

## 6. Focused iteration template
```markdown
# Codex Iteration — project / task / milestone
Milestone remains OPEN.
## Prior handoff and exact tested source
## Retrieved evidence / failed check and actual observation
## Unresolved AC IDs
## Bounded correction and permitted paths/actions
## Locked constraints unchanged
## Explicitly excluded work
## Revalidation needed and human-only criteria still pending
## Approval required for changed design / plan
## Required completion evidence and next review
```
Do not regenerate unrelated scope or restart from the complete design library. Start from the observed failure and likely files, expand only when evidence requires, then stop at the verification boundary. If a change affects design, issue a change request rather than quietly changing the implementation target.

## 7. Returned-results review order and verdicts
Retrieve the actual evidence before judging: scope diff → contract conformance → build/static diagnostics → focused correctness → integration/conformance/regression → performance/scale/stress → design/player behavior → durable state. Claims, proposed tests, screenshots or zero exit codes alone do not demonstrate correctness. Keep failed attempts and missing/not-run outcomes visible. Current raw artifacts, source/configuration hashes, task/project identities and AC mappings must agree.

Use READY TO CLOSE, PASS WITH DEFERRED ITEMS, ITERATION REQUIRED, DESIGN CHANGE REQUIRED or BLOCKED. These are review recommendations; only the human closes the milestone. Preserve pending human playtest even when every automated check passes. A source-defined expected behavior that disagrees with a green test is DESIGN CHANGE REQUIRED or ITERATION REQUIRED, not evidence that the approved design changed.

## 8. Completion report and design review template
```markdown
# M## — Completion / design review
Status: READY FOR REVIEW / COMPLETE only after human closure
Project/task, handoff version/hash, exact source revision and dirty-input snapshot:
Evidence transport and files actually retrieved:
Review independence and unavailable evidence:
## Scope delivered and file/component diff
## Claims versus verified observations
## Criterion table: AC ID | expectation | result | receipt/raw evidence | limitation
## Build/static, focused, contract/persistence, integration/regression results
## Performance/scale: workload, units, thresholds, observed result
## Playtest/UX/narrative/accessibility and unresolved design validity
## Deviations, decisions/ADRs, risks and documentation updates
## Review verdict and bounded correction/change request
## Deferred work, owner/revisit trigger and impact on next milestone
## Human closure decision, source and exact accepted snapshot
```

## 9. Integration gates and final system acceptance
Periodically compare the accumulated system, not only the most recent milestone: architecture/dependency drift; API/schema stability; aggregate resource use; save/migration compatibility; neighboring regressions; duplication/technical debt; clean-consumer/reuse evidence; authoring burden. Use risk-triggered gates, including after shared contracts or persistence changes and before major dependency fan-out. At final acceptance compare original requirements, implemented behavior, integration, scale, design hypotheses and known limitations. Do not equate last milestone closure with system acceptance.

## 10. Change request and feedback transport
Use schema `change_request`, retaining prior handoff hash, prior/new decision, reason, alternatives, affected AC/check IDs, impacts, evidence and genuine approval. PROPOSED is not HUMAN_APPROVED. A material approved change invalidates/re-evaluates the affected plan and evidence; issue a new bounded task and preserve old history. Do not lower a test target simply to fit existing code.

Transfer RETURN.json/RETURN.md, pinned design/handoff, referenced receipts and the relevant raw artifacts by explicit upload or human-authorized immutable repository paths. Local paths alone cannot be read by the design GPT. Mark evidence unavailable until retrieved. Do not imply automatic communication among ChatGPT Projects, custom GPTs and Codex.

## 11. Source-retained detail checks (retrieve only when applicable)
Use these checks while preparing the milestone and its test/authoring plan, not as a second always-loaded Codex policy. They retain the inspected legacy templates and specialty skills; record a reason for inapplicable categories rather than inventing new scope.

**Behavior and contracts.** Specify actor, trigger/preconditions, canonical owner and allowed writers; input units/ranges/stable IDs; exact transition and semantic feedback; clock/order/reentrancy; repeated, stale, invalid and cancelled requests; reset, disable/re-enable, pooling, scene unload and disconnect where relevant. Separate definitions, instance state, campaign state, participant knowledge and presentation. Identify existing APIs versus explicitly approved new deliverables. Do not choose missing player behavior merely to fill a template.

**Authoring completeness.** Name the scene/prefab/definition purpose, actual source assets, component/reference/input/animation/layer bindings, metadata ownership, entry/reset and observable checks. An inspected builder needs safe roots, idempotent rerun, conflict/undo/cancellation handling and preservation of hand-authored work. Never invent GUIDs or claim an unavailable Editor step completed. Scripts without required configuration are an incomplete feature.

**Experiments and measurement.** An experiment needs its own bounded approval or recorded exception, controls/variants and deliberately changed factors, common content/build/configuration, reset and seed policy when needed, input/participant/accessibility segments, order/practice effects, confounds, privacy/consent and neutral observation. Specify falsification, approved versus proposed thresholds, warm-up/repetitions/distributions for performance, instrumentation overhead and actual raw-evidence capture. Keep default/toggle/removal and release/save exclusion explicit. Do not select a winner or infer production adoption from a prototype pass.

**Persistence, co-op and narrative.** Apply only to approved scope: stable IDs versus display/process handles, old-data compatibility, partial writes/corruption/unknown content and approved recovery; never destructive tests on a player's only save. Network host, save owner, narrative choice and participant consent are different authorities. Test duplicate/reordered/cancelled transactions and separate processes where required; do not assume exactly-once delivery. Keep world truth, player knowledge and dialogue history distinct; preserve the current project's approved reveal/recap/retry and information-access rules without assuming equal roles, sample dialogue, optional bots or future session features.

**Shared-record deltas.** .bh machine task state is not PROJECT_CONTEXT, CURRENT_STATE, the decision register or roadmap. Codex proposes each canonical delta with target section, prior/new statement, observed evidence, affected scope and unresolved conflict. Direct publication requires explicit delegated files/fields and limits; preserve superseded history. Design approval, implementation evidence, accepted risk and human closure remain separate statuses. An existing genuine approval of the exact reconciled technical proposal may satisfy its gate; never ask again for ordinary edits already covered.

## 12. Game-agnostic compilation boundary
The reusable package defines workflow, not a game design. Obtain project identity, genre, mechanics, narrative, player counts, state rules, required middleware, rendering pipeline and numerical budgets from current approved project artifacts. Never extract defaults from an old project, a reference worked example or an evaluation fixture. Empty/unknown project facts remain explicit blockers for affected work. Preserve the project-overlay extension mechanism, but ship only clearly synthetic generic examples; generate a real overlay only for the explicitly identified project. Historical source records are review references and are not Instructions or knowledge uploads.
