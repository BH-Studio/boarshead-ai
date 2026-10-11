---
id: GDR-CAND-20261010-P01-PAT-01
kind: pattern
title: Redundant critical-state cues
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
- accessible state cues
- critical cue alternatives
tags:
- critical-state
- redundant-cues
- semantic-consistency
- accessibility
- attention
related_topics:
- GDR-CAND-20261010-P01-TOP-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns: []
related_genres: []
source_ids:
- GDR-SRC-20261010-P01-05
- GDR-SRC-20261010-P01-06
- GDR-SRC-20261010-P01-10
- GDR-SRC-20261010-P01-11
- GDR-SRC-20261010-P01-18
- GDR-SRC-20261010-P01-20
reviewer: null
approved_by: null
approved_date: null
---

# Redundant critical-state cues

**Draft, inference-led pattern candidate — not a validated recipe or released reference.** The proposal is to preserve a required task fact through usable representations when one presentation channel is unavailable or unreliable. It is **not** “more signals always work better,” and it does not establish equal emotion across modalities. [C-01, C-04, C-06]

## Purpose

Help a player determine a consequential current state and their available response without depending on one inaccessible cue. Examples include an unavailable route, completion of a required operation, or a state that invalidates an action the player is about to take. The pattern concerns semantic access to declared task facts, not decorative repetition or mandatory audiovisual intensity. [C-01]

## Context and prerequisites

Use only when the team can describe the underlying state, what the player is entitled to know, the decision it informs and the consequence of missing it. At least one additional representation must be feasible and usable in the target context. The state’s owner must be able to account for changes, corrections, resolution and any necessary persistence. Those are proposed design prerequisites, not a claim that every game needs this pattern. [C-01, C-02]

Before application, record the platform/display/viewing context, available listening and haptic output, preferred input, relevant access needs, language, task load, current settings and existing conventions. A color and a shape are different visual encodings, but neither supplies nonvisual information. Haptics may be unavailable or disabled. Do not assume that adding an output establishes a usable route for combined sensory needs. [C-03]

**Initial exit:** If the required fact is not defined, contradictory, or illegitimate knowledge for the player, repair the information contract first. If an already usable, simpler representation satisfies the need, do not add redundant output merely to use the pattern. [C-07]

## Mechanism and evidence

| Proposed causal link | Support | Limit / possible falsification |
| --- | --- | --- |
| A defined state can be represented consistently. | An inference from semantic information and error/recovery requirements. | A shared description alone does not prevent stale or contradictory outputs. |
| A non-color distinction and suitable alternative channel remove a specific single-channel dependency. | XAG 103/104 guidance; concrete information reasoning. | The alternative may carry too little detail, require another unavailable sense, or arrive too late. |
| The player detects and interprets the alternative. | Intended outcome; not directly tested by this pattern’s corpus. | Symbol unfamiliarity, reading burden, noise, speech overlap or device context can defeat it. |
| The player acts correctly with acceptable effort. | Hypothesis requiring task evaluation. | More output can distract, reveal unintended information or slow a task. |
| The experience remains desirable. | Separate hypothesis, not a consequence of preserved facts. | Access and comfort can improve while the desired emotional interpretation changes, or vice versa. |

The original sources justify considering accessible channels and coherent information. They do not experimentally validate this complete recipe, any universal response-time benefit or an optimal number of cues. The full-chain efficacy claim remains low confidence. [C-01–C-06]

## Recipe

All steps are **proposed application guidance**. No prototype, state system, audio asset, caption implementation or participant test was made in this batch. [C-06]

### 1. Specify the fact and uncertainty

Write the event or state, relevance, allowed interpretation, available response and what remains unknown. Distinguish “an unexplained impact occurred nearby” from “a particular attacker is behind the door.” The latter is inappropriate when the original information does not identify a cause. [C-02, C-04]

**Exit:** If the design cannot say what is required knowledge versus intended uncertainty, return to the owning interface/system decision. Do not let alternative wording silently decide it.

### 2. Separate current state from notification

Describe when the state begins, changes and resolves. Decide whether the player needs a persistent indicator, an attention event, a history record, or some combination. Dismissing a notification must not silently mean the underlying condition has ended. [C-02, C-05]

**Branch:** If the state is still necessary after an announcement disappears, retain an inspectable current-state route. If it is no longer relevant, avoid continuing to announce it as current. This is a semantic policy, not an engine architecture.

### 3. Choose the smallest useful set of representations

For a visual representation, give essential distinctions a usable non-color meaning where appropriate. Add an alternative sensory representation suited to the required facts and the player’s available channels. A brief tone might attract attention without specifying direction or action; it is not automatically sufficient. [C-01, C-03]

**Branch:** Prefer an existing known cue or readable state representation when sufficient. Use explicit wording when a new symbol would require unsupported interpretation. Do not make a shape, a caption and a vibration compulsory for every decorative event.

### 4. Match semantic content, not sensory appearance

Check each representation against the same required facts and uncertainty. Decide how direction is described and whether its reference is screen-relative, player-relative or world-relative; preserve the meaning when the view changes. Match meaningful state and timing, not waveform, pixel or vibration identity. [C-02, C-04]

**Exit:** If an alternative cannot communicate a necessary distinction without unacceptable disclosure or ambiguity, revise the event or task contract. Do not claim equivalent information merely because both modes contain an alert.

### 5. Constrain interruption and competing output

Choose which changes warrant attention, which may be grouped and which must remain independently inspectable. Plan the relationship to current narration, dialogue, captions and an active task. Prioritize by declared consequence rather than an arbitrary bright color or loud sound. [C-05]

**Branch:** If repeated output obscures a more important fact, reduce or defer nonessential announcements while preserving the required state. A queued warning that arrives after the decision is not a successful alternative.

### 6. Respect settings and recovery

Describe the effect of disabling, lowering or changing a channel. Make supported alternatives reachable before the barrier they address. Test resolution, cancellation, loading/return, corrections and repeated exposure. Clarify which representation is authoritative when a presentation error is discovered; no contradictory output should be treated as harmless redundancy. [C-02, C-05, C-06]

**Exit:** If the supported configuration loses a required fact or an essential state cannot be maintained honestly, block the claimed access route and revise or explicitly narrow scope. Do not force intensity upward as the default remedy.

### 7. Compare before retaining the extra complexity

After separate authorization, compare the proposed representation set with the existing route and a simpler usable alternative. Check information, actual use, load and comfort separately. Keep only the coverage and benefit supported by the results. [C-06, C-08]

### Adjustable variables

| Variable | Design choice to record | Constraint |
| --- | --- | --- |
| Semantic precision | Exact value, category, direction, approximate location or event awareness. | Do not reveal unsupported certainty or omit required precision. |
| Persistence | Current state, event-only notice, replay/history or inspect-on-demand. | Duration follows the decision; no universal seconds value is supported. |
| Priority and repetition | Interrupt, queue, coalesce, update or suppress nonessential repeats. | Essential facts must remain usable at the decision point. |
| Visual encoding | Label, symbol, shape, outline, placement or backing. | Non-color information remains necessary where hue alone would carry meaning. |
| Alternative channels | Narration, caption, sound, haptic or another appropriate route. | Channel presence does not prove comprehension or combined-needs coverage. |
| Player control | Enabled categories, verbosity, intensity, location and access route. | Changing settings must not silently invalidate the declared support claim. |
| Familiarity | Existing convention, learnable new cue or explicit explanation. | Recognition must be checked, not inferred from repeated exposure alone. |

The variables are proposed authoring decisions, not universal parameter settings. [C-02–C-06]

## Worked examples

### Illustrative example: a temporarily unavailable route

**Synthetic — not a game observation or test result.** A player is selecting a service route. The system knows that Route B is unavailable because a valve is closed, and the player is entitled to that reason. Their available responses are to choose Route A or inspect the valve task. [C-06]

The design contract is “Route B unavailable; valve closed; Route A remains selectable.” A visual route row carries the route name, state word and distinct state mark. Focus remains separate from availability. A meaningful narration route can identify that same state and the available actions when the route is focused. A change announcement may draw attention when availability changes, but persistent state is still available on inspection. [C-01–C-05]

If the valve opens while another menu is active, the current-state representations update and a relevant change can be announced without claiming that the player has selected Route B. When a stale queued message would contradict the new state, the delivery policy must cancel or correct it. The exact behavior requires later design and testing; no queue was implemented here. [C-02, C-05]

**Simpler comparison:** an accessible, persistent route list with no separate change announcement. It may be enough when the player is already inspecting routes. The pattern must earn any extra interruption by supporting a real decision, not by showing that another sound can be played. [C-06, C-07]

### Illustrative example: uncertain environmental event

A distant impact matters because the player may investigate, but its cause is unknown. A caption can describe the impact and relevant direction without naming an unseen source. An alternative that announces an enemy identity changes the information rather than merely providing access. If the event is entirely decorative and does not matter to the declared task, a persistent critical warning is not justified. [C-04, C-07]

This example does not promote the prior audio pilot’s contextual-tension hypothesis. The intended emotional effect and audio evidence remain outside this pattern’s claim. Preserving facts does not prove preserving suspense.

## Tradeoffs and alternatives

The possible benefit is availability of required information through supported routes. Costs include additional content, translation, state-change handling, interruption policies and regression combinations. Those are identified work categories, not a staffing or budget estimate. [C-02, C-05, C-06]

Alternatives include one simpler usable signal; a persistent inspectable state without an announcement; removing an unnecessary time pressure; revising a confusing underlying interaction; or omitting an irrelevant event. A single representation can be sufficient for a particular supported context; the pattern does not require simultaneous use of every available channel. [C-01, C-07]

## Failure cases

| Warning sign in a later evaluation | Explanation to investigate | Proposed response |
| --- | --- | --- |
| Player notices a cue but cannot identify the required action. | Attention event lacks semantic content. | Add the missing meaning or choose a more explicit representation. |
| Color and symbol appear different, but nonvisual access fails. | Both encodings require sight. | Provide an appropriate nonvisual route or narrow the support claim. |
| Caption/narration reveals a hidden cause. | Alternative carries more knowledge than the contract permits. | Revise wording or the intended uncertainty. |
| State and announcement disagree. | Stale update, queued event or correction failure. | Repair state/delivery handling before claiming access. |
| Repeated speech obscures current dialogue or a decision. | Unbounded redundancy or poor priority. | Reduce nonessential output; preserve the essential fact elsewhere. |
| The route works only at default settings. | Preferred configuration removes the only usable fact. | Repair the supported configuration or state its limitation honestly. |
| Extra cues add effort with no useful task benefit. | Complexity solves no demonstrated problem. | Prefer the simpler alternative. |

These are proposed failure observations, not results obtained in P01. [C-02–C-08]

## Counterexamples and do not use conditions

**Strongest opposing case:** the current route already communicates the required fact and the user is concentrating on another sensory task. Adding an announcement can increase burden without adding access. The evidence does not establish that redundancy wins that comparison. [C-05–C-07]

Do not use this pattern to turn every decorative event into an alert, manufacture certainty, bypass a missing task definition, conceal stale information or claim universal access from a pair of channels. Do not retain it when supported preferences make required facts unavailable. Where different modalities cannot preserve the desired experience, describe the difference and decide deliberately; do not claim equivalence. [C-04, C-07]

## Playtest

**PROPOSED — NOT PERFORMED.** This is one future test proposal, not an executed extension of the audio pilot. [C-08]

**Compare** the existing presentation, the proposed redundant set and a simpler usable alternative. Keep underlying state, player entitlement, actions and consequences identical where possible. Where the design intentionally changes information or response timing, label that as a separate factor rather than crediting redundancy alone.

**Participants and conditions:** include people who rely on the intended alternatives, first-use and practiced users, relevant languages and actual preferred devices/settings. Examine ordinary and realistically competing task loads. Do not force an inaccessible or distressing baseline; missing channels can first be checked technically. A hearing reviewer’s muted run or a visual filter is a failure-discovery aid, not a representative participant substitute.

**Procedure:** identify required facts before the session; exercise state onset, repeated updates, correction and resolution; include at least one return or interrupted task; ask for interpretation and available actions; measure actual response and recovery. Select participant numbers and any quantitative acceptance margins from the decision and variance before a separately authorized study. No numerical threshold is asserted here.

**Measures and confounds:** required-fact accuracy, mistaken certainty, contradictory state reports, usable timing, task correctness, interruption cost, comfort and requested settings changes. Record prior cue familiarity, reading/narration speed, task learning, display/listening context and prototype defects.

**Falsify or narrow:** reject an information-equivalence claim when a route changes necessary knowledge or delivers it too late. A critical supported-route failure blocks advancement under this proposed rule. Reject a general benefit claim when it appears only under one favorable setting; narrow to that setting when defensible. Prefer the simpler candidate when the extra output adds no meaningful value or creates unacceptable burden. A small inconclusive comparison does not prove equality. Stop on request or discomfort.

## Related entries and history

The owning topic connections are [Visual communication](../topics/visual-communication.md), [Interface and information](../topics/interface-and-information.md), and [Accessibility and inclusive interaction](../topics/accessibility-and-inclusive-interaction.md). They reuse the same evidence and are not corroborating studies. No genre relationship is asserted. The [review packet](../reviews/full-run-20261010-p01-review-packet.md) owns P01-local contradictions and the independent-review/host-validation gaps.

## Claim ledger

Claim class and confidence are separate. Confidence describes the exact, limited proposition, not the effectiveness of a whole design. Proposed illustrations, recipes and participant protocols are not observations.

### C-01

**Claim:** Redundant critical-state cues are a conditional way to preserve required task facts when a chosen channel is unavailable or unreliable. **Class:** `inference`. **Confidence:** moderate: Supported as access-oriented design guidance, not validated as a complete pattern.

**Sources and locators:** GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.; GDR-SRC-20261010-P01-20 — Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Does the alternative actually carry the facts needed for this decision?

### C-02

**Claim:** A shared semantic state can reduce the risk of contradictory representations, but it does not itself guarantee consistent or timely delivery. **Class:** `inference`. **Confidence:** moderate: Logical design dependency; no engine or latency validation.

**Sources and locators:** GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.; GDR-SRC-20261010-P01-18 — Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Do update, cancellation and correction paths stay synchronized?

### C-03

**Claim:** XAG 103 recommends complementary ways to convey key information and cautions against reliance on color or haptics alone. **Class:** `practitioner-heuristic`. **Confidence:** high: Accurate scope-limited source statement.

**Sources and locators:** GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which channels are genuinely usable in the intended context?

### C-04

**Claim:** Match uncertainty and actionable content across representations without asserting equal emotion or identical sensory experience. **Class:** `inference`. **Confidence:** moderate: Semantic access requirement, not an affect-equivalence finding.

**Sources and locators:** GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.; GDR-SRC-20261010-P01-20 — Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Does a text label reveal knowledge absent from the original cue?

### C-05

**Claim:** Priority, persistence and player control should constrain redundancy so that nonessential output does not overwhelm essential information. **Class:** `inference`. **Confidence:** moderate: Guidance informs an unvalidated arbitration policy; more signals need not be better.

**Sources and locators:** GDR-SRC-20261010-P01-06 — Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.; GDR-SRC-20261010-P01-10 — Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which combinations mask, interrupt or exhaust the user?

### C-06

**Claim:** This recipe, adjustable variables, examples and proposed comparisons may improve access to critical state without unacceptable burden. **Class:** `hypothesis`. **Confidence:** low: No full-chain comparative experiment or local test has been performed.

**Sources and locators:** GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.; GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Would equivalent or better results arise from one simpler usable signal?

### C-07

**Claim:** Do not apply the pattern to every decorative event or invent certainty; replace it when its prerequisites or access contract fail. **Class:** `inference`. **Confidence:** moderate: Boundary follows the stated purpose and information constraints.

**Sources and locators:** GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.; GDR-SRC-20261010-P01-20 — Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.; GDR-SRC-20261010-P01-10 — Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What is the least intrusive sufficient representation?

### C-08

**Claim:** Proposed channel-loss and realistic-load tests can falsify claims about information access, consistency and added value. **Class:** `hypothesis`. **Confidence:** low: A prospective test design, not evidence that the pattern works.

**Sources and locators:** GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Can failures be identified without confusing absence of significance with equivalence?

## References

All identities below are **temporary P01 source candidates**. Access date: **2026-10-10**. `relevant-excerpt` means the cited passages were inspected, not every linked resource. Repeated records enable standalone reading and are not independent corroboration. Cross-batch reconciliation by canonical URL/DOI/edition remains pending.

### GDR-SRC-20261010-P01-05

**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.

**Local claims:** C-01, C-03, C-04, C-06, C-07. **Limits:** Alternative channels are recommended; no task-time, comprehension-equivalence, or affect-equivalence experiment is supplied.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-06

**Microsoft.** [Xbox Accessibility Guideline 106: Screen narration](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → UI text, interactive components, contextual information, meaningful graphical information and decorative graphics.

**Local claims:** C-02, C-05. **Limits:** Semantics and usability must be verified in an actual build; this inspection proves no engine or screen-reader compatibility.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-10

**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.

**Local claims:** C-05, C-07. **Limits:** Motion controls do not establish photosensitivity safety, camera comfort across platforms, or an appropriate numerical limit.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-11

**W3C Web Accessibility Initiative, Education and Outreach Working Group; editor Shawn Lawton Henry.** [Involving Users in Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/involving-users/). W3C WAI. **Publication/update:** First published 2005-11; content updated 2021-06-01; links updated 2024-04-30. **Edition/version:** Dated informative WAI web guidance.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official evaluation guidance (practitioner-heuristic). **Precise inspected locators:** Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Local claims:** C-06, C-08. **Limits:** Web evaluation guidance, not a game-specific sampling theorem. A few users cannot stand in for every disability, device, or language.

**Independence/derivation:** Same standards organization as sources 01–02, different informative purpose; not a new empirical dataset. **Rights:** W3C document copyright/use terms apply; paraphrase only.

### GDR-SRC-20261010-P01-18

**Microsoft.** [Xbox Accessibility Guideline 115: Error messages and destructive actions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/115). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Goal; Implementation guidelines → identifying errors and recovery; reviewing, correcting or reversing stored-data actions; alternatives to prolonged confirmation holds.

**Local claims:** C-02. **Limits:** No study here estimates error reduction, confirmation habituation or transaction risk. Security-related exceptions require separate assessment.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-20

**Microsoft.** [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Goal and Overview; Implementation guidelines → captions for important non-speech sounds and direction, pre-play availability, configurable categories, preview and localization.

**Local claims:** C-01, C-04, C-07. **Limits:** Caption availability does not demonstrate usable reading time, equal information in a particular event, or equivalent emotional experience.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

## Open questions and change history

**2026-10-10 — 0.1.0, initial draft.** Bounded P01 public-source research and author synthesis only. Source inspection does not establish production approval, participant validation or acceptance of a recommendation. The author’s challenge and actual document checks are recorded in the [batch review packet](../reviews/full-run-20261010-p01-review-packet.md). Independent review has not occurred. Formal reviewer and approval fields remain null.

Open questions include transfer across platforms, viewing/listening contexts, languages, input and assistive technologies; interactions between access needs; novice/expert differences; maintenance cost; and the comparative value of the proposed alternatives. Resolve source-reporting and dependency gaps before widening claims. No genre entry, canonical integration, permanent ID allocation, live host validation or release is asserted.
