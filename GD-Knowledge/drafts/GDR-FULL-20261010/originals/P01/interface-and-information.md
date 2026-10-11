---
id: GDR-CAND-20261010-P01-TOP-02
kind: topic
title: Interface and information
version: 0.1.0
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P01
identity_scope: temporary run-scoped candidate; permanent allocation pending
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- HUD design
- menus and inventories
- maps and notifications
- settings discoverability
tags:
- interface
- information
- HUD
- menus
- inventories
- maps
- notifications
- settings
- discoverability
related_topics:
- GDR-CAND-20261010-P01-TOP-01
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-P01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P01-01
- GDR-SRC-20261010-P01-04
- GDR-SRC-20261010-P01-06
- GDR-SRC-20261010-P01-07
- GDR-SRC-20261010-P01-09
- GDR-SRC-20261010-P01-10
- GDR-SRC-20261010-P01-11
- GDR-SRC-20261010-P01-14
- GDR-SRC-20261010-P01-15
- GDR-SRC-20261010-P01-16
- GDR-SRC-20261010-P01-17
- GDR-SRC-20261010-P01-18
reviewer: null
approved_by: null
approved_date: null
---

# Interface and information

**Draft research candidate — not released guidance.** The central recommendation is to choose representations around a task-information contract, not to rank interfaces by how little screen space they occupy or how convincingly they belong to the fictional world. That recommendation is an inference; the inspected studies do not establish a universally superior HUD or menu architecture. [C-01–C-03]

## Decision and scope

**Decision:** What information should be available, where, when, through which interaction route, and with what recovery path so that a player can make an intended decision?

Own HUDs, menus, inventories, maps, notifications, settings and interface discoverability. This entry concerns representation and access to information, not the full design of progression, inventory economies, spatial layouts, quest systems or learning/onboarding. Foundations owns learning/onboarding mental models; those explanations are deliberately not duplicated here. The related [visual topic](visual-communication.md) owns visual communication, and the [accessibility topic](accessibility-and-inclusive-interaction.md) owns end-to-end access planning and representative evaluation.

### Working definitions

For this draft, a **HUD** is information presented during ongoing play. A **diegetic representation** is attributed to the fictional world; a **world-attached representation** is positioned in relation to a world object, whether or not it is fictional-world content. Neither property guarantees accessibility, clarity or involvement. A **menu** organizes available choices; an **inventory** supports decisions about held or available entities; a **map** communicates spatial relationships; a **notification** calls attention to a change. **Discoverability** means finding an available action or setting without already knowing its exact location—not a claim that an entire mechanic has been learned. [C-01, C-03, C-09]

### Task-information contract

The following is a proposed design record. It is not an approved runtime schema or implementation specification. [C-01]

| Field | Question the designer must answer |
| --- | --- |
| Decision and entitlement | What may the player decide now, and what facts are they legitimately entitled to know? |
| State and uncertainty | What is known, unavailable, pending, approximate or intentionally undisclosed? |
| Temporal relevance | Is the fact persistent, newly changed, time-sensitive or historical? What makes it stale? |
| Required precision | Does the task need an exact amount, a category, direction, relative order or merely awareness? |
| Accessible representation | Which preferred input and output routes carry the needed meaning, not just a decorative alert? |
| Action and recovery | What action is available, what happens on activation, and how can the player cancel, correct or return? |
| Ownership | Which content/state owner is responsible for updates, translation, access equivalents and correction? |

A later application must declare display size/resolution/distance, input method, listening context, assistive technology, languages, current task load and first-use versus practiced context. No specific game, engine, desktop setup or platform is assumed. This batch did not measure any interface in use. [C-12, C-13]

## Core explanation and mechanisms

An interface can fail because information is absent, hard to locate, misinterpreted, stale, impossible to act on, or impossible to recover from. These are different repair targets. Adding an icon addresses none of them automatically. The proposed chain is **available facts → findable representation → interpretable state/action → operable choice → understandable result/recovery**. Guidance supports portions of this chain; no inspected experiment validates the whole architecture for all games. [C-01, C-04–C-10]

### What the HUD evidence permits

Iacovides and colleagues used a selected Battlefield 3 level in two studies. Study 1 involved nine experienced male players. Study 2 involved 24 participants, with 10 self-classified experts and 14 novices; seven potential participants were excluded for control difficulties. The comparison therefore did not represent players unable to manage those controls. [C-02; GDR-SRC-20261010-P01-14]

For Study 2 overall involvement, the reported condition effect was p=.117, expertise interaction p=.051 and expert simple comparison p=.058. Those comparisons do not establish an overall benefit of HUD removal. Subscale results differ, and a reported expertise F(1,20)=6.13 paired with p=.797 is internally inconsistent. No correction or reanalysis was performed here. Preserve the source’s suggestive, narrow result without adopting stronger abstract/discussion wording as proof. [C-02]

The design implication is not “always show a HUD.” It is to compare representations while preserving required facts and evaluating the intended population. If removing a display also changes available information, response effort or access routes, those differences belong in the explanation of the result. “Less interface” is not an isolated mechanism. [C-03]

### Guidelines and outcome evidence are different

XAG 112 recommends reachable access settings from initial launch and consistent navigation. XAG 113 addresses focus visibility and modal focus. XAG 106 addresses meaningful narration. XAG 115 addresses errors and destructive actions. These documents provide concrete review questions, not measured proof that every proposed application below improves play. [C-04, C-06, C-07; GDR-SRC-20261010-P01-06, GDR-SRC-20261010-P01-09, GDR-SRC-20261010-P01-17, GDR-SRC-20261010-P01-18]

A source cross-reference needs correction at use: XAG 113’s resource table labels WCAG 2.4.11 as a Focus Appearance criterion. The current inspected WCAG 2.2 Recommendation names 2.4.11 **Focus Not Obscured (Minimum)** and places **Focus Appearance** at 2.4.13. [C-14; GDR-SRC-20261010-P01-01] This is a stale locator, not evidence that focus visibility is unimportant. The accessibility topic owns the formal standards discussion. [C-05; GDR-SRC-20261010-P01-17]

## Design choices and alternatives

### Choose presentation by task, not a diegetic/non-diegetic ranking

| Representation | Reason to consider it | Important cost and exit condition |
| --- | --- | --- |
| Stable screen-space HUD | Frequent decisions depend on a repeatedly consulted state. | Occupies view and can compete with play. Reduce or make optional when persistent display has no useful decision role. |
| World-attached or world-attributed display | Location or relationship to an object contributes meaning. | Distance, camera framing and occlusion can remove access. Provide another route when those conditions block required facts. |
| On-demand panel | Information is needed for deliberate planning or review rather than continuous response. | Retrieval has an interaction/time cost. Do not hide a required urgent fact behind an unworkable sequence. |
| Contextual summary plus detail | A compact current state suffices until a player asks why or compares alternatives. | The summary can conceal an exception or available action. Preserve a discoverable expansion and return path. |
| No additional display | Existing representations already support the decision. | Demonstrate that required facts remain obtainable; omission is not justified by aesthetic preference alone. |

These are conditional inferences. A mixed presentation is a legitimate comparison, not a compromise that must be worse than a “pure” style. [C-01, C-03]

### Decisions across the assigned interface surfaces

| Surface | Proposed decision policy | Alternative or counterpressure |
| --- | --- | --- |
| Menus | Use honest labels, a coherent navigation order and an explicit return/cancel behavior. Make focus distinct from activation. | Different devices may need different presentation without changing action meanings. Uniform geometry is not the goal. |
| Inventories | Support the actual comparison: attributes, compatibility, quantities, current selection and consequences. Keep selection identifiable when sort/filter changes. | A spatial grid can communicate shape/placement; a labeled list can support serial review. Neither format owns every task. |
| Maps | Represent the spatial facts the task needs, including uncertainty. Consider a structured route/location list when purely spatial interaction is inaccessible. | A list may omit adjacency or route shape. Describe what it retains, what it loses and how users obtain missing facts. |
| Notifications | Separate a state change, its priority and its history. Define acknowledgement, resolution, expiry and replay independently. | A replay log cannot replace a usable timely warning; every minor update need not interrupt the current action. |
| Settings | Make choices reachable and understandable before the affected barrier. Explain effect and scope, offer a credible preview or safe return, and distinguish applied from saved values. | Mandatory long configuration can itself block entry; a preset without local overrides can be wrong for a particular need. |
| Discoverability | Name the action/setting in language connected to its visible effect, with usable feedback when it changes. | More explanations can obstruct frequent operations. Offer detail without requiring memorization of a hidden gesture. |

These policies are proposed application processes, not findings from one universal interface experiment. [C-05, C-08–C-10, C-12]

### Notification and settings tradeoffs

A proposed notification record distinguishes **current state**, **change event**, **urgency** and **history**. Repeating “route blocked” on every update may provide no new decision information. Suppressing the only current blocked-state signal, however, is a different error. Compare coalescing repeated events with preserving inspectable current state; do not treat them as the same operation. [C-08]

For settings, consider accessible defaults and a short first-run route, with later detail and local overrides. The Access Profiles study supplies a relevant challenge: participants raised trust and implementation concerns and differed over startup prompts. That is qualitative evidence of tensions, not proof that profiles or a particular menu reduce configuration burden. [C-10, C-11; GDR-SRC-20261010-P01-15]

Decide separately whether a setting applies to a device, player, save or current session. Do not silently restore a different access configuration when loading a save, changing input, or trying a preset. That is an autonomy/recovery inference; no save-system behavior or cloud synchronization was implemented or verified here. [C-10, C-13]

## Application process

1. **Diagnose a real decision failure.** Record whether information was absent, undiscovered, misunderstood, stale, inoperable or unrecoverable. Do not start with a preferred interface aesthetic.
2. **Write the contract.** Use the fields above for each consequential decision. Include what remains legitimately unknown and which changes warrant interruption.
3. **Choose and compare representations.** Select the smallest set that can carry the required facts. Identify what a simpler representation would lose and what a more elaborate one adds.
4. **Specify interaction transitions.** Describe focus, selection, activation, pending result, cancellation, completion and return. State what happens after an item disappears or a list changes. Keep the result intelligible through chosen access routes.
5. **Specify settings and localization behavior.** Explain setting effects, persistence scope, preview, reset and recovery. Track labels against actual remapped actions. Plan translation and semantic narration together.
6. **Prototype and evaluate only under later authorization.** Use representative tasks, access routes and first-use/practiced contexts. Revise the contract or remove the presentation when it adds cost without needed information.

This is conceptual design guidance, not engine implementation authority. [C-01, C-05, C-08–C-13]

## Patterns and genre adaptations

[Redundant critical-state cues — GDR-CAND-20261010-P01-PAT-01](../patterns/redundant-critical-state-cues.md) is relevant when a required state is currently tied to one unreliable or unavailable presentation channel. It does not justify duplicating all notifications or removing player controls. The [visual topic](visual-communication.md) addresses the appearance of hierarchy and state; the [accessibility topic](accessibility-and-inclusive-interaction.md) addresses end-to-end usability.

No genre research was assigned here. No one-file-per-genre artifact is implied by these task examples. Foundations’ learning/onboarding, challenge/difficulty and decision design; Worlds’ spatial/quest work; and this domain’s controls, localization, platform and multimodal full topics remain named dependencies, not fabricated file links.

## Examples and counterexamples

### Illustrative worked example: comparing and dismantling equipment

**Synthetic; not a shipped-game observation or test.** The player is comparing two items and may permanently dismantle one. Required facts are the selected item, relevant comparison attributes, dismantling consequence and whether the operation can be undone. [C-12]

A compact list provides names and a meaningful comparison summary; a detail panel provides the full attributes. Digital focus moves between rows without dismantling anything. A sort change retains the selected item by meaning rather than implying that the same row position is still the same object. A narration route identifies the item and selected action, not every decorative flourish. These transition rules are proposed, not implemented. [C-05, C-06, C-09]

If dismantling is reversible, an explicit result and usable undo may be a better candidate than a repeated confirmation dialog. If genuinely irreversible, present the affected item and consequence before commitment, with an ordinary cancel path that does not require an inaccessible hold. Confirmation friction is a choice to test; imposing it on every harmless action may create unnecessary burden. [C-07, C-12]

**Failure branches:** A filter hides the selected item; state where selection moved or clear it explicitly. A stale comparison refers to the previous item; reject the version rather than blaming the player. A reset command also erases access settings; separate its scope and provide recovery. These corrections address semantic/interaction failures, not just layout polish. [C-05, C-07, C-13]

### Illustrative worked example: a map update during a menu task

The player is reviewing supplies when a selected route becomes unavailable. A brief notification reports that change, while the map and its accessible route list reflect the current state. The route remains unavailable until the underlying state changes, whether or not the notification is dismissed. The history can explain what changed but must not present stale information as a current route recommendation. [C-08, C-09, C-12]

Do not steal modal focus for every low-priority update. Conversely, a change that invalidates the action about to be committed may need intervention. The contract must decide which case applies; urgency is not determined solely by an artist’s choice of red. [C-01, C-05, C-08]

### Strongest counterexample: continuous precision demand

An on-demand panel may work for deliberate planning but fail when the player cannot safely leave the current task. A persistent summary can then be preferable despite occupying space. The reverse also occurs as a design possibility: a persistent display can distract from a task that needs it only between actions. Neither example supplies measured efficacy; they demonstrate why one universal HUD policy is under-specified. [C-03, C-12]

## Failure modes and constraints

**Access.** Avoid a settings bootstrap failure: a player should not need a function they cannot use merely to enable its alternative. Focus, reading order, remapped prompts and the result of a choice all matter. An accessible menu alone does not establish that the subsequent map or inventory is operable. [C-04–C-06]

**Cognitive effort and interruption.** A log can reduce memory demands only if the relevant information is findable and correctly dated. Extra warnings can be ignored or burdensome; that outcome is a hypothesis requiring actual evaluation, not a reason to omit essential facts. [C-08, C-12]

**Localization.** Labels, comparison units, sort order, text expansion and narration need consistent meaning. A compact abbreviation that works in one language is not an automatically reusable icon system. Coordinate translations without claiming that a general text guideline validates every script. [C-13]

**Ethics.** Do not disguise destructive actions, conceal the effect of a preset, or make undo/cancel less intelligible to produce commitment. Avoid collecting diagnoses merely to choose an interface preset. These are original ethical constraints for review, not legal conclusions or empirically measured harms. [C-07, C-10, C-12]

**Production.** Maintain an inventory of states, transitions, settings interactions and content exceptions. Assign ownership for updates and access equivalents. Test changes to sorting, selection, filtering, translation and state persistence together when they interact. No engine architecture, certification checklist, budget or staffing estimate was produced. [C-13]

## Playtest and validation

**PROPOSED — NOT PERFORMED.** No prototype, participant session, input/assistive compatibility test or host test occurred. [C-12]

**Question and comparisons.** Can the player find the needed information, choose correctly and recover? Compare the current representation with a contract-driven repair. For HUD questions, preserve required task facts across representations or declare the information difference a separate factor. Do not use “immersion” as a substitute for task success or access.

**Procedure.** Use first-entry configuration, inventory comparison, a map decision, a notification during another task, a changed setting and recovery from an error. Counterbalance matched task variants and distinguish novice from practiced use. Record familiar input, access needs and chosen settings. Test delayed return and changed content because memorizing one menu is not evidence of general discoverability.

**Participants.** Recruit users relevant to the supported access routes and languages, not solely people who can already complete the default controls. Decide sample size and precision from the decision and pilot variability before later execution. Resource limits must narrow the resulting claim rather than erase excluded populations.

**Measures.** Record independent task completion, interpretation of current versus historical state, focus/selection errors, time and navigation effort, wrong commitments, recovery success, need for researcher assistance, comfort and preference separately. A narration transcript can be semantically complete yet too slow or confusing for the task; measure actual use.

**Falsification.** Reject the proposed architecture’s advantage when equivalent information is not preserved, when improvement disappears outside practiced use, or when a supported access route is blocked. A critical stale-state or irreversible-action misunderstanding blocks advancement of that candidate under this proposed policy. Otherwise predeclare locally meaningful improvement and tolerated costs. An insignificant result is not proof of equal usability. Prefer a simpler version when added interface structure has no relevant value. Stop on participant request or discomfort.

## Claim ledger

Claim class and confidence are separate. Confidence describes the exact, limited proposition, not the effectiveness of a whole design. Proposed illustrations, recipes and participant protocols are not observations.

### C-01

**Claim:** Specify a task-information contract before choosing HUD, menu, map or notification presentation. **Class:** `inference`. **Confidence:** moderate: Information and operability requirements motivate the contract; no one layout is established.

**Sources and locators:** GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.; GDR-SRC-20261010-P01-09 — Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.; GDR-SRC-20261010-P01-18 — Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which facts need persistence, timing, uncertainty and recovery?

### C-02

**Claim:** The inspected HUD paper does not establish a general overall-involvement advantage for HUD removal. **Class:** `empirical-evidence`. **Confidence:** moderate: Two narrow studies; overall statistical claims and exclusions restrict interpretation.

**Sources and locators:** GDR-SRC-20261010-P01-14 — Study 1 and Study 2 methods; Study 2 Results and Table 2, PDF pp.5–7 (including repository cover), especially p.7; Discussion/limitations. Table page screenshot inspected.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Would a matched comparison with necessary information preserved change the conclusion?

### C-03

**Claim:** Treat fixed, world-attached and on-demand interfaces as conditional alternatives rather than immersion rankings. **Class:** `inference`. **Confidence:** moderate: A world-attributed display can still be occluded or inaccessible; comparative benefit is unresolved.

**Sources and locators:** GDR-SRC-20261010-P01-14 — Study 1 and Study 2 methods; Study 2 Results and Table 2, PDF pp.5–7 (including repository cover), especially p.7; Discussion/limitations. Table page screenshot inspected.; GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which representation best supports the required decisions for this audience?

### C-04

**Claim:** XAG 112 recommends an accessible path to settings from initial launch and consistent navigation. **Class:** `practitioner-heuristic`. **Confidence:** high: Accurate attribution; no universal startup flow has been demonstrated.

**Sources and locators:** GDR-SRC-20261010-P01-09 — Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which first-run configuration remains operable without prior configuration?

### C-05

**Claim:** Separate focus, selection, activation and modal ownership, and retain a usable return path. **Class:** `inference`. **Confidence:** moderate: Derived from focus/input guidance; detailed transition policy is proposed.

**Sources and locators:** GDR-SRC-20261010-P01-17 — Implementation guidelines → visible focus, keeping focused elements in view, focus within modal dialogs; Resources and tools.; GDR-SRC-20261010-P01-07 — Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What happens after reordering, deletion, device change and closing a modal?

### C-06

**Claim:** XAG 106 recommends meaningful screen narration of interface information and controls rather than indiscriminate reading of decoration. **Class:** `practitioner-heuristic`. **Confidence:** high: Source guidance inspected; actual assistive compatibility not tested.

**Sources and locators:** GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Can users identify state, action and result in the actual implementation?

### C-07

**Claim:** XAG 115 recommends understandable errors and review/correction/reversal around destructive actions. **Class:** `practitioner-heuristic`. **Confidence:** high: Vendor guidance, not measured confirmation efficacy.

**Sources and locators:** GDR-SRC-20261010-P01-18 — Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** When should recovery replace a confirmation, and which actions are genuinely irreversible?

### C-08

**Claim:** Make notifications accountable to state, priority, freshness and replay needs rather than treating every event as an interrupt. **Class:** `inference`. **Confidence:** moderate: Synthesis seeks to retain useful information without constant interruption.

**Sources and locators:** GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.; GDR-SRC-20261010-P01-10 — Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.; GDR-SRC-20261010-P01-18 — Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Can coalescing, expiry or speech interruption conceal a critical change?

### C-09

**Claim:** Provide inventory/map representations appropriate to the decision, including usable non-spatial alternatives when spatial presentation blocks access. **Class:** `inference`. **Confidence:** moderate: Logical dependence of comparison/navigation on available facts; no universal list-versus-grid result.

**Sources and locators:** GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.; GDR-SRC-20261010-P01-07 — Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.; GDR-SRC-20261010-P01-16 — Experiment: Clutter Rankings for Maps; Results, printed pp.767–768 (PDF pp.7–8); Figure 2 and Conclusions on printed p.768/PDF p.8. Page image inspected.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What meaningful spatial or comparative information is lost by the alternative?

### C-10

**Claim:** Combine reachable settings, legible explanations and reversible changes; neither maximal options nor compulsory configuration is inherently inclusive. **Class:** `inference`. **Confidence:** moderate: Guidance plus limited qualitative evidence warrant alternatives, not a fixed menu architecture.

**Sources and locators:** GDR-SRC-20261010-P01-09 — Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.; GDR-SRC-20261010-P01-15 — §4.1 player study; §4.2 developer study; §4.3 analysis; §5.3.2 hesitations; §6.4 limitations; Copyright statement.; GDR-SRC-20261010-P01-18 — Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which defaults, overrides and configuration burden fit the actual users?

### C-11

**Claim:** Access Profiles participants raised implementation-trust and configuration concerns, including differing reactions to startup prompts. **Class:** `empirical-evidence`. **Confidence:** moderate: Qualitative findings in a small probe/interview study, not population prevalence or causal efficacy.

**Sources and locators:** GDR-SRC-20261010-P01-15 — §4.1 player study; §4.2 developer study; §4.3 analysis; §5.3.2 hesitations; §6.4 limitations; Copyright statement.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Will similar tensions appear outside experienced and indie-development samples?

### C-12

**Claim:** The proposed workflows, worked cases and tests can be evaluated for task success, discoverability and recoverability without presuming a preferred visual style. **Class:** `hypothesis`. **Confidence:** low: All application/test details are original prospective proposals.

**Sources and locators:** GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.; GDR-SRC-20261010-P01-14 — Study 1 and Study 2 methods; Study 2 Results and Table 2, PDF pp.5–7 (including repository cover), especially p.7; Discussion/limitations. Table page screenshot inspected.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Does the design improve required outcomes across relevant access and experience groups?

### C-13

**Claim:** Interface localization, input labels, setting persistence and state consistency require production ownership and regression review. **Class:** `inference`. **Confidence:** moderate: Dependencies are explicit; engine behavior, staffing and implementation cost were not measured.

**Sources and locators:** GDR-SRC-20261010-P01-04 — Background and foundational information → measuring text body height; Implementation guidelines → Text size, Text scaling, Font, and language-dependent alignment.; GDR-SRC-20261010-P01-07 — Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.; GDR-SRC-20261010-P01-09 — Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.; GDR-SRC-20261010-P01-18 — Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Can changes remain coherent across languages, devices and save states?

### C-14

**Claim:** In the inspected WCAG 2.2 Recommendation, 2.4.11 is Focus Not Obscured (Minimum), while 2.4.13 is Focus Appearance. **Class:** `formal-standard`. **Confidence:** high: Normative publisher headings inspected; this corrects a stale vendor resource-table label, not a native-game conformance finding.

**Sources and locators:** GDR-SRC-20261010-P01-01 — Status of This Document; §§1.3.3, 1.4.1, 1.4.3, 1.4.10, 1.4.11; §§2.4.3, 2.4.7, 2.4.11–2.4.13; §§2.5.7–2.5.8; conformance scope.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which focus criteria apply to a later declared product scope?

## References

All identities below are **temporary P01 source candidates**. Access date: **2026-10-10**. `relevant-excerpt` means the cited passages were inspected, not every linked resource. Repeated records enable standalone reading and are not independent corroboration. Cross-batch reconciliation by canonical URL/DOI/edition remains pending.

### GDR-SRC-20261010-P01-01

**World Wide Web Consortium (W3C).** [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). W3C. **Publication/update:** 2024-12-12. **Edition/version:** W3C Recommendation, WCAG 2.2, dated revision.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Normative accessibility specification (formal-standard within its scope). **Precise inspected locators:** Status of This Document; §§1.3.3, 1.4.1, 1.4.3, 1.4.10, 1.4.11; §§2.4.3, 2.4.7, 2.4.11–2.4.13; §§2.5.7–2.5.8; conformance scope.

**Inspected access route:** [public copy](https://www.w3.org/TR/WCAG22/). **Local claims:** C-14. **Limits:** Web-content criteria, not automatic native-game conformance, legal advice, or a complete audit. Exceptions and conformance level matter. No universal native display or controller size follows.

**Independence/derivation:** Source 02 interprets this family for non-web use; several XAG resource lists refer to WCAG. Those are not independent experiments. **Rights:** W3C document copyright/use terms apply; paraphrase only, no reproduced figures.

### GDR-SRC-20261010-P01-04

**Microsoft.** [Xbox Accessibility Guideline 101: Text display](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Background and foundational information → measuring text body height; Implementation guidelines → Text size, Text scaling, Font, and language-dependent alignment.

**Local claims:** C-13. **Limits:** Pixel body height is not a font point/em size. Display category and resolution are explicit. Numeric suggestions are vendor guidance, not universal perception thresholds.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-06

**Microsoft.** [Xbox Accessibility Guideline 106: Screen narration](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.

**Local claims:** C-01, C-03, C-06, C-08, C-09. **Limits:** Semantics and usability must be verified in an actual build; this inspection proves no engine or screen-reader compatibility.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-07

**Microsoft.** [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.

**Local claims:** C-05, C-09, C-13. **Limits:** Remapping alone is not a remedy for all physical or timing demands. Embedded demonstrations were not independently played.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-09

**Microsoft.** [Xbox Accessibility Guideline 112: UI navigation](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.

**Local claims:** C-01, C-04, C-10, C-13. **Limits:** No comparative study establishes one universal settings-onboarding sequence. Linked game examples are vendor accounts.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-10

**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.

**Local claims:** C-08. **Limits:** Motion controls do not establish photosensitivity safety, camera comfort across platforms, or an appropriate numerical limit.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-11

**W3C Web Accessibility Initiative, Education and Outreach Working Group; editor Shawn Lawton Henry.** [Involving Users in Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/involving-users/). W3C WAI. **Publication/update:** First published 2005-11; content updated 2021-06-01; links updated 2024-04-30. **Edition/version:** Dated informative WAI web guidance.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official evaluation guidance (practitioner-heuristic). **Precise inspected locators:** Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Local claims:** C-12. **Limits:** Web evaluation guidance, not a game-specific sampling theorem. A few users cannot stand in for every disability, device, or language.

**Independence/derivation:** Same standards organization as sources 01–02, different informative purpose; not a new empirical dataset. **Rights:** W3C document copyright/use terms apply; paraphrase only.

### GDR-SRC-20261010-P01-14

**Ioanna Iacovides, Anna Cox, Richard Kennedy, Paul Cairns, Charlene Jennett.** [Removing the HUD: The Impact of Non-Diegetic Game Elements and Expertise on Player Involvement](https://doi.org/10.1145/2793107.2793120). ACM CHI PLAY; White Rose Research Online copy. **Publication/update:** 2015; CHI PLAY conference 2015-10-05 to 2015-10-07. **Edition/version:** Accepted Version deposited at White Rose; proceedings pp.13–22.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original mixed-methods game-interface study (empirical-evidence). **Precise inspected locators:** Study 1 and Study 2 methods; Study 2 Results and Table 2, PDF pp.5–7 (including repository cover), especially p.7; Discussion/limitations. Table page screenshot inspected.

**Inspected access route:** [public copy](https://eprints.whiterose.ac.uk/id/eprint/130581/1/Diegesis_and_immersion_final.pdf). **Local claims:** C-02, C-03, C-12. **Limits:** One selected Battlefield 3 level; expertise and input-selection limits; weak overall comparisons and an internally inconsistent reported statistic require caution. No reanalysis or replication.

**Independence/derivation:** UCL metadata, DOI and White Rose are routes to the same paper; its two studies do not independently establish a universal HUD policy. **Rights:** Repository cover states rights reserved unless otherwise indicated; accepted manuscript paraphrased, no game screenshots redistributed.

### GDR-SRC-20261010-P01-15

**Lloyd May, Dan-Ha Le, Graham Lazorchak, Emily Q. Wang.** [Reimagining infrastructure for video game accessibility: exploring Access Profiles with players with disabilities and game designer-developers](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1823366/full). Frontiers. **Publication/update:** 2026-07-20. **Edition/version:** Frontiers in Computer Science 8:1823366; DOI 10.3389/fcomp.2026.1823366.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original qualitative research-through-design studies (empirical-evidence for reported participant findings). **Precise inspected locators:** §4.1 player study; §4.2 developer study; §4.3 analysis; §5.3.2 hesitations; §6.4 limitations; Copyright statement.

**Local claims:** C-10, C-11. **Limits:** Small, experienced, convenience-recruited groups; microgame probe and interviews, not a released cross-game infrastructure or controlled outcome benefit.

**Independence/derivation:** Player/developer groups form one paper and design inquiry, not independent causal replications; related standards and prior literature are acknowledged dependencies. **Rights:** CC BY stated in article; attribution retained; no participant quotations, images, or datasets reproduced.

### GDR-SRC-20261010-P01-16

**Ruth Rosenholtz, Yuanzhen Li, Jonathan Mansfield, Zhenlan Jin.** [Feature Congestion: A Measure of Display Clutter](https://www.mit.edu/~yzli/clutter.pdf). ACM CHI; MIT author-hosted copy. **Publication/update:** 2005; CHI conference 2005-04-02 to 2005-04-07. **Edition/version:** CHI 2005 paper, pp.761–770; MIT-hosted PDF; DOI not independently verified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original display-perception study (empirical-evidence). **Precise inspected locators:** Experiment: Clutter Rankings for Maps; Results, printed pp.767–768 (PDF pp.7–8); Figure 2 and Conclusions on printed p.768/PDF p.8. Page image inspected.

**Local claims:** C-09. **Limits:** Clutter rankings of printed maps, not game-task performance or a universal information-density threshold. Individual judgments differed; no reanalysis.

**Independence/derivation:** Original 2005 work; related 2007 Measuring visual clutter paper remains a separate uninspected lead. **Rights:** ACM copyright/personal or classroom-use notice; no paper pages or figures redistributed.

### GDR-SRC-20261010-P01-17

**Microsoft.** [Xbox Accessibility Guideline 113: UI focus handling](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/113). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → visible focus, keeping focused elements in view, focus within modal dialogs; Resources and tools.

**Local claims:** C-05. **Limits:** The resource table uses an outdated WCAG 2.4.11 Focus Appearance label. Use the inspected WCAG 2.2 Recommendation for current clause names.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-18

**Microsoft.** [Xbox Accessibility Guideline 115: Error messages and destructive actions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/115). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Local claims:** C-01, C-07, C-08, C-10, C-13. **Limits:** No study here estimates error reduction, confirmation habituation or transaction risk. Security-related exceptions require separate assessment.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

## Open questions and change history

**2026-10-10 — 0.1.0, initial draft.** Bounded P01 public-source research and author synthesis only. Source inspection does not establish production approval, participant validation or acceptance of a recommendation. The author’s challenge and actual document checks are recorded in the [batch review packet](../reviews/full-run-20261010-p01-review-packet.md). Independent review has not occurred. Formal reviewer and approval fields remain null.

Open questions include transfer across platforms, viewing/listening contexts, languages, input and assistive technologies; interactions between access needs; novice/expert differences; maintenance cost; and the comparative value of the proposed alternatives. Resolve source-reporting and dependency gaps before widening claims. No genre entry, canonical integration, permanent ID allocation, live host validation or release is asserted.
