---
id: GDR-CAND-20261010-P05-TOP-02
kind: topic
title: Music design
version: 0.1.0
candidate_revision: initial-author-draft
status: draft
run_id: GDR-FULL-20261010
batch_key: P05
attempt_id: P05-authoring-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: coverage-open
aliases:
- adaptive score decisions
- musical transitions and interpretation
tags:
- presentation
- research-candidate
- coverage-open
related_topics:
- GDR-CAND-20261010-P05-TOP-01
- GDR-CAND-20261010-P05-TOP-03
related_patterns:
- GDR-CAND-20261010-P05-PAT-01
related_genres: []
dependency_ids:
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-F01-PAT-01
source_ids:
- GDR-SRC-20261010-P05-001
- GDR-SRC-20261010-P05-004
- GDR-SRC-20261010-P05-005
- GDR-SRC-20261010-P05-006
- GDR-SRC-20261010-P05-011
- SRC-0005
- SRC-0007
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: []
change_summary: Initial P05 author draft; no previous batch, pilot, source or canonical
  file replaced.
byte_hash_record: ../reviews/full-run-20261010-p05-review-packet.md#candidate-byte-receipt
---

# Music design

**Draft research candidate — coverage open; no released score recipe.** The central decision is not how much music to add, but what musical organization contributes to a particular task or expression, and what it costs in responsiveness, attention, meaning and production. [C-08, C-12]

## Decision and scope

**Decision:** Choose among authored scoring, adaptive combinations, transition rules, motifs, player-linked performance and deliberate absence of music without equating a game-state variable with the player’s emotion.

This entry covers adaptive structure, motifs, transitions, rhythm, silence and emotional interpretation. General mixing/spatial presentation belongs to [Audio design](audio-design.md); translated lyrics, captions and voice/context issues belong to [Localization and presentation](localization-and-presentation.md). It does not survey all music theory, prescribe a middleware, compose a soundtrack, or replace genre research. [C-01, C-08, C-11, C-12]

**Working terms:** An *authored sequence* has a composed progression whose order is largely fixed for a defined use. *Vertical adaptation* changes simultaneous musical components; *horizontal adaptation* changes sequential segments. A *motif* is a recurring identifiable musical idea; its intended association is a separate design claim. *Player-linked performance* makes musical action or its timing part of what the player controls. *Silence* here means an intentional absence of score, not necessarily absence of environmental sound, essential feedback or assistive speech. These are analytic conventions for this draft. [C-07, C-08, C-11]

A future application must state whether music is optional, task-bearing or itself the action; audience familiarity and linguistic/cultural context; device/room and chosen levels; hearing and other access needs; input method; pause/re-entry rules; platform/build; and viewing context. No keyboard/controller timing, beats-per-minute range or emotional response is assumed universal. [C-06, C-09, C-11]

## Core explanation and mechanisms

### Three different propositions

A system may **implement** a response to a timer. A composer may **intend** that response to convey pressure. A player may **report** feeling calm, tense, distracted or nothing in particular. These propositions require different evidence. Game variables can control musical presentation without being valid sensors of the player’s state. [C-01, C-04]

The conditional mechanism proposed here is: a musical choice becomes perceivable in context → a listener interprets it through the task and prior experience → that interpretation may change experience or action. The evidence below concerns particular links and comparisons, not a validated complete chain for all games. [C-01–C-03, C-08]

### Original interactive evidence and its strongest limitation

Plut and Pasquier studied **30 analyzed participants** after five incomplete remote submissions were excluded from 35 recruited. Participants encountered four conditions in randomized order in *Galactic Escape*: no score, static-neutral, inverse-adaptive and congruent-adaptive music. The task used pursuit/timer pressure and stochastic outcomes; musical materials differed. Responses were self-reported using a modified instrument. [C-02; GDR-SRC-20261010-P05-005]

For reported tension, the paper gives **F(3,87)=3.662, p=.015, partial η²=.112**. Its reported pairwise findings favor inverse and congruent adaptation over static-neutral music (**p=.048** and **p=.036**). They do **not** establish congruent-over-inverse or congruent-over-no-music superiority. The conclusion is broader than those reported comparisons. Small mixed testing contexts, composition differences, instrument modification and unverified game/music-tension constructs limit transfer; no reanalysis was performed. This is a reason to test adaptivity, not mandate emotional matching. [C-02; GDR-SRC-20261010-P05-005]

### Cultural interpretation is neither arbitrary nor a universal lookup table

Cowen and colleagues report shared dimensions in responses to brief musical excerpts across US and Chinese samples. Experiment 1 reports 1,011 US and 895 Chinese raters; Experiment 2 reports 580 and 363. The Methods section’s combined total is inconsistent with its country counts; P05 preserves that reporting gap rather than inventing a corrected study total. [C-03; GDR-SRC-20261010-P05-006]

The authors explicitly leave within-country variation, prior exposure, longer musical experience and the distinction between perceived and experienced emotion unresolved. Their design is not gameplay, and shared associations do not establish an innate emotion dictionary. Ask separately what the music seems to express and what the player actually experiences. Neither a national label nor a mode/tempo label certifies a response. [C-03]

### Structure should answer a decision, not demonstrate a feature

Use an authored arc when preserving a specific expressive progression matters more than frequent state response. Use adaptive combinations when actual state differences warrant different musical organization, and the alternatives can remain compositionally and semantically coherent. Use player-linked performance when timing, agency or creating sound is itself the activity. Consider no score when listening to the environment, reading, rest or another expressive element is the priority. These are selection inferences, not rankings from the studies. [C-06, C-08, C-09]

Supergiant’s account of early musical work on Bastion offers a production example of using music while defining tone. It does not prove that an early soundtrack or one recognizable style improves every production. A small exploratory sketch may resolve an artistic question; producing a large reactive system before the question is clear may not. [C-05, C-08]

### Transitions have musical and state-validity constraints

Scheduling facilities can align playback with an audio clock, but they cannot decide whether a pending segment still describes the current situation. Waiting for a phrase boundary can preserve an intended musical relation while delaying or falsifying a state response. An immediate cut can be appropriate when responsiveness matters; an authored transition can be preferable when expression matters; silence can be an intentional resolution rather than a fault. [C-04, C-06, C-08]

The proposed [State-valid musical transition](../patterns/state-valid-musical-transition.md) separates request, pending choice, validity recheck, audible commitment and recovery. It is not a tested universal scheduler. Urgent task information should not wait solely for a musical boundary. Conversely, a player deliberately performing rhythm should not have their intended timing silently overwritten by a background-scoring rule. [C-06, C-09, C-10]

### Motifs and rhythm: preserve the unanswered questions

Define which feature makes a motif recognizable and what relationship, if any, it signals. Then test identity recognition independently from inference about a character, place or state. A repeated melodic idea can acquire different meanings in different scenes; forcing a single association may undermine deliberate ambiguity. No inspected source establishes a reliable number of repetitions for learning a motif. [C-07]

For rhythm, distinguish a perceptual/expressive pulse from a required action window. Player action, input processing and audio presentation are different events. P02’s reviewed input/feedback distinctions transfer, but no P05 latency, entrainment, tempo or timing-window experiment was performed. A music-driven task needs a separately reviewed timing/access specification; decorative scoring cannot justify silently changing its rules. [C-06, C-09, C-11]

## Design choices and alternatives

| Choice | Conditions worth considering | Costs, countercase and simpler option |
|---|---|---|
| Authored progression | A scene supports an intended arc without frequent state changes. | Can diverge from player pacing. Allow an appropriate stopping/re-entry policy or use fewer musical events. [C-06, C-08] |
| Adaptive layers | A real presentation distinction can be expressed by combinations of compatible parts. | Every meaningful combination needs review. More layers can add concurrency without useful state meaning. [C-08, C-11] |
| Segment transitions | Distinct states warrant distinct passages and transitions can remain valid. | Late/outdated arrivals, repeated entrances and abandoned transitions require handling. Compare a simpler continuous bed. [C-06, C-10] |
| Motif family | Recognition or an evolving relationship is an explicit goal. | Familiarity is not comprehension; repetition can be unwanted. Compare a non-motif treatment and unfamiliar listeners. [C-07] |
| Player-linked performance | The player is meant to create, align with or alter music. | Automatic smoothing can contradict agency. Treat latency and alternative inputs as task design, not scoring polish. [C-06, C-09] |
| No score / selective score | Another task or expression benefits from musical absence. | Absence may remove a learned required signal. Preserve the task contract; do not pretend muting proves equal emotion. [C-08, C-09] |

## Application process

1. **State the contribution.** Name the expression, knowledge or action music is meant to affect. Write separate measures for perceived expression, felt response, task comprehension and preference. [C-01–C-03]
2. **Classify its role.** Optional, informative, task-bearing or performative. Identify what must still work under player-selected settings and whether hidden information may be revealed. [C-09]
3. **Choose a modest structure.** Compare the intended authored option with one meaningfully different alternative; do not create an elaborate adaptive graph merely because the tools permit it. [C-04, C-08]
4. **Write transition contracts.** Specify request, valid source/destination, musical boundaries, allowed delay, preemption, cancellation, pause/re-entry and what happens if a request becomes false. Numerical values await a local approved specification. [C-06, C-10]
5. **Plan variants and maintenance.** Identify needed combinations, transitions, language/voice conflicts, settings, repeated-play contexts and resource/version dependencies. Stop expanding when those cannot be verified within scope. [C-08, C-11]
6. **Evaluate after separate authorization.** Prefer the simpler choice absent worthwhile demonstrated added value; preserve intentional differences and genuine uncertainty. [C-08, C-11, C-12]

## Patterns and genre adaptations

The distinct P05 pattern is [State-valid musical transition — GDR-CAND-20261010-P05-PAT-01](../patterns/state-valid-musical-transition.md), a hypothesis-led recipe. Motif-learning and musical-absence extensions are not silently counted as validated patterns; proposed next work is in the [queue](../reviews/full-run-20261010-p05-review-packet.md#queued-child-work).

These topics are genre-neutral. An exact rhythmic action, an open-ended exploration passage and a quiet reflective scene can impose different constraints even within one game. Specify the scene’s promise rather than infer that a genre “requires” continuous scoring or rising intensity. No genre file or universal preference has been established. [C-06–C-12]

## Examples and counterexamples

**Illustrative — changing inspection priorities.** A player investigates a remote station. A process becomes unstable, prompting a possible move from a sparse score to a more active arrangement. Before the chosen musical boundary, the player resolves the fault. A state-valid treatment drops the pending escalation and selects an appropriate continuation. An alternative simply uses a continuous authored passage; another omits music and retains the event information. The point is to compare truthful response, expression and cost, not assume an adaptive arrangement will feel more tense. [C-01, C-06, C-08, C-10, C-11]

**Strong counterexample.** In a scene where the player intentionally performs a held note across a change, switching automatically to match the game state can negate the performance. The correct alternative may be to respect the action and communicate state elsewhere. Likewise, ironic or contrasting music can be an intended artistic choice; “matching” must not erase that choice in the name of responsiveness. [C-06, C-08, C-09]

**Empirical counterpressure.** The inverse-adaptive condition is a genuine challenge to a simple congruence mandate. It is not proof that irony or inverse scoring is always better. [C-02]

## Failure modes and constraints

Potential failures include a motif interpreted as a guaranteed threat detector; an escalation arriving after a resolution; constant transitions where a stable passage would suffice; assistive speech competing with essential music; repeated entrances creating unwanted emphasis; and alternate settings removing the task’s only timing information. Investigate these as different problems rather than treating them all as inadequate intensity. [C-06–C-11]

Production review should cover compositional compatibility, usable transitions in both directions, partial/repeated states, buffering and memory constraints on the chosen target, voice/language conflicts, rights to recordings/compositions, and maintenance when gameplay changes. No asset count, staffing formula or royalty/cost advice is supported here. The current research authorizes none of those commitments. [C-08, C-11, C-12]

## Playtest and validation

**PROPOSED — NOT RUN.** No composition, rendering, game build, participant test, input timing measurement or physiological measurement was made. [C-11, C-12]

**Question:** Does the chosen organization add a worthwhile intended contribution over a credible authored or no-score alternative without information, agency or comfort loss? Separate a structure experiment from a congruence experiment. Use comparable musical materials and log differences in density, level, duration and orchestration; otherwise describe the result as a package comparison, not a pure adaptivity effect. [C-01–C-03, C-08, C-11]

**Protocol proposal:** Use matched task variants with counterbalanced musical order and multiple cue families. Include first/repeat exposure, state reversal before a scheduled transition, interruption by speech, pause/resume and a relevant player-controlled timing case. Record the event that requested a transition, the state when it became audible and why a request was canceled. Do not fix the actual gameplay outcome to an artificial value and then claim normal agency. [C-06, C-10, C-11]

**Participants:** Define intended listening devices, access needs, musical familiarity, languages/cultural context and input methods before recruitment. Include participants who use relevant access modes, rather than simulating their needs solely by muting sound. No sample-size guarantee is borrowed from the papers. A later study owner must justify resources, sample and any inferential analysis. [C-03, C-09, C-11]

**Measures and rejection:** Collect perceived musical expression, actual felt response, state comprehension, response/recovery, agency, comfort and preference separately. A score that is liked but communicates a false state fails that informational use. A delayed musical response that harms the player’s intentional performance fails that control contract. Reject claims of motif learning when an unseen probe changing the correct answer exposes mere answer repetition; preserve the F01 reviewed discrimination correction. Report uncertain/no-added-value findings without converting them into equivalence. Freeze locally meaningful benefit/cost margins before any test, and stop immediately on withdrawal or discomfort. [C-01–C-03, C-06–C-11]

## Coverage checkpoint

| Assigned facet | Researched here | Remaining discriminating question |
|---|---|---|
| Adaptive structure | One interactive study; documented scheduling; conditional comparisons. | Does matched content reproduce a useful adaptive benefit in the actual task? |
| Motifs | Explicit recognition/meaning hypothesis and production context. | Can a motif communicate intended relations on new cases without false prediction? No learning study inspected. |
| Transitions | Documentation capability and distinct state-validity pattern. | Does validity checking help enough to justify delay, cancellation and authoring cost? |
| Rhythm | Task-versus-decoration boundary and P02 transfer. | Target timing, entrainment and alternative-input evidence absent. |
| Silence | Serious no-score/selective-score alternatives. | When is absence useful rather than information loss? No local comparison run. |
| Emotional interpretation | Interactive and cross-cultural results with limits. | Actual audience, perceived versus felt response, long/repeat exposure and cultural variation remain open. |

All facets remain **coverage-open**. [C-01–C-12]

## Claim ledger

Claim identifiers are local to this entry. Confidence describes the exact scoped proposition, not the strength of the entire technique. Source recommendations, documentation behavior, measured responses and our proposals are not interchangeable.

### C-01

**Claim:** A gameplay variable can drive music without measuring the player’s felt emotion.

**Class:** `inference`. **Support and locator:** GDR-SRC-20261010-P05-005, §IV/§V mapping and §VIII limitations; GDR-SRC-20261010-P05-004, scheduling description.

**Applicability / opposition:** Bridge: distance/timer state and an audio scheduling clock are not a listener response measure. **Confidence:** High for the logical distinction, not a claim that state-driven music is ineffective. **Unresolved:** Which player-reported construct is the local intervention intended to change?

### C-02

**Claim:** In the inspected game experiment, both adaptive conditions had higher reported tension than the static-neutral condition in the reported pairwise tests.

**Class:** `empirical-evidence`. **Support and locator:** GDR-SRC-20261010-P05-005, §V–VI, Table VII and §VI-B p.7; study record in Core explanation.

**Applicability / opposition:** Not evidence that congruent adaptation beats inverse adaptation or no music; musical content and mapping both differed. **Confidence:** Moderate: original small experiment with narrow outcomes and reporting/analysis limitations. **Unresolved:** Would matched musical material and a preregistered contrast reproduce the result?

### C-03

**Claim:** The cross-cultural listening research reports shared response dimensions while leaving within-culture variation and perceived-versus-experienced distinctions unresolved.

**Class:** `empirical-evidence`. **Support and locator:** GDR-SRC-20261010-P05-006, Experiment 1 p.3; Experiment 2 p.7; Discussion pp.9–10; Methods p.10.

**Applicability / opposition:** Brief samples in US/China, not gameplay or universal emotional grammar. A total-count reporting inconsistency is not repaired by guesswork. **Confidence:** Moderate for the bounded published result; population and instrument transfer uncertain. **Unresolved:** How do intended audiences interpret the actual cue in its playable context?

### C-04

**Claim:** Unity documents music playback scheduling on a DSP timeline independently of frame rate.

**Class:** `observed-example`. **Support and locator:** GDR-SRC-20261010-P05-004, Parameters and Description.

**Applicability / opposition:** Capability, not seamless composition, target latency, state validity or user-input responsiveness. **Confidence:** High for documentation scope; runtime untested. **Unresolved:** What are the actual prepare/cancel/resume constraints of the eventual implementation?

### C-05

**Claim:** Supergiant reports using early musical work to help define Bastion’s tone.

**Class:** `practitioner-heuristic`. **Support and locator:** GDR-SRC-20261010-P05-011, Bastion FAQ soundtrack answer.

**Applicability / opposition:** One creator account; no comparative early/late music outcome. **Confidence:** Moderate for report, unknown causal production benefit. **Unresolved:** Does early music exploration usefully resolve the current art/experience decision?

### C-06

**Claim:** Musical continuity, truthful state response, timely information and player performance are separate transition goals that can conflict.

**Class:** `inference`. **Support and locator:** C-01/C-04; GDR-SRC-20261010-P05-001, snapshots/ducking; SRC-0007, assistive speech; reviewed P02 controls/feedback.

**Applicability / opposition:** A beat/phrase boundary is not automatically a permitted deadline; abrupt response can be intentional. **Confidence:** Moderate for conflict analysis; low for an optimal resolution rule. **Unresolved:** Which delay, cancellation or cut is least harmful in the actual task?

### C-07

**Claim:** A small motif family may support recognition, but repeated identity does not establish one fixed meaning or prevent fatigue.

**Class:** `hypothesis`. **Support and locator:** C-03/C-05 are contextual leads only; no matched motif-learning experiment inspected.

**Applicability / opposition:** Motif recognition, semantic learning, liking and anticipation require separate evidence. **Confidence:** Low for applied learning/fatigue effect. **Unresolved:** Can players identify the intended relation on novel cases rather than repeat a memorized answer?

### C-08

**Claim:** Authored scoring, adaptive combinations, player-linked performance and deliberate absence of music deserve comparison rather than automatic escalation to adaptivity.

**Class:** `inference`. **Support and locator:** C-01–C-06; evidence does not rank all alternatives.

**Applicability / opposition:** Selection follows the local decision, not a universal hierarchy; musical material should not be an intentionally weak control. **Confidence:** Moderate as evidence-calibrated selection, low for outcome ranking. **Unresolved:** Which alternative supplies useful value at acceptable authoring and access cost?

### C-09

**Claim:** Music can be optional ornament, meaningful but nonessential expression, or required task information; classify its role explicitly.

**Class:** `inference`. **Support and locator:** SRC-0007, category control; SRC-0005 via inspected audio/locale dependencies; C-01.

**Applicability / opposition:** Turning music off need not preserve identical experience, but a hidden critical dependency requires a usable alternative or explicit task/access redesign. **Confidence:** Moderate for requirement analysis; mode usability untested. **Unresolved:** What task changes when the player declines the score?

### C-10

**Claim:** State-valid musical transitions are a distinct candidate recipe whose cancellation and recovery steps require local validation.

**Class:** `hypothesis`. **Support and locator:** C-04/C-06 and linked P05-PAT-01; documentation supplies capability only.

**Applicability / opposition:** Not an empirical validation of state hysteresis, musical smoothness or emotional benefit. **Confidence:** Low for comparative effectiveness. **Unresolved:** Does rechecking pending transitions reduce false presentation without excessive delay or silence?

### C-11

**Claim:** All scenarios, musical structure definitions and proposed comparisons here are original prospective specifications.

**Class:** `hypothesis`. **Support and locator:** Original P05 synthesis under the supplied brief; no new audio assets, players or measurements.

**Applicability / opposition:** No BPM, repetition count, timing law, sample-power guarantee or affect-equivalence threshold is proposed as universal. **Confidence:** Low until locally evaluated. **Unresolved:** Which controlled comparisons and inclusion criteria are feasible?

### C-12

**Claim:** This batch authorizes music research and draft artifacts, not recording, runtime implementation or release.

**Class:** `studio-decision`. **Support and locator:** Doug, current P05 instruction and complete brief, 2026-10-10.

**Applicability / opposition:** All drafts retain null approval fields; scope is genre-neutral. **Confidence:** High for bounded permission. **Unresolved:** Whether to revise and advance the candidates to independent review.

## References

All records below were inspected as **relevant-excerpt** on **2026-10-10**. Dates identify the inspected snapshot, not a claim of latest engine support. Repeated records are provenance copies, not independent corroboration. Existing pilot/W02 identities are retained; all P05 identities are run-scoped proposals.

### GDR-SRC-20261010-P05-001

**Unity Technologies.** [Audio Mixer window](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html). **Publication/update:** Publication/update unknown. **Edition:** Unity 6.0 / 6000.0 documentation snapshot.

**Locator:** Audio Mixer window opening; How it works; Snapshots; Ducking (HTML text 125–148). **Type:** Official technical documentation. **Supports:** C-06; transition capability only.

**Limits/independence:** Described routing capability only; Web support caveat retained. Not a runtime test, perceptual benefit, recommended bus count or middleware selection. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-004

**Unity Technologies.** [AudioSource.PlayScheduled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayScheduled.html). **Publication/update:** Publication/update unknown. **Edition:** Unity 6.0 / 6000.0 scripting reference snapshot.

**Locator:** Parameters → time; Description and following explanatory paragraph (HTML text 248–258). **Type:** Official technical documentation. **Supports:** C-04; inferred C-06/C-10.

**Limits/independence:** DSP-timeline capability; example scheduling lead times are not design deadlines. No program executed, cancellation semantics certified or platform latency measured. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-005

**Cale Plut and Philippe Pasquier.** [Music Matters: An empirical study on the effects of adaptive music on experienced and perceived player affect](https://ieee-cog.org/2019/papers/paper_106.pdf). **Publication/update:** 2019; exact publication day not established. **Edition:** IEEE Conference on Games 2019 proceedings paper, eight-page conference PDF.

**Locator:** §V method/participants pp.5–6; Table III p.4; Table V p.6; §VI-B and Table VII p.7; §VII–VIII pp.7–8 (PDF page numbers counted from first page). **Type:** Original interactive experiment. **Supports:** C-02; C-01 and C-08 inference.

**Limits/independence:** Small mixed remote/in-person sample; different musical material; reported pairwise comparisons narrower than conclusion; no raw-data or multiplicity reanalysis. Independent of Cowen cohort. **Rights:** Copyright/reuse permission not established from inspected pages; no figures or stimuli redistributed.

### GDR-SRC-20261010-P05-006

**Alan S. Cowen, Xia Fang, Disa Sauter and Dacher Keltner.** [What music makes us feel: At least 13 dimensions organize subjective experiences associated with music across different cultures](https://doi.org/10.1073/pnas.1910704117). **Publication/update:** Online 2020-01-06; journal issue 2020-01-28. **Edition:** PNAS 117(4), 1924–1934; author-hosted eleven-page journal copy.

**Locator:** Experiment 1 methods p.3; Experiment 2 p.7; Discussion pp.9–10; Methods p.10 (copy page numbering). **Type:** Original cross-cultural listening research. **Supports:** C-03; C-07 limited contextual support.

**Limits/independence:** Two national samples, brief excerpts, perceived/experienced distinction unresolved; reported total does not reconcile with country counts. Text inspected; figure rendering attempts failed; no figure-derived estimate or raw-data audit. **Rights:** PNAS article; reuse license not verified; no music, figures or questionnaire reproduced.

[Inspected author-hosted copy](https://static1.squarespace.com/static/5bb46f713560c364c1a4b340/t/5fc567d7e6d49a06bb494f59/1606772700340/CowenEtAlMusic.pdf).

### GDR-SRC-20261010-P05-011

**Supergiant Games.** [Bastion FAQ](https://www.supergiantgames.com/blog/19/). **Publication/update:** Original archive entry 2011-05-11; FAQ states updated 2026-07-14. **Edition:** Live archival FAQ; game build unspecified.

**Locator:** Bastion FAQ → Is Bastion’s soundtrack available? (web text 239–241). **Type:** Firsthand production account. **Supports:** C-05; C-07/C-08 production rationale.

**Limits/independence:** Early musical direction is reported intent, not measured tonal coherence. No playback, game build, awards or sales inference. Independent production from SOMA. **Rights:** Reuse license not verified; attributed paraphrase only.

### SRC-0005

**Microsoft.** [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). **Publication/update:** Updated 2026-03-04; original date unknown. **Edition:** Unnumbered live XAG 104 revision.

**Locator:** Goal; Overview; Implementation guidelines: important speech/non-speech, speaker/direction, category settings (web text 31–117). **Type:** Official vendor guidance. **Supports:** C-09 task-information inference.

**Limits/independence:** Not a formal standard or certification claim; no cross-language reading-speed or emotional-equivalence finding. Same issuer as SRC-0007. **Rights:** Reuse license not verified; attributed paraphrase only.

### SRC-0007

**Microsoft.** [Xbox Accessibility Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105). **Publication/update:** Updated 2026-03-04; original date unknown. **Edition:** Unnumbered live XAG 105 revision.

**Locator:** Goal; Overview; Implementation guidelines: separate categories, mono, spatial audio, pause exceptions, assistive speech (web text 31–102). **Type:** Official vendor guidance. **Supports:** C-06/C-09 access inference.

**Limits/independence:** Recommendations, not an implemented configuration, hearing-safety standard or measured usability. Same issuer as SRC-0005. **Rights:** Reuse license not verified; attributed paraphrase only.

## Open questions and change history

**2026-10-10 — initial-author-draft, version 0.1.0.** No predecessor P05 artifact; no supersession or new canonical assignment. Evidence checked means the source passages and named dependency bytes were inspected, not that their conclusions were approved. The separate author self-review is in the [P05 packet](../reviews/full-run-20261010-p05-review-packet.md#author-self-review). No independent P05 review has occurred.

**Handoff:** complete draft artifact, bounded source coverage and unresolved local outcomes. Gate C independent review and acceptance remain outstanding; P05 host Gate D tests are NOT RUN; Gate E acceptance/release is NOT PASSED. Next decision: Coordination reviews scope, evidence precision, identity/overlap mapping and proposed child work before any separately authorized validation or release.
