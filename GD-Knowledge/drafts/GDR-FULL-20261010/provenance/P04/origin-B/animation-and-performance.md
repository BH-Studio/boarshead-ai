---
id: GDR-CAND-20261010-P04-TOP-02
kind: topic
title: Animation and performance
version: 0.1.0
candidate_revision: initial-draft-1
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P04
attempt_id: P04-authoring-01
identity_scope: temporary-run-scoped
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- animation responsiveness
- expressive behavior
- animation transitions
tags:
- animation
- posing
- timing
- interruption
- performance
- input
- network-context
related_topics:
- GDR-CAND-20261010-P04-TOP-01
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-W01-TOP-03
- GDR-CAND-20261010-W02-TOP-01
related_patterns:
- GDR-CAND-20261010-P04-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P04-004
- GDR-SRC-20261010-P04-005
- GDR-SRC-20261010-P04-006
- GDR-SRC-20261010-P04-007
- GDR-SRC-20261010-P04-008
- GDR-SRC-20261010-P04-009
- GDR-SRC-20261010-P04-010
- GDR-SRC-20261010-P01-05
- GDR-SRC-20261010-P01-10
- GDR-SRC-20261010-P04-011
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial P04 submission; does not replace or resend any previous batch.
byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
---

# Animation and performance

**Draft 0.1.0; candidate revision initial-draft-1. Not released or independently reviewed for P04.** The strongest recommendation is to specify the action’s meaning, commitment and interruption behavior before treating a polished transition as successful interaction. This is a design **inference**, not a rule that responsiveness must always defeat expressive or physical commitment. [C-10]

## Decision and scope

**Decision:** How should posing, anticipation, timing, transitions and expressive behavior communicate an action while preserving the control, consequences and recovery opportunities the game intends?

*Animation* here concerns changing presented pose or form over time. *Performance* includes the interpreted behavior of a character or other expressive agent, not just animation-system speed. *Responsiveness* must identify its endpoint: acknowledged input, first noticeable pose change, effective movement, action eligibility, consequential event, or completed transition. These endpoints are not interchangeable. A *cancel* may stop visual playback, stop an action before commitment, leave an action after commitment, or reverse a consequence; the design must say which. These are analytic conventions for this draft, not an industry standard. [C-01]

The scope includes player-controlled and non-player actors, anticipation, posing, timing and spacing, blending, interruption/recovery, expressive beats, authored and selected motion, and conceptual platform/network constraints. It excludes implementing an engine controller, prescribing combat frame data, creating motion assets, casting or performance contracts, certifying accessibility, and equating an intended emotion with measured player response. [C-01, C-15]

### Reviewed guidance transferred and missing neighbors

Actual selected P02 `review-correction-1` bytes were inspected. Controls and input separates input receipt, qualification/buffering and action execution. Feedback and game feel separates acknowledgement, pending state, accepted action and confirmed outcome. Multimodal communication and the P01 corrected access work separate available information from emotional equivalence. These are retained candidate distinctions, not newly validated empirical results. [C-01, C-04]

W01 Character design and W02 Dialogue and voice were inspected for **intended characterization versus player interpretation** and the boundary between a selected contribution and its performed meaning. The selected W02 intent-and-response pattern, F07 legible-commitment pattern and G02 bounded-action-grace pattern were inspected for ownership overlap. P04’s new pattern owns **animation/action phase synchronization and exits**, not a new general consent pattern, dialogue-label pattern or input-grace recipe. Exact identities, revisions, hashes and locators are in the [dependency record](../reviews/full-run-20261010-p04-review-packet.md#inspected-dependency-transfers).

P03 camera/platform and F04 combat/traversal candidate bytes remain missing. No numerical comfort, latency, cancel-window, turn-rate, frame-rate or display setting is inherited from unseen work. Original P01 numerical-accessibility corrections remain intact; CSS pixels or rendered body height are not animation timings. [C-01, C-13]

**Assumptions for a later application:** actor/controller authority; whether the player controls that actor; action consequences; input method and chosen assistance; viewing angle, actor size and motion visibility; animation sample rate and playback rate; simulation and display timing; local or networked roles; permitted interruption; camera motion; language and performance context; relevant access needs. First-person, third-person, fixed-view, touch, controller and XR situations are not assumed equivalent. [C-01, C-10]

## Core explanation and mechanisms

### Anticipation is an option with a viewer and a purpose

Lasseter describes anticipation, staging, timing and follow-through as animation techniques for communicating action to a viewer; the same paper allows minimized anticipation for some slow actions. Its film examples do not establish a mandatory pre-action delay for a player-controlled action. [C-02]

**Bridge:** ask *who needs to predict what*. A non-player actor’s preparation may communicate an impending action. A player who just requested a routine action may already know the intention and instead need immediate acknowledgement. A performed gesture can prepare attention without postponing every consequential response. The correct choice depends on what information and commitment are intended; no single body pose, number of frames or preparation duration guarantees comprehension. [C-10, C-11]

Posing, timing and transitions should therefore be considered together. A distinctive key pose may be invisible from the actual view, crossed too quickly, hidden by another body part, or blurred by a blend. Conversely, a long held pose may be legible but falsely imply that the actor is still committed after control has returned. Those are testable failure mechanisms, not results observed in P04. [C-10, C-14]

### A narrow experiment challenges automatic naturalness benefits

Normoyle and Jörg studied 67 mostly-student participants using gamepad-controlled, third-person platform tasks with five controller variants; a shared Blend condition served two comparisons. A separate 12-person video study rated MoveTree most natural. In play, MoveTree took longer to reach goals than Switch/Blend; cape variation reduced enjoyment versus Blend. Trade-off enjoyment differences were not significant. Some satisfaction/control comparisons were only at the paper’s .1 level, not .05. Naturalness and gameplay motion-quality questions differed. [C-03]

These results support separating task outcomes from visual appraisal, not declaring “animation does not matter,” “never blend,” or a modern motion-matching system inferior. The older controller restricted switching during transitions and changed turning behavior. Its operational responsiveness includes visible request completion, not merely our local acknowledgement endpoint. No new milliseconds, effect-size estimate, equivalence claim or raw-data analysis is inferred. [C-03, C-04]

**Evidence-to-application bridge:** a transition can be aesthetically desirable while delaying a task-relevant event. Compare the actual action consequences and input history, not only a rendered clip. Conversely, deliberate physical commitment may be the intended decision cost; shortening it changes the task rather than simply polishing the same task. A local test must expose that distinction. [C-04, C-10, C-11]

### Engine transitions are mechanisms, not gameplay permission

Unity 6.3 documents transition duration, exit conditions and interruption ordering; duration can use seconds or a normalized source-state fraction. Those controls describe Animator behavior. They do not themselves specify whether an inventory transfer, collision event or other consequence should be undone. [C-05]

Epic’s root-motion documentation describes animation-driven displacement as an alternative to movement driving the visual layer. Its networked Character Movement documentation separately identifies responsibilities for coordinating root-motion animation through gameplay. A visually matching local transition does not establish consistent authority across participants. [C-06, C-07]

**Bridge:** a design record needs separate answers for movement authority, action eligibility, consequence authority and visual continuity. The same animation can remain useful under different control policies, but those policies are not interchangeable. A visual blend finishing is not automatic proof that an action succeeded; an interrupted clip is not proof that it did not. This is an inference from distinct facilities and the inspected P02 state distinctions, not a tested synchronization architecture. [C-01, C-10]

### Authored transitions and data-driven selection have different failure surfaces

Epic’s Motion Matching documentation selects poses using a database/schema rather than only a manually enumerated state graph. It documents repeated notify events from adjacent pose selections and limitations of trying to repair mismatched motion data through weights alone. These are concrete authoring/verification concerns, not a measured superiority claim. [C-08]

The implication is to evaluate the **coverage of the intended actions**, not choose a technique by its label. An authored system can make particular exits explicit but accumulate exceptions. A data-driven system can reuse a broad motion collection yet still require appropriate data, selection criteria, event handling and out-of-coverage behavior. These are conceptual work categories; this draft does not estimate asset volume, memory, runtime cost or staffing. [C-10]

### Expressive performance is interpretation, not a pose dictionary

Naughty Dog’s retrospective describes facial-capture work requiring a new rig/system and NPC traversal exits depending on AI/scripting coordination. It is an account of production dependencies, not evidence that captured performance automatically produces believable behavior or better control. [C-09]

For a prospective scene, write the **intended beat** and the **interpretation to investigate** separately. An agent pauses before returning an object: intended hesitation is not proof that players perceive reluctance, deception or concern. Ask what players thought was happening and why, while distinguishing that interpretation from the action’s literal result. Performance direction can permit ambiguity without changing what a player-controlled character agreed to do. [C-12]

A later localized performance review should examine gesture, posture, gaze, timing, speech and captions in their context. Do not assume that identical motion timing across languages preserves pragmatic meaning, or that a fluent back-translation validates a gesture. This is a proposed investigation and risk control; no cross-cultural performance study, gesture equivalence or legal conclusion is established here. [C-12, C-14]

### A recent production choice is not a universal capture policy

In the 2026 Play by Play interview, Laygo describes exaggerated hand-keyed poses/timing and a shared base animation set with selected character-specific additions. This is a contemporary production alternative to equating naturalism with motion capture or requiring every actor to have a unique set. It reports intention and reuse, not measured responsiveness, savings or superiority. [C-16]

## Design choices and alternatives

| Choice | Conditional use | Cost, countercase and alternative |
|---|---|---|
| Immediate effective action with a short or overlapping visual transition | The player’s task requires direct response and the animation need not impose a commitment. | Abrupt changes may undermine the intended physical behavior. Compare a selective transition without claiming all smoothness is harmful. [C-10, C-11] |
| Authored anticipation before consequence | Preparation communicates a relevant future action or is part of a disclosed commitment. | Repeating it for a routine command may add unwanted delay. Minimize or move preparation earlier when prediction is already available; verify semantics. [C-02, C-10] |
| Clip-led physical commitment | Positioning, weight, deliberate execution or a staged performance is the intended constraint. | Cancellation can change the decision structure. Preserve disclosed stakes while making control return and failure/recovery legible. [C-10] |
| Movement-led pose selection | Position and response policy must be independently controlled. | Visual feet, hands or props can cease to agree with the motion unless authored appropriately. Test rather than prescribe a particular correction technology. [C-06, C-10] |
| Selectively interruptible authored graph | A manageable set of actions has important, explicit exits. | Every extra transition adds cases to verify; interruption priority is not itself a gameplay cancellation policy. [C-05, C-10] |
| Motion-database selection | The production can supply and review motion covering the action space and its boundary cases. | Missing data, repeated events and query mismatch remain possible. A smaller authored solution may be easier to reason about for a limited task. [C-08, C-10] |
| Full-body expressive beat | The actor, view and attention opportunity can carry meaning through posture and gesture. | Repetition or interruption may change that meaning. Use a shorter acknowledgement, a deferred beat, or no performance when expression is unnecessary. [C-12] |
| Reduced secondary motion | Decorative motion competes with a task, player preference or comfort. | Do not remove the only essential state indicator. An alternative fact channel must be usable, not merely present. [C-13] |

## Application process

This is proposed design work, not an engine implementation recipe. [C-10, C-14]

1. **Diagnose the mismatch.** State whether the failure concerns identification, input acknowledgement, effective action, consequence prediction, recovery, expression or comfort. A dislike of a turn is not automatically input latency; a late consequence is not automatically a blending problem.
2. **Define the action phases and authorities.** Record request/trigger, acceptance or pending state, preparation, commitment, consequence, recovery and return of control as appropriate. Merge or omit phases when the action does not need them. Assign a conceptual owner to the actual consequence separately from its animation.
3. **Specify permitted exits.** At each phase, describe rejection, cancellation, interruption by another event, pause/re-entry and completion. State what is retained, consumed, refunded, repositioned or merely represented differently. “Interruptible” is too vague without these consequences.
4. **Choose the motion strategy.** Compare the simplest viable authored, blended, root-driven, movement-driven or selected-motion approach. Decide which poses and durations carry information and which are decorative. Preserve critical distinctions under the chosen access settings.
5. **Plan observation under real task conditions.** Record first visible acknowledgement, effective action and control return separately. Include transitions initiated from unusual states, repeated inputs, late cancellations and interrupted/repeated expressive beats. Add network roles and display conditions only when resourced, with no untested equivalence claim.
6. **Evaluate and revise.** Compare action understanding and errors with preference, perceived control, intended expression and comfort. Shorten or simplify when added performance has no relevant value; retain a deliberate commitment when it is part of the agreed task, not because the clip happens to be long.

### Example action-phase record

The following fields are an illustrative specification format, not approved engine data: current phase; true state; event that permits progression; what the player sees/hears/otherwise receives; which input or external event can interrupt; effect of interruption; next allowed action; persistence on pause/re-entry; network authority if applicable; and unresolved ambiguity. This extends P02’s feedback distinctions to the life of a motion. It does not create new buffering or input-remapping rules. [C-01, C-10]

## Patterns and genre adaptations

[Action-phase and interruption contract — GDR-CAND-20261010-P04-PAT-02](../patterns/action-phase-and-interruption-contract.md) gives an actionable recipe for synchronizing action meaning with animation phases and exits. [Role-preserving style variation](../patterns/role-preserving-style-variation.md) is relevant when costume or shape changes interact with motion identity; neither pattern independently validates the other.

Task-specific examples are not genre guidance. An actor observed for expression, an actor controlled for precise positioning, and an actor whose commitment must be predicted can warrant different timing choices in the same game. Do not choose a “winning” genre rule. Future combat/traversal and camera/platform reconciliation remains explicit. Additional localized expressive-beat work is queued, not delivered as a third pattern. [C-10–C-12]

## Examples and counterexamples

### Illustrative worked example — extracting a service module

**Invented, not implemented or tested.** A player commands an agent to remove a module. Before a latch releases, cancelling should leave the module installed. Once the module is transferred, stopping the flourish should not place it back merely because the animation was interrupted. [C-10, C-14]

| Phase | Actual proposed meaning | Presentation and exit |
|---|---|---|
| Request received | A command arrived; eligibility is not yet resolved. | A modest acknowledgement must not depict a completed transfer. Repeated requests are not assumed additional transfers. |
| Accepted / preparation | The module is available and the agent is preparing. | Reach/brace pose may communicate the pending action; cancellation returns to a valid pre-transfer state. |
| Commitment and transfer | The module’s location changes under the authoritative rule. | Presentation agrees with that event; a later visual exit cannot silently undo it. A separately designed undo would be a different action. |
| Recovery | Transfer is complete; the actor may still be settling or holding the module. | Specify which next actions are allowed; do not make a decorative settle determine undisclosed eligibility. |
| Denial / external interruption | Availability changed, a request was rejected, or another event took precedence. | Present the actual result and a valid next option, not a success pose followed by unexplained reversal. |

In a networked variation, a local request may remain pending until the relevant authority resolves it. The exact prediction/correction policy is outside this research; a purely visual solution is not assumed. In a cinematic-only variation, the player may not control the actor at all, so input acknowledgement is irrelevant. The phase vocabulary is optional, not a requirement to insert every phase into both situations. [C-01, C-07, C-10, C-14]

### Illustrative expressive countercase — an interrupted greeting

An agent begins a welcoming gesture when the player approaches, then must attend to a newly urgent task. Resuming the greeting from its old midpoint could suggest continued welcome after the context has changed. Candidate alternatives are to drop it, restart only if still meaningful, or finish with a context-valid acknowledgement. The intended tone, literal state and repeated-exposure response should be reviewed separately. No named game or psychological outcome is asserted. [C-12, C-14]

### Strongest opposing case

An action may deliberately commit the actor to a slow, readable movement whose cost is fundamental to planning. Allowing instant direction changes or cancelling after its consequence can make performance easier by changing that cost. Better completion time would not prove the original animation was inferior. Compare the intended decision and commitment, not a cosmetically similar but mechanically easier task. This countercase blocks a universal responsiveness-first recommendation. [C-10, C-11]

## Failure modes and constraints

| Warning sign to investigate | Possible cause | Proposed correction |
|---|---|---|
| The actor reacts immediately, but the requested action is still unavailable. | Acknowledgement confused with eligibility/effective action. | Separate the state presentations and measure the task-relevant endpoint. |
| The clip ends but the outcome is pending. | Visual completion incorrectly treated as authority. | Show a truthful pending/result transition; review action ownership. |
| Cancelling duplicates or reverses a consequence unexpectedly. | Exit handling follows clip position rather than action state. | Specify retained consequences and valid next states before adjusting blend polish. |
| A readable key pose disappears during transition. | The selected view/blend crosses it without enough task-relevant presentation. | Evaluate the moving sequence, not only reference poses; consider a different cue. |
| Repeated selections produce doubled footsteps or other events. | Animation event emission is not aligned with selected pose changes. | Investigate event identity and selection behavior; no timeout is prescribed. |
| A gesture reads differently after interruption or translation. | Timing/context changed its implication. | Re-evaluate the complete beat, not just the local pose or word. |
| Reduced-motion mode loses essential information. | A required fact was embedded only in decorative movement. | Supply and evaluate an appropriate alternative; keep mood equivalence unclaimed. |
| A natural turn passes clip review but harms task performance. | Review excluded control constraints or changed the endpoint measured. | Compare representative input/action sequences and separate enjoyment from completion. |

Failure interpretations and remedies are proposed, with the documented event-selection example limited to C-08. They are not P04 test results. [C-10–C-14]

**Accessibility and ethics:** respect chosen motion settings, pauses and withdrawal in later evaluation. The goal is not to prove one “normal” body, expression or input speed is ideal. A still body, unusual motion or disability-associated movement should not be treated as evidence of character morality. Asset/capture permission, performer attribution and adaptation rights need separate production review; no legal status is asserted. Proposed studies should not expose a person to effects they decline merely to obtain a comparable trial. [C-12–C-15]

**Production:** conceptual costs include action coverage, transition exceptions, rig compatibility, prop contact, selection/event behavior, alternative presentations, localization and maintenance after rule changes. No source supplies a universal cost advantage for hand-keying, motion capture, root motion, motion matching or more animation. Determine scope and compare local work only after authorization. [C-09, C-10]

## Playtest and validation

**PROPOSED — NOT PERFORMED.** No controller, actor, scene, capture, participant, network trace or frame-time measurement exists from P04. [C-14, C-15]

**Primary question:** Can players predict action state and permitted recovery, and does the chosen presentation support the intended task without unnecessary control or comfort failures?

**Conditions:** compare A, a whole-clip presentation with disclosed commitment; B, a phase-aware presentation with selectively permitted exits but the **same true commitment and consequences**; C, a simpler presentation. A/B is interpretable only when the mechanical contract is matched. A separate experiment may vary commitment itself, but then cannot attribute the result solely to animation. Do not deliberately make A unreadable to manufacture a benefit.

**Control and procedure:** use matched tasks, rules, assistance, input devices and camera views. Counterbalance sequence and action families where feasible. Test normal completion, pre-consequence cancellation, post-consequence exit, denial, repeated requests and external interruption. Include cases where the same-looking interruption has different correct retained consequences. Ask for a state prediction before asking what action a participant prefers; this retains the F01 corrected transfer distinction. Observe ordinary and repeated use separately. Record when a prediction question primes attention.

**Participants/context:** recruit a population justified by the later project, including relevant input/access needs and both unfamiliar and experienced users. Use preferred settings. Test cinematic interpretation with an audience task separately from controlled movement; do not combine ratings from those tasks into one score. A study owner must set sample size and analysis precision before collection; this source set does not supply a population guarantee.

**Measures:** distinguish true receipt, first perceived acknowledgement, first effective action, consequence time and control return; later technical instrumentation must define clocks and uncertainty. Pair observations with state/exit predictions, action errors, repeated inputs, perceived control, motion quality, expression interpretation and comfort. Ask about enjoyment separately. For performance beats, record open interpretations before forced labels, and compare first/repeated/interrupted presentations. Network roles, render/display conditions and alternative modalities require explicit analysis rather than silent pooling.

**Falsification and decisions:** reject a claim that B improves comprehension if apparent success occurs only on repeated answers or disappears on new valid action states. Revise when B misrepresents retained consequences, loses essential information, or reduces desired commitment rather than preserving it. Prefer a simpler alternative if the more elaborate presentation adds no decision-relevant value within the predeclared uncertainty tolerance. A nonsignificant result does not establish equivalence. Any critical action-state contradiction or participant stop request blocks advancement or ends the session as appropriate. Set tolerances, exclusions and stop procedures before execution; do not select them after favorable outcomes.

## Claim ledger

### C-01
**Claim:** Input receipt, action eligibility, visual acknowledgement, effective action, consequence and recovery require distinct definitions when they differ. **Class:** `inference`. **Support:** inspected P02 Controls/Feedback state distinctions; GDR-SRC-20261010-P04-005 introduction’s responsiveness definition; original P04 phase vocabulary. **Confidence:** moderate for analytic usefulness. **Limit:** not every action needs separate phases. **Unresolved:** operational endpoints for the actual task and authority model.

### C-02
**Claim:** Traditional animation anticipation/staging/timing are practitioner communication techniques, not guaranteed gameplay effects or mandatory delays. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-004, §§2.2–2.5, including the slow-action anticipation exception. **Confidence:** high for attribution, low for an untested interactive transfer. **Limit:** film/viewer examples; no timing numbers adopted. **Unresolved:** which preparation a particular player or observer needs.

### C-03
**Claim:** The inspected controller experiment challenges automatic player benefits from increased naturalness under its particular task/controllers. **Class:** `empirical-evidence`. **Support:** GDR-SRC-20261010-P04-005, §§3.2–3.4, 4.8, 5–6; sample, task and principal outcomes above. **Confidence:** moderate, narrow study. **Limits:** shared comparison group, different rating questions, older constrained controllers; .1-level findings not treated as .05-level findings; nulls not equivalence. **Unresolved:** effect estimates and transfer to other tasks, populations and modern systems.

### C-04
**Claim:** Evaluate visual appraisal and gameplay outcomes separately; a more favorable score on one need not justify the other. **Class:** `inference`. **Support:** C-03 and inspected P02 Feedback outcome separation. **Confidence:** moderate as a measurement safeguard. **Limit:** not a claim that visual quality is irrelevant. **Unresolved:** which outcomes should govern a later approved design decision.

### C-05
**Claim:** Unity 6.3 documents duration/exit/interruption controls for Animator transitions, not an automatic action-cancellation contract. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-006, Transition properties and Transition interruption. **Confidence:** high for documented scope. **Limit:** no engine verification or recommended settings. **Unresolved:** implementation-specific relation between action state and animation.

### C-06
**Claim:** Epic’s root-motion facility can use animation data to drive displacement, distinct from movement driving visual animation. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-007, Overview/Root Motion/Results, UE 5.8. **Confidence:** high for attribution. **Limit:** no universal selection rule or benchmark. **Unresolved:** desired movement authority and action coverage.

### C-07
**Claim:** Epic’s networked Character Movement root-motion workflow leaves animation coordination responsibilities to gameplay. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-008, root-motion special-case movement paragraphs. **Confidence:** high for scoped documentation. **Limit:** not a general multiplayer protocol or proof of synchronization. **Unresolved:** authority, prediction and correction behavior in a later implementation.

### C-08
**Claim:** Epic documents pose-search motion selection with event-duplication and data/weight mismatch concerns. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-009, Overview, Anim Notify Filtering and Channel Weights. **Confidence:** high for documentation. **Limit:** no default timeout/weight, quality guarantee or performance comparison extracted. **Unresolved:** actual motion coverage, event semantics and validation cost.

### C-09
**Claim:** The inspected Naughty Dog account identifies facial-rig/system and AI/traversal dependencies in expressive/locomotion production. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-010, UNCHARTED TERRITORY. **Confidence:** high for reported process. **Limit:** not measured response or causal proof of believability. **Unresolved:** applicable work and resources for another production.

### C-10
**Claim:** Specify action phases, authorities, permitted exits and retained consequences before choosing or polishing transitions. **Class:** `inference`. **Support:** C-01/C-04–C-09 and inspected candidate ownership boundaries; the evidence-to-application bridge is in Core explanation. **Confidence:** moderate as consistency guidance, low for unmeasured benefit. **Countercase:** some action commitment is intentional and must remain. **Unresolved:** minimum useful phase model and value relative to a simpler specification.

### C-11
**Claim:** A phase-aware presentation may preserve comprehension/control better than an unnecessarily clip-constrained alternative, without requiring all actions to be freely cancellable. **Class:** `hypothesis`. **Support:** C-03 is adjacent, not a direct test of this recipe. **Confidence:** low for a new application. **Limit:** changing commitment changes mechanics; cannot be called an animation-only improvement. **Unresolved:** matched local comparison and boundary conditions.

### C-12
**Claim:** Intended expressive beats, their interpretation and their interruption/localization behavior should be investigated separately from literal action consequences. **Class:** `hypothesis`. **Support:** C-02/C-09, inspected W01/W02 distinctions and original P04 scenarios. **Confidence:** low for a particular interpretation. **Limit:** no culture-wide pose dictionary or expressive-equivalence study. **Unresolved:** language, performer, audience, view and repeat-exposure effects.

### C-13
**Claim:** Important animation-carried facts require appropriate access alternatives; optional motion controls do not imply removal of essential gameplay. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-05 and P01-10, freshly inspected implementation guidance. **Confidence:** high for attribution; usability untested. **Limit:** vendor guidance, not formal certification, safe-motion thresholds or emotional parity. **Unresolved:** actual alternative-route comprehension and comfort.

### C-14
**Claim:** Recipes, scenarios, measures and disconfirmation rules in this entry are proposed and unperformed. **Class:** `hypothesis`. **Support:** original P04 synthesis; F01’s selected transfer-discrimination correction constrains the proposed tests, not their results. **Confidence:** low for eventual usefulness. **Limit:** no prototype, participant or technical data. **Unresolved:** authorized study design, thresholds, sampling and feasibility.

### C-15
**Claim:** Doug’s dispatch authorizes bounded research and draft P04 artifacts only. **Class:** `studio-decision`. **Owner/date:** Doug, supplied P04 brief, 2026-10-10, Authorization Update/Assigned Outputs/boundaries. **Confidence:** high for explicit scope. **Limit:** no implementation, release, participant work, permanent IDs or Project changes. **Unresolved:** independent review and subsequent coordination decisions.

### C-16
**Claim:** A recent creator describes hand-keyed timing/posing and shared base animations with selective individual variation. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-011, Laygo animation answer. **Confidence:** high for attribution. **Limit:** pre-beta creator interview, not a tested current build, population response or cost benchmark. **Unresolved:** appropriate reuse, retargeting and identity for another production.

## References

All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.

### GDR-SRC-20261010-P04-004

**John Lasseter. [Principles of Traditional Animation Applied to 3D Computer Animation](https://www.cs.utexas.edu/~fussell/courses/cs384g-fall2011/projects/animator/lasseter.pdf).** ACM Computer Graphics 21(4), SIGGRAPH 1987, pp. 35–44. Date: 1987-07. Edition/build: Original paper; University of Texas course-hosted copy.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Practitioner exposition with film examples. **Locators:** §2.2 Timing, printed p. 37; §§2.3–2.4 Anticipation/Staging, pp. 38–39; §2.5 Follow Through and Overlapping Action, p. 39. **Supports:** C-02; indirect C-10/C-12.

**Limits:** Viewer-directed animation, not an interactive performance experiment. PDF text inspected; screenshot route failed. Historical anatomy/absolute claims and frame recipes not adopted. **Relationship:** Synthesizes earlier animation practice; those cited books were not independently inspected. **Rights:** Copyrighted paper; paraphrase only; no frames or figures redistributed.

### GDR-SRC-20261010-P04-005

**Aline Normoyle and Sophie Jörg. [Trade-offs between Responsiveness and Naturalness for Player Characters](https://alinen.net/research/normoyle14Tradeoffs.pdf).** ACM, Motion in Games 2014. Date: 2014-11-06–08, conference dates. Edition/build: MIG 2014 paper; DOI 10.1145/2668064.2668087.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original game-controller experiment and separate video-rating calibration. **Locators:** §§3.2–3.4, PDF p. 4; §4.8, pp. 6–7; §§5.1–5.5, pp. 7–9; §6, p. 9. **Supports:** C-03; indirect C-04/C-11.

**Limits:** One old controller/task family; relevant PDF prose inspected. Screenshots and local download failed; no graph digitization, table-only result or raw-data reanalysis used. **Relationship:** Shared Blend group in two comparisons is not an independent replication; later journal extension not inspected. **Rights:** ACM copyright notice; paraphrase only; source PDF not redistributed.

### GDR-SRC-20261010-P04-006

**Unity Technologies. [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html).** Unity Manual. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unity 6.3 LTS (6000.3).

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Transition properties (Fixed Duration, Transition Duration, Has Exit Time); Transition interruption; Interruption Source; Ordered Interruption. **Supports:** C-05; indirect C-10.

**Limits:** Describes Animator transitions, not input buffering or automatic cancellation of gameplay consequences. No engine execution. **Relationship:** Independent vendor from Epic; two implementations are not evidence of better player outcomes. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-007

**Epic Games. [Root Motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation; 5.6 route also inspected but not source of current-version claims.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Overview; Root Bone; Root Motion; Enabling Root Motion; Results. **Supports:** C-06; indirect C-10.

**Limits:** One movement/animation facility; neither a universal motion authority rule nor an implemented benchmark. **Relationship:** Same Epic documentation family as networked movement and motion matching. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-008

**Epic Games. [Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Network roles/movement cycle; Replicating Special Case Movement with Root Motion; root-motion montage and Gameplay Ability System paragraphs (web extraction lines 194–218). **Supports:** C-07; indirect C-10.

**Limits:** Character Movement workflow only; no general netcode guarantee, latency target or local synchronization test. **Relationship:** Same issuer and feature family as root motion, not a separate efficacy study. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-009

**Epic Games. [Motion Matching](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-matching-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Overview and Pose Search schema; Anim Notify Filtering; Pose Search Schema Channel Weights (web extraction lines 310–337). **Supports:** C-08; indirect C-10.

**Limits:** Documented selection system and failure cases; no quality/cost/speed benchmark or recommended weights/timeouts. **Relationship:** Same Epic family; source demonstrations not played as independent observations. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-010

**Dinah Bakeer; accounts by Marianne Hayden and Almudena Soria. [Uncharted 4: A Thief’s End: The 5-Year Anniversary Retrospective](https://www.naughtydog.com/blog/uncharted_4_a_thiefs_end_the_5_year_anniversary_retrospective).** Naughty Dog. Date: 2021-05-10. Edition/build: Retrospective on original PlayStation 4 production; engine/build number unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator retrospective. **Locators:** UNCHARTED TERRITORY, Hayden facial-capture and Soria traversal/AI paragraphs (web extraction lines 17–31). **Supports:** C-09; production context C-10/C-12.

**Limits:** Production account, not measured interpretation, responsiveness or staffing savings; no gameplay footage inspected. **Relationship:** Independent production from Valve/Riot, with similar retrospective selection bias. **Rights:** Reuse license not established; paraphrase only.

### GDR-SRC-20261010-P01-05

**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-13.

**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P01-10

**Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Overview; Implementation guidelines; Moving/blinking/scrolling content and essential-gameplay exceptions; Camera movement options. **Supports:** C-13.

**Limits:** No safe-motion numerical threshold or blanket removal of all gameplay animation; not certification. **Relationship:** Reuses P01-10; P02-010 duplicates this URL. Same issuer as XAG 103, not independent player evidence. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-011

**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-beta creator interview; Unreal Engine 5, minor/build unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator interview. **Locators:** Questions about stylized likeness and character animation; Johnston/Laygo answers, web extraction lines 57–67. **Supports:** C-16, animation portion only.

**Limits:** Design intentions and reported reuse, not measured responsiveness, audience response, savings or a current release-status claim. **Relationship:** Separate production from Valve/Riot/Naughty Dog; hosted by its engine vendor, with promotional incentives. **Rights:** Reuse license not established; paraphrase only; no media redistributed.

## Open questions and change history

| Subtopic | Inspected coverage | Remaining question/dependency |
|---|---|---|
| Anticipation, posing and timing | Original practitioner account and recent hand-keyed production rationale. | Which actor/viewer needs prediction, and when is preparation redundant? |
| Responsiveness versus naturalness | One older game-controller experiment plus separate video calibration. | Matched-commitment comparison with modern controllers and target populations. |
| Blending, exit timing and interruption | Current Unity documentation and phase-consistency synthesis. | Does the actual action remain true through every permitted exit? |
| Root/movement authority and network context | Current Epic documentation; no implementation or traces. | Reconcile action, movement, prediction and visual completion with an authorized system design. |
| Motion selection and transitions | Current motion-matching facility/failure documentation. | Out-of-coverage states, event semantics and actual production/runtime cost. |
| Expressive behavior and performance | Creator dependencies and inspected W01/W02 distinctions. | Direct interpretation evidence across locale, retargeted bodies, interrupted/repeated beats and small views. |
| Access and sensory comfort | Current scoped XAG guidance; no safe numerical setting. | Essential-fact preservation with actual users and chosen settings; P03 bytes still missing. |
| Combat/traversal-specific commitment | Logical countercases only, not F04 guidance. | Inspect F04 before asserting mechanical defaults or genre-sensitive cancel policies. |

P04-CON-03/04/05/06 remain open in the packet. The localized-expression extension is queued as child work, not a third pattern or completed evidence. No inference of whole-heading completion follows from this file existing.

**History:** 2026-10-10, version 0.1.0 / initial-draft-1; first P04 submission; predecessor/supersession null. Late creator-source inspection added C-16 without reallocating existing claims. Author self-review is not independent review. Gates C, D and E remain unpassed for this candidate. See the [review packet](../reviews/full-run-20261010-p04-review-packet.md) and [integrity receipt](../reviews/full-run-20261010-p04-integrity-receipt.md).
