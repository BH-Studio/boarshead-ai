---
id: GDR-CAND-20261010-F04-PAT-01
kind: pattern
title: Response-feasible threat composition
version: 0.1.0
status: draft
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_id: F04
candidate_revision: independent-review-correction-1
attempt_id: F04-attempt-1
updated: '2026-10-11'
date_basis: America/Los_Angeles; public access crossed 2026-10-11 UTC
evidence_checked: '2026-10-11'
aliases:
- joint threat feasibility
- response policy audit
- overlapping attack conflicts
tags:
- encounters
- timing
- positioning
- resources
- hypothesis
related_topics:
- GDR-CAND-20261010-F04-TOP-01
- GDR-CAND-20261010-F04-TOP-02
related_patterns: []
related_genres: []
source_ids:
- GDR-SRC-20261010-F04-001
- GDR-SRC-20261010-F04-002
- GDR-SRC-20261010-F04-003
- GDR-SRC-20261010-F04-004
reviewer: null
approved_by: null
approved_date: null
independent_review: bounded-review-with-open-conditions
coverage_status: coverage-open
predecessor_sha256: afade7d1c604155f8dfd01ba10130f6dccc199cc4af0d6066408a306570f79d4
supersedes: null
integrity_receipt: ../reviews/f04-local-revision-receipt.md
---

# Response-feasible threat composition

**Draft research candidate — not released guidance.** Version 0.1.0; candidate revision independent-review-correction-1. Bounded independent review and local clarification recorded on 2026-10-11; no approval, game implementation, prototype, gameplay observation, participant recruitment or playtest. Examples explicitly marked illustrative are inventions for analysis. Original submission history below is historical; the local revision receipt identifies selected bytes.

## Purpose

Audit whether **consequential combinations of threats leave an allowed response sequence for the declared goal and entry state**. The intended player-facing benefit is a conflict whose commitments can be understood and acted upon, rather than a combination that accidentally contradicts its promise. The complete experience benefit is a hypothesis; the recipe is not a universal rule that every attack must be dodgeable. [C-01, C-06, C-07]

This pattern owns the systems question of joint response feasibility. It does not own spatial composition, cue styling, enemy behavior implementation, automatic difficulty adjustment or input buffering. A valid plan in a model is not proof that a player sees it, can execute it, enjoys it or considers the outcome fair. [C-04, C-06]

## Context and prerequisites

Use when several threats, objectives or costs can overlap and the design makes some response promise: survive with specified capabilities, protect an actor, reach an exit, interrupt a danger, or avoid damage after adequate preparation. Define the promise rather than assuming one. Real-time systems can be examined through ordered events; discrete systems can use explicit turns. [C-01, C-02]

Required inputs are a bounded encounter slice; allowed entry states; relevant movement/defense/actions; resource costs; threat resolution conditions; and a description of information available before each commitment. Include support/assistance states the project actually intends to support. The team needs authority to change the design later; this research artifact grants none. [C-02, C-03, C-05]

**Prerequisite exit:** when goals, timing, entry conditions or available actions are unknown, record an unresolved case. Do not invent a successful response or broaden the game’s promise. When a no-win outcome is deliberate, audit whether its information and consequence serve that purpose instead of forcing a survival solution. [C-06]

## Mechanism and evidence

| Link in the proposed mechanism | Evidence status | What does not follow |
|---|---|---|
| Explicit state/action/cost definitions permit a bounded feasibility check. | Logical/model claim. The worked example establishes only its stipulated cases. [C-01, C-03] | The model need not represent the actual game accurately. |
| Ordering responses can reveal opportunities or conflicts missed by checking attacks separately. | Inference supported by the sequence example; counterplay-timescale rationale is practitioner evidence. [C-02] | Every attack should gain an immediate counter. |
| A feasible policy can become understandable and executable through valid information and controls. | Conditional hypothesis, informed by clarity/input guidance. [C-04] | A witness alone proves accessibility or fairness. |
| Better understood commitments can improve the intended conflict experience. | Unverified whole-pattern hypothesis. [C-07] | More survival, lower damage or more options automatically means better play. |

The Riot and Valve sources are creator/practitioner material, not controlled studies of this recipe. The Naughty Dog document shows an option context, not causal benefit. Existing reviewed candidates supply distinctions, not new independent empirical corroboration. [C-02–C-05]

## Recipe

1. **Write the goal precisely.** Distinguish survive, avoid harm, preserve a location, escort, escape and accept a sacrifice. Identify any permitted partial outcome. Do not retroactively redefine success to excuse an unintended impossible state. [C-01, C-06]
2. **Bound the entry-state promise.** Record available actions, positions/support, resources, relevant information and assist settings. Separate forced entry conditions from deficits created by earlier disclosed choices. [C-03, C-05]
3. **Describe each consequential threat.** State what triggers it, what can change after commitment, when/where it resolves, what it affects, and whether it can be interrupted, mitigated, evaded or strategically avoided. Do not require every small attack to support every category. [C-02]
4. **Enumerate candidate response sequences.** Include preparing, repositioning, spending, guarding, interrupting, waiting, accepting allowed harm or leaving. Use the actual action budget and target/context rules. A list of individually successful actions is insufficient. A fixed sequence witnesses only its stipulated trajectory. If threats branch or information is hidden, specify which observations are available before each choice and require a response policy that uses only those observations, not future or hidden facts. State whether the promise concerns every allowed branch, some possible outcome, or a defined probability of success; do not silently substitute one for another. [C-01, C-02]
5. **Check interactions at each consequential boundary.** Can responding to one threat invalidate another response? Does a displacement change range or support? Is a resource consumed before its second use? Does guarding prevent reaching the objective? [C-03]
6. **Classify the evidence from a failed search.** Failure to find a witness is an unresolved result unless a complete bounded enumeration or explicit proof establishes infeasibility under the declared rules and information. Distinguish that result from unavailable information, execution difficulty, a consequence of prior commitment or intentional loss. Do not label all of these “unfair.” [C-04, C-06, C-08]
7. **Change the smallest responsible rule, when authorized.** Candidate revisions include ordering threats differently, changing a conditional trigger, preserving an escape, exposing a relevant preparation requirement or revising the goal honestly. Compare removing a redundant threat with adding another defensive mechanic. [C-02, C-07]
8. **Recheck lower-bound and transition cases.** Include the lowest allowed resources, interruption, assist exceptions, allies/other players when relevant, and return from a reset. Record unresolved coverage rather than claiming exhaustive validation. [C-03, C-05]
9. **Evaluate the experience separately.** A model witness is only the structural part. Test predictions, actual legal actions, failure explanations, accepted commitments and valued tension through later authorized evaluation. Preserve required accommodations. [C-04, C-07, C-08]
10. **Retain, narrow or exit.** Keep the technique only if it clarifies the intended promise and adds value beyond simpler composition. If achieving universal no-hit feasibility erases desired commitment, narrow the promise or reject that use of the pattern. [C-06, C-07]

### Adjustable variables

The local variables are concurrency, order, commitment and recovery periods, movement/target constraints, resource availability, assistance state, escape conditions, permitted harm and disclosure. Author them against the actual task. No standard count of enemies, universal telegraph duration, minimum defense window, fixed resource reserve or acceptable death rate is supplied. [C-02, C-03, C-05]

### Exit conditions

Stop and document the gap when the response depends on unavailable data, an unreviewed dependency or a prohibited action. Do not add automatic escape to a deliberately binding decision simply to make the audit pass. Do not erase a necessary accommodation to make another mode’s witness easier to describe. Stop expanding the state enumeration when a bounded next discriminating case is more useful; record what remains unexamined. [C-03, C-05–C-07]

## Worked examples

### Illustrative: three positions and two deadlines

This is an invented discrete model, not a running game or performed playtest. Positions are **L, C, R**, with the actor starting at C. On each beat the actor may move to an adjacent position, wait, or guard. There is one action per beat. Moving gives no invulnerability and there is no off-grid exit or interrupt. Guard costs one charge and lasts through resolution at the end of that beat. [C-01]

A beam resolves at the end of beat 2 and hits C; guarding cannot stop it. A sweep resolves at the end of beat 2 and hits L and R; guarding can stop it. The declared goal is **take no damage**. Both threats are visible before beat 1. The model assumes their effects resolve against the actor’s final position; these are local stipulations, not general combat rules. [C-01, C-06]

| Initial condition / change | Candidate policy | Deduction under the stipulated rules |
|---|---|---|
| One guard charge | Move C→L on beat 1; guard on beat 2 | Avoids the center beam and blocks the side sweep. A temporal sequence works even though no one action solves everything. |
| Zero guard charges, unchanged threats | Any sequence ends beat 2 at L, C or R | Every endpoint is covered and the sweep cannot be guarded. No no-damage policy exists within this model. |
| Zero charge; sweep moved to end of beat 3 | Move to L on beat 1; wait on beat 2; move to C on beat 3 | The beam has finished before the actor returns to C, and the later side sweep misses. |

The second row is a structural counterexample, not a claim that zero resources is always unfair. If zero charge is a forced permitted entry state and the game promises a no-hit solution, the composition contradicts that promise. If the player knowingly spent the charge to gain another advantage, that earlier choice may be the relevant response opportunity. If the real goal is survival and one hit is allowed, a no-damage audit would be enforcing an extra promise. [C-01, C-03, C-06]

The third row changes threat timing, not the player’s reflexes. Whether it creates an interesting encounter is unknown. A simpler single-threat composition might be preferable; the pattern requires that comparison rather than treating logical feasibility as sufficient quality. [C-07]

### Illustrative extension: protect a goal while moving

Replace the no-damage goal with protecting a vulnerable relay at C. Moving to L may now expose the relay even when it saves the actor. The witness must be reconsidered against the new goal; copying the earlier successful movement sequence would be invalid. This is a **changed-goal analysis**, not a same-rule learning-transfer result. [C-01, C-06, C-08]

## Tradeoffs and alternatives

An explicit audit can make hidden action conflicts easier to discuss, but state enumeration and authoring coverage have costs. The pattern can become a false precision exercise when the model omits ally behavior, contact, input restrictions or the actual goal. Use it for consequential combinations rather than as a requirement to enumerate every possible moment. [C-03, C-07]

Alternatives include fewer threats, more separated encounters, fixed authored sequences, clearly intentional pressure without a survival promise, or allowing the player to avoid the encounter strategically. Adding a universal dodge, invulnerability, cancellation or adaptive scheduler may be more expensive and may change the intended skill. Neither is required by this recipe. [C-02, C-06, C-07]

## Failure cases

| Warning sign | Likely diagnostic distinction | Candidate correction to evaluate |
|---|---|---|
| The witness uses an ability the player cannot have | Incorrect entry-state model | Narrow the applicable state or revise the promised encounter. [C-03] |
| The plan works only with knowledge hidden until too late | Information prerequisite missing | Change the permitted information, preparation opportunity or intended goal. [C-04] |
| Inputs arrive but actions remain locked | Eligibility mistaken for latency | Review commitment and action acceptance, not merely cue intensity. [C-04, C-08] |
| A supported assist breaks the sequence | Mode/state coverage gap | Re-evaluate the actual supported combination without withdrawing access. [C-05] |
| Every threat is harmless after revision | Feasibility confused with triviality | Restore meaningful commitment or use a narrower audit promise. [C-06, C-07] |
| Audit passes, but players cannot explain failures | Model correctness mistaken for comprehension | Test event prediction, feedback and alternative interpretations. [C-04, C-08] |

## Counterexamples and do not use conditions

Do not use this pattern to require immediate reactions to every strategic error, to reverse deliberate sacrifices, or to make intentional no-win scenes survivable. A decisive punish after a disclosed commitment can be meaningful even though no last-moment response exists. A threat can also impose an acceptable cost while leaving another goal achievable. [C-02, C-06]

Do not make an enemy’s entire intention public solely to guarantee an immediate response. Preserve the distinction between unknown intent and uncommunicated rules. Do not claim equal competitive conditions, moral fairness, accessibility certification or player enjoyment because one legal action sequence exists. [C-04–C-06]

## Playtest

**Proposed, not performed.** Begin with a later authorized rule-level check of the declared states, then a separate player study. Compare the candidate composition with its baseline and a simpler reduced-threat alternative. Keep objective, relevant resources, visibility and nominal threat pressure comparable where possible; record what cannot be matched instead of describing the comparison as controlled. [C-07, C-08]

Recruit relevant familiarity/access profiles, record exact build/scene/input/camera and retain required accommodations. Ask event and legal-response predictions before action, then observe choices, execution, explanations, failure cost and desired tension. Include cases where guarding is correct, incorrect or unavailable; an always-guard strategy must not satisfy the learning check. Separate same-rule transfer from changed-goal or changed-rule adaptation. [C-04, C-05, C-08]

**Reject or narrow** the experience recommendation if the audit does not locate the actual failures, the simpler alternative performs as well with less cost, understanding does not improve, required access fails, or the revision removes a locally important kind of commitment. Better survival alone is insufficient. Predefine meaningful margins and uncertainty with the local research owner; no sample count or numerical success threshold is universal. No results are available. [C-07, C-08]

## Claim ledger

Confidence applies to the stated proposition, not to universal effectiveness. Proposed design models are not formal standards or approved studio decisions. Local claim IDs do not identify claims in another entry.

### C-01

**Claim:** Under explicit state, action and outcome rules, separate feasible threats can compose into an infeasible joint response problem.

**Class:** `inference`. **Support / contrary case:** Logical three-position worked example; no source is needed to establish the stipulated model result. GDR-SRC-20261010-F04-001 and GDR-SRC-20261010-F04-003 motivate the design question, not its general efficacy.

**Applicability:** The goal, entry state, resource budget and available action sequence must be declared.

**Confidence:** High for the model result; not evidence of player-perceived fairness.

**Unresolved / discriminating question:** Does the real task have additional actions, partial outcomes or prior commitments that alter feasibility?

### C-02

**Claim:** Audit response policies over time rather than requiring one immediate universal response to every attack.

**Class:** `inference`. **Support / contrary case:** GDR-SRC-20261010-F04-001, tactical/strategic distinction and rejection of tactical counterplay for every spell; reviewed F02-decision commitment analysis.

**Applicability:** Consequential threat combinations under the intended response timescale.

**Confidence:** Moderate: source rationale and sequence logic align; optimal audit method untested.

**Unresolved / discriminating question:** Is the relevant response preparation, interruption, evasion, accepting harm or withdrawal?

### C-03

**Claim:** The composition audit should use actual entry capabilities and costs, not ideal resources or an unconstrained empty test space.

**Class:** `inference`. **Support / contrary case:** Model dependence in C-01; GDR-SRC-20261010-F04-003, role/placement and pacing sections, is one production context. F03/W03 quantitative guidance not transferred.

**Applicability:** Includes permitted low-resource, assistance and shared-player states relevant to the promise.

**Confidence:** Moderate for audit validity; no exhaustive-state coverage guarantee.

**Unresolved / discriminating question:** Does a proposed solution depend on an unavailable resource or an earlier decision the player could not make?

### C-04

**Claim:** A response witness must be communicable and executable for the intended context before its existence can support an experience recommendation.

**Class:** `hypothesis`. **Support / contrary case:** GDR-SRC-20261010-F04-002, Clarity in League/Abilities; reviewed P02-input and P02-multimodal distinguish information, eligibility and execution.

**Applicability:** A model witness is necessary only for the declared feasibility promise, not sufficient for understanding or success.

**Confidence:** Low for a general experience benefit; the separate links need testing.

**Unresolved / discriminating question:** Do players perceive and choose the witness, or merely succeed through unrelated tactics?

### C-05

**Claim:** Assistance can change which response policies exist; do not silently remove it or ignore documented exceptions.

**Class:** `inference`. **Support / contrary case:** GDR-SRC-20261010-F04-004, Combat Accessibility and encounter exceptions; reviewed F02-difficulty.

**Applicability:** Local option combinations and mode rules, with access needs preserved.

**Confidence:** Moderate for checking validity; not evidence that all assistance must be allowed in every competitive mode.

**Unresolved / discriminating question:** Which supported assistance state is excluded by the current composition?

### C-06

**Claim:** Threat feasibility is not the same as a guarantee of no damage, no failure, immediate reversibility or universal fairness.

**Class:** `inference`. **Support / contrary case:** C-01–C-03; GDR-SRC-20261010-F04-001 and reviewed F02-decision support timescale/commitment boundaries.

**Applicability:** The declared goal may allow damage, sacrifice or a no-win outcome for a different purpose.

**Confidence:** High for distinguishing propositions; moral/player judgments remain contextual.

**Unresolved / discriminating question:** Is the audit enforcing a stronger promise than the game actually makes?

### C-07

**Claim:** Using this audit may improve understandable agency without eliminating desired commitment, but that complete causal claim is untested.

**Class:** `hypothesis`. **Support / contrary case:** Original F04 synthesis; no inspected source compares this full recipe with baseline or simpler threat reduction.

**Applicability:** Only after matching the intended task and testing rival explanations.

**Confidence:** Low: no F04 gameplay evaluation or independent replication.

**Unresolved / discriminating question:** Does the audited version outperform a simpler alternative on the intended experience without flattening it?

### C-08

**Claim:** Validation must distinguish state infeasibility, misunderstood information, failed execution and disliked consequences.

**Class:** `inference`. **Support / contrary case:** Reviewed F01-transfer, F02-decision/difficulty and P02-input; logically separate failure categories in this recipe.

**Applicability:** Proposed mixed structural and player evaluation; no tests performed.

**Confidence:** Moderate for measurement separation, not for any empirical outcome.

**Unresolved / discriminating question:** Can both correct and incorrect response predictions be discriminated on new same-rule cases?

## References

All source IDs are temporary F04 identities. Access date: 2026-10-11 UTC (2026-10-10 in America/Los_Angeles). Locators specify the inspected extent, not an assertion that every linked item was read in full. Public-source bytes were not archived or hash-verified.

### GDR-SRC-20261010-F04-001

Riot Scruffy. **[Quick Gameplay Thoughts: May 14](https://www.leagueoflegends.com/en-us/news/dev/quick-gameplay-thoughts-may-14/)**. Riot Games; 2021-05-14. Edition/build: Historical League of Legends developer article; game build not specified.

**Access:** `full`. **Type:** Firsthand developer rationale. **Locator:** Champion Counterplay: definition; tactical versus strategic examples; Tactical Counterplay bullet containing “Not every spell needs tactical counterplay”; strengths/weaknesses paragraphs. **Limits:** No comparative study or effect size supplied. The article is not a current champion specification. **Relationships:** Same institutional source as F04-002; the two articles are not independent experiments. Central deduplication pending. **Rights:** Copyright Riot Games; paraphrase only; no media redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-002

bananaband1t / Riot Games. **[Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)**. Riot Games; 2021-03-12. Edition/build: Historical developer article; example builds not identified.

**Access:** `relevant-excerpt`. **Type:** Firsthand development account; textual descriptions of visual examples. **Locator:** “The Unbreakable Vows”; “Abilities,” including the Arcane Comet ground-circle example; “Changes From Development”. **Limits:** Text inspected, not an independent game replay or a perceptual experiment. Embedded media were not used to establish behavior. **Relationships:** Same institutional source as F04-001; no independent causal corroboration. Central deduplication pending. **Rights:** Copyright Riot Games; paraphrase only; embedded images/animations not redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-003

Michael Booth / Valve. **[The AI Systems of Left 4 Dead](https://cdn.akamai.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf)**. Valve; AIIDE presentation; 2009; exact publication day unknown. Edition/build: 2009 presentation, 95-page PDF; historical Left 4 Dead system account.

**Access:** `relevant-excerpt`. **Type:** Firsthand technical/design presentation. **Locator:** PDF pp. 64–65 (Structured Unpredictability); p. 69 (special-infected placement); pp. 78–82 (intensity and pacing states); p. 92 (pacing versus difficulty). Page numbering is 1-based PDF position. Screenshots inspected for pp. 81 and 92.. **Limits:** An authored intensity proxy is not a validated measurement of a player’s emotional state. No causal comparison of the proposed F04 techniques. **Relationships:** One Valve production account, not one independent source per slide. Central deduplication pending. **Rights:** Copyright Valve; paraphrase only; PDF/slides not redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-004

Naughty Dog; displayed byline Matthew Dunnerstick. **[The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed)**. Naughty Dog; 2020-06-09. Edition/build: PS4 launch-era feature documentation; page also contains Patch 1.01/1.02 annotations; not a current remaster verification.

**Access:** `relevant-excerpt`. **Type:** Official feature documentation. **Locator:** “Alternate Controls”; “Assistance”; “Navigation and Traversal” rows Navigation Assistance, Traversal Assistance and Ledge Guard; “Combat Accessibility” rows and encounter exceptions. **Limits:** Documents intended options, not measured accessibility, enjoyment, transfer, or efficacy in a verified running build. **Relationships:** Same URL appears in reviewed F02 as GDR-SRC-20261010-F02-011 and W02 as GDR-SRC-20261010-W02-017. Re-inspected here; mapping/deduplication pending, not independent evidence. **Rights:** Copyright Naughty Dog; paraphrase only; no screenshots or videos redistributed. Claim bindings appear in this entry’s ledger.

### Inspected reviewed-candidate dependencies

These are unreleased library candidates, not independent empirical sources. Exact bytes were read from the parent-selected archive; only the stated conceptual distinctions transfer. Their original public empirical findings are not reasserted without fresh source inspection. Missing package-local copies are deliberate: previous batches are not resent.

- **`GDR-CAND-20261010-F02-TOP-01`**, `selected-drafts/topics/decision-design.md`, version `0.1.0`, draft, revision `initial-capture-1`. SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`. Inspected relevance: Decision/scope, mechanisms, choices and claim ledger; decision prediction versus preference; commitment and information.
- **`GDR-CAND-20261010-F02-TOP-02`**, `selected-drafts/topics/challenge-and-difficulty.md`, version `0.1.0`, draft, revision `independent-review-correction-1`. SHA-256 `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1`. Inspected relevance: Mechanisms, assistance, recovery and tests; corrected evidence locator preserved without importing empirical numerical results.
- **`GDR-CAND-20261010-P02-TOP-01`**, `selected-drafts/topics/controls-and-input.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `b9235153ba8b742c6df47e9e23844d9ab5da82e4212ebd22f04e314f6ccce21b`. Inspected relevance: Action recognition/eligibility/outcome; buffering/context validity; remapping versus input-demand changes.
- **`GDR-CAND-20261010-P02-TOP-03`**, `selected-drafts/topics/multimodal-communication.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c`. Inspected relevance: Fact-preserving alternatives; deadline/context boundaries; competing attention; no modality-equivalence claim.
- **`GDR-CAND-20261010-F01-PAT-01`**, `selected-drafts/patterns/supported-attempt-and-transfer-check.md`, version `0.1.0`, draft, revision `independent-review-correction-1`. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Inspected relevance: Corrected answer-varying examples; same-rule transfer separated from changed-rule adaptation.

Archive receipt, transfer limits and unresolved links: [F04 review packet](../reviews/full-run-20261010-f04-review-packet.md#reviewed-dependency-inspection). No canonical identity or release is implied.

## Related entries and history

Related topics: [Combat and conflict systems](../topics/combat-and-conflict-systems.md) and [Movement and traversal](../topics/movement-and-traversal.md). Contrast with [State-conditioned traversal preview](state-conditioned-traversal-preview.md): that pattern changes information, not threat feasibility. Reviewed G02 input grace is a separate eligibility technique; spatial orchestration and resource pacing await W03/F03 dependency review.

Relevant open conflicts: `F04-CON-01` (counterplay timescale), `F04-CON-02` (information versus uncertainty), `F04-CON-03` (pacing/resource coupling). This pattern is one of exactly two F04 pattern candidates, not an allocation of permanent identity or a ceiling on useful future work.

Version `0.1.0`; revision `initial-1`; attempt `F04-attempt-1`; predecessor/supersession null. First submission, author self-review only, no independent F04 review. See the [review packet](../reviews/full-run-20261010-f04-review-packet.md) and [integrity receipt](../reviews/full-run-20261010-f04-integrity-receipt.md). The next decision concerns independent review and evidence gaps, not adoption or release.


**Local independent-review revision, 2026-10-11:** Stable provisional ID, version 0.1.0, draft and null approval fields retained. Clarifications and predecessor/selected hashes are recorded in [local revision receipt](../reviews/f04-local-revision-receipt.md). Earlier initial-submission/no-review history describes the original snapshot, not this later review. No gameplay or participant results added.
