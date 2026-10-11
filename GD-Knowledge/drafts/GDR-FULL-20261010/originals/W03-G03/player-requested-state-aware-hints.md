---
id: GDR-CAND-20261010-G03-PAT-02
kind: pattern
title: Player-requested state-aware hints
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
predecessor_sha256: null
supersedes: null
change_summary: Initial G03 capture; no earlier G03 artifact superseded.
run_id: GDR-FULL-20261010
batch_id: G03
attempt_id: G03-attempt-01
identity_scope: run-scoped-temporary-candidate
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_timezone: America/Los_Angeles
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate + supplied G03 brief + inspected
  first-wave selected-draft excerpts
aliases:
- optional contextual hints
- request-scoped hints
tags:
- assistance
- discovery
- state-aware-help
- spoiler-control
- access
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-G03-PAT-01
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G03-GEN-01
- GDR-CAND-20261010-G03-GEN-02
- GDR-CAND-20261010-G03-GEN-03
source_ids:
- GDR-SRC-20261010-G03-007
- GDR-SRC-20261010-G03-004
- GDR-SRC-20261010-G03-006
- GDR-SRC-20261010-G03-011
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G03
hash_record: ../reviews/full-run-20261010-g03-review-packet.md#candidate-inventory
---

# Player-requested state-aware hints

**Hypothesis-led pattern candidate, not a validated hint algorithm.** The technique concerns optional, bounded help on the player’s current problem. It does not infer disability, certify learning, or require a fixed number of hint tiers.

## Purpose

Reduce the mismatch between the help a player requests and the information a system provides, while preserving the player’s chosen discovery boundaries. It is intended for situations where several goals or blockers can coexist and a generic answer may be irrelevant, premature or incorrect. The complete recipe has no direct efficacy evidence in G03. [C-01]

This is different from the inspected F01 Supported attempt and transfer check. The F01 candidate concerns guided practice and evidence of rule transfer; this pattern concerns requested relief from a present blockage. A player can appropriately use a direct answer without demonstrating learning. Do not turn help use into an assessment unless a separately stated purpose and method justify it. [C-07]

## Context and prerequisites

Use only where the design can represent the relevant current state with adequate confidence, present a help request through supported interfaces, and distinguish information already available from information that would reveal a solution. Multiple characters, alternative clue orders, localized text and older saves must be considered where they exist. [C-02; C-05]

The player must be able to request help **without already knowing the solution’s target object**. A general help entry point can offer active questions, a recap or an explicit choice of problem. It must not expose unseen goals merely by listing them. Input instructions, access to essential facts and other accommodations remain available independently of puzzle-hint preferences. [C-02; C-07]

**Exit condition:** if state is unreliable, the request cannot be understood sufficiently, or essential information is inaccessible, do not generate confidently specific advice. Offer a labeled general recap, clarify the request at a nonspoiling level, provide an explicit alternative route where designed, or defer the state-specific system until its prerequisites can be met. Do not claim that a guess is personalized certainty. [C-05]

## Mechanism and evidence

| Causal link proposed | What supports it | What remains unsupported |
| --- | --- | --- |
| Removing the need to target the unknown solution makes a help request possible in more blocked situations. | Gilbert describes rejecting a target-dependent hint interaction. [C-02; GDR-SRC-20261010-G03-007] | No controlled estimate of request success or frustration reduction. |
| Valid current state makes it possible to avoid already completed or unavailable steps. | The same account warns that missing old-save variables can produce inaccurate hints. [C-02] | State completeness and the G03 selection recipe are unverified. |
| Separating destinations/facts from solutions allows different disclosure choices. | Mobius discusses the relation between destination signaling and discovery. [C-03; GDR-SRC-20261010-G03-004] | In some games the destination itself is the discovery; no neutral tier is guaranteed. |
| Giving the player control over requested scope may better align help with preference. | A narrow assistance study distinguishes task performance and preferences; it does not test this recipe. [C-04; GDR-SRC-20261010-G03-006] | No claim of improved adventure satisfaction, learning or accessibility can be imported. |
| Correct scoped help improves progress without sacrificing valued discovery. | This is the complete pattern’s intended effect. [C-01; C-06] | **Low-confidence hypothesis.** Faster progress can coexist with spoilers, dependency or loss of agency. |

A bypass is a distinct alternative. Naughty Dog’s documented puzzle skip shows why reaching the next state must not be described as equivalent participation in the skipped reasoning. Nor does optional help by itself make every aspect of a game accessible. [C-08; GDR-SRC-20261010-G03-011]

## Recipe

1. **Separate access from answer assistance.** Identify whether the request concerns controls, perceiving information, recalling encountered facts, locating a next investigation, interpreting evidence, executing an action or obtaining the answer. Do not force players to disclose a diagnosis to get a usable interaction. An inaccessible required fact is not protected as a “spoiler” from the person entitled to it. [C-07]

2. **Identify the requested question without demanding its solution.** Provide a reachable help entry point. Use player-confirmed current goals or a nonspoiling clarification, not an omniscient list of all future puzzle nodes. Permit “I do not know what to investigate” as distinct from “I know the problem and want the answer.” [C-02; C-05]

3. **Validate the relevant state.** Check which prerequisites are completed, currently possible, already disclosed, consumed or blocked by another condition. Mark uncertainty from older saves, unsupported transitions or incomplete state history. If the state cannot be trusted, exit to a general, explicitly limited aid rather than issuing a false instruction. This is a conceptual requirement, not an implemented runtime check. [C-02; C-05]

4. **Define disclosure choices for that question.** Possible responses include an encountered-fact recap, a restated goal, a suggested place to investigate, a relationship between facts, a concrete action, or an explicit solution/bypass. These are options, not mandatory fixed tiers. Determine what each reveals relative to the player’s stated request; a location hint may already be the answer. [C-03; C-06]

5. **Let the player choose or consent to the next disclosure.** State the kind of help about to be given when that distinction matters. Avoid unsolicited escalation, artificial delays or rewards for remaining stuck. Do not require a player requesting the answer to labor through increasingly obvious riddles. The proposed policy is request-sensitive, not anti-direct-help. [C-06]

6. **Deliver a bounded, accessible response.** Explain the currently relevant step without claiming the player has encountered unseen facts. Preserve localized meaning and relevant uncertainty. A response should distinguish a knowledge problem from an authorization, resource, interface or execution problem; otherwise it can send the player searching for evidence that is not missing. [C-05; C-07]

7. **Revalidate before further help.** A prior response can change the player’s actions and the game state. Do not simply advance a counter to a more revealing line. Allow revisiting a previous response, requesting a different question, declining further help or explicitly choosing a solution. Never withdraw an access accommodation because the system assumes learning occurred. [C-05; C-07]

8. **Evaluate and revise the contract.** In a separately authorized study, compare requested scope with revealed content, correctness, progress and valued discovery. Remove or simplify the pattern if it routinely selects the wrong question, over-discloses, relies on fragile state inference or adds more friction than a straightforward help mode. Do not convert completion into a claim of learning. [C-06; C-09]

### Adjustable variables and decision points

| Variable | Local choices | Important limit |
| --- | --- | --- |
| Request channel | Menu, dialogue, journal, dedicated control or another supported interface | A diegetic channel is not automatically discoverable or accessible. |
| Goal selection | Player-named problem, confirmed active task, bounded clarification | Listing unknown objectives can itself spoil discovery. |
| State confidence | Verified state, partial history, unknown history | Unknown state requires a qualified fallback, not fabricated precision. |
| Disclosure | Recall, direction, relation, action, solution or bypass | No universal order, number of tiers or “safe” first hint. |
| Escalation | Explicit next request or selected assistance mode | Avoid unrequested answer leakage; no universal waiting timer. |
| Persistence | Re-readable help, separately marked encountered facts, current versus obsolete guidance | A saved hint can become stale after a different route succeeds. |
| Localization | Semantic equivalent or puzzle-specific adaptation | Literal translation may change clue strength or reveal the answer. |
| Evaluation | Requested scope, correctness, interpretation, effort, progress, spoilers and preference | Faster completion is insufficient evidence of benefit. |

## Worked example — illustrative, not an implemented system

**The interrupted signal station.** A player is trying to contact a mountain outpost. The current scene could be blocked by a power fault, an unaligned transmitter or an authorization code. The system must not assume that every request concerns the transmitter merely because it is the prominent object. These invented conditions illustrate the recipe. [C-10]

The player asks, “What am I missing?” A proposed help interaction first offers to clarify the current problem without listing undiscovered story outcomes. The player selects the already known goal of making contact. A conceptual state check indicates that power is restored and the transmitter is aligned, but the authorization has not been granted. A response about finding alignment markings would therefore be wrong even if it were a valid hint in another save. [C-05; C-10]

The player requests only a reminder. The response can restate the encountered instruction that the operator must approve contact, without revealing the operator’s private motive. If the player next requests the concrete next step, a response can identify the already introduced appointment or conversation condition. If that condition depends on an unseen clue, the response must label its disclosure rather than pretend it is remembered information. [C-06; C-07; C-10]

An older save lacks the record needed to distinguish “not authorized” from “authorization history unknown.” The state-aware path exits to a limited recap and communicates that it cannot reliably identify the remaining condition. The design might instead provide a deliberately authored state-repair or alternate progression policy, but that is a separate decision—not permission for the hint system to invent history. [C-05; C-10]

**Counterexample:** if discovering that authorization exists is the main mystery, even naming it would spoil the task. The initial clarification must then be less specific, or the player must explicitly request revelation of the hidden requirement. Conversely, a player who requests an explicit solution may find several rounds of vague guidance patronizing. Both cases challenge a fixed “gentle hint ladder.” [C-06; C-10]

## Tradeoffs and alternatives

State-aware help requires authored distinctions and maintenance across supported progression routes. A new puzzle solution or changed conversation can make a formerly correct hint obsolete. More detailed player-state tracking can also create privacy and production concerns if collected externally; this pattern requires no external player profiling or telemetry by default. [C-05; C-09]

Alternatives include a clear goal statement, better baseline feedback, a journal of encountered facts, optional explicit solutions, a selectable difficulty/access mode, human-authored general help, or removing a weak puzzle. A small linear activity may need only a direct help button, not a state model. A state-aware system should not compensate indefinitely for missing evidence or an incoherent gate. [C-06; C-07]

A designer can choose an intentionally unassisted mode, but should not equate it with inaccessible controls or deny basic required information. A skip can preserve continuity while changing the activity. Neither decision proves what all adventure audiences prefer. [C-07; C-08]

## Failure cases

| Failure | Future observable warning | Candidate correction |
| --- | --- | --- |
| Wrong inferred goal | Player requests help on access; response explains a puzzle they already solved. | Let the player confirm the question and distinguish blocker categories. |
| Stale or absent state | Hint refers to an unavailable object or completed step. | Revalidate, disclose uncertainty and use a bounded fallback. |
| Unwanted reveal | A “small nudge” discloses an unknown destination or relationship the player wanted to discover. | Classify disclosure relative to the task and request, not a fixed tier label. |
| Help is hard to request | Player must name or select the hidden solution object. | Use an independent entry point or nonspoiling goal-level request. |
| Access mistaken for answer dependence | Basic labels or alternative controls disappear as hints fade. | Separate persistent accommodations from answer-leading prompts. |
| Progress mistaken for understanding | The player copies a solution and is reported as having learned the rule. | Use a separate, discriminating assessment only when appropriate. |
| Localization changes hint strength | A translated clue names the answer directly or loses its logical relationship. | Review semantic function and test the adapted puzzle, not only string fit. |

These warnings and remedies are proposals, not reported frequencies or validated automatic detection rules. [C-05–C-07; C-09]

## Counterexamples and do not use conditions

Do not use a complex contextual system where a single known task and explicit help button would suffice. Do not rely on this pattern when state is unreliable, goal inference is inherently ambiguous, or the design cannot distinguish a clue from a solution. Do not use it to normalize deliberately obscure prerequisites, sell relief from frustration, or infer a player’s diagnosis. Do not claim that optional help guarantees comfort, access, learning or equivalent experience. [C-05–C-09]

Some experiences deliberately depend on discovering what the question is. Offering a menu of live hidden dependencies could defeat them. Other players intentionally seek unassisted interpretation. In both cases, maintain a clearly controlled disclosure boundary and allow no additional help; do not impose assistance merely because a timer elapsed. [C-06]

## Proposed playtest — NOT PERFORMED

**Question:** does player-confirmed, validated help better match the requested problem and disclosure boundary than a suitable simpler alternative, without increasing incorrect guidance or interaction burden? [C-09]

Compare a state-aware candidate with an appropriate authored alternative, such as requested general help or an explicit solution option. Use equivalent baseline access accommodations and the same substantive puzzle facts. Avoid forcing a knowingly inaccessible condition as control. Include more than one legitimate clue order, a return after interruption, and states with different blockers where applicable. Old-save technical compatibility is a separate build-specific test, not a simulated player outcome. [C-09]

Record what help was requested, the information actually revealed, whether it was correct in that state, the player’s next interpretation/action, unwanted spoilers, effort and perceived control. Progress and satisfaction should be separate outcomes. If rule learning is also a research question, use the corrected F01 technique with new cases requiring different answers and a prediction/action distinction; do not infer transfer from assisted completion. [C-07; C-09]

Relevant participants vary by puzzle familiarity, language, access needs, device and desire for explicit help. Confounds include prior solution knowledge, repeated puzzle exposure, unequal clue visibility and the fact that people self-select help at different kinds of blockage. A comparison of help users and nonusers alone cannot establish the effect of the aid. [C-09]

Reject or simplify when requests are repeatedly misinterpreted, hints are incorrect or stale, desired discoveries are exposed without consent, interaction burden outweighs relevance, or a simpler aid serves the same request. Narrow benefits to the populations and task measured. Define project-specific thresholds before data collection; no universal number of tiers, delay, sample size or acceptable spoiler rate is justified here. [C-09]

## Claim ledger

| ID | Claim | Class | Source and locator | Confidence and limit |
| --- | --- | --- | --- | --- |
| C-01 | Request-sensitive state-aware help may better align assistance with a current blockage and chosen discovery boundary. | hypothesis | Synthesis of C-02–C-04 with the limitations below. | Low; the complete recipe has not been evaluated. |
| C-02 | Gilbert reports a target-dependent help-design problem and warns of incomplete old-save hint state. | practitioner-heuristic | 007, HintTron/telephone rationale and old-save warning. | High attribution; no controlled efficacy or reliability estimate adopted. |
| C-03 | A creator account distinguishes guiding investigation toward a destination from revealing its contents. | practitioner-heuristic | 004, destination and deliberate-wandering discussion. | High attribution; the distinction’s usefulness is task-dependent. |
| C-04 | A visual-search assistance study provides narrow evidence that performance/preferences depend on technique and task. | empirical-evidence | 006, Participants/Procedure/Performance/Subjective Measures; context discrepancy retained. | Moderate within 16 experienced adults and two short custom tasks; no inventory-puzzle or G03 recipe validation. |
| C-05 | Unknown state and ambiguous goals warrant a qualified fallback rather than confidently specific advice. | inference | C-02’s failure mechanism; logical state/knowledge distinction. | Moderate as a safeguard; correct implementation and fallback usability remain untested. |
| C-06 | Player-controlled disclosure may preserve desired discovery, but any tier can spoil the actual task or add friction. | hypothesis | 004/007 rationale; explicit counterexamples in this entry. | Low until tested with relevant requests and participants. |
| C-07 | Access, requested answers and learning assessment need separate treatment; discriminating transfer checks must retain accommodations. | inference | Inspected corrected F01-PAT-01 and P01-TOP-02/P01-TOP-03 excerpts. | Moderate bounded transfer from reviewed drafts, not newly validated empirical support. |
| C-08 | Official puzzle-skip documentation does not establish equivalent participation in the skipped reasoning. | inference | 011, Navigation and Traversal / Skip Puzzle Option; scope distinction. | High logical caution, not a measured equivalence study. |
| C-09 | The proposed evaluation can reject the intervention for incorrectness, unwanted disclosure or excess burden. | hypothesis | Proposed method and counterconditions; no executed tests. | Low until tested; production and privacy constraints are proposals, not approved studio policy. |
| C-10 | The signal-station example illustrates the recipe and a state-confidence exit. | hypothesis | Author-created illustrative specification. | Low predicted-effect confidence; no implementation or observed player. |

Source suffixes expand to `GDR-SRC-20261010-G03-<nnn>`. Local conflicts `G03-CON-03`, `G03-CON-04` and `G03-CON-05` remain unresolved. Sources support rationale links; they do not validate this whole pattern.

## References

Access date for every record below: **2026-10-10, America/Los_Angeles**. Web-text line numbers identify this inspected retrieval; headings and named paragraphs are the portable locators. A source identity is temporary, reused within G03; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G03-007

**Ron Gilbert. [Dialogs, Hints and more...](https://blog.thimbleweedpark.com/hints_and_dialogs.html).** Official Thimbleweed Park development blog. Date: 2017-06-20.

**Edition/context:** Build 1388.918 update account; Steam availability reported, other platforms pending in that post. **Access:** `relevant-excerpt`. **Type:** Firsthand implementation/failure account.

**Inspected locator:** Author body, especially rejected HintTron object-targeting/cooldown design, telephone hints and old-save state warning. Web-text lines 7–44.

**Support in this artifact:** C-02; rationale for the state/request safeguards, without claimed efficacy.

**Limits:** No controlled evaluation; old-save reliability percentage is an unvalidated author estimate and is not reused. Comments and embedded configuration instructions are not evidence or instructions to execute. **Independence:** Same author as 001/002/009. Hint content credited to Jenn and, with permission, Meghann O’Neill’s earlier online hints; that underlying hint work was not independently inspected.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-004

**Mobius Digital interview with creative director Alex Beachum; interviewer unnamed. [The Intentionality of Wandering](https://www.mobiusdigitalgames.com/news/the-intentionality-of-wandering).** Mobius Digital. Date: 2016-08-18.

**Edition/context:** Pre-release design interview. **Access:** `relevant-excerpt`. **Type:** Firsthand creator interview.

**Inspected locator:** Opening pathing discussion and questions on conscious wandering, telegraphing destinations, probe constraints and future free exploration tests. Web-text lines 20–46.

**Support in this artifact:** C-03; task-dependent distinction informing disclosure choices.

**Limits:** Design intentions and informal observations, not controlled proof or a verified shipped route. Proposed future tests in the interview are not G03 results. **Independence:** Same underlying production context as 003.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-006

**Jawad Jandali Refai, Scott Bateman and Michael W. Fleming. [External Assistance Techniques That Target Core Game Tasks for Balancing Game Difficulty](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2020.00017/full).** Frontiers in Computer Science 2:17. Date: 2020-06-04.

**Edition/context:** Version of record, DOI 10.3389/fcomp.2020.00017; HTML methods/results/discussion. **Access:** `relevant-excerpt`. **Type:** Original empirical research.

**Inspected locator:** “Apparatus and Setup,” “Participants,” “Procedure,” “Experimental Task,” “External Assistance Technique Performance,” “Subjective Measures,” “Summary of Study Results,” and “Explanation for Results of the Study.” Web-text lines 549–634.

**Support in this artifact:** C-04 only. Full study context and unresolved wording are retained in the G03 packet.

**Limits:** Sixteen mouse/keyboard-experienced adults; two custom visual-search tasks, not authored inventory puzzles. No raw-data reanalysis or figure-only values used. Summary/discussion differ in the context attached to an over-assistance exception; retain that ambiguity. **Independence:** Independent research group relative to the creator accounts; its literature review is not separate inspection of every cited source.

**Rights:** CC BY as stated in the article copyright notice; paraphrased with attribution; no figures or dataset redistributed.

### GDR-SRC-20261010-G03-011

**Matthew Dunnerstick / Naughty Dog. [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed).** Naughty Dog. Date: 2020-06-09; later patch references present; last-update date unknown.

**Edition/context:** Original-release, controller-oriented documentation; puzzle row explicitly mentions patches 1.01 and 1.02; not a checked current PC/remaster build. **Access:** `relevant-excerpt`. **Type:** Official feature documentation.

**Inspected locator:** “Accessibility Presets,” “Alternate Controls,” and “Navigation and Traversal” / “Skip Puzzle Option”; web-text lines 13–39 and 94–106.

**Support in this artifact:** C-08: documented bypass is not equivalent reasoning participation.

**Limits:** Documents offered controls and a stated puzzle-access limit. Feature existence or bypass does not establish equal access to puzzle reasoning or equivalent experience. **Independence:** Separate studio from other creator sources; promotional/support documentation, not an independent accessibility audit.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

## Inspected shared-candidate provenance

Source container: **GD-Knowledge-first-wave-reviewed-drafts-2026-10-10.zip**, Library `libfile_6852a9bc35108191bdcf23bd487e3b42`; actual bytes retrieved in G03 and SHA-256 matched to parent receipt: `e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef`. Root is `GD-Knowledge-first-wave-reviewed-drafts-2026-10-10/`. The following are inspected **excerpts of selected drafts**, not re-verification of their entire public bibliographies. All remain version **0.1.0**, status **draft**, null approval metadata. They are not resent with G03.

**GDR-CAND-20261010-F01-TOP-03** — `selected-drafts/topics/learning-and-onboarding.md`; revision `original`; SHA-256 `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598`. Locator: “Guidance should track the learning demand”; “Discovery and explanation”; “Practice”; “Feedback”; “Re-entry,” inspected lines 65–103.

**GDR-CAND-20261010-F01-PAT-01** — `selected-drafts/patterns/supported-attempt-and-transfer-check.md`; revision `independent-review-correction-1`; SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Locator: Purpose, prerequisites, mechanism, recipe and corrected transfer probes, inspected lines 49–118; correction.diff.md lines 18–43.

**GDR-CAND-20261010-P01-TOP-02** — `selected-drafts/topics/interface-and-information.md`; revision `review-correction-1`; SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`. Locator: “Working definitions” and “Task-information contract,” inspected lines 63–81.

**GDR-CAND-20261010-P01-TOP-03** — `selected-drafts/topics/accessibility-and-inclusive-interaction.md`; revision `review-correction-1`; SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. Locator: Definition/access chain and proposed evaluation, inspected lines 54–87 and 193–221; corrections/P01/CORRECTION_RECEIPT.md lines 3–21.

The parent-selected correction receipts govern which draft was inspected; they do not make its hypotheses accepted evidence. External dependency file paths are recorded as text because the files are not in this delivery. The [G03 packet](../reviews/full-run-20261010-g03-review-packet.md#dependency-register) holds unresolved links and proposed integration ownership.

## Related entries and history

Genre adaptations: [Action adventure](../genres/action-adventure.md), [Adventure](../genres/adventure.md), [Point-and-click adventure](../genres/point-and-click-adventure.md). Complement: [Recoverable dependency gate](recoverable-dependency-gate.md), which addresses supported state/recovery rather than the correctness or scope of a hint.

Shared-owner proposal: Presentation information/access with Worlds W02 quest/dialogue state and Foundations learning/difficulty consultation. Those downstream candidates remain uncaptured here. Coordinate against existing and pending pattern concepts before any canonical placement; a new candidate ID does not establish novelty or ownership approval.

Initial capture `initial-capture-1`, version `0.1.0`, draft, null predecessor/supersession and approval fields. Author self-review identifies the strongest objection: even a correct “next destination” hint can reveal the discovery being sought, and helping performance is not the same as preserving the desired experience. The recommendation therefore remains conditional and low-confidence. Independent G03 review, player tests, implementation and release have not occurred. See the [packet](../reviews/full-run-20261010-g03-review-packet.md) for byte identity and next decisions.
