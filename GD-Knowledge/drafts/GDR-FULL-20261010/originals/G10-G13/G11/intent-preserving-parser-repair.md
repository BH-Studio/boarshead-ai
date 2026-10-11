---
id: GDR-CAND-20261010-G11-PAT-01
kind: pattern
title: Intent-preserving parser repair
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
- bounded command repair
- clarify before committing
tags:
- input-repair
- text-input
- ambiguity
- recoverability
- hypothesis
related_topics:
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-G11-PAT-02
- GDR-CAND-20261010-W02-PAT-01
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G11-GEN-01
- GDR-CAND-20261010-G11-GEN-02
source_ids:
- GDR-SRC-20261010-G11-002
- GDR-SRC-20261010-G11-004
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G11
predecessor_sha256: null
supersedes: null
change_summary: Initial G11 candidate; no earlier batch resent, source replaced, or canonical identity allocated.
byte_hash_record: ../reviews/full-run-20261010-g11-review-packet.md#candidate-byte-receipt
---

# Intent-preserving parser repair

**Conditional pattern candidate; effectiveness unvalidated.** Repair the expression of a supported action without silently changing which action the player asked to perform. This is a recognition-and-clarification technique, not an unrestricted natural-language interface or a general puzzle-hint system. [C-03, C-04]

## Purpose

The intended problem is a player having a supported intention but being blocked by wording, reference ambiguity or an unhelpful rejection. The intended benefit is more accurate recognition and recovery with fewer unintended commitments. That benefit is a hypothesis. The narrower consistency requirement is inspectable: the system should not resolve uncertainty by carrying out a different intention without a new player choice. [C-03, C-04]

This pattern can apply to parser fiction, text-command adventure interfaces or another bounded action vocabulary. It does not require a particular engine or genre. Apply it to a VN only where the hybrid actually accepts such input; ordinary dialogue choice-to-performance consistency belongs to the existing `GDR-CAND-20261010-W02-PAT-01`. [C-03]

## Context and prerequisites

The design needs an identifiable set of supported actions, current referents and knowledge boundaries. It must be possible to distinguish **recognition**, **clarification**, **feasibility**, **commitment** and **consequence**. Those are conceptual responsibilities, not a mandated code architecture. If an input cannot be interpreted without inventing an intention, do not claim to have repaired it. [C-03, C-05]

Establish whether exact wording is an intended challenge. Establish whether an unsuccessful input or clarification consumes fictional time, expends a resource, or commits a response. The default proposal here is not to mutate the fiction while resolving recognition ambiguity; a deliberately costly communication system needs an explicit alternate contract and different tests. [C-04, C-05]

The team also needs a way to review target-language phrasings and reproduce relevant states. A long synonym list in one language is not evidence that ambiguity is solved in another. Assistance must not disclose a hidden object, a secret action or the correct interpretation merely because the player happened to type a related word. [C-05]

## Mechanism and evidence

| Proposed causal link | Evidence actually available | What remains unproven |
|---|---|---|
| Distinguishing recognition/error categories enables a more specific authored response. | Inform documents grammar, mistake handling and parser-error distinctions. [C-01] | A particular application’s classifier can still misidentify the issue. Documentation was not executed here. |
| Clarifying an ambiguous referent before commitment avoids committing to an unchosen referent. | This follows from the stated contract, provided no commitment happens before the clarification. [C-03] | Whether the additional question improves experience, or whether its alternatives leak information. |
| A narrowly relevant repair reduces unintended input burden. | Plausible application of contextual error handling; Dreamhold’s help illustrates separate assistance routes. [C-02, C-04] | The size or existence of a benefit for actual participants, languages or access needs. |
| Accurate recognition helps the player form a correct model. | A testable proposal, not a consequence guaranteed by acceptance. [C-04, C-07] | Players may memorize a phrase, guess successfully, or misunderstand a rule. |

No link establishes enjoyment, immersion, general language understanding, or a universal reduction in difficulty. A repair can succeed operationally while harming a work whose central activity is discovering the right words. [C-05]

## Recipe

1. **Name the supported intention.** For the chosen interaction, record action, target, any second referent, relevant state and what would count as commitment. Also record what the design intentionally does not support. Exit if there is no stable action interpretation to preserve. [C-03]
2. **Separate the failure classes.** Distinguish unknown action wording, unclear referent, incomplete supported command, unavailable referent, unsupported intention and an understood-but-currently-impossible action. Do not tell the player that grammar failed when the action was understood but prohibited by the world. [C-01, C-03]
3. **Audit disclosure before suggesting repair.** Limit suggested referents and actions to what the current information contract permits. An error handler should not become an oracle for concealed people or objects. Exit to neutral help when a precise diagnosis would reveal the secret. [C-05]
4. **Choose the least committing repair.** Accept a known equivalent phrase when its meaning is genuinely the same. Ask a bounded referent question when it is not unique. Offer syntax guidance when the intention is incomplete. Explain the actual limitation when the action is unsupported. Never replace “destroy” with “give” because only the latter is implemented. [C-03, C-04]
5. **Make clarification reversible.** Allow the player to cancel, reformulate or choose a visible referent. Keep the original request available as needed for context without exposing private logs. Define explicitly whether fictional time is paused; do not hide costs behind the word “help.” [C-04, C-06]
6. **Commit only the resolved action.** Restate the relevant object or action in the resulting response where needed to identify what happened. Then apply the normal world rule. Recognition success should not silently bypass a prerequisite or guarantee fictional success. [C-03]
7. **Probe both false negatives and false positives.** Test legitimate alternative phrasings, ambiguous formulations, nearby different intentions, out-of-scope referents and changed situations. Include both cases where the same rule permits action and cases where it does not. Keep access accommodations in place. [C-07]
8. **Keep, narrow or omit.** Keep the repair only if it preserves intention and information boundaries. Revise recurring misclassification; replace with an explicit action menu when action formulation is not the desired task; omit semantic repair when exact language is the challenge. Reopen the review when the action set or a localization changes. [C-05, C-08]

### Adjustable variables and exit conditions

| Variable | Local decision | Exit or simplify when… |
|---|---|---|
| Action vocabulary and equivalent expressions | Which forms have the same supported meaning in this locale? | Coverage expands faster than the team can verify semantic distinctions. |
| Clarification granularity | Ask for the missing referent, action detail or intended target. | The prompt would reveal a secret or choose the intention itself. |
| Assistance visibility | Always visible syntax help, contextual prompt or optional deeper guidance. | Assistance hides essential controls or converts the intended inference into a solution disclosure. |
| Time/resource policy | Clarification-freeze, explicit cost, or another declared model. | The UI cannot keep the declared commitment boundary. |
| Wording and character voice | Neutral diagnosis or an in-fiction response that still identifies the issue. | Humorous refusal makes the player unable to distinguish unsupported wording from impossible action. |
| Recovery | Cancel, revise, history, or separately authorized undo. | A failed clarification cannot return to a safe comprehensible state. |

No default count of retries, synonym coverage, word length or response time is claimed. These settings must follow the intended task and testing context. [C-04, C-05]

## Worked examples

### Illustrative: two parcels and an irreversible handover

**Invented example, not a game observation or performed test.** A counter displays a sealed parcel and an open parcel. A clerk accepts one delivery. The intended decision is which parcel to send; the action vocabulary is not a word puzzle. [C-08]

The player enters “send the parcel.” The proposed repair asks whether they mean the sealed or open parcel and offers cancellation. It does not hand over the first object found by an internal ordering rule. Selecting the open parcel resolves the referent; the resulting acknowledgment identifies that parcel. Only then is the transfer recorded. If the player cancels, neither parcel moves. These are expected requirements, not observed results. [C-03, C-08]

The phrase “mail the open parcel” may be accepted as equivalent only after the local author confirms that mailing and handing to this clerk have the same intended outcome in the scene. “Open the sealed parcel” is a different intention and must not be accepted as a delivery. A later scene with a damaged parcel should test feasibility independently: the action may be understood but declined by the clerk. A helper that turns the parcel into an acceptable one has gone beyond repair. [C-03, C-07, C-08]

The new scene is a valid transfer probe only if the acceptance rule has not secretly changed. Include an acceptable parcel and a rejected one, and ask for the predicted outcome. A participant who thinks “all actions using the word parcel fail” should be distinguishable from one who understands the actual restriction. This preserves the reviewed F01 correction rather than equating repeated rejection with understanding. [C-07]

### Illustrative: a deliberately constrained language

A ritual puzzle requires constructing a phrase with a particular grammatical relation. Automatically converting any approximate request into the valid form removes the activity. A command guide may explain how to enter text or inspect already-known words, but should not supply the relation being investigated. Here the exit condition is triggered: do not use semantic repair for the puzzle’s defining phrase. [C-05, C-08]

### Source-artifact precedents

The inspected Inform examples demonstrate contextual handling rather than proving this complete recipe. The Dreamhold help shows that assistance and world actions can be documented separately. Neither source is presented as a measured before/after evaluation of the proposed parcel interaction. [C-01, C-02]

## Tradeoffs and alternatives

A finite visible action menu avoids some wording problems but changes the activity from proposing an action to recognizing an option. A broader grammar preserves more formulation freedom but requires verification of equivalent and non-equivalent cases. A neutral failure message preserves hidden information but may leave an avoidable burden. An optional hint can help at the content level, but it is not a substitute for making the interface operable. These are conditional alternatives, not a ranking proven by comparative trials. [C-04, C-05]

The main production cost is maintaining the distinction the repair claims to preserve across objects, states and locales. The pattern makes that obligation explicit; it does not claim a net cost saving. Shared dialogue intent contracts become relevant after the action has been selected, while shared reconvergence governs what later consequences must retain. [C-03]

## Failure cases and warning signs

| Failure | Warning sign in a proposed review | Correction to consider |
|---|---|---|
| Silent intention substitution | Player says the system acted on a different object or performed a different verb. | Clarify or reject; do not treat acceptance rate as success. |
| Secret leakage | An error names an unencountered object or implies the correct solution. | Reduce diagnostic specificity within the knowledge contract. |
| State mutation during clarification | A question spends a turn, gives away an item or records a moral choice unexpectedly. | Move the commitment boundary or disclose and test the alternate rule. |
| Vocabulary blame for a world restriction | Players keep rewriting a well-understood action that is impossible in this state. | Explain the relevant feasibility boundary without revealing hidden information. |
| Repair prevents learning the rule | Players repeat a corrected phrase but cannot predict a valid nearby case. | Change the feedback and transfer probe; keep accommodations. |
| Characterful error obscures diagnosis | Humor is read as evidence that an object is important or that the action nearly worked. | Preserve the voice only where the diagnostic meaning remains usable. |

These are predicted failure modes to look for, not failures measured in a local build. [C-04–C-08]

## Counterexamples and do-not-use conditions

Do not use automatic semantic repair where exact wording is the skill being tested, where the author cannot determine the requested intention, where a suggestion discloses protected fictional knowledge, or where a repair would replace a deliberate player refusal. Do not call an unbounded generated response an instance of this pattern without a separately verified action/commitment contract. Deliberate fictional misinterpretation may be authored as an event, but it must not be confused with claiming the interface correctly executed the player’s request. [C-05]

## Proposed playtest and falsification

**Not performed.** Compare a baseline rejection with the bounded repair on equivalent scenes, keeping supported actions and narrative stakes comparable. Recruit relevant parser experience levels and target input/language/access contexts. Counterbalance scene order and do not remove needed access support to manufacture a control condition. Choose the local practical-benefit criterion and recruitment rationale before collecting data. [C-07, C-08]

Measure intended versus committed action, ambiguity resolution, false-positive substitution, hidden-information leakage, correction effort, rule prediction, narrative attention and preference separately. Record the participant’s intended action before interpreting a failed input; otherwise the evaluator risks labeling its own guess as the truth. Consent and minimal retention are required for free-text logs. [C-06, C-08]

Reject or narrow the recommendation if repair increases completed actions by performing actions participants did not intend, gives away a required inference, or produces worse rule discrimination. Prefer an explicit menu if it preserves the intended activity with less burden. A repeated successful command alone does not certify transfer; include a new valid case and a nearby invalid case governed by the same rule. No numerical success threshold or universal sample size is supplied. [C-07, C-08]

## Claim ledger

Claim IDs are local to this artifact. Confidence describes the stated claim, not approval or universal applicability. Proposed application claims remain untested.

| Claim | Material claim | Class | Support and precise locator | Confidence and limit / unresolved question |
|---|---|---|---|---|
| C-01 | Inform provides documented grammar and error/mistake distinctions usable as design precedents. | observed-example | GDR-SRC-20261010-G11-002, §§17.1, 17.21, 18.35 | High for document content; no compiler/runtime or outcome test. |
| C-02 | A creator help artifact separates assistance and system controls from fictional actions. | observed-example | GDR-SRC-20261010-G11-004, Commands, System Commands, Special Commands | High for artifact; behavior and effectiveness unknown. |
| C-03 | Resolving reference uncertainty before commitment preserves the chosen action only if meaning and state boundaries are honored. | inference | C-01; recipe steps 1–6; reviewed D-06 distinction from accepted dialogue intent | Moderate for conditional logic; ambiguous semantic equivalence must be locally verified. |
| C-04 | Bounded contextual repair may reduce unintended effort while improving accurate recognition. | hypothesis | C-01–03; mechanism table and proposed playtest | Low for player benefit; no comparative trial of this recipe. |
| C-05 | Exact-word challenges, unknown intentions and secret-leaking repairs are stop conditions, not merely tuning issues. | hypothesis | Author’s constrained-language counterexample and information-contract analysis; reviewed D-08 | Moderate as scope reasoning; artistic and access tradeoffs require local review. |
| C-06 | Clarification and input research need explicit time, privacy and recovery policies. | hypothesis | Author-proposed recipe step 5 and study safeguards | Low for effect claims; no legal or ethics-board approval asserted. |
| C-07 | Test same-rule valid and invalid transfer cases and retain accommodations rather than certify repeated response. | inference | Reviewed D-05, corrected recipe/examples lines 77–123 | Moderate for diagnostic logic; no G11 learning result. |
| C-08 | The parcel and ritual examples and falsification rules are proposed applications only. | hypothesis | Worked examples; playtest section | Low; illustrative, not implemented or tested. |

## References

Access date for every record below: **2026-10-10**. “Observed example” refers to an inspected document or source artifact unless explicitly stated otherwise; no game executable was run. Source identities are temporary; global deduplication and permanent allocation remain pending.

### GDR-SRC-20261010-G11-002
**Graham Nelson / Inform documentation project. Writing with Inform.** Publication/update: unknown. Publisher: Inform documentation project.
**URL:** [Writing with Inform](https://ganelson.github.io/inform-website/book/WI_17_1.html). [§17.21](https://ganelson.github.io/inform-website/book/WI_17_21.html); [§18.35](https://ganelson.github.io/inform-website/book/WI_18_35.html).
**Edition/build:** Author-hosted HTML edition; exact release/commit not stated in inspected pages. **Locator:** §17.1 Understand, including Xylan; §17.21 Understanding mistakes, including Query and Hot Glass Looks Like Cold Glass; §18.35 Printing a parser error, including WXPQ.
**Access:** `relevant-excerpt`. **Type:** Official authoring manual and worked source artifacts. **Limits/independence:** Grammar examples inspected as text, not compiled. Contextual repair does not establish multilingual natural-language understanding or player benefit. Sections belong to one manual, not independent corroboration.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-004
**Andrew Plotkin. The Dreamhold — Help.** Publication/update: unknown. Publisher: Author’s website.
**URL:** [The Dreamhold — Help](https://eblong.com/zarf/zweb/dreamhold/help.html).
**Edition/build:** Web help; game release/build/platform behavior not verified. **Locator:** Basics; Commands; System Commands; Special Commands; Strategy.
**Access:** `relevant-excerpt`. **Type:** Creator-written instructions for a named game. **Limits/independence:** Documentation only; no game play, transcript capture, or measured outcome. Save/restore/undo and hints describe different controls, not an automatic accessibility certification.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

## Related entries and history

Applies conditionally to [Interactive fiction](../genres/interactive-fiction.md), `GDR-CAND-20261010-G11-GEN-01`, and only to free-form-input hybrids of [Visual novel](../genres/visual-novel.md), `GDR-CAND-20261010-G11-GEN-02`. Complementary: [State-safe narrative rereading](state-safe-narrative-rereading.md), `GDR-CAND-20261010-G11-PAT-02`.

Existing inspected dependencies: `GDR-CAND-20261010-W02-PAT-01` (accepted intention to response), `GDR-CAND-20261010-F01-PAT-01` (corrected transfer discrimination), and `GDR-CAND-20261010-F02-TOP-01` (information contract). Their bytes and locators are in the [review packet](../reviews/full-run-20261010-g11-review-packet.md#reviewed-dependencies); they are not reissued. Local conflicts G11-CON-02 and G11-CON-05 remain open.

Version 0.1.0, initial-draft-1, no predecessor. Reviewer and approval fields remain null. No independent G11 review or player test occurred. Exact SHA-256 is recorded externally in the packet. Cross-domain pattern ownership is proposed for coordination, not reassigned by this draft.
