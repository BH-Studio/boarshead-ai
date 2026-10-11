---
id: GDR-CAND-20261010-P03-PAT-01
kind: pattern
title: Recoverable camera assistance
version: 0.1.0
candidate_revision: initial-1
status: draft
id_scope: run-scoped-temporary
run_id: GDR-FULL-20261010
batch_id: P03
attempt_id: P03-authoring-20261010-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus inspected selected first-wave reviewed drafts; archive SHA-256 e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef
aliases:
- camera assist recovery
- recoverable recentering
tags:
- camera
- authority
- assistance
- recovery
- accessibility
- hypothesis
related_topics:
- GDR-CAND-20261010-P03-TOP-01
- GDR-CAND-20261010-P03-TOP-02
related_patterns:
- GDR-CAND-20261010-P03-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P03-001
- GDR-SRC-20261010-P03-002
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial P03 research candidate; no predecessor or released guidance replaced.
hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
---

# Recoverable camera assistance

**Draft 0.1.0, revision `initial-1`; unvalidated pattern hypothesis.** This is a recipe for allocating, intervening in and recovering view control. It is not a rule that every game needs free camera movement, automatic recentering or multiple viewpoints. The owning [Camera and framing topic](../topics/camera-and-framing.md) distinguishes task information, physical looking, authored motion and intended experience. [C-01, C-02]

## Purpose

Help a player obtain a usable view without an unwanted or unrecoverable transfer of control. Intended benefit: reduce avoidable camera-operation burden while preserving legitimate knowledge, orientation and the player's chosen assistance. Added value over a fixed view, ordinary manual view or simple scene repair remains unestablished. Use the pattern to specify a comparison, not as released guidance. [C-01]

## Context and prerequisites

There must be an identified view-control problem, an explicit information boundary, an operable assistance/recovery route and a camera policy that can be described in states. “The shot would look more dramatic” is not by itself a reason to take control. Conversely, a player may choose ongoing assistance rather than requesting every movement individually. The recipe must accommodate that choice rather than make manual camera ability a prerequisite. [C-02, C-03]

Before proceeding, identify which target or relationship may be revealed, which dimensions can change, what the player is currently doing, which inputs and accommodations remain available, what happens to gameplay during the intervention, and how to get back to a meaningful state. A return to the exact old coordinates is not required if those coordinates have become obstructed; recovery means restoring a usable, intelligible view under the chosen policy. [C-03, C-04]

The abstract recipe is device-neutral. A specific application must declare flat screen versus contained HMD window versus immersive tracked presentation, active input, viewing assumptions and access needs. It must not treat disabling physical head tracking as an ordinary “camera off” option. The current evidence does not validate direct application to AR tracking, competitive shared cameras or every accessible input. [C-05, C-08]

## Mechanism and evidence

| Proposed causal link | Support and limit |
|---|---|
| Chosen assistance reduces unnecessary simultaneous view-control work. | GDR-SRC-20261010-P03-002 describes an assistance rationale, not a measured effect of this recipe. C-01 remains a hypothesis. |
| A clear authority policy makes intervention understandable. | Original design inference C-02; no inspected authority-policy experiment. |
| A permitted, bounded reorientation exposes relevant information. | C-03 is a logical task constraint; an unobstructed target is not proof of attention or comprehension. |
| Cancellation, adjustment or restoration prevents a bad intervention from trapping the player. | Proposed recipe mechanism C-04, not tested reliability or a promise of costless exit in every game. |
| Useful operation and tolerability improve without erasing agency. | The complete outcome claim C-01 is unvalidated. Separate those measures; do not infer them from correct camera coordinates. |

XAG 117 provides customization guidance; the creator account demonstrates that automatic assistance can be an intentional access option. Neither source establishes that the sequence below is sufficient, universally necessary or better than a simpler policy. The strongest objection is that adding states and controls can itself create burden. [C-01, C-02, C-06]

## Recipe

All steps and parameters are **proposed**, not implemented, playtested or approved for adoption. [C-07, C-08]

### 1. Name the view problem and minimum facts

Specify the task that the player cannot currently perform reliably, the information needed now, and any deliberately unknown facts. Identify the least complicated comparator: scene adjustment, stable framing, an inspect action, manual control or the existing assistance.

**Exit:** do not add intervention if the actual problem is unreadable text, ambiguous state information, unavailable input or a task that does not need the proposed reveal. Route those issues to their owners rather than treating all difficulty as a camera problem. [C-03, C-06]

### 2. Establish the chosen authority policy

For ordinary movement, inspection and any special action, name the controlling party for position, orientation and framing. Provide the supported choice of assistance where appropriate. A player can choose sustained help, axis-limited help, a requested reorientation or the available fixed policy; the pattern does not require all choices in every game.

**Adjustable variables:** dimensions under assistance, whether the trigger is explicit or ongoing, which input has priority, persistence of the choice, and how the setting is communicated. These variables have no sourced universal values.

**Exit:** when the player cannot discover or operate the authority choice through their supported route, redesign the interface or use a simpler policy before adding automatic behavior. [C-02, C-05]

### 3. Admit an intervention only for a legitimate target

Identify the target or relationship, the allowed knowledge, and the intervention's end condition. A known door can be a valid requested target; an unseen answer to a mystery is not automatically valid. Resolve competing target priorities explicitly rather than letting a solver decide game meaning.

**Branch:** when a camera move is unnecessary, use a stable frame or authorized information equivalent. When the target cannot be exposed without revealing prohibited facts, change the scene/task or offer an explicitly chosen hint rather than hiding the disclosure inside assistance.

**Adjustable variables:** target selection, eligibility, trigger, path constraints, current action state, maximum permitted disruption and fallback. “Maximum” denotes a later task-specific decision, not a numerical threshold provided here. [C-03]

### 4. Execute only the needed change while preserving operation

Keep the chosen assistance policy distinct from decorative bob, shake and other effects. Do not automatically remove useful assistance when reducing nonessential motion. Define whether the player can continue acting, how competing manual input is handled and how the intervention is signaled through a usable route.

**Branch:** do not require constant manual correction to hold a chosen inspection view. Equally, do not make one accidental camera input permanently remove needed assistance. Compare explicit suspend/resume behavior or another stable rule in the actual context.

**Exit:** if no allowed movement path or presentation can preserve required operation, return to a stable alternative and disclose the limitation. A failed solver should not produce repeated uncontrollable searching for a shot. [C-02, C-04, C-05]

### 5. Recover to a meaningful control state

Specify the effects of completion, cancellation, skip, obstruction, menu interruption, loading and input-device changes. Restore the chosen policy and a valid orientation/reference; do not reset user preferences as a side effect. Define what a held movement input means across the handoff.

**Adjustable variables:** destination policy, valid fallback view, interruption semantics, held-input interpretation and accessible recovery action. Choose them with input and movement owners. P02/F04 actual candidate evidence was not available here.

**Exit:** block use of the proposed version when recovery requires an input the player cannot perform, transfers the player into unintended consequential movement, or leaves them without necessary information. [C-04, C-05]

### 6. Compare, retain narrowly, simplify or remove

After separate study authorization, compare the proposed policy with the viable simpler alternative. Keep the assistance only for the task/context where evidence supports its added value. A participant preferring automation and another preferring manual control are not necessarily contradictory results.

**Exit:** remove or revise the version when its added state/interaction cost is not justified, its knowledge boundary fails, or the recovery policy is unreliable. No additional gameplay intensity is warranted merely because task completion improved. [C-01, C-06, C-07]

### State and recovery specification

| State | Required specification | Unacceptable silent behavior |
|---|---|---|
| Ordinary chosen policy | Authority and retained assistance preference. | Reverting to an author-preferred default after every action. |
| Assistance eligible/requested | Legitimate target, allowed knowledge and trigger. | Choosing a hidden answer without consent to that hint. |
| Intervention in progress | Input priority, available actions, usable cancellation/adjustment. | Fighting meaningful player input with no understandable escape. |
| Suspended/interrupted | Preserved state and visible means to resume or decline. | Treating a menu, disconnection or cut as a reset of access choices. |
| Completed/recovered | Valid view, intended mapping and preferred policy restored. | Releasing held input into a newly transformed direction without review. |

The table is a proposed design specification, not a runtime architecture or an engine state machine delivered for execution. [C-04, C-07]

## Worked examples

### Illustrative: requested machine inspection

A player operates movement through a single supported control route and chooses assistance to inspect a machine. They already know the machine's location and need its status, but the cause of a distant event remains unknown. The designer first defines the permitted target and confirms that the same requested action is available through the player's controls. [C-03, C-07]

The assist reframes the machine without selecting the distant event. A stable status representation preserves the necessary fact. If the view is obstructed, a known alternative inspection point is offered; the camera does not hunt indefinitely. When inspection ends, the chosen movement-and-assist policy resumes with the same known exit available. Turning off decorative motion leaves this requested assistance intact. All of these behaviors are hypothetical specifications. [C-02–C-05, C-07]

The comparison is not intentionally inaccessible manual-only play. It is the simplest usable alternative for this participant, such as a stable interaction view or a relocated control. If that alternative works with fewer interruptions, the added assist lacks demonstrated value. [C-06, C-07]

### Illustrative: a cinematic return while input is held

A player is moving toward a known opening when a staged view begins. The proposed handoff record identifies whether movement pauses, which held input persists and what reference will be visible on return. Skipping the sequence must resolve the same meaningful state rather than bypassing necessary information or changing the direction of an ongoing action without warning. No particular cut, blend or delay is prescribed. [C-04, C-07]

## Tradeoffs and alternatives

The candidate benefit is less avoidable camera work and fewer unrecoverable transitions. The costs are settings discoverability, mode awareness, authored target/knowledge rules, multiple recovery paths and additional testing across inputs, languages and interruptions. None of those costs has a measured multiplier in this corpus. The simplest alternative may be moving the interaction point or keeping a fixed view. A free camera can be the best option when looking is the intended activity; a sustained assist can be better for a player who chooses to avoid simultaneous view work. [C-01, C-02, C-06]

An assistance mode may intentionally change task difficulty. State that explicitly rather than claiming complete competitive or experiential equivalence. A cinematic can intentionally interrupt control, but that does not remove the need to specify how its promised interaction resumes. No genre preference or compulsory production investment is inferred. [C-03, C-04, C-06]

## Failure cases

| Future observable warning | Candidate explanation | Proposed correction |
|---|---|---|
| Player repeatedly steers against the camera | Trigger or authority mismatch. | Requested/limited assistance or stable manual priority. |
| Correct target exposed but task still misunderstood | Presentation/semantics rather than framing. | Repair information route, not a larger camera move. |
| Help reveals a previously unknown answer | Target eligibility lacks a knowledge boundary. | Redesign eligibility or label it a chosen hint. |
| Reduced-motion option makes assistance unusable | Useful authority and decorative motion are coupled. | Separate choices and evaluate their combination. |
| Skip/load/disconnect restores a different policy | Preference, transient state and recovery are confused. | Restore chosen intent and a valid current view. |
| Any recovery control is inaccessible | The nominal escape route is not operable. | Replace it or reject the recipe for that context. |

These are falsifying candidates, not observed findings. [C-03–C-07]

## Counterexamples and do not use conditions

Do not use the recipe to “help” with a task whose intended decision is precisely where to look, unless the intervention preserves that decision or is explicitly chosen as a hint. Do not use it when a simple stable view already works, the task cannot tolerate interruption, no permitted target exists, or an operable recovery cannot be provided. [C-03, C-06]

Do not transfer the recipe directly into HMD head-pose tracking. An authored virtual-camera intervention and physical looking are distinct. A headset application needs a separately scoped platform review before deciding how any virtual reorientation relates to the tracked view. The recipe is not evidence that a given virtual rotation is comfortable. [C-05]

The strongest opposing case is that a “recoverable” assist adds a confusing mode and recovery control to an otherwise simple task. A successful falsification would show no useful reduction in operation burden, or show greater confusion/preference loss even when the intended target is visible. The burden of evidence remains on adding the intervention. [C-01, C-06, C-07]

## Playtest

**PROPOSED — NOT RUN.** Compare the candidate with a viable baseline under matched task facts, permitted knowledge and consequences. Use actual intended input/access routes and separate flat-screen from HMD contexts. Counterbalance scene/order; inspect repeated use, obstruction, intentional camera input, interruption, skip and recovery. Record assistance state and prior experience. No sample-size guarantee or universal timing/intensity setting is supplied. [C-07]

Measure task-fact comprehension, camera correction burden, orientation/held-input errors, knowledge leaks, recovery success, chosen help usage, perceived control and tolerability separately. A person declining an action may still understand it; a person completing an action may simply be following the camera. Use changed situations that distinguish those possibilities without withdrawing accommodations. [C-07]

Reject or revise when the help cannot be operably adjusted/recovered, reveals prohibited knowledge or causes consequential unintended actions on return. Narrow benefits to the contexts actually observed. Prefer a simpler policy when added complexity lacks a locally meaningful benefit; an inconclusive small comparison does not prove equivalence. A later study owner must fix analysis and meaningful margins before testing. Stop exposure on request and retain withdrawals/failures in the record. [C-07, C-08]

## Claim ledger and sources

### C-01
**Claim:** Recoverable assistance may reduce avoidable camera-operation burden without unacceptable information, control or tolerability losses. **Class:** `hypothesis`. **Support:** GDR-SRC-20261010-P03-001, Implementation guidelines; 002, Camera Assist, motivate components only. **Confidence:** low; no complete-policy comparison inspected. **Applicability:** explicit view problem with an operable alternative/recovery. **Unresolved:** benefit over simpler choices. Owning topic C-14 is the same hypothesis, not corroboration.

### C-02
**Claim:** Camera authority should respect the chosen assistance policy rather than mandate either manual operation or automation. **Class:** `inference`. **Bridge/sources:** 001 offers customization; 002 supplies a firsthand assistance rationale. **Confidence:** moderate as conditional logic. **Limit:** no optimal mode/default established. **Unresolved:** operability and unwanted interference for the actual task.

### C-03
**Claim:** A framing intervention should preserve required and permitted information rather than reveal every target it can expose. **Class:** `inference`. **Basis:** original task/knowledge analysis; camera topic C-11 and inspected P01 information distinctions. **Confidence:** moderate for the constraint. **Limit:** no information-leak experiment or genre rule. **Unresolved:** legitimate knowledge boundaries and hint choice.

### C-04
**Claim:** Explicit intervention, interruption and recovery semantics may prevent avoidable handoff failures. **Class:** `hypothesis`. **Basis:** original recipe; camera topic C-12. **Confidence:** low for comparative efficacy. **Limit:** no inspected cinematic-return experiment or engine test. **Unresolved:** held-input mapping, recovery burden and unpausable contexts.

### C-05
**Claim:** Useful assistance, decorative motion and physical HMD tracking must not be treated as the same configuration channel. **Class:** `inference`. **Bridge:** 001 motion options and 002 assistance rationale serve different purposes; camera topic C-09/C-13 retains XR limits. **Confidence:** moderate for separation, not implementation correctness. **Unresolved:** current device-specific realization and access combinations.

### C-06
**Claim:** Simpler fixed/manual/scene-repair alternatives remain valid and can defeat the case for added assistance. **Class:** `inference`. **Basis:** no source validates full-policy superiority; original complexity/benefit comparison. **Confidence:** moderate as burden-of-evidence reasoning. **Limit:** not proof any alternative is best. **Unresolved:** actual tradeoffs and maintenance cost.

### C-07
**Claim:** Recipe branches, examples, state records and tests are unvalidated proposed specifications. **Class:** `hypothesis`. **Basis:** original synthesis under P03; F01 correction's understanding-versus-action caution retained. **Confidence:** low for diagnostic validity. **Limits:** no approved values, sample or participant data. **Unresolved:** protocol approval, feasibility and local margins.

### C-08
**Claim:** This pattern is authorized draft research only. **Class:** `studio-decision`. **Owner/date/source:** Doug, 2026-10-10, complete P03 brief, Assigned Outputs/execution limits. **Confidence:** high for scope. **Limit:** no implementation, study, publication or release permission. **Unresolved:** independent evidence review and later human decision.

## References

All source identities below are run-scoped candidates. Access was `relevant-excerpt` on 2026-10-10: actual public HTML/text or transcript passages, not merely search summaries. Repeated records support standalone reading, not corroboration.

### GDR-SRC-20261010-P03-001

Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). Microsoft Learn. **Date:** Updated 2026-03-04; original publication unknown. **Edition:** Unnumbered live revision. **Type:** Official vendor guidance. **Locators:** Goal; Overview; Implementation guidelines → camera movement, field of view, sensitivity, automatic movement, nonessential effects, background motion while reading. **Limits:** Recommendations, not a formal standard, medical guarantee or efficacy comparison. **Relationship:** Same issuer as 011/012; URL matches P01-10, central reconciliation pending. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-002

Matthew Gallant, Lead Systems Designer, Naughty Dog. [The Last of Us Part II: Accessibility features detailed](https://blog.playstation.com/2020/06/09/the-last-of-us-part-ii-accessibility-features-detailed/). PlayStation Blog. **Date:** 2020-06-09; page also displays 2020-06-10. **Edition:** Historical launch-era account; exact game build not inspected. **Type:** Firsthand creator account. **Locators:** Accessibility Presets; Alternate Controls → Assistance → Camera Assist; Navigation and Traversal → Navigation Assistance; Motion Sickness. **Limits:** Reported features and intent; no played build, controlled outcomes or measured comfort benefit. **Relationship:** One production account, independent of Microsoft documentation; not a replication. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

## Related entries and history

[Camera and framing — GDR-CAND-20261010-P03-TOP-01](../topics/camera-and-framing.md) owns definitions, competing mechanisms and adjacent empirical limits. [Platform and display context — GDR-CAND-20261010-P03-TOP-02](../topics/platform-and-display-context.md) owns environment changes. [Task-preserving context profiles](task-preserving-context-profiles.md) is complementary, not corroborating.

P02 controls/input, feedback and multimodal drafts, F04 movement, and W03 spatial-design evidence remain missing external dependencies. They are not fabricated relative links. No genre file is asserted. Batch conflicts and queued work are in the [P03 packet](../reviews/full-run-20261010-p03-review-packet.md).

**2026-10-10:** initial `initial-1`, 0.1.0 draft; no predecessor or superseded entry. Author self-review only; independent P03 review, host validation, empirical efficacy and release remain outstanding. Next decision: challenge the full-policy hypothesis against simpler alternatives before selecting a separately authorized validation route.
