---
id: GDR-CAND-20261010-P04-PAT-02
kind: pattern
title: Action-phase and interruption contract
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
- animation cancellation contract
- state-consistent animation exits
tags:
- animation
- action-state
- interruption
- recovery
- conditional-recipe
related_topics:
- GDR-CAND-20261010-P04-TOP-02
related_patterns:
- GDR-CAND-20261010-P04-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P04-006
- GDR-SRC-20261010-P04-007
- GDR-SRC-20261010-P04-008
- GDR-SRC-20261010-P01-05
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial P04 submission; does not replace or resend any previous batch.
byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
---

# Action-phase and interruption contract

**Draft 0.1.0; initial-draft-1. A conditional design-inference pattern, not a validated control system, approved implementation or released rule.**

## Purpose

Keep an action’s true state, visible performance and permitted exits consistent when animation is blended, interrupted, replaced, replayed or completed. The intended benefit is understandable action and recovery, not universal instant cancellation. A smooth clip can be successful art while communicating the wrong current state. The value of this full recipe has not been experimentally established. [C-01]

## Context and prerequisites

Use when a meaningful action can be interrupted or its visual phases can differ from its actual consequences. The designer must know what the action does, when consequences become committed, what can interrupt it, which facts the player needs, and who owns those facts. It applies to movement, manipulation or an expressive beat only where those distinctions are useful; a simple noninteractive loop may need none of this structure. [C-02]

Declare player/NPC authority, input path and assistance, view and actor visibility, motion preferences, local/network roles, action persistence and relevant cultural/language context. For a purely observed performance, do not invent player input acknowledgement. For a player-controlled actor, do not imply that an expressive gesture guarantees the requested outcome. [C-02]

Inspected parent P02 control/feedback distinctions inform this pattern; the selected F07 safe-exit pattern concerns broader commitments and retained stakes, G02 bounded-action-grace concerns eligibility leniency, and W02 intent-and-response concerns the meaning of selected dialogue. P04 owns the narrower **animation/action phase and exit consistency record**. Relationships remain provisional, not a merge or independently approved new canonical home. See the [overlap record](../reviews/full-run-20261010-p04-review-packet.md#pattern-ownership-and-overlap). [C-02]

## Mechanism and evidence

The [Animation and performance topic](../topics/animation-and-performance.md) owns the empirical and technical comparison. The pattern draws a design inference from facilities that separate visual transitions, movement and action authority. It does not treat a vendor API as evidence that the proposed recipe improves players. [C-01, C-03]

| Candidate causal link | Support | Limit |
|---|---|---|
| Name true action phases independently of clip playback. | P02 state distinctions and the documented separation of animation/movement responsibilities. | A phase model is an authoring convention, not a standard state machine. [C-02, C-03] |
| Specify exits and retained consequences. | An interrupted visual sequence need not correspond to reversal of its underlying action. | Consistency logic; not a measured reduction in errors. [C-01, C-02] |
| Communicate only the state actually reached. | P02 distinguishes acknowledgement, pending and confirmed outcome. | The chosen presentation still needs an actual comprehension test. [C-04] |
| Compare equivalent commitments, not just similar clips. | The owning topic’s narrow controller evidence warns against conflating appearance and task effects. | It does not validate this complete recipe or prove a responsiveness-first policy. [C-01, C-05] |
| Retain readable state through alternative access routes. | XAG 103 supplies additional-channel guidance. | Information availability is not usability or equal experience. [C-04] |

## Recipe

### 1. Write the action and its consequence

State what is requested or triggered, what becomes different in the world, and what remains outside the actor/player’s control. Identify whether the action is reversible, cancellable before a consequence, interruptible after it, or simply skippable in presentation. Avoid treating those as synonyms. [C-02]

**Exit:** if the team cannot state the consequence or who owns it, stop polishing transitions and resolve the design ambiguity. No animation-only repair can define an unknown commitment honestly. [C-06]

### 2. Use only the phases the action needs

Candidate phases are receipt/trigger, pending eligibility, acceptance, preparation, commitment, consequence, recovery and control return. Merge phases when they truly coincide. Record what makes each phase true rather than prescribing that a particular clip timestamp always controls it. [C-02]

For each phase, record: true facts; visible and alternative presentation; progression condition; permitted interrupting events; retained/changed consequences; next allowed action; pause/re-entry behavior; authority where relevant. The record can be a short table rather than an elaborate system. [C-02]

### 3. Define interruption before choosing its blend

For each important interruption, distinguish stopping the visual action from stopping the underlying action. Specify the next valid pose/behavior and the actual next state. Include denial, conflicting commands, external interruption, repeated request, late cancel and recovery after a changed context. Do not promise rollback merely because a blend is easy. [C-02, C-03]

**Branch:** when a deliberate commitment is part of the task, preserve it and make its boundary understandable. The pattern is not permission to cancel every action or remove an agreed cost. When an optional flourish unnecessarily blocks a valid next action, compare a presentation-only exit. [C-01, C-06]

### 4. Choose transition and movement responsibilities

Select authored transitions, a movement-driven visual layer, root-driven movement, pose selection or a simpler presentation according to the action’s needs. Unity’s transition interruption controls and Epic’s movement facilities are implementation examples, not engine mandates. [C-03]

**Variables:** what initiates motion; which phases can overlap; event ownership; animation playback/blend duration and units; priority of interruptions; recovery pose; semantic meaning of repeats; alternate state presentation. No universal frame count, timeout, blend length or root-motion policy is supplied. [C-03, C-05]

For networked use, record which participant’s view is provisional and what confirms the consequence. A local visual sequence is not sufficient proof of shared state. Keep the actual replication/prediction design with its authorized implementation owner. [C-03]

### 5. Align acknowledgement and expression with truth

A request acknowledgement must not depict confirmed success while the action is still pending. A successful transfer can retain its consequence after a decorative settle is skipped. A resumed expression should still make sense in the new context. Preserve the legitimate unknowns without obscuring required state or exit information. [C-04]

Evaluate the actual view and chosen motion/access settings. Do not add mandatory visual busyness merely because a key pose exists in the animator’s reference. Provide an appropriate alternative for important information and review whether its meaning differs. [C-04, C-05]

### 6. Compare normal and adversarial sequences

After separate authorization, test normal completion and the important exits. Include paired cases with the same visible interruption but different true consequences. Predict the current state before asking what the participant wishes to do next. A repeated “cancel means no effect” answer should not pass a set containing a post-consequence exit. [C-05]

**Stop:** contradictory state presentation, duplicated/forgotten consequences or an inaccessible essential exit blocks recommending that version. Fix the semantic mismatch before treating a cleaner transition as success. Distress/withdrawal stops a participant session. [C-06]

### 7. Keep, simplify or restrict

Compare the contract and its presentation with a simpler valid action. Retain only phases and exceptions needed to preserve the actual promise. If added flexibility changes the intended challenge, record that as a mechanics change needing separate approval, not a pure animation improvement. Reopen review when action consequences or interruption policy change. [C-01, C-05, C-06]

## Worked examples

### Illustrative: module extraction

**Invented; no engine, asset or participant test was created.** An agent removes a service module. The player can withdraw the request before the module leaves its socket. After transfer, skipping the final settle leaves the module transferred; it does not put it back. An explicit return-module action would be different. [C-05]

| Event | Proposed true result | Permitted presentation/exit |
|---|---|---|
| Request arrives while availability is unresolved. | Pending; no module transferred. | Acknowledge receipt without depicting success. Cancel the pending request where the contract permits. |
| Preparation begins with eligibility confirmed. | Accepted but not yet transferred. | Reach/brace; pre-transfer cancellation returns to a valid original state. |
| Transfer is committed. | Module has changed location under the actual rule. | Show that result. Interrupting the remaining performance retains it. |
| Another event interrupts recovery. | Transfer remains; actor must respond from a valid new state. | Leave the flourish or settle, then present the permitted next behavior. |
| A late duplicate request arrives. | It does not automatically create another module transfer. | Present the actual eligibility/result; input policy remains with Controls/Foundations. |

A test should ask about one cancellation before transfer and another visual exit after transfer. Their correct retained-state answers differ. Add unfamiliar actions with the same distinction to examine transfer, rather than repeating the same two familiar clips. This preserves F01’s corrected test-discrimination principle, not its numerical example. [C-05]

### Illustrative: an interrupted expressive beat

An agent starts a greeting but turns to address an urgent task. Restarting the greeting is not automatically appropriate, and resuming an old smile need not preserve the intended tone. The design can finish a brief acknowledgement, drop the greeting, or defer it if still relevant. The literal task outcome and the audience’s emotional interpretation require different checks. This is a candidate application, not a gesture-equivalence finding. [C-04, C-05]

## Tradeoffs and alternatives

More explicit exits increase authoring and verification work. Very permissive exits can remove deliberate physical stakes; very rigid playback can impose costs that were never part of the intended choice. The useful comparison is the **same underlying commitment** presented and recovered differently. [C-01, C-02]

Alternatives include a whole-clip action with a clearly disclosed commitment, an immediate action with little performed detail, fewer action variants, a short acknowledgement while the real outcome remains pending, or a fixed scene without claimed player control. A design may choose slower embodied action for a particular purpose; this pattern asks that its truth and exits remain coherent, not that it be made fast. [C-06]

## Failure cases

A success flourish while the action is pending misrepresents state. A cancelled animation that leaves an unexplained completed consequence misrepresents cancellation. A recovery pose that repeats an already committed event risks duplicating presentation or, in a flawed later implementation, consequences. A technically valid resumed gesture may no longer fit the character’s current situation. These are proposed diagnostic failures, not bugs observed in a shipped game during P04. [C-02, C-04, C-05]

Repair the truth-to-presentation relationship first; then adjust transition polish, pose selection, event handling or alternative information. Do not attribute every failure to timing, or claim that one engine facility handles all consequence and network cases automatically. [C-03, C-06]

## Counterexamples and do not use conditions

A planning task may deliberately require committing to an action before its result. Removing that commitment can improve completion by making a different task. A purely decorative, noninteractive background cycle may also need no action-state contract. In both cases, applying every phase in this recipe would overreach. [C-06]

Do not use this as a universal cancel-window specification, a rollback guarantee, an input buffer, a general safe-exit/monetization policy, a legal consent model, or a claim that smoother/longer/shorter animation is always preferable. Missing authority, unresolved essential access, or an unhonorable exit promise is a reason to stop this recommendation, not fill the gap with an invented engine rule. [C-02, C-03, C-06]

## Playtest

**PROPOSED — NOT PERFORMED.** The owning topic contains the full plan. Compare a valid whole-clip action, a selectively interruptible phase-aware presentation with the same true consequences, and a simpler presentation. Separate experiments that alter the actual commitment from animation-only comparisons. [C-05]

After an authorized protocol establishes sample/precision and relevant access populations, counterbalance action family/order where feasible. Observe ordinary completion, pre-commit cancellation, post-consequence exit, denial, external interruption and repeated requests. Include novel cases with both retained and absent consequences. Record true state, perceived state and next-action preference separately; later instrumentation must distinguish acknowledgement, effective action and control return. Report enjoyment, expressive interpretation and comfort separately from errors or completion time. [C-05]

Reject or narrow the claim when the apparent benefit relies on easier mechanics, repeated answers, omitted negative cases or mismatched views/input. Revise any critical state/exit misinformation before advancement. An inconclusive result does not prove equivalence; select local acceptance tolerances before collecting data. No participant, prototype, technical measurement or adopted threshold exists in this research. [C-05, C-06]

## Claim ledger and sources

### C-01
**Claim:** A phase/exit contract is a useful candidate consistency method, not a proven responsiveness-first rule. **Class:** `inference`. **Support:** owning topic C-01/C-04/C-10; source facilities in C-03 and original causal bridge. **Confidence:** moderate for conceptual separation, low for local efficacy. **Unresolved:** complete-recipe benefit and minimum useful complexity.

### C-02
**Claim:** Distinguish actual commitment, presentation, cancellation, recovery and ownership; not every action needs every phase. **Class:** `inference`. **Support:** inspected P02 candidate distinctions and F07/W02/G02 boundary inspection; owning topic C-10. **Confidence:** moderate for consistency. **Limit:** no prescribed state machine. **Unresolved:** valid exits for the actual task and overlap acceptance by Coordination.

### C-03
**Claim:** Documented transition, root-motion and network facilities address different responsibilities. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-006, Transition properties/interruption; P04-007, Overview/Results; P04-008, root-motion special-case movement. **Confidence:** high for scoped documentation. **Limit:** no engine run, replication guarantee or universal settings. **Unresolved:** a separately authorized implementation’s exact responsibilities.

### C-04
**Claim:** Acknowledgement, actual outcome and interpreted expression should remain distinguishable through appropriate access routes. **Class:** `inference`. **Support:** owning topic C-01/C-12/C-13; inspected P02 feedback and W02 performance distinctions; GDR-SRC-20261010-P01-05 Implementation guidelines. **Confidence:** moderate for the information distinction; affective result unknown. **Unresolved:** actual understanding under selected presentation/context.

### C-05
**Claim:** Recipe benefits, examples and tests are hypotheses, not results. **Class:** `hypothesis`. **Support:** original P04 synthesis and selected F01 transfer-discrimination correction; owning topic C-11/C-14. **Confidence:** low for effectiveness. **Limit:** no prototype, participants, numeric defaults or actual QA of action behavior. **Unresolved:** approved protocol, matched commitments and relevant populations.

### C-06
**Claim:** Preserve deliberate stakes and stop when an action’s truth, exits or essential information cannot be represented honestly. **Class:** `inference`. **Support:** C-01–C-05 and explicit task contract. **Confidence:** moderate as scope/stop guidance. **Limit:** not a claim that every action must be cancellable or reversible. **Unresolved:** later project owner’s acceptable commitment and assistance policy.

### C-07
**Claim:** P04 authorizes draft research, not implementing or testing this pattern. **Class:** `studio-decision`. **Owner/date:** Doug; P04 dispatch, 2026-10-10, Assigned Outputs and boundaries. **Confidence:** high. **Limit:** null approval fields, provisional identity, no release or repo/Project changes. **Unresolved:** independent review and subsequent decisions.

## References

All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.

### GDR-SRC-20261010-P04-006

**Unity Technologies. [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html).** Unity Manual. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unity 6.3 LTS (6000.3).

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Transition properties (Fixed Duration, Transition Duration, Has Exit Time); Transition interruption; Interruption Source; Ordered Interruption. **Supports:** C-03, Animator scope only.

**Limits:** Describes Animator transitions, not input buffering or automatic cancellation of gameplay consequences. No engine execution. **Relationship:** Independent vendor from Epic; two implementations are not evidence of better player outcomes. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-007

**Epic Games. [Root Motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation; 5.6 route also inspected but not source of current-version claims.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Overview; Root Bone; Root Motion; Enabling Root Motion; Results. **Supports:** C-03, movement/animation facility only.

**Limits:** One movement/animation facility; neither a universal motion authority rule nor an implemented benchmark. **Relationship:** Same Epic documentation family as networked movement and motion matching. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-008

**Epic Games. [Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** Network roles/movement cycle; Replicating Special Case Movement with Root Motion; root-motion montage and Gameplay Ability System paragraphs (web extraction lines 194–218). **Supports:** C-03, scoped network responsibilities only.

**Limits:** Character Movement workflow only; no general netcode guarantee, latency target or local synchronization test. **Relationship:** Same issuer and feature family as root motion, not a separate efficacy study. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P01-05

**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-04, indirect information-access bridge.

**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.

## Related entries and history

Owner: [Animation and performance — GDR-CAND-20261010-P04-TOP-02](../topics/animation-and-performance.md). Complement: [Role-preserving style variation](role-preserving-style-variation.md). The owning topic contains the original controller-study record; this pattern does not present a second study or silently transfer uninspected prior statistical results.

P02 Controls/Feedback, F07 Legible commitment and safe exit, G02 Bounded action grace and W02 Intent and response contract remain inspected, unbundled candidate dependencies. Exact boundaries and hashes are in the [review packet](../reviews/full-run-20261010-p04-review-packet.md#pattern-ownership-and-overlap). No merge, retirement or permanent home is allocated here.

**2026-10-10:** initial P04 pattern, version 0.1.0 / initial-draft-1; predecessor and supersession null. Same-author self-review only; independent P04 review not performed. No engine, participant, release, game-adoption or repository/Project action. [C-07]
