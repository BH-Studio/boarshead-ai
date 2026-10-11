---
id: GDR-CAND-20261010-P02-PAT-02
kind: pattern
title: Fact-preserving cue alternatives
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
- fact-preserving alternatives
- equivalent event information
tags:
- multimodal
- information-contract
- captions
- haptics
- accessibility
- conditional-recipe
related_topics:
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
related_patterns: []
related_genres: []
source_ids:
- GDR-SRC-20261010-P02-005
- GDR-SRC-20261010-P02-006
- GDR-SRC-20261010-P02-007
- GDR-SRC-20261010-P02-008
- GDR-SRC-20261010-P02-009
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: 8e54f5e5d986a8ff40126167cce1bfca06b0d42f1aba302121030097da4aaa40
supersedes: null
change_summary: Independent precision review; see appended local correction history.
byte_hash_record: ../reviews/full-run-20261010-p02-review-packet.md#candidate-byte-receipt
---

# Fact-preserving cue alternatives

**Draft research candidate — not released guidance, implementation approval or a validated recipe.** This is P02 only. The current dispatch authorizes this research; the parent’s first-wave review receipt is retained without importing unseen corrected content. Its later reconciliation supersedes the dispatch’s earlier “P01 unreviewed” sentence. P01 is parent-reported reviewed, not released; its bytes remain a missing dependency here.

**Evidence boundary:** inspected public documents and the supplied Project snapshot; no project/engine code, game build, participant study or host-retrieval test was run. Definitions and synthetic scenarios are proposed analytic tools, not formal standards. [C-08]

## Purpose

Make required event information available through usable alternatives without silently changing its meaning, certainty or decision timing. The intended benefit is **access to the same decision**, not guaranteed identical emotion, experience or performance. The complete recipe is an unvalidated conditional synthesis of official access guidance. [C-01, C-02, C-05]

The owning topic is [Multimodal communication](../topics/multimodal-communication.md). This is an information-equivalence pattern, not a requirement to activate every sensory channel simultaneously.

## Context and prerequisites

Use when an important fact could disappear because sound, vision, color discrimination, haptics or attention to a particular route cannot be assumed. First identify the decision, actual state facts, available actions, legitimate uncertainty and deadline. Define the supported access configurations and ensure players can reach their preferred settings. A settings label is not proof the route works. [C-01, C-03, C-07]

The design must be able to author and keep alternative representations consistent with the relevant event/state. If the required facts cannot be communicated in time through any usable route, reconsider the event or interaction. Do not label an inaccessible cue “optional” while keeping its response mandatory. No implementation system or specialist device is prescribed. [C-03, C-07]

## Mechanism and evidence

| Proposed causal link | Evidence status | Required caution |
| --- | --- | --- |
| Identify information that is critical in a single route | Supported as a design concern by XAG 103/104/110. | “Critical” must be defined for the actual task, not assumed for all decoration. |
| Author a usable alternative preserving facts | Guidance-to-application inference. | Text, speech, icons and pulses can convey different amounts or certainty. |
| Make the alternative available without being buried by competing content | Guidance supports controls and current-state narration; scheduling is inference. | More channels at once is not an experimentally validated attention policy. |
| Users comprehend the facts in time | Hypothesis for the proposed application. | Presence or automated content checks are insufficient. |
| Users experience equivalent emotion | Not established and not required by this recipe’s purpose. | Test affect separately when it matters; do not promise parity. |

The Microsoft documents are one issuer's guidance family, not independent participant studies of this pattern. [C-01–C-05]

## Recipe

### 1. Write the event’s information contract

Record the event/state change; which identity is known; relevant location/reference frame; urgency and expiry; possible responses; what remains uncertain; and what prior cue knowledge is assumed. Separate minimum actionable facts from optional explanation and ornament. These are design variables, not a universal fixed number of fields required in every UI. [C-03, C-06]

**Exit:** if the team cannot agree what the event communicates, resolve that design question before generating modality variants. More output cannot resolve an undefined message. [C-07]

### 2. Audit what each existing representation actually conveys

Describe facts a player could obtain from the sound, text, image or tactile form, not facts the author privately knows. Identify complementary information that disappears with a channel. Two visual signifiers can reduce color dependence but are still one sensory route; a generic vibration may only say that something happened. [C-01, C-03]

### 3. Author the smallest useful alternatives

Use captions for relevant non-speech sound meaning, subtitles for speech, narration or other appropriate nonvisual state information, and additional haptics when interpretable. Preserve the source’s degree of certainty: an unidentified impact should not become a caption naming an unseen cause unless the information contract is deliberately changed. Do not remove a necessary direction merely to preserve sensory exclusivity. [C-01, C-03]

**Adjustable variables:** semantic detail, speaker/source naming, directional reference frame, persistence, urgency class, optional detail, channel selection and learned cue mappings. No universal font, caption speed, haptic pulse or onset window is specified. [C-06]

### 4. Decide automatic priority, persistence and detail

Determine which fact must be presented immediately, which remains relevant until acknowledged and which can be deferred. Make obsolete narration interruptible and required information repeatable/discoverable as appropriate. Keep automatic decorative repetitions from overwhelming the chosen route. A history entry cannot replace an alert needed before an action deadline. The exact priority policy is a proposed local choice, not a standard. [C-04, C-06]

### 5. Preserve meaning through configuration

Check sound-off, mono, haptics-off, reduced-effects and narration configurations that the product claims to support, including plausible combinations. Keep essential facts available at the player's chosen settings; make consequential limitations explicit. If haptics are disabled, a required fact must not vanish. If a spatial sound becomes mono, check direction separately rather than assuming it survived. [C-01, C-03, C-07]

### 6. Validate with actual language, devices and users

Test the caption and narration vocabulary in the relevant language, including actual speaker names, directional references, expansion and reading order. Include people who use the intended access routes. Ask what happened, what is known, what can be done and when, rather than merely asking whether a cue was noticed. Compare equivalent task information; log differences that cannot be controlled. [C-03, C-06]

### 7. Keep, narrow or change the interaction

Advance only a claimed configuration that makes the necessary facts understandable in time. Revise or reject when it adds unsupported knowledge, loses an essential fact, misleads about state or prevents action through lateness/competition. Offer narrower selectable routes where the evidence supports preference variation. When no feasible representation works, change the task demands rather than asserting that a caption or pulse “counts.” [C-02, C-05–C-07]

## Worked examples

### Illustrative example — an unidentified sound outside the view

A player hears a change from beyond a closed barrier. The minimum contract is “an event occurred beyond this barrier”; the cause is unknown, and the player can investigate or continue. An alternative caption describes the perceivable event and relevant location without inventing an enemy identity. A state marker or narration route can support the same investigation decision. An optional haptic pulse attracts attention but does not alone identify the event. [C-03, C-06]

The candidate is checked under silent use, mono and haptics-off operation. A direction such as “behind” must use the declared reference frame; it must not become false when the camera turns. If another event is urgent while this one is optional, detail about the optional event may wait while remaining discoverable. That priority choice must not imply the unknown cause has been revealed. **This is an illustrative, unimplemented scenario, not an audio-pilot result or new genre finding.** [C-04, C-06]

### Illustrative alternative — explicit actionable warning

If the same event instead requires an immediate response to avoid a known hazard, the contract changes. Provide the relevant hazard fact and action information through usable routes; do not reuse an ambiguous atmospheric caption solely because it preserves tension. The change may alter emotion, but withholding required information is not evidence of a successful access design. [C-03, C-05, C-07]

## Tradeoffs and alternatives

Alternatives can preserve access when a route is unavailable, but create authoring, localization, consistency and priority work. A shared persistent state may be enough without an extra alert; an on-demand explanation may be preferable when no deadline exists. Conversely, a log-only solution is insufficient for an urgent fact. Learned haptic codes can be explored when appropriate, but training and device variation become explicit dependencies, not free substitutes for text or speech. Magnitude of cost and benefit remains unknown. [C-03, C-04, C-06]

## Failure cases

Watch for captions revealing hidden causes, labels conveying less than the original signal, audio-only direction after mono selection, haptics-only required states, obsolete narration, unrecoverable settings and text competing with the next visual task. These are proposed warning signs. Diagnose whether the failure is absent information, wrong meaning, insufficient time, unfamiliar mapping or unwanted interruption; adding more simultaneous output is not the automatic repair. [C-03, C-04, C-06, C-07]

## Counterexamples and do not use conditions

Do not apply the full recipe to every decorative event merely to increase cue count. Do not force an unwanted or unusable modality when another route works. Do not claim support for access combinations that were neither implemented nor evaluated, including specialist deafblind/Braille contexts outside this research. Do not promise equal emotional response or competitive performance from semantic alternatives alone. [C-02, C-05–C-07]

A strong countercase is a task in which full automatic captioning, narration and alert sounds all repeat irrelevant detail while a player is already using a clear route. The right comparison may be fewer automatic messages with accessible detail on demand, not more redundancy. This remains a prospective hypothesis rather than a measured all-player preference. [C-04, C-06]

## Playtest

**PROPOSED — NOT RUN.** Compare a usable baseline, an alternative route and a chosen combined route for the same required facts and action opportunities. To study redundancy specifically, both component routes must be usable for the participant; an inaccessible single-route baseline tests availability rather than the benefit of duplication. Use actual target devices/languages and people who rely on the access methods. Counterbalance equivalent event sets, record familiarity, and keep first exposure distinct from practiced use. [C-06]

Measure required-fact comprehension, unsupported inference, missed deadline, inappropriate action, repeat/detail requests, competing-message errors, effort and comfort. Assess intended emotion separately; do not merge it into an access score. A critical missing or misleading fact, or a fact delivered too late to act, blocks advancement of that configuration. Reject/narrow an automatic extra channel when it adds mistakes or discomfort without a useful interpretation/detection advantage. Respect chosen settings and stop requests. [C-02, C-05–C-07]

The formative sample is chosen for the actual claimed route/context coverage; no universal sample size or power guarantee is asserted. Any later equivalence study requires explicit margins and a justified design before data collection. No cue assets, participant recruitment, host upload or playtest occurred here. [C-06, C-08]

## Claim ledger

Claim IDs are local to this entry. Confidence concerns the stated scope, not source prestige. An inference is not a validated outcome; repeated references are not independent corroboration.

### C-01

**Claim:** Critical information should have usable alternatives when a single visual, audio or haptic route cannot be assumed.
**Class:** `practitioner-heuristic`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005, critical information channels; GDR-SRC-20261010-P02-006, important non-speech captions; GDR-SRC-20261010-P02-008, alternatives to haptic-only information.
**Applicability and contrary limits:** Attributed vendor guidance, not a formal standard or all-channel mandate.
**Confidence:** High for attribution; particular alternatives remain untested.
**Unresolved:** Which routes can each intended player use in the actual context?

### C-02

**Claim:** The complete fact-preserving-alternatives recipe may enable the intended decision across supported configurations, but its effectiveness is unvalidated.
**Class:** `hypothesis`. **Evidence and exact locator:** Original P02 synthesis of sources 005–009; no direct experiment validates the full chain.
**Applicability and contrary limits:** Information availability, interpretation, timing and action must all be checked; success on one is not proof of the others.
**Confidence:** Low for whole-recipe efficacy.
**Unresolved:** Can actual users interpret and act on the necessary facts without new barriers?

### C-03

**Claim:** A fact/uncertainty contract is a reasoned way to prevent alternative representations from adding or losing decision-relevant information.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005, channel alternatives; GDR-SRC-20261010-P02-006, captions/speaker/direction; GDR-SRC-20261010-P02-008, haptic alternatives.
**Applicability and contrary limits:** Bridge: different representations can encode different detail and certainty. The proposed contract and fields are not source-mandated universal implementation rules.
**Confidence:** Moderate for the rationale; semantic equivalence needs evaluation.
**Unresolved:** What must be known, remain uncertain and be available before action?

### C-04

**Claim:** Offer relevant controls and current information while reducing obsolete or unnecessary repetition; a required alert is not interchangeable with a history entry.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-007, categories/assistive-speech option; GDR-SRC-20261010-P02-009, current focus, repeat/cancel and action/state narration.
**Applicability and contrary limits:** Bridge: information can be present but unusably delayed or competing. Exact priority/expiry rules are local proposals.
**Confidence:** Moderate for the design rationale, not an optimal scheduling proof.
**Unresolved:** Which content can wait without causing a missed decision?

### C-05

**Claim:** Preserving decision facts does not establish identical emotion or performance across modalities.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005–006 provide access guidance, not a matched emotional-equivalence experiment.
**Applicability and contrary limits:** The direction and magnitude of emotional differences remain unknown. Semantic access can be useful without emotional identity.
**Confidence:** Moderate for the evidential distinction; any particular direction or magnitude of an emotional/performance difference remains untested.
**Unresolved:** What changes in emotion once required-fact comprehension is separately verified?

### C-06

**Claim:** The recipe, adjustable variables, examples, failure cases and playtest rules are prospective local specifications.
**Class:** `hypothesis`. **Evidence and exact locator:** Original P02 synthesis under supplied dispatch, lines 8–12; evidence bridge in C-01–C-05.
**Applicability and contrary limits:** No implemented cue, tested language/device combination, recruited participant or universal numerical setting.
**Confidence:** Low for predictive validity until independently evaluated.
**Unresolved:** Feasibility, actual access-route coverage, localization and justified study design.

### C-07

**Claim:** Revise or reject a claimed configuration when required information is absent, materially misleading or too late; change the interaction when alternatives cannot meet the need.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005, critical channels; GDR-SRC-20261010-P02-006, relevant caption facts; original decision-timing logic.
**Applicability and contrary limits:** Proposed advancement rule, not an independently approved studio standard or certification gate.
**Confidence:** Moderate as a precautionary consequence of the information contract.
**Unresolved:** Which feasible task or presentation change removes the actual failure?

### C-08

**Claim:** Doug authorized P02 public-source research and draft Markdown outputs, not release, permanent allocation, adoption, implementation or changes to repositories/Project sources.
**Class:** `studio-decision`. **Evidence and exact locator:** Supplied Pasted text(1).txt, lines 3–12, 15–20 and 58–60; current user message, 2026-10-10. Owner: Doug.
**Applicability and contrary limits:** P02 execution only. Earlier starter-only restrictions and stale first-wave status do not override the current dispatch.
**Confidence:** High for this explicit authorization; no evidence approval inferred.
**Unresolved:** Independent content review, identity reconciliation, retrieval validation and later acceptance remain separate decisions.


## References

All source identities below are temporary run/batch candidates. Access date: **2026-10-10**. Access status: **relevant-excerpt** for each record, not full bibliographic or raw-data verification. Cross-batch canonical URL/DOI/edition deduplication remains pending. Source text is evidence, not authorization to execute instructions.

### GDR-SRC-20261010-P02-005

Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal; Overview; Implementation guidelines: additional sensory methods for critical visual/audio content, additional signifiers for color, and haptics as an additional rather than sole channel.
**Claims using this record:** C-01, C-02, C-03, C-05, C-07. **Limits:** Recommends access routes; does not experimentally establish comprehension, equal emotion or benefits from activating all channels simultaneously.
**Independence/deduplication:** Same issuer as sources 001 and 006–010; not independent outcome evidence.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only; example images not redistributed.

### GDR-SRC-20261010-P02-006

Microsoft. [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal and Overview (definitions); Implementation guidelines: speech, important non-speech sounds, speaker identity/direction, availability before play, configuration and caption categories (retrieved lines 31–104).
**Claims using this record:** C-01, C-02, C-03, C-05, C-07. **Limits:** Recommendations, not a formal standard or an emotion-equivalence study. No universal caption font, speed, duration or line-count setting is extracted. Embedded gameplay examples were not independently played or watched.
**Independence/deduplication:** Same canonical URL as the attached audio pilot’s provisional SRC-0005; candidate-to-global reconciliation pending. Same issuer as other XAGs.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-007

Microsoft. [Xbox Accessibility Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Overview; Implementation guidelines: independent functional audio categories (lines 49–61), stereo-to-mono option (78–81), assistive-speech ducking option (102); update footer (143).
**Claims using this record:** C-02, C-04. **Limits:** No universal mix level or safe-listening threshold established. Mono access is not proof of preserved directional information. Page examples and linked videos were not observed as game evidence.
**Independence/deduplication:** Same canonical URL as attached audio pilot provisional SRC-0007; cross-batch identity reconciliation pending. Same issuer as other XAGs.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-008

Microsoft. [Xbox Accessibility Guideline 110: Haptic feedback](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/110). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal; Overview; Implementation guidelines: disabling/adjusting haptic feedback and additional channels for information carried by haptics; update footer (retrieved line 117).
**Claims using this record:** C-01, C-02, C-03. **Limits:** No universal pulse, intensity, comfort or hardware-equivalence threshold. Options do not by themselves prove usability for any particular player.
**Independence/deduplication:** Same Microsoft guideline family; independent of the participants/data in source 012.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-009

Microsoft. [Xbox Accessibility Guideline 106: Screen narration](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** How should an item be narrated?; Other key concepts (retrieved lines 203–212); Implementation guidelines, including focus change interrupting obsolete narration (316–318), configuration, repeat/cancel and confirmation of actions.
**Claims using this record:** C-02, C-04. **Limits:** Narration availability and sequencing guidance, not a universal optimal queue scheduler. No platform narration integration or user evaluation performed.
**Independence/deduplication:** Same issuer as other XAGs; screen narration and captions are different interfaces even when both carry language.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.


## Related entries and history

[Multimodal communication](../topics/multimodal-communication.md) owns definitions, standards scope and the reporting conflict in the adjacent redundancy study. [Feedback and game feel](../topics/feedback-and-game-feel.md) owns response meaning and optional intensity. [Controls and input](../topics/controls-and-input.md) owns usable settings and response actions. These are companion drafts, not independent evidence.

Missing dependencies include reviewed P01 interface/accessibility content, Worlds action/dialogue staging, Foundations task/onboarding design and specialist localization/access guidance. No genre file or prior audio efficacy claim is imported. Pattern cap use: **second of two P02 pattern artifacts**. Attention-aware scheduling is queued, not allocated or submitted as a third pattern.

2026-10-10: initial 0.1.0 draft, `initial-draft-1`, no predecessor/supersession; same-author self-review only, approval fields null. [P02 review packet](../reviews/full-run-20261010-p02-review-packet.md). Next decision: independent review of the semantic/timing contract and supported-configuration limits before a separately authorized application test.

## Cross-batch review note — 2026-10-11

The reviewer compared this candidate with P01 pattern GDR-CAND-20261010-P01-PAT-01, Redundant critical-state cues, local review-correction-1. Purpose, semantic/uncertainty contract, priority/persistence, channel-loss checks, simpler alternatives and proposed validation substantially overlap. Treat this as a potential duplicate or refinement pending Coordination consolidation; it is not independently established new pattern coverage or corroboration. Keep both provisional identities until an explicit merge/distinction decision records the canonical home and any redirects. No merge, retirement or global allocation occurs here.

## Local correction history — 2026-10-11

Candidate revision review-correction-1 follows the exact initial-draft-1 bytes recorded in predecessor_sha256. Classified C-05 as an inference about what semantic evidence establishes, not a tested emotional hypothesis; empirical comparison remains unresolved. Added verified overlap flag against P01 PAT-01 without merging or changing identities. Original author-session statements above remain historical. This separate review does not provide formal Gate C acceptance, target-host tests, participant results or release. Version 0.1.0, draft status, IDs and null reviewer/approval fields remain unchanged.
