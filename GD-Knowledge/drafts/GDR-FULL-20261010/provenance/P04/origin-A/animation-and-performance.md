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
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; run identifier retains dispatch date 2026-10-10
identity_scope: run-scoped candidate; permanent allocation pending
predecessor_sha256: null
supersedes: null
change_summary: Initial P04 candidate; no predecessor submitted.
aliases:
- animation responsiveness
- animation interruption
- expressive motion
tags:
- animation
- performance
- posing
- timing
- interruption
- recovery
- accessibility
related_topics:
- GDR-CAND-20261010-P04-TOP-01
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
related_patterns:
- GDR-CAND-20261010-P04-PAT-02
- GDR-CAND-20261010-P04-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P04-003
- GDR-SRC-20261010-P04-004
- GDR-SRC-20261010-P04-005
- GDR-SRC-20261010-P04-006
- GDR-SRC-20261010-P04-007
- GDR-SRC-20261010-P04-008
- GDR-SRC-20261010-P04-009
- GDR-SRC-20261010-P04-010
- GDR-SRC-20261010-P04-011
reviewer: null
approved_by: null
approved_date: null
---

# Animation and performance

**Draft 0.1.0, initial-draft-1 — not released or implemented.** Animation quality, control responsiveness, expressive interpretation and task performance are separate questions. The inspected evidence supports conditional design choices and specific documented mechanisms, not a universal anticipation duration, cancel window or rule that realism always improves play. [C-01–C-09, C-16]

## Decision and scope

**Decision:** How should posing, preparation, timing, transitions and expressive behavior communicate an action or character while preserving the control, commitment and recovery that the task actually promises?

This entry covers character/object animation and performed visual behavior, including anticipation, timing, posing, transitions, responsiveness, expression, interruption and recovery. “Performance” includes expressive delivery; it does not imply a frame-rate benchmark. The topic remains engine-neutral. Unity and Unreal documentation supply bounded examples of mechanisms, not an implementation choice or code package. [C-01, C-07–C-09, C-12]

Excluded: complete combat/traversal rules, camera tuning, rig construction, a motion-capture production manual, network architecture, lip-sync implementation, character canon, performer contracts, assets, participant experiments and certification. P03 camera/platform and F04 combat/traversal remain missing active/queued dependencies; their absence prevents final action-specific settings or authoritative movement policies. [C-15, C-16]

### Working distinctions

These definitions are proposed analytic tools, not a formal state-machine standard. [C-01, C-10, C-15]

| Term | Meaning used here | Boundary to preserve |
| --- | --- | --- |
| Pose / staging | A configuration and presentation that emphasizes a relevant action or interpretation. | A strong pose can be hidden by the view or interpreted differently. |
| Anticipation | Visible preparation, an advance communicative cue, or both. | It need not be delay after a player’s request; the cue can precede a decision. |
| Timing / spacing | When meaningful poses and events occur, and how motion progresses between them. | Total clip length alone does not specify the temporal experience. |
| Commitment | A gameplay rule limiting what can change after a point or condition. | Not necessarily the same as waiting for an animation to finish. |
| Cancel window | A locally defined interval or condition allowing an action to be replaced or ended. | A blending feature does not create that permission. |
| Buffer | A request retained for possible later eligibility. | It is not acceptance, completion or a promise to execute after context changes. |
| Blend / handoff | Presentation changes from one pose/motion state toward another. | Smooth interpolation is not evidence that the game state is correct. |
| Recovery | A period or condition governing the next action and/or settling motion. | Mechanical unavailability and cosmetic follow-through can end at different times. |
| Expressive reading | A player’s interpretation of intention, effort, attitude or feeling. | It is not the author’s intention or a diagnosis of a real person. |

### Application assumptions

Declare the actor’s role, task, input, display/view, local or networked authority, ability to pause, relevant access settings and audience familiarity. A player-controlled action, an observed agent and a noninteractive performance have different control obligations. A reversible starting context for the proposed evaluation is flat-display play with familiar controls; findings would not automatically transfer to VR body motion, remote spectators, switch input or every display. No hardware, timing or numerical comfort settings are assumed. [C-01, C-09–C-15]

## Core explanation and mechanisms

### Preparation can inform without making every action wait

Craft vocabulary provides ways to examine attention, apparent effort and continuity; C-02 records its evidence class. P04’s inference is to ask what each preparatory beat is for. It may inform an observer, establish a character intention, acknowledge the player or represent a deliberately committed action. These functions should not be conflated with technical delay. A brief response that only acknowledges a request must not falsely communicate a completed effect. [C-01, C-02, C-10]

**Proposed mechanism:** a visible state matches the relevant action promise → the player interprets the available choices → execution or recovery behaves accordingly → perceived control or impact may improve. The first relation can be audited in a specification; interpretation and experience still require evaluation. Immediate movement can feel wrong when the task is about deliberate commitment, just as extended preparation can feel wrong when the task promises prompt correction. [C-10, C-11, C-15]

### Naturalness and responsiveness do not collapse into one quality score

The empirical results and their reporting limitations are retained in C-04–C-06. They justify separating outcomes, not optimizing every game toward a single controller. A participant’s “easy to control,” an observer’s “natural,” a director’s “expressive,” and a logged success rate are not interchangeable measures. Adding a trailing garment or fuller turn can alter more than visual polish; removing motion can also remove intention, identity or action information. [C-04–C-06, C-12, C-14]

The decision is therefore conditional: retain the expressive beat when its value warrants the control and authoring consequences; decouple optional settling when it falsely implies a lock; or use a simpler transition when the task needs an unambiguous state change. None of these is established as a universal improvement. [C-10–C-12]

### Interruption is an action policy and a presentation problem

Write two separate records: **what the game permits** and **how that change becomes visible**. A controller might accept a cancellation while the old pose persists; another might blend beautifully to an action that was never accepted. Both can miscommunicate. Unity’s documented timing/ordering facilities and Unreal’s source-evaluation behavior make this separation concrete; they do not resolve a game’s policy. [C-07, C-08, C-11]

For each permitted handoff, identify which promises survive: movement/contact, target, completion, tool ownership, visible active state and permission for the next input. Identify which must stop. Do not leave an essential state change dependent on a presentation event that the chosen transition may discard. Equally, do not transfer an old action’s success effect to a replacement merely to preserve visual continuity. These are failure-prevention inferences, not engine changes performed here. [C-08, C-11]

### Networked presentation adds another distinction

An actor’s displayed preparation, predicted local response and accepted remote outcome may differ. The component-specific documentation in C-09 establishes that animation agreement is not something to assume blindly. P04 proposes labeling a pending state honestly and checking how correction appears to the owner and observers. It does not prescribe prediction, rollback, smoothing values or a networked combat model. Those decisions need the missing system/platform work and an implementation review. [C-09, C-11, C-15]

### Expressive behavior is contextual

A held gaze, rapid turn or restrained gesture might suggest concentration, discomfort, determination or something else. A plausible performance does not establish a single psychological reading. Establish what may remain interpretively open and what the task requires the player to know. Expression can be intentionally deceptive or ambiguous while action availability remains clear. Review posture, costume, voice/text context and viewing distance together rather than treating an emotion label on a clip as measured communication. [C-06, C-12, C-14]

## Design choices and alternatives

These options are conceptual design alternatives; they do not assert equal cost or universal engine behavior. [C-10–C-15]

| Choice | Appropriate context | Cost, failure risk and alternative |
| --- | --- | --- |
| Authored committed motion | The action deliberately includes a nonreversible or constrained phase. | May discard corrective intent or obscure the next available action. Communicate commitment and recovery; compare a clearer but equally committed presentation. |
| Interruptible authored motion | The task promises timely redirection. | Requires destination coverage, contact/trajectory repair and event ownership. A clear short handoff can be preferable to an elaborate blend. |
| Cosmetic follow-through after readiness | Settling or expressive motion should continue after control returns. | The old pose may imply the action is still locked. Separate readiness information and test conflicting inputs. |
| Captured performance | Nuanced human delivery or an existing capture pipeline suits the project. | Selection, editing, retargeting and adaptation remain work. No evidence here establishes universal naturalness or lower total cost. |
| Procedural or responsive adaptation | Many target, terrain or pose contexts exceed a small authored set. | Behavioral range and failure modes need testing; plausibility is not semantic correctness. Restrict adaptation when identity, contact or explicit staging matters more. |
| Hybrid layers | Some parts of behavior must adapt while others preserve an authored read. | Conflicting layers can erase a pose or imply a contradictory intention. Fewer layers or explicit state-specific poses remain valid alternatives. |
| Minimal transition / no extra ornament | The changed state is already clear or repeated motion distracts. | May remove expression or a needed cue. Preserve essential facts; do not present motion removal as universally better. |

### Motion ownership, not a preferred engine

A later design should state whether displacement is primarily chosen by gameplay, authored in motion, or coordinated between them, and who resolves disagreement. The relevant question is how to preserve the allowed path/contact and visible action under interruptions, scaling and corrections. P04 does not benchmark root motion against in-place motion, prescribe either, or supply integration instructions. No universal choice follows from the documentation examples. [C-07–C-09, C-11, C-12]

## Application process

**Proposed — not performed.** [C-15]

1. **Diagnose the complaint.** Ask whether the problem is missing acknowledgement, unexpected commitment, poor state legibility, unwanted motion, weak expression or a true technical delay. Do not treat all reports of “floaty” as the same issue.
2. **Specify the action contract.** Record eligibility, acceptance, commitment, result and recovery only where meaningful. Identify legitimate cancellation and buffering conditions, target validity and what the player can know. Mechanical policy belongs to the system owner.
3. **Sketch meaningful poses and beats conceptually.** Identify the required preparation, active state and exit/readiness. Name the intended expressive reading and plausible alternatives. Do not set universal frame counts or insist that each state needs a separate clip.
4. **Audit handoffs.** For each permitted interruption, record what stops, what survives, what the destination must show and which events must still occur exactly once. Include denial, pause/resume, target loss and state changes during a transition.
5. **Choose the least complex adequate motion treatment.** Compare a committed clip, an interruptible/hybrid version and a clear simpler handoff without secretly changing the action’s balance. Record when changing policy is itself the intended experiment.
6. **Plan access and localization with the performance.** Identify nonessential repeated motion, essential gesture/state information, voice/text dependencies and alternative routes. Do not assume a reduced-motion variant communicates the same emotion or that a translated line fits identical mouth/gesture timing.
7. **Evaluate and retain only the supported scope.** Separate prediction of permission, recognition of actual state, control experience, expression, comfort and production work. A smooth transition that hides denial is a failure even when liked; a deliberately abrupt transition can be appropriate when clarity is the priority.

The detailed interruption recipe is [State-aligned animation handoff](../patterns/state-aligned-animation-handoff.md). This process creates a reviewable design proposal, not an authorized implementation specification. [C-11, C-15, C-16]

## Patterns and genre adaptations

`GDR-CAND-20261010-P04-PAT-02` owns state-aligned motion transfer. [Recognition-preserving style variation](../patterns/recognition-preserving-style-variation.md), `GDR-CAND-20261010-P04-PAT-01`, is relevant when poses, accessories or gesture families help identify the same entity across variants. [Art direction](art-direction.md) owns the shared visual system rather than the control policy.

The [reviewed dependency record](../reviews/full-run-20261010-p04-review-packet.md#reviewed-dependency-transfer) identifies P02’s action semantics and fact-preserving presentation, P01’s readability/access boundaries, F01’s corrected discrimination test and W01/W02’s limited ownership transfer. Old “unavailable here” sentences inside those candidates describe their original authoring sessions, not P04’s actual access. P04 does not republish those files.

No genre file or gameplay timing rule is created. A situation rewarding deliberate commitment and one rewarding continuous correction can legitimately need different handoffs. Resolve that task-level conflict explicitly; a genre label alone does not decide it. [C-10, C-15]

## Examples and counterexamples

### Creator-reported case

C-03 records a production tension between expressive posing and alignment with a fixed gameplay volume. It is a reported design rationale and problem account, not observed gameplay or a measured improvement. The study boundary cases in C-04–C-06 remain separate from that creator intent. [C-03–C-06]

### Illustrative worked example — interrupted inspection

**Synthetic; no assets or prototype.** A player directs a character to inspect a panel. The task permits turning away before inspection commits. After commitment, the inspection must finish or enter an explicit cancellation outcome; merely releasing a button is not assumed to undo it. [C-15]

Record the distinction between “request received,” “moving to inspect,” “inspection committed,” “result available” and “ready for another action.” Some can share a pose, but their meaning must not be silently collapsed. An early turn-away should lead to a destination pose that no longer implies active inspection. A post-commit turn request may be denied or queued according to the future game’s policy; its animation cannot falsely imply that cancellation succeeded. [C-01, C-10, C-11, C-15]

If the handoff stops evaluating the old motion, the required result must still have an explicitly assigned owner rather than depending on a clip event that might no longer arrive. A trailing hand movement can continue after readiness only when it does not imply the tool is still locked to the panel. Compare against a neutral, simpler handoff and a fully committed presentation with the same action rules. Test cases must include both permitted and denied redirection, not repeatedly reward “cancel immediately.” [C-08, C-11, C-15]

### Illustrative worked example — expressive waiting

A noncontrolled character waits beside a doorway while a player reads an optional message. The intended performance suggests impatience, but the action contract permits waiting without penalty. A repetitive large gesture may compete with reading or imply a hidden deadline. Test a quieter pose, optional motion reduction and clarification of timing; do not conclude that all idle animation is harmful. Measure interpretations such as “waiting,” “angry,” “hurried” and “uncertain” without forcing the intended label. This is a hypothetical communication problem, not an observed audience result. [C-13–C-15]

### Strong counterexample — commitment is the point

A task deliberately requires committing to a weighted action and choosing when to begin. Making every frame cancellable would change the decision, not merely improve the animation. Preserve the intended commitment and make its onset/recovery legible; compare presentation changes separately from mechanical generosity. A spectator-only performance also has no obligation to echo nonexistent controller intent. These countercases defeat a universal “instant response above all” prescription. [C-05, C-10–C-12, C-15]

## Failure modes and constraints

| Observable sign in a later evaluation | Possible cause | Proposed correction or stop |
| --- | --- | --- |
| Players repeat inputs after an accepted action. | Receipt or current eligibility is unclear. | Distinguish acknowledgement from success; inspect the timing path rather than just increasing motion amplitude. |
| The destination pose looks active but the action was denied. | Presentation outran gameplay permission. | Correct the state-to-motion relation; do not reward the attempted action with a success cue. |
| Completion disappears or occurs twice after interruption. | State ownership depended on clip evaluation or duplicated transition events. | Block progression of that version until a separately authorized design resolves ownership. |
| Smooth transition, wrong contact or target. | Interpolation retained a pose without its semantic/physical conditions. | Use an explicit release/reacquire or simpler handoff; do not conceal the mismatch with blur. |
| A costume change obscures a state or shifts the apparent body away from allowed interaction. | Accessory or expressive movement conflicts with the gameplay read. | Review combined model/motion/view; allow justified variation limits. |
| Players call the motion natural but control frustrating. | Different outcomes have been merged. | Report them separately and compare mechanical policy independently. |
| Reduced-motion mode hides the only readiness cue. | Optional presentation carried essential information. | Preserve a usable fact route and reevaluate, without promising equal emotion. |
| One cultural or bodily style is treated as the only believable performance. | Narrow references or instruments enforce a stereotype. | Revise direction and interpretation questions; seek appropriately scoped review. |

These are proposed diagnostic hypotheses, not failures measured by P04. [C-10–C-15]

**Accessibility and sensory context:** XAG guidance supports examining nonessential motion and alternative critical information; its exceptions matter. Do not turn this into a blanket requirement to freeze every character or a certification claim. Consider users reading captions or narration, users who prefer reduced motion, and people whose input pace differs. A task-critical gesture needs an appropriate accessible route, not simply a duplicate decorative pulse. P01’s CSS/text/platform distinctions remain intact. [C-13]

**Expression and localization:** translated speech can change the timing and interpretation of a gesture. Facial movement, gaze and bodily manner should not be assumed to diagnose feeling or honesty. Record intended subtext, legitimate alternatives and task facts separately. Sign-language performance, detailed facial localization and broad cross-cultural interpretation are coverage gaps; they are not solved by this draft’s generic procedure. [C-14, C-15]

**Production constraints:** budget conceptually for transitions, outfit/prop interactions, retargeting, contact correction, event ownership and exceptional states, not just clip count. The evidence does not provide a universal cost saving from motion capture, procedural animation or shared rigs. Performer/reference consent and reuse rights require the relevant human/rights process; this is neither legal advice nor permission to reuse a likeness. [C-12, C-14, C-16]

## Playtest and validation

**PROPOSED — NOT RUN.** No prototype, participant work, frame-time measurement, controller instrumentation or network test occurred. [C-15, C-16]

**Question:** Does a proposed animation handoff communicate actual permission and recovery while providing a worthwhile expressive benefit over a simpler alternative?

**Comparisons:** A, existing committed presentation; B, state-aligned handoff under the same mechanical permission rules; C, clear minimal handoff. Where the intended experiment changes cancellation policy, make it a separately labeled factor rather than attributing all effects to animation. Keep task, actual outcomes, view and target conditions comparable. Test local authority first only when that is the chosen scope; a separate later owner/observer network comparison cannot be inferred from it.

**Procedure and participants:** include practiced and unfamiliar users and actual users of relevant access/input settings. Choose sample and precision based on the local decision, not a stock count. Collect permission/state predictions before feedback across eligible, ineligible, target-lost, pending and recovery conditions. Include interrupted transitions and repeated exposure. Counterbalance presentation order and avoid training every participant to respond the same way before the comparison.

**Measures:** mistaken acceptance/cancellation beliefs, premature re-inputs, missed or duplicated outcomes, task errors and recovery choices; separately, perceived controllability, intended-expression interpretations, comfort and willingness to retain the presentation. Report actual elapsed response only after a measurement method distinguishes input acquisition, recognized request, accepted state, visible change and display presentation. No universal timing threshold follows from the cited studies.

**Falsifying decisions:** reject a version that presents a denied action as accepted, loses/duplicates an essential result, or removes necessary information under a supported access route. Reject the proposed explanatory mechanism when an apparent benefit disappears after controlling changed mechanical permissions or when viewers cannot distinguish the intended state. Where the richer presentation adds no credible local value and costs more, prefer the simpler one without claiming statistical equivalence. Preserve intentional commitment when that is the task’s approved premise. Any discomfort or withdrawal request stops that session; tolerability is not inferred from an average rating.

The future study owner must predeclare practical decision criteria, sample rationale, exposure and analysis before execution. Unknown variance or an unrepresented population means limited conclusions, not automatic success. [C-10–C-15]

## Claim ledger

Claim IDs are local to this entry. Confidence describes the exact scoped wording, not a source’s prestige or the recipe’s overall efficacy. Proposed procedures and examples are not approved studio decisions.

### C-01

**Claim:** Separate action receipt, gameplay permission, commitment, visible preparation, result and recovery when diagnosing animation-related control problems. **Class:** `inference`. **Confidence:** moderate as an analytic decomposition, not a required number of states.

**Support / precise locator:** Reviewed P02 controls-and-input, Timing path; feedback-and-game-feel, Action receipt versus outcome; GDR-SRC-20261010-P04-007, transition properties.

**Applicability, contrary evidence and unresolved question:** Use only meaningful distinctions for the action. “Performance” here includes expressive delivery, not a promised CPU/frame-time benchmark.

### C-02

**Claim:** Timing, anticipation, staging and follow-through are craft concepts in Lasseter’s account, not demonstrated universal gameplay requirements. **Class:** `practitioner-heuristic`. **Confidence:** high for this boundary of the inspected source.

**Support / precise locator:** GDR-SRC-20261010-P04-006, §2.2–2.5, printed pp.37–39.

**Applicability, contrary evidence and unresolved question:** Historical animation argument and examples, not controlled interactive timing evidence. Do not import its frame anecdotes as control delays or call every action mandatory anticipation.

### C-03

**Claim:** Riot reports changing Lee Sin’s pose timing/spacing for intended impact and constraining cosmetic motion relative to his fixed hitbox. **Class:** `practitioner-heuristic`. **Confidence:** moderate for production attribution, not measured response.

**Support / precise locator:** GDR-SRC-20261010-P04-003, Animation → Making Lee’s Animations More Impactful; Float like a Butterfly, Sliding Hitboxes like a Lee.

**Applicability, contrary evidence and unresolved question:** No before/after participant data or direct footage observation here. “More satisfying” remains intended/reported, not a measured P04 finding.

### C-04

**Claim:** In the inspected controller study, MoveTree received lower ease-of-control ratings than Switch, and Cape lower enjoyment than Blend. **Class:** `empirical-evidence`. **Confidence:** moderate within the restricted experiment.

**Support / precise locator:** GDR-SRC-20261010-P04-005, §3.3–3.4 and §5.1–5.2: 84 recruited, 78 analyzed after six exclusions; between-controller play across three levels; reported controller omnibus tests p<.05, with the named post-hoc differences.

**Applicability, contrary evidence and unresolved question:** Predominantly student sample and restricted controller choices. No significant enjoyment effect in the responsiveness-tradeoff comparison; this is not equivalence. It does not justify “always prioritize responsiveness” or removing all embellishment.

### C-05

**Claim:** Withhold a directional performance claim from the author manuscript’s internally inconsistent lives-lost discussion; its satisfaction claim also uses a weaker stated significance threshold. **Class:** `inference`. **Confidence:** high that the inspected text requires this qualification.

**Support / precise locator:** GDR-SRC-20261010-P04-005, §5.3–5.4, manuscript pp.26–28; §6, pp.31–33; P04-CON-04.

**Applicability, contrary evidence and unresolved question:** §5.4’s fewer-lives comparison conflicts with its more-lives summary; §5.3 reports p<.1. Do not silently correct wording, upgrade certainty or treat null results as equality. Published full-text/author clarification remains missing.

### C-06

**Claim:** In a separate brief-viewing experiment, half-face freezing was unpleasant, while a static-eye manipulation did not significantly differ from the unaltered condition. **Class:** `empirical-evidence`. **Confidence:** moderate for the narrow stimuli.

**Support / precise locator:** GDR-SRC-20261010-P04-004, §5.2–5.2.1: 12 viewers, five render styles and manipulated male-character motion.

**Applicability, contrary evidence and unresolved question:** Little horizontal head movement limits the static-eye comparison. No evidence that eyes are unimportant or any expression is universally interpreted; no gameplay or live-performance task.

### C-07

**Claim:** The Unity 6000.3 manual distinguishes exit-time conditions, duration units and interruption ordering. **Class:** `observed-example`. **Confidence:** high for the inspected documentation artifact, not runtime validation.

**Support / precise locator:** GDR-SRC-20261010-P04-007, Properties and Transition interruption.

**Applicability, contrary evidence and unresolved question:** Seconds and normalized portions are distinct. A transition facility is not gameplay cancellation permission, a measured latency or an instruction to use Unity.

### C-08

**Claim:** UE 5.6 inertialization documentation states that the source stops being evaluated and its Animation Notifies stop after blending begins. **Class:** `observed-example`. **Confidence:** high for documented behavior, not execution.

**Support / precise locator:** GDR-SRC-20261010-P04-008, Inertialization, source evaluation and Animation Notifies paragraphs.

**Applicability, contrary evidence and unresolved question:** Important completion information must not be assumed to arrive from a discarded source clip. That design consequence is an inference; exact runtime ownership needs separate implementation review.

### C-09

**Claim:** UE 5.6 documentation distinguishes network smoothing and root-motion replication and states that matching animation playback is not automatically verified between server and autonomous client. **Class:** `observed-example`. **Confidence:** high for the stated component documentation.

**Support / precise locator:** GDR-SRC-20261010-P04-009, Network Smoothing; Replicating Special Case Movement with Root Motion → From AnimMontages.

**Applicability, contrary evidence and unresolved question:** Not all networking models behave this way. Do not infer a universal prediction strategy, acceptable latency or competitive fairness result.

### C-10

**Claim:** Keep expressive preparation and gameplay commitment negotiable separately; immediate acknowledgement need not imply immediate action success. **Class:** `inference`. **Confidence:** moderate for the semantic argument; experienced benefit remains local.

**Support / precise locator:** GDR-SRC-20261010-P04-006, Anticipation; GDR-SRC-20261010-P04-007, transition conditions; reviewed P02 feedback timing and receipt/outcome distinction.

**Applicability, contrary evidence and unresolved question:** An intentionally committed action is a valid countercase. Opponent warning may precede the player’s opportunity to respond. No fixed anticipation or cancel window is justified.

### C-11

**Claim:** A motion handoff should explicitly preserve or terminate the relevant action promises, rather than assuming visual smoothness proves state correctness. **Class:** `inference`. **Confidence:** moderate for the failure-prevention logic, untested player benefit.

**Support / precise locator:** GDR-SRC-20261010-P04-007–009, locators in C-07–C-09; GDR-SRC-20261010-P04-003, cosmetic hitbox account.

**Applicability, contrary evidence and unresolved question:** Source and destination must have an agreed state owner. Cancel, buffer, blend and authority transfer are different operations. Local mechanics and network policy remain F04/implementation dependencies.

### C-12

**Claim:** Judge authored, captured, procedural and hybrid motion by the required controllability and expressive range, not an assumed naturalness hierarchy. **Class:** `inference`. **Confidence:** moderate as a decision framework, not an empirical ranking.

**Support / precise locator:** GDR-SRC-20261010-P04-005, §6 limitations; GDR-SRC-20261010-P04-006, craft account; GDR-SRC-20261010-P04-003, rig and cross-skin production discussion.

**Applicability, contrary evidence and unresolved question:** No inspected equal-budget comparison of motion-capture versus authored/procedural pipelines. Authorship, cleanup, contact correction and exceptions are cost categories, not measured savings.

### C-13

**Claim:** Reducing nonessential motion should be evaluated alongside access to required facts rather than assumed to preserve every effect or feeling. **Class:** `inference`. **Confidence:** moderate as a scoped guidance-to-design bridge.

**Support / precise locator:** GDR-SRC-20261010-P04-010, alternatives to visual-only cues; GDR-SRC-20261010-P04-011, moving UI/background exception and non-core animation; reviewed P02 information versus emotion.

**Applicability, contrary evidence and unresolved question:** No blanket animation freeze, equivalent affect, medical safety or certification claim. Deafblind, sign-language and specialist tactile performance needs remain unresearched.

### C-14

**Claim:** Treat expressive interpretation and intended character behavior as separate records; avoid diagnosing real people or standardizing one culturally preferred movement as normal. **Class:** `inference`. **Confidence:** moderate as an ethical/measurement safeguard, not an effect estimate.

**Support / precise locator:** GDR-SRC-20261010-P04-004, deliberately selected stimuli and brief ratings; reviewed W01 character-design, Decision and scope; W02 dialogue-and-voice, Performance is an interpretation.

**Applicability, contrary evidence and unresolved question:** Nonhuman performers, languages, movement differences and cultures are not comprehensively represented. Specific casting/performance rights require separate review; no legal advice.

### C-15

**Claim:** The recipes, examples, measurements and comparisons here are proposed and have not been implemented or tested. **Class:** `hypothesis`. **Confidence:** low for unknown local effect and feasibility.

**Support / precise locator:** Original P04 synthesis under the current brief; conditional applications of C-10–C-14.

**Applicability, contrary evidence and unresolved question:** No recruitment, instrumented gameplay, latency measurement, network test, animation asset creation or participant result. Study choices must be agreed before a later authorized test.

### C-16

**Claim:** This animation deliverable is authorized only as a provisional P04 research candidate. **Class:** `studio-decision`. **Confidence:** high from explicit instruction.

**Support / precise locator:** Doug’s P04 message and attached brief, Authorization update / Assigned outputs / Current jobs and boundaries; run dated 2026-10-10.

**Applicability, contrary evidence and unresolved question:** Owner Doug. Independent review, permanent identity reconciliation, host validation, release and game implementation remain separate gates.

## References

All public records below were inspected in the stated passages on **2026-10-11 UTC**. IDs are P04-scoped source records, not permanent SRC allocations. Dates of older works are publication dates, not claims of current game behavior. Repeated reference records support standalone reading; they are not extra evidence.

### GDR-SRC-20261010-P04-003

**ASU Team, Riot Games; named concept, character, technical-art and animation contributors.** [/dev: Modernizing the Monk](https://www.leagueoflegends.com/en-gb/news/dev/dev-modernizing-the-monk/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2024-04-08. **Edition/build:** Lee Sin art-and-sustainability update developer article; exact game build unspecified.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary multidisciplinary creator account. **Exact locators:** Creating Consistency Across Skins; Preparing the Ponytail; Base Meshes and 3D Sustainability; Animation → Making Lee’s Animations More Impactful, Float like a Butterfly, Sliding Hitboxes like a Lee, Making Skins with Style. **Claims supported in this entry:** C-03; indirect C-11/C-12.

**Limits:** Intentions and reported production issues, not measured satisfaction, cost savings or a directly observed build. Animation contributors: Sean “Riot Redepoka” Yeung and Einar “Riot Beinhar” Langfjord. Embedded media not played. **Independence/deduplication:** Same production line as source 002; multiple contributors are not separate efficacy studies. Cross-batch deduplication pending. **Rights:** Reuse license not established; paraphrase only; no likenesses, media or assets copied.

### GDR-SRC-20261010-P04-004

**Rachel McDonnell, Martin Breidt and Heinrich H. Bülthoff.** [Render me Real? Investigating the Effect of Render Style on the Perception of Animated Virtual Humans](https://www.scss.tcd.ie/Rachel.McDonnell/papers/Siggraph2012a.pdf). **Publisher:** ACM Transactions on Graphics. **Publication/update:** 2012-07. **Edition/build:** 31(4), Article 91; eleven-page author PDF; DOI 10.1145/2185520.2185587.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original human perception experiments. **Exact locators:** §4 Choosing Render Styles; §5.1 Still vs. Moving, methods/results, PDF pages 4–6; §5.2 Motion Anomalies and §5.2.1 Results, PDF pages 6–7. **Claims supported in this entry:** C-06; context for C-14.

**Limits:** Selected male-character stimuli and brief viewing tasks, not controlled gameplay. A deliberately ill-looking treatment complicates a neutral realism continuum. No raw-data reanalysis. PDF pages 5 and 7 visually inspected; the page-6 screenshot route failed. **Independence/deduplication:** Original study; author PDF and DOI/publisher record are one source. Cited by source 005: independent cohorts, not disconnected intellectual lines. Lowercase author-path route failed; uppercase path succeeded. **Rights:** ACM copyright; no new reuse permission inferred from author hosting. No figures or stimulus media redistributed.

### GDR-SRC-20261010-P04-005

**Aline Normoyle and Sophie Jörg.** [The effect of animation controller and avatar on player perceptions](https://www.researchgate.net/publication/310603130_The_effect_of_animation_controller_and_avatar_on_player_perceptions). **Publisher:** Computer Animation and Virtual Worlds / Wiley; author manuscript via ResearchGate. **Publication/update:** First online 2016-11-20; journal issue 2018. **Edition/build:** 29(6), e1731; DOI 10.1002/cav.1731. Inspected author manuscript uploaded 2021-01-26; manuscript pagination, not journal pagination.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original controlled game experiment and separate observer study; primary author manuscript. **Exact locators:** §3.2–3.4, manuscript pp.12–17; §4.9, pp.23–24; §5.1 Control and §5.2 Enjoyment, pp.25–26; §5.3 Satisfaction, pp.26–27; §5.4 Performance, pp.27–28; §6 Conclusion and Future Work, pp.31–33. **Claims supported in this entry:** C-04/C-05; limitations for C-12.

**Limits:** Publisher full-text request redirected to abstract; full manuscript text was read on the author-upload route. Exact equivalence to the version of record not verified. Restricted controller/task designs, mainly student sample and differing observer/player questions limit generalization. Internal performance-direction inconsistency retained as P04-CON-04. No footage, raw data or graph digitization used. **Independence/deduplication:** Cites source 004 and earlier work by these authors. Manuscript, abstract and DOI are one work, not multiple confirmations. Cross-batch deduplication pending. **Rights:** Author manuscript copyright; redistribution license not established. Attributed paraphrase only; no participant data copied.

### GDR-SRC-20261010-P04-006

**John Lasseter, Pixar.** [Principles of Traditional Animation Applied to 3D Computer Animation](https://cgvr.cs.uni-bremen.de/teaching/cg_literatur/Principles%20of%20traditional%20animation%20applied%20to%203D%20computer%20animation.pdf). **Publisher:** ACM SIGGRAPH Computer Graphics. **Publication/update:** 1987-07. **Edition/build:** 21(4), printed pp.35–44; university-hosted paper PDF.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary practitioner craft account. **Exact locators:** §2.2 Timing, printed p.37; §2.3 Anticipation, p.38; §2.4 Staging, pp.38–39; §2.5 Follow Through and Overlapping Action, p.39. **Claims supported in this entry:** C-02; indirect C-10.

**Limits:** Film/computer-animation craft vocabulary, not an interactive-control experiment or formal standard. Fixed-frame anecdotes are not gameplay timing prescriptions. Text inspected; two web PDF screenshot attempts failed, so no figure-specific observation is claimed. **Independence/deduplication:** Historical craft source, not current engine guidance. CMU route failed; Bremen PDF text succeeded. Cross-batch edition deduplication pending. **Rights:** 1987 ACM copyright; no illustrations or extended passages reproduced.

### GDR-SRC-20261010-P04-007

**Unity Technologies.** [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html). **Publisher:** Unity Manual. **Publication/update:** Publication/update date unknown. **Edition/build:** Unity 6.3 / 6000.3 documentation, selected edition; no claim that it is the newest engine.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Properties → Has Exit Time, Fixed Duration, Transition Duration and conditions; Transition interruption → Interruption Source and Ordered Interruption. **Claims supported in this entry:** C-07; indirect C-01/C-10/C-11.

**Limits:** Documents facilities and units; does not measure this project’s latency, responsiveness or cancellation policy. No engine execution. Recheck exact dependency version before implementation. **Independence/deduplication:** One vendor mechanism reference, not efficacy evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined. Paraphrase only, no code copied.

### GDR-SRC-20261010-P04-008

**Epic Games.** [Animation Blueprint Blend Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Inertialization: source evaluation, interruption, and Animation Notifies paragraphs; parsed text lines 121–150. **Claims supported in this entry:** C-08; indirect C-11.

**Limits:** No benchmark or runtime test. Documented source-evaluation behavior does not by itself prescribe gameplay event ownership. Experimental facilities are not endorsed for shipping. **Independence/deduplication:** Same vendor as source 009, different page/mechanism. Version parameter is part of this source identity; central deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.

### GDR-SRC-20261010-P04-009

**Epic Games.** [Understanding Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Network Smoothing; Replicating Special Case Movement with Root Motion → From AnimMontages; parsed text lines 174–203. **Claims supported in this entry:** C-09; indirect C-11.

**Limits:** Character Movement Component behavior, not a universal networking model or proof of fair combat. No server/client, network or frame-time tests performed. **Independence/deduplication:** Same vendor as source 008. Distinct mechanism, not independent user-outcome evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.

### GDR-SRC-20261010-P04-010

**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal and Overview; Implementation guidelines → alternatives to color and visual-only information; simulation-filter and actual-player evaluation paragraphs. **Claims supported in this entry:** C-13.

**Limits:** Practitioner guidance, not a formal standard, legal advice or certification. Availability of an alternative is not demonstrated usability or emotional equivalence. Public body inspected despite authorization boilerplate. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-05 and GDR-SRC-20261010-P02-005; central reconciliation pending. Same issuer as source 011. **Rights:** Vendor page; content reuse license not inspected; paraphrase only; no example media copied.

### GDR-SRC-20261010-P04-011

**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Implementation guidelines → moving/blinking/scrolling UI and its background-motion exception; camera motion; repetitive non-core animation; parsed text lines 43–121. **Claims supported in this entry:** C-13.

**Limits:** Not a universal freeze-all-gameplay requirement, medical safety threshold or certification. No FOV, flashing or animation-duration limit is extracted. Camera-setting research remains P03 ownership. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-10 and GDR-SRC-20261010-P02-010; central reconciliation pending. Related vendor guidance is not independent efficacy evidence. **Rights:** Vendor page; content reuse license not inspected; paraphrase only.

## Open questions and change history

Open coverage: action-specific cancellation/commitment from F04; actual P03 view/display constraints; locomotion/contact systems beyond the inspected documentation; modern equal-budget capture/procedural/authored comparisons; cross-cultural expressive interpretation; sign-language and facial-localization requirements; networked owner/observer outcomes; and measured production/performance budgets.

P04-CON-03 retains control versus authored commitment as a contextual design tradeoff. P04-CON-04 retains the manuscript reporting inconsistency and weaker satisfaction threshold; it is not resolved by assuming a typo. The selected evidence does not validate an entire animation pipeline or fixed timing recipe.

**2026-10-11 UTC:** initial 0.1.0 draft, revision initial-draft-1, no predecessor/supersession. Author self-review only; independent review, host validation, canonical identity allocation and release remain pending. The next decision is review/revision and dependency reconciliation, not engine adoption, participant work or game implementation.
