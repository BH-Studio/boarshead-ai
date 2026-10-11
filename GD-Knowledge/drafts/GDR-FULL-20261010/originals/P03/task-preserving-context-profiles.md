---
id: GDR-CAND-20261010-P03-PAT-02
kind: pattern
title: Task-preserving context profiles
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
- context profile recovery
- task-preserving device switch
tags:
- platform
- display
- context-switching
- preferences
- accessibility
- hypothesis
related_topics:
- GDR-CAND-20261010-P03-TOP-01
- GDR-CAND-20261010-P03-TOP-02
related_patterns:
- GDR-CAND-20261010-P03-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P03-009
- GDR-SRC-20261010-P03-013
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial P03 research candidate; no predecessor or released guidance replaced.
hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
---

# Task-preserving context profiles

**Draft 0.1.0, revision `initial-1`; unvalidated process hypothesis.** This pattern owns preservation and recovery when viewing, listening or input context changes. It does not own the choice of cue encodings, detailed input mappings or platform compliance. The [Platform and display context topic](../topics/platform-and-display-context.md) supplies definitions and scoped source comparisons. [C-01, C-02]

## Purpose

Reduce the risk that a context change makes an ongoing task, chosen access route or meaningful state unusable. A profile is a candidate way to change presentation without silently changing what the player is doing or allowed to know. It may be unnecessary when one flexible presentation and a small number of explicit settings already work. No inspected experiment establishes profile superiority or equal experience across devices. [C-01, C-06]

## Context and prerequisites

Consider the recipe when the game supports recurring changes that matter to interaction: a handheld is docked, a window changes shape, an input route changes, the player selects sound-off play, or a preferred reading/motion setting changes the usable presentation. Do not infer the entire situation from a device model or a single input event. [C-02, C-03]

The designer must be able to name the task's necessary facts and actions, the state that must survive, the supported input/access routes, and a stable recovery presentation. There must be an operable initial settings route; the player should not first need the failed profile to reach the means of fixing it. Where the context is unsupported, the responsible output is a bounded support claim or an accessible limitation, not an automatic guess. [C-02, C-04]

The specific application must record its display/content region, actual inputs, listening options, language and chosen assistance. Neither physical viewing distance nor a medical/access need is inferred automatically. Participant data collection, microphone sensing and platform configuration are not prerequisites and are not authorized here. [C-03, C-07, C-08]

## Mechanism and evidence

| Proposed link | Evidence-to-application bridge | Limit |
|---|---|---|
| Recognize a consequential context change. | GDR-SRC-20261010-P03-013 distinguishes input availability/activity and mixed use. | No universal detector, confidence threshold or adaptation delay established. |
| Separate durable preference from local presentation settings. | GDR-SRC-20261010-P03-009 distinguishes device-specific graphics choices. The access-intent separation is original inference. | The source does not prescribe a complete preference architecture. |
| Adapt representation while preserving task semantics. | Original C-02/C-04, informed by the owning topic and inspected P01 information framing. | No guarantee of equivalent comprehension, difficulty or emotion. |
| Preserve a recovery route through failure or interruption. | Original C-04/C-05. | Not an implemented transaction/state machine or demonstrated reliability result. |
| Reduce burden compared with simpler presentation. | C-01 is the full-process hypothesis. | No direct comparison inspected; extra profiles can make operation worse. |

The source set motivates distinctions rather than validating the recipe. Accepting input from multiple devices does not prove that the resulting interface is intelligible or that the current selection survives. Correct technical settings do not prove that a copied scale value preserves readability. [C-01–C-04]

## Recipe

All steps, branches and parameters are proposed design work, not software executed in this batch. [C-07, C-08]

### 1. Record the task invariant

Write down the decision the player is making, required facts, available actions, current selection/progress and any legitimately unknown information. Specify which meaning must remain constant across the change. Do not treat “same visual layout” as the invariant when the goal is an informed comparison or action.

**Exit:** if the task itself must change for a context, document the mode/rule change explicitly and evaluate it as a different experience. Do not call that an equivalent presentation profile. [C-02]

### 2. Define the supported contexts and the least expensive baseline

Describe actual cases, not only device families: handheld touch, handheld controller, docked controller, accessible keyboard route, muted play, selected magnification, or another justified combination. Identify a shared flexible layout and ordinary settings as the primary simpler comparator.

**Adjustable variables:** content density, layout region, font/render scale, prompt set, available information routes and decorative effects. No universal numbers or mandatory profile count are provided.

**Exit:** if the baseline already serves the declared contexts, keep it and omit an extra named profile. If necessary contexts cannot be meaningfully supported within production scope, narrow the claim rather than create an untested profile label. [C-01, C-06]

### 3. Separate three kinds of state

Distinguish (a) the player's meaningful preferences, (b) device-local rendering/presentation choices, and (c) temporary task state. For example, an intention to retain readable text is not identical to a particular scale value, and a device's graphics quality selection is not the same as the player's current item selection.

**Branch:** retain explicit personal choices unless the player changes them; reevaluate local realization in the new context and communicate any limitation. Do not copy every technical setting across devices, reset all preferences on device change, or deduce disability from an assistance choice.

**Adjustable variables:** which settings are portable by meaning, which are device-local, which are transient, persistence boundaries and override behavior. These are proposed classifications requiring product-specific review. [C-03]

### 4. Respond to the actual change without removing working routes

Consider supported and active input, content region and user-selected context. Avoid switching an entire interaction mode because of an incidental keypress. Mixed input can be intentional. A named profile can be user-selected; the pattern does not require automatic sensing.

**Branch:** when automatic detection is uncertain, retain a stable operable presentation or offer an explicit choice rather than repeatedly rearranging the interface. Recheck prompts and focus, not just whether an input event was accepted.

**Adjustable variables:** trigger, stability policy, manual override, which elements change and what remains visible. Any delay or threshold must be justified locally rather than invented as a universal value. [C-03, C-04]

### 5. Apply the presentation change with a defined recovery

Keep the current meaningful selection, task facts, assistance intent and supported action route. Reflow or scale content without dropping necessary information; distinguish world-camera changes from interface layout changes. Decide how an interruption, rejected profile, disconnected device or failed layout returns to a stable usable state.

**Exit:** do not apply a profile that removes the only path to settings, leaves focus nowhere, hides the task's decisive fact or makes text entry depend on an unavailable route. In a live shared activity, specify a feasible local fallback rather than assuming the whole simulation can pause.

The term “recovery” is a design outcome, not permission to implement transactional software or alter saves. [C-04, C-05]

### 6. Verify at the final presentation and retain user control

After separate authorization, check the actual rendered text/content region, input route and required information during the ongoing task. Evaluate changes at first launch, mid-task, return from interruption and later reuse. Make the chosen profile and relevant overrides discoverable through the supported route.

**Exit:** reject, revise or narrow the profile when it loses meaningful state, silently overwrites a preference or adds burden without useful benefit relative to the baseline. Do not claim broad accessibility from a successful author-only route check. [C-01, C-05–C-08]

### Transition record to prepare

| Field | Required content in a later specification |
|---|---|
| Before | Task, selection/progress, necessary facts, preferred assistance and active/supported inputs. |
| Trigger | Actual user/context change; uncertainty and explicit override. |
| Allowed changes | Layout/render/audio/input-prompt presentation changes, separated from game-rule changes. |
| Preserved meaning | Facts, legitimate uncertainty, intended action availability and chosen access intent. |
| Recovery | Operable fallback, interruption/disconnection handling, restored focus and preference handling. |
| Validation | Comparison context, interpretation/action measures, known untested combinations and reject rules. |

The record is illustrative structure to populate for a real task; it is not an approved schema or a test result. [C-07]

## Worked examples

### Illustrative: docked comparison with enlarged text

A player has selected one of two objects and expanded their comparison details on a handheld. They switch to a television and controller. The task invariant is which properties are known and which actions remain available, not the original card dimensions. The profile proposes a larger reading layout and controller-operated focus while preserving the selection and the expanded comparison. [C-02, C-07]

A previously selected readable-text preference survives as intent; final rendering is checked at the new display rather than trusting the old scale. Device-specific graphics settings are handled separately. If a profile cannot preserve the comparison or hides the confirm/cancel route, it falls back to a stable accessible screen instead of applying a half-functional layout. This is a proposed behavior specification, not a claim that a platform provides it automatically. [C-03–C-05]

The future comparison includes the simpler shared layout with explicit settings. If that already works with less configuration effort, no profile is justified. A larger screenshot alone is not evidence of easier comparison; the player must be able to identify the properties and act from the current input route. [C-01, C-06, C-07]

### Illustrative: keyboard shortcut during controller use

A player uses a keyboard shortcut to filter a list but continues selection with a controller. The candidate accepts the supported input without necessarily hiding controller access or moving focus. A stable prompt preference or locally evaluated hint-switching policy may be preferable to full mode changes. The selection and filter are task state; the hint set is presentation state. A single keyboard event supplies no basis to infer a new display or disability. [C-03, C-04]

### Illustrative: sound-off selection without changed knowledge

A player chooses sound-off play during an inspection. The profile retains the required event facts through a usable selected alternative, not merely by adding every possible cue. It does not reveal a hidden event cause that the original information did not disclose, and it does not claim an unchanged emotional experience. P01's cue pattern owns the encoding choices; P03 owns preserving and recovering the choice as context changes. No audio rendering or playtest occurred. [C-02, C-05, C-07]

## Tradeoffs and alternatives

Profiles can make common context choices easier to find, but they add naming, override, persistence and testing burden. The application may be better served by responsive content bounds, simple scaling, stable mixed-input prompts and a few explicit settings. A profile should not become a compulsory gate that forces the player to identify with a demographic or medical label. [C-03, C-06]

Prioritizing a limited set of supported contexts is reasonable when those boundaries are visible. It is not reasonable to represent a profile name as proof of usability. Test the actual combinations with the relevant users before expanding the claim. Localized text, assistive speech, larger layouts and shared-session constraints can interact; passing them individually does not establish the combination. This is a proposed coverage caution, not a measured interaction effect. [C-05–C-07]

## Failure cases

| Future warning sign | Candidate cause | Proposed response |
|---|---|---|
| Profile switch loses the selected object or comparison | Task and presentation state bundled together. | Separate meaningful state and verify recovery paths. |
| New device restores an unwanted motion or caption default | Preference treated as disposable local graphics state. | Retain intent; check its new realization and explain limitations. |
| Prompts/layout flicker between modes | Last input event overinterpreted. | Stable mixed-input presentation or explicit preference; test local trigger policy. |
| Touch-dependent control remains after docking | Presence mistaken for practical availability. | Supply the supported controller/keyboard route or narrow support. |
| Enlarged or localized content hides the deciding fact | Scaling substituted for task validation. | Reflow/paginate with an intelligible return path and reassess comprehension. |
| Recovery itself requires inaccessible input | Fallback was only nominally accessible. | Replace the fallback or reject the profile for this context. |

These are proposed falsifiers, not P03 observations. [C-02–C-07]

## Counterexamples and do not use conditions

Do not add profiles when a simple presentation already supports the task, when context cannot be determined sufficiently and no usable explicit choice exists, or when switching removes the only supported action route. Do not silently change task rules or difficulty and label the result an equivalent layout. [C-02, C-06]

A player deliberately mixing inputs is a strong counterexample to exclusive automatic modes. A player who needs a stable interface can be harmed by repeated “helpful” rearrangement. A profile that requires personal disclosure or sensors merely to enable readable content also conflicts with this recipe's purpose. Use a stable selectable alternative instead, subject to actual evaluation. [C-03, C-06]

The complete hypothesis is falsified for a declared context if adaptation reliably causes more consequential state/operation failures than the simpler baseline or if its supposed benefit is only that an author prefers the new layout. Null or sparse evidence should remain uncertain rather than being promoted to equivalence. [C-01, C-07]

## Playtest

**PROPOSED — NOT RUN.** Compare a viable shared presentation with the proposed profile at the same task, information and chosen access settings. Include cold start and mid-task switching; mixed input and loss/reconnection of a supported route; changed window/aspect; appropriate text/language expansion; and preferred listening modes. Separate flat-screen and XR protocols. Do not force harmful exposure or remove accommodations for a baseline. [C-07, C-08]

Use participants who actually use the relevant routes and report context-specific findings. Counterbalance task/device order where feasible; log familiarity, performance conditions, input mix and active settings. Define sample size, analysis and meaningful benefit/margins through the later study review, not an arbitrary pattern default. [C-07]

Measure necessary-fact comprehension, correct prompt/action association, task-state retention, recovery success, reading/navigation effort, preference retention and perceived control/tolerability separately. A correct action alone does not show correct understanding; a different preferred action need not show failure. Reject a version that strands a player, loses required information or silently resets a necessary choice. Narrow benefits confined to one context, and prefer the baseline when added complexity has no justified value. Every comparison and decision rule here remains unexecuted. [C-07]

## Claim ledger and sources

### C-01
**Claim:** Task-preserving profiles may reduce context-change burden without unacceptable state, information or control losses. **Class:** `hypothesis`. **Support:** GDR-SRC-20261010-P03-009 and 013 motivate component distinctions, not the full effect. **Confidence:** low; no direct profile comparison inspected. **Applicability:** recurring consequential changes with operable fallback. **Unresolved:** added value over simple flexible presentation; owning topic C-12 is the same claim.

### C-02
**Claim:** Preserve task meaning and legitimate knowledge while allowing presentation to change. **Class:** `inference`. **Basis:** original task analysis; owning topic C-09 and inspected P01 information-route distinctions. **Confidence:** moderate as a design criterion. **Limit:** no equivalence claim for emotion, difficulty or every input method. **Unresolved:** whether the new representation is understood and usable.

### C-03
**Claim:** Separate meaningful preferences, device-local settings and temporary task state; allow intentional mixed input. **Class:** `inference`. **Sources/locators:** 009, graphics-settings advice; 013, Additional considerations/active-input guidance. **Bridge:** device-specific technical settings do not make a person's preference or current selection disposable. **Confidence:** moderate. **Limits:** complete architecture and trigger policy unvalidated; no diagnosis inferred. **Unresolved:** minimal usable persistence/override design.

### C-04
**Claim:** Explicit context triggers and preservation rules may avoid destructive mode changes. **Class:** `hypothesis`. **Basis:** original synthesis; 013 mixed-input guidance provides adjacent rationale only. **Confidence:** low for comparative efficacy. **Unresolved:** detection uncertainty, prompt stability and recovery burden; no universal delay prescribed.

### C-05
**Claim:** A profile must be assessed at the actual task and final presentation, including failure/recovery paths. **Class:** `inference`. **Bridge:** available inputs or correctly sized elements alone do not establish preserved operation; owning topic C-09/C-11. **Confidence:** moderate for diagnostic discipline. **Limit:** not a conformance test suite or user-equivalence proof. **Unresolved:** combined access/language/context behavior.

### C-06
**Claim:** Profiles should be omitted or simplified when their state/configuration cost lacks task-specific benefit. **Class:** `inference`. **Basis:** original cost/alternative analysis and absence of complete-process evidence. **Confidence:** moderate for conditional choice, magnitude unknown. **Limit:** not proof that profiles generally fail. **Unresolved:** useful context granularity and maintenance burden.

### C-07
**Claim:** Examples, transition records and playtests are proposals, not validated instruments or performed work. **Class:** `hypothesis`. **Basis:** original P03 synthesis with inspected F01 discrimination correction retained as a caution. **Confidence:** low for diagnostic validity. **Limits:** no approved numeric threshold/sample, empirical result or disability simulation. **Unresolved:** study approval, feasibility and representative evaluation.

### C-08
**Claim:** The brief authorizes this draft pattern, not implementation, participant work or release. **Class:** `studio-decision`. **Owner/date/source:** Doug, 2026-10-10, complete P03 brief, Assigned Outputs and execution limits. **Confidence:** high for explicit scope. **Unresolved:** independent review, allocation reconciliation and later decisions.

## References

All source identities below are run-scoped candidates. Access was `relevant-excerpt` on 2026-10-10: actual public HTML/text or transcript passages, not merely search summaries. Repeated records support standalone reading, not corroboration.

### GDR-SRC-20261010-P03-009

Valve. [Getting your game ready for Steam Deck and Steam Machine](https://partner.steamgames.com/doc/steamhardware/recommendations). Steamworks Documentation. **Date:** Publication/update unknown. **Edition:** Unnumbered current Steamworks web revision. **Type:** Official platform recommendations. **Locators:** Input → controller and mixed mouse/gamepad input; Game Features → graphics settings and supported resolutions/aspect ratios. **Limits:** Not a formal standard, benchmark or verified game implementation. **Relationship:** Old /steamdeck/recommendations route redirects here; same issuer/program family as 010. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-013

Google. [Enable natural input on all form factors](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors). Android Developers. **Date:** Updated 2026-09-24 UTC; original publication unknown. **Edition:** Current Android game-development web revision. **Type:** Official platform/technical guidance. **Locators:** Keyboard input → configuration change; Gamepad input; Additional considerations; How to respond to user input. **Limits:** General Android support advice; exact engine/device behavior untested here. **Relationship:** Same issuer as 014; neither is a participant study. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

## Related entries and history

[Platform and display context — GDR-CAND-20261010-P03-TOP-02](../topics/platform-and-display-context.md) owns context definitions, measurement scopes and full coverage gaps. [Camera and framing](../topics/camera-and-framing.md) and [Recoverable camera assistance](recoverable-camera-assistance.md) own view-control effects of a profile change.

P01's inspected `GDR-CAND-20261010-P01-PAT-01`, Redundant critical-state cues, owns cue encodings, not this transition lifecycle. Its selected file is not redelivered or falsely linked as part of this five-file packet. P02 controls/feedback/multimodal and P05 full audio/localization remain missing substantive dependencies. No genre files are asserted.

**2026-10-10:** initial `initial-1`, 0.1.0 draft; predecessor and supersedes null. No implementation, independent P03 review, host test, player comparison, acceptance or release. Exact hashes, source bindings, conflicts and next child-work decisions are in the [P03 review packet](../reviews/full-run-20261010-p03-review-packet.md). Next decision: review whether profiles add enough discriminating value to warrant a separately authorized test rather than using the simpler baseline.
