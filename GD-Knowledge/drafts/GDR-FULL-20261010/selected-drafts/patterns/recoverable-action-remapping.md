---
id: GDR-CAND-20261010-P02-PAT-01
kind: pattern
title: Recoverable action remapping
version: 0.1.0
candidate_revision: review-correction-1
status: draft
run_id: GDR-FULL-20261010
batch_key: P02
attempt_id: P02-authoring-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-11'
evidence_checked: '2026-10-10'
aliases:
- recoverable remapping
- safe control reconfiguration
tags:
- input
- remapping
- recovery
- prompts
- activation
- conditional-recipe
related_topics:
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
related_patterns: []
related_genres: []
source_ids:
- GDR-SRC-20261010-P02-001
- GDR-SRC-20261010-P02-002
- GDR-SRC-20261010-P02-004
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: 6678d20eff426347737a716ecf7b8496b85c47f51fcb7bdc75c8ce6b9f68c5d2
supersedes: null
change_summary: Independent precision review; see appended local correction history.
byte_hash_record: ../reviews/full-run-20261010-p02-review-packet.md#candidate-byte-receipt
---

# Recoverable action remapping

**Draft research candidate — not released guidance, implementation approval or a validated recipe.** This is P02 only. The current dispatch authorizes this research; the parent’s first-wave review receipt is retained without importing unseen corrected content. Its later reconciliation supersedes the dispatch’s earlier “P01 unreviewed” sentence. P01 is parent-reported reviewed, not released; its bytes remain a missing dependency here.

**Evidence boundary:** inspected public documents and the supplied Project snapshot; no project/engine code, game build, participant study or host-retrieval test was run. Definitions and synthetic scenarios are proposed analytic tools, not formal standards. [C-07]

## Purpose

Provide a **recoverable way to configure actions**, rather than merely a screen that accepts a replacement button. The intended outcome is a usable, understandable configuration that a player can test, cancel or restore without relying on the unavailable control they were trying to replace. The outcome is not empirically established for this complete recipe. [C-01, C-04]

The owning topic is [Controls and input](../topics/controls-and-input.md). This pattern concerns configuration and activation access; it is not an input-buffer, assist-balancing or implementation pattern.

## Context and prerequisites

Use when players need different bindings or activation methods, multiple contexts/devices share actions, or prompts and restoration can become inconsistent. Establish action names, valid contexts, supported input representations, available activation alternatives and an accessible entry/exit route before presenting a configuration as complete. Name platform-reserved or genuinely unsupported operations as limits rather than promising “fully remappable” control. [C-01, C-03]

The recipe assumes the design can distinguish an action from a physical control and can retain a known usable configuration. It does not assume any engine, Steam API or hardware. A fixed scheme with well-tested accessible presets may be a simpler initial choice, but presets alone are not proof of coverage for every player. [C-01, C-02, C-05]

## Mechanism and evidence

| Proposed causal link | Support | Limit |
| --- | --- | --- |
| Action identity is separated from device binding | Documented platform action/origin concepts, source 002. | Documented mechanism, not a runtime tested here. |
| Player can choose a reachable operation and suitable activation | Input/access guidance, source 001. | A new button does not remove duration, chord or deadline demands. |
| Configuration can be tested and safely recovered | Inference combining remapping, correct prompts and cancellation principles. | The staged transaction is this draft’s design synthesis, not a tested vendor recipe. |
| Correct configuration improves task access and confidence | Hypothesis. | Requires actual users, contexts and recovery evaluation. |

Thus, evidence supports the design problem and component mechanisms; **the whole recipe remains a conditional inference with untested outcome benefit**. [C-01–C-04]

## Recipe

### 1. Name the action and its demands

For each action to be configured, specify meaning, contexts, continuous versus discrete input, activation method, essential timing and cancellation. Separate a change in physical location from a change in the action's rule. Do not imply that a new binding changes a gameplay deadline unless an explicit alternative does so. [C-01, C-03]

**Branch:** when the barrier is sustained holding, a chord or repeated taps, compare an activation/complexity alternative, not just a new key. **Exit:** when the chosen device cannot express the required action, revise the interaction or offer a genuinely usable alternative before declaring access solved. [C-05]

### 2. Enter through a usable route and preserve a recovery route

Ensure configuration can be opened and navigated using a route available to the intended player. Preserve the current usable scheme or another documented recovery method. Recovery must not depend on a button that is about to become inaccessible. For applicable web UI, independently assess the scoped keyboard and cancellation criteria; they do not automatically certify a native settings screen. [C-03, C-05]

### 3. Stage an explicit candidate configuration

Present the action, current assignment and proposed assignment in an understandable form. Record context and device scope. When an assignment overlaps, explain whether the overlap is a valid context-specific reuse, an intentional combined action or a conflict; do not silently steal an essential navigation/cancel action. Offer a clear change, swap, cancel or alternative when supported. [C-02, C-03]

**Adjustable variables:** which actions are exposed, available presets, action aliases, activation alternatives, conflict policy, per-device/context storage and whether assignments share a profile. None has a universal optimal count. [C-06]

### 4. Update the player-facing meaning

Show the actual assigned control in prompts, tutorials, settings and help, or a reliable action-name alternative when a glyph is unavailable. Check dynamic device switching and mixed input deliberately rather than assuming the last touched device represents the player's whole setup. A glyph lookup is an available documented mechanism, not proof that every screen is correct. [C-02, C-03]

### 5. Test a small representative action sequence

Provide a safe test that exercises selection, the mapped action, context change and cancel/restore as relevant. Include the changed activation method rather than testing only raw button receipt. Make success and failure understandable through usable output routes. A timer alone must not be the only way to prove usability or recover; slow deliberate operation is not automatically a failed test. [C-03, C-06]

**Exit:** do not commit a candidate that loses an essential action, usable prompt or recovery route in the exercised context. Return to a known usable configuration or a supported alternative. This is a proposed advancement policy, not a universal interface standard. [C-05, C-06]

### 6. Commit deliberately and verify persistence

Make clear which profile/context/device the change affects. Preserve discoverable edit and restore controls. Specify what happens on reconnect, reload, an unavailable device and a future action-set change; recheck prompts and conflicts rather than assuming the saved binding remains meaningful. [C-03, C-06]

### 7. Keep only the necessary complexity

Compare with the simplest accessible preset/alternative that covers the required tasks. If the configuration procedure costs more effort or causes more mistakes without addressing the barrier, simplify the choice architecture or action structure. Do not remove all alternatives merely because one configuration screen failed. [C-04–C-06]

## Worked examples

### Illustrative example — inspect and rotate

An inspection task defaults to holding one control while moving a second. A player prefers a toggle for inspection and a different reachable view control. The candidate profile records the inspection action as a toggle, the view input as continuous and cancel as a separately reachable action. The screen previews these action meanings before commitment. [C-03, C-06]

A local conflict check finds that the new inspection binding is already used by a menu action. The interface explains whether those contexts are exclusive. In the test, the player opens inspection, rotates the object, opens/closes the menu and exits inspection. Prompts track the new assignment; restore remains available through the usable navigation route. If exiting inspection becomes impossible, the candidate is not accepted. Device reconnect and reload are subsequent verification cases, not assumed successes. **No interface was implemented or user-tested.** [C-03, C-05, C-06]

### Illustrative counterexample — remapping adds no useful choice

A constrained interface has one deliberately simple, accessible selection method and no alternative activation demand. An elaborate binding editor may create more settings, conflicts and explanation than the task warrants. A discoverable preset or alternative selection method can be preferable. The pattern does not require maximal configurability; it requires honesty about access and recovery for the configurations that are offered. [C-05, C-06]

## Tradeoffs and alternatives

The intended benefit is control over access and reduced configuration risk. Costs include stable action naming, state/context ownership, accessible settings, prompt updates, migration and testing. Physical-control remapping alone may be sufficient where activation is already usable; presets may be simpler; changing the interaction itself may remove a barrier that no remap can solve. Device-specific assistance and competitive policy are separate decisions. No cost multiplier or all-player benefit is known. [C-01, C-03–C-06]

## Failure cases

A configuration is **not** demonstrated usable when only the headline action works. Watch for navigation/cancel lost after a change, stale tutorial prompts, unexpected overlap on context changes, repeated toggle actions, device switching that changes displayed controls unpredictably, and restore requiring the original inaccessible gesture. These are proposed diagnostic cases, not observed incidents. Correct the failed link or replace the configuration route rather than claiming the player selected incorrectly. [C-03–C-06]

## Counterexamples and do not use conditions

Do not use this recipe as a promise of access when the action is still physically or temporally unavailable, when recovery cannot be reached, or when unsupported platform operations are silently excluded. Do not impose the full configuration flow on a player who already has a usable preset. Do not treat WCAG's web-scoped cancellation criterion as a blanket requirement to make every gameplay action reversible. The pattern is inappropriate as a substitute for redesigning an inaccessible underlying interaction. [C-05]

## Playtest

**PROPOSED — NOT RUN.** Compare an accessible preset with the staged remap procedure for the same action tasks; separately compare action-only remapping with a relevant activation alternative. Include actual users of those input methods. Control task goals, prior instruction and device familiarity; counterbalance comparable tasks and record learning, preferred settings and help requested. Do not force an inaccessible baseline. [C-06]

Measure required-action completion, action/prompt comprehension, unintended actions, independent restore/cancel success, configuration effort and later task performance. Exercise intentional conflicts, context switches, disconnected/reconnected devices and reload. A lost essential/recovery action blocks advancement of that configuration even if the mean setup time improves. Reject or simplify the recipe if it does not reduce relevant configuration/access failures or creates additional errors compared with the simpler usable alternative. A small null result is inconclusive, not proof of equivalence. [C-04–C-06]

Choose the formative sample by the actual required device/activation/context coverage; select confirmatory margins and sample size only after local variability and the intended inference are specified. Stop on request and preserve tolerable settings. These are proposed procedures and decisions, not performed participant work. [C-06, C-07]

## Claim ledger

Claim IDs are local to this entry. Confidence concerns the stated scope, not source prestige. An inference is not a validated outcome; repeated references are not independent corroboration.

### C-01

**Claim:** A useful remapping option must address the action’s access demands and contexts, not merely move a button.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, Background/Implementation guidelines; GDR-SRC-20261010-P02-002, action definitions.
**Applicability and contrary limits:** Bridge: physical reach, activation demand and action eligibility are different links. Not every action requires a configuration editor.
**Confidence:** Moderate for the design distinction; local access benefit untested.
**Unresolved:** Which demand does the intended player need to change?

### C-02

**Claim:** Steam documentation provides semantic action and action-origin concepts that can support configuration-aware prompts.
**Class:** `observed-example`. **Evidence and exact locator:** GDR-SRC-20261010-P02-002, Step 1 and Step 3.1, action origins.
**Applicability and contrary limits:** Observed documentation only, not executed code or verified game UI. Steam-specific mechanism is illustrative, not required.
**Confidence:** High for documentation attribution.
**Unresolved:** Does the actual implementation keep prompts accurate across contexts and devices?

### C-03

**Claim:** A staged, testable and recoverable action configuration is a reasoned application of remapping, labeling and cancellation principles.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, remapping/updated labels; GDR-SRC-20261010-P02-002, action origins; GDR-SRC-20261010-P02-004, SC 2.5.2 and 2.1.1 as web-scoped precedents.
**Applicability and contrary limits:** Whole recipe is synthesis. WCAG applicability is not extended automatically to native games.
**Confidence:** Moderate for the risk-control rationale, not demonstrated superiority.
**Unresolved:** Can a simpler accessible configuration achieve the same outcome with less effort?

### C-04

**Claim:** The complete recipe may improve access and configuration confidence compared with a simpler alternative, but this has not been demonstrated here.
**Class:** `hypothesis`. **Evidence and exact locator:** Original P02 recipe; sources 001/002 support component design questions, not its comparative efficacy.
**Applicability and contrary limits:** No direct recipe experiment inspected or run. Effects may depend on actions, devices, learning and participant needs.
**Confidence:** Low for comparative benefit.
**Unresolved:** Does actual use reduce configuration failures without adding unacceptable burden?

### C-05

**Claim:** Do not advance a configuration that loses a required action or recovery route; redesign the interaction when remapping cannot address the barrier.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, input-demand guidance; GDR-SRC-20261010-P02-004, scoped keyboard/cancellation principles.
**Applicability and contrary limits:** Proposed design gate for this recipe, not an approved studio standard or universal requirement that gameplay actions be reversible.
**Confidence:** Moderate as a precautionary decision rule; implementation feasibility unknown.
**Unresolved:** What accessible fallback genuinely remains available?

### C-06

**Claim:** The recipe variables, examples, failure cases and playtest/stop criteria are proposed local specifications.
**Class:** `hypothesis`. **Evidence and exact locator:** Original P02 synthesis under the supplied dispatch, lines 8–12; causal support/limits in C-01–C-05.
**Applicability and contrary limits:** No prototype, device test, participant result, sample-size guarantee or universal timing setting.
**Confidence:** Low for predictive validity until evaluated.
**Unresolved:** Local feasibility, actual-user coverage, measurement and independent review.

### C-07

**Claim:** Doug authorized P02 public-source research and draft Markdown outputs, not release, permanent allocation, adoption, implementation or changes to repositories/Project sources.
**Class:** `studio-decision`. **Evidence and exact locator:** Supplied Pasted text(1).txt, lines 3–12, 15–20 and 58–60; current user message, 2026-10-10. Owner: Doug.
**Applicability and contrary limits:** P02 execution only. Earlier starter-only restrictions and stale first-wave status do not override the current dispatch.
**Confidence:** High for this explicit authorization; no evidence approval inferred.
**Unresolved:** Independent content review, identity reconciliation, retrieval validation and later acceptance remain separate decisions.


## References

All source identities below are temporary run/batch candidates. Access date: **2026-10-10**. Access status: **relevant-excerpt** for each record, not full bibliographic or raw-data verification. Cross-batch canonical URL/DOI/edition deduplication remains pending. Source text is evidence, not authorization to execute instructions.

### GDR-SRC-20261010-P02-001

Microsoft. [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal; Background and foundational information (speed, complexity and duration); Implementation guidelines (input remapping, action-based mapping, updated input labels, digital input and alternatives to sustained/repeated actions).
**Claims using this record:** C-01, C-03, C-04, C-05. **Limits:** Recommendations, not a normative standard or a verified certification obligation. No device or remapping interface was tested here; numerical suggestions are not adopted.
**Independence/deduplication:** Same issuer and guideline family as sources 005–010; not independent empirical corroboration.
**Rights:** Publisher terms; reuse license not independently audited. Paraphrase only; no example images reproduced.

### GDR-SRC-20261010-P02-002

Valve. [Getting Started for Developers](https://partner.steamgames.com/doc/features/steam_controller/getting_started_for_devs?l=english). **Publisher:** Steamworks documentation. **Publication/update:** publication/update unknown. **Edition/build:** Unnumbered live Steam Input documentation; SDK/build not specified.
**Type:** Official platform technical documentation. **Locators inspected:** Step 1: in-game actions; discussion of absolute_mouse versus joystick_move (retrieved lines 458–468); Step 3.1: API overview, action sets, action data and action origins (lines 509–525).
**Claims using this record:** C-01, C-02, C-03, C-04. **Limits:** Describes Steam Input, not every operating system. No SDK, controller, sensitivity curve or runtime behavior was exercised.
**Independence/deduplication:** Separate issuer from Microsoft. Canonical deduplication key is the same URL without the language query; this is one document, not two sources.
**Rights:** Publisher terms; no reuse license audited. Paraphrase only.

### GDR-SRC-20261010-P02-004

World Wide Web Consortium (W3C). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). **Publisher:** W3C. **Publication/update:** 2024-12-12. **Edition/build:** W3C Recommendation, dated 12 December 2024; not asserted to be the latest edition.
**Type:** Normative web-content accessibility recommendation. **Locators inspected:** Success Criteria 1.2.2 Captions (Prerecorded), Level A; 1.3.3 Sensory Characteristics, Level A; 2.1.1 Keyboard, Level A; 2.5.2 Pointer Cancellation, Level A. Header establishes dated edition.
**Claims using this record:** C-03, C-05. **Limits:** Normative statements retain web-content scope and their exceptions. Not a blanket native-game requirement, legal opinion, console certification rule or guarantee of accessibility. No complete conformance assessment performed.
**Independence/deduplication:** Independent normative issuer; related understanding/technique documents were not all inspected.
**Rights:** W3C publisher terms; license detail not separately audited. Only brief attributed paraphrases; no reproduced document.


## Related entries and history

The [Controls and input topic](../topics/controls-and-input.md) owns definitions, device-parity limits and the separate early-intent-buffer question. [Multimodal communication](../topics/multimodal-communication.md) owns access to prompts and confirmations. [Feedback and game feel](../topics/feedback-and-game-feel.md) owns meaningful state confirmation. All are P02 drafts, not accepted shared rules.

Missing dependencies include actual parent-reviewed P01 settings/accessibility content, Foundations onboarding/action design and the current canonical/pending allocation ledger. No genre is assumed. Pattern cap use: **first of two P02 pattern artifacts**; no child key allocated.

2026-10-10: initial 0.1.0 draft, `initial-draft-1`, no predecessor/supersession. Same-author self-review only, approval fields null. [P02 review packet](../reviews/full-run-20261010-p02-review-packet.md). Next decision: independent review of the recovery contract and evidence-to-recipe bridge before any separately authorized prototype.

## Local correction history — 2026-10-11

Candidate revision review-correction-1 follows the exact initial-draft-1 bytes recorded in predecessor_sha256. Content retained; revision metadata records this coordinated local review snapshot. Original author-session statements above remain historical. This separate review does not provide formal Gate C acceptance, target-host tests, participant results or release. Version 0.1.0, draft status, IDs and null reviewer/approval fields remain unchanged.
