# Preserved GDR-CAND-20261010-P04-PAT-02-comparison.diff

Original payload SHA-256: `927100af203d3cb56b0eed556cd02a398245885e81a1dac0b75b228a2bf7abf8`. Complete original record follows in Markdown.

```text
--- earlier/state-aligned-animation-handoff.md
+++ later/action-phase-and-interruption-contract.md
@@ -1,7 +1,7 @@
 ---
 id: GDR-CAND-20261010-P04-PAT-02
 kind: pattern
-title: State-aligned animation handoff
+title: Action-phase and interruption contract
 version: 0.1.0
 candidate_revision: initial-draft-1
 status: draft
@@ -9,308 +9,218 @@
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
-- animation state handoff
-- interruptible motion handoff
+- animation cancellation contract
+- state-consistent animation exits
 tags:
 - animation
+- action-state
 - interruption
-- state-clarity
 - recovery
 - conditional-recipe
 related_topics:
 - GDR-CAND-20261010-P04-TOP-02
-- GDR-CAND-20261010-P04-TOP-01
 related_patterns:
 - GDR-CAND-20261010-P04-PAT-01
 related_genres: []
 source_ids:
-- GDR-SRC-20261010-P04-005
+- GDR-SRC-20261010-P04-006
 - GDR-SRC-20261010-P04-007
 - GDR-SRC-20261010-P04-008
-- GDR-SRC-20261010-P04-009
-- GDR-SRC-20261010-P04-010
-- GDR-SRC-20261010-P04-011
+- GDR-SRC-20261010-P01-05
 reviewer: null
 approved_by: null
 approved_date: null
+predecessor_sha256: null
+supersedes: null
+change_summary: Initial P04 submission; does not replace or resend any previous batch.
+byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
-# State-aligned animation handoff
-
-**Draft 0.1.0 / initial-draft-1; hypothesis-led, not implemented or validated.** This pattern coordinates how one action’s visible motion gives way to another without falsely changing what the game permits or has completed. It is not a recommendation that every action be cancellable or that every transition be smooth. [C-01, C-02, C-08]
+# Action-phase and interruption contract
+
+**Draft 0.1.0; initial-draft-1. A conditional design-inference pattern, not a validated control system, approved implementation or released rule.**
 
 ## Purpose
 
-Make acceptance, interruption, commitment and recovery legible when animation changes. The intended benefit is fewer misleading state transitions while retaining the expressive motion the situation warrants. The owning [Animation and performance topic](../topics/animation-and-performance.md) provides alternatives and empirical limits. [C-01, C-04]
-
-The pattern owns **motion-state handoff obligations**. P02 owns input mapping, retained intent and broader feedback semantics; its cue-alternative pattern remains responsible for fact-preserving modality choices. This is not a second remapping or redundant-cue recipe. [C-02, C-06]
+Keep an action’s true state, visible performance and permitted exits consistent when animation is blended, interrupted, replaced, replayed or completed. The intended benefit is understandable action and recovery, not universal instant cancellation. A smooth clip can be successful art while communicating the wrong current state. The value of this full recipe has not been experimentally established. [C-01]
 
 ## Context and prerequisites
 
-Consider the pattern when an action can be interrupted, redirected, denied, superseded or visually blended while important state information must remain accurate. It may apply to a controlled character, an interactive object or an observed actor, but their promises differ. [C-01, C-02]
-
-The future design needs an identifiable action/state owner, agreed cancellation and commitment policy, named important outcomes and a way to inspect transitions under actual input/view conditions. When networking matters, identify whose state is authoritative and whose presentation is being evaluated. These are prerequisites to a meaningful review, not a mandated runtime architecture. [C-02, C-03, C-05]
-
-**Exit before authoring:** when gameplay permission or result ownership is unresolved, record the question and stop at design review. A blend graph cannot settle an undefined rule. Current F04/P03 dependencies are missing; this pattern supplies no substitute numerical settings or combat/traversal policy. [C-02, C-07, C-08]
+Use when a meaningful action can be interrupted or its visual phases can differ from its actual consequences. The designer must know what the action does, when consequences become committed, what can interrupt it, which facts the player needs, and who owns those facts. It applies to movement, manipulation or an expressive beat only where those distinctions are useful; a simple noninteractive loop may need none of this structure. [C-02]
+
+Declare player/NPC authority, input path and assistance, view and actor visibility, motion preferences, local/network roles, action persistence and relevant cultural/language context. For a purely observed performance, do not invent player input acknowledgement. For a player-controlled actor, do not imply that an expressive gesture guarantees the requested outcome. [C-02]
+
+Inspected parent P02 control/feedback distinctions inform this pattern; the selected F07 safe-exit pattern concerns broader commitments and retained stakes, G02 bounded-action-grace concerns eligibility leniency, and W02 intent-and-response concerns the meaning of selected dialogue. P04 owns the narrower **animation/action phase and exit consistency record**. Relationships remain provisional, not a merge or independently approved new canonical home. See the [overlap record](../reviews/full-run-20261010-p04-review-packet.md#pattern-ownership-and-overlap). [C-02]
 
 ## Mechanism and evidence
 
-| Proposed link | Support and limit |
-| --- | --- |
-| Identify the actual permission/state change. | Reviewed P02 distinctions and source 007 motivate the decomposition; no single required state count. [C-02] |
-| Carry forward or terminate each important promise explicitly. | Source 008 documents why source-clip continuation cannot simply be assumed. The ownership rule is an inference. [C-03] |
-| Present the destination without implying false acceptance or completion. | Logical information-to-action bridge; end-to-end comprehension untested. [C-01] |
-| Preserve useful expression and perceived control. | Source 005 motivates separate measures, not a guaranteed improvement from this recipe. [C-04] |
-| Preserve required facts under settings and authority differences. | Guidance and component documentation identify constraints; usability and remote fairness remain untested. [C-05, C-06] |
-
-A mechanically correct action can still look misleading, and a persuasive motion can describe a mechanically incorrect state. Neither smoothness nor an animation editor preview certifies the full chain. [C-01, C-04]
+The [Animation and performance topic](../topics/animation-and-performance.md) owns the empirical and technical comparison. The pattern draws a design inference from facilities that separate visual transitions, movement and action authority. It does not treat a vendor API as evidence that the proposed recipe improves players. [C-01, C-03]
+
+| Candidate causal link | Support | Limit |
+|---|---|---|
+| Name true action phases independently of clip playback. | P02 state distinctions and the documented separation of animation/movement responsibilities. | A phase model is an authoring convention, not a standard state machine. [C-02, C-03] |
+| Specify exits and retained consequences. | An interrupted visual sequence need not correspond to reversal of its underlying action. | Consistency logic; not a measured reduction in errors. [C-01, C-02] |
+| Communicate only the state actually reached. | P02 distinguishes acknowledgement, pending and confirmed outcome. | The chosen presentation still needs an actual comprehension test. [C-04] |
+| Compare equivalent commitments, not just similar clips. | The owning topic’s narrow controller evidence warns against conflating appearance and task effects. | It does not validate this complete recipe or prove a responsiveness-first policy. [C-01, C-05] |
+| Retain readable state through alternative access routes. | XAG 103 supplies additional-channel guidance. | Information availability is not usability or equal experience. [C-04] |
 
 ## Recipe
 
-**Proposed for a later authorized design/prototype, not execution now.** [C-07, C-08]
-
-### 1. State the current and requested actions
-
-Record the current action, destination request, target/context and whether the request is merely received, permitted now, retained for later or denied. Include what the player should know, not only the internal label.
-
-**Branch:** a denied request must not receive the destination’s accepted-action presentation. A retained request must not be treated as a completed action. Intentional ambiguity about a character’s motive may remain; required action permission cannot silently become ambiguous. [C-01, C-02]
-
-### 2. Mark the permitted handoff conditions
-
-Specify what allows replacement: a state condition, a commitment boundary, an external event or a valid target. Record whether new intent replaces old intent and what invalidates a retained request. Do not derive permissions from a clip’s convenient blend point alone.
-
-**Exit:** when the task deliberately prohibits cancellation, keep the committed state and provide an appropriate denied/pending presentation. Changing the policy is a separate mechanics decision, not a visual polish fix. [C-02]
-
-### 3. Inventory the promises that cross the boundary
-
-For this action, identify relevant movement/contact, held object, target, completion result, active-effect indication and next-action readiness. Not every action needs every field. Mark each obligation as retained, terminated, replaced or still pending.
-
-**Stop:** if an important result depends on a source presentation event that may disappear under the selected handoff, do not assume it will occur. Assign its intended ownership for later implementation review, including prevention of duplicate completion. [C-03]
-
-### 4. Choose the visible destination and transition
-
-Compare an explicit pose change, short authored transition, conventional blend, adaptive handoff or continuing partial-body settling. Choose based on what must remain readable and what motion continuity is worth in this task, not a blanket preference for the smoothest result.
-
-**Adjustable variables:** source/destination pose coverage; transition duration and its declared units; ordering/priority of interruptions; retained body regions; contact or tool-release presentation; extent of optional follow-through; readiness cue; and allowed target changes. All values are local design/test variables, not sourced universal settings. [C-02–C-04]
-
-### 5. Inspect the semantic transition, not just the visual seam
-
-Ask whether the destination implies an accepted action, a valid contact or a completed outcome that the rules do not support. Examine interruption while a transition is already occurring, not only transitions from a settled idle. Include target loss, pause/resume, denied replacement and repeated input.
-
-**Branch:** if a smooth handoff obscures release, denial or readiness, compare a simpler explicit change. Do not hide disagreement with extra effects. [C-01, C-03, C-04]
-
-### 6. Check authority and access variants where relevant
-
-For a networked case, distinguish local pending/predicted presentation, accepted outcome and observer presentation; record what corrections are allowed to communicate. For preferred motion/access settings, preserve a usable route to each required state fact without promising identical feeling.
-
-**Exit:** do not approve a variant whose authority or required fact route cannot be evaluated. Restrict the claim to the actual tested context; offline inspection does not validate remote behavior. [C-05, C-06]
-
-### 7. Evaluate with contrasting decisions and retain only supported handoffs
-
-Include cases in which replacement should succeed, should be denied and should become invalid before consumption. Obtain state/permission predictions before feedback. Separate comprehension and control outcomes from expression and comfort.
-
-**Reject or revise:** lost/duplicated essential outcome, false acceptance, unavailable critical fact or recurring misinterpretation of readiness. If extra continuity adds no credible local value and increases maintenance, use the simpler alternative. Preserve intentional commitment; do not “repair” every refusal into a cancel. [C-01–C-07]
-
-### Proposed handoff record
-
-| Field | Required question |
-| --- | --- |
-| Source and destination | What is ending and what has actually been requested? |
-| Permission | Allowed now, denied, pending or invalidated — under which condition? |
-| Preserved / terminated obligations | Which result, contact, target or held object survives? |
-| Visible account | What should owner/observer believe at each meaningful change? |
-| Readiness | What makes another action valid, and how is that available to the player? |
-| Failure and exit | What would require a simpler handoff, policy clarification or stopping this variant? |
-
-This is a proposed review record, not a schema installed in a harness. [C-07, C-08]
+### 1. Write the action and its consequence
+
+State what is requested or triggered, what becomes different in the world, and what remains outside the actor/player’s control. Identify whether the action is reversible, cancellable before a consequence, interruptible after it, or simply skippable in presentation. Avoid treating those as synonyms. [C-02]
+
+**Exit:** if the team cannot state the consequence or who owns it, stop polishing transitions and resolve the design ambiguity. No animation-only repair can define an unknown commitment honestly. [C-06]
+
+### 2. Use only the phases the action needs
+
+Candidate phases are receipt/trigger, pending eligibility, acceptance, preparation, commitment, consequence, recovery and control return. Merge phases when they truly coincide. Record what makes each phase true rather than prescribing that a particular clip timestamp always controls it. [C-02]
+
+For each phase, record: true facts; visible and alternative presentation; progression condition; permitted interrupting events; retained/changed consequences; next allowed action; pause/re-entry behavior; authority where relevant. The record can be a short table rather than an elaborate system. [C-02]
+
+### 3. Define interruption before choosing its blend
+
+For each important interruption, distinguish stopping the visual action from stopping the underlying action. Specify the next valid pose/behavior and the actual next state. Include denial, conflicting commands, external interruption, repeated request, late cancel and recovery after a changed context. Do not promise rollback merely because a blend is easy. [C-02, C-03]
+
+**Branch:** when a deliberate commitment is part of the task, preserve it and make its boundary understandable. The pattern is not permission to cancel every action or remove an agreed cost. When an optional flourish unnecessarily blocks a valid next action, compare a presentation-only exit. [C-01, C-06]
+
+### 4. Choose transition and movement responsibilities
+
+Select authored transitions, a movement-driven visual layer, root-driven movement, pose selection or a simpler presentation according to the action’s needs. Unity’s transition interruption controls and Epic’s movement facilities are implementation examples, not engine mandates. [C-03]
+
+**Variables:** what initiates motion; which phases can overlap; event ownership; animation playback/blend duration and units; priority of interruptions; recovery pose; semantic meaning of repeats; alternate state presentation. No universal frame count, timeout, blend length or root-motion policy is supplied. [C-03, C-05]
+
+For networked use, record which participant’s view is provisional and what confirms the consequence. A local visual sequence is not sufficient proof of shared state. Keep the actual replication/prediction design with its authorized implementation owner. [C-03]
+
+### 5. Align acknowledgement and expression with truth
+
+A request acknowledgement must not depict confirmed success while the action is still pending. A successful transfer can retain its consequence after a decorative settle is skipped. A resumed expression should still make sense in the new context. Preserve the legitimate unknowns without obscuring required state or exit information. [C-04]
+
+Evaluate the actual view and chosen motion/access settings. Do not add mandatory visual busyness merely because a key pose exists in the animator’s reference. Provide an appropriate alternative for important information and review whether its meaning differs. [C-04, C-05]
+
+### 6. Compare normal and adversarial sequences
+
+After separate authorization, test normal completion and the important exits. Include paired cases with the same visible interruption but different true consequences. Predict the current state before asking what the participant wishes to do next. A repeated “cancel means no effect” answer should not pass a set containing a post-consequence exit. [C-05]
+
+**Stop:** contradictory state presentation, duplicated/forgotten consequences or an inaccessible essential exit blocks recommending that version. Fix the semantic mismatch before treating a cleaner transition as success. Distress/withdrawal stops a participant session. [C-06]
+
+### 7. Keep, simplify or restrict
+
+Compare the contract and its presentation with a simpler valid action. Retain only phases and exceptions needed to preserve the actual promise. If added flexibility changes the intended challenge, record that as a mechanics change needing separate approval, not a pure animation improvement. Reopen review when action consequences or interruption policy change. [C-01, C-05, C-06]
 
 ## Worked examples
 
-### Illustrative — changing intent during inspection
-
-**Synthetic; no game build, animation or test.** A controlled actor begins inspecting a panel. Turning away is allowed before commitment; after commitment it is denied until the result or a defined cancellation outcome. [C-07]
-
-| Situation | Actual policy in this illustration | Required presentation question |
-| --- | --- | --- |
-| Turn request before commitment | Replace inspection with turning. | Does inspection visibly end without implying a result? |
-| Turn request after commitment | Deny replacement. | Can the player tell inspection remains active rather than thinking the turn was accepted? |
-| Retained next action loses its target | Invalidate the retained request. | Is a stale action prevented from appearing to succeed after recovery? |
-| Inspection result becomes available during settling | Result exists; settling is optional. | Does the remaining motion falsely imply that control is still unavailable? |
-
-The exact policies are illustrative choices, not library recommendations. The recipe’s value is that each outcome has a clear question and can be contradicted by a later test. If a source animation stops being evaluated, the future implementation must still honor the action’s specified outcome ownership; no engine code is supplied here. [C-02, C-03, C-07]
-
-Compare the candidate with a neutral explicit handoff and with the original committed presentation under the same policies. Aesthetic continuity may be valuable, but it does not compensate for showing a cancelled inspection as complete. [C-01, C-04, C-07]
-
-### Illustrative — remote movement correction
-
-An observing player sees another actor start a movement whose acceptance is not yet settled locally. The design must decide whether that view communicates preparation, prediction or confirmed motion and what a correction means. This pattern asks for those distinctions; it does not choose a netcode solution, permitted correction distance or fairness rule. A local-only test cannot answer this case. [C-05, C-07]
+### Illustrative: module extraction
+
+**Invented; no engine, asset or participant test was created.** An agent removes a service module. The player can withdraw the request before the module leaves its socket. After transfer, skipping the final settle leaves the module transferred; it does not put it back. An explicit return-module action would be different. [C-05]
+
+| Event | Proposed true result | Permitted presentation/exit |
+|---|---|---|
+| Request arrives while availability is unresolved. | Pending; no module transferred. | Acknowledge receipt without depicting success. Cancel the pending request where the contract permits. |
+| Preparation begins with eligibility confirmed. | Accepted but not yet transferred. | Reach/brace; pre-transfer cancellation returns to a valid original state. |
+| Transfer is committed. | Module has changed location under the actual rule. | Show that result. Interrupting the remaining performance retains it. |
+| Another event interrupts recovery. | Transfer remains; actor must respond from a valid new state. | Leave the flourish or settle, then present the permitted next behavior. |
+| A late duplicate request arrives. | It does not automatically create another module transfer. | Present the actual eligibility/result; input policy remains with Controls/Foundations. |
+
+A test should ask about one cancellation before transfer and another visual exit after transfer. Their correct retained-state answers differ. Add unfamiliar actions with the same distinction to examine transfer, rather than repeating the same two familiar clips. This preserves F01’s corrected test-discrimination principle, not its numerical example. [C-05]
+
+### Illustrative: an interrupted expressive beat
+
+An agent starts a greeting but turns to address an urgent task. Restarting the greeting is not automatically appropriate, and resuming an old smile need not preserve the intended tone. The design can finish a brief acknowledgement, drop the greeting, or defer it if still relevant. The literal task outcome and the audience’s emotional interpretation require different checks. This is a candidate application, not a gesture-equivalence finding. [C-04, C-05]
 
 ## Tradeoffs and alternatives
 
-Explicit handoff ownership adds design and verification work, particularly when outfits, tools, target changes and access variants multiply combinations. A fully committed clip can be simpler and more expressive when its rule is appropriate. A minimal explicit transition can communicate state better than preserving continuous motion. Hybrid or partial-body movement can retain expression but create inconsistent implications between body regions. These are tradeoffs to test, not established rankings. [C-02–C-04, C-07]
-
-The alternative of changing the mechanic itself may be valid but must be recognized as such. Allowing earlier cancellation, longer retained intent or a different recovery condition changes the task and may change fairness or difficulty. Those are not incidental consequences to smuggle in under an animation refinement. [C-02, C-05]
+More explicit exits increase authoring and verification work. Very permissive exits can remove deliberate physical stakes; very rigid playback can impose costs that were never part of the intended choice. The useful comparison is the **same underlying commitment** presented and recovered differently. [C-01, C-02]
+
+Alternatives include a whole-clip action with a clearly disclosed commitment, an immediate action with little performed detail, fewer action variants, a short acknowledgement while the real outcome remains pending, or a fixed scene without claimed player control. A design may choose slower embodied action for a particular purpose; this pattern asks that its truth and exits remain coherent, not that it be made fast. [C-06]
 
 ## Failure cases
 
-| Warning sign | Likely question to investigate | Stop or repair proposal |
-| --- | --- | --- |
-| The old success effect appears after cancellation. | Was a terminated promise retained? | Correct ownership and test cancellation cases. |
-| A necessary result never appears after blending. | Was completion tied to a discarded source event? | Block advancement until its disposition is defined. |
-| A new action animates but rules reject it. | Did visible transfer occur before permission? | Show receipt/denial rather than acceptance. |
-| A ready actor still looks locked to the old target. | Does follow-through imply mechanical commitment? | Separate readiness or choose a clearer exit pose. |
-| Repeated interruptions produce unreadable motion. | Is continuity hiding state or exceeding pose coverage? | Restrict or simplify the visual handoff; do not silently change mechanics. |
-| Observer and owner infer contradictory outcomes. | Are prediction and authority distinctions missing? | Restrict the claim and investigate the actual network policy. |
-| Reduced motion loses the only critical cue. | Was required information treated as ornament? | Restore a usable fact route and test its interpretation. |
-
-These warning signs and remedies are hypotheses for future evaluation, not observed P04 results. [C-01–C-07]
+A success flourish while the action is pending misrepresents state. A cancelled animation that leaves an unexplained completed consequence misrepresents cancellation. A recovery pose that repeats an already committed event risks duplicating presentation or, in a flawed later implementation, consequences. A technically valid resumed gesture may no longer fit the character’s current situation. These are proposed diagnostic failures, not bugs observed in a shipped game during P04. [C-02, C-04, C-05]
+
+Repair the truth-to-presentation relationship first; then adjust transition polish, pose selection, event handling or alternative information. Do not attribute every failure to timing, or claim that one engine facility handles all consequence and network cases automatically. [C-03, C-06]
 
 ## Counterexamples and do not use conditions
 
-Do not use this as a mandate for cancellation during deliberate commitment, as a demand for input acknowledgement in a wholly noninteractive performance, or as permission to rewrite network authority. Do not add a complex handoff matrix when an existing simple state change already satisfies the task. Do not preserve continuity at the expense of an honest action result. [C-02–C-05]
-
-The strongest opposing case is that the action’s intention is best served by a clear committed sequence and a straightforward recovery. An intricate handoff could increase errors and costs while weakening expression. The inspected study and documentation do not prove this recipe wins that comparison. [C-01, C-04]
+A planning task may deliberately require committing to an action before its result. Removing that commitment can improve completion by making a different task. A purely decorative, noninteractive background cycle may also need no action-state contract. In both cases, applying every phase in this recipe would overreach. [C-06]
+
+Do not use this as a universal cancel-window specification, a rollback guarantee, an input buffer, a general safe-exit/monetization policy, a legal consent model, or a claim that smoother/longer/shorter animation is always preferable. Missing authority, unresolved essential access, or an unhonorable exit promise is a reason to stop this recommendation, not fill the gap with an invented engine rule. [C-02, C-03, C-06]
 
 ## Playtest
 
-**PROPOSED — NOT RUN.** Compare existing, proposed and minimal handoff presentations under identical cancellation/commitment rules. A separate mechanics factor is necessary when permissions themselves change. Include valid, denied, pending, invalidated and repeated-interruption cases. Counterbalance exposure, use matched tasks and collect permission predictions before feedback. [C-07]
-
-Participants should include relevant familiarity and actual access/input users; identify owner/observer roles where networking is part of the question. Measure false acceptance/cancellation beliefs, lost/duplicated outcomes, readiness errors, recovery behavior and separate control/expression/comfort reports. View, device, prior learning, mechanical differences and display/network conditions are confounds; record rather than conceal them.
-
-Reject a version with an essential unavailable fact, lost/duplicated result or misleading acceptance. Reject the proposed mechanism when benefits depend on changed permissions rather than motion communication. Retain an expressive handoff only when its local value and cost are supported under predeclared criteria; inconclusive findings do not establish equivalence. No universal duration, sample size or power guarantee is supplied. No test, participant recruitment, network measurement or implementation is authorized by this draft. [C-01, C-04–C-08]
-
-## Claim ledger
-
-Claim IDs are local to this entry. Confidence describes the exact scoped wording, not a source’s prestige or the recipe’s overall efficacy. Proposed procedures and examples are not approved studio decisions.
+**PROPOSED — NOT PERFORMED.** The owning topic contains the full plan. Compare a valid whole-clip action, a selectively interruptible phase-aware presentation with the same true consequences, and a simpler presentation. Separate experiments that alter the actual commitment from animation-only comparisons. [C-05]
+
+After an authorized protocol establishes sample/precision and relevant access populations, counterbalance action family/order where feasible. Observe ordinary completion, pre-commit cancellation, post-consequence exit, denial, external interruption and repeated requests. Include novel cases with both retained and absent consequences. Record true state, perceived state and next-action preference separately; later instrumentation must distinguish acknowledgement, effective action and control return. Report enjoyment, expressive interpretation and comfort separately from errors or completion time. [C-05]
+
+Reject or narrow the claim when the apparent benefit relies on easier mechanics, repeated answers, omitted negative cases or mismatched views/input. Revise any critical state/exit misinformation before advancement. An inconclusive result does not prove equivalence; select local acceptance tolerances before collecting data. No participant, prototype, technical measurement or adopted threshold exists in this research. [C-05, C-06]
+
+## Claim ledger and sources
 
 ### C-01
-
-**Claim:** Explicitly separating permission, motion transfer and result ownership may reduce misleading action-state presentation. **Class:** `hypothesis`. **Confidence:** low for the complete recipe; no direct validation.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-007–009, transition/inertialization/network-root-motion locators; animation-and-performance C-07–C-11.
-
-**Applicability, contrary evidence and unresolved question:** Documentation supports possible failure mechanisms, not a measured reduction in errors from this workflow.
+**Claim:** A phase/exit contract is a useful candidate consistency method, not a proven responsiveness-first rule. **Class:** `inference`. **Support:** owning topic C-01/C-04/C-10; source facilities in C-03 and original causal bridge. **Confidence:** moderate for conceptual separation, low for local efficacy. **Unresolved:** complete-recipe benefit and minimum useful complexity.
 
 ### C-02
-
-**Claim:** Gameplay cancellation, queued intent and animation interruption are distinct operations and should not silently stand in for one another. **Class:** `inference`. **Confidence:** moderate for the semantic distinction.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-007, transition interruption; reviewed P02 controls-and-input, Timing path; feedback-and-game-feel, Action receipt versus outcome.
-
-**Applicability, contrary evidence and unresolved question:** Intentional commitment remains valid. No universal cancellation permission or buffer duration is implied.
+**Claim:** Distinguish actual commitment, presentation, cancellation, recovery and ownership; not every action needs every phase. **Class:** `inference`. **Support:** inspected P02 candidate distinctions and F07/W02/G02 boundary inspection; owning topic C-10. **Confidence:** moderate for consistency. **Limit:** no prescribed state machine. **Unresolved:** valid exits for the actual task and overlap acceptance by Coordination.
 
 ### C-03
-
-**Claim:** A handoff needs an explicit disposition for important action outcomes when source motion may no longer be evaluated. **Class:** `inference`. **Confidence:** moderate for the reasoning; implementation not verified.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-008, Inertialization, source evaluation and Animation Notifies paragraphs; animation-and-performance C-08.
-
-**Applicability, contrary evidence and unresolved question:** This is an event-ownership question, not an instruction to install an engine, use one notify system or implement code.
+**Claim:** Documented transition, root-motion and network facilities address different responsibilities. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-006, Transition properties/interruption; P04-007, Overview/Results; P04-008, root-motion special-case movement. **Confidence:** high for scoped documentation. **Limit:** no engine run, replication guarantee or universal settings. **Unresolved:** a separately authorized implementation’s exact responsibilities.
 
 ### C-04
-
-**Claim:** Smoothness, apparent naturalness and control outcomes should be evaluated separately. **Class:** `inference`. **Confidence:** moderate from a narrow experiment and distinct constructs.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-005, §5.1–5.3 and §6; owning animation-and-performance C-04/C-05.
-
-**Applicability, contrary evidence and unresolved question:** No universal ordering of expressivity and control. Internal performance-direction inconsistency prevents transferring that result. No comparison here establishes equal quality.
+**Claim:** Acknowledgement, actual outcome and interpreted expression should remain distinguishable through appropriate access routes. **Class:** `inference`. **Support:** owning topic C-01/C-12/C-13; inspected P02 feedback and W02 performance distinctions; GDR-SRC-20261010-P01-05 Implementation guidelines. **Confidence:** moderate for the information distinction; affective result unknown. **Unresolved:** actual understanding under selected presentation/context.
 
 ### C-05
-
-**Claim:** Compare the owner’s and observer’s presented states when networked movement or predicted action is relevant. **Class:** `inference`. **Confidence:** moderate for the need to check the specific system.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-009, Network Smoothing and root-motion From AnimMontages paragraphs.
-
-**Applicability, contrary evidence and unresolved question:** Not every game uses these components; no latency/fairness threshold, prediction architecture or network test is supplied.
+**Claim:** Recipe benefits, examples and tests are hypotheses, not results. **Class:** `hypothesis`. **Support:** original P04 synthesis and selected F01 transfer-discrimination correction; owning topic C-11/C-14. **Confidence:** low for effectiveness. **Limit:** no prototype, participants, numeric defaults or actual QA of action behavior. **Unresolved:** approved protocol, matched commitments and relevant populations.
 
 ### C-06
-
-**Claim:** A reduced-motion or alternative presentation must be checked for required state facts independently of expressive equivalence. **Class:** `inference`. **Confidence:** moderate from scoped vendor guidance.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-010, critical visual information alternatives; GDR-SRC-20261010-P04-011, non-core motion and background exception; reviewed P02 information contract.
-
-**Applicability, contrary evidence and unresolved question:** No medical safety claim, blanket animation freeze or guarantee that another modality conveys the same emotion.
+**Claim:** Preserve deliberate stakes and stop when an action’s truth, exits or essential information cannot be represented honestly. **Class:** `inference`. **Support:** C-01–C-05 and explicit task contract. **Confidence:** moderate as scope/stop guidance. **Limit:** not a claim that every action must be cancellable or reversible. **Unresolved:** later project owner’s acceptable commitment and assistance policy.
 
 ### C-07
-
-**Claim:** The interruption matrix, examples and falsifying comparisons are proposed local methods, not performed tests or authorized implementation. **Class:** `hypothesis`. **Confidence:** low for untested effect and feasibility.
-
-**Support / precise locator:** Original P04 synthesis under the dispatch; reviewed F01 corrected contrasting-response test structure.
-
-**Applicability, contrary evidence and unresolved question:** No engine, network, input instrumentation, assets or participants. Sampling and practical decision tolerances need a later study owner.
-
-### C-08
-
-**Claim:** This pattern remains a provisional P04 draft, not an accepted controller or animation architecture. **Class:** `studio-decision`. **Confidence:** high from the current user authorization.
-
-**Support / precise locator:** Doug’s P04 message and attached brief, Authorization update, Assigned outputs and Current jobs and boundaries.
-
-**Applicability, contrary evidence and unresolved question:** No permanent IDs, release, implementation, repository/Project changes or participant work are approved.
+**Claim:** P04 authorizes draft research, not implementing or testing this pattern. **Class:** `studio-decision`. **Owner/date:** Doug; P04 dispatch, 2026-10-10, Assigned Outputs and boundaries. **Confidence:** high. **Limit:** null approval fields, provisional identity, no release or repo/Project changes. **Unresolved:** independent review and subsequent decisions.
 
 ## References
 
-All public records below were inspected in the stated passages on **2026-10-11 UTC**. IDs are P04-scoped source records, not permanent SRC allocations. Dates of older works are publication dates, not claims of current game behavior. Repeated reference records support standalone reading; they are not extra evidence.
-
-### GDR-SRC-20261010-P04-005
-
-**Aline Normoyle and Sophie Jörg.** [The effect of animation controller and avatar on player perceptions](https://www.researchgate.net/publication/310603130_The_effect_of_animation_controller_and_avatar_on_player_perceptions). **Publisher:** Computer Animation and Virtual Worlds / Wiley; author manuscript via ResearchGate. **Publication/update:** First online 2016-11-20; journal issue 2018. **Edition/build:** 29(6), e1731; DOI 10.1002/cav.1731. Inspected author manuscript uploaded 2021-01-26; manuscript pagination, not journal pagination.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original controlled game experiment and separate observer study; primary author manuscript. **Exact locators:** §3.2–3.4, manuscript pp.12–17; §4.9, pp.23–24; §5.1 Control and §5.2 Enjoyment, pp.25–26; §5.3 Satisfaction, pp.26–27; §5.4 Performance, pp.27–28; §6 Conclusion and Future Work, pp.31–33. **Claims supported in this entry:** C-04.
-
-**Limits:** Publisher full-text request redirected to abstract; full manuscript text was read on the author-upload route. Exact equivalence to the version of record not verified. Restricted controller/task designs, mainly student sample and differing observer/player questions limit generalization. Internal performance-direction inconsistency retained as P04-CON-04. No footage, raw data or graph digitization used. **Independence/deduplication:** Cites source 004 and earlier work by these authors. Manuscript, abstract and DOI are one work, not multiple confirmations. Cross-batch deduplication pending. **Rights:** Author manuscript copyright; redistribution license not established. Attributed paraphrase only; no participant data copied.
+All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.
+
+### GDR-SRC-20261010-P04-006
+
+**Unity Technologies. [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html).** Unity Manual. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unity 6.3 LTS (6000.3).
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Transition properties (Fixed Duration, Transition Duration, Has Exit Time); Transition interruption; Interruption Source; Ordered Interruption. **Supports:** C-03, Animator scope only.
+
+**Limits:** Describes Animator transitions, not input buffering or automatic cancellation of gameplay consequences. No engine execution. **Relationship:** Independent vendor from Epic; two implementations are not evidence of better player outcomes. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-007
 
-**Unity Technologies.** [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html). **Publisher:** Unity Manual. **Publication/update:** Publication/update date unknown. **Edition/build:** Unity 6.3 / 6000.3 documentation, selected edition; no claim that it is the newest engine.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Properties → Has Exit Time, Fixed Duration, Transition Duration and conditions; Transition interruption → Interruption Source and Ordered Interruption. **Claims supported in this entry:** C-01/C-02.
-
-**Limits:** Documents facilities and units; does not measure this project’s latency, responsiveness or cancellation policy. No engine execution. Recheck exact dependency version before implementation. **Independence/deduplication:** One vendor mechanism reference, not efficacy evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined. Paraphrase only, no code copied.
+**Epic Games. [Root Motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation; 5.6 route also inspected but not source of current-version claims.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Overview; Root Bone; Root Motion; Enabling Root Motion; Results. **Supports:** C-03, movement/animation facility only.
+
+**Limits:** One movement/animation facility; neither a universal motion authority rule nor an implemented benchmark. **Relationship:** Same Epic documentation family as networked movement and motion matching. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-008
 
-**Epic Games.** [Animation Blueprint Blend Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Inertialization: source evaluation, interruption, and Animation Notifies paragraphs; parsed text lines 121–150. **Claims supported in this entry:** C-01/C-03.
-
-**Limits:** No benchmark or runtime test. Documented source-evaluation behavior does not by itself prescribe gameplay event ownership. Experimental facilities are not endorsed for shipping. **Independence/deduplication:** Same vendor as source 009, different page/mechanism. Version parameter is part of this source identity; central deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.
-
-### GDR-SRC-20261010-P04-009
-
-**Epic Games.** [Understanding Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Network Smoothing; Replicating Special Case Movement with Root Motion → From AnimMontages; parsed text lines 174–203. **Claims supported in this entry:** C-01/C-05.
-
-**Limits:** Character Movement Component behavior, not a universal networking model or proof of fair combat. No server/client, network or frame-time tests performed. **Independence/deduplication:** Same vendor as source 008. Distinct mechanism, not independent user-outcome evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.
-
-### GDR-SRC-20261010-P04-010
-
-**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal and Overview; Implementation guidelines → alternatives to color and visual-only information; simulation-filter and actual-player evaluation paragraphs. **Claims supported in this entry:** C-06.
-
-**Limits:** Practitioner guidance, not a formal standard, legal advice or certification. Availability of an alternative is not demonstrated usability or emotional equivalence. Public body inspected despite authorization boilerplate. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-05 and GDR-SRC-20261010-P02-005; central reconciliation pending. Same issuer as source 011. **Rights:** Vendor page; content reuse license not inspected; paraphrase only; no example media copied.
-
-### GDR-SRC-20261010-P04-011
-
-**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Implementation guidelines → moving/blinking/scrolling UI and its background-motion exception; camera motion; repetitive non-core animation; parsed text lines 43–121. **Claims supported in this entry:** C-06.
-
-**Limits:** Not a universal freeze-all-gameplay requirement, medical safety threshold or certification. No FOV, flashing or animation-duration limit is extracted. Camera-setting research remains P03 ownership. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-10 and GDR-SRC-20261010-P02-010; central reconciliation pending. Related vendor guidance is not independent efficacy evidence. **Rights:** Vendor page; content reuse license not inspected; paraphrase only.
+**Epic Games. [Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Network roles/movement cycle; Replicating Special Case Movement with Root Motion; root-motion montage and Gameplay Ability System paragraphs (web extraction lines 194–218). **Supports:** C-03, scoped network responsibilities only.
+
+**Limits:** Character Movement workflow only; no general netcode guarantee, latency target or local synchronization test. **Relationship:** Same issuer and feature family as root motion, not a separate efficacy study. **Rights:** Reuse license not inspected; paraphrase only.
+
+### GDR-SRC-20261010-P01-05
+
+**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-04, indirect information-access bridge.
+
+**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.
 
 ## Related entries and history
 
-Owning topic: [Animation and performance — GDR-CAND-20261010-P04-TOP-02](../topics/animation-and-performance.md). Complement: [Recognition-preserving style variation](recognition-preserving-style-variation.md), not a replacement for P02 controls/feedback or its fact-preserving cue recipe. Exact external candidate identities are in the [dependency record](../reviews/full-run-20261010-p04-review-packet.md#reviewed-dependency-transfer). No genre files are linked or created.
-
-P04-CON-03 preserves deliberate commitment as a countercase; P04-CON-04 prevents upgrading the controller manuscript’s inconsistent or weaker results. Missing F04/P03 work blocks final action/platform-specific settings, not this bounded qualified draft.
-
-**2026-10-11 UTC:** initial 0.1.0 / initial-draft-1, no predecessor/supersession. Author self-review only. Independent review, host validation, permanent identity allocation and release remain pending. A valid research recipe is not an approved controller architecture.
+Owner: [Animation and performance — GDR-CAND-20261010-P04-TOP-02](../topics/animation-and-performance.md). Complement: [Role-preserving style variation](role-preserving-style-variation.md). The owning topic contains the original controller-study record; this pattern does not present a second study or silently transfer uninspected prior statistical results.
+
+P02 Controls/Feedback, F07 Legible commitment and safe exit, G02 Bounded action grace and W02 Intent and response contract remain inspected, unbundled candidate dependencies. Exact boundaries and hashes are in the [review packet](../reviews/full-run-20261010-p04-review-packet.md#pattern-ownership-and-overlap). No merge, retirement or permanent home is allocated here.
+
+**2026-10-10:** initial P04 pattern, version 0.1.0 / initial-draft-1; predecessor and supersession null. Same-author self-review only; independent P04 review not performed. No engine, participant, release, game-adoption or repository/Project action. [C-07]

```
