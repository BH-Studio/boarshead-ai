# Preserved GDR-CAND-20261010-P04-TOP-02-comparison.diff

Original payload SHA-256: `36a2a98745843b2291f2538a6bb4a0172f1df0ffd10078fa48325a0bd6c6a67c`. Complete original record follows in Markdown.

```text
--- earlier/animation-and-performance.md
+++ later/animation-and-performance.md
@@ -9,35 +9,31 @@
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
-updated: '2026-10-11'
-evidence_checked: '2026-10-11'
-date_basis: UTC; run identifier retains dispatch date 2026-10-10
-identity_scope: run-scoped candidate; permanent allocation pending
-predecessor_sha256: null
-supersedes: null
-change_summary: Initial P04 candidate; no predecessor submitted.
+identity_scope: temporary-run-scoped
+updated: '2026-10-10'
+evidence_checked: '2026-10-10'
 aliases:
 - animation responsiveness
-- animation interruption
-- expressive motion
+- expressive behavior
+- animation transitions
 tags:
 - animation
-- performance
 - posing
 - timing
 - interruption
-- recovery
-- accessibility
+- performance
+- input
+- network-context
 related_topics:
 - GDR-CAND-20261010-P04-TOP-01
 - GDR-CAND-20261010-P02-TOP-01
 - GDR-CAND-20261010-P02-TOP-02
+- GDR-CAND-20261010-W01-TOP-03
+- GDR-CAND-20261010-W02-TOP-01
 related_patterns:
 - GDR-CAND-20261010-P04-PAT-02
-- GDR-CAND-20261010-P04-PAT-01
 related_genres: []
 source_ids:
-- GDR-SRC-20261010-P04-003
 - GDR-SRC-20261010-P04-004
 - GDR-SRC-20261010-P04-005
 - GDR-SRC-20261010-P04-006
@@ -45,383 +41,324 @@
 - GDR-SRC-20261010-P04-008
 - GDR-SRC-20261010-P04-009
 - GDR-SRC-20261010-P04-010
+- GDR-SRC-20261010-P01-05
+- GDR-SRC-20261010-P01-10
 - GDR-SRC-20261010-P04-011
 reviewer: null
 approved_by: null
 approved_date: null
+predecessor_sha256: null
+supersedes: null
+change_summary: Initial P04 submission; does not replace or resend any previous batch.
+byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
 # Animation and performance
 
-**Draft 0.1.0, initial-draft-1 — not released or implemented.** Animation quality, control responsiveness, expressive interpretation and task performance are separate questions. The inspected evidence supports conditional design choices and specific documented mechanisms, not a universal anticipation duration, cancel window or rule that realism always improves play. [C-01–C-09, C-16]
+**Draft 0.1.0; candidate revision initial-draft-1. Not released or independently reviewed for P04.** The strongest recommendation is to specify the action’s meaning, commitment and interruption behavior before treating a polished transition as successful interaction. This is a design **inference**, not a rule that responsiveness must always defeat expressive or physical commitment. [C-10]
 
 ## Decision and scope
 
-**Decision:** How should posing, preparation, timing, transitions and expressive behavior communicate an action or character while preserving the control, commitment and recovery that the task actually promises?
-
-This entry covers character/object animation and performed visual behavior, including anticipation, timing, posing, transitions, responsiveness, expression, interruption and recovery. “Performance” includes expressive delivery; it does not imply a frame-rate benchmark. The topic remains engine-neutral. Unity and Unreal documentation supply bounded examples of mechanisms, not an implementation choice or code package. [C-01, C-07–C-09, C-12]
-
-Excluded: complete combat/traversal rules, camera tuning, rig construction, a motion-capture production manual, network architecture, lip-sync implementation, character canon, performer contracts, assets, participant experiments and certification. P03 camera/platform and F04 combat/traversal remain missing active/queued dependencies; their absence prevents final action-specific settings or authoritative movement policies. [C-15, C-16]
-
-### Working distinctions
-
-These definitions are proposed analytic tools, not a formal state-machine standard. [C-01, C-10, C-15]
-
-| Term | Meaning used here | Boundary to preserve |
-| --- | --- | --- |
-| Pose / staging | A configuration and presentation that emphasizes a relevant action or interpretation. | A strong pose can be hidden by the view or interpreted differently. |
-| Anticipation | Visible preparation, an advance communicative cue, or both. | It need not be delay after a player’s request; the cue can precede a decision. |
-| Timing / spacing | When meaningful poses and events occur, and how motion progresses between them. | Total clip length alone does not specify the temporal experience. |
-| Commitment | A gameplay rule limiting what can change after a point or condition. | Not necessarily the same as waiting for an animation to finish. |
-| Cancel window | A locally defined interval or condition allowing an action to be replaced or ended. | A blending feature does not create that permission. |
-| Buffer | A request retained for possible later eligibility. | It is not acceptance, completion or a promise to execute after context changes. |
-| Blend / handoff | Presentation changes from one pose/motion state toward another. | Smooth interpolation is not evidence that the game state is correct. |
-| Recovery | A period or condition governing the next action and/or settling motion. | Mechanical unavailability and cosmetic follow-through can end at different times. |
-| Expressive reading | A player’s interpretation of intention, effort, attitude or feeling. | It is not the author’s intention or a diagnosis of a real person. |
-
-### Application assumptions
-
-Declare the actor’s role, task, input, display/view, local or networked authority, ability to pause, relevant access settings and audience familiarity. A player-controlled action, an observed agent and a noninteractive performance have different control obligations. A reversible starting context for the proposed evaluation is flat-display play with familiar controls; findings would not automatically transfer to VR body motion, remote spectators, switch input or every display. No hardware, timing or numerical comfort settings are assumed. [C-01, C-09–C-15]
+**Decision:** How should posing, anticipation, timing, transitions and expressive behavior communicate an action while preserving the control, consequences and recovery opportunities the game intends?
+
+*Animation* here concerns changing presented pose or form over time. *Performance* includes the interpreted behavior of a character or other expressive agent, not just animation-system speed. *Responsiveness* must identify its endpoint: acknowledged input, first noticeable pose change, effective movement, action eligibility, consequential event, or completed transition. These endpoints are not interchangeable. A *cancel* may stop visual playback, stop an action before commitment, leave an action after commitment, or reverse a consequence; the design must say which. These are analytic conventions for this draft, not an industry standard. [C-01]
+
+The scope includes player-controlled and non-player actors, anticipation, posing, timing and spacing, blending, interruption/recovery, expressive beats, authored and selected motion, and conceptual platform/network constraints. It excludes implementing an engine controller, prescribing combat frame data, creating motion assets, casting or performance contracts, certifying accessibility, and equating an intended emotion with measured player response. [C-01, C-15]
+
+### Reviewed guidance transferred and missing neighbors
+
+Actual selected P02 `review-correction-1` bytes were inspected. Controls and input separates input receipt, qualification/buffering and action execution. Feedback and game feel separates acknowledgement, pending state, accepted action and confirmed outcome. Multimodal communication and the P01 corrected access work separate available information from emotional equivalence. These are retained candidate distinctions, not newly validated empirical results. [C-01, C-04]
+
+W01 Character design and W02 Dialogue and voice were inspected for **intended characterization versus player interpretation** and the boundary between a selected contribution and its performed meaning. The selected W02 intent-and-response pattern, F07 legible-commitment pattern and G02 bounded-action-grace pattern were inspected for ownership overlap. P04’s new pattern owns **animation/action phase synchronization and exits**, not a new general consent pattern, dialogue-label pattern or input-grace recipe. Exact identities, revisions, hashes and locators are in the [dependency record](../reviews/full-run-20261010-p04-review-packet.md#inspected-dependency-transfers).
+
+P03 camera/platform and F04 combat/traversal candidate bytes remain missing. No numerical comfort, latency, cancel-window, turn-rate, frame-rate or display setting is inherited from unseen work. Original P01 numerical-accessibility corrections remain intact; CSS pixels or rendered body height are not animation timings. [C-01, C-13]
+
+**Assumptions for a later application:** actor/controller authority; whether the player controls that actor; action consequences; input method and chosen assistance; viewing angle, actor size and motion visibility; animation sample rate and playback rate; simulation and display timing; local or networked roles; permitted interruption; camera motion; language and performance context; relevant access needs. First-person, third-person, fixed-view, touch, controller and XR situations are not assumed equivalent. [C-01, C-10]
 
 ## Core explanation and mechanisms
 
-### Preparation can inform without making every action wait
-
-Craft vocabulary provides ways to examine attention, apparent effort and continuity; C-02 records its evidence class. P04’s inference is to ask what each preparatory beat is for. It may inform an observer, establish a character intention, acknowledge the player or represent a deliberately committed action. These functions should not be conflated with technical delay. A brief response that only acknowledges a request must not falsely communicate a completed effect. [C-01, C-02, C-10]
-
-**Proposed mechanism:** a visible state matches the relevant action promise → the player interprets the available choices → execution or recovery behaves accordingly → perceived control or impact may improve. The first relation can be audited in a specification; interpretation and experience still require evaluation. Immediate movement can feel wrong when the task is about deliberate commitment, just as extended preparation can feel wrong when the task promises prompt correction. [C-10, C-11, C-15]
-
-### Naturalness and responsiveness do not collapse into one quality score
-
-The empirical results and their reporting limitations are retained in C-04–C-06. They justify separating outcomes, not optimizing every game toward a single controller. A participant’s “easy to control,” an observer’s “natural,” a director’s “expressive,” and a logged success rate are not interchangeable measures. Adding a trailing garment or fuller turn can alter more than visual polish; removing motion can also remove intention, identity or action information. [C-04–C-06, C-12, C-14]
-
-The decision is therefore conditional: retain the expressive beat when its value warrants the control and authoring consequences; decouple optional settling when it falsely implies a lock; or use a simpler transition when the task needs an unambiguous state change. None of these is established as a universal improvement. [C-10–C-12]
-
-### Interruption is an action policy and a presentation problem
-
-Write two separate records: **what the game permits** and **how that change becomes visible**. A controller might accept a cancellation while the old pose persists; another might blend beautifully to an action that was never accepted. Both can miscommunicate. Unity’s documented timing/ordering facilities and Unreal’s source-evaluation behavior make this separation concrete; they do not resolve a game’s policy. [C-07, C-08, C-11]
-
-For each permitted handoff, identify which promises survive: movement/contact, target, completion, tool ownership, visible active state and permission for the next input. Identify which must stop. Do not leave an essential state change dependent on a presentation event that the chosen transition may discard. Equally, do not transfer an old action’s success effect to a replacement merely to preserve visual continuity. These are failure-prevention inferences, not engine changes performed here. [C-08, C-11]
-
-### Networked presentation adds another distinction
-
-An actor’s displayed preparation, predicted local response and accepted remote outcome may differ. The component-specific documentation in C-09 establishes that animation agreement is not something to assume blindly. P04 proposes labeling a pending state honestly and checking how correction appears to the owner and observers. It does not prescribe prediction, rollback, smoothing values or a networked combat model. Those decisions need the missing system/platform work and an implementation review. [C-09, C-11, C-15]
-
-### Expressive behavior is contextual
-
-A held gaze, rapid turn or restrained gesture might suggest concentration, discomfort, determination or something else. A plausible performance does not establish a single psychological reading. Establish what may remain interpretively open and what the task requires the player to know. Expression can be intentionally deceptive or ambiguous while action availability remains clear. Review posture, costume, voice/text context and viewing distance together rather than treating an emotion label on a clip as measured communication. [C-06, C-12, C-14]
+### Anticipation is an option with a viewer and a purpose
+
+Lasseter describes anticipation, staging, timing and follow-through as animation techniques for communicating action to a viewer; the same paper allows minimized anticipation for some slow actions. Its film examples do not establish a mandatory pre-action delay for a player-controlled action. [C-02]
+
+**Bridge:** ask *who needs to predict what*. A non-player actor’s preparation may communicate an impending action. A player who just requested a routine action may already know the intention and instead need immediate acknowledgement. A performed gesture can prepare attention without postponing every consequential response. The correct choice depends on what information and commitment are intended; no single body pose, number of frames or preparation duration guarantees comprehension. [C-10, C-11]
+
+Posing, timing and transitions should therefore be considered together. A distinctive key pose may be invisible from the actual view, crossed too quickly, hidden by another body part, or blurred by a blend. Conversely, a long held pose may be legible but falsely imply that the actor is still committed after control has returned. Those are testable failure mechanisms, not results observed in P04. [C-10, C-14]
+
+### A narrow experiment challenges automatic naturalness benefits
+
+Normoyle and Jörg studied 67 mostly-student participants using gamepad-controlled, third-person platform tasks with five controller variants; a shared Blend condition served two comparisons. A separate 12-person video study rated MoveTree most natural. In play, MoveTree took longer to reach goals than Switch/Blend; cape variation reduced enjoyment versus Blend. Trade-off enjoyment differences were not significant. Some satisfaction/control comparisons were only at the paper’s .1 level, not .05. Naturalness and gameplay motion-quality questions differed. [C-03]
+
+These results support separating task outcomes from visual appraisal, not declaring “animation does not matter,” “never blend,” or a modern motion-matching system inferior. The older controller restricted switching during transitions and changed turning behavior. Its operational responsiveness includes visible request completion, not merely our local acknowledgement endpoint. No new milliseconds, effect-size estimate, equivalence claim or raw-data analysis is inferred. [C-03, C-04]
+
+**Evidence-to-application bridge:** a transition can be aesthetically desirable while delaying a task-relevant event. Compare the actual action consequences and input history, not only a rendered clip. Conversely, deliberate physical commitment may be the intended decision cost; shortening it changes the task rather than simply polishing the same task. A local test must expose that distinction. [C-04, C-10, C-11]
+
+### Engine transitions are mechanisms, not gameplay permission
+
+Unity 6.3 documents transition duration, exit conditions and interruption ordering; duration can use seconds or a normalized source-state fraction. Those controls describe Animator behavior. They do not themselves specify whether an inventory transfer, collision event or other consequence should be undone. [C-05]
+
+Epic’s root-motion documentation describes animation-driven displacement as an alternative to movement driving the visual layer. Its networked Character Movement documentation separately identifies responsibilities for coordinating root-motion animation through gameplay. A visually matching local transition does not establish consistent authority across participants. [C-06, C-07]
+
+**Bridge:** a design record needs separate answers for movement authority, action eligibility, consequence authority and visual continuity. The same animation can remain useful under different control policies, but those policies are not interchangeable. A visual blend finishing is not automatic proof that an action succeeded; an interrupted clip is not proof that it did not. This is an inference from distinct facilities and the inspected P02 state distinctions, not a tested synchronization architecture. [C-01, C-10]
+
+### Authored transitions and data-driven selection have different failure surfaces
+
+Epic’s Motion Matching documentation selects poses using a database/schema rather than only a manually enumerated state graph. It documents repeated notify events from adjacent pose selections and limitations of trying to repair mismatched motion data through weights alone. These are concrete authoring/verification concerns, not a measured superiority claim. [C-08]
+
+The implication is to evaluate the **coverage of the intended actions**, not choose a technique by its label. An authored system can make particular exits explicit but accumulate exceptions. A data-driven system can reuse a broad motion collection yet still require appropriate data, selection criteria, event handling and out-of-coverage behavior. These are conceptual work categories; this draft does not estimate asset volume, memory, runtime cost or staffing. [C-10]
+
+### Expressive performance is interpretation, not a pose dictionary
+
+Naughty Dog’s retrospective describes facial-capture work requiring a new rig/system and NPC traversal exits depending on AI/scripting coordination. It is an account of production dependencies, not evidence that captured performance automatically produces believable behavior or better control. [C-09]
+
+For a prospective scene, write the **intended beat** and the **interpretation to investigate** separately. An agent pauses before returning an object: intended hesitation is not proof that players perceive reluctance, deception or concern. Ask what players thought was happening and why, while distinguishing that interpretation from the action’s literal result. Performance direction can permit ambiguity without changing what a player-controlled character agreed to do. [C-12]
+
+A later localized performance review should examine gesture, posture, gaze, timing, speech and captions in their context. Do not assume that identical motion timing across languages preserves pragmatic meaning, or that a fluent back-translation validates a gesture. This is a proposed investigation and risk control; no cross-cultural performance study, gesture equivalence or legal conclusion is established here. [C-12, C-14]
+
+### A recent production choice is not a universal capture policy
+
+In the 2026 Play by Play interview, Laygo describes exaggerated hand-keyed poses/timing and a shared base animation set with selected character-specific additions. This is a contemporary production alternative to equating naturalism with motion capture or requiring every actor to have a unique set. It reports intention and reuse, not measured responsiveness, savings or superiority. [C-16]
 
 ## Design choices and alternatives
 
-These options are conceptual design alternatives; they do not assert equal cost or universal engine behavior. [C-10–C-15]
-
-| Choice | Appropriate context | Cost, failure risk and alternative |
-| --- | --- | --- |
-| Authored committed motion | The action deliberately includes a nonreversible or constrained phase. | May discard corrective intent or obscure the next available action. Communicate commitment and recovery; compare a clearer but equally committed presentation. |
-| Interruptible authored motion | The task promises timely redirection. | Requires destination coverage, contact/trajectory repair and event ownership. A clear short handoff can be preferable to an elaborate blend. |
-| Cosmetic follow-through after readiness | Settling or expressive motion should continue after control returns. | The old pose may imply the action is still locked. Separate readiness information and test conflicting inputs. |
-| Captured performance | Nuanced human delivery or an existing capture pipeline suits the project. | Selection, editing, retargeting and adaptation remain work. No evidence here establishes universal naturalness or lower total cost. |
-| Procedural or responsive adaptation | Many target, terrain or pose contexts exceed a small authored set. | Behavioral range and failure modes need testing; plausibility is not semantic correctness. Restrict adaptation when identity, contact or explicit staging matters more. |
-| Hybrid layers | Some parts of behavior must adapt while others preserve an authored read. | Conflicting layers can erase a pose or imply a contradictory intention. Fewer layers or explicit state-specific poses remain valid alternatives. |
-| Minimal transition / no extra ornament | The changed state is already clear or repeated motion distracts. | May remove expression or a needed cue. Preserve essential facts; do not present motion removal as universally better. |
-
-### Motion ownership, not a preferred engine
-
-A later design should state whether displacement is primarily chosen by gameplay, authored in motion, or coordinated between them, and who resolves disagreement. The relevant question is how to preserve the allowed path/contact and visible action under interruptions, scaling and corrections. P04 does not benchmark root motion against in-place motion, prescribe either, or supply integration instructions. No universal choice follows from the documentation examples. [C-07–C-09, C-11, C-12]
+| Choice | Conditional use | Cost, countercase and alternative |
+|---|---|---|
+| Immediate effective action with a short or overlapping visual transition | The player’s task requires direct response and the animation need not impose a commitment. | Abrupt changes may undermine the intended physical behavior. Compare a selective transition without claiming all smoothness is harmful. [C-10, C-11] |
+| Authored anticipation before consequence | Preparation communicates a relevant future action or is part of a disclosed commitment. | Repeating it for a routine command may add unwanted delay. Minimize or move preparation earlier when prediction is already available; verify semantics. [C-02, C-10] |
+| Clip-led physical commitment | Positioning, weight, deliberate execution or a staged performance is the intended constraint. | Cancellation can change the decision structure. Preserve disclosed stakes while making control return and failure/recovery legible. [C-10] |
+| Movement-led pose selection | Position and response policy must be independently controlled. | Visual feet, hands or props can cease to agree with the motion unless authored appropriately. Test rather than prescribe a particular correction technology. [C-06, C-10] |
+| Selectively interruptible authored graph | A manageable set of actions has important, explicit exits. | Every extra transition adds cases to verify; interruption priority is not itself a gameplay cancellation policy. [C-05, C-10] |
+| Motion-database selection | The production can supply and review motion covering the action space and its boundary cases. | Missing data, repeated events and query mismatch remain possible. A smaller authored solution may be easier to reason about for a limited task. [C-08, C-10] |
+| Full-body expressive beat | The actor, view and attention opportunity can carry meaning through posture and gesture. | Repetition or interruption may change that meaning. Use a shorter acknowledgement, a deferred beat, or no performance when expression is unnecessary. [C-12] |
+| Reduced secondary motion | Decorative motion competes with a task, player preference or comfort. | Do not remove the only essential state indicator. An alternative fact channel must be usable, not merely present. [C-13] |
 
 ## Application process
 
-**Proposed — not performed.** [C-15]
-
-1. **Diagnose the complaint.** Ask whether the problem is missing acknowledgement, unexpected commitment, poor state legibility, unwanted motion, weak expression or a true technical delay. Do not treat all reports of “floaty” as the same issue.
-2. **Specify the action contract.** Record eligibility, acceptance, commitment, result and recovery only where meaningful. Identify legitimate cancellation and buffering conditions, target validity and what the player can know. Mechanical policy belongs to the system owner.
-3. **Sketch meaningful poses and beats conceptually.** Identify the required preparation, active state and exit/readiness. Name the intended expressive reading and plausible alternatives. Do not set universal frame counts or insist that each state needs a separate clip.
-4. **Audit handoffs.** For each permitted interruption, record what stops, what survives, what the destination must show and which events must still occur exactly once. Include denial, pause/resume, target loss and state changes during a transition.
-5. **Choose the least complex adequate motion treatment.** Compare a committed clip, an interruptible/hybrid version and a clear simpler handoff without secretly changing the action’s balance. Record when changing policy is itself the intended experiment.
-6. **Plan access and localization with the performance.** Identify nonessential repeated motion, essential gesture/state information, voice/text dependencies and alternative routes. Do not assume a reduced-motion variant communicates the same emotion or that a translated line fits identical mouth/gesture timing.
-7. **Evaluate and retain only the supported scope.** Separate prediction of permission, recognition of actual state, control experience, expression, comfort and production work. A smooth transition that hides denial is a failure even when liked; a deliberately abrupt transition can be appropriate when clarity is the priority.
-
-The detailed interruption recipe is [State-aligned animation handoff](../patterns/state-aligned-animation-handoff.md). This process creates a reviewable design proposal, not an authorized implementation specification. [C-11, C-15, C-16]
+This is proposed design work, not an engine implementation recipe. [C-10, C-14]
+
+1. **Diagnose the mismatch.** State whether the failure concerns identification, input acknowledgement, effective action, consequence prediction, recovery, expression or comfort. A dislike of a turn is not automatically input latency; a late consequence is not automatically a blending problem.
+2. **Define the action phases and authorities.** Record request/trigger, acceptance or pending state, preparation, commitment, consequence, recovery and return of control as appropriate. Merge or omit phases when the action does not need them. Assign a conceptual owner to the actual consequence separately from its animation.
+3. **Specify permitted exits.** At each phase, describe rejection, cancellation, interruption by another event, pause/re-entry and completion. State what is retained, consumed, refunded, repositioned or merely represented differently. “Interruptible” is too vague without these consequences.
+4. **Choose the motion strategy.** Compare the simplest viable authored, blended, root-driven, movement-driven or selected-motion approach. Decide which poses and durations carry information and which are decorative. Preserve critical distinctions under the chosen access settings.
+5. **Plan observation under real task conditions.** Record first visible acknowledgement, effective action and control return separately. Include transitions initiated from unusual states, repeated inputs, late cancellations and interrupted/repeated expressive beats. Add network roles and display conditions only when resourced, with no untested equivalence claim.
+6. **Evaluate and revise.** Compare action understanding and errors with preference, perceived control, intended expression and comfort. Shorten or simplify when added performance has no relevant value; retain a deliberate commitment when it is part of the agreed task, not because the clip happens to be long.
+
+### Example action-phase record
+
+The following fields are an illustrative specification format, not approved engine data: current phase; true state; event that permits progression; what the player sees/hears/otherwise receives; which input or external event can interrupt; effect of interruption; next allowed action; persistence on pause/re-entry; network authority if applicable; and unresolved ambiguity. This extends P02’s feedback distinctions to the life of a motion. It does not create new buffering or input-remapping rules. [C-01, C-10]
 
 ## Patterns and genre adaptations
 
-`GDR-CAND-20261010-P04-PAT-02` owns state-aligned motion transfer. [Recognition-preserving style variation](../patterns/recognition-preserving-style-variation.md), `GDR-CAND-20261010-P04-PAT-01`, is relevant when poses, accessories or gesture families help identify the same entity across variants. [Art direction](art-direction.md) owns the shared visual system rather than the control policy.
-
-The [reviewed dependency record](../reviews/full-run-20261010-p04-review-packet.md#reviewed-dependency-transfer) identifies P02’s action semantics and fact-preserving presentation, P01’s readability/access boundaries, F01’s corrected discrimination test and W01/W02’s limited ownership transfer. Old “unavailable here” sentences inside those candidates describe their original authoring sessions, not P04’s actual access. P04 does not republish those files.
-
-No genre file or gameplay timing rule is created. A situation rewarding deliberate commitment and one rewarding continuous correction can legitimately need different handoffs. Resolve that task-level conflict explicitly; a genre label alone does not decide it. [C-10, C-15]
+[Action-phase and interruption contract — GDR-CAND-20261010-P04-PAT-02](../patterns/action-phase-and-interruption-contract.md) gives an actionable recipe for synchronizing action meaning with animation phases and exits. [Role-preserving style variation](../patterns/role-preserving-style-variation.md) is relevant when costume or shape changes interact with motion identity; neither pattern independently validates the other.
+
+Task-specific examples are not genre guidance. An actor observed for expression, an actor controlled for precise positioning, and an actor whose commitment must be predicted can warrant different timing choices in the same game. Do not choose a “winning” genre rule. Future combat/traversal and camera/platform reconciliation remains explicit. Additional localized expressive-beat work is queued, not delivered as a third pattern. [C-10–C-12]
 
 ## Examples and counterexamples
 
-### Creator-reported case
-
-C-03 records a production tension between expressive posing and alignment with a fixed gameplay volume. It is a reported design rationale and problem account, not observed gameplay or a measured improvement. The study boundary cases in C-04–C-06 remain separate from that creator intent. [C-03–C-06]
-
-### Illustrative worked example — interrupted inspection
-
-**Synthetic; no assets or prototype.** A player directs a character to inspect a panel. The task permits turning away before inspection commits. After commitment, the inspection must finish or enter an explicit cancellation outcome; merely releasing a button is not assumed to undo it. [C-15]
-
-Record the distinction between “request received,” “moving to inspect,” “inspection committed,” “result available” and “ready for another action.” Some can share a pose, but their meaning must not be silently collapsed. An early turn-away should lead to a destination pose that no longer implies active inspection. A post-commit turn request may be denied or queued according to the future game’s policy; its animation cannot falsely imply that cancellation succeeded. [C-01, C-10, C-11, C-15]
-
-If the handoff stops evaluating the old motion, the required result must still have an explicitly assigned owner rather than depending on a clip event that might no longer arrive. A trailing hand movement can continue after readiness only when it does not imply the tool is still locked to the panel. Compare against a neutral, simpler handoff and a fully committed presentation with the same action rules. Test cases must include both permitted and denied redirection, not repeatedly reward “cancel immediately.” [C-08, C-11, C-15]
-
-### Illustrative worked example — expressive waiting
-
-A noncontrolled character waits beside a doorway while a player reads an optional message. The intended performance suggests impatience, but the action contract permits waiting without penalty. A repetitive large gesture may compete with reading or imply a hidden deadline. Test a quieter pose, optional motion reduction and clarification of timing; do not conclude that all idle animation is harmful. Measure interpretations such as “waiting,” “angry,” “hurried” and “uncertain” without forcing the intended label. This is a hypothetical communication problem, not an observed audience result. [C-13–C-15]
-
-### Strong counterexample — commitment is the point
-
-A task deliberately requires committing to a weighted action and choosing when to begin. Making every frame cancellable would change the decision, not merely improve the animation. Preserve the intended commitment and make its onset/recovery legible; compare presentation changes separately from mechanical generosity. A spectator-only performance also has no obligation to echo nonexistent controller intent. These countercases defeat a universal “instant response above all” prescription. [C-05, C-10–C-12, C-15]
+### Illustrative worked example — extracting a service module
+
+**Invented, not implemented or tested.** A player commands an agent to remove a module. Before a latch releases, cancelling should leave the module installed. Once the module is transferred, stopping the flourish should not place it back merely because the animation was interrupted. [C-10, C-14]
+
+| Phase | Actual proposed meaning | Presentation and exit |
+|---|---|---|
+| Request received | A command arrived; eligibility is not yet resolved. | A modest acknowledgement must not depict a completed transfer. Repeated requests are not assumed additional transfers. |
+| Accepted / preparation | The module is available and the agent is preparing. | Reach/brace pose may communicate the pending action; cancellation returns to a valid pre-transfer state. |
+| Commitment and transfer | The module’s location changes under the authoritative rule. | Presentation agrees with that event; a later visual exit cannot silently undo it. A separately designed undo would be a different action. |
+| Recovery | Transfer is complete; the actor may still be settling or holding the module. | Specify which next actions are allowed; do not make a decorative settle determine undisclosed eligibility. |
+| Denial / external interruption | Availability changed, a request was rejected, or another event took precedence. | Present the actual result and a valid next option, not a success pose followed by unexplained reversal. |
+
+In a networked variation, a local request may remain pending until the relevant authority resolves it. The exact prediction/correction policy is outside this research; a purely visual solution is not assumed. In a cinematic-only variation, the player may not control the actor at all, so input acknowledgement is irrelevant. The phase vocabulary is optional, not a requirement to insert every phase into both situations. [C-01, C-07, C-10, C-14]
+
+### Illustrative expressive countercase — an interrupted greeting
+
+An agent begins a welcoming gesture when the player approaches, then must attend to a newly urgent task. Resuming the greeting from its old midpoint could suggest continued welcome after the context has changed. Candidate alternatives are to drop it, restart only if still meaningful, or finish with a context-valid acknowledgement. The intended tone, literal state and repeated-exposure response should be reviewed separately. No named game or psychological outcome is asserted. [C-12, C-14]
+
+### Strongest opposing case
+
+An action may deliberately commit the actor to a slow, readable movement whose cost is fundamental to planning. Allowing instant direction changes or cancelling after its consequence can make performance easier by changing that cost. Better completion time would not prove the original animation was inferior. Compare the intended decision and commitment, not a cosmetically similar but mechanically easier task. This countercase blocks a universal responsiveness-first recommendation. [C-10, C-11]
 
 ## Failure modes and constraints
 
-| Observable sign in a later evaluation | Possible cause | Proposed correction or stop |
-| --- | --- | --- |
-| Players repeat inputs after an accepted action. | Receipt or current eligibility is unclear. | Distinguish acknowledgement from success; inspect the timing path rather than just increasing motion amplitude. |
-| The destination pose looks active but the action was denied. | Presentation outran gameplay permission. | Correct the state-to-motion relation; do not reward the attempted action with a success cue. |
-| Completion disappears or occurs twice after interruption. | State ownership depended on clip evaluation or duplicated transition events. | Block progression of that version until a separately authorized design resolves ownership. |
-| Smooth transition, wrong contact or target. | Interpolation retained a pose without its semantic/physical conditions. | Use an explicit release/reacquire or simpler handoff; do not conceal the mismatch with blur. |
-| A costume change obscures a state or shifts the apparent body away from allowed interaction. | Accessory or expressive movement conflicts with the gameplay read. | Review combined model/motion/view; allow justified variation limits. |
-| Players call the motion natural but control frustrating. | Different outcomes have been merged. | Report them separately and compare mechanical policy independently. |
-| Reduced-motion mode hides the only readiness cue. | Optional presentation carried essential information. | Preserve a usable fact route and reevaluate, without promising equal emotion. |
-| One cultural or bodily style is treated as the only believable performance. | Narrow references or instruments enforce a stereotype. | Revise direction and interpretation questions; seek appropriately scoped review. |
-
-These are proposed diagnostic hypotheses, not failures measured by P04. [C-10–C-15]
-
-**Accessibility and sensory context:** XAG guidance supports examining nonessential motion and alternative critical information; its exceptions matter. Do not turn this into a blanket requirement to freeze every character or a certification claim. Consider users reading captions or narration, users who prefer reduced motion, and people whose input pace differs. A task-critical gesture needs an appropriate accessible route, not simply a duplicate decorative pulse. P01’s CSS/text/platform distinctions remain intact. [C-13]
-
-**Expression and localization:** translated speech can change the timing and interpretation of a gesture. Facial movement, gaze and bodily manner should not be assumed to diagnose feeling or honesty. Record intended subtext, legitimate alternatives and task facts separately. Sign-language performance, detailed facial localization and broad cross-cultural interpretation are coverage gaps; they are not solved by this draft’s generic procedure. [C-14, C-15]
-
-**Production constraints:** budget conceptually for transitions, outfit/prop interactions, retargeting, contact correction, event ownership and exceptional states, not just clip count. The evidence does not provide a universal cost saving from motion capture, procedural animation or shared rigs. Performer/reference consent and reuse rights require the relevant human/rights process; this is neither legal advice nor permission to reuse a likeness. [C-12, C-14, C-16]
+| Warning sign to investigate | Possible cause | Proposed correction |
+|---|---|---|
+| The actor reacts immediately, but the requested action is still unavailable. | Acknowledgement confused with eligibility/effective action. | Separate the state presentations and measure the task-relevant endpoint. |
+| The clip ends but the outcome is pending. | Visual completion incorrectly treated as authority. | Show a truthful pending/result transition; review action ownership. |
+| Cancelling duplicates or reverses a consequence unexpectedly. | Exit handling follows clip position rather than action state. | Specify retained consequences and valid next states before adjusting blend polish. |
+| A readable key pose disappears during transition. | The selected view/blend crosses it without enough task-relevant presentation. | Evaluate the moving sequence, not only reference poses; consider a different cue. |
+| Repeated selections produce doubled footsteps or other events. | Animation event emission is not aligned with selected pose changes. | Investigate event identity and selection behavior; no timeout is prescribed. |
+| A gesture reads differently after interruption or translation. | Timing/context changed its implication. | Re-evaluate the complete beat, not just the local pose or word. |
+| Reduced-motion mode loses essential information. | A required fact was embedded only in decorative movement. | Supply and evaluate an appropriate alternative; keep mood equivalence unclaimed. |
+| A natural turn passes clip review but harms task performance. | Review excluded control constraints or changed the endpoint measured. | Compare representative input/action sequences and separate enjoyment from completion. |
+
+Failure interpretations and remedies are proposed, with the documented event-selection example limited to C-08. They are not P04 test results. [C-10–C-14]
+
+**Accessibility and ethics:** respect chosen motion settings, pauses and withdrawal in later evaluation. The goal is not to prove one “normal” body, expression or input speed is ideal. A still body, unusual motion or disability-associated movement should not be treated as evidence of character morality. Asset/capture permission, performer attribution and adaptation rights need separate production review; no legal status is asserted. Proposed studies should not expose a person to effects they decline merely to obtain a comparable trial. [C-12–C-15]
+
+**Production:** conceptual costs include action coverage, transition exceptions, rig compatibility, prop contact, selection/event behavior, alternative presentations, localization and maintenance after rule changes. No source supplies a universal cost advantage for hand-keying, motion capture, root motion, motion matching or more animation. Determine scope and compare local work only after authorization. [C-09, C-10]
 
 ## Playtest and validation
 
-**PROPOSED — NOT RUN.** No prototype, participant work, frame-time measurement, controller instrumentation or network test occurred. [C-15, C-16]
-
-**Question:** Does a proposed animation handoff communicate actual permission and recovery while providing a worthwhile expressive benefit over a simpler alternative?
-
-**Comparisons:** A, existing committed presentation; B, state-aligned handoff under the same mechanical permission rules; C, clear minimal handoff. Where the intended experiment changes cancellation policy, make it a separately labeled factor rather than attributing all effects to animation. Keep task, actual outcomes, view and target conditions comparable. Test local authority first only when that is the chosen scope; a separate later owner/observer network comparison cannot be inferred from it.
-
-**Procedure and participants:** include practiced and unfamiliar users and actual users of relevant access/input settings. Choose sample and precision based on the local decision, not a stock count. Collect permission/state predictions before feedback across eligible, ineligible, target-lost, pending and recovery conditions. Include interrupted transitions and repeated exposure. Counterbalance presentation order and avoid training every participant to respond the same way before the comparison.
-
-**Measures:** mistaken acceptance/cancellation beliefs, premature re-inputs, missed or duplicated outcomes, task errors and recovery choices; separately, perceived controllability, intended-expression interpretations, comfort and willingness to retain the presentation. Report actual elapsed response only after a measurement method distinguishes input acquisition, recognized request, accepted state, visible change and display presentation. No universal timing threshold follows from the cited studies.
-
-**Falsifying decisions:** reject a version that presents a denied action as accepted, loses/duplicates an essential result, or removes necessary information under a supported access route. Reject the proposed explanatory mechanism when an apparent benefit disappears after controlling changed mechanical permissions or when viewers cannot distinguish the intended state. Where the richer presentation adds no credible local value and costs more, prefer the simpler one without claiming statistical equivalence. Preserve intentional commitment when that is the task’s approved premise. Any discomfort or withdrawal request stops that session; tolerability is not inferred from an average rating.
-
-The future study owner must predeclare practical decision criteria, sample rationale, exposure and analysis before execution. Unknown variance or an unrepresented population means limited conclusions, not automatic success. [C-10–C-15]
+**PROPOSED — NOT PERFORMED.** No controller, actor, scene, capture, participant, network trace or frame-time measurement exists from P04. [C-14, C-15]
+
+**Primary question:** Can players predict action state and permitted recovery, and does the chosen presentation support the intended task without unnecessary control or comfort failures?
+
+**Conditions:** compare A, a whole-clip presentation with disclosed commitment; B, a phase-aware presentation with selectively permitted exits but the **same true commitment and consequences**; C, a simpler presentation. A/B is interpretable only when the mechanical contract is matched. A separate experiment may vary commitment itself, but then cannot attribute the result solely to animation. Do not deliberately make A unreadable to manufacture a benefit.
+
+**Control and procedure:** use matched tasks, rules, assistance, input devices and camera views. Counterbalance sequence and action families where feasible. Test normal completion, pre-consequence cancellation, post-consequence exit, denial, repeated requests and external interruption. Include cases where the same-looking interruption has different correct retained consequences. Ask for a state prediction before asking what action a participant prefers; this retains the F01 corrected transfer distinction. Observe ordinary and repeated use separately. Record when a prediction question primes attention.
+
+**Participants/context:** recruit a population justified by the later project, including relevant input/access needs and both unfamiliar and experienced users. Use preferred settings. Test cinematic interpretation with an audience task separately from controlled movement; do not combine ratings from those tasks into one score. A study owner must set sample size and analysis precision before collection; this source set does not supply a population guarantee.
+
+**Measures:** distinguish true receipt, first perceived acknowledgement, first effective action, consequence time and control return; later technical instrumentation must define clocks and uncertainty. Pair observations with state/exit predictions, action errors, repeated inputs, perceived control, motion quality, expression interpretation and comfort. Ask about enjoyment separately. For performance beats, record open interpretations before forced labels, and compare first/repeated/interrupted presentations. Network roles, render/display conditions and alternative modalities require explicit analysis rather than silent pooling.
+
+**Falsification and decisions:** reject a claim that B improves comprehension if apparent success occurs only on repeated answers or disappears on new valid action states. Revise when B misrepresents retained consequences, loses essential information, or reduces desired commitment rather than preserving it. Prefer a simpler alternative if the more elaborate presentation adds no decision-relevant value within the predeclared uncertainty tolerance. A nonsignificant result does not establish equivalence. Any critical action-state contradiction or participant stop request blocks advancement or ends the session as appropriate. Set tolerances, exclusions and stop procedures before execution; do not select them after favorable outcomes.
 
 ## Claim ledger
 
-Claim IDs are local to this entry. Confidence describes the exact scoped wording, not a source’s prestige or the recipe’s overall efficacy. Proposed procedures and examples are not approved studio decisions.
-
 ### C-01
-
-**Claim:** Separate action receipt, gameplay permission, commitment, visible preparation, result and recovery when diagnosing animation-related control problems. **Class:** `inference`. **Confidence:** moderate as an analytic decomposition, not a required number of states.
-
-**Support / precise locator:** Reviewed P02 controls-and-input, Timing path; feedback-and-game-feel, Action receipt versus outcome; GDR-SRC-20261010-P04-007, transition properties.
-
-**Applicability, contrary evidence and unresolved question:** Use only meaningful distinctions for the action. “Performance” here includes expressive delivery, not a promised CPU/frame-time benchmark.
+**Claim:** Input receipt, action eligibility, visual acknowledgement, effective action, consequence and recovery require distinct definitions when they differ. **Class:** `inference`. **Support:** inspected P02 Controls/Feedback state distinctions; GDR-SRC-20261010-P04-005 introduction’s responsiveness definition; original P04 phase vocabulary. **Confidence:** moderate for analytic usefulness. **Limit:** not every action needs separate phases. **Unresolved:** operational endpoints for the actual task and authority model.
 
 ### C-02
-
-**Claim:** Timing, anticipation, staging and follow-through are craft concepts in Lasseter’s account, not demonstrated universal gameplay requirements. **Class:** `practitioner-heuristic`. **Confidence:** high for this boundary of the inspected source.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-006, §2.2–2.5, printed pp.37–39.
-
-**Applicability, contrary evidence and unresolved question:** Historical animation argument and examples, not controlled interactive timing evidence. Do not import its frame anecdotes as control delays or call every action mandatory anticipation.
+**Claim:** Traditional animation anticipation/staging/timing are practitioner communication techniques, not guaranteed gameplay effects or mandatory delays. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-004, §§2.2–2.5, including the slow-action anticipation exception. **Confidence:** high for attribution, low for an untested interactive transfer. **Limit:** film/viewer examples; no timing numbers adopted. **Unresolved:** which preparation a particular player or observer needs.
 
 ### C-03
-
-**Claim:** Riot reports changing Lee Sin’s pose timing/spacing for intended impact and constraining cosmetic motion relative to his fixed hitbox. **Class:** `practitioner-heuristic`. **Confidence:** moderate for production attribution, not measured response.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-003, Animation → Making Lee’s Animations More Impactful; Float like a Butterfly, Sliding Hitboxes like a Lee.
-
-**Applicability, contrary evidence and unresolved question:** No before/after participant data or direct footage observation here. “More satisfying” remains intended/reported, not a measured P04 finding.
+**Claim:** The inspected controller experiment challenges automatic player benefits from increased naturalness under its particular task/controllers. **Class:** `empirical-evidence`. **Support:** GDR-SRC-20261010-P04-005, §§3.2–3.4, 4.8, 5–6; sample, task and principal outcomes above. **Confidence:** moderate, narrow study. **Limits:** shared comparison group, different rating questions, older constrained controllers; .1-level findings not treated as .05-level findings; nulls not equivalence. **Unresolved:** effect estimates and transfer to other tasks, populations and modern systems.
 
 ### C-04
-
-**Claim:** In the inspected controller study, MoveTree received lower ease-of-control ratings than Switch, and Cape lower enjoyment than Blend. **Class:** `empirical-evidence`. **Confidence:** moderate within the restricted experiment.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-005, §3.3–3.4 and §5.1–5.2: 84 recruited, 78 analyzed after six exclusions; between-controller play across three levels; reported controller omnibus tests p<.05, with the named post-hoc differences.
-
-**Applicability, contrary evidence and unresolved question:** Predominantly student sample and restricted controller choices. No significant enjoyment effect in the responsiveness-tradeoff comparison; this is not equivalence. It does not justify “always prioritize responsiveness” or removing all embellishment.
+**Claim:** Evaluate visual appraisal and gameplay outcomes separately; a more favorable score on one need not justify the other. **Class:** `inference`. **Support:** C-03 and inspected P02 Feedback outcome separation. **Confidence:** moderate as a measurement safeguard. **Limit:** not a claim that visual quality is irrelevant. **Unresolved:** which outcomes should govern a later approved design decision.
 
 ### C-05
-
-**Claim:** Withhold a directional performance claim from the author manuscript’s internally inconsistent lives-lost discussion; its satisfaction claim also uses a weaker stated significance threshold. **Class:** `inference`. **Confidence:** high that the inspected text requires this qualification.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-005, §5.3–5.4, manuscript pp.26–28; §6, pp.31–33; P04-CON-04.
-
-**Applicability, contrary evidence and unresolved question:** §5.4’s fewer-lives comparison conflicts with its more-lives summary; §5.3 reports p<.1. Do not silently correct wording, upgrade certainty or treat null results as equality. Published full-text/author clarification remains missing.
+**Claim:** Unity 6.3 documents duration/exit/interruption controls for Animator transitions, not an automatic action-cancellation contract. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-006, Transition properties and Transition interruption. **Confidence:** high for documented scope. **Limit:** no engine verification or recommended settings. **Unresolved:** implementation-specific relation between action state and animation.
 
 ### C-06
-
-**Claim:** In a separate brief-viewing experiment, half-face freezing was unpleasant, while a static-eye manipulation did not significantly differ from the unaltered condition. **Class:** `empirical-evidence`. **Confidence:** moderate for the narrow stimuli.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-004, §5.2–5.2.1: 12 viewers, five render styles and manipulated male-character motion.
-
-**Applicability, contrary evidence and unresolved question:** Little horizontal head movement limits the static-eye comparison. No evidence that eyes are unimportant or any expression is universally interpreted; no gameplay or live-performance task.
+**Claim:** Epic’s root-motion facility can use animation data to drive displacement, distinct from movement driving visual animation. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-007, Overview/Root Motion/Results, UE 5.8. **Confidence:** high for attribution. **Limit:** no universal selection rule or benchmark. **Unresolved:** desired movement authority and action coverage.
 
 ### C-07
-
-**Claim:** The Unity 6000.3 manual distinguishes exit-time conditions, duration units and interruption ordering. **Class:** `observed-example`. **Confidence:** high for the inspected documentation artifact, not runtime validation.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-007, Properties and Transition interruption.
-
-**Applicability, contrary evidence and unresolved question:** Seconds and normalized portions are distinct. A transition facility is not gameplay cancellation permission, a measured latency or an instruction to use Unity.
+**Claim:** Epic’s networked Character Movement root-motion workflow leaves animation coordination responsibilities to gameplay. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-008, root-motion special-case movement paragraphs. **Confidence:** high for scoped documentation. **Limit:** not a general multiplayer protocol or proof of synchronization. **Unresolved:** authority, prediction and correction behavior in a later implementation.
 
 ### C-08
-
-**Claim:** UE 5.6 inertialization documentation states that the source stops being evaluated and its Animation Notifies stop after blending begins. **Class:** `observed-example`. **Confidence:** high for documented behavior, not execution.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-008, Inertialization, source evaluation and Animation Notifies paragraphs.
-
-**Applicability, contrary evidence and unresolved question:** Important completion information must not be assumed to arrive from a discarded source clip. That design consequence is an inference; exact runtime ownership needs separate implementation review.
+**Claim:** Epic documents pose-search motion selection with event-duplication and data/weight mismatch concerns. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-009, Overview, Anim Notify Filtering and Channel Weights. **Confidence:** high for documentation. **Limit:** no default timeout/weight, quality guarantee or performance comparison extracted. **Unresolved:** actual motion coverage, event semantics and validation cost.
 
 ### C-09
-
-**Claim:** UE 5.6 documentation distinguishes network smoothing and root-motion replication and states that matching animation playback is not automatically verified between server and autonomous client. **Class:** `observed-example`. **Confidence:** high for the stated component documentation.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-009, Network Smoothing; Replicating Special Case Movement with Root Motion → From AnimMontages.
-
-**Applicability, contrary evidence and unresolved question:** Not all networking models behave this way. Do not infer a universal prediction strategy, acceptable latency or competitive fairness result.
+**Claim:** The inspected Naughty Dog account identifies facial-rig/system and AI/traversal dependencies in expressive/locomotion production. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-010, UNCHARTED TERRITORY. **Confidence:** high for reported process. **Limit:** not measured response or causal proof of believability. **Unresolved:** applicable work and resources for another production.
 
 ### C-10
-
-**Claim:** Keep expressive preparation and gameplay commitment negotiable separately; immediate acknowledgement need not imply immediate action success. **Class:** `inference`. **Confidence:** moderate for the semantic argument; experienced benefit remains local.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-006, Anticipation; GDR-SRC-20261010-P04-007, transition conditions; reviewed P02 feedback timing and receipt/outcome distinction.
-
-**Applicability, contrary evidence and unresolved question:** An intentionally committed action is a valid countercase. Opponent warning may precede the player’s opportunity to respond. No fixed anticipation or cancel window is justified.
+**Claim:** Specify action phases, authorities, permitted exits and retained consequences before choosing or polishing transitions. **Class:** `inference`. **Support:** C-01/C-04–C-09 and inspected candidate ownership boundaries; the evidence-to-application bridge is in Core explanation. **Confidence:** moderate as consistency guidance, low for unmeasured benefit. **Countercase:** some action commitment is intentional and must remain. **Unresolved:** minimum useful phase model and value relative to a simpler specification.
 
 ### C-11
-
-**Claim:** A motion handoff should explicitly preserve or terminate the relevant action promises, rather than assuming visual smoothness proves state correctness. **Class:** `inference`. **Confidence:** moderate for the failure-prevention logic, untested player benefit.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-007–009, locators in C-07–C-09; GDR-SRC-20261010-P04-003, cosmetic hitbox account.
-
-**Applicability, contrary evidence and unresolved question:** Source and destination must have an agreed state owner. Cancel, buffer, blend and authority transfer are different operations. Local mechanics and network policy remain F04/implementation dependencies.
+**Claim:** A phase-aware presentation may preserve comprehension/control better than an unnecessarily clip-constrained alternative, without requiring all actions to be freely cancellable. **Class:** `hypothesis`. **Support:** C-03 is adjacent, not a direct test of this recipe. **Confidence:** low for a new application. **Limit:** changing commitment changes mechanics; cannot be called an animation-only improvement. **Unresolved:** matched local comparison and boundary conditions.
 
 ### C-12
-
-**Claim:** Judge authored, captured, procedural and hybrid motion by the required controllability and expressive range, not an assumed naturalness hierarchy. **Class:** `inference`. **Confidence:** moderate as a decision framework, not an empirical ranking.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-005, §6 limitations; GDR-SRC-20261010-P04-006, craft account; GDR-SRC-20261010-P04-003, rig and cross-skin production discussion.
-
-**Applicability, contrary evidence and unresolved question:** No inspected equal-budget comparison of motion-capture versus authored/procedural pipelines. Authorship, cleanup, contact correction and exceptions are cost categories, not measured savings.
+**Claim:** Intended expressive beats, their interpretation and their interruption/localization behavior should be investigated separately from literal action consequences. **Class:** `hypothesis`. **Support:** C-02/C-09, inspected W01/W02 distinctions and original P04 scenarios. **Confidence:** low for a particular interpretation. **Limit:** no culture-wide pose dictionary or expressive-equivalence study. **Unresolved:** language, performer, audience, view and repeat-exposure effects.
 
 ### C-13
-
-**Claim:** Reducing nonessential motion should be evaluated alongside access to required facts rather than assumed to preserve every effect or feeling. **Class:** `inference`. **Confidence:** moderate as a scoped guidance-to-design bridge.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-010, alternatives to visual-only cues; GDR-SRC-20261010-P04-011, moving UI/background exception and non-core animation; reviewed P02 information versus emotion.
-
-**Applicability, contrary evidence and unresolved question:** No blanket animation freeze, equivalent affect, medical safety or certification claim. Deafblind, sign-language and specialist tactile performance needs remain unresearched.
+**Claim:** Important animation-carried facts require appropriate access alternatives; optional motion controls do not imply removal of essential gameplay. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-05 and P01-10, freshly inspected implementation guidance. **Confidence:** high for attribution; usability untested. **Limit:** vendor guidance, not formal certification, safe-motion thresholds or emotional parity. **Unresolved:** actual alternative-route comprehension and comfort.
 
 ### C-14
-
-**Claim:** Treat expressive interpretation and intended character behavior as separate records; avoid diagnosing real people or standardizing one culturally preferred movement as normal. **Class:** `inference`. **Confidence:** moderate as an ethical/measurement safeguard, not an effect estimate.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-004, deliberately selected stimuli and brief ratings; reviewed W01 character-design, Decision and scope; W02 dialogue-and-voice, Performance is an interpretation.
-
-**Applicability, contrary evidence and unresolved question:** Nonhuman performers, languages, movement differences and cultures are not comprehensively represented. Specific casting/performance rights require separate review; no legal advice.
+**Claim:** Recipes, scenarios, measures and disconfirmation rules in this entry are proposed and unperformed. **Class:** `hypothesis`. **Support:** original P04 synthesis; F01’s selected transfer-discrimination correction constrains the proposed tests, not their results. **Confidence:** low for eventual usefulness. **Limit:** no prototype, participant or technical data. **Unresolved:** authorized study design, thresholds, sampling and feasibility.
 
 ### C-15
-
-**Claim:** The recipes, examples, measurements and comparisons here are proposed and have not been implemented or tested. **Class:** `hypothesis`. **Confidence:** low for unknown local effect and feasibility.
-
-**Support / precise locator:** Original P04 synthesis under the current brief; conditional applications of C-10–C-14.
-
-**Applicability, contrary evidence and unresolved question:** No recruitment, instrumented gameplay, latency measurement, network test, animation asset creation or participant result. Study choices must be agreed before a later authorized test.
+**Claim:** Doug’s dispatch authorizes bounded research and draft P04 artifacts only. **Class:** `studio-decision`. **Owner/date:** Doug, supplied P04 brief, 2026-10-10, Authorization Update/Assigned Outputs/boundaries. **Confidence:** high for explicit scope. **Limit:** no implementation, release, participant work, permanent IDs or Project changes. **Unresolved:** independent review and subsequent coordination decisions.
 
 ### C-16
-
-**Claim:** This animation deliverable is authorized only as a provisional P04 research candidate. **Class:** `studio-decision`. **Confidence:** high from explicit instruction.
-
-**Support / precise locator:** Doug’s P04 message and attached brief, Authorization update / Assigned outputs / Current jobs and boundaries; run dated 2026-10-10.
-
-**Applicability, contrary evidence and unresolved question:** Owner Doug. Independent review, permanent identity reconciliation, host validation, release and game implementation remain separate gates.
+**Claim:** A recent creator describes hand-keyed timing/posing and shared base animations with selective individual variation. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-011, Laygo animation answer. **Confidence:** high for attribution. **Limit:** pre-beta creator interview, not a tested current build, population response or cost benchmark. **Unresolved:** appropriate reuse, retargeting and identity for another production.
 
 ## References
 
-All public records below were inspected in the stated passages on **2026-10-11 UTC**. IDs are P04-scoped source records, not permanent SRC allocations. Dates of older works are publication dates, not claims of current game behavior. Repeated reference records support standalone reading; they are not extra evidence.
-
-### GDR-SRC-20261010-P04-003
-
-**ASU Team, Riot Games; named concept, character, technical-art and animation contributors.** [/dev: Modernizing the Monk](https://www.leagueoflegends.com/en-gb/news/dev/dev-modernizing-the-monk/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2024-04-08. **Edition/build:** Lee Sin art-and-sustainability update developer article; exact game build unspecified.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary multidisciplinary creator account. **Exact locators:** Creating Consistency Across Skins; Preparing the Ponytail; Base Meshes and 3D Sustainability; Animation → Making Lee’s Animations More Impactful, Float like a Butterfly, Sliding Hitboxes like a Lee, Making Skins with Style. **Claims supported in this entry:** C-03; indirect C-11/C-12.
-
-**Limits:** Intentions and reported production issues, not measured satisfaction, cost savings or a directly observed build. Animation contributors: Sean “Riot Redepoka” Yeung and Einar “Riot Beinhar” Langfjord. Embedded media not played. **Independence/deduplication:** Same production line as source 002; multiple contributors are not separate efficacy studies. Cross-batch deduplication pending. **Rights:** Reuse license not established; paraphrase only; no likenesses, media or assets copied.
+All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.
 
 ### GDR-SRC-20261010-P04-004
 
-**Rachel McDonnell, Martin Breidt and Heinrich H. Bülthoff.** [Render me Real? Investigating the Effect of Render Style on the Perception of Animated Virtual Humans](https://www.scss.tcd.ie/Rachel.McDonnell/papers/Siggraph2012a.pdf). **Publisher:** ACM Transactions on Graphics. **Publication/update:** 2012-07. **Edition/build:** 31(4), Article 91; eleven-page author PDF; DOI 10.1145/2185520.2185587.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original human perception experiments. **Exact locators:** §4 Choosing Render Styles; §5.1 Still vs. Moving, methods/results, PDF pages 4–6; §5.2 Motion Anomalies and §5.2.1 Results, PDF pages 6–7. **Claims supported in this entry:** C-06; context for C-14.
-
-**Limits:** Selected male-character stimuli and brief viewing tasks, not controlled gameplay. A deliberately ill-looking treatment complicates a neutral realism continuum. No raw-data reanalysis. PDF pages 5 and 7 visually inspected; the page-6 screenshot route failed. **Independence/deduplication:** Original study; author PDF and DOI/publisher record are one source. Cited by source 005: independent cohorts, not disconnected intellectual lines. Lowercase author-path route failed; uppercase path succeeded. **Rights:** ACM copyright; no new reuse permission inferred from author hosting. No figures or stimulus media redistributed.
+**John Lasseter. [Principles of Traditional Animation Applied to 3D Computer Animation](https://www.cs.utexas.edu/~fussell/courses/cs384g-fall2011/projects/animator/lasseter.pdf).** ACM Computer Graphics 21(4), SIGGRAPH 1987, pp. 35–44. Date: 1987-07. Edition/build: Original paper; University of Texas course-hosted copy.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Practitioner exposition with film examples. **Locators:** §2.2 Timing, printed p. 37; §§2.3–2.4 Anticipation/Staging, pp. 38–39; §2.5 Follow Through and Overlapping Action, p. 39. **Supports:** C-02; indirect C-10/C-12.
+
+**Limits:** Viewer-directed animation, not an interactive performance experiment. PDF text inspected; screenshot route failed. Historical anatomy/absolute claims and frame recipes not adopted. **Relationship:** Synthesizes earlier animation practice; those cited books were not independently inspected. **Rights:** Copyrighted paper; paraphrase only; no frames or figures redistributed.
 
 ### GDR-SRC-20261010-P04-005
 
-**Aline Normoyle and Sophie Jörg.** [The effect of animation controller and avatar on player perceptions](https://www.researchgate.net/publication/310603130_The_effect_of_animation_controller_and_avatar_on_player_perceptions). **Publisher:** Computer Animation and Virtual Worlds / Wiley; author manuscript via ResearchGate. **Publication/update:** First online 2016-11-20; journal issue 2018. **Edition/build:** 29(6), e1731; DOI 10.1002/cav.1731. Inspected author manuscript uploaded 2021-01-26; manuscript pagination, not journal pagination.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original controlled game experiment and separate observer study; primary author manuscript. **Exact locators:** §3.2–3.4, manuscript pp.12–17; §4.9, pp.23–24; §5.1 Control and §5.2 Enjoyment, pp.25–26; §5.3 Satisfaction, pp.26–27; §5.4 Performance, pp.27–28; §6 Conclusion and Future Work, pp.31–33. **Claims supported in this entry:** C-04/C-05; limitations for C-12.
-
-**Limits:** Publisher full-text request redirected to abstract; full manuscript text was read on the author-upload route. Exact equivalence to the version of record not verified. Restricted controller/task designs, mainly student sample and differing observer/player questions limit generalization. Internal performance-direction inconsistency retained as P04-CON-04. No footage, raw data or graph digitization used. **Independence/deduplication:** Cites source 004 and earlier work by these authors. Manuscript, abstract and DOI are one work, not multiple confirmations. Cross-batch deduplication pending. **Rights:** Author manuscript copyright; redistribution license not established. Attributed paraphrase only; no participant data copied.
+**Aline Normoyle and Sophie Jörg. [Trade-offs between Responsiveness and Naturalness for Player Characters](https://alinen.net/research/normoyle14Tradeoffs.pdf).** ACM, Motion in Games 2014. Date: 2014-11-06–08, conference dates. Edition/build: MIG 2014 paper; DOI 10.1145/2668064.2668087.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original game-controller experiment and separate video-rating calibration. **Locators:** §§3.2–3.4, PDF p. 4; §4.8, pp. 6–7; §§5.1–5.5, pp. 7–9; §6, p. 9. **Supports:** C-03; indirect C-04/C-11.
+
+**Limits:** One old controller/task family; relevant PDF prose inspected. Screenshots and local download failed; no graph digitization, table-only result or raw-data reanalysis used. **Relationship:** Shared Blend group in two comparisons is not an independent replication; later journal extension not inspected. **Rights:** ACM copyright notice; paraphrase only; source PDF not redistributed.
 
 ### GDR-SRC-20261010-P04-006
 
-**John Lasseter, Pixar.** [Principles of Traditional Animation Applied to 3D Computer Animation](https://cgvr.cs.uni-bremen.de/teaching/cg_literatur/Principles%20of%20traditional%20animation%20applied%20to%203D%20computer%20animation.pdf). **Publisher:** ACM SIGGRAPH Computer Graphics. **Publication/update:** 1987-07. **Edition/build:** 21(4), printed pp.35–44; university-hosted paper PDF.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary practitioner craft account. **Exact locators:** §2.2 Timing, printed p.37; §2.3 Anticipation, p.38; §2.4 Staging, pp.38–39; §2.5 Follow Through and Overlapping Action, p.39. **Claims supported in this entry:** C-02; indirect C-10.
-
-**Limits:** Film/computer-animation craft vocabulary, not an interactive-control experiment or formal standard. Fixed-frame anecdotes are not gameplay timing prescriptions. Text inspected; two web PDF screenshot attempts failed, so no figure-specific observation is claimed. **Independence/deduplication:** Historical craft source, not current engine guidance. CMU route failed; Bremen PDF text succeeded. Cross-batch edition deduplication pending. **Rights:** 1987 ACM copyright; no illustrations or extended passages reproduced.
+**Unity Technologies. [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html).** Unity Manual. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unity 6.3 LTS (6000.3).
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Transition properties (Fixed Duration, Transition Duration, Has Exit Time); Transition interruption; Interruption Source; Ordered Interruption. **Supports:** C-05; indirect C-10.
+
+**Limits:** Describes Animator transitions, not input buffering or automatic cancellation of gameplay consequences. No engine execution. **Relationship:** Independent vendor from Epic; two implementations are not evidence of better player outcomes. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-007
 
-**Unity Technologies.** [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html). **Publisher:** Unity Manual. **Publication/update:** Publication/update date unknown. **Edition/build:** Unity 6.3 / 6000.3 documentation, selected edition; no claim that it is the newest engine.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Properties → Has Exit Time, Fixed Duration, Transition Duration and conditions; Transition interruption → Interruption Source and Ordered Interruption. **Claims supported in this entry:** C-07; indirect C-01/C-10/C-11.
-
-**Limits:** Documents facilities and units; does not measure this project’s latency, responsiveness or cancellation policy. No engine execution. Recheck exact dependency version before implementation. **Independence/deduplication:** One vendor mechanism reference, not efficacy evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined. Paraphrase only, no code copied.
+**Epic Games. [Root Motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation; 5.6 route also inspected but not source of current-version claims.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Overview; Root Bone; Root Motion; Enabling Root Motion; Results. **Supports:** C-06; indirect C-10.
+
+**Limits:** One movement/animation facility; neither a universal motion authority rule nor an implemented benchmark. **Relationship:** Same Epic documentation family as networked movement and motion matching. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-008
 
-**Epic Games.** [Animation Blueprint Blend Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Inertialization: source evaluation, interruption, and Animation Notifies paragraphs; parsed text lines 121–150. **Claims supported in this entry:** C-08; indirect C-11.
-
-**Limits:** No benchmark or runtime test. Documented source-evaluation behavior does not by itself prescribe gameplay event ownership. Experimental facilities are not endorsed for shipping. **Independence/deduplication:** Same vendor as source 009, different page/mechanism. Version parameter is part of this source identity; central deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.
+**Epic Games. [Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Network roles/movement cycle; Replicating Special Case Movement with Root Motion; root-motion montage and Gameplay Ability System paragraphs (web extraction lines 194–218). **Supports:** C-07; indirect C-10.
+
+**Limits:** Character Movement workflow only; no general netcode guarantee, latency target or local synchronization test. **Relationship:** Same issuer and feature family as root motion, not a separate efficacy study. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-009
 
-**Epic Games.** [Understanding Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Network Smoothing; Replicating Special Case Movement with Root Motion → From AnimMontages; parsed text lines 174–203. **Claims supported in this entry:** C-09; indirect C-11.
-
-**Limits:** Character Movement Component behavior, not a universal networking model or proof of fair combat. No server/client, network or frame-time tests performed. **Independence/deduplication:** Same vendor as source 008. Distinct mechanism, not independent user-outcome evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.
+**Epic Games. [Motion Matching](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-matching-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Overview and Pose Search schema; Anim Notify Filtering; Pose Search Schema Channel Weights (web extraction lines 310–337). **Supports:** C-08; indirect C-10.
+
+**Limits:** Documented selection system and failure cases; no quality/cost/speed benchmark or recommended weights/timeouts. **Relationship:** Same Epic family; source demonstrations not played as independent observations. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-010
 
-**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal and Overview; Implementation guidelines → alternatives to color and visual-only information; simulation-filter and actual-player evaluation paragraphs. **Claims supported in this entry:** C-13.
-
-**Limits:** Practitioner guidance, not a formal standard, legal advice or certification. Availability of an alternative is not demonstrated usability or emotional equivalence. Public body inspected despite authorization boilerplate. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-05 and GDR-SRC-20261010-P02-005; central reconciliation pending. Same issuer as source 011. **Rights:** Vendor page; content reuse license not inspected; paraphrase only; no example media copied.
+**Dinah Bakeer; accounts by Marianne Hayden and Almudena Soria. [Uncharted 4: A Thief’s End: The 5-Year Anniversary Retrospective](https://www.naughtydog.com/blog/uncharted_4_a_thiefs_end_the_5_year_anniversary_retrospective).** Naughty Dog. Date: 2021-05-10. Edition/build: Retrospective on original PlayStation 4 production; engine/build number unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator retrospective. **Locators:** UNCHARTED TERRITORY, Hayden facial-capture and Soria traversal/AI paragraphs (web extraction lines 17–31). **Supports:** C-09; production context C-10/C-12.
+
+**Limits:** Production account, not measured interpretation, responsiveness or staffing savings; no gameplay footage inspected. **Relationship:** Independent production from Valve/Riot, with similar retrospective selection bias. **Rights:** Reuse license not established; paraphrase only.
+
+### GDR-SRC-20261010-P01-05
+
+**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-13.
+
+**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.
+
+### GDR-SRC-20261010-P01-10
+
+**Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Overview; Implementation guidelines; Moving/blinking/scrolling content and essential-gameplay exceptions; Camera movement options. **Supports:** C-13.
+
+**Limits:** No safe-motion numerical threshold or blanket removal of all gameplay animation; not certification. **Relationship:** Reuses P01-10; P02-010 duplicates this URL. Same issuer as XAG 103, not independent player evidence. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-011
 
-**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Implementation guidelines → moving/blinking/scrolling UI and its background-motion exception; camera motion; repetitive non-core animation; parsed text lines 43–121. **Claims supported in this entry:** C-13.
-
-**Limits:** Not a universal freeze-all-gameplay requirement, medical safety threshold or certification. No FOV, flashing or animation-duration limit is extracted. Camera-setting research remains P03 ownership. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-10 and GDR-SRC-20261010-P02-010; central reconciliation pending. Related vendor guidance is not independent efficacy evidence. **Rights:** Vendor page; content reuse license not inspected; paraphrase only.
+**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-beta creator interview; Unreal Engine 5, minor/build unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator interview. **Locators:** Questions about stylized likeness and character animation; Johnston/Laygo answers, web extraction lines 57–67. **Supports:** C-16, animation portion only.
+
+**Limits:** Design intentions and reported reuse, not measured responsiveness, audience response, savings or a current release-status claim. **Relationship:** Separate production from Valve/Riot/Naughty Dog; hosted by its engine vendor, with promotional incentives. **Rights:** Reuse license not established; paraphrase only; no media redistributed.
 
 ## Open questions and change history
 
-Open coverage: action-specific cancellation/commitment from F04; actual P03 view/display constraints; locomotion/contact systems beyond the inspected documentation; modern equal-budget capture/procedural/authored comparisons; cross-cultural expressive interpretation; sign-language and facial-localization requirements; networked owner/observer outcomes; and measured production/performance budgets.
-
-P04-CON-03 retains control versus authored commitment as a contextual design tradeoff. P04-CON-04 retains the manuscript reporting inconsistency and weaker satisfaction threshold; it is not resolved by assuming a typo. The selected evidence does not validate an entire animation pipeline or fixed timing recipe.
-
-**2026-10-11 UTC:** initial 0.1.0 draft, revision initial-draft-1, no predecessor/supersession. Author self-review only; independent review, host validation, canonical identity allocation and release remain pending. The next decision is review/revision and dependency reconciliation, not engine adoption, participant work or game implementation.
+| Subtopic | Inspected coverage | Remaining question/dependency |
+|---|---|---|
+| Anticipation, posing and timing | Original practitioner account and recent hand-keyed production rationale. | Which actor/viewer needs prediction, and when is preparation redundant? |
+| Responsiveness versus naturalness | One older game-controller experiment plus separate video calibration. | Matched-commitment comparison with modern controllers and target populations. |
+| Blending, exit timing and interruption | Current Unity documentation and phase-consistency synthesis. | Does the actual action remain true through every permitted exit? |
+| Root/movement authority and network context | Current Epic documentation; no implementation or traces. | Reconcile action, movement, prediction and visual completion with an authorized system design. |
+| Motion selection and transitions | Current motion-matching facility/failure documentation. | Out-of-coverage states, event semantics and actual production/runtime cost. |
+| Expressive behavior and performance | Creator dependencies and inspected W01/W02 distinctions. | Direct interpretation evidence across locale, retargeted bodies, interrupted/repeated beats and small views. |
+| Access and sensory comfort | Current scoped XAG guidance; no safe numerical setting. | Essential-fact preservation with actual users and chosen settings; P03 bytes still missing. |
+| Combat/traversal-specific commitment | Logical countercases only, not F04 guidance. | Inspect F04 before asserting mechanical defaults or genre-sensitive cancel policies. |
+
+P04-CON-03/04/05/06 remain open in the packet. The localized-expression extension is queued as child work, not a third pattern or completed evidence. No inference of whole-heading completion follows from this file existing.
+
+**History:** 2026-10-10, version 0.1.0 / initial-draft-1; first P04 submission; predecessor/supersession null. Late creator-source inspection added C-16 without reallocating existing claims. Author self-review is not independent review. Gates C, D and E remain unpassed for this candidate. See the [review packet](../reviews/full-run-20261010-p04-review-packet.md) and [integrity receipt](../reviews/full-run-20261010-p04-integrity-receipt.md).

```
