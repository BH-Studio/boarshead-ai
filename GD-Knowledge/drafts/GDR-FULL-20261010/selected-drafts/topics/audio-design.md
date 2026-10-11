---
id: GDR-CAND-20261010-P05-TOP-01
kind: topic
title: Audio design
version: 0.1.0
candidate_revision: independent-review-correction-1
status: draft
run_id: GDR-FULL-20261010
batch_key: P05
attempt_id: P05-authoring-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-11'
evidence_checked: '2026-10-10'
coverage_status: coverage-open
aliases:
- sound design decision contract
- audio mix and spatial information
tags:
- presentation
- research-candidate
- coverage-open
related_topics:
- GDR-CAND-20261010-P05-TOP-02
- GDR-CAND-20261010-P05-TOP-03
- GDK-TOP-0001
related_patterns:
- GDK-PAT-0001
related_genres: []
dependency_ids:
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-W02-TOP-01
source_ids:
- SRC-0003
- SRC-0005
- SRC-0007
- GDR-SRC-20261010-P05-001
- GDR-SRC-20261010-P05-002
- GDR-SRC-20261010-P05-003
- GDR-SRC-20261010-P05-012
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: 5671ba5fe03df995f07213f514ecf02156140a5da96f73588e6ff3af999e8d54
supersedes: []
change_summary: Independent metadata correction adds the already-used W02 dialogue
  dependency; no substantive claim, identity, approval or canonical origin changed.
byte_hash_record: ../reviews/full-run-20261010-p05-review-packet.md#candidate-byte-receipt
---

# Audio design

**Draft expansion and reconciliation candidate — coverage open.** This entry helps choose what sound should communicate, how it should be presented, and when additional sound or simulation is not worth adding. It is not a replacement for `GDK-TOP-0001` or a second canonical Audio design allocation. Existing `GDK-PAT-0001` remains the sole contextual-audio-anomaly identity. P05 does not rerun that pilot or upgrade its evidence. [C-01, C-12]

## Decision and scope

**Decision:** For a particular task and intended experience, which environmental sounds, signals, spatial relationships and mix behaviors should a player be able to perceive, interpret, ignore, configure or recover?

The scope covers ambience, cues, sonic identity, spatial audio, mixing, occlusion, dynamic range and audio accessibility. Music structure is owned by [Music design](music-design.md); language-specific text/performance is owned by [Localization and presentation](localization-and-presentation.md). P02 owns general input, feedback and multimodal principles. This entry applies those reviewed boundaries to audio rather than extracting another generic redundant-cue pattern. [C-08, C-09, C-12]

### Working definitions and assumptions

The following are proposed analytic conventions, not universal terminology requirements. **Ambience** establishes ongoing or recurring environmental activity. A **cue** is an event or change that may inform a judgment; audibility does not establish understood meaning. **Sonic identity** is a deliberately related family of sound characteristics, distinct from the reliability of a particular gameplay signal. **Spatial presentation** represents a source’s apparent relation to a listener. **Mix priority** concerns which signal may displace another under a stated task, not merely which is loudest. **Interruption recovery** concerns whether the still-relevant information can be recovered after presentation stops. [C-03, C-07, C-08, C-11]

For each future application, specify the target build/platform; headphones, speakers or mono; listening environment and chosen volume; player input and movement; caption display distance/size; language; hearing, attention and other access needs; availability of pause; and whether sound carries a required decision. None is silently set to the studio’s hardware. Non-VR seated examples below are illustrative only; VR, handheld, public/noisy and couch contexts require separate evaluation. No medically safe listening level is specified. [C-05, C-06, C-10, C-11]

## Core explanation and mechanisms

### Follow the information, not the asset

A useful diagnostic chain is **valid state → authored signal → rendering → noticed event → interpreted meaning → available response**, with intended experience evaluated alongside it. Rendering documentation supports only selected technical links. A perfectly scheduled and spatialized sound can remain irrelevant, unintelligible, stale or unpleasant. Conversely, an abstract, nonspatial signal may serve a task well. The chain is a proposed way to locate failure, not a proven causal model of engagement. [C-02, C-03, C-08, C-11]

Write the cue’s contract before its timbre: what occurred; what is known and unknown; whether direction matters; any deadline; whether the state may expire; available action; and recovery if missed. Distinguish decorative environmental activity from a required warning even when they share a source object. Do not hide an essential fact under an “ambience” control merely because its recording sounds environmental. The physical source, expressive role and required-information role are different classifications. [C-05, C-06, C-08]

### Context can be expressive without becoming a law

Justice’s SOMA account is a firsthand example of deliberately contrasting environmental soundscapes. It does not establish a general relationship between realism and fear. The corrected pilot’s main comparison remains unresolved: locally recognized context has not been shown there to outperform a matched isolated cue for anticipation. “Necessary sequence unsupported” is not “context never helps.” Silence, an explicit warning, an already familiar cue and no added tension device remain serious alternatives. [C-01, C-07]

For sonic identity, propose a small contrast brief: which families should feel related, which must remain distinct, and what unfamiliar listeners should infer. An attractive family resemblance can be counterproductive when a confirmation and a warning become difficult to distinguish. Recognition of a repeated sound is not proof that the player understands its consequence. Test the relationship rather than count variations or infer success from a finished palette. [C-08, C-09, C-11]

### Spatial plausibility is not automatically useful information

The inspected Steam Audio documentation separates HRTF-based rendering from geometry-driven occlusion, transmission and reflections. Its descriptions also expose source-extent, geometry and material assumptions. These are technical capabilities, not a demonstration that a particular player will locate a source accurately. [C-03]

The design bridge is to ask what spatial distinction the task actually needs. Is the decision “an event happened,” “check the other room,” or “choose a precise direction now”? A small geometric detail may matter to the latter but not the former. Compare a simpler authored approximation with more detailed processing; retain the latter only for a stated informational or expressive benefit. A wall should not be allowed to conceal all access to a mandatory alarm simply because acoustic obstruction is plausible. Nor should an alternate indicator reveal a hidden actor’s identity when the sound communicates only an unidentified event. [C-06, C-08, C-09]

Avoid turning mono support into a claim of spatial equivalence. Evaluate the necessary directional facts through an appropriate accessible representation. Do not assume that an HRTF option, a documented geometry model, or an author’s listening session covers individual hearing profiles, different output devices and camera/listener relationships. P03’s reviewed camera/platform bytes were not available in the selected dependency snapshot; listener-frame policy remains a dependency, not invented reviewed guidance. [C-03, C-05, C-10]

### Range, volume and attention are different decisions

The mixer reference describes group routing, snapshots and ducking; the compressor reference describes a particular range-reducing effect. A blanket gain change and content-dependent range processing therefore should not be treated as the same intervention. The specific documented Unity compressor is fixed-ratio limiting; its inspector defaults are not recommended settings for this library. [C-02, C-04]

A proposed low-range option should be evaluated for quiet information, wanted expressive contrast, competing speech and unpleasant transitions at the participant’s chosen volume. Simply making every component prominent can defeat the reason for prioritization. Conversely, leaving wide expressive contrasts untouched may make some task facts difficult to recover in a given environment. These competing possibilities are hypotheses, not a recommendation to compress every mix. Hearing safety, loudness normalization and device-calibrated exposure are unresearched here. [C-04, C-09, C-10]

### Interruption requires truth and recovery checks

Protecting assistive speech is supported by XAG guidance. A specific scheduling policy is not supplied by that recommendation. When a line or event is interrupted, decide whether to resume it, restart it, summarize its current meaning or discard it as expired. Replaying a now-false warning is not successful recovery. A current-state summary can be preferable to draining a queue of outdated events; a decorative sound may need no replay at all. These are inferences extending the reviewed P02 and W02 distinctions, not a verified audio scheduler. [C-05, C-08]

## Design choices and alternatives

| Decision | Option worth considering | Cost / competing option / exit |
|---|---|---|
| Ambience | Reuse a legible existing relationship when a place or change matters. | More density and setup are not inherently better. Prefer fewer events or no extra preparation if context adds no useful value. [C-01, C-07, C-09] |
| Sonic identity | Related timbral/material families with deliberately distinct decision roles. | Family resemblance may blur warnings and confirmations. Keep an intentionally contrasting signal when classification matters. [C-08, C-11] |
| Spatial treatment | Model the spatial fact the decision requires. | Simulation introduces geometry, state and device checks. An authored region cue or explicit accessible marker may be sufficient. [C-03, C-09] |
| Occlusion | Preserve plausibility when location and obstruction matter. | Reconsider the event contract when obstruction hides required information; do not simply increase intensity. [C-06, C-09] |
| Mix competition | Temporarily reduce or omit nonessential competitors for a valid foreground event. | Constant priority switching may itself distract. Fewer concurrent events or player-requested repetition can be simpler. [C-02, C-05, C-08, C-10] |
| Dynamic range | Offer a content-appropriate alternative after comparison at chosen settings. | No universal range, threshold, attack or release. Category controls and quieter content can be preferable to blanket processing. [C-04, C-05, C-10] |
| Recovery | Current-state summary, replay or discard according to truth and purpose. | Do not replay expired flavor or silently remove a still-needed instruction. A persistent non-audio record may be appropriate. [C-06, C-08] |

## Application process

1. **Diagnose the failure.** Distinguish inaudibility, failed source localization, misunderstood meaning, missing action, unwanted intensity and merely insufficient artistic interest. Do not solve all of them by adding sound. [C-08, C-11]
2. **Specify the contract.** Record role, state validity, permitted uncertainty, deadline, configurable category, competing events and recovery. Name the minimum task facts available without sound. [C-05, C-06, C-08]
3. **Choose the least complex candidate and a credible comparator.** Use existing ambience, authored spatial approximations or explicit signals before committing to another dependency. Preserve legitimate expressive goals separately from task-success measures. [C-01, C-09]
4. **Prepare a conceptual verification matrix.** Include first/repeat exposure, volume/category changes, mono, alternative output, interrupted speech, paused/resumed tasks and changed geometry. Actual implementation remains separately gated. [C-03, C-10, C-11]
5. **Evaluate and revise after authorization.** Locate failures along the information chain; retain conflicting findings. A successful warning with reduced tension may be the correct outcome for a task requiring action. Remove additions that produce no decision-relevant or accepted expressive benefit. [C-08–C-11]

## Patterns and genre adaptations

`GDK-PAT-0001` is an existing low-confidence contextual-anomaly candidate, not a new P05 pattern. The P01 redundant-critical-state and P02 fact-preserving-alternative patterns remain a reviewed-overlap question; P05 does not resolve or duplicate them. See the [dependency receipt](../reviews/full-run-20261010-p05-review-packet.md#reviewed-dependency-transfer).

P05’s two extracted patterns belong to musical transitions and locale-resilient message units. An audio-specific listening-priority extension is [queued for a distinctness decision](../reviews/full-run-20261010-p05-review-packet.md#queued-child-work), rather than forced into this packet. There are no genre files here. A restorative scene, a precise timed task and an uncertain exploration scene can legitimately prioritize different outcomes; those are illustrative experience constraints, not researched genre preferences. [C-09, C-11, C-12]

## Examples and counterexamples

**Illustrative — an inspection station.** A player compares instrument readings while a ventilation system runs. A neighboring station reports a fault. The proposed contract says which station needs checking, not what caused the fault. Compare: a dense realistic rendering; the same event with nonessential ventilation reduced during the report; and a simpler station indicator with optional audio. Keep the underlying task and fault identical. A localized caption identifies the event/station without inventing the fault’s cause. If assistive speech is active, avoid merely postponing the report until it is obsolete; offer a still-valid summary. Nothing was rendered or tested. [C-08–C-11]

**Strong countercase.** In an environment-identification exercise, the apparently decorative ventilation texture is the material being investigated. Aggressively reducing it for every notification destroys the task. Reclassify the signal rather than treating “ambience” as a permanent low-priority category. An expressive listening scene can also reasonably value continuity over rapid interruption. [C-08, C-09, C-11]

**Documented creator example.** SOMA supplies an account of sonic differentiation, not a reproduced scene, measured listener result or proof of the illustrative station design. [C-07]

## Failure modes and constraints

| Warning sign to investigate | Competing explanations | Proposed response |
|---|---|---|
| Players hear the event but act on the wrong object. | Source meaning, spatial rendering, translation or visual conflict. | Isolate the failed fact before modifying intensity or geometry. [C-03, C-08] |
| A cue works only in the author’s headphones. | Device/listener differences, unavailable settings, competing sound. | Restrict the claim; evaluate intended devices and access routes. [C-03, C-05, C-10] |
| Priority changes are more noticeable than the message. | Overfrequent switching, poorly bounded foreground events, unnecessary concurrency. | Compare suppression or fewer events; do not assume more smoothing solves semantics. [C-08, C-10] |
| An option removes a mandatory fact. | Role incorrectly classified as decorative or another channel also unavailable. | Repair the contract and block candidate advancement for that use. [C-05, C-06, C-09] |
| Recovered speech contradicts the current state. | Stale queued content or a source-language update mismatch. | Cancel or summarize current facts; audit linked text/voice revisions. [C-08] |

Production scope includes recording/editorial work, meaningful variants, geometry/material maintenance, event dependencies, settings behavior, localized captions, alternate information, and repeated testing after changes. These are work categories, not estimates. Rights and permission for recordings, voices and derivative assets remain a separate approval matter; this research grants none. Do not manufacture startling intensity or required listening exposure merely to obtain a favorable response. [C-09–C-12]

## Playtest and validation

**PROPOSED — NOT RUN.** No audio asset, prototype, participant recruitment, listening session, latency measurement, game observation or host test was performed in P05. [C-11, C-12]

**Primary comparison:** In one approved task, compare a fixed mix with a bounded foreground-priority treatment and a simpler reduced-content alternative. Preserve valid event facts, target waveform where practicable, task timing, available actions, threat/state behavior and relevant presentation. Record any acoustic differences rather than pretending the mechanisms are isolated when content or loudness changed. Test spatial modeling separately when spatial interpretation is the actual question; do not bundle both interventions and attribute all changes to one. [C-09–C-11]

**Participants and context:** Recruit only after separate authorization, with intended device/input/locale coverage and people who rely on relevant access routes. Determine sample and analytic precision from the actual question and resources, not an arbitrary default. A muted run by a hearing author is an information-availability inspection, not representative access evaluation. Use chosen comfortable settings, allow adjustments and withdrawal, and never force exposure to discomfort. [C-05, C-10, C-11]

**Measures:** Record detection, station/direction identification when required, state-fact comprehension, correct action, recovery after interruption, task cost, perceived agency and comfort separately. Ask about the intended experience without substituting startle for anticipation or physiology for emotion. Record first and repeat exposures and whether a baseline relationship was actually recognized. [C-01, C-08, C-11]

**Decision criteria proposed for later preregistration:** A critical fact becoming unavailable, false or unrecoverable blocks advancement for that task even when preference increases. A more elaborate treatment needs a predeclared worthwhile informational or expressive benefit and acceptable cost relative to its simpler comparator. If no reliable additional value is demonstrated, prefer simplification without claiming statistical equivalence. Report individuals, uncertainty and excluded/missing observations. The study owner must set any quantitative margins before collection; none is approved here. [C-09–C-11]

## Coverage checkpoint

| Assigned facet | Inspected coverage | Open question / missing evidence |
|---|---|---|
| Ambience | Existing corrected pilot and creator rationale. | Matched contextual benefit, repeated play and less-sound comparisons remain open. |
| Cues / sonic identity | Information-role synthesis; creator differentiation. | Recognition versus meaning across unfamiliar audiences; no comparative palette study. |
| Spatial audio | Official HRTF/geometry descriptions. | Perceptual accuracy, non-VR/VR transfer, target listener frame and devices not validated. |
| Mixing / competing signals | Routing/ducking documentation and access guidance. | Comparative priority/recovery policy; no mix, performance or masking measurement. |
| Occlusion | Technical distinctions and conceptual alternatives. | Actual topology/material errors and required-information failures untested. |
| Dynamic range | One documented effect and proposed comparisons. | No loudness standard, safe-listening recommendation, calibration or measured mix targets. |
| Audio accessibility | XAG and reviewed P01/P02 boundaries. | Actual combined-needs participants, localization and chosen-setting outcomes absent. |

Every row remains **coverage-open**. Documentation inspection is not completion of perception research or implementation verification. [C-01–C-12]

## Claim ledger

Claim identifiers are local to this entry. Confidence describes the exact scoped proposition, not the strength of the entire technique. Source recommendations, documentation behavior, measured responses and our proposals are not interchangeable.

### C-01

**Claim:** The supplied corrected pilot does not establish an anticipation advantage for recognizable local ambience over a matched isolated cue; necessity remains unresolved.

**Class:** `observed-example`. **Support and locator:** DEP-PILOT-T: GDK-TOP-0001, 0.1.0/review-correction-1, C-01/C-02/C-17; DEP-PILOT-H addendum. Exact bytes in packet.

**Applicability / opposition:** This observes a draft’s qualified evidence record, not a new replication or universal disproof. **Confidence:** High for the inspected wording; low for the underlying gameplay hypothesis. **Unresolved:** Does a matched interactive comparison demonstrate added value?

### C-02

**Claim:** Unity’s mixer documentation provides groups, snapshots and ducking as separate facilities.

**Class:** `observed-example`. **Support and locator:** GDR-SRC-20261010-P05-001, Audio Mixer window; Snapshots; Ducking.

**Applicability / opposition:** Documentation observation only, not a measured mix or universal architecture. **Confidence:** High for that documentation; untested on a target build. **Unresolved:** Which routing and recovery behavior is available in the eventual target?

### C-03

**Claim:** Steam Audio documents HRTF filtering and separately configurable geometry, occlusion, transmission and reflections.

**Class:** `observed-example`. **Support and locator:** GDR-SRC-20261010-P05-002, HRTF overview; GDR-SRC-20261010-P05-003, named spatial/geometry sections.

**Applicability / opposition:** Capabilities and assumptions do not establish perceived direction, physical fidelity or acceptable cost. **Confidence:** High for described distinctions; low for untested player benefit. **Unresolved:** Which spatial errors actually change a player’s decision?

### C-04

**Claim:** The named Unity compressor is documented as narrowing dynamic range with fixed-ratio limiting; its controls are not recommended game settings.

**Class:** `observed-example`. **Support and locator:** GDR-SRC-20261010-P05-012, opening and Properties.

**Applicability / opposition:** Not a general model of every compressor; no safe exposure level or accessibility outcome inferred. **Confidence:** High for document scope. **Unresolved:** Which content-dependent processing preserves wanted contrast without lost information?

### C-05

**Claim:** XAG 105 recommends independent audio controls, mono options and protecting assistive speech from competition.

**Class:** `practitioner-heuristic`. **Support and locator:** SRC-0007, Goal/Overview/Implementation guidelines.

**Applicability / opposition:** Official guidance, not a formal standard or evidence that any proposed setup is usable. **Confidence:** High for attribution; implementation results untested. **Unresolved:** Can intended users configure and recover important information in context?

### C-06

**Claim:** XAG 104 recommends usable text coverage of relevant speech/non-speech information and contextual speaker/direction cues.

**Class:** `practitioner-heuristic`. **Support and locator:** SRC-0005, Implementation guidelines.

**Applicability / opposition:** No universal caption density, literacy threshold or emotional parity. **Confidence:** High for attribution; mode-specific comprehension unknown. **Unresolved:** Which facts and uncertainties survive competing captions and chosen settings?

### C-07

**Claim:** The SOMA account reports deliberate soundscape contrast and grounded ambience.

**Class:** `practitioner-heuristic`. **Support and locator:** SRC-0003, opening/Upsilon paragraphs.

**Applicability / opposition:** Creator intention in one historical production, not directly observed gameplay or measured emotion. **Confidence:** Moderate for production report; unknown causal effect. **Unresolved:** Which aspects, if any, transfer outside that production and audience?

### C-08

**Claim:** Specify event truth, decision relevance, allowed uncertainty, expiry and recovery before choosing sonic treatment.

**Class:** `inference`. **Support and locator:** C-02/C-05/C-06; inspected P02 multimodal/feedback and W02 dialogue C-12/C-13, packet DEP rows.

**Applicability / opposition:** Bridge: an accurately rendered old or irrelevant cue can still communicate the wrong action. No optimal priority algorithm is established. **Confidence:** Moderate for exposing contradictions; low for comparative benefit. **Unresolved:** Does a truth/expiry policy outperform simpler suppression in this task?

### C-09

**Claim:** Compare authored simplification and mix priority with increasing intensity or acoustic simulation; preserve non-audio access to required facts.

**Class:** `inference`. **Support and locator:** C-02–C-06 and P02 corrected semantic-equivalence boundary.

**Applicability / opposition:** Added rendering detail is useful only insofar as the actual task or desired experience benefits; expressiveness can be a legitimate separate goal. **Confidence:** Moderate as a decision framework, not a measured ranking. **Unresolved:** What additional value justifies the extra authored states and tests?

### C-10

**Claim:** Changing mix range, spatial treatment or alternative modality may alter comfort, interpretation and emotion differently.

**Class:** `hypothesis`. **Support and locator:** C-03–C-06 motivate separate comparisons; no P05 outcome evidence.

**Applicability / opposition:** Do not assume that reduced range is always comfortable or mono preserves spatial information. **Confidence:** Low for any local outcome. **Unresolved:** Which adjustment solves a barrier without creating a new one?

### C-11

**Claim:** The proposed definitions, scenarios, diagnostic sequence and validation rules are testable design proposals.

**Class:** `hypothesis`. **Support and locator:** Original P05 synthesis; source-adjacent constraints above; no results support chosen local procedures.

**Applicability / opposition:** All listening tests, rendering, measurements and participant work NOT RUN; numerical design defaults intentionally absent. **Confidence:** Low until study/production review. **Unresolved:** Are the tasks, controls, accommodations and stop rules feasible and discriminating?

### C-12

**Claim:** P05 is a run-scoped expansion/reconciliation draft, not a replacement or new canonical identity for the pilot.

**Class:** `studio-decision`. **Support and locator:** Doug, P05 complete brief: Assigned outputs; Domain decision questions; Prior audio checkpoint; current user instruction, 2026-10-10.

**Applicability / opposition:** Research/output permission only; excludes implementation, source changes and release. **Confidence:** High for explicit authority. **Unresolved:** Coordination must decide the eventual topic/subtopic mapping and pending allocations.

## References

All records below were inspected as **relevant-excerpt** on **2026-10-10**. Dates identify the inspected snapshot, not a claim of latest engine support. Repeated records are provenance copies, not independent corroboration. Existing pilot/W02 identities are retained; all P05 identities are run-scoped proposals.

### SRC-0003

**Samuel Justice; Frictional Games.** [SOMA – Behind The Sound](https://frictionalgames.com/2015-09-soma-behind-the-sound/). **Publication/update:** 2015-09-17; page also displays 2023-10-10, change scope unknown. **Edition:** Developer article; described game build/platform unspecified.

**Locator:** Opening soundscape/Upsilon paragraphs (web text 13–18); closing production/integration discussion. **Type:** Firsthand production account. **Supports:** C-07; indirect C-09.

**Limits/independence:** Intent, not measured response. No embedded audio/video or build observed. Same production as pilot account, not independent corroboration. **Rights:** Reuse license not verified; attributed paraphrase only.

### SRC-0005

**Microsoft.** [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). **Publication/update:** Updated 2026-03-04; original date unknown. **Edition:** Unnumbered live XAG 104 revision.

**Locator:** Goal; Overview; Implementation guidelines: important speech/non-speech, speaker/direction, category settings (web text 31–117). **Type:** Official vendor guidance. **Supports:** C-06; inferred C-08–C-10.

**Limits/independence:** Not a formal standard or certification claim; no cross-language reading-speed or emotional-equivalence finding. Same issuer as SRC-0007. **Rights:** Reuse license not verified; attributed paraphrase only.

### SRC-0007

**Microsoft.** [Xbox Accessibility Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105). **Publication/update:** Updated 2026-03-04; original date unknown. **Edition:** Unnumbered live XAG 105 revision.

**Locator:** Goal; Overview; Implementation guidelines: separate categories, mono, spatial audio, pause exceptions, assistive speech (web text 31–102). **Type:** Official vendor guidance. **Supports:** C-05; inferred C-08–C-10.

**Limits/independence:** Recommendations, not an implemented configuration, hearing-safety standard or measured usability. Same issuer as SRC-0005. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-001

**Unity Technologies.** [Audio Mixer window](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html). **Publication/update:** Publication/update unknown. **Edition:** Unity 6.0 / 6000.0 documentation snapshot.

**Locator:** Audio Mixer window opening; How it works; Snapshots; Ducking (HTML text 125–148). **Type:** Official technical documentation. **Supports:** C-02; indirect C-08/C-09.

**Limits/independence:** Described routing capability only; Web support caveat retained. Not a runtime test, perceptual benefit, recommended bus count or middleware selection. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-002

**Valve.** [HRTF — Steam Audio C API](https://valvesoftware.github.io/steam-audio/doc/capi/hrtf.html). **Publication/update:** Unknown. **Edition:** Unnumbered live documentation; SDK/plugin build not established.

**Locator:** HRTF overview; IPLHRTFSettings type and sofaFileName descriptions. **Type:** Official technical documentation. **Supports:** C-03; indirect C-09/C-10.

**Limits/independence:** HRTF representation and available data route, not evidence of localization accuracy for a player. Same product/documentation family as P05-003. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-003

**Valve.** [Steam Audio Unreal Engine Integration — User’s Guide](https://valvesoftware.github.io/steam-audio/doc/unreal/guide.html). **Publication/update:** Unknown. **Edition:** Unnumbered live guide; integration build not established.

**Locator:** Spatialize an audio source; Use a custom HRTF; Tag geometry; dynamic geometry/materials; Model occlusion by geometry; transmission; reflections; baking (web text 5–283). **Type:** Official technical documentation. **Supports:** C-03; indirect C-09/C-10.

**Limits/independence:** Geometry, source-extent and processing descriptions only. No performance measurement, engine recommendation or verified acoustic fidelity. Same product as P05-002. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-012

**Unity Technologies.** [Audio Compressor Effect](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioCompressor.html). **Publication/update:** Publication/update unknown; documentation build stamp 2026-10-09. **Edition:** Unity 6.0 / 6000.0 manual snapshot.

**Locator:** Opening description and fixed-limiter clarification; Properties (HTML text 126–165). **Type:** Official technical documentation. **Supports:** C-04; indirect C-10.

**Limits/independence:** This named implementation is described as fixed-ratio limiting, not a generic adjustable-ratio compressor. Its defaults are not design targets or safe-listening thresholds. **Rights:** Reuse license not verified; attributed paraphrase only.

## Open questions and change history

**2026-10-10 — initial-author-draft, version 0.1.0.** No predecessor P05 artifact; no supersession or new canonical assignment. Evidence checked means the source passages and named dependency bytes were inspected, not that their conclusions were approved. The separate author self-review is in the [P05 packet](../reviews/full-run-20261010-p05-review-packet.md#author-self-review). No independent P05 review has occurred.

**Handoff:** complete draft artifact, bounded source coverage and unresolved local outcomes. Gate C independent review and acceptance remain outstanding; P05 host Gate D tests are NOT RUN; Gate E acceptance/release is NOT PASSED. Next decision: Coordination reviews scope, evidence precision, identity/overlap mapping and proposed child work before any separately authorized validation or release.

## Independent review correction 1 — 2026-10-11

An independent content review of the byte-identical Library candidates added `GDR-CAND-20261010-W02-TOP-01` to `dependency_ids`, matching the existing C-08 and interruption-recovery attribution. No substantive research claim changed. The preceding author-stage history and packet byte receipt describe the preserved original; the selected corrected hash is in the separate P05 correction receipt. Both Library origins remain equivalent byte sources with no canonical-origin selection; author final-response provenance is unverified and the private response was not accessed. Version remains 0.1.0, status draft, coverage open, and all reviewer/approval fields remain null. Independent inspection is complete for this correction; acceptance, host validation and release remain outstanding. No player, runtime or host test was run.
