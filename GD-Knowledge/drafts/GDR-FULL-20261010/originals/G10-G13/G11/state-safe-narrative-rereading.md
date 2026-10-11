---
id: GDR-CAND-20261010-G11-PAT-02
kind: pattern
title: State-safe narrative rereading
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_key: G11
attempt_identity: G11-authoring-attempt-01
identity_scope: temporary run-scoped candidate; permanent allocation pending
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_state: open
input_snapshot: Supplied G11 brief + starter files + inspected selected waves 1–2 dependency excerpts
aliases:
- history versus rollback
- read-only narrative return
- replay state contract
tags:
- rereading
- state-integrity
- reader-control
- replay
- hypothesis
related_topics:
- GDR-CAND-20261010-W01-TOP-01
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-G11-PAT-01
- GDR-CAND-20261010-W01-PAT-01
- GDR-CAND-20261010-W02-PAT-01
related_genres:
- GDR-CAND-20261010-G11-GEN-01
- GDR-CAND-20261010-G11-GEN-02
source_ids:
- GDR-SRC-20261010-G11-007
- GDR-SRC-20261010-G11-008
- GDR-SRC-20261010-G11-009
- GDR-SRC-20261010-G11-010
- GDR-SRC-20261010-G11-011
- GDR-SRC-20261010-G11-013
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G11
predecessor_sha256: null
supersedes: null
change_summary: Initial G11 candidate; no earlier batch resent, source replaced, or canonical identity allocated.
byte_hash_record: ../reviews/full-run-20261010-g11-review-packet.md#candidate-byte-receipt
---

# State-safe narrative rereading

**Conditional pattern candidate; effectiveness unvalidated.** Define what returning to previously encountered narrative material does—and does not—change. Preserve the chosen contract across history, replay, choice revision, persistent records and localization. The pattern does not require an engine, a branching plot or a universal right to reverse fictional consequences. [C-05, C-06]

## Purpose

The intended problem is a reader using a return control to understand a passage but accidentally changing story state, or believing a decision was undone when only earlier text was shown. The intended benefit is recoverability with accurate state expectations. That benefit requires testing; “state-safe” names the design goal, not a certification of a proposed implementation. [C-05, C-06]

This is reusable for a VN backlog, a text-fiction transcript, narrative scene replay, or another authored experience where previous material can be revisited. It is not a full save-system architecture, platform synchronization design, or replacement for the shared narrative-state owner. [C-05]

## Context and prerequisites

First identify why the return is needed: recover lost place, check an earlier statement, hear a performance again, revise a commitment, or inspect an alternate traversal. These are different tasks. The design must be able to describe the difference between current fictional state, reading position, encounter history and cross-play records. A name such as “Back” does not establish that distinction. [C-01, C-02, C-05]

The author needs a stable identity for the material being revisited and enough context to select the intended variant. “The same words appeared” is not sufficient when speaker, route, language, performance or relevant knowledge differs. A simple text-only history may be appropriate precisely because the team cannot faithfully reproduce an earlier performed scene. State that limitation instead of presenting it as full replay. [C-04, C-07]

Exit before offering choice revision if the project cannot restore or reconstruct the states it promises to change. Exit before offering isolated replay if replay effects cannot be separated from current play. A read-only record is a legitimate simpler outcome, not a failed version of unrestricted rollback. [C-05, C-08]

## Mechanism and evidence

| Link | Support | Evidence limit |
|---|---|---|
| Different return operations can have different state scopes. | Ren’Py separately documents history, rollback and persistent records. [C-01, C-02] | Facility descriptions do not validate a particular game’s state model. |
| Naming an operation by its scope can support a more accurate expectation. | Inference from the difference between viewing and changing; proposed labels and tests below. [C-05, C-06] | The wording may be misunderstood; no label experiment was performed. |
| Keeping review-only traversal from reapplying effects prevents a class of continuity errors. | Conditional consistency reasoning: a read-only contract is violated by an undisclosed write. [C-05] | Actual state isolation and compatibility must be verified in the eventual implementation. |
| Revisit and skip policies can preserve relevant new context. | Author’s contextual-change analysis plus documented history, voice and translation facilities. [C-03, C-04, C-07] | Seeing, comprehending and valuing material remain distinct; no evidence proves a universal contextual novelty detector. |
| Better state understanding improves the reading experience. | Hypothesis, not an automatic consequence of technical correctness. [C-06] | More explicit controls can burden or spoil an intentionally uncertain experience. |

The recipe combines capability precedents with new application reasoning. It is not a measured result of the Ren’Py project or a validated property of all narrative engines. [C-06]

## Recipe

1. **Choose the task and operation.** Write a plain-language contract for the return feature before selecting a UI control: view prior material, replay performance, change a prior choice, revisit under locked choices, or start an alternate context. Do not combine these under one ambiguous action without explaining the transition. [C-05]
2. **Declare the state scopes.** Identify current-story values, reading/history records, presentation settings, and cross-play unlocks or knowledge. For each, specify whether the operation reads, changes, restores, preserves or ignores it. Mark any intentionally irreversible or external effect. This is a conceptual review, not implementation code. [C-02, C-05]
3. **Bind content to its relevant context.** Identify the passage or scene variant, speaker, route-relevant facts, locale and necessary performance association. Store or reconstruct only what is justified by the task; do not expose a future branch’s facts through a summary. [C-04, C-07]
4. **Control side effects and re-entry.** Require review-only operations to leave the current-fiction commitment unchanged. For a changeable return, define the point to which the fiction is restored and what remains persistent. For replay, state whether it is isolated or part of current play. Exit to a simpler record when those promises cannot be honored. [C-05, C-08]
5. **Separate access from automatic progression.** Make return, resume, voice replay and skip behavior understandable through the supported input/access routes. A preference for fast text is not permission to select a default narrative response. Do not silently start automated advancement when the user only requested a past line. [C-03, C-06]
6. **Review repeated material for changed meaning.** Decide whether skip policy uses exact content identity, route context, explicit reader marking, or another locally justified rule. Identify its false positives: newly meaningful material labeled old. Never label a system’s encounter flag “the player understood.” [C-07]
7. **Test transitions and variants.** Include interruption, language change, alternate route, altered performance, current versus persistent state, and custom-screen behavior where relevant. Check both the intended state transition and the reader’s prediction of it. Preserve the distinction between those checks and preference. [C-04, C-09]
8. **Keep the smallest reliable contract.** Retain the operation only when its stated boundaries can be verified and readers can use it appropriately. Narrow to a transcript or chapter boundary when precise return cannot be supported. Reopen review when state logic, script identifiers, localization or save compatibility changes. [C-08, C-09]

### Operation contract matrix — illustrative, not an engine specification

| Operation | Current fiction | Reading position | Cross-play records | Crucial label or limit |
|---|---|---|---|---|
| History-only view | Proposed: unchanged. | Inspect earlier encountered material, then resume. | Proposed: unchanged. | “Review conversation”; not “undo.” |
| Voice replay of an encountered line | Proposed: unchanged. | Retain the current reading position. | Proposed: unchanged. | Make the line/context identifiable; do not imply scene restoration. |
| Changeable return | Restore to a declared point before a commitment. | Resume from that point. | Explicit policy; not automatically reset. | State which decision can change and what cannot. |
| Locked-choice rereading | Follow the prior committed path. | Revisit then return or continue as declared. | Explicit policy. | Clearly distinguish reading backward from choosing differently. |
| Isolated scene replay | Proposed: no effect on current play. | Enter a specified reconstruction and exit. | Explicit unlock/read policy. | Warn when the recreation omits context or uses a default variant. |
| New route or fresh traversal | A separately declared context, not a partial rollback. | Start at the defined entry point. | May retain unlocks only by explicit design. | “New route” is not the same as restoring a save. |

The defaults in this matrix are proposed local contracts, not asserted native behavior of any engine. [C-05, C-08]

### Adjustable variables

Choose the granularity of return, history retention, variant identification, persistent-state policy, spoiler exposure, skip criteria, voice behavior, available input routes and the point at which the reader resumes. All are task-dependent. No route count, retention length, text rate, debounce interval or universal persistence policy is prescribed. [C-06–C-09]

## Worked examples

### Illustrative: the letter and the response

**Invented design example; no implementation or participant test.** A protagonist gives a sealed letter to a friend, then later learns that its address was incomplete. The reader wants to revisit the handover conversation. The current story records the handover; the history records the words encountered; a cross-play gallery records that the illustration has been unlocked. [C-08]

The proposed **Review conversation** control displays only that conversation from this traversal and preserves the present handover state. **Change this decision**, where offered, restores a declared point before the handover and explains that the gallery illustration remains unlocked across plays. **Replay scene** is not exposed unless the team can reconstruct the chosen scene without reapplying the handover or revealing another route. [C-05, C-08]

A test should ask what changes before the reader uses each control. Then compare the actual state with the declared contract. If a reader thinks opening history returned the letter, the interface failed even if the story data remained intact. If the history control gives the letter back, the state contract failed even if the reader preferred the surprise. These are two different failure classes. [C-06, C-09]

### Illustrative: repeated words with new knowledge

A later route repeats a phrase from an earlier meeting, but the reader has now encountered a different fact that makes the phrase suspicious. A skip policy based only on previous display can bypass the intended reinterpretation. The proposed solution is not to forbid all skipping; it is to decide what identifies a new interpretation-bearing scene and to let the reader recover when the policy is wrong. A simple “skip nothing in this section” policy may be cheaper and more reliable than a complex novelty model, but its repetition cost must be tested. [C-07, C-08]

### Documented precedent versus new recipe

History entries, rollback controls, persistent data and preference settings in the inspected documentation provide separate technical precedents. They do not prove that this letter example, its isolation policy or its contextual skip rule works. Translation and voice association also require rechecking against the exact runtime/version before implementation. [C-01–C-04]

## Tradeoffs and alternatives

A transcript is cheaper in scope than a full scene reconstruction but can omit important staging. A chapter return reduces fine-grained restoration obligations but may repeat unwanted material. Locked-choice rereading can protect a commitment while still allowing review, but its distinction from ordinary rollback must be understandable. A new route can make comparison explicit but may impose repetition or spoilers. These are conditional comparisons to investigate, not measured cost ratios or universal player preferences. [C-05–C-08]

This pattern can conflict with an intended uncertain narrative state. Avoid exposing a complete hidden-state ledger to the reader merely to make internal behavior easy to debug. The required clarity is the **control’s scope**, not necessarily the truth of every fictional claim. It can also conflict with continuous simulation: a history panel might intentionally leave the world running. Such a design needs an explicit alternate timing contract rather than being silently treated as the read-only-paused illustration. [C-05, C-08]

## Failure cases

| Failure | Observable warning sign to seek | Conditional correction |
|---|---|---|
| Side effects repeat | Reviewing a line advances a day, duplicates an item or changes a relationship. | Isolate review or remove the feature until its contract can be guaranteed. |
| Partial undo | A visible choice resets but its later consequences remain without explanation. | Restore the declared scope or offer a clearly read-only return instead. |
| Persistent knowledge leaks | The current protagonist uses information from another route unintentionally. | Separate reader history, protagonist knowledge and intended cross-route mechanics. |
| Performance variant mismatch | History or voice replay uses another route’s delivery. | Bind the right context or disclose a limited text record. |
| Translation re-entry error | Switching language changes story facts or selects unrelated content. | Review language-change behavior and identifiers for the exact build. |
| False skip | New context is suppressed because a line was marked encountered. | Narrow the skip predicate or use reader-controlled marking and recovery. |
| Accurate system, wrong mental model | A reader expects reversal from a view-only control. | Relabel, demonstrate scope or separate controls; technical correctness alone is insufficient. |

These are predicted hazards, not bugs found in a tested project. [C-04–C-09]

## Counterexamples and do-not-use conditions

Do not offer an undo promise for irreversible external events that cannot be reversed. Do not reconstruct a past scene from current state and present it as the original without a justified context policy. Do not force detailed summaries that resolve a mystery whose task is interpretation. Do not assume a strictly paced work needs arbitrary mid-scene replay; an explicit, accessible limited return may better preserve its composition. These restrictions narrow the pattern rather than invalidate the value of rereading everywhere else. [C-05, C-08]

An intentionally unreliable narrator can misrepresent the fiction while the return control still behaves consistently. Conversely, a perfectly accurate transcript can be insufficient when visual staging carried required information. Keep narrative unreliability, presentation completeness and state integrity as separate review questions. [C-05, C-07]

## Proposed playtest and falsification

**Not performed.** Compare clearly named history-only, locked-choice rereading and changeable-return variants in matched scenes. Use interrupted and continuous reading, first and repeat traversal, and target language/input/access contexts. Counterbalance scenes; account for prior knowledge and spoilers. Do not claim that this design validates a particular engine’s serialization. [C-09]

Record predicted and actual state changes, unintended commitments, ability to resume, comprehension of relevant past information, access effort, perceived control and preference independently. Include an unchanged-context repeat and a changed-context repeat. Give the reader a reason to want each kind of return so that non-use is not mistaken for a bad control. [C-06, C-07, C-09]

Reject or narrow the technique when an operation changes a scope it promised to preserve, readers repeatedly confuse review with reversal, or the additional controls impose burden without helping the declared task. A preference for irreversibility does not by itself justify a confusing history control. A reduction in rereading time does not by itself prove better comprehension. Predefine the local practical margin and recruit on a justified basis; no numerical universal threshold is provided. [C-09]

## Claim ledger

Claim IDs are local to this artifact. Confidence describes the stated claim, not approval or universal applicability. Proposed application claims remain untested.

| Claim | Material claim | Class | Support and precise locator | Confidence and limit / unresolved question |
|---|---|---|---|---|
| C-01 | Ren’Py documents history and saved/rollback state as distinct facilities. | observed-example | GDR-SRC-20261010-G11-007 opening/HistoryEntry; GDR-SRC-20261010-G11-008 Saving and Loading, Rollback | High for the manual; runtime behavior in a project unverified. |
| C-02 | Persistent data has a scope distinct from a point in current play. | observed-example | GDR-SRC-20261010-G11-009 opening and examples | High for documentation; which facts persist is a project decision not made here. |
| C-03 | Text, skip, auto-forward and voice controls are separately documented facilities. | observed-example | GDR-SRC-20261010-G11-010 Preferences; GDR-SRC-20261010-G11-013 opening and replay functions | High for documented controls; exposure, compatibility and benefit untested. |
| C-04 | Translation and performance associations introduce context/re-entry obligations to inspect. | inference | GDR-SRC-20261010-G11-011 Translating Dialogue and language-change tips; GDR-SRC-20261010-G11-013 automatic/translated voice | Moderate for potential dependencies; no executed failure or universal behavior claimed. |
| C-05 | A return operation must be judged against its declared state scope rather than its label alone. | inference | C-01–04; operation matrix and stop conditions | Moderate for consistency reasoning; no implementation certification. |
| C-06 | Distinct scope contracts may improve accurate recovery and perceived control. | hypothesis | Mechanism table; C-05; proposed comparison | Low for effect; added controls may increase burden. |
| C-07 | Encounter history cannot establish comprehension or unchanged interpretive context. | inference | C-01; illustrative repeated-words case; reviewed D-01/D-03 knowledge and interpretation distinction | Moderate for logical non-equivalence; benefit of any novelty policy untested. |
| C-08 | The operation defaults, examples, alternatives and exclusions are proposed design contracts. | hypothesis | Recipe and illustrative letter/repeated-words cases | Low; no scene replay, state test or production estimate performed. |
| C-09 | Assess state integrity, reader prediction, comprehension and preference separately and reject scope violations. | hypothesis | Author-designed proposed playtest; reviewed D-05/D-08 discrimination principles | Low for efficacy; static consistency is necessary to the promise but not sufficient for enjoyment. |

## References

Access date for every record below: **2026-10-10**. “Observed example” refers to an inspected document or source artifact unless explicitly stated otherwise; no game executable was run. Source identities are temporary; global deduplication and permanent allocation remain pending.

### GDR-SRC-20261010-G11-007
**Ren'Py project. Dialogue History.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Dialogue History](https://www.renpy.org/doc/html/history.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening description; HistoryEntry fields; rollback_identifier.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** History entries and rollback references are distinct; a history pane is not a complete record of all audiovisual context. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-008
**Ren'Py project. Saving, Loading, and Rollback.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Saving, Loading, and Rollback](https://www.renpy.org/doc/html/save_load_rollback.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** What is Saved; Saving and Loading; Rollback; Blocking Rollback; Fixing Rollback.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Engine-specific state and custom-screen constraints. Vendor judgments about blocking rollback are practitioner advice, not an effect experiment. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-009
**Ren'Py project. Persistent Data.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Persistent Data](https://www.renpy.org/doc/html/persistent.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening distinction from data tied to a game point; persistent data example; merging discussion.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Cross-play persistence is not the same scope as a story save. No project reset policy or implementation verified. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-010
**Ren'Py project. Screen Actions, Values, and Functions.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Screen Actions, Values, and Functions](https://www.renpy.org/doc/html/screen_actions.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Preferences: text speed; skip; after choices; auto-forward; wait for voice.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Preference facilities are documented, not proof that a shipped UI exposes them or that a particular speed is effective. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-011
**Ren'Py project. Translation.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Translation](https://www.renpy.org/doc/html/translation.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Primary and Alternate Languages; Translating Dialogue; translation units; tips concerning language changes.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Text, interface, style and image facilities do not prove equivalent cultural interpretation. Identifier stability and replayed translation-block effects require project-specific review. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-013
**Ren'Py project. Voice.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Voice](https://www.renpy.org/doc/html/voice.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening voice statement behavior; voice tags; automatic voice; translated voice; voice replay functions.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Engine documentation, not audience evidence that voice improves comprehension or preference. Audio builds and delivery platforms untested. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

## Related entries and history

Genre adaptations: [Interactive fiction](../genres/interactive-fiction.md), `GDR-CAND-20261010-G11-GEN-01`; [Visual novel](../genres/visual-novel.md), `GDR-CAND-20261010-G11-GEN-02`. Complementary pattern: [Intent-preserving parser repair](intent-preserving-parser-repair.md), `GDR-CAND-20261010-G11-PAT-01`.

Inspected shared narrative, dialogue and accessibility excerpts are identified in the [review packet](../reviews/full-run-20261010-g11-review-packet.md#reviewed-dependencies). Reviewed dedicated session structure, localization/presentation and narrative systems interfaces were not supplied/inspected for transfer. Their owners should review this pattern’s boundary before adoption. Local conflicts G11-CON-03, G11-CON-04 and G11-CON-05 remain open.

Version 0.1.0, candidate_revision initial-draft-1; no predecessor. Null reviewer/approval fields are retained. Exact file hash is external in the review packet. No independent G11 review, implementation or player test was performed; local file checks do not pass Gate D as a whole.
