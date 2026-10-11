---
id: GDK-TOP-0001
kind: topic
title: "Audio tension and ambience"
version: 0.1.0
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
updated: "2026-10-10"
evidence_checked: "2026-10-10"
aliases: ["ambient tension", "audio suspense"]
tags: [audio, ambience, anticipation, uncertainty, comprehension, accessibility, exploration, waiting]
related_topics: []
related_patterns: [GDK-PAT-0001]
related_genres: []
source_ids: [SRC-0001, SRC-0002, SRC-0003, SRC-0004, SRC-0005, SRC-0006, SRC-0007, SRC-0008]
reviewer: null
approved_by: null
approved_date: null
---

# Audio tension and ambience

**Draft research candidate, not released knowledge or a validated recipe.** Based on the accessible GD-Knowledge-Starter-v0.1.0 candidate and Doug’s supplied bounded brief. All new identities are snapshot-scoped proposals. `evidence_checked` records the actual public-text inspection on this date; it does not mean the original graphic, every linked source, or a game build was inspected. SRC-0001 remains lead-only. Formal reviewer and approval fields remain unassigned.

## Decision and scope

**Decision:** When is recognizable ambient context worth establishing before an anomalous sound, rather than using an isolated cue, an expected cue’s absence, sustained uncertainty, an overt warning, or no additional tension technique?

**Finding:** The inspected evidence does **not** establish that contextual preparation produces more anticipation or unease than a matched isolated cue in player-controlled exploration. It supports an adjacent perceptual mechanism and supplies production rationales, not the requested causal comparison. Treat the recipe as an optional hypothesis to evaluate, not a default, necessary sequence, or sufficient cause of tension. [C-01, C-02, C-05, C-17]

**Proposed experience:** intelligible anticipation or unease while retaining task comprehension, meaningful choices and player-controlled sensory comfort. Fear, surprise, startle and confusion are not interchangeable successes. Some designs should pursue comfort or concentration instead. [C-15, C-17]

The bounded context is exploration or waiting between encounters where environmental sound may suggest uncertain threat. The entry is game- and engine-neutral. Music, captions, interface warnings, threat behavior and encounter staging are comparison variables, not separate researched topics. No engine settings, audio assets, game adoption, or participant testing are authorized. No neighboring topic or genre entries are assumed to exist. [C-16]

### Operational definitions

These are **proposed analytic conventions**, not a formal standard or a validated emotional scale. Use them to avoid changing the dependent variable halfway through a test. [C-15]

| Term | Working meaning for this pilot | Distinction to preserve |
| --- | --- | --- |
| Ambience | Ongoing or recurrent environmental sound providing a sense of place or ordinary activity. | A recorded loop is not automatically a context the player recognizes. |
| Cue | A perceivable event or change that a player might use to infer a state. | An audible event need not communicate useful information. |
| Recognizable context | The player can describe or predict some relevant regularity, source, or ordinary relationship before the deviation. | Do not infer recognition from an author’s intended soundscape or elapsed time alone. |
| Familiarity | Prior experience with a sound, its source, or its learned game meaning. | Everyday familiarity, familiarity with a genre convention, and learning this game’s cue mapping are different. |
| Expectation | A prospective belief about what could occur, including when, where, or from what cause. | It need not be correct or verbalized; this pilot measures only selected reportable expectations. |
| Anomaly | A deviation relative to an expectation or recognized relationship. | “Strange to the designer” is not proof of deviation for a player. |
| Uncertainty | Incomplete knowledge of cause, state, timing, location, or outcome. | Uncertainty about a possible outcome differs from not understanding a required action. |
| Tension / suspense | For this design decision, future-oriented anticipation of a consequential unresolved event; record anticipation and unease separately. | The cited papers’ broader “suspense” ratings are not automatically this construct. |
| Fear / perceived threat | Fear is a reported emotional response; perceived threat is a judgment that harm or loss is possible. | Neither proves the other, and neither proves anticipation. |
| Surprise / startle | Surprise concerns an unexpected event; startle is an abrupt reported or observed reflex-like reaction. | A momentary flinch is not evidence of sustained anticipation. No reflex instrumentation was used here. |
| Confusion / comfort | Confusion concerns difficulty interpreting the event or task; comfort concerns tolerability and willingness to continue at chosen settings. | Higher confusion or lower comfort is not a substitute for the intended experience. |
| Absence / silence | Absence is omission of a locally expected event; silence is reduced or absent sound output. | Turning all audio off is not the same manipulation as omitting one expected cue. |
| Diegetic / music / warning | World-attributed environmental event; musical presentation; explicit informational alert. | Their role and meaning can overlap; classify by the particular implementation rather than its asset type. |

### Assumptions to make explicit in a later application

Record the intended viewing context, listening device and room noise, chosen volume and assistance settings, display/caption legibility, input method, current task, familiarity, and opportunity to wait or withdraw. The proposed test below begins with adult, non-VR, seated exploration/waiting tasks using the participant’s familiar keyboard/mouse or controller. That test scope is not a claim that the findings transfer to VR, handheld/mobile, children, every hearing profile, or noisy public environments. The studio’s own hardware and any particular game are not the default context. [C-15]

## Core explanation and mechanisms

### Evidence comparison before a recipe

| Evidence | What it addresses | What it cannot establish |
| --- | --- | --- |
| Original auditory-scene experiment, SRC-0002 | New-source detection in regular versus random tone streams. See the exact study record in C-05. | Threat meaning, sustained unease, or superiority to a matched isolated cue. |
| Original film experiment, SRC-0004 | Self-reported suspense under audio/video presentation differences; measurement dissociation. See C-06. | The effectiveness or necessity of the proposed gameplay recipe. |
| Original repeat-viewing experiment, SRC-0008 | Changes across repeated suspenseful film segments. See C-07. | A universal habituation schedule or effects of learning a game’s cue reliability. |
| Creator accounts, SRC-0003 and SRC-0006 | Intended grounded context, selective density, and production constraints. See C-09/C-10. | Player responses measured under controlled comparisons. |
| Official guidance, SRC-0005 and SRC-0007 | Access to important information and configurable audio presentation. See C-08/C-11. | Certification, emotional equivalence, or validation of this particular recipe. |

**Candidate causal chain:** a player acquires a relevant expectation → notices a deviation → interprets it as potentially consequential → remains uncertain about an outcome while retaining useful choices. Only the early perceptual link has direct adjacent experimental support in this inspected corpus. The semantic, affective and agency links are hypotheses for the bounded game context. A detected mismatch could instead be harmless novelty, amusement, a technical-error interpretation, or distraction. [C-01, C-05, C-12, C-13]

Do not substitute “regular” for “safe,” “realistic” for “recognized,” or “recognized” for “threatening.” A familiar alarm may communicate urgency without newly establishing ambience. Conversely, a regular mechanical sound can reassure rather than disturb. These are logical alternatives and illustrative mechanisms, not measured effects of the pilot. [C-13, C-15]

### Serious alternative explanations

An apparent advantage might come from loudness or spectral contrast, an already learned horror convention, clearer information, a change in actual threat behavior, task interruption, or a demand to report suspense. Conversely, an A–B null difference could reflect failure to establish a recognized context, insensitive measurement, or a genuinely unnecessary preparation step. The comparison must distinguish these interpretations rather than treat every result as confirmation. [C-01, C-06, C-15]

**Necessity and sufficiency:** an observed benefit in one condition would establish neither. A convincing counterexample can defeat a specified universal claim, but it does not identify the best alternative. In this corpus, film evidence challenges the broad three-stage story; it does not cleanly falsify every interpretation of the seed inside the bounded interactive context. Preserve `CON-0001` as an unsupported necessity proposition with unresolved scope, not “scientifically disproven in all games.” [C-02, C-17]

## Design choices and alternatives

The following are **conditional design inferences and testable options**, not established rankings. [C-12, C-13, C-15, C-17]

| Choice | Conditions worth testing | Costs / exit conditions |
| --- | --- | --- |
| Recognized context plus deviation | A meaningful baseline can be learned without delaying the task; interpreting a changed relationship matters more than a brief impact. | Requires baseline legibility, state consistency and repeat-exposure testing. Exit when the baseline is unnoticed or preparation adds no useful value. |
| Isolated cue without local preparation | Existing player knowledge supplies meaning, or little preparation time is available. | Check unfamiliar listeners and avoid assuming that an abrupt response is anticipation. It is the primary simpler comparison, not an intentionally weak control. |
| Missing expected cue / selective absence | A specific event was actually expected and its omission is detectable in available modalities. | Loss of a decorative loop may convey nothing. Preserve essential feedback and differentiate absence from playback failure. |
| Sustained uncertainty without a new anomaly | The unresolved situation already supports meaningful choices and an additional cue would over-specify the outcome. | Can become aimless waiting or confusion. Provide interpretable progress or an exit rather than extending uncertainty indefinitely. |
| Overt warning | Timely state comprehension or a required response takes precedence over ambiguity. | May reduce ambiguity, but that is not automatically an emotional failure. Test its meaning, reliability and access. |
| Less sound / no added tension device | The task requires concentration, the existing scene is sufficient, sensory comfort is the priority, or added audio has no demonstrated value. | “Do less” does not remove essential information or accessibility support. Avoid inventing threat simply to justify a pattern. |

### Information contract

Specify what every player needs to know at the decision point: that an event occurred, whether it is relevant, any required direction/timing, the available actions, and the stated reliability of the signal. Put optional ambiguity in unresolved cause or future outcome, not in access to required information. A caption can report an unexplained impact without naming an unseen enemy; a critical danger cue cannot be hidden merely to preserve a hearing-dependent mystery. This contract is a proposed application of accessibility guidance, not a tested optimal policy. [C-04, C-08, C-11, C-12]

## Application process

1. **Diagnose.** State the desired experience and required task facts. Identify whether the current problem is missing anticipation, unreadable information, startle-only impact, discomfort, or a misplaced desire for more audio.
2. **Choose.** Compare the least complex options above. Identify the player’s actual prior knowledge; document the mechanism you expect and what would disconfirm it.
3. **Specify before authoring.** Define the ordinary relationship, candidate deviation, semantic reliability, allowed player responses and accessible alternatives. Do not impose an arbitrary preparation duration or number of layers.
4. **Prototype only after separate authorization.** Use a matched A–B comparison and the justified C alternative below. Log differences rather than attributing all effects to context.
5. **Evaluate and revise.** Keep experience, information access and sensory comfort outcomes separate. Narrow, remove or replace the recipe when it adds cost without relevant value.

This process is proposed research-to-design guidance; only public-source research and Markdown specifications occurred here. [C-15, C-16, C-17]

## Patterns and genre adaptations

The only pattern candidate is [Contextual audio anomaly — GDK-PAT-0001, draft 0.1.0](../patterns/contextual-audio-anomaly.md). It turns the hypothesis into adjustable steps and explicit exits; it is not independent corroboration of this topic.

**Illustrative adaptations, not genre research:** A horror-oriented experience may intentionally preserve uncertainty about a sound’s cause, while a precision task may require a reliable explicit warning. Exploration focused on understanding a place may benefit from letting a changed sound remain investigable rather than immediately escalating danger. A comfort-oriented promise may favor an ordinary explanation or no anomaly. In a hybrid, state which promise controls the particular scene; do not assume every player sharing a genre label wants the same tension. [C-12, C-15, C-17]

No genre files are produced or linked. `related_genres: []` preserves the future separate, one-file-per-genre design. No missing neighboring topics are represented as existing knowledge. [C-16]

## Examples and counterexamples

**Creator-reported context, not directly observed gameplay:** Justice describes SOMA’s differentiated soundscapes and intended grounded corridor unease. Dang and Schumann describe a separate VR production using sparser exploration audio. These establish that creators report different context/density choices, not which choice caused an emotion. Their relevant facts and limitations are in C-09/C-10 and the full references. Neither account is a controlled A–B game comparison. [C-09, C-10]

**Illustrative worked situation — a maintenance passage:** A player is waiting for a door diagnostic while a nearby mechanism cycles normally. Later, a cycle ends with an unfamiliar scrape from beyond the door. The intended interpretation is “something changed; I can check, wait, or leave,” not “an enemy is definitely there.” A readable status indicator and configurable caption preserve the information that an unexplained event occurred. The ordinary sound, event timing and interpretation are design variables; no particular number of repetitions is guaranteed to teach the context. Nothing in this example was implemented or tested. [C-01, C-12, C-13, C-15]

**Illustrative do-not-use case:** During a time-sensitive navigation task, the same sound is the sole signal of a route hazard. Keeping its importance obscure in order to produce unease undermines the task contract. Prefer an explicit accessible warning, or remove the staged anomaly. This is a design countercase, not an observed test result. [C-12, C-15, C-17]

**Empirical boundary case:** SRC-0004 reports suspense in an audio-only film condition without the visual story cues; it did not operationalize or require the seed’s ambient/familiar/anomaly stages. This challenges an unrestricted necessity account. However, its full audio track, musical expectations and relaxation baseline prevent describing it as a context-free isolated-sound experiment. [C-02, C-06]

## Failure modes and constraints

| Observable warning sign for later evaluation | Competing explanation | Proposed correction, not a tested result |
| --- | --- | --- |
| Player hears an event but cannot say what changed. | No recognized baseline, unfamiliar source, or excessive density. | Simplify the baseline or use a legible cue; do not just extend exposure. |
| Immediate flinch, no subsequent anticipation. | Abrupt acoustic contrast rather than the proposed semantic mechanism. | Recheck matched cue properties and aftermath measures; reject the mechanism claim if needed. |
| Player predicts certain threat after every decorative anomaly. | Learned signal mapping differs from the intended uncertainty. | Separate required warnings from optional texture; document reliability rather than endlessly randomizing. |
| Correct recognition but irrelevant waiting or searching. | Ambiguity concerns the task instead of the outcome. | Clarify available actions and consequences. |
| Repeat exposure produces fast, competent response with lower unease. | Learning may have replaced uncertainty; lower tension is not necessarily a design failure. | Decide whether the scene should now support mastery rather than restore fear. |
| Important cue or assistive speech is missed. | Competing sound, settings, device limitations, caption timing, or attention demands. | Reduce nonessential sound and verify information access at the player’s chosen settings. |
| Discomfort, avoidance of settings, or withdrawal. | The intensity or intended experience is unwelcome. | Stop, offer adjustment/exit, and treat comfort failure as substantive rather than a player deficit. |

The observable signs and proposed repairs above remain hypotheses; the access concerns have adjacent official guidance, not pilot outcome data. [C-03, C-04, C-11, C-13, C-15]

**Access:** plan captions or other non-audio information channels for relevant events; preserve uncertainty only where it does not withhold required facts. Offer category controls and accommodate mono use. A player turning ambience down must not unknowingly lose a critical cue categorized as decorative audio. Test caption availability and semantic specificity; do not equate a silent run by a hearing reviewer with evaluation by people who rely on captions. [C-04, C-08, C-11, C-12]

**Cost:** contextual dependencies add work beyond recording one sound: authoring ordinary states, transitions, legitimate exceptions, retriggers/reloads, alternative-modality content, localization, and tests across settings and repeated exposure. These are conceptual cost categories, not measured estimates or middleware instructions. Reuse a coherent existing context before proposing more assets. No universal asset count, decibel setting, timing window, budget or staffing level is supported. [C-14, C-17]

## Playtest and validation

**Status: PROPOSED — NOT RUN.** No participant recruitment, consent collection, prototype, audio rendering, playtest, or statistical reanalysis was performed. The following plan requires a later authorized study design review; its sample and thresholds are proposals, not studio-approved standards. [C-15, C-16]

### Question, conditions and controls

**Primary question:** Does locally recognized context increase anticipation after a matched deviation, without unacceptable comprehension, agency, or comfort costs?

| Condition | Proposed manipulation | Interpretation boundary |
| --- | --- | --- |
| A — recognized context + deviation | Present a coherent ordinary relationship during a task, then a deviation. Measure whether the player actually recognized that relationship. | Assignment to A does not establish successful learning. |
| B — matched isolated deviation | Present the identical target waveform at the same task point, without establishing A’s predictive relationship. Use an equal-duration, non-predictive history from matched materials rather than an obviously impoverished scene. | “Isolated” means without that local learned relationship, not devoid of all lifelong context. B can develop its own expectations. |
| C — overt warning | At the same event point, communicate the same minimum state facts through a recognizable explicit warning, retaining comparable scene, task and threat behavior. | A decision alternative, not a pure context ablation; semantic explicitness necessarily differs. |

Use the same scene geometry, player objective, available actions, actual threat schedule and consequences. In A/B, retain the identical event waveform, position, onset, duration and event-time background where feasible; match overall exposure and baseline material amounts. Deliberately vary only the predictive relationship in the earlier history. Document remaining acoustic and attentional differences, including onset contrast, spectral overlap, music, spatial processing and perceived loudness. Matching digital amplitude alone does not establish perceptual matching; no matching was actually measured here. [C-01, C-15]

A/B is sufficient for the bounded conditional hypothesis; C tests whether the extra ambiguity is worth choosing at all. Do not add a silence condition simply to create another pattern. A later omission comparison is justified only when the team’s actual decision concerns a missing expected event. [C-13, C-15, C-17]

### Participants, exposure and procedure

**Proposed formative allocation:** 18 adult sessions for A/B/C, three allocations per each of the six possible condition orders. This is an order-coverage and workload rationale, **not a power calculation** or population guarantee. Plan a separate six-session access-focused review with people who actually rely on captions/visual cues, one allocation per order. Its purpose is finding information failures, not proving equivalence across disabilities. These are prospective slots, not recruited participants. [C-15]

Before recruitment, the later study owner must confirm resources, inclusion criteria, accommodations, cue/task tolerances and analysis rules. A confirmatory sample cannot be justified from this literature alone: first obtain local variability or a defensible prior estimate and choose a precision/power target before collecting confirmatory data. Failure to resource relevant access evaluation means restricting the conclusion, not claiming representative coverage. [C-15]

Use distinct matched cue families to reduce A-to-B learning transfer, counterbalancing family-to-condition mapping and first order. Present initial exposure and a later repeat separately; retain each exposure label in analysis. A neutral baseline-recognition check uses the same prompt in all conditions; record its potential to prime attention. Reject a “context mechanism” interpretation when that check fails to distinguish A from B. Collect prior sound familiarity, relevant play experience and any inference about the experimental purpose. [C-13, C-15]

Record usual device, volume, room noise, input and access settings. Divide the proposed main sessions between headphone and speaker contexts where feasible, reporting those contexts descriptively rather than claiming a powered device comparison. Do not add environmental noise or defeat hearing aids to simulate disability. Access-focused sessions use the person’s preferred reading/display settings and available non-audio information. A later low-volume, mono or sound-off verification is a distinct information-access check, not proof of emotional equivalence. [C-04, C-15]

### Separate measures

Use proposed, locally worded 0–6 response scales with explicit endpoints. The numbers are practical proposed settings, not validated norms. After each scene, ask separately about: anticipation of what might happen next; unease; surprise at the cue; reflex-like startle; confusion; perceived threat; fear; comfort; and sense of meaningful choice. Do not create a single “fear score” by combining these. Ask what happened, what remained unknown, which actions were available, and why the participant chose their action. [C-15]

The primary experience measure concerns the proposed **2–12 seconds after the event**, before any designed outcome reveal; a separate item addresses the immediate onset. These windows are local protocol proposals, not perceptual laws. Later preflight must ensure the task and threat schedule actually leave the window interpretable. If movement or early discovery changes it, log and analyze that difference rather than silently deleting the trial. [C-15]

Pair reports with predefined behavioral observations: task-fact accuracy, an inappropriate action traceable to misunderstood information, orienting or checking behavior, wait/withdraw choice, and completion. None alone directly measures fear. There is no physiological measure in the proposed formative protocol; adding one would require a justified, separately reviewed protocol and must not be called an objective fear meter. [C-06, C-15]

### Proposed local decision rules, frozen before any future execution

**Advance only as a candidate for further testing:** A shows at least a one-point median paired advantage over B on the 0–6 aftermath-anticipation item, with the same directional advantage on repeat exposure, successful baseline recognition, and no meaningful task, comfort or agency failure. This is a resource-allocation heuristic, not statistical proof; report all individual paired results and uncertainty, not just the median. Unease is secondary and cannot substitute for a failed anticipation result. [C-15]

**Reject or narrow:** prefer the simpler alternative when the proposed added-value threshold is not met; label an inconclusive small-sample result as inconclusive rather than equivalence. Reject the proposed mechanism if the difference is attributable only to onset startle/loudness or if A did not establish recognition. Restrict to first exposure if repeat value disappears. A one-point median reduction in comfort or agency, or any critical task-information failure, triggers revision and blocks advancement of that version. Any distress or request to stop ends that session immediately regardless of aggregated scores. [C-15]

**Access criterion:** every predeclared essential task fact must be available without sound. A critical fact unavailable in an alternative modality is a design failure even when aggregate tension rises. Observed availability is not population-level usability or emotional-equivalence evidence; actual access participants must still be able to interpret it. [C-04, C-12, C-15]

Obtain informed consent, describe the possibility of uncertain-threat audio without revealing the hypotheses, permit adjustable intensity and pauses, and provide withdrawal without penalty. Do not test an intensity a participant declines. Do not label stop requests or accessibility barriers as inconvenient outliers. No pilot study is implied by the specificity of this specification. [C-15, C-16]

## Claim ledger

Claim classes are separate from confidence. Confidence concerns the exact wording and scope, not the prestige of a source. Support below is direct only where stated. Original C-01 through C-04 remain hypotheses; no proposition has been silently upgraded.

### C-01

**Claim:** Recognizable context may add anticipation/unease beyond a matched isolated cue. **Class:** `hypothesis`. **Confidence:** low: no inspected study directly compares those gameplay conditions. **Support:** SRC-0002, Results → Behavioral data, is indirect detection evidence; SRC-0003, opening soundscape paragraphs, is production rationale. **Opposition/limits:** SRC-0006’s quiet-moments answer supports considering less sound, not the exact opposite causal comparison. **Applicability:** bounded exploration/waiting only. **Unresolved:** whether recognition changes aftermath anticipation once acoustics, task and threat are comparable.

### C-02

**Claim:** The seed’s three-stage sequence is not necessary for audio-related tension. **Class:** `hypothesis`, retained from the brief. **Confidence:** low for the bounded game proposition. **Support:** SRC-0004, Results → Differences between conditions and plot segments and Conclusions and limitations, provides a boundary challenge to an unrestricted necessity account. **Limits:** film, whole audio track, prior expectations and a relaxation baseline; not a clean interactive falsification. **Unresolved:** operational definition of “three stages” in the uninspected graphic. **Conflict:** `CON-0001`; do not use the unsupported universal as a rule while this remains unresolved.

### C-03

**Claim:** Repeated exposure may change interpretation or tension effects of a cue in the bounded gameplay context. **Class:** `hypothesis`. **Confidence:** low for game-cue transfer; see C-07 for measured adjacent results. **Support:** SRC-0008, Methods and Results, is film evidence. **Limits:** does not isolate cue familiarity, learned reliability or gameplay mastery. **Unresolved:** whether reduced unease accompanies improved comprehension, indifference, or unchanged engagement.

### C-04

**Claim:** An alternative modality may preserve task information while changing emotional experience. **Class:** `hypothesis`. **Confidence:** low for a particular implementation’s outcome. **Support:** SRC-0005/SRC-0007 recommend access; they do not test this affective comparison. **Applicability:** captions/visual or other accessible equivalents appropriate to the required facts. **Unresolved:** both actual information usability and the direction, size or absence of emotional differences. No emotional-equivalence claim is made.

### C-05

**Claim:** In an artificial auditory-scene task, regular backgrounds improved detection of an appearing source relative to random backgrounds. **Class:** `empirical-evidence`. **Confidence:** moderate, narrow original experiment. **Study:** SRC-0002; 13 active and 14 passive listeners, self-reported normal hearing; concurrent tone streams, active detection or an unrelated visual task, with MEG. **Outcome:** active detection accuracy and speed favored regular scenes (reported p<.001 and p<.01). **Locators:** Results → Behavioral data; Materials and methods → Participants/Stimuli/Procedure. **Limits:** detection, not tension, threat meaning or no-context comparison; no reanalysis or direct replication inspected. **Unresolved:** ecological and affective transfer.

### C-06

**Claim:** A film’s audio-only presentation supported reported suspense without visual story cues; subjective and physiological measures did not align uniformly. **Class:** `empirical-evidence`. **Confidence:** moderate for this stimulus. **Study:** SRC-0004; 105 US university students, randomized to audiovisual, audio-only or video-only Love Field; continuous nine-point suspense ratings and pulse/skin-conductance measures. **Locators:** Method; Results → Differences between conditions and plot segments; Discussion → Self-reported suspense (CRM). **Limits:** music plus effects, common baseline, one film, possible genre-judgment demand; framewise tests uncorrected. **Unresolved:** genuine felt anticipation versus rating conventions and transfer to interaction. The study did not test the present recipe.

### C-07

**Claim:** Repeated suspenseful film segments showed reduced suspense reports initially, without establishing disappearance of suspense or equivalence of enjoyment. **Class:** `empirical-evidence`. **Confidence:** moderate, with reporting caveat. **Study:** SRC-0008; 50 Korean university students recruited, one reported exclusion; repeated running segments with changing endings, two instruction groups, self-report/SCL/ECG. **Outcome:** nine-point suspense means (SD) 6.80 (1.59) → 5.08 (2.22) → 4.69 (2.08); first–second difference significant, second–third not; enjoyment change not significant. **Locators:** Materials and Methods; Results opening paragraphs; Tables 1–2. **Limits:** nonidentical endings; self-report degrees of freedom and stated analysis n are not reconciled here. **Unresolved:** applicability to repeated game cues, not elimination or unchanged enjoyment.

### C-08

**Claim:** XAG 104 recommends captions for important non-speech sounds not otherwise communicated visually, including relevant direction. **Class:** `practitioner-heuristic` (official vendor guidance). **Confidence:** high that the inspected document recommends this; effectiveness in this pattern untested. **Source/locator:** SRC-0005, Goal and Implementation guidelines. **Limits:** not classified as a formal standard or certification obligation; no emotional comparison. **Unresolved:** wording and presentation appropriate to the actual task and audience.

### C-09

**Claim:** SOMA’s audio director reports designing contrasting, grounded soundscapes and intending distant ambiguous sounds to retain plausibility. **Class:** `practitioner-heuristic`. **Confidence:** moderate as a firsthand account; causal efficacy unknown. **Source/locator:** SRC-0003, opening soundscape and Upsilon paragraphs. **Applicability:** one production’s design intent. **Limits:** not a directly observed sequence or participant finding. **Unresolved:** whether the intended response occurred, for whom, and because of which feature.

### C-10

**Claim:** Rogue Incursion’s creators report reducing ambience during exploration to clarify important sounds and preserve contrast. **Class:** `practitioner-heuristic`. **Confidence:** moderate as a named creator account. **Source/locator:** SRC-0006, GES-facility answer and quiet-exploration answer. **Applicability:** an independent VR action-horror production context. **Limits:** claims of elevated heart rate are not measured results; not evidence that less sound always works. **Unresolved:** comparative efficacy and non-VR transfer.

### C-11

**Claim:** XAG 105 recommends independent audio-category controls, mono conversion and protecting assistive speech from competing game audio. **Class:** `practitioner-heuristic` (official vendor guidance). **Confidence:** high for accurate attribution. **Source/locator:** SRC-0007, Goal, Overview and Implementation guidelines. **Applicability:** access-oriented options, checked against the later project’s actual needs. **Limits:** no formal-standard or quantitative mixing claim. **Unresolved:** whether a proposed configuration preserves the required cues.

### C-12

**Claim:** Separate optional uncertainty about cause/outcome from access to required task information. **Class:** `inference`. **Confidence:** moderate: derived from C-08/C-11 and the task contract, not an ambiguity experiment. **Sources/locators:** SRC-0005, important-sound captions; SRC-0007, Overview. **Reasoning:** players cannot exercise a required choice on information they cannot obtain. **Limits:** optimal ambiguity and caption specificity depend on context. **Unresolved:** whether added explicitness changes desirable anticipation.

### C-13

**Claim:** Familiarity and learned reliability may alter anomaly interpretation; an omission cue requires an expected event to be missing. **Class:** `hypothesis`. **Confidence:** low for the gameplay effect. **Support:** SRC-0002 and SRC-0008 are adjacent evidence only; omission’s expectation requirement is the local operational definition. **Limits:** no inspected probability/reliability manipulation in this game context. **Unresolved:** first versus practiced play, culturally different meanings, and when an absence is noticed rather than ignored.

### C-14

**Claim:** Contextual dependencies create authoring and verification work beyond a standalone asset, without implying a universal cost. **Class:** `inference`. **Confidence:** moderate for the identified work categories, low for any unmeasured magnitude. **Sources/locators:** SRC-0003, final integration discussion; SRC-0006, implementation and mixing answers. **Reasoning:** each meaningful state/exception and access equivalent must be authored and checked. **Limits:** no engine benchmark, staffing estimate or cost model. **Unresolved:** marginal effort for an actual approved project.

### C-15

**Claim:** The definitions, illustrative cases, procedures, sample allocations and thresholds in this draft are proposals suitable for challenge, not validated instruments or approved study settings. **Class:** `hypothesis`. **Confidence:** low regarding their eventual usefulness and sensitivity. **Source:** original pilot synthesis under the user’s brief, sections 2 and 7; no empirical result supports the chosen local thresholds. **Limits:** all participant work and technical checks described there are NOT RUN. **Unresolved:** later study-owner review, feasibility, variance and measurement validity.

### C-16

**Claim:** Doug authorized this bounded public-source research and three draft Markdown outputs, excluding implementation, uploads, participant work and release. **Class:** `studio-decision`. **Confidence:** high; explicit current user instruction and supplied coordination brief, sections 1, 4, 7–8, dated 2026-10-10. **Owner:** Doug. **Scope:** this research session only. **Limits:** not completed-pilot acceptance, taxonomy-wide approval, global ID reservation or runtime-model certification. **Unresolved:** later review decisions.

### C-17

**Claim:** Do not mandate the three-stage seed; compare the least complex candidate that satisfies the intended experience and task/access contract. **Class:** `inference`. **Confidence:** moderate as evidence-calibrated decision guidance, not demonstrated effectiveness. **Support:** C-01–C-14; particularly SRC-0002, Results → Behavioral data; SRC-0004, Conclusions and limitations; SRC-0006, quiet-exploration answer. **Limits:** lack of support is not universal disproof. **Unresolved:** local comparative value. Adoption and implementation remain separately gated.

## References

All IDs are provisional administrative proposals. Complete records are repeated where needed so neither this entry nor its pattern depends on the review packet for provenance. Repetition is not corroboration. No original graphic, game audio recording or player study was inspected as an observed-game dataset.

### SRC-0001

**Provisional identity; not globally reserved.** Unknown. Unattributed audio graphic / vendor-email lead (administrative description, not a verified original title); verified original URL/DOI: unknown. Unknown. **Publication/update:** Unknown. **Edition/build:** Unknown.

**Access:** lead-only; checked 2026-10-10. **Source type:** Uninspected graphic/email lead. **Exact locators:** No original passage inspected. The starter specification, lines 16–22, and REGISTERS.md, line 15, describe this lead. **Entry claims:** None; lead-only context for C-02 / CON-0001.

**Limits:** Supports no substantive audio claim. The starter’s statement that someone visually inspected the graphic is not an observation performed in this chat. **Relationships:** One unresolved lead inherited from the starter, not a public-source evidence record. **Rights:** Unknown; original image and email were not obtained or redistributed.

### SRC-0002

**Provisional identity; not globally reserved.** Ediz Sohoglu and Maria Chait. [Detecting and representing predictable structure during auditory scene analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC5014546/); [DOI](https://doi.org/10.7554/eLife.19113). eLife, volume 5, article e19113; inspected through the NCBI PMC full-text mirror. **Publication/update:** 2016-09-07. **Edition/build:** Published article, DOI 10.7554/eLife.19113.

**Access:** relevant-excerpt; checked 2026-10-10. **Source type:** Original human psychophysics / magnetoencephalography study. **Exact locators:** Results → Behavioral data, first two paragraphs; Materials and methods → Participants, Stimuli, Procedure; Discussion → Adaptation versus precision. HTML text inspected; no PDF used. **Entry claims:** C-05 directly; C-01/C-13/C-17 indirectly.

**Limits:** Artificial tone-stream detection, not semantic threat, game tension, or an isolated-cue comparison. Small, self-reported-normal-hearing sample. Study methods/outcomes are specified in the empirical claim record. **Relationships:** Original study; eLife and PMC are two access routes to the same work, not corroboration. **Rights:** Creative Commons Attribution license stated by the article; no figures or stimulus files reproduced.

### SRC-0003

**Provisional identity; not globally reserved.** Samuel Justice, SOMA audio director; embedded contribution from Kpow Audio. [SOMA – Behind The Sound](https://frictionalgames.com/2015-09-soma-behind-the-sound/). Frictional Games. **Publication/update:** 2015-09-17; page also displays 2023-10-10, with the substance of that update unknown. **Edition/build:** Developer article; game platform/build unknown for the described examples.

**Access:** relevant-excerpt; checked 2026-10-10. **Source type:** Firsthand development account. **Exact locators:** Opening paragraphs beginning “For those of you who don’t know” through the Upsilon corridor example; final Kpow integration paragraphs and closing production paragraph. Browser text lines 13–18, 54–61. **Entry claims:** C-09; production basis for C-01/C-14.

**Limits:** Reported intentions and production choices, not controlled player-response data or an independently observed build. Embedded audio/video not played. **Relationships:** One production context, including its contractor account; not multiple independent efficacy studies. **Rights:** Reuse license not established in inspected text. Paraphrase only; no audio, screenshots, or images reproduced.

### SRC-0004

**Provisional identity; not globally reserved.** Gary Bente, Kevin Kryston, Nolan T. Jahn, and Ralf Schmälzle. [Building blocks of suspense: subjective and physiological effects of narrative content and film music](https://www.nature.com/articles/s41599-022-01461-5); [DOI](https://doi.org/10.1057/s41599-022-01461-5); [inspected public HTML route](https://www.nature.com/articles/s41599-022-01461-5?code=research&error=cookies_not_supported). Humanities and Social Sciences Communications, volume 9, article 449, Springer Nature. **Publication/update:** 2022-12-13. **Edition/build:** Version of record, DOI 10.1057/s41599-022-01461-5.

**Access:** relevant-excerpt; checked 2026-10-10. **Source type:** Original human film-response experiment. **Exact locators:** Method → Participants, Stimulus material, Audience response measures, Procedure; Results → Differences between conditions and plot segments; Discussion → Self-reported suspense (CRM); Conclusions and limitations. HTML text inspected, including figure captions; plots were not digitized. **Entry claims:** C-06; boundary/measurement support for C-02/C-17.

**Limits:** One film and a student sample; audio track included music AND sound effects, not isolated music throughout. Common relaxation baseline. Self-report instruction may cue genre judgments. Framewise comparisons are reported as uncorrected; no new analysis or multiplicity correction performed. **Relationships:** Distinct dataset from SRC-0008, which this paper cites. Coauthor Schmälzle is named in SRC-0008’s reviewer footer; these are not wholly disconnected intellectual lines. Publisher HTML succeeded with the public query ?code=research&error=cookies_not_supported; normal route and PDF attempts failed. **Rights:** CC BY 4.0 stated in Rights and permissions; no film, figures, or supplementary media reproduced.

### SRC-0005

**Provisional identity; not globally reserved.** Microsoft. [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication date unknown. **Edition/build:** Unnumbered live web revision inspected 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal; Overview; Implementation guidelines → important non-speech sounds and spatial indication, availability before play, configurable caption categories. Browser text lines 31–39, 64–96; update line 188. **Entry claims:** C-08; indirect C-04/C-12.

**Limits:** Classified here as practitioner-heuristic, not a formal standard or a certification requirement. Recommends information access, not demonstrated emotional equivalence. Linked normative/technical documents and examples were not independently verified. **Relationships:** Related to SRC-0007 and issued by the same organization; not independent evidence of player outcomes. **Rights:** Microsoft page; a content reuse license was not inspected. Paraphrase only; no screenshots reproduced.

### SRC-0006

**Provisional identity; not globally reserved.** Jennifer Walden, interviewer; Chris Dang, Survios Head of Audio Department, and Tim Schumann, Senior Technical Sound Designer, interviewees. [Crafting Immersive Audio for Action-horror VR game Alien: Rogue Incursion – with Chris Dang and Tim Schumann](https://www.asoundeffect.com/alien-rogue-incursion-vr-game-audio/). A Sound Effect. **Publication/update:** 2025-02-26; subsequent update date unknown. **Edition/build:** Published interview; described game build and recording date unknown.

**Access:** relevant-excerpt; checked 2026-10-10. **Source type:** Firsthand creator interview in an industry publication. **Exact locators:** Questions on the GES facility, scaring players, implementation, mixing, and “What about quiet, exploration-focused moments …”; particularly the final answer about removing ambience. Browser text lines 248–253, 368–371, 384–395, 408–413. **Entry claims:** C-10; indirect C-14/C-17.

**Limits:** VR action-horror production account, not measured causality. Claims about heart rate are interview rhetoric, not a reported physiological study. Hardware/platform wording is historical interview context, not a current product assertion. **Relationships:** Survios is a separate production context from Frictional’s SOMA. Shared horror-selection bias remains. The publication also sells audio products; no product recommendation is made. **Rights:** Reuse license not established in inspected text. Paraphrase only; no trailer, images, or assets reproduced.

### SRC-0007

**Provisional identity; not globally reserved.** Microsoft. [Xbox Accessibility Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105). Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication date unknown. **Edition/build:** Unnumbered live web revision inspected 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal; Overview; Implementation guidelines → independently adjustable audio types, stereo-to-mono option, and lowering game audio during assistive-technology speech. Browser text lines 31–38, 47–61, 78–81, 102; update line 143. **Entry claims:** C-11; indirect C-04/C-12.

**Limits:** Not treated as a formal standard, legal mandate, or evidence that a particular mix is accessible. No numerical mix or safe-listening threshold is extracted. **Relationships:** Same issuer as SRC-0005, different document. New snapshot-scoped allocation proposal beyond the brief’s initial slots; Coordination reconciliation required. **Rights:** Microsoft page; a content reuse license was not inspected. Paraphrase only; no screenshots reproduced.

### SRC-0008

**Provisional identity; not globally reserved.** Changui Chun, Byungho Park, and Chungkon Shi. [Re-Living Suspense: Emotional and Cognitive Responses During Repeated Exposure to Suspenseful Film](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.558234/full); [DOI](https://doi.org/10.3389/fpsyg.2020.558234). Frontiers in Psychology, volume 11, article 558234. **Publication/update:** 2020-10-23. **Edition/build:** Published article, DOI 10.3389/fpsyg.2020.558234.

**Access:** relevant-excerpt; checked 2026-10-10. **Source type:** Original human repeated-film-exposure experiment. **Exact locators:** Materials and Methods → Stimuli, Dependent Measures, Participants, Procedure, Data Analysis; Results, first five paragraphs; Tables 1–2 in HTML; Discussion, opening paragraphs and limitations. Browser text lines 436–490, 493–529, 548–571, 597–601. **Entry claims:** C-07; indirect C-03/C-13.

**Limits:** Repeated first halves had different endings and instruction groups; not a clean repeat of an identical whole experience and not a game-audio ablation. Authors report 50 recruited, one exclusion, analysis n=49; reported self-report degrees of freedom are not fully reconciled with that statement. No raw-data audit performed. **Relationships:** Separate authors and cohort from SRC-0004; SRC-0004 cites this work and one of its authors is named in the reviewer footer here. New allocation proposal requiring Coordination reconciliation. **Rights:** CC BY stated in the article’s Copyright section. No film clips or figures reproduced.


## Open questions and change history

**Open:** the exact A–B game comparison; semantic familiarity versus temporal regularity; cue reliability learning; omission versus playback-failure interpretations; affect across access modes; wider populations/devices; direct gameplay observation; actual authoring cost. These gaps limit the recommendation rather than becoming invented findings.

**CON-0001:** retained as an unsupported necessity proposition with unresolved original provenance and bounded falsification; see the [review packet assessment](../pilots/audio-tension-and-ambience-review-packet.md#con-0001-assessment).

**History, 2026-10-10, version 0.1.0:** initial bounded candidate; seeded hypotheses retained; three empirical records, two production accounts and two vendor-guidance records inspected in relevant public HTML passages. No move to `in-review` or `released`. Same-session, non-independent content review is reported in the packet; formal reviewer/approval fields remain null.

**Handoff:** this topic and its single pattern are artifacts for Coordination review. Evidence is indirect for the main recipe; host validation and human acceptance remain outstanding. Next decision: whether to revise these drafts or proceed to allocation reconciliation and separately authorized host validation, before Doug’s completed-pilot acceptance decision.
