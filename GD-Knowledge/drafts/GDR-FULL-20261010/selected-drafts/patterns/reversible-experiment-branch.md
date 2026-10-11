---
id: GDR-CAND-20261010-G13-PAT-02
kind: pattern
title: Reversible experiment branch
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_identity: G13-authoring-20261010-A1
predecessor_sha256: null
supersedes: null
change_summary: Initial G13 capture in this session; no predecessor G13 artifact was
  supplied or located in the bounded retrieval.
identity_scope: temporary-run-scoped-candidate
run_id: GDR-FULL-20261010
batch_id: G13
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_state: coverage-open
independent_review_state: not-yet-reviewed
aliases:
- isolated trial state
- try without committing
- protected experiment copy
tags:
- recovery
- experimentation
- state-boundary
- rule-fidelity
- hypothesis
- coverage-open
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G13-PAT-01
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G13-GEN-01
- GDR-CAND-20261010-G13-GEN-02
- GDR-CAND-20261010-G13-GEN-03
source_ids:
- GDR-SRC-20261010-G13-012
- GDR-SRC-20261010-G13-013
- GDR-SRC-20261010-G13-014
reviewer: null
approved_by: null
approved_date: null
byte_hash_record: ../reviews/full-run-20261010-g13-integrity-receipt.md
proposed_domain_owner: BH-GDR-Foundations-and-Systems; coordination decision pending
---

# Reversible experiment branch

**Draft 0.1.0 · GDR-CAND-20261010-G13-PAT-02 · hypothesis, coverage-open.** Offer an explicitly isolated trial state for a consequential experiment, with an honest path back to the protected original. This is a conceptual design pattern. It is not a save-system implementation, a guarantee against data loss or a claim that consequence-free experimentation is always desirable.

## Purpose

Address a player's reluctance to test an unfamiliar configuration when the original state has value and a misleading or incomplete rollback would violate the experience's promise. The intended outcome is an opportunity to investigate consequences without committing changes to a declared protected state. Separate **state preservation**, **learning a rule** and **willingness to experiment**; none proves the others. [C-01, C-04]

## Context and prerequisites

Consider a branch when a coupled change is too broad for an ordinary local undo, when the state can be isolated at a meaningful boundary, and when the intended experience permits previewing consequences. Examples include a settlement layout, a simulated routine or a construction experiment. These are illustrative applications, not verified shipped uses of this exact pattern. [C-04]

The design needs an identifiable original, a defined branch start, a rule/version/configuration record and a reliable choice to keep the original or continue from the branch. It needs a policy for time, random state, inventory, schedules, permissions, external services and shared actions. If relevant effects cannot be isolated, either narrow the promise or choose a different technique. Never call the branch safe merely because a save file was copied. [C-03, C-05]

## Mechanism and evidence

Wube's undo retrospective describes omitted operations and uncertainty about distant undo targets. Minecraft's experimental-feature guide documents a copy workflow for an existing world in a particular Bedrock route and warns about experimental content. These show two different production concerns: operation coverage and isolated version testing. Neither directly establishes this pattern's player-facing causal effect. [C-02, C-03; GDR-SRC-20261010-G13-012; GDR-SRC-20261010-G13-014]

| Proposed causal link | Evidence support | Limit / necessary test |
|---|---|---|
| A declared state boundary can be preserved while a separate state changes | Documented copy precedent; logical design possibility | The actual protected state and external effects require verification |
| A faithful trial can expose consequences of a candidate action | Inference if rules and relevant initial conditions match | Altered simulation rules, random state or hidden time can invalidate the comparison |
| Explicit origin/branch labels can prevent accidental commitment | Hypothesis informed by Wube's report of undo-target ambiguity | Labels can be ignored or misunderstood; test choice and recovery |
| Available recovery can increase useful experimentation | Hypothesis, not established by either source | It may instead reduce tension, encourage indiscriminate trials or spoil discovery |
| Trial experience can improve later decision-making | Hypothesis requiring rule discrimination and delayed assessment | One copied successful action is not transfer; irreversible player knowledge remains |

The strongest recommendation is conditional: **offer a branch only when its protected-state boundary and rule fidelity can be demonstrated, and when advance experimentation belongs in the intended experience.** No universal recovery guarantee or required branch feature follows. [C-04–C-06]

## Recipe

1. **Name the consequential question.** Specify the action the player wants to investigate and the valued state they do not intend to commit. Ask whether a readable forecast, small preview or local undo would answer the same question with less complexity. [C-04, C-07]
2. **Define the protection boundary.** Enumerate the state covered by the promise: not only objects, but relevant resources, schedules, timers, permissions and dependencies. Record what is not covered, including remembered discoveries or other people's actions. This is a proposed conceptual inventory, not engine code. [C-05]
3. **Establish an unmistakable branch origin.** Identify the original, branch creation point, rules/version and relevant options. Give the branch a persistent, accessible label and preserve the origin through save/load. Avoid relying on color alone. [C-05, C-08]
4. **Choose the fidelity contract.** Either preserve the rules relevant to the question or explicitly label a changed-rule demonstration. A no-cost construction mode cannot silently prove that the original settlement can afford the construction. A changed seed cannot establish the same event sequence. [C-06]
5. **Isolate changes before the experiment.** Prevent unintended writes to the protected original and any external state covered by the promise. Declare how time and autonomous activity behave outside the branch. If isolation is unavailable, stop and use a limited forecast or an independently created test scenario instead. [C-05]
6. **Let the player investigate a bounded contrast.** Support the proposed action and an informative contrasting case. Preserve useful access supports. Let the player ask “what happens?” without treating the choice to avoid or accept the consequence as correct or incorrect. [C-06, C-09]
7. **Make disposition explicit.** Offer a clearly distinguished return to the protected original or continuation of the branch as the chosen play state. Do not silently merge arbitrary histories. Any proposed merge needs its own conflict, ownership and fidelity design and is outside this pattern's current recipe. [C-05]
8. **Verify the promise before assessing its benefit.** Check all protected state after branch creation, re-entry, return and interruption. Only then evaluate comprehension and experimentation. If an excluded effect makes the advertised question unanswerable, revise or withdraw the branch rather than hide the limitation. [C-05, C-09]

### Adjustable variables

Proposed variables include branch scope, lifetime, state fidelity, random-state handling, time behavior, naming, persistence, disposition choices and whether previews expose hidden information. No storage budget, autosave interval, checkpoint frequency or participant count is prescribed. The simplest adequate boundary is preferred as a hypothesis about clarity and production burden, not a quantified optimization result. [C-05, C-07]

## Worked examples

**Illustrative: rerouting a settlement's heating and water network.** The player wants to test whether a new route will leave a distant workshop without service during the next work period. The original includes the existing layout, stock, work schedules, current time and relevant options. A labelled branch records that state and runs the same relevant rules. A more modest alternative is a network connectivity preview; use the branch only if delayed interactions genuinely matter. [C-04–C-07]

In the branch, the player moves a junction and advances through the work period. The test records both the target workshop and an off-screen dependency. On returning, the original's junction, stock, schedule and time are unchanged under the proposed protection contract. The player still remembers the trial. If a cloud service, shared player or external clock changed something relevant, the branch must either have excluded it clearly or cannot claim complete recovery for this question. No such prototype was executed in G13. [C-05, C-06]

A contrasting branch retains the same routing rule but uses a feasible resource situation rather than an infeasible one. Ask for the outcome before executing it. Changing the rule itself—for example by disabling material costs—is a separately labelled mode demonstration, not proof of transfer under the original rule. The player may knowingly choose a less efficient layout for its appearance; that does not negate correct prediction. [C-06, C-09]

**Illustrative: daily-life planning.** A designer might offer a private trial of a household schedule while preserving the original narrative state. A branch that lets the player discover every relationship response can undermine an intended commitment or discovery experience. A calendar preview with uncertain outcomes may be preferable. Never present predicted fictional relationships as validated models of real people. [C-07, C-08]

## Tradeoffs and alternatives

A local undo is preferable when the important action and its dependencies can be reversed faithfully without maintaining a separate world. A preview can be preferable when a consequence is predictable and a full simulation adds no information. A fresh test scenario can be useful when the player only needs to learn an invariant rule, not inspect their precise current state. A forgiving mode changes consequences rather than preserving the same decision conditions; it may be valuable but is a different intervention. [C-06, C-07]

Branches add persistence, migration, discovery-spoiler and authority risks. Arbitrary merges add another problem and are not included. A deliberately irreversible decision can be valuable when stakes are legible and appropriate to the intended experience; do not erase it by default. [C-05, C-07]

## Failure cases

| Failure | Observable warning sign in a proposed evaluation | Response |
|---|---|---|
| Partial restoration masquerades as recovery | A protected stock, timer or off-screen dependency changes | Reject the safety claim; repair the boundary or narrow it explicitly |
| Branch rules differ silently | A successful trial fails under the original affordability or scheduling rule | Preserve the relevant rule or label a different-mode demonstration |
| Branch/original confusion | The player continues or replaces the wrong state | Improve persistent identification, simplify disposition or remove replacement |
| External state leaks | Shared work or an external service changes during a “private” test | Stop that use; do not promise isolation without authority |
| Time exposure invalidates the question | The original progresses while the player believes it is protected | Disclose and redesign time behavior or use a narrower forecast |
| Restored state is mistaken for restored ignorance | A mystery or relationship outcome remains known | Treat knowledge as irreversible; choose a different experience or avoid the branch |
| Branching overwhelms ordinary play | Players cannot identify which state contains the intended project | Reduce available branch persistence and choices, or substitute local undo |

These are author-proposed diagnostics, not observed failures of the named products. Wube's historical omissions are separately recorded as practitioner evidence, not as a reproduction of these hypothetical cases. [C-02, C-05–C-09]

## Counterexamples and do not use conditions

Do not use this pattern to promise rollback over external purchases, real communications, non-isolated multiplayer state or other people's independent work. Do not deploy it where the intended question depends on irreversible discovery and a preview would defeat that experience. A short, inexpensive local action may need only undo; a static tool may need neither. [C-07, C-08]

The official Minecraft restoration/recreation help result remains **lead-only** because its article body was inaccessible. It supplies no evidence that a seed recreates a prior state or that any recovery method is complete. The inspected experimental-world copy procedure is a different source and a narrower precedent. [C-03; GDR-SRC-20261010-G13-013; GDR-SRC-20261010-G13-014]

## Playtest

**Proposed, NOT PERFORMED.** First perform separately authorized fidelity tests against a declared state inventory. Include an interruption, off-screen dependency, saved setting and a queued action. A reproducible protected-state violation rejects that protection promise regardless of reassuring participant responses. This authoring task executed no engine or project code. [C-09]

For a later player comparison, use the simplest credible alternatives: forecast/local undo versus a branch, not a deliberately unsafe control. Match the substantive question, access aids and instruction quality. Record relevant prior experience and whether participants prefer irreversible stakes or exploratory composition; these are recruitment dimensions, not proven genre populations. Justify sample size and practical benefit/harm limits before collection. [C-09]

Measure branch/original identification, predictions for contrasting cases, correct disposition, restoration accuracy and self-chosen experiments attempted. Separately ask whether the feature spoils stakes or discovery. Do not treat more experiments as better without examining their relevance to the participant's intention. Reject the added feature when it offers no relevant advantage over the simpler alternative, creates unacceptable confusion, or undermines the intended commitment even while recovery functions. [C-09]

## Related entries, ownership and unresolved questions

Genre adaptations: [colony simulation](../genres/colony-simulation.md), [life simulation](../genres/life-simulation.md) and [sandbox](../genres/sandbox.md). Complement: [scoped autonomous changes](scoped-autonomous-changes.md). The inspected `GDR-CAND-20261010-F01-PAT-01` supplies the corrected rule-discrimination test; `GDR-CAND-20261010-F07-PAT-02` supplies a distinct commitment/exit context. This pattern proposes isolation and return-to-origin semantics rather than relabelling either upstream entry. Novelty, ownership and overlap remain pending Library Coordination. [C-10]

See [dependency manifest](../reviews/full-run-20261010-g13-review-packet.md#reviewed-dependency-manifest) and local issues G13-CON-04/G13-CON-05. Missing evidence includes actual persistence-failure behavior, longer-term learning, representative willingness to experiment, multiplayer isolation and maintenance cost. No educational or mental-health efficacy is claimed.

## Claim ledger

Confidence applies to the stated claim, not to the genre as a whole. Documentation observations are observations of published artifacts, not direct game observations. Recommendations not approved by Doug are `inference` or `hypothesis`, not `studio-decision`.

| Claim | Precise statement and classification | Support / locator | Confidence and reason | Limits / next discriminator |
|---|---|---|---|---|
| C-01 | **`inference`** — State preservation, learning and willingness to experiment are separate outcomes of a proposed branch. | Reviewed F01 learning/transfer and F07 evaluation distinctions; original scope. | Moderate for measurement separation. | None of the three outcomes was measured here. |
| C-02 | **`practitioner-heuristic`** — Wube reports historical undo coverage omissions and uncertainty about distant undo targets. | GDR-SRC-20261010-G13-012, “Undo information and confirmation”/“Undo Improvements”. | Moderate: concrete firsthand account, no dataset. | The reported preview is not a tested universal recovery system; internal tests not independent evidence. |
| C-03 | **`observed-example`** — Minecraft documents a copied existing world for the specified Bedrock experimental-feature workflow. | GDR-SRC-20261010-G13-014, Windows → Bedrock Edition and opening warning. | High for the published artifact, narrow scope. | No runtime test; development preview is not gameplay rollback. Source 013 is inaccessible lead-only and provides no recovery claim. |
| C-04 | **`hypothesis`** — An isolated experiment branch may support investigation without committing the declared original state. | C-02/C-03 as distinct precedents; original mechanism/settlement example. | Low: no direct player comparison of this complete pattern. | Only applies where isolation and advance experimentation fit the experience. |
| C-05 | **`inference`** — A truthful branch needs an explicit state boundary, lifecycle, identity, time and disposition contract. | C-02 recovery omissions; C-03 limited copy precedent; original logical requirements. | Moderate for prerequisites implied by the claim of isolation. | No technical implementation or proof of safety; external and shared effects may make the contract infeasible. |
| C-06 | **`inference`** — A trial supports the original decision only to the extent that relevant rules and conditions are preserved or disclosed. | Corrected F01-PAT-01 §Worked examples/§Playtest; original affordability contrast. | Moderate for logical scope, not demonstrated distant transfer. | Changed-rule demos must be announced; player preference is not correctness. |
| C-07 | **`hypothesis`** — Use simpler forecasts, local undo or fixed test scenarios when they answer the relevant question; preserve deliberate stakes. | Original comparison and do-not-use analysis; reviewed F07-PAT-02 counterexamples. | Low for comparative benefit and preferred sequence. | No universal obligation to offer undo or eliminate consequences. |
| C-08 | **`inference`** — Recovery does not erase knowledge or grant authority over external/shared effects; labels and access routes need testing. | Reviewed P01-TOP-03 process and F07-PAT-02 context; original boundary analysis. | Moderate for limits; no population effect or legal conclusion. | A restored file alone cannot establish a restored experience or shared-world permission. |
| C-09 | **`hypothesis`** — Fidelity, comprehension, rule prediction and experience fit require separate falsifying evaluations. | Corrected F01-PAT-01; F07-TOP-01 §Playtest; original proposed protocols. | Moderate for test logic; protocol not validated. | No actual software tests or participant tests; no sample-size or efficacy guarantee. |
| C-10 | **`hypothesis`** — Isolation and return-to-origin may justify a pattern distinct from supported transfer and safe exit. | Inspected F01-PAT-01 and F07-PAT-02; original novelty statement. | Low: latest canonical/pending inventory not available. | Proposed Foundations owner and novelty must be checked centrally; no canonical allocation. |

## References

Access date for every record: **2026-10-10 America/Los_Angeles / 2026-10-11 UTC**. Rights: copyrighted source text remains with its owner; only brief paraphrases and bibliographic metadata are included. No screenshots, videos or source-page copies are redistributed. Source IDs are temporary G13 identities; canonical URL/edition deduplication remains pending.

### GDR-SRC-20261010-G13-012

**StrangePan and Lou / Wube Software; relevant undo sections by StrangePan. Friday Facts #412 — Undo/Redo improvements & Car Latency driving.** Publication/update: 2024-05-24. Publisher: the organization named above (Steam hosts source 005). [Source](https://www.factorio.com/blog/post/fff-412).

**Edition/build:** Historical Factorio 2.0 development preview; actual released implementation not reproduced. **Access:** `relevant-excerpt`. **Inspection route:** Public primary HTML text inspected through web retrieval. **Type:** Firsthand developer account including reported internal playtesting.

**Exact locator:** “Undo information and confirmation”; “Undo Improvements”; “Conclusion”; retrieved text lines 33–82. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Reports old undo omissions and proposed improvements. Methods/participants absent; no measured effect size and no guarantee that all game state is reversible. Embedded videos not viewed. **Independence/provenance:** Independent developer from Mojang; different operation semantics, not a replication of the same recovery design.

### GDR-SRC-20261010-G13-013

**Mojang / Minecraft Help (attribution from indexed lead). Restore or Recreate a Minecraft: Bedrock Edition World.** Publication/update: unknown. Publisher: the organization named above (Steam hosts source 005). [Source](https://help.minecraft.net/hc/en-us/articles/43622310316045).

**Edition/build:** Help article indexed in search; no article-body inspection. **Access:** `lead-only`. **Inspection route:** Search lead found; two opens returned only the site shell, not the article body. **Type:** Official help lead.

**Exact locator:** No usable body locator: opening returned navigation/footer only. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Search-result text is not inspected support. No claims about restoration or seed recreation rely on this source. **Independence/provenance:** Same product family as 009/014. A separate article, not independent evidence.

### GDR-SRC-20261010-G13-014

**Staff / Mojang Studios. Testing New Minecraft Features.** Publication/update: 2022-10-14 (displayed); later revisions unknown. Publisher: the organization named above (Steam hosts source 005). [Source](https://www.minecraft.net/en-us/article/testing-new-minecraft-features).

**Edition/build:** Version-testing guide as retrieved; Windows Bedrock subsection; no game build used. **Access:** `relevant-excerpt`. **Inspection route:** Public primary HTML text inspected through web retrieval. **Type:** Creator technical documentation.

**Exact locator:** Opening instability/corruption warning, lines 513–525; Windows 10 & 11 → Bedrock Edition, lines 557–563. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Documents a copy of an existing world when experimental features are enabled in the described route. This is not proof of a general gameplay undo/rollback feature or validation of the proposed branch pattern. **Independence/provenance:** Same product family as 009/013. Preview/testing context differs from ordinary gameplay.


## Review and history

2026-10-10, `initial-capture-1`: initial complete author draft for G13. Version remains `0.1.0`; predecessor/supersession are null, not a claim that a canonical registry was searched exhaustively. Author self-review is in the [G13 packet](../reviews/full-run-20261010-g13-review-packet.md#author-self-review). Independent review has not occurred for this candidate. No participant tests, executable game observations, implementation, release or adoption occurred.

Exact bytes are recorded outside this file in the [integrity receipt](../reviews/full-run-20261010-g13-integrity-receipt.md). Existing upstream IDs, revisions and source meanings remain unchanged. This draft adds no permanent IDs and does not supersede a reviewed dependency.
