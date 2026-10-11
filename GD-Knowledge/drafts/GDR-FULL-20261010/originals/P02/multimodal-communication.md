---
id: GDR-CAND-20261010-P02-TOP-03
kind: topic
title: Multimodal communication
version: 0.1.0
candidate_revision: initial-draft-1
status: draft
run_id: GDR-FULL-20261010
batch_key: P02
attempt_id: P02-authoring-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- redundant cues
- caption alternatives
- cross-channel information
- competing attention
tags:
- multimodal
- captions
- subtitles
- narration
- haptics
- attention
- accessibility
- localization
related_topics:
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
related_patterns:
- GDR-CAND-20261010-P02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P02-004
- GDR-SRC-20261010-P02-005
- GDR-SRC-20261010-P02-006
- GDR-SRC-20261010-P02-007
- GDR-SRC-20261010-P02-008
- GDR-SRC-20261010-P02-009
- GDR-SRC-20261010-P02-010
- GDR-SRC-20261010-P02-013
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded P02 draft; no predecessor P02 artifact found in the
  inspected Project snapshot.
byte_hash_record: ../reviews/full-run-20261010-p02-review-packet.md#candidate-byte-receipt
---

# Multimodal communication

**Draft research candidate — not released guidance, implementation approval or a validated recipe.** This is P02 only. The current dispatch authorizes this research; the parent’s first-wave review receipt is retained without importing unseen corrected content. Its later reconciliation supersedes the dispatch’s earlier “P01 unreviewed” sentence. P01 is parent-reported reviewed, not released; its bytes remain a missing dependency here.

**Evidence boundary:** inspected public documents and the supplied Project snapshot; no project/engine code, game build, participant study or host-retrieval test was run. Definitions and synthetic scenarios are proposed analytic tools, not formal standards. [C-12]

## Decision and scope

**Decision:** Which facts must a player obtain, through which usable channels and at what point in the task, when hearing, vision, haptics or attention cannot be assumed? Choose accessible alternatives and purposeful combinations rather than maximizing the number of simultaneous signals. **Access to the same decision facts is not a claim of equal emotional experience.** [C-01, C-07–C-10]

This topic owns cross-channel information meaning, captions/narration as communication routes, and conflicts among competing messages. It does not provide a complete localization system, subtitle rendering standard, medical sensory-safety protocol or platform certification checklist. Current primary guidance was inspected directly; parent-reviewed P01 numerical accessibility content was not available and is not reconstructed. [C-02–C-04, C-11, C-12]

### Working distinctions

| Term | Proposed use in this entry | Important boundary |
| --- | --- | --- |
| Modality | A sensory route, such as visual, auditory or tactile presentation. | Text and a colored icon on one display are both visual. |
| Redundant cue | Another representation of substantially the same decision-relevant fact. | An extra effect with no interpretable fact is ornament, not necessarily useful redundancy. |
| Complementary cue | A representation carrying different facts that must be combined. | Losing one channel can remove a required part of the decision. |
| Subtitle | Representation of speech in text, following the terminology in source 006. | Does not automatically include important non-speech information. |
| Caption | Text conveying relevant speech and non-speech sound information. | Cannot be presumed to recreate every spatial or affective property of sound. |
| Narration | Spoken interface/state information, including screen-reader-style access. | Another audio stream can compete with speech, music and voice chat. |
| Information contract | A proposed record of the event, required facts, certainty, timing, actions and permitted ambiguity. | A design specification to evaluate, not a universal formal standard. |

These distinctions organize the source guidance and the proposed tests. The number of channels is not a measure of accessibility or quality. [C-03, C-07, C-10, C-11]

### Context to declare

Record viewing and listening environment, display/window scale, available input, haptic device/contact, chosen captions/narration, language and reading direction, task deadlines, ability to pause, and concurrent information streams. Include actual users of the intended access routes. A sound-off check by a hearing author verifies only some missing-information cases, not usability for people who rely on captions; a narration script is not proof that navigation is usable without vision. Deafblind access, sign-language content and specialist tactile/Braille interfaces are unresearched dependencies here, not silently covered by “multimodal.” [C-07–C-11]

## Core explanation and mechanisms

### Specify facts before choosing channels

Microsoft’s XAG 103 and 110 recommend alternatives to critical information conveyed in a single sensory route, including haptics that may be unavailable or disabled. The application proposed here is to identify the necessary fact first, then author a usable alternative without changing what is known. The benefit is **hypothesized access to the decision**, not a guaranteed identical response or emotion. [C-01, C-07, C-09]

A useful contract might distinguish “an event occurred behind the player” from “a particular hidden agent caused it.” A caption, vibration or speech cue should not silently assert the second fact when the original cue disclosed only the first. Conversely, withholding a required direction to preserve ambiguity would leave some players unable to make the intended choice. This is a design tradeoff about legitimate uncertainty, not a universal requirement to name all causes. [C-07, C-10]

**Proposed causal chain:** required facts are identified → alternative representations preserve their meaning and availability → the player detects and interprets at least one usable route → the player can make the intended decision. Official guidance directly supports designing alternative routes. The end-to-end usability, attentional and emotional links remain application-specific hypotheses. A cue can be present, legible and still misunderstood or too late. [C-01, C-07–C-09]

### Redundancy is not proof of benefit

The inspected Moon et al. study supplies an adjacent laboratory question about paired force-feedback and visual memory under interruption, not a game-caption experiment. Its authors report an accuracy interaction but no corresponding reaction-time interaction. **Its displayed Table 1 interruption labels conflict with the surrounding interpretation.** The draft therefore withholds the condition-specific magnitude and does not use this source to establish a general redundancy benefit. The discrepancy and study population/device are retained in C-05/C-06, not repaired by guesswork. [C-05, C-06]

More fundamentally, repetition can mean different things. A second channel may offer a usable alternative when the first is unavailable. Repeating a full message in every route at once can also occupy the very attention needed for the task. Offering selectable alternatives, brief state changes and on-demand detail is not the same as automatically playing all available content. Guidance about audio-category controls and interruptible narration supports this design distinction; the best scheduling policy is not established by that guidance. [C-04, C-08]

### Captions and narration have different costs

A caption may compete with visual inspection or aiming, while narration may compete with dialogue, environmental audio or communication. Simply copying the same text into both routes does not solve timing, terminology, speaker identity or the player's current focus. The proposed response is to preserve the decision facts while permitting concise forms, meaningful priority and access to detail, rather than treating literal duplication as the target. [C-03, C-04, C-08, C-10]

Where audio is downmixed to mono, the existence of the sound does not by itself preserve a direction formerly carried by spatial separation. Where haptics provide only a general pulse, direction or event identity must not be assumed unless the player can interpret the intended mapping on the actual hardware. These are limits on inference, not a claim that mono or haptics are ineffective. [C-01, C-04, C-07, C-10]

## Design choices and alternatives

| Choice | Appropriate condition | Tradeoff, alternative and exit |
| --- | --- | --- |
| Caption an important non-speech event | The sound communicates a relevant fact not otherwise available visually. | Author meaning, speaker/source uncertainty and direction; avoid adding privileged knowledge. Another usable visual representation may already cover the fact. |
| Subtitle speech | Speech conveys content the player needs or elects to follow. | Text presentation, speaker attribution and localization need evaluation. Do not assume dialogue-only text covers alarms or off-screen events. |
| Screen narration | Relevant interface/state information needs a nonvisual route. | Stale or repetitive speech can compete with current information. Offer usable focus, repeat/cancel and detail controls rather than one uninterrupted recital. |
| Additional haptic signal | It communicates a learnable event distinction on supported hardware. | Optional/unavailable haptics cannot be the sole required route. Avoid pretending a generic pulse carries detailed language. |
| Persistent or on-demand detail | The information remains relevant and immediate delivery would interrupt another task. | A log is not a replacement for an alert that must be acted on before a deadline. |
| Less automatic presentation | Decorative messages or repeated status dominate attention. | Do not silently suppress required information. Preserve availability, prioritization and explicit settings. |

The choices above are conditional applications of guidance and proposed hypotheses; no channel combination is universally optimal. [C-01, C-03, C-04, C-07–C-11]

### Formal standard versus recommendation

In the **dated W3C WCAG 2.2 Recommendation**, SC 1.2.2 (Level A) addresses captions for prerecorded audio in synchronized media, except clearly marked media alternatives for text. SC 1.3.3 (Level A) prevents instructions from relying solely on sensory characteristics such as sound, shape or location. These are web-content criteria with defined applicability, not general native-game or console certification requirements. Real-time gameplay-event captioning in this entry is supported by vendor guidance and design inference, not by pretending the prerecorded-media clause covers every game event. [C-02]

XAGs 103, 104, 105, 106 and 110 are treated here as **official practitioner guidance**. They are not participant evidence or a formal standard simply because the issuer is a platform vendor. No universal font size, reading speed, caption duration, simultaneous-cue count or safe vibration value is imported. [C-01–C-04, C-11]

## Application process

1. **Define the minimum facts.** For each important event, write what happened, whose/source identity is actually known, relevant location, urgency, available actions, certainty and expiry. Identify what may remain unknown. [C-07]
2. **Map facts to routes.** Determine which facts each proposed visual, audio, text/narrated and tactile representation carries. Mark complementary facts that would disappear when a channel is unavailable; do not count two visual signifiers as a second sensory route. [C-01, C-07, C-10]
3. **Author meaningful alternatives.** Choose captions, state labels, narration, spatial indicators or haptic signals appropriate to the fact. Ensure every label describes the current state without an unintended spoiler or unsupported causal attribution. [C-03, C-07]
4. **Resolve attention conflicts.** Identify deadlines and obsolescence. Keep urgent actionable information usable; defer or reduce decorative/repeated detail. Allow chosen categories and repeat/detail controls. Do not bury an urgent cue in a history-only fallback. [C-04, C-08]
5. **Check configuration and localization.** Evaluate sound off, mono, haptics off, reduced effects, narration use and realistically supported combinations. Check actual translated text and speaker/direction references; do not infer reading time from English character count alone. [C-03, C-07, C-11]
6. **Prototype and evaluate only when authorized.** Test required-fact comprehension, decision timing, workload/comfort and unintended disclosure separately. Revise the event or interaction itself when no feasible alternative can communicate the necessary facts in time. [C-07–C-12]

## Patterns and genre adaptations

[Fact-preserving cue alternatives](../patterns/fact-preserving-cue-alternatives.md) — `GDR-CAND-20261010-P02-PAT-02` — owns the detailed conditional recipe. [Controls and input](controls-and-input.md) owns usable access to settings and response actions; [Feedback and game feel](feedback-and-game-feel.md) owns outcome semantics and optional impact.

Attention-aware notification scheduling is queued as additional child work, not a third pattern artifact. More empirical interruption research and reviewed interface/action-staging dependencies are required before specifying an authoritative priority system.

No genre files are created. **Illustrative contextual contrast:** investigation may preserve uncertainty about a source; a time-limited required response may need explicit direction; dialogue may permit pausing or replay while concurrent action may not. A hybrid must expose the conflict and select a scene/task contract, not rank genres as universal authorities. [C-11]

## Examples and counterexamples

### Illustrative worked example — a changed route condition

A player is examining an object when a nearby passage becomes unavailable. The required facts are that the route changed, which passage is affected and which alternative action remains available. The exact cause is not yet known. An audio-only design that encodes location through stereo placement risks losing a fact in silent or mono use. [C-04, C-07, C-11]

The candidate adds a configurable caption describing the audible change without naming an unseen actor, a legible passage-state indication and narration that can convey the route's changed state when needed. A haptic event may attract attention, but it does not alone identify the passage. The caption's direction uses a specified reference frame; changing camera orientation cannot silently reverse its intended meaning. Optional background commentary is deferred while the actionable event is presented. [C-03, C-07, C-08, C-10, C-11]

**Alternative:** if the passage change has no immediate relevance, keep a discoverable state update and on-demand history rather than interrupting inspection. If it demands immediate action, a history-only record is insufficient. Both alternatives need evaluation; none was built, heard, seen by participants or tested. [C-08, C-11]

### Strong counterexample — all channels active, no usable attention route

Dialogue, narration, several captions, a flashing decoration and repeated vibration announce every minor event during a precision task. Required facts may technically exist yet remain unusable. First distinguish essential from decorative content and offer the player's chosen channels; reduce or defer nonessential repetition. Do not respond by removing captions while leaving decorative effects intact. This is an illustrative failure hypothesis, not a measured universal overload threshold. [C-08, C-11]

### Counterexample to literal equivalence

A caption that names an unseen cause can give more decision information than an ambiguous sound; a generic rumble can give less. Matching asset count or onset does not establish semantic parity. Conversely, preserving facts can change suspense, surprise or ease of interpretation. Emotional equivalence remains unproven, and an access improvement need not recreate the same emotional profile to be useful. [C-07, C-09, C-10]

## Failure modes and constraints

| Warning sign in later evaluation | Question to investigate | Proposed correction |
| --- | --- | --- |
| One channel disabled, task impossible | Was a required fact only present there? | Add a usable alternative or change the task; do not call the channel optional. |
| Event is noticed but cannot be identified | Is the alternative merely an attention pulse? | Encode the necessary distinction or provide timely detail. |
| Captions imply knowledge not otherwise available | Was creator knowledge substituted for perceivable evidence? | Match semantic certainty or explicitly approve the changed information contract. |
| Narration describes an obsolete focus | Does the speech queue retain stale information? | Interrupt obsolete content and preserve replay/detail of relevant state. |
| Translation covers required visual evidence | Has actual language expansion/layout been evaluated? | Recompose, prioritize or change interaction pacing; not a universal smaller-font fix. |
| Participants can recite facts but miss the action deadline | Was availability mistaken for usable timing? | Reduce competing content or adjust the interaction, then retest. |

The proposed fixes are hypotheses/inferences, not tested results. Hardware and language combinations add content, state synchronization, settings, regression and access-review work. Long-session fatigue, literacy, multilingual overlap, live speech-to-text accuracy and specialist sensory access require further evidence. Do not record private voice/chat content for evaluation without a justified and approved data plan. [C-07–C-11]

## Playtest and validation

**PROPOSED — NOT RUN.** No media assets, device implementation, translated build, participant comparison or accessibility certification was performed. [C-11, C-12]

**Question:** Does each supported access configuration provide the necessary facts in time for the intended decision without excessive competing presentation or unintended disclosure?

**Comparisons:** select an already usable baseline route, a candidate alternative route and a chosen combination. Test the same underlying event facts and action opportunities. Do not force participants to use a known inaccessible route to create an experimental control. To test redundancy rather than availability, compare one usable route with two usable routes for that participant, holding the facts and urgency constant.

**Procedure:** obtain informed consent, record actual access practices/devices/languages and permit chosen settings. Use matched event sets, counterbalance order when practical and separate first-use interpretation from learned cue use. Include meaningful concurrent tasks and a recovery situation; the Moon study is not evidence that its needle-interruption task transfers to games. Ask what happened, what was known versus inferred, where/when a response was needed and what actions were available.

**Measures:** required-fact accuracy; inappropriate action caused by missing/misleading information; missed deadlines; requests to repeat; successful navigation to detail; competing-message errors; comfort, effort and intended emotional response as separate reports. Report the source of uncertainty and the affected access configuration, not only an overall mean.

**Falsification and stop rules:** a critical fact unavailable or materially misleading in a claimed supported configuration blocks advancement. Missing an action deadline because the alternative is too late requires revision even if recall is good afterward. Reject an automatic extra channel when it adds errors/discomfort without useful detection or interpretation value; retain it as selectable only when the evidence and user preference support that narrower use. Equal average scores or non-significance do not prove semantic or emotional equivalence. Stop on request; do not classify distress/access failure as an inconvenient outlier.

**Sampling:** formative sessions must cover the actual claimed access routes with people who use them, and the actual language/layout cases selected for the application. Such coverage is not population representation. A confirmatory equivalence study requires independently justified margins, sample size and analysis before data collection; none is set or executed here. All procedure and decision proposals remain hypotheses. [C-11]

## Claim ledger

Claim IDs are local to this entry. Confidence concerns the stated scope, not source prestige. An inference is not a validated outcome; repeated references are not independent corroboration.

### C-01

**Claim:** Microsoft recommends additional routes for critical visual/audio information and alternatives to haptic-only critical information.
**Class:** `practitioner-heuristic`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005, Goal/Implementation guidelines; GDR-SRC-20261010-P02-008, Implementation guidelines.
**Applicability and contrary limits:** Official vendor guidance. Does not require every possible channel at maximum intensity or prove that a chosen combination is usable.
**Confidence:** High for attribution; usability depends on implementation and audience.
**Unresolved:** Which alternative is actually usable for each supported access configuration?

### C-02

**Claim:** WCAG 2.2 specifies prerecorded-media captions and non-sensory-only instructions within its web-content scope.
**Class:** `formal-standard`. **Evidence and exact locator:** GDR-SRC-20261010-P02-004, dated Recommendation 2024-12-12, SC 1.2.2 and 1.3.3, Level A.
**Applicability and contrary limits:** SC 1.2.2 has the clearly marked media-alternative-for-text exception. Neither clause establishes blanket native-game caption certification.
**Confidence:** High for the scoped normative statement; product applicability not assessed.
**Unresolved:** What is the actual conformance scope of a future web-based component?

### C-03

**Claim:** XAG guidance distinguishes speech subtitles, important non-speech captions and screen narration of relevant interface/state information.
**Class:** `practitioner-heuristic`. **Evidence and exact locator:** GDR-SRC-20261010-P02-006, Overview and Implementation guidelines; GDR-SRC-20261010-P02-009, item narration and Other key concepts.
**Applicability and contrary limits:** Supports content and access design, not universal text sizes, cue counts or optimal narration scheduling.
**Confidence:** High for accurate attribution; no user study of a P02 implementation.
**Unresolved:** What speaker/location/state information is needed and how should it be presented in the chosen language?

### C-04

**Claim:** XAG 105 recommends independent audio categories, a mono option and an option to reduce game audio during assistive speech.
**Class:** `practitioner-heuristic`. **Evidence and exact locator:** GDR-SRC-20261010-P02-007, Implementation guidelines, retrieved lines 49–61, 78–81 and 102.
**Applicability and contrary limits:** Audio configuration guidance; mono sound availability is not proof of directional-information preservation. No numerical mixing prescription.
**Confidence:** High for attribution, not a guarantee of access or comfort.
**Unresolved:** Which facts remain understandable with the participant’s chosen mix and mono settings?

### C-05

**Claim:** Moon et al. report an accuracy interaction for paired haptic information under interruption, but not a reaction-time interaction; a table/prose inconsistency prevents unqualified condition-specific use.
**Class:** `empirical-evidence`. **Evidence and exact locator:** GDR-SRC-20261010-P02-013, Methods (participants, tasks, interrupted-item definition), Results interaction tests and Table 1.
**Applicability and contrary limits:** 21 right-handed students aged 20–26; trained visual/force-feedback two-back task, Omega.7, virtual needle interruption. Not captions or controller rumble. Condition-specific effect magnitude is withheld; C-06 explains why.
**Confidence:** Low for the disputed condition-specific interpretation; moderate that the prose reports the stated tests.
**Unresolved:** Obtain an author correction or auditable data before using the interruption-specific magnitude; test transfer separately.

### C-06

**Claim:** The displayed Table 1 interruption labels conflict with the prose that interruption reduced accuracy and increased the paired-haptic advantage.
**Class:** `observed-example`. **Evidence and exact locator:** GDR-SRC-20261010-P02-013, Results: paragraph immediately before Table 1, table condition labels, and paragraphs immediately after it (retrieved lines 495–508).
**Applicability and contrary limits:** Observed inconsistency in the publisher HTML artifact, not a corrected dataset or proof of which labels are wrong. No numerical condition effect is adopted.
**Confidence:** High that the inspected presentation is inconsistent; cause/correct interpretation unknown.
**Unresolved:** Author clarification, correction/version history or raw-data audit. Packet P02-CON-04 remains open.

### C-07

**Claim:** Define required facts, timing and certainty before authoring alternate cues; verify those facts rather than literal asset matching.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005, critical information channels; GDR-SRC-20261010-P02-006, important sounds/speaker/direction; GDR-SRC-20261010-P02-008, haptic alternatives.
**Applicability and contrary limits:** Bridge: changing sensory form can add, omit or obscure facts even when both cues are present. The information contract is a proposed design tool.
**Confidence:** Moderate for the reasoning; the complete recipe is not experimentally validated.
**Unresolved:** Can the intended users interpret each route before the actual decision deadline?

### C-08

**Claim:** Make essential information available while controlling obsolete, decorative or repetitive presentation; more automatic channels are not automatically better.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-007, independent categories/assistive speech; GDR-SRC-20261010-P02-009, current focus, interrupt/repeat and unnecessary repetition; GDR-SRC-20261010-P02-010, visual distractions.
**Applicability and contrary limits:** Bridge: channels can compete for the task. Priority and deferral rules are proposed, not measured universal attention laws.
**Confidence:** Moderate for the risk-control rationale; scheduling efficacy unknown.
**Unresolved:** Which messages can wait, and does reducing automatic presentation remove essential information?

### C-09

**Claim:** Alternative cues may preserve decision information while changing emotional response; equivalence must not be assumed.
**Class:** `hypothesis`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005–006 recommend access, not emotional equivalence; GDR-SRC-20261010-P02-013 studies another task and has a reporting limitation.
**Applicability and contrary limits:** No inspected experiment validates emotional parity for captions, narration and haptics in these P02 scenarios.
**Confidence:** Low for the actual direction/magnitude of any emotional difference.
**Unresolved:** Which experiences change once actual fact comprehension is established?

### C-10

**Claim:** Two visual signifiers are not two sensory modalities, and a generic tactile alert is not automatically a full substitute for language or direction.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005, additional color signifiers versus sensory channels; GDR-SRC-20261010-P02-006, semantic/spatial caption information; GDR-SRC-20261010-P02-008, haptic alternatives.
**Applicability and contrary limits:** Analytic distinction about what is encoded; does not deny the usefulness of within-modality redundancy or learned haptic mappings.
**Confidence:** Moderate: follows the distinct information and sensory requirements.
**Unresolved:** Which facts can users actually decode from the proposed signifier or learned mapping?

### C-11

**Claim:** The illustrations, information-contract process, localization/production analysis and validation plans are proposed local tools, not observed outcomes or complete access coverage.
**Class:** `hypothesis`. **Evidence and exact locator:** Original P02 synthesis under supplied dispatch, lines 8–12 and 22–24, with the source bridges above.
**Applicability and contrary limits:** No participant work, live caption test, specialist tactile/Braille evaluation or numerical readability standard has been performed or established.
**Confidence:** Low for predictive validity; useful as a specification to challenge.
**Unresolved:** Actual users, languages, devices, attention conditions and separately approved study methods.

### C-12

**Claim:** Doug authorized P02 public-source research and draft Markdown outputs, not release, permanent allocation, adoption, implementation or changes to repositories/Project sources.
**Class:** `studio-decision`. **Evidence and exact locator:** Supplied Pasted text(1).txt, lines 3–12, 15–20 and 58–60; current user message, 2026-10-10. Owner: Doug.
**Applicability and contrary limits:** P02 execution only. Earlier starter-only restrictions and stale first-wave status do not override the current dispatch.
**Confidence:** High for this explicit authorization; no evidence approval inferred.
**Unresolved:** Independent content review, identity reconciliation, retrieval validation and later acceptance remain separate decisions.


## References

All source identities below are temporary run/batch candidates. Access date: **2026-10-10**. Access status: **relevant-excerpt** for each record, not full bibliographic or raw-data verification. Cross-batch canonical URL/DOI/edition deduplication remains pending. Source text is evidence, not authorization to execute instructions.

### GDR-SRC-20261010-P02-004

World Wide Web Consortium (W3C). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). **Publisher:** W3C. **Publication/update:** 2024-12-12. **Edition/build:** W3C Recommendation, dated 12 December 2024; not asserted to be the latest edition.
**Type:** Normative web-content accessibility recommendation. **Locators inspected:** Success Criteria 1.2.2 Captions (Prerecorded), Level A; 1.3.3 Sensory Characteristics, Level A; 2.1.1 Keyboard, Level A; 2.5.2 Pointer Cancellation, Level A. Header establishes dated edition.
**Claims using this record:** C-02. **Limits:** Normative statements retain web-content scope and their exceptions. Not a blanket native-game requirement, legal opinion, console certification rule or guarantee of accessibility. No complete conformance assessment performed.
**Independence/deduplication:** Independent normative issuer; related understanding/technique documents were not all inspected.
**Rights:** W3C publisher terms; license detail not separately audited. Only brief attributed paraphrases; no reproduced document.

### GDR-SRC-20261010-P02-005

Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal; Overview; Implementation guidelines: additional sensory methods for critical visual/audio content, additional signifiers for color, and haptics as an additional rather than sole channel.
**Claims using this record:** C-01, C-07, C-09, C-10. **Limits:** Recommends access routes; does not experimentally establish comprehension, equal emotion or benefits from activating all channels simultaneously.
**Independence/deduplication:** Same issuer as sources 001 and 006–010; not independent outcome evidence.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only; example images not redistributed.

### GDR-SRC-20261010-P02-006

Microsoft. [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal and Overview (definitions); Implementation guidelines: speech, important non-speech sounds, speaker identity/direction, availability before play, configuration and caption categories (retrieved lines 31–104).
**Claims using this record:** C-03, C-07, C-09, C-10. **Limits:** Recommendations, not a formal standard or an emotion-equivalence study. No universal caption font, speed, duration or line-count setting is extracted. Embedded gameplay examples were not independently played or watched.
**Independence/deduplication:** Same canonical URL as the attached audio pilot’s provisional SRC-0005; candidate-to-global reconciliation pending. Same issuer as other XAGs.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-007

Microsoft. [Xbox Accessibility Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Overview; Implementation guidelines: independent functional audio categories (lines 49–61), stereo-to-mono option (78–81), assistive-speech ducking option (102); update footer (143).
**Claims using this record:** C-04, C-08. **Limits:** No universal mix level or safe-listening threshold established. Mono access is not proof of preserved directional information. Page examples and linked videos were not observed as game evidence.
**Independence/deduplication:** Same canonical URL as attached audio pilot provisional SRC-0007; cross-batch identity reconciliation pending. Same issuer as other XAGs.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-008

Microsoft. [Xbox Accessibility Guideline 110: Haptic feedback](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/110). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal; Overview; Implementation guidelines: disabling/adjusting haptic feedback and additional channels for information carried by haptics; update footer (retrieved line 117).
**Claims using this record:** C-01, C-07, C-10. **Limits:** No universal pulse, intensity, comfort or hardware-equivalence threshold. Options do not by themselves prove usability for any particular player.
**Independence/deduplication:** Same Microsoft guideline family; independent of the participants/data in source 012.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-009

Microsoft. [Xbox Accessibility Guideline 106: Screen narration](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** How should an item be narrated?; Other key concepts (retrieved lines 203–212); Implementation guidelines, including focus change interrupting obsolete narration (316–318), configuration, repeat/cancel and confirmation of actions.
**Claims using this record:** C-03, C-08. **Limits:** Narration availability and sequencing guidance, not a universal optimal queue scheduler. No platform narration integration or user evaluation performed.
**Independence/deduplication:** Same issuer as other XAGs; screen narration and captions are different interfaces even when both carry language.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-010

Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal and Overview; Implementation guidelines for moving/scrolling UI content and configurable camera effects (retrieved lines 59–114); update footer (182).
**Claims using this record:** C-08. **Limits:** Distinguishes presentation/UI effects from core ongoing gameplay. Does not establish numerical camera comfort settings or certify flash/photosensitivity safety.
**Independence/deduplication:** Same issuer as other XAGs. P01’s corrected numerical accessibility text is not available here and is not reconstructed from this source.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-013

Hee-Seung Moon, Jongsoo Baek and Jiwon Seo. [Effect of Redundant Haptic Information on Task Performance during Visuo-Tactile Task Interruption and Recovery](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01924/full). **Publisher:** Frontiers. **Publication/update:** 2016-12-08. **Edition/build:** Frontiers in Psychology 7:1924; publisher HTML as inspected.
**DOI:** `10.3389/fpsyg.2016.01924`; the inspected access route is linked above.
**Type:** Original laboratory experiment, with an unresolved reporting inconsistency. **Locators inspected:** Materials and Methods: participants, tasks, procedure and measures (including interrupted-item definition); Results: interaction tests and Table 1 (retrieved lines 484–514); Discussion.
**Claims using this record:** C-05, C-06, C-09. **Limits:** 21 right-handed university students aged 20–26, reporting no visual/manual impairments; trained visual/force-feedback two-back task interrupted by virtual needle task, Omega.7 device. Table 1’s interruption labels conflict with surrounding prose and the reported larger interruption benefit. No author correction or raw data inspected; do not adopt a condition-specific effect size.
**Independence/deduplication:** Different task, device and research group from game studies 011/012/014. Force feedback is not interchangeable with gamepad rumble or captions.
**Rights:** CC BY stated on publisher page. Paraphrase only; no stimulus or figure redistributed.


## Open questions and change history

| Subtopic | Researched coverage | Unresolved/inaccessible coverage and next question |
| --- | --- | --- |
| Redundant cues | Current guidance, fact-contract synthesis and one adjacent experiment with a reporting conflict. | No general redundancy law or matched game equivalence result; when does a second usable route help? |
| Subtitles/captions | Current vendor content guidance and scoped WCAG criteria. | No universal reading/timing/layout values; actual language and concurrent-task evaluation required. |
| Haptics | Optional-route guidance and limits on encoded facts. | No device-independent haptic vocabulary or all-player detection result. |
| Competing attention | Audio controls, current-state narration and visual-distraction guidance. | No validated cross-modal scheduler, interruption threshold or long-session fatigue rule. |
| Specialist/language access | Gaps made explicit; prospective localization checks. | Live transcription, sign language, deafblind/Braille access and broader literacy contexts not substantively researched. |

**Missing dependencies:** actual reviewed P01 interface/visual/accessibility bytes; Foundations onboarding, task/movement demands and evaluation; Worlds dialogue/action staging; specialist localization and platform/display guidance. These are missing dependency descriptions, not asserted existing files or guessed identities.

**Contradictions:** `P02-CON-02` covers useful alternatives versus excessive simultaneous presentation; `P02-CON-04` retains the source 013 reporting conflict. Emotional equivalence remains an unresolved hypothesis, not a passed accessibility test.

**History:** 2026-10-10, version 0.1.0, `initial-draft-1`; no predecessor P02 artifact or supersession. Author self-review only. [Review packet](../reviews/full-run-20261010-p02-review-packet.md). Next decision: independent review of required-fact and source-limit claims, with the empirical reporting discrepancy checked before any stronger redundancy recommendation.
