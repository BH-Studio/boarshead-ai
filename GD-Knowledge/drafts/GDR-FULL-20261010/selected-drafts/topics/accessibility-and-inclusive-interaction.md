---
id: GDR-CAND-20261010-P01-TOP-03
kind: topic
title: Accessibility and inclusive interaction
version: 0.1.0
candidate_revision: review-correction-1
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P01
identity_scope: temporary run-scoped candidate; permanent allocation pending
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- game accessibility
- inclusive interaction
- assist options
- accessibility evaluation
tags:
- accessibility
- sensory-access
- motor-access
- cognitive-access
- assists
- representative-evaluation
related_topics:
- GDR-CAND-20261010-P01-TOP-01
- GDR-CAND-20261010-P01-TOP-02
related_patterns:
- GDR-CAND-20261010-P01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P01-01
- GDR-SRC-20261010-P01-02
- GDR-SRC-20261010-P01-03
- GDR-SRC-20261010-P01-05
- GDR-SRC-20261010-P01-06
- GDR-SRC-20261010-P01-07
- GDR-SRC-20261010-P01-08
- GDR-SRC-20261010-P01-09
- GDR-SRC-20261010-P01-10
- GDR-SRC-20261010-P01-11
- GDR-SRC-20261010-P01-15
- GDR-SRC-20261010-P01-18
- GDR-SRC-20261010-P01-19
- GDR-SRC-20261010-P01-20
reviewer: null
approved_by: null
approved_date: null
---

# Accessibility and inclusive interaction

**Draft research candidate — not released guidance, a compliance assessment or an accessibility certification.** The most defensible starting point is an end-to-end account of what the player must perceive, understand and operate, followed by scoped checks and evaluation with relevant users. No inspected source establishes that a feature count, one preset or one disabled participant proves a whole game accessible. [C-01–C-12]

## Decision and scope

**Decision:** Which barriers should be removed by default, which activities should be configurable or assisted, and what evidence is needed to describe the resulting access honestly?

Own sensory, motor and cognitive access; assist-option decisions; representative evaluation; and interactions between these areas. Accessibility is also a review obligation of the other domains, not a final overlay delegated solely to this file. [Visual communication](visual-communication.md) and [Interface and information](interface-and-information.md) own their detailed representations and interface processes. Foundations owns learning/onboarding and challenge/difficulty as full topics. This entry does not replace those topics, a legal review, platform certification, a clinical assessment or an engine integration design.

### Working definitions

**Access** means the person can obtain the required information and perform the intended activity through a supported route under stated conditions. **An assist** changes a demand or supplies support; it need not change the same demand as a difficulty preset. **Inclusive interaction** concerns whether supported participation and choice account for varied needs and contexts rather than merely fitting an assumed default user. These are proposed analytic definitions, not a diagnostic taxonomy or a guarantee of universal usability. [C-01, C-05–C-08]

A barrier can concern entry, information, comprehension, action, timing, endurance, error recovery or social participation. Several can interact. A player may need both readable captions and a less demanding input route; addressing one does not demonstrate the other is accessible. Design around the functional demand and the player’s stated preferences rather than inferring a single need from a diagnosis. [C-01, C-12]

### Scope assumptions to record before application

Specify physical display/viewing distance and lighting; resolution and scaling; listening device/noise and preferred volume; input devices and available controls; actual assistive technology and experience using it; language/script; experience with the activity; session duration and opportunities to pause; and whether the experience is solo, cooperative or competitive. These are proposed context variables, not populations tested here. [C-01, C-12, C-15]

The abstract recommendations are platform-neutral. The inspected normative criteria concern web content; XAG recommendations include particular game/platform contexts. No automatic transfer to VR/AR, mobile, every controller, every age group, every language, or combined sensory limitations is claimed.

## Core explanation and mechanisms

### The complete task matters

The proposed access chain is **enter/configure → perceive → interpret → operate → verify/recover → continue participating**. It is a practical diagnostic model, not an empirically established sequence of mental stages. An unreachable configuration menu can prevent every subsequent assist from being used. A visible message may remain unreadable; a readable message may not explain an action; a remapped action can remain too physically demanding. [C-01, C-05–C-07]

| Link | Inspected support | What remains an inference or unresolved outcome |
| --- | --- | --- |
| Reach configuration without already needing it enabled | XAG 112’s first-launch pathways. | Which startup flow minimizes burden for the actual audience. |
| Obtain required sensory information | XAG 103/104/106 and scoped web criteria. | Whether the chosen alternatives communicate equal task facts, at a usable time. |
| Understand current state and available action | Interface/narration/recovery guidance. | Whether language, attention and prior knowledge allow correct interpretation. |
| Operate without an avoidable incompatible demand | XAG 107 and scoped pointer criteria. | Whether the actual preferred device/assist configuration works in the complete task. |
| Adjust demands without unwanted loss of agency | XAG 108; exploratory Access Profiles findings. | The best assist granularity, default and competitive policy. |
| Establish credible usability evidence | WAI user-evaluation guidance. | Population coverage, effect size and comparative outcomes for this game. |

Consequently, a technically present alternative is a **candidate access route**, not an observed access outcome. The pattern’s full causal benefit remains untested. [C-05, C-10–C-12, C-15]

### Standards and guidance: edition, clause and applicability

| Inspected original document | Date/version | Classification and permissible use |
| --- | --- | --- |
| W3C WCAG 2.2 | Recommendation dated 2024-12-12 | `formal-standard` for its normative web criteria. Identify level, clause, scope and exception before asserting a requirement. |
| W3C WCAG2ICT | Group Note dated 2025-12-11 | `practitioner-heuristic`: informative non-web application guidance; it explicitly creates no requirements. |
| Microsoft Xbox Accessibility Guidelines | V3.2 suite published 2023-06-08; overview updated 2026-08-14; cited numbered pages updated 2026-03-04 | `practitioner-heuristic`: official game guidance, explicitly not a legal/compliance checklist. |
| WAI guidance on involving users in evaluation | Content updated 2021-06-01; links updated 2024-04-30 | `practitioner-heuristic`: informative web-evaluation guidance, applied to games only by stated reasoning. |

This distinction is consequential: a normative web requirement, an informative mapping, a vendor recommendation and a user-study observation cannot be combined into an invented universal rule. No ISO/EN procurement standard or jurisdiction-specific legal analysis was conducted; no claim of satisfying such requirements is made. [C-02–C-04, C-11]

**Example of a scoped numerical rule, not a native-game default:** WCAG 2.2 SC 2.5.8 (AA) requires a pointer target size of at least 24 by 24 CSS pixels, subject to its spacing, equivalent-control, inline, user-agent and essential exceptions. SC 2.5.7 (AA) addresses single-pointer alternatives to dragging, with exceptions. These do not specify every game’s controller selection target, physical touch size or required motor timing. The [visual topic](visual-communication.md) owns this batch’s contrast and text-size examples. [C-02; GDR-SRC-20261010-P01-01]

## Design choices and alternatives

### Sensory access: preserve usable meaning, not just extra output

Compare non-color visual encoding, meaningful narration, captions for relevant sounds, and appropriate alternative cues against the actual information contract. A symbol plus a color can address hue reliance but still requires sight. A caption can preserve an event description while changing its sensory or emotional experience. A vibration can attract attention without identifying which action is needed. Those distinctions follow from the information carried, not a measured equivalence finding. [C-05]

Use visual/text and nonvisual alternatives where relevant, with player control over presentation. Investigate competition between speech, effects, music, captions and visual tasks rather than assuming all outputs should be active at maximum prominence. For combined sensory needs, neither captions alone nor narration alone is a demonstrated solution; specialist requirements and appropriate participants remain a gap in this batch. [C-05, C-12]

### Motor access: diagnose the demand before selecting an assist

XAG 107 explicitly distinguishes speed, complexity and duration from control placement. Its guidance includes action-level remapping and alternatives to repeated, sustained or simultaneous inputs. Changing a button’s location does not logically remove a requirement to sustain it or execute it quickly. [C-06; GDR-SRC-20261010-P01-07]

| Demand to investigate | Candidate support | Counterpressure and alternative |
| --- | --- | --- |
| Precision pointing or dragging | Digital navigation, select-then-place, or another suitable action route. | The alternative may require many steps or lose spatial feedback; evaluate the whole task. |
| Sustained holding | Toggle, automatic continuation or a different activation rule. | A toggle needs clear state and a reachable stop action; unattended continuation may be unwanted. |
| Repetition or simultaneous inputs | Single action mapping, adjustable demand or bypass where appropriate. | Replacing tapping with holding can substitute one incompatible demand for another. |
| Timing | Adjustable response window, pause where compatible, or task-specific assistance. | Shared real-time play may constrain timing changes; expose that limit and investigate other routes. |
| Endurance or posture | Interruptible tasks, retained progress and usable controls in the preferred setup. | A technically short task may still be burdensome in sequence; evaluate session context. |

The table is a proposed diagnosis-to-option process. It is not proof that any one assist preserves every intended challenge or all competitive conditions. Full input-system and balancing design remain separate dependencies. [C-01, C-06, C-08, C-15]

### Cognitive access: reduce unnecessary interpretation and recovery burdens

Start with concrete questions: Can the player tell which mode is active? Is a changed value current or historical? Does the prompt describe the actual remapped action? Can an error be corrected without remembering a hidden sequence? Can nonessential movement or interruption be reduced? These questions connect interface, input and distraction guidance; they are not clinical treatment claims. [C-07]

Consider plain effect descriptions, accessible reminders or logs, consistent transitions, inspectable instructions and reversible choices. An always-expanded instruction panel can itself crowd a comparison task; a log can be unhelpful when poorly organized. Do not equate fewer words with easier comprehension or equate a diagnosis with a single ideal presentation. The useful comparison is whether a particular person can complete and understand the task at acceptable effort. [C-07, C-15]

### Assist options and defaults

XAG 108 recommends changing difficulty without losing progress and adjusting discrete mechanics or assists. This supports identifying the demand being changed rather than calling every alternative an “easy mode.” It does not establish an optimal number of presets or a universal difficulty policy. [C-08; GDR-SRC-20261010-P01-08]

An access aid can change perception, input, timing, knowledge, execution or consequences. Label which effect occurs. Lowering damage does not resolve an unreadable menu; enlarged text does not resolve a required input chord. Where an assist changes shared rules or outcomes, describe that effect neutrally and coordinate with the systems owner. Do not silently remove progress or stigmatize a player for selecting an access route. These are ethical/design inferences, not measured fairness results. [C-01, C-08, C-14]

**Evidence against “more configuration is always better.”** May and colleagues studied nine access-focused player participants using interviews and microgame probes, and five indie developers in interviews. The inquiry reports implementation-trust and configuration tensions, not a controlled improvement in access. Its experienced, convenience-recruited groups and partial prototype limit transfer. The paper is evidence that choices and concerns deserve investigation—not that a cross-game profile architecture is ready to adopt. [C-09; GDR-SRC-20261010-P01-15]

For a later design, compare accessible initial presentation, a short settings route and optional detailed configuration. Make changes inspectable and locally reversible. A proposed preset should express feature preferences rather than infer a diagnosis; avoid collecting sensitive information that the setting does not require. Do not claim privacy simply because a feature is called a profile. Data storage, sharing and consent need separate review. [C-10, C-14]

## Application process

1. **Define the supported activities and claims.** Identify the complete path from first launch through ordinary play, interruption, failure and return. State which platforms, inputs, languages and access routes are actually in scope.
2. **Build a demand/barrier record.** For each activity, record sensory facts, interpretation, precision, timing, simultaneous/sustained input, memory, interruption and recovery demands. Ask users about functional needs without assigning a preset from a diagnosis.
3. **Remove unnecessary barriers before adding options.** Repair contradictory labels, unreachable focus or inaccessible confirmation. An option should not be the only repair for a broken default path.
4. **Choose targeted alternatives.** State what the option changes, what it preserves, and its exit/disable path. Resolve conflicts between settings and explain consequences honestly.
5. **Plan maintenance and evaluation.** Assign owners for content, localization, narration/captions, input prompts, persistence and regression checks. Combine applicable criteria review with user tasks; neither substitutes for the other.
6. **Prototype or recruit only under later authorization.** Test real supported routes with relevant users, retain failures, revise or narrow claims, and record untested combinations.

All workflow steps are proposed application guidance. This batch did not execute a game, configure assistive software, recruit participants or make any purchase. [C-01, C-10–C-15]

## Patterns and genre adaptations

[Redundant critical-state cues — GDR-CAND-20261010-P01-PAT-01](../patterns/redundant-critical-state-cues.md) addresses an important subset: a required fact tied to an unavailable or unreliable channel. It does not solve motor access, every cognitive barrier or the entire accessibility chain. It should be omitted or simplified when extra output does not solve the identified problem. [C-05]

No genre files were assigned. Contexts such as precision, reflection or shared real-time activity are task constraints, not stereotypes about genre audiences. Genre-owned guidance remains separate and unavailable here. Related full topics on controls, camera comfort, multimodal communication, localization, platform/display and Foundations’ learning/difficulty/evaluation remain unresolved dependency links, not claimed completed coverage.

## Examples and counterexamples

### Illustrative worked example: first launch through a timed selection

**Synthetic; no participant or prototype result.** The player must configure presentation and then choose a route before a panel closes. Initial configuration has meaningful labels, a supported digital navigation path and an available narration route; it does not require precision pointing just to enable non-pointer operation. [C-15]

The route task then exposes three separate demands: distinguishing the routes, understanding the consequence and completing an action within the window. Non-color state encoding addresses only part of the first demand. A text/narration explanation addresses meaning, subject to actual comprehension. A timing option or different interaction route addresses the third. No single “accessibility on” flag demonstrates all three. [C-01, C-05–C-08]

The designer records whether the time limit is fundamental to an approved shared activity or incidental interface friction. Where incidental, removing it may be simpler than adding a timing slider. Where fundamental, an alternative must be considered with the systems owner; this research does not silently authorize rule changes. [C-08, C-14]

**Failure branches:** The narration repeats every minor change and obscures the current choice; revise priorities. The toggle continues an action without a discoverable stop; repair control and state feedback. A reset makes the menu unreadable again; preserve or recover the chosen access configuration. These are proposed falsifiable failure cases, not evidence that the example has been validated. [C-05–C-07, C-10, C-15]

### Illustrative counterexample: option abundance

A player encounters a long mandatory configuration screen before learning what its labels change. More available settings can coexist with poor access to the activity. Compare a usable initial state with discoverable local adjustments, keeping advanced options available. Do not replace the problem with an inaccessible “skip” control or hide consequential preset changes. [C-09, C-10, C-15]

### Illustrative counterexample: removing the desired activity

An assist automatically chooses every meaningful route to remove input effort. It may enable progression while also removing the decision the player wanted to make. Consider an alternative input route that retains choice. If no such route is feasible, describe the experience change rather than declaring equivalent participation. This is a candidate countercase, not a claim that automation is always undesirable. [C-01, C-08, C-15]

## Failure modes, ethics and production constraints

**Intersecting needs.** Enlarged text can obscure action information; narration can compete with important sound; simplified input can leave too many sequential steps; a preferred color setting can conflict with a coded state. Treat combinations as meaningful design states, not just independent checkboxes. Their actual frequency and severity remain unmeasured. [C-05–C-07, C-14]

**Photosensitivity and discomfort.** XAG 118 calls for assessing content and addressing problematic presentation rather than relying solely on a warning. This file sets no clinical threshold or safety certificate. Qualified technical review must precede any later exposure study; do not deliberately provoke symptoms to “prove” a warning works. Reduced motion and photosensitivity assessment are distinct checks. [C-13; GDR-SRC-20261010-P01-19]

**Representation and research ethics.** Ask for accommodations, permit a support person where appropriate, provide accessible study materials and withdrawal without penalty, and protect sensitive disclosures. Budget participant compensation before a later study; no compensation or recruitment occurred here. Report barriers as design/context findings, not participant deficits. Avoid assuming one disability identity speaks for everyone with that label. [C-11, C-12, C-15]

**Localization.** Translate setting effects, action prompts and meaningful captions/narration, not just menu headings. Treat script support, text expansion, names, spatial wording and differing language conventions as verification work. No default English interface demonstrates all-language access. [C-14]

**Production and honesty.** Plan access features alongside the content they must represent, then recheck changes. If support cannot be delivered, state the unavailable activities and contexts precisely instead of advertising a broad accessibility claim. This is a proposed disclosure/maintenance policy; actual cost, platform approval and legal obligations are not established. [C-04, C-14]

## Playtest and validation

**PROPOSED — NOT PERFORMED.** No user study, clinical screening, technical photosensitivity analysis, engine test, prototype or compatibility test occurred. [C-15]

### Questions and comparisons

Can users reach the activity, obtain required facts, operate their preferred supported route, recover and continue without unwanted loss of choice? Compare default and targeted alternatives where participation is possible and consented. Do not force a participant through an inaccessible or distressing baseline merely to obtain paired data. Technical checks can establish that a route is missing without exposing a person to it.

Separate **feature presence**, **correct information**, **successful use**, **effort/comfort**, and **desired experience**. A caption exists; it accurately describes a relevant fact; a user can read it; the timing is tolerable; and the experience is desired are distinct propositions. No one measure substitutes for them. [C-05, C-12, C-15]

### Proposed representative-evaluation matrix

| Dimension | Include where relevant | Avoid claiming |
| --- | --- | --- |
| Sensory information | People who rely on captions, non-color presentation, narration or another supported route; preferred configurations. | A muted run by a hearing reviewer represents deaf users, or a filter represents all vision differences. |
| Motor interaction | Users of relevant digital, adaptive or alternative input; differing timing/endurance demands. | Remapping or one successful controller run establishes motor access. |
| Cognitive interpretation | Users with relevant reading, attention, memory or processing needs, considered functionally; first-use and practiced contexts. | One simplified mode suits every cognitive profile. |
| Context and intersections | Actual target devices, languages, interruptions and combinations of access settings. | Testing each feature alone validates all combinations. |
| Experience | Newcomers as well as experienced players and assistive-technology users. | Excluding everyone unable to use the default controls leaves an access-representative sample. |

This matrix is a proposed sampling rationale, not a requirement to collect diagnostic labels or a claim that all cells can be covered in one study. Choose participant numbers from the question, acceptable uncertainty, study design and resources. Report coverage and missing cells explicitly. WAI’s guidance supports combining criteria review and user evaluation, not a universal sample-size guarantee. [C-11, C-12]

### Procedure, measures and confounds

Preflight task facts and supported routes; obtain accessible consent and accommodations; use familiar devices where appropriate; record settings and meaningful prior experience; run representative tasks and error recovery; then allow participants to explain barriers and preferences. Counterbalance only comparable, tolerable conditions. Separate differences caused by content, input familiarity, assistive technology, interface semantics and the prototype’s limitations.

Record independent completion, unavailable facts, wrong interpretations, failed actions, effort, time where appropriate, recovery, requests for help, pauses and withdrawal. Do not discard a barrier because a researcher can explain how to bypass it. Report participant-specific findings and uncertainty instead of converting a small convenience sample into population prevalence. [C-12, C-15]

### Proposed decision rules

A missing required fact or inoperable supported path blocks an unqualified claim about that path. A serious unresolved barrier prompts redesign or explicit scope restriction. Keep an assist only to the extent that actual evidence supports its benefit and acceptable consequences; reject an equivalence claim when choice or knowledge differs. Predeclare any local quantitative benefit and tolerance before execution; none is a universal library threshold. An inconclusive study remains inconclusive. Any request to stop ends the activity, and no distress-provoking exposure test is authorized by this document. [C-05, C-13, C-15]

## Claim ledger

Claim class and confidence are separate. Confidence describes the exact, limited proposition, not the effectiveness of a whole design. Proposed illustrations, recipes and participant protocols are not observations.

### C-01

**Claim:** Assess access through an end-to-end task chain, using functional demands and intersections rather than a diagnosis-to-feature checklist. **Class:** `inference`. **Confidence:** moderate: An unavailable prerequisite blocks downstream tasks; this is a reasoning model, not a population taxonomy.

**Sources and locators:** GDR-SRC-20261010-P01-07 — Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.; GDR-SRC-20261010-P01-09 — Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.; GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which barriers remain after individual features are added?

### C-02

**Claim:** WCAG 2.2 web requirements have defined clauses, conformance levels and exceptions. **Class:** `formal-standard`. **Confidence:** high: Normative publisher inspected; native applicability cannot be presumed.

**Sources and locators:** GDR-SRC-20261010-P01-01 — WCAG 2.2 SC 2.5.8 (AA), Target Size (Minimum), including all five exceptions; SC 2.5.7 (AA), Dragging Movements, including essential and user-agent exceptions; Status of This Document and web conformance scope. The visual topic separately owns contrast and text-size examples.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What is the exact product/component scope of a future conformance claim?

### C-03

**Claim:** WCAG2ICT is an informative Group Note and sets no requirements. **Class:** `practitioner-heuristic`. **Confidence:** high: Explicit scope and status statement.

**Sources and locators:** GDR-SRC-20261010-P01-02 — Abstract; Status of This Document; introductory scope and application to non-web documents/software.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which mappings are defensible for the intended native product?

### C-04

**Claim:** XAG V3.2 is game-accessibility guidance, not a legal/compliance checklist. **Class:** `practitioner-heuristic`. **Confidence:** high: Explicit publisher statement; individual recommendations need context.

**Sources and locators:** GDR-SRC-20261010-P01-03 — Introduction; explanation of guideline scope; Note on best-practice examples.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which guidelines are applicable and verified in an actual product?

### C-05

**Claim:** Offer usable sensory alternatives without claiming that information access, emotional equivalence and total game accessibility are the same outcome. **Class:** `inference`. **Confidence:** moderate: Guidance supports access; semantic and affective equivalence need separate evaluation.

**Sources and locators:** GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.; GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.; GDR-SRC-20261010-P01-20 — Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What facts or experiences differ for the selected channels?

### C-06

**Claim:** XAG 107 treats timing, complexity and duration as input demands beyond remapping. **Class:** `practitioner-heuristic`. **Confidence:** high: Source distinguishes these demands explicitly.

**Sources and locators:** GDR-SRC-20261010-P01-07 — Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which alternatives preserve the intended activity without a new physical barrier?

### C-07

**Claim:** A cognitive-access review should test understandable state, manageable interruption, recoverable action and discoverable help; diagnosis alone cannot choose a suitable interface. **Class:** `inference`. **Confidence:** moderate: Reasoned functional synthesis, not a clinical intervention or one cognitive profile.

**Sources and locators:** GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.; GDR-SRC-20261010-P01-09 — Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.; GDR-SRC-20261010-P01-10 — Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.; GDR-SRC-20261010-P01-18 — Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which supports reduce burden without removing wanted control or information?

### C-08

**Claim:** XAG 108 recommends adjustable difficulty and discrete mechanics/assists rather than treating every mode as the same difficulty option. **Class:** `practitioner-heuristic`. **Confidence:** high: Correct attribution; no universally optimal set or number follows.

**Sources and locators:** GDR-SRC-20261010-P01-08 — Implementation guidelines → changing difficulty without lost progress, regular saves, discrete mechanics and assists; distinction between modes and difficulty.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which demand is changed and what experience or competitive consequence follows?

### C-09

**Claim:** The Access Profiles paper reports exploratory player/developer findings, not proven cross-game personalization outcomes. **Class:** `empirical-evidence`. **Confidence:** moderate: Methods and limitations inspected; small convenience samples and a partial probe.

**Sources and locators:** GDR-SRC-20261010-P01-15 — §4.1 player study; §4.2 developer study; §4.3 analysis; §5.3.2 hesitations; §6.4 limitations; Copyright statement.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What generalizes to less experienced players, other access needs and larger productions?

### C-10

**Claim:** Player-controlled local overrides and transparent settings effects are preferable candidates to silent diagnosis-based personalization. **Class:** `inference`. **Confidence:** moderate: Autonomy and error-correction rationale; no implementation or privacy guarantee established.

**Sources and locators:** GDR-SRC-20261010-P01-15 — §4.1 player study; §4.2 developer study; §4.3 analysis; §5.3.2 hesitations; §6.4 limitations; Copyright statement.; GDR-SRC-20261010-P01-09 — Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What data are needed, and can the player understand and reverse each change?

### C-11

**Claim:** WAI recommends combining standards-based and user evaluation and attending to a range of users. **Class:** `practitioner-heuristic`. **Confidence:** high: Informative web-evaluation guidance; game transfer requires care.

**Sources and locators:** GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What combination of tasks, devices and relevant users is adequate for the intended claim?

### C-12

**Claim:** Use representative functional contexts and people who rely on the relevant accommodations; simulations and checklist passes do not establish population access. **Class:** `inference`. **Confidence:** moderate: Combines source limits with the distinction between feature presence and task performance.

**Sources and locators:** GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.; GDR-SRC-20261010-P01-07 — Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.; GDR-SRC-20261010-P01-20 — Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which populations and intersecting needs remain untested?

### C-13

**Claim:** XAG 118 calls for photosensitivity assessment and addressing problematic content, not reliance on a warning alone. **Class:** `practitioner-heuristic`. **Confidence:** high: Accurate guidance attribution; no clinical/safety certification is claimed.

**Sources and locators:** GDR-SRC-20261010-P01-19 — Goal; Overview; Implementation guidelines → evaluate all games and address problematic content.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What qualified technical review is required before any exposure testing?

### C-14

**Claim:** Plan access as maintained behavior across content, localization and settings, with honest limitations and non-stigmatizing choices. **Class:** `inference`. **Confidence:** moderate: Identifiable dependencies and ethical reasoning; no measured maintenance multiplier.

**Sources and locators:** GDR-SRC-20261010-P01-03 — Introduction; explanation of guideline scope; Note on best-practice examples.; GDR-SRC-20261010-P01-07 — Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.; GDR-SRC-20261010-P01-15 — §4.1 player study; §4.2 developer study; §4.3 analysis; §5.3.2 hesitations; §6.4 limitations; Copyright statement.; GDR-SRC-20261010-P01-20 — Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Can the planned feature remain usable across the supported release surface?

### C-15

**Claim:** The proposed barrier audit, illustrations and evaluation protocol may improve evidence about local access but are not executed or approved participant research. **Class:** `hypothesis`. **Confidence:** low: No recruitment, prototype, participant session, clinical test or quantified result occurred.

**Sources and locators:** GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What would a later approved evaluation reject, revise or narrow?

## References

All identities below are **temporary P01 source candidates**. Access date: **2026-10-10**. `relevant-excerpt` means the cited passages were inspected, not every linked resource. Repeated records enable standalone reading and are not independent corroboration. Cross-batch reconciliation by canonical URL/DOI/edition remains pending.

### GDR-SRC-20261010-P01-01

**World Wide Web Consortium (W3C).** [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). W3C. **Publication/update:** 2024-12-12. **Edition/version:** W3C Recommendation, WCAG 2.2, dated revision.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Normative accessibility specification (formal-standard within its scope). **Precise inspected locators:** Status of This Document; §§1.3.3, 1.4.1, 1.4.3, 1.4.10, 1.4.11; §§2.4.3, 2.4.7, 2.4.11–2.4.13; §§2.5.7–2.5.8; conformance scope.

**Inspected access route:** [public copy](https://www.w3.org/TR/WCAG22/). **Local claims:** C-02. **Limits:** Web-content criteria, not automatic native-game conformance, legal advice, or a complete audit. Exceptions and conformance level matter. No universal native display or controller size follows.

**Independence/derivation:** Source 02 interprets this family for non-web use; several XAG resource lists refer to WCAG. Those are not independent experiments. **Rights:** W3C document copyright/use terms apply; paraphrase only, no reproduced figures.

### GDR-SRC-20261010-P01-02

**W3C Accessibility Guidelines Working Group; editors Mary Jo Mueller, Phil Day, Daniel Montalvo.** [Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT)](https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/). W3C. **Publication/update:** 2025-12-11. **Edition/version:** W3C Group Note; WCAG2ICT for WCAG 2.2.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official informative guidance (practitioner-heuristic, not a normative requirement). **Precise inspected locators:** Abstract; Status of This Document; introductory scope and application to non-web documents/software.

**Inspected access route:** [public copy](https://www.w3.org/TR/wcag2ict-22/). **Local claims:** C-03. **Limits:** The Note explicitly sets no requirements. No complete native-game clause mapping or certification audit was performed.

**Independence/derivation:** Derivative interpretation of WCAG, not separate causal support. **Rights:** W3C document copyright/use terms apply; paraphrase only.

### GDR-SRC-20261010-P01-03

**Microsoft.** [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines). Microsoft Learn. **Publication/update:** Suite V3.2 published 2023-06-08; overview page updated 2026-08-14. **Edition/version:** V3.2 suite; live overview revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor guidance (practitioner-heuristic). **Precise inspected locators:** Introduction; explanation of guideline scope; Note on best-practice examples.

**Local claims:** C-04, C-14. **Limits:** Explicitly not a legal/compliance checklist. A showcased feature does not establish complete accessibility of its game.

**Independence/derivation:** Umbrella for all XAG records here; community/industry-informed but not twelve independent validation studies. **Rights:** Content reuse license not separately inspected; paraphrase only.

### GDR-SRC-20261010-P01-05

**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.

**Local claims:** C-05. **Limits:** Alternative channels are recommended; no task-time, comprehension-equivalence, or affect-equivalence experiment is supplied.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-06

**Microsoft.** [Xbox Accessibility Guideline 106: Screen narration](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.

**Local claims:** C-05, C-07. **Limits:** Semantics and usability must be verified in an actual build; this inspection proves no engine or screen-reader compatibility.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-07

**Microsoft.** [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Background and foundational information → speed, complexity, duration and remappable actions; Implementation guidelines → navigation, single presses, remapping and alternatives to holds/repeats/gestures.

**Local claims:** C-01, C-06, C-12, C-14. **Limits:** Remapping alone is not a remedy for all physical or timing demands. Embedded demonstrations were not independently played.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-08

**Microsoft.** [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → changing difficulty without lost progress, regular saves, discrete mechanics and assists; distinction between modes and difficulty.

**Local claims:** C-08. **Limits:** Recommendations are not a measured ranking of assist designs. Difficulty balancing and competitive policy need separate work.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-09

**Microsoft.** [Xbox Accessibility Guideline 112: UI navigation](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Overview; Implementation guidelines → accessible pathways from initial launch; logical and consistent navigation order.

**Local claims:** C-01, C-07, C-10. **Limits:** No comparative study establishes one universal settings-onboarding sequence. Linked game examples are vendor accounts.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-10

**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.

**Local claims:** C-07. **Limits:** Motion controls do not establish photosensitivity safety, camera comfort across platforms, or an appropriate numerical limit.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-11

**W3C Web Accessibility Initiative, Education and Outreach Working Group; editor Shawn Lawton Henry.** [Involving Users in Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/involving-users/). W3C WAI. **Publication/update:** First published 2005-11; content updated 2021-06-01; links updated 2024-04-30. **Edition/version:** Dated informative WAI web guidance.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official evaluation guidance (practitioner-heuristic). **Precise inspected locators:** Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Local claims:** C-01, C-11, C-12, C-15. **Limits:** Web evaluation guidance, not a game-specific sampling theorem. A few users cannot stand in for every disability, device, or language.

**Independence/derivation:** Same standards organization as sources 01–02, different informative purpose; not a new empirical dataset. **Rights:** W3C document copyright/use terms apply; paraphrase only.

### GDR-SRC-20261010-P01-15

**Lloyd May, Dan-Ha Le, Graham Lazorchak, Emily Q. Wang.** [Reimagining infrastructure for video game accessibility: exploring Access Profiles with players with disabilities and game designer-developers](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1823366/full). Frontiers. **Publication/update:** 2026-07-20. **Edition/version:** Frontiers in Computer Science 8:1823366; DOI 10.3389/fcomp.2026.1823366.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original qualitative research-through-design studies (empirical-evidence for reported participant findings). **Precise inspected locators:** §4.1 player study; §4.2 developer study; §4.3 analysis; §5.3.2 hesitations; §6.4 limitations; Copyright statement.

**Local claims:** C-09, C-10, C-14. **Limits:** Small, experienced, convenience-recruited groups; microgame probe and interviews, not a released cross-game infrastructure or controlled outcome benefit.

**Independence/derivation:** Player/developer groups form one paper and design inquiry, not independent causal replications; related standards and prior literature are acknowledged dependencies. **Rights:** CC BY stated in article; attribution retained; no participant quotations, images, or datasets reproduced.

### GDR-SRC-20261010-P01-18

**Microsoft.** [Xbox Accessibility Guideline 115: Error messages and destructive actions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/115). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Local claims:** C-07. **Limits:** No study here estimates error reduction, confirmation habituation or transaction risk. Security-related exceptions require separate assessment.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-19

**Microsoft.** [Xbox Accessibility Guideline 118: Photosensitivity](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/118). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Goal; Overview; Implementation guidelines → evaluate all games and address problematic content.

**Local claims:** C-13. **Limits:** Not clinical advice, a diagnostic tool, a safety certificate, or a universal safe-flash threshold. Linked testing tools were not used.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-20

**Microsoft.** [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.

**Local claims:** C-05, C-12, C-14. **Limits:** Caption availability does not demonstrate usable reading time, equal information in a particular event, or equivalent emotional experience.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

## Open questions and change history

**2026-10-10 — 0.1.0, initial draft.** Bounded P01 public-source research and author synthesis only. Source inspection does not establish production approval, participant validation or acceptance of a recommendation. The author’s challenge and actual document checks are recorded in the [batch review packet](../reviews/full-run-20261010-p01-review-packet.md). Independent review has not occurred. Formal reviewer and approval fields remain null.

Open questions include transfer across platforms, viewing/listening contexts, languages, input and assistive technologies; interactions between access needs; novice/expert differences; maintenance cost; and the comparative value of the proposed alternatives. Resolve source-reporting and dependency gaps before widening claims. No genre entry, canonical integration, permanent ID allocation, live host validation or release is asserted.
