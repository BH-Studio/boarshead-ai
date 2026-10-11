---
id: GDR-CAND-20261010-G04-PAT-01
kind: pattern
title: Provisional-versus-confirmed impact feedback
version: 0.1.0
candidate_revision: initial-capture-1
status: draft
run_id: GDR-FULL-20261010
batch_key: G04
attempt_id: G04-authoring-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- attempt versus confirmed impact
- late hit confirmation
- truthful provisional feedback
tags:
- asynchronous-feedback
- state-clarity
- correlation
- occlusion
- conditional-pattern
related_topics:
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G04-GEN-01
- GDR-CAND-20261010-G04-GEN-02
- GDR-CAND-20261010-G04-GEN-03
source_ids:
- GDR-SRC-20261010-G04-002
- GDR-SRC-20261010-P02-005
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G04 capture; no prior G04 candidate superseded.
byte_hash_record: ../reviews/full-run-20261010-g04-integrity-receipt.md
coverage_state: bounded-research-completed-coverage-open
independent_review: not-performed-for-G04
---

# Provisional-versus-confirmed impact feedback

**Draft 0.1.0 · initial-capture-1.** Proposed owner: BH-GDR-Presentation-and-Interaction; coordination with Foundations combat/conflict is pending. This is a cross-genre temporal-confirmation technique, not an approved implementation or an experimentally validated recipe.

## Purpose

Help a player distinguish an attempted or launched action from a **confirmed effect**, when asynchronous resolution or changing spatial context can make them appear equivalent. The intended problem is a false belief such as “that target was affected,” not merely weak spectacle. The intended benefit—fewer false success beliefs without excessive burden—remains a hypothesis. [C-02, C-05]

This pattern specializes temporal correlation and presentation lifetime. P02’s feedback topic owns the broader state distinctions; P02’s fact-preserving cue alternatives owns modality equivalence. G04 does not rename either as a new generic pattern. It adds a conditional recipe for provisional effects, confirmation, late/rejected results and target-relative interpretation. [C-DEP]

## Context and prerequisites

Use when an action can be acknowledged before its effect is settled, or when the eventual result is liable to be attributed to the wrong target, location or attempt. Examples could include a networked projectile, a remote interaction, a spell whose effect resolves later, or a collaborative tool action. These are applicability hypotheses, not claims that every such interaction needs extra UI. [C-02, C-06]

Prerequisites: a defined source of authoritative outcome; ability to distinguish action instances and their possible results conceptually; an information contract specifying what the player may learn; and at least one perceivable representation of the necessary fact. The design must distinguish a confirmed hit from a confirmed elimination, and both from a launch. If the authoritative outcome is unavailable, do not label it confirmed. [C-02, C-04]

**Entry stop condition:** when the task resolves immediately and one cue is unambiguous, omit this extra structure. When the underlying state is wrong or undefined, correct that problem rather than claim presentation can repair correctness. [C-01, C-02]

## Mechanism and evidence

| Causal link | Support | Limit and competing explanation |
|---|---|---|
| Early feedback can precede known effect | Described in the Riot development account. [C-01] | A historical architecture example, not a rule for every engine. |
| Treating early feedback as success can misrepresent the known state | Semantic inference from that distinction and inspected P02-F. [C-02] | Players may already understand the cue; absence of an extra marker may be preferable. |
| Correctly correlated result feedback can remove that false implication | Proposed design inference. [C-02, C-03] | Incorrect target association or stale spatial placement can create a new error. |
| Preserving facts through configured alternatives can keep the decision available | Guidance-to-application inference. [C-04] | Availability is not demonstrated timely comprehension or equal performance. |
| Players make fewer erroneous follow-up decisions | **Hypothesis**, not established by the account or the source’s planned fix. [C-05] | Added cues may overload attention or reduce the feeling of direct control. |

No empirical effect size, acceptable latency, required number of cue layers or universal intensity hierarchy is supported. [C-05, C-06]

## Recipe

### 1. Write the action-and-result contract

Record the attempted action, eligible targets, local acceptance, provisional effect, authoritative outcomes and meaningful follow-up decisions. Include rejection, partial effect, target disappearance and an unresolved timeout where those are genuine states. Do not invent a visible cue for every possible internal state; the map exists to prevent false claims. [C-02]

**Exit:** if “accepted,” “hit” and “completed” cannot be distinguished semantically, resolve the interaction specification first. A brighter effect cannot clarify an undefined result. [C-02]

### 2. Decide the minimum truthful early feedback

Choose whether the player needs to know input receipt, action launch or neither separately. A weapon motion or visible traveling object can acknowledge a launch without asserting a hit. Avoid an early sound, marker or wording already taught to mean successful effect. When early acknowledgment serves no decision and adds clutter, omit it. [C-01, C-02, C-06]

### 3. Associate a result with its intended action and target

Specify how repeated attempts, multiple targets, partial effects, late results and target changes will be understood. A late confirmation of action A must not masquerade as the result of the more recent action B. Do not confirm an elimination merely because damage occurred. This is a conceptual correlation requirement, not an instruction to implement a particular networking protocol. [C-02, C-06]

**Exit:** when correct association cannot be supplied, use only a narrower truthful result or remove the ambiguous feedback until the state model is resolved. Do not choose a visually convincing fiction. [C-02]

### 4. Choose spatial anchoring and lifetime against the information contract

Evaluate world contact position, target-relative placement and nonspatial confirmation. Each can mislead in different conditions. A contact effect at a past position may appear to hit a different body region after motion; a target-attached effect can reveal movement behind cover. Select the smallest representation that conveys the legitimate confirmed fact. [C-03, C-04]

Riot’s discussion of possible attachment changes is **reported planned work**, not a license to assert that all effects should attach to targets or that the proposed change shipped unchanged. Treat obstruction and information leakage as tests, not optional polish. [C-03]

### 5. Distinguish rejection, expiry and unresolved state

If the attempted action cannot produce the believed result, avoid leaving a success impression. Where a pending state matters, allow it to resolve or expire intelligibly. “No result yet” must not be translated into a confirmed miss when the system does not know that. Where a transient decorative effect naturally ends without implying success, additional error messaging may be unnecessary. [C-02, C-06]

### 6. Preserve result meaning through configured cue routes

For sound-off, reduced-effects, haptics-off and other supported configurations, retain the necessary result through usable alternatives. Preserve uncertainty and access boundaries: an unidentified hit does not become a caption naming an unseen opponent. Check the actual context and language instead of equating visual, audio and haptic intensity. [C-04]

### 7. Compare, narrow or remove

Evaluate false beliefs, misattributed targets/actions and follow-up decisions, not just perceived impact strength. If added distinction produces more confusion or unnecessary waiting, simplify or remove it. If only particular action types need it, narrow the pattern to them rather than propagate an elaborate state display across the game. [C-05, C-06]

## Adjustable variables

Adjustable choices include event granularity, which state is acknowledged early, result categories, spatial reference, visibility under occlusion, lifetime, aggregation of repeated results, optional detail and cue-route selection. Any timing, animation duration or display threshold chosen by a project is a **local experimental parameter** until supported for that context. No default milliseconds, colors, body-region markers or effect layers are prescribed. [C-06]

## Worked examples

### Illustrative example — remote repair capsule

A cooperative player launches a capsule at a damaged moving drone. The local launch animation acknowledges that the attempt was made; it does not use the “repair complete” symbol. A confirmed attachment identifies the affected drone to the extent the player is entitled to know it. A later repair-completed result is separate if the drone can interrupt or lose the capsule before completion. These rules and objects are invented. [C-06]

Apply the recipe by listing the player’s follow-up choices: fire again, switch drone or wait. If the drone moves behind an obstruction, do not attach an always-visible repair beacon that supplies otherwise hidden location. A nonspatial completion cue may be enough when the affected target is already unambiguous. If multiple launches overlap, test whether the eventual result can be assigned to the correct attempt; suppress or aggregate decorative cues that cannot be distinguished usefully. [C-02–C-06]

### Illustrative counterexample — immediate local target switch

A local abstract puzzle resolves a ray and changes a switch in the same authoritative step. Its changed switch state is already the relevant confirmation. Adding “received,” “pending” and “confirmed” messages can invent delay and increase task burden. Here the appropriate adaptation is to omit the pattern, while retaining clear final state and supported access alternatives. [C-02, C-04, C-06]

## Tradeoffs and alternatives

A single authoritative cue is simpler and preferable when it arrives soon enough for the task and is unambiguous. A provisional acknowledgment may preserve useful responsiveness but costs semantic education and correlation. World-space contact effects preserve collision location yet may be misread after motion; target-relative effects preserve association yet can leak information. A nonspatial result reduces those spatial ambiguities but may lose necessary direction or target identity. These are conditional tradeoffs, not a ranked universal solution list. [C-02–C-06]

The pattern does not repair unreliable simulation, provide anti-cheat assurance, or decide whether a game should reveal hit confirmation at all. A deliberately uncertain simulation may withhold an outcome consistently; accessibility should preserve the available evidence, not override that decision for one cue route. [C-01, C-04]

## Failure cases and observable warning signs

| Failure | Warning sign to investigate | Proposed correction |
|---|---|---|
| Early cue reads as success | Players stop the action while believing an unconfirmed target was affected. | Revise the taught meaning or omit the early success-like signal. [C-02, C-05] |
| Late result attributed to a new attempt | Explanations name the currently aimed target rather than the actual result. | Reduce ambiguity through association, aggregation or narrower result detail. [C-02, C-06] |
| Spatially misleading confirmation | Players infer a hit region or location not supported by the result. | Compare anchoring/lifetime against moving and occluded cases. [C-03] |
| Access alternative leaks knowledge | A caption or marker identifies hidden actors unavailable in the original evidence. | Preserve the uncertainty and legitimate facts. [C-04] |
| Overcomplicated state display | Players monitor UI instead of the intended task, or cannot distinguish result classes. | Collapse unnecessary stages; retain only meaningful distinctions. [C-05, C-06] |

## Counterexamples and do-not-use conditions

Do not apply when success is intentionally unknowable and a confirmation would defeat that uncertainty; when the task is already instantly unambiguous; when the only issue is wrong simulation; or when the team cannot maintain result association. Also reject when the added cue would expose protected multiplayer information or when required access configurations cannot communicate its meaning in time. [C-02–C-06]

## Proposed playtest — not performed

**P-A: Truthful temporal distinction versus simpler feedback.** Compare the existing cue, a simplified authoritative-only cue and the proposed distinction using the same action/outcome sequence. Hold collision rules, result timing, target paths, aim assistance and eligible information constant; record any unavoidable changes. Use plausible result orderings, moving targets, rejected attempts and partial success without requiring purchased stakes. This is a proposed design, not a constructed harness. [C-05, C-06]

Include relevant devices, experience levels and participants who use the intended access routes. Counterbalance exposure where appropriate. Measure beliefs about whether, when and which target was affected; mistaken switches/repeats; missed information; burden and preference. Track latency variability, learned cue meanings, language and target visibility as confounds. A player’s preference for stronger effects is not proof of more accurate understanding. [C-04–C-06]

**Falsification:** reject the claimed benefit if correct attribution does not improve in the diagnosed case, if the simple authoritative cue performs as well with lower burden, or if an access configuration loses necessary facts. Any hidden-information leak is a design failure even when hit comprehension rises. Define project-specific acceptable differences and sample justification before recruiting; no power guarantee or universal decision threshold is supplied. [C-05, C-06]

## Related entries, remaining gaps and history

Applicable genres: [Shooter](../genres/shooter.md), [Tactical shooter](../genres/tactical-shooter.md), and some interactions in [Extraction game](../genres/extraction-game.md). The pattern is not mandatory for any of them. Pending ownership links are P02 feedback/multimodal and F04 combat/conflict; this is not a new genre-neutral topic. [C-DEP]

Open evidence includes contextual user validation, perception across devices/languages, complex action aggregation, current engine authority behavior and occlusion-sensitive information contracts. Initial capture only, null predecessor/supersession, independent G04 review not performed, no release. See local conflict G04-CON-04 and author challenge in the packet. [C-DEP]
## Inspected shared guidance and dependency status

These are parent-selected **0.1.0 draft** dependencies, not released references. Relevant bytes were inspected in the cumulative archive; no earlier batch is resubmitted. This transfers scoped reasoning, not the empirical findings of unopened underlying papers. Full identity/hash receipt and the exact missing-source list are in the [review packet](../reviews/full-run-20261010-g04-review-packet.md#reviewed-dependencies).

| Selected candidate | Revision and precise local locator | Conditional transfer |
|---|---|---|
| `GDR-CAND-20261010-P02-TOP-02` | `review-correction-1`; archive `selected-drafts/topics/feedback-and-game-feel.md`, lines 77–89 | Attempt, acceptance, pending and outcome are different facts; no fixed cue quota. |
| `GDR-CAND-20261010-P02-TOP-03` | `review-correction-1`; archive `selected-drafts/topics/multimodal-communication.md`, lines 84–96; 119–130 | Alternative cues preserve known facts, uncertainty and decision timing. |
| `GDR-CAND-20261010-P02-PAT-02` | `review-correction-1`; archive `selected-drafts/patterns/fact-preserving-cue-alternatives.md`, lines 50–107 | Information contracts, configured alternatives, and rejection when timely meaning is lost. |
| `GDR-CAND-20261010-P02-TOP-01` | `review-correction-1`; archive `selected-drafts/topics/controls-and-input.md`, lines 60–105; 109–120 | Action/binding/activation distinctions, physical demand and device parity limits. |
| `GDR-CAND-20261010-F07-TOP-01` | `initial-capture-1`; archive `selected-drafts/topics/evaluation-and-balancing.md`, lines 67–93; 123–133 | Denominators, qualitative explanation and interacting-player units. |

F03 progression/economy and F04 combat/traversal outputs are **unreviewed running/queued dependencies without inspected bytes here**. No exact candidate ID or path is invented. Current canonical index/pending allocations and the live recovery ledger are missing. Shared ownership links remain proposals. The supplied audio pilot is hypothesis context only, never a requirement for this genre or recipe. [C-DEP]

## Claim ledger

Claim classes describe support, not certainty. `observed-example` refers only to the identified document when no game observation is stated. Confidence applies to the narrowly worded claim.

| Claim | Precise claim | Class | Sources and locators | Confidence and reason | Limits / unresolved question |
|---|---|---|---|---|---|
| C-01 | Riot’s developer account distinguishes simulated correctness from misleading presentation and distinguishes local shot effects from server-confirmed hits. | practitioner-heuristic | GDR-SRC-20261010-G04-002: Correctness vs Clarity; From Click to Headshot | Moderate: primary development explanation, not independent testing of this pattern. | Historical account; embedded videos not inspected; no claim about the latest build. |
| C-02 | Correlating feedback to the correct action, target and known result is a plausible way to avoid implying unconfirmed success. | inference | C-01; inspected P02-F, lines 77–89 | Moderate for the semantic constraint; effectiveness depends on implementation and comprehension. | A single clear cue may suffice when no meaningful ambiguity exists. |
| C-03 | A truthful cue can still mislead spatially when its displayed position and the interpreted target move out of agreement. | practitioner-heuristic | GDR-SRC-20261010-G04-002: Case Study 2; Planned Clarity Improvements | Moderate for the reported failure; the reported proposed correction is not a verified universal solution. | Attachment may reveal occluded information; no blanket instruction to attach all impacts to a target. |
| C-04 | Alternative confirmation routes should preserve result, uncertainty and legitimate information, not just add sensory intensity. | inference | GDR-SRC-20261010-P02-005: Goal/Overview; inspected P02-A, lines 50–107 | Moderate: platform guidance plus explicitly scoped design reasoning. | Does not establish emotion or competitive-performance equivalence. |
| C-05 | The complete recipe may reduce false success beliefs without unacceptable response burden in asynchronous tasks. | hypothesis | C-01–C-04 causal chain; proposed P-A test | Low: no G04 prototype or user test. | This is the principal unvalidated benefit; reject if cue complexity causes equal or greater confusion. |
| C-06 | The examples, adjustable variables and test decision rules are illustrative local proposals, not validated numerical defaults. | hypothesis | G04 authored recipe/examples; inspected F07-E | Low until evaluated in the actual task and access configurations. | No code, network experiment, gameplay, participant or host test has run. |
| C-DEP | The pattern is proposed P&I-owned cross-genre work using inspected draft dependencies; canonical ownership/allocation remain pending. | observed-example | G04 dependency and ownership receipts | High for present administrative state only. | It is not a replacement for P02 feedback or fact-preserving cue alternatives. |
## References

All access dates are 2026-10-10. In relationship notes, `G04-NNN` abbreviates `GDR-SRC-20261010-G04-NNN`; it is not another source identity. Observation route: assistant inspection of the identified public document, not game play, a match recording or participant observation. All excerpts are paraphrased; copyright remains with the rights holders. No source text, media or paper is redistributed. Dates refer to the named document unless explicitly identified as a game release.

### GDR-SRC-20261010-G04-002

Kevin Lee, game systems software engineer, Riot Games. **[The State of Hit Registration](https://playvalorant.com/en-us/news/dev/the-state-of-hit-registration/)**. Date: 2020-08-06. Publisher: Riot Games. Edition/build: 2020 account, including beta 0.50 context; proposed improvements are not verified current features. Access: `relevant-excerpt`. Type: firsthand development explanation.

**Precise locator:** “Correctness vs Clarity”; “From Click to Headshot”; “Case Study 2: Crouching into Shot VFX”; “Planned Clarity Improvements”. **Claims supported here:** C-01, C-03; context for C-02/C-05 only. **Limits:** Text inspected; embedded recordings not watched. Does not measure benefit of the G04 recipe. **Independence:** Same Riot provenance group as G04-001/015; P02 feedback transfers are not additional experiments. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-P02-005

Microsoft. **[Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103)**. Date: updated 2026-03-04. Publisher: Microsoft Learn. Edition/build: Unnumbered web guidance revision; reopened for G04. Access: `relevant-excerpt`. Type: platform accessibility guidance.

**Precise locator:** “Goal”; “Overview”; “Scoping questions”; multisensory communication options. **Claims supported here:** C-04. **Limits:** No inference that simultaneous cue multiplication improves all performance; preserves meaning rather than promising equal experience. **Independence:** Identity reused from inspected P02 source record; same Microsoft guidance family as P02-001 and G04-013. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.
