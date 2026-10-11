---
id: GDR-CAND-20261010-P02-TOP-02
kind: topic
title: Feedback and game feel
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
- game feel
- juicy feedback
- impact feedback
- response clarity
tags:
- feedback
- game-feel
- haptics
- state-clarity
- latency
- sensory-load
related_topics:
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-P02-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P02-005
- GDR-SRC-20261010-P02-007
- GDR-SRC-20261010-P02-008
- GDR-SRC-20261010-P02-009
- GDR-SRC-20261010-P02-010
- GDR-SRC-20261010-P02-011
- GDR-SRC-20261010-P02-012
- GDR-SRC-20261010-P02-014
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded P02 draft; no predecessor P02 artifact found in the
  inspected Project snapshot.
byte_hash_record: ../reviews/full-run-20261010-p02-review-packet.md#candidate-byte-receipt
---

# Feedback and game feel

**Draft research candidate — not released guidance, implementation approval or a validated recipe.** This is P02 only. The current dispatch authorizes this research; the parent’s first-wave review receipt is retained without importing unseen corrected content. Its later reconciliation supersedes the dispatch’s earlier “P01 unreviewed” sentence. P01 is parent-reported reviewed, not released; its bytes remain a missing dependency here.

**Evidence boundary:** inspected public documents and the supplied Project snapshot; no project/engine code, game build, participant study or host-retrieval test was run. Definitions and synthetic scenarios are proposed analytic tools, not formal standards. [C-12]

## Decision and scope

**Decision:** What response should follow an action or state change so that players understand what happened, can act on it and experience the intended impact without unnecessary latency, sensory load or misleading success signals? Separate **intended impact** from measured enjoyment, competence, control, task accuracy and comfort. Increasing one is not evidence of increasing the others. [C-01–C-04]

This topic owns the relation between action/state and presented response: visual, audio, haptic, animation and selected timing effects. It does not prescribe combat balance, camera settings, a renderer, a mix target or a network-authority model. Input recognition belongs to [Controls and input](controls-and-input.md); access to event facts belongs to [Multimodal communication](multimodal-communication.md). Art, animation, camera and onboarding dependencies remain uninspected as shared reviewed entries. [C-01, C-09, C-12]

### Working definitions and context

**Feedback** is a response that may communicate an action, state, consequence or error. **Impact** is an intended quality of that response, such as weight, decisiveness or delicacy. **Game feel** is used here as a design question about experienced interaction, not a single validated score. **Juiciness** names a family of amplified or embellished feedback approaches; the particular visual/haptic manipulations in inspected studies do not define every possible use of the term. **Sensory load** here means the presentation competing with the current task or the player's tolerable settings; no physiological threshold is implied. [C-01, C-02, C-03, C-09]

A later application must declare device, display/frame conditions, viewing distance, listening method and noise, haptic hardware/contact, preferred intensity and access settings, expected session length and task demands. A vibration effect tested on an iPhone is not the same stimulus on every controller; silent use and haptics-off operation are valid contexts to design for, not defects to dismiss. These are test-scope requirements proposed from the source limits and guidance. [C-03, C-05, C-09, C-10]

## Core explanation and mechanisms

### What the comparative evidence does and does not show

The strongest inspected challenge to “stronger feedback is better” is not a general preference for minimalism. In Kao and colleagues’ amplification comparison, amplified feedback reduced reported effectance and competence, while direct effects on enjoyment and voluntary playtime were not significant. Singhal and Schneider found benefits of adding haptics for selected experience measures, but no significant low-versus-high haptic difference on those player-experience constructs. These findings concern different games, stimuli and populations; together they require conditional comparison, not a universal optimal intensity. The exact study records and limitations are in C-02 and C-03. [C-02, C-03]

Neither study validates the full P02 recommendation. Adding an embellishment changes more than “strength”: visibility, event specificity, temporal form, repetition and meaning can change together. Source 011 discusses agency/occlusion as a possible explanation; that explanation was not isolated as a second experiment. A large sample cannot remove a confound built into the intervention. [C-02, C-08]

### Distinguish action receipt from outcome

For design purposes, specify the states the player may need to distinguish: input recognized, action accepted, action underway, success, partial result, rejection, cancellation and uncertain/pending outcome. Not every action needs a separate cue for every state; use the distinctions to avoid false claims. A decorative response to an attempted action can be legitimate, but an attempted action should not automatically receive a cue that players have learned means success. [C-01, C-06]

**Proposed causal chain:** feedback corresponds to the actual relevant state → the player can perceive and interpret that relation → the player can choose a useful next action → experienced control or impact may improve. Official narration guidance supports explicit state/action information; game experiments inform selected experience outcomes. The last link remains a hypothesis for a particular application. A recognizable response can instead be irritating, emotionally flat or too late to help. [C-05–C-07]

### Timing and sensory intensity are different variables

An emphatic impact effect can arrive late. A prompt can appear immediately but describe the wrong state. Source 014 provides narrow evidence that added input delay harmed a controlled aiming task; it does not establish a universal feedback delay or prove that removing every intentional pause improves interaction. A deliberate anticipation or impact pause is part of the action's designed temporal contract; technical stalls, variable arrival and misleading confirmation are different questions. No duration for hitstop, animation anticipation or modality synchronization is prescribed here. [C-01, C-04, C-07, C-09]

### Information survives reduced ornament

The proposed application of access guidance is to separate required state information from optional intensity. Reducing camera shake, ambient sound or vibration should not silently erase a fact that the player must act on. This does not mean retaining every effect in another channel or turning every low-intensity preset into a narration stream. Preserve a usable route to the required facts, then test whether that route competes with other information. [C-05, C-10]

## Design choices and alternatives

| Choice | Useful when | Main tradeoff and exit |
| --- | --- | --- |
| Small, consistent acknowledgement | The player mainly needs to know that a reversible action was received. | May be too subtle or emotionally inappropriate. Keep the least complex response that is actually interpreted, not merely the smallest asset. |
| Outcome-specific visual/audio/haptic response | Distinguishing success, miss, denial or partial completion matters. | More states and localizations to author; misleading reuse destroys the distinction. Exit when players cannot decode the difference. |
| Stronger embellishment | The intended experience calls for a salient event and task visibility remains intact. | Can obscure the next action or overwhelm preferred settings. Compare against the same event with less embellishment. |
| Repeated/progress feedback | A sustained action needs progress or continued-state information. | Repeated cues can dominate attention. Consider a persistent state indication or on-demand detail instead. |
| Intentional pause or animation commitment | Timing itself communicates weight or commitment. | Can delay control or confuse cancellation. Retain only with a clear action contract and evaluated alternatives. |
| No extra feedback | The changed world state is already clear and adding another response supplies no useful information or desired expression. | “No extra” cannot mean omitting the only accessible acknowledgement. |

These are conditional options, not universal rankings. In particular, the simplest sufficient informational response is not automatically the best aesthetic response. Evaluate both. [C-06–C-10]

### A proposed state-to-response specification

| State question | Proposed response contract | Forbidden inference |
| --- | --- | --- |
| Was my request recognized? | Indicate receipt when it is useful, without asserting final success. | Receipt means a remote or delayed outcome is already confirmed. |
| Why did nothing happen? | Communicate a relevant reason or available remedy when that fact matters. | Silence always means rejection, or a vague error sound explains a recovery action. |
| What changed? | Present the result and the information needed for the next decision. | Bigger particles mean a quantitatively stronger result unless the system defines that mapping. |
| Is it still happening? | Retain an interpretable persistent state or progress route. | Continuous vibration is necessary to communicate continued activity. |
| Can I stop or undo it? | Make cancellation/reversibility clear where those actions exist. | A reassuring cue grants an undo capability the system does not have. |

The table is an original design specification for evaluation, not a shipped-game observation. [C-01, C-06, C-09]

## Application process

1. **Diagnose the missing outcome.** Decide whether the problem is unreadable state, weak intended impact, late response, incorrect interpretation, discomfort or an absent accessible route. Do not start with an asset-count or intensity target. [C-01, C-07]
2. **Specify state meanings.** Write the response contract for the action, including rejection, partial result, cancellation and pending outcome where applicable. Name which properties communicate meaning and which are decoration. [C-06]
3. **Choose alternatives with a common information baseline.** Compare no additional ornament, a restrained response and a justified richer response. Keep the gameplay result and minimum information constant where the purpose is isolating presentation; log unavoidable differences. [C-07, C-08]
4. **Design controls and fallback information concurrently.** Support relevant reduced-effects, audio-category and haptic options. Test the required facts with those options selected. A player's choice to disable an effect is not evidence they failed to understand the intended experience. [C-05, C-10]
5. **Prototype and measure only with separate authorization.** Inspect actual onset and persistence in each channel, task visibility, response interpretation and hardware variation. Do not treat a nominal script timestamp as a measured end-to-end perceptual result. [C-04, C-09]
6. **Keep, narrow or remove.** Advance only a response with useful experience or comprehension value and acceptable access/control costs. Preserve cases where different participants prefer different levels. A net preference score must not conceal a critical missed cue or a stop request. [C-07, C-09]

## Patterns and genre adaptations

[Fact-preserving cue alternatives](../patterns/fact-preserving-cue-alternatives.md) — `GDR-CAND-20261010-P02-PAT-02` — supplies the access-equivalence hypothesis and fallback recipe. The input-side [Recoverable action remapping](../patterns/recoverable-action-remapping.md) — `GDR-CAND-20261010-P02-PAT-01` — is relevant when poor feel is actually a mapping/activation failure.

An **outcome-specific feedback ladder** is queued as additional child work, not a third pattern artifact or allocated child identity. Its distinct question is how much acknowledgement/progress/result detail each action needs without misleading success or delaying control. The queue and dependencies are recorded in the packet.

No genre-specific preferences are asserted. **Illustrative adaptations:** precise inspection may value stable visual detail; a celebratory event may warrant a richer response; a suspenseful event may preserve uncertainty about cause while clarifying available action. A hybrid must decide which promise governs the moment rather than maximize all of them. [C-09]

## Examples and counterexamples

### Illustrative worked example — placing a structure

A player moves a candidate object, selects a position and requests placement. A preview explains whether placement is currently valid. The request response acknowledges intent; final placement feedback occurs only when placement is actually accepted. A denied request identifies the relevant obstruction or unavailable resource through the selected information route. [C-06, C-09]

The richer candidate adds a brief constructed-form animation, a sound and optional vibration to an accepted placement. The restrained alternative changes the object to its placed state with a readable confirmation. Both preserve position validity, success/failure and what can happen next. Reduced-effects mode removes shake/ornament without hiding denial. Measure decision accuracy and continued placement as well as felt satisfaction; a louder completion sound alone does not establish a better interaction. **No version was built or tested.** [C-07–C-10]

### Counterexample — action art masks the next decision

An elaborate response covers an object that the player must immediately inspect. Players might report a strong impact yet miss the state change or repeat an already completed action. In that case, moving or reducing the ornament may be preferable to increasing it, but a different composition that preserves visibility could also work. This is a prospective causal explanation, not a claim that every rich effect impairs attention. [C-07–C-09]

### Contrary evidence against “less is always better”

Source 012's haptic-presence result is a concrete reason not to turn source 011's amplification finding into an anti-feedback law. There may be value in a richer response for the tested context. That does not justify a particular rumble intensity, all-player preference or an untested haptic-only task signal. [C-02, C-03, C-05]

## Failure modes and constraints

**State ambiguity:** similar cues for different outcomes can make a successful press feel unreliable. **Masking:** ornament can hide the next target or compete with narration. **Timing mismatch:** channels may imply different event boundaries. **Setting dependence:** essential information can disappear when an optional channel is disabled. **Habituation or fatigue:** repeated emphasis may change its meaning or tolerability. These are hypotheses to investigate, not measured failure rates. [C-06–C-10]

**Accessibility:** XAG guidance supports configurable audio categories, haptics and visual motion. These are vendor recommendations, not numerical safety limits. A low-motion setting is not a completed photosensitivity review; no flash-frequency or camera-motion threshold is certified by this topic. Required perceptual access and preferred emotional intensity must be evaluated separately. [C-05, C-10]

**Production and ethics:** response variants add event-state ownership, asset and localization work, settings combinations, device tests and regression checks. An effect that celebrates an unsuccessful or disadvantageous outcome can be misleading when players reasonably interpret it as success; outcome semantics deserve explicit review rather than default positive reinforcement. No monetization, engagement or retention claim is supported here, and no production-cost multiplier is known. [C-06, C-09, C-11]

## Playtest and validation

**PROPOSED — NOT RUN.** No assets, prototype, participant session, sensory measurement or benchmark was produced. [C-09, C-12]

**Primary question:** Does a candidate response improve the intended interaction outcome without obscuring state, delaying useful action or excluding preferred access settings?

**Design:** begin with a common functional-information baseline. Compare restrained and embellished responses that share the same gameplay outcomes, event semantics and input timing. Where the question is outcome specificity, compare state-specific and non-specific responses separately from intensity; do not change both and claim the effect belongs to only one. Where hardware cannot reproduce the same haptic stimulus, treat device as a context variable rather than a nuisance to average away.

**Participants and procedure:** include people who use the relevant access options and actual target devices; record familiarity, audio environment, haptic preference and display context. Counterbalance condition order and comparable event sets, keep initial learning and repeated use distinct, allow chosen tolerable intensity and stop on request. A mandatory high-intensity exposure is not required to evaluate a setting the participant declines.

**Separate measures:** ability to identify receipt/result/rejection; unnecessary retries; accuracy on the next task; time to the next intended action; perceived control, intended impact, enjoyment and comfort. Measure channel-onset delay only with a declared instrumentation route. Self-reported intensity is not proof of measured response latency or emotional engagement.

**Decision rules:** a critical state misinterpretation, loss of required information in a supported setting or requested stop blocks advancement of that condition. Added ornament must show a predeclared useful experience or comprehension advantage over the simpler comparator without an unacceptable task/control regression. If benefits are preference-dependent, retain a configurable or narrower candidate rather than an averaged “best” setting. If evidence is inconclusive, say so; non-significance is not equivalent experience. Confirmatory margins and sample size require justified local variability and a separate study approval, not a library-wide number. All criteria here are proposed. [C-09]

## Claim ledger

Claim IDs are local to this entry. Confidence concerns the stated scope, not source prestige. An inference is not a validated outcome; repeated references are not independent corroboration.

### C-01

**Claim:** Feedback should be evaluated as a relation between actual action/state and player interpretation, with impact, control, accuracy, enjoyment and comfort kept distinct.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-009, action/state narration; GDR-SRC-20261010-P02-011, §§3.3 and 4.2; GDR-SRC-20261010-P02-014, measures and results.
**Applicability and contrary limits:** Working definition, not a validated universal game-feel score. Not every action needs every proposed response state.
**Confidence:** Moderate for the conceptual distinction; a particular response contract remains untested.
**Unresolved:** Which information and experience outcomes matter at this decision point?

### C-02

**Claim:** In Kao et al.’s Model A, amplified feedback lowered effectance and competence; direct effects on enjoyment and free-choice playtime were not significant.
**Class:** `empirical-evidence`. **Evidence and exact locator:** GDR-SRC-20261010-P02-011, PDF p. 8 §§3.5–3.7; p. 9 §4.2; p. 14 §6.
**Applicability and contrary limits:** The whole study analyzed 1,699 adults; Model A compared 678 participants in standard versus amplified non-success-dependent, non-varied conditions in one short desktop action-RPG. Working audio/English fluency were required. No universal harm or optimal minimum follows.
**Confidence:** Moderate for this reported comparison; bundled implementation and task limits remain.
**Unresolved:** Would the result hold with task visibility, event specificity and aesthetic intent controlled differently?

### C-03

**Claim:** In Singhal and Schneider’s Study 2, haptic presence improved selected experience measures, while low/high haptic variants did not significantly differ on those player-experience measures.
**Class:** `empirical-evidence`. **Evidence and exact locator:** GDR-SRC-20261010-P02-012, PDF pp. 8–9 §§6.3–6.5, Figure 6/Table 1; p. 10 §7.4.
**Applicability and contrary limits:** 36 analyzed adults after two exclusions from 38; remote compatible iPhones; three haptic by two visual conditions within participant, one Breakout-style game. HX expressivity did differ; HX questions were not yet validated. No equivalence, disability representation or amplitude-only causal claim.
**Confidence:** Moderate within the experiment; not a device-independent intensity law.
**Unresolved:** Benefits across devices, tasks, prolonged use and players who disable/cannot perceive haptics.

### C-04

**Claim:** An added-delay experiment supplies a reason to measure actual response timing, not a universal timing threshold for feedback or intentional animation.
**Class:** `empirical-evidence`. **Evidence and exact locator:** GDR-SRC-20261010-P02-014, PDF pp. 8–11 §§3.2, 4.1–4.4 and results; p. 18 limitations.
**Applicability and contrary limits:** 36 participants; stationary mouse aiming; zero versus 150 ms added delay on top of nonzero baseline. Not haptic onset, intentional hitstop or jitter.
**Confidence:** Moderate for reported task effects; transfer outside the experiment is limited.
**Unresolved:** Which latency endpoint and action timing need separate measurement in an application?

### C-05

**Claim:** Microsoft recommends controllable audio categories, haptic options and reduced visual distractions/motion, rather than assuming a single sensory presentation works for all players.
**Class:** `practitioner-heuristic`. **Evidence and exact locator:** GDR-SRC-20261010-P02-007, Implementation guidelines; GDR-SRC-20261010-P02-008, Implementation guidelines; GDR-SRC-20261010-P02-010, Implementation guidelines.
**Applicability and contrary limits:** Vendor guidance, not formal-standard or numerical safety certification. Options themselves are not proof of access.
**Confidence:** High for accurate attribution; local effect and coverage unverified.
**Unresolved:** Do the chosen settings preserve usable required information?

### C-06

**Claim:** Use response meanings that distinguish actual receipt, result, rejection or uncertainty when those differences affect the next decision.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-009, action confirmation and state narration; GDR-SRC-20261010-P02-011, success-dependence manipulation (§3.2) as a design distinction, not an unrestricted outcome proof.
**Applicability and contrary limits:** Bridge: a success-like response to a mere attempt can invite an incorrect next action. Decorative attempt feedback is not prohibited when its meaning is clear.
**Confidence:** Moderate as a semantic-risk rationale; the full state ladder has not been tested.
**Unresolved:** How many distinctions can players use without unnecessary burden?

### C-07

**Claim:** Compare the least complex useful response with richer alternatives; do not presume either maximum or minimum intensity is best.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-011, §4.2; GDR-SRC-20261010-P02-012, §6.5; GDR-SRC-20261010-P02-014, task-latency experiment.
**Applicability and contrary limits:** Bridge: comparative findings are context-dependent and measure different outcomes. Cost, desired expression and actual comprehension justify testing alternatives.
**Confidence:** Moderate for the decision rule, not a proven optimum.
**Unresolved:** Which richer alternative adds worthwhile value for the intended audience and task?

### C-08

**Claim:** The inspected feedback interventions bundle properties, so an agency, occlusion or amplitude explanation should not be claimed as separately proven.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-011, §§3.2, 5.1 and 6; GDR-SRC-20261010-P02-012, §6.1 and §7.4.
**Applicability and contrary limits:** Specific mechanisms remain distinguishable hypotheses. The source 011 Model B sample-description discrepancy is retained in the packet, not repaired by assumption.
**Confidence:** Moderate for the methodological limitation; no raw-data/analysis audit.
**Unresolved:** Which controlled ablation would distinguish meaning, visibility, timing and sensory intensity?

### C-09

**Claim:** The definitions, response specifications, illustrations and validation plans are proposed local research/design tools, not executed tests or approved settings.
**Class:** `hypothesis`. **Evidence and exact locator:** Original P02 synthesis under the supplied dispatch, lines 8–12 and 22–24, with bridges in C-01–C-08.
**Applicability and contrary limits:** No prototype, emotional response, comfort limit, timing or sample-size guarantee is established.
**Confidence:** Low for predictive validity until evaluated.
**Unresolved:** Feasibility, suitable measures, actual users/settings and justified confirmatory decision margins.

### C-10

**Claim:** Reducing ornament or disabling a channel should preserve a usable route to required state facts, without promising identical emotion.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-005, critical information channels; GDR-SRC-20261010-P02-007, audio controls; GDR-SRC-20261010-P02-008, alternatives to haptic-only information; GDR-SRC-20261010-P02-010, motion options.
**Applicability and contrary limits:** Bridge: optional intensity cannot be the only route to a required decision fact. Simultaneous maximal duplication is not required by this synthesis.
**Confidence:** Moderate for the access rationale; usability and affect remain untested.
**Unresolved:** Can the chosen reduced-effects configuration communicate the required facts at the needed time?

### C-11

**Claim:** State-dependent variants create authoring and verification obligations; misleading celebration and assumed engagement gains require explicit challenge.
**Class:** `inference`. **Evidence and exact locator:** C-06 and C-10 supply the information/access rationale; workload categories and ethical counterexample are original P02 analysis.
**Applicability and contrary limits:** No staffing estimate, retention result or universal ban on expressive feedback is asserted.
**Confidence:** Moderate for the identified obligations; magnitude and downstream effects unknown.
**Unresolved:** Which variants are necessary, affordable and understandable without misrepresenting outcomes?

### C-12

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
**Claims using this record:** C-10. **Limits:** Recommends access routes; does not experimentally establish comprehension, equal emotion or benefits from activating all channels simultaneously.
**Independence/deduplication:** Same issuer as sources 001 and 006–010; not independent outcome evidence.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only; example images not redistributed.

### GDR-SRC-20261010-P02-007

Microsoft. [Xbox Accessibility Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Overview; Implementation guidelines: independent functional audio categories (lines 49–61), stereo-to-mono option (78–81), assistive-speech ducking option (102); update footer (143).
**Claims using this record:** C-05, C-10. **Limits:** No universal mix level or safe-listening threshold established. Mono access is not proof of preserved directional information. Page examples and linked videos were not observed as game evidence.
**Independence/deduplication:** Same canonical URL as attached audio pilot provisional SRC-0007; cross-batch identity reconciliation pending. Same issuer as other XAGs.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-008

Microsoft. [Xbox Accessibility Guideline 110: Haptic feedback](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/110). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal; Overview; Implementation guidelines: disabling/adjusting haptic feedback and additional channels for information carried by haptics; update footer (retrieved line 117).
**Claims using this record:** C-05, C-10. **Limits:** No universal pulse, intensity, comfort or hardware-equivalence threshold. Options do not by themselves prove usability for any particular player.
**Independence/deduplication:** Same Microsoft guideline family; independent of the participants/data in source 012.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-009

Microsoft. [Xbox Accessibility Guideline 106: Screen narration](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** How should an item be narrated?; Other key concepts (retrieved lines 203–212); Implementation guidelines, including focus change interrupting obsolete narration (316–318), configuration, repeat/cancel and confirmation of actions.
**Claims using this record:** C-01, C-06. **Limits:** Narration availability and sequencing guidance, not a universal optimal queue scheduler. No platform narration integration or user evaluation performed.
**Independence/deduplication:** Same issuer as other XAGs; screen narration and captions are different interfaces even when both carry language.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-010

Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision.
**Type:** Official vendor accessibility guidance. **Locators inspected:** Goal and Overview; Implementation guidelines for moving/scrolling UI content and configurable camera effects (retrieved lines 59–114); update footer (182).
**Claims using this record:** C-05, C-10. **Limits:** Distinguishes presentation/UI effects from core ongoing gameplay. Does not establish numerical camera comfort settings or certify flash/photosensitivity safety.
**Independence/deduplication:** Same issuer as other XAGs. P01’s corrected numerical accessibility text is not available here and is not reconstructed from this source.
**Rights:** Publisher terms; reuse license not audited. Paraphrase only.

### GDR-SRC-20261010-P02-011

Dominic Kao, Nick Ballou, Kathrin Gerling, Heiko Breitsohl and Sebastian Deterding. [How does Juicy Game Feedback Motivate? Testing Curiosity, Competence, and Effectance](https://people.csail.mit.edu/dkao/pdf/3613904.3642656.pdf). **Publisher:** Association for Computing Machinery. **Publication/update:** 2024; conference held 11–16 May 2024; exact publication day not established. **Edition/build:** CHI 2024 conference paper; author-hosted PDF, 16 pages.
**DOI:** `10.1145/3613904.3642656`; the inspected access route is linked above.
**Type:** Original randomized game experiment. **Locators inspected:** PDF pp. 5–8, §§3.1–3.7; p. 8 Table 1 and §3.5 participants; p. 9 §§4.2–4.3; p. 11 Figures 4–5; p. 14 §6 limitations. PDF text and relevant page images inspected.
**Claims using this record:** C-01, C-02, C-06, C-07, C-08. **Limits:** One short desktop action-RPG task and selected English-fluent adults with working audio. Effects bundled particular audiovisual implementations. Model A is the clean amplification comparison; §3.7’s amplified-only Model B description and §4.3’s n=1699 label are not reconciled here. No raw-data or analysis-code audit.
**Independence/deduplication:** Distinct study from source 012, in an overlapping juiciness research literature; not a direct replication. Author explanations of agency/occlusion are not separately established causal mechanisms.
**Rights:** CC BY-SA 4.0 stated in the paper. No figures, game assets or PDF redistributed.

### GDR-SRC-20261010-P02-012

Tanay Singhal and Oliver Schneider. [Juicy Haptic Design: Vibrotactile Embellishments Can Improve Player Experience in Games](https://uwspace.uwaterloo.ca/bitstreams/723405dd-f236-4aab-96f2-c1db3491e37e/download). **Publisher:** ACM CHI 2021; inspected via University of Waterloo. **Publication/update:** 2021; CHI conference held 8–13 May 2021; exact publication day not established. **Edition/build:** Author manuscript in University of Waterloo repository, 11 PDF pages.
**DOI:** `10.1145/3411764.3445463`; the inspected access route is linked above.
**Type:** Original game experiment; Study 2 is used here. **Locators inspected:** PDF pp. 7–9, §§6.1–6.5, Figure 6 and Table 1; p. 10 §7.4 limitations. Relevant PDF page images, methods/results and rights footer inspected.
**Claims using this record:** C-03, C-07, C-08. **Limits:** Study 2: 38 recruited, 36 analyzed, remote compatible-iPhone users able to feel a test vibration. Three haptic by two visual conditions, within participant, one Breakout-style game. HX instrument noted as not yet validated. Non-significant low/high differences are not equivalence; implementations do not isolate amplitude alone.
**Independence/deduplication:** Separate experiment from source 011; same broad literature and some shared prior references. Study 1 and Study 2 in this paper are not counted as independent replications of the P02 recipes.
**Rights:** Author-manuscript personal-use/copyright notice. Paraphrase only; no manuscript, screenshots or stimuli redistributed.

### GDR-SRC-20261010-P02-014

David Halbhuber, Philipp Schauhuber, Valentin Schwind and Niels Henze. [The Effects of Latency and In-Game Perspective on Player Performance and Game Experience](https://epub.uni-regensburg.de/55325/1/3611070.pdf). **Publisher:** ACM; University of Regensburg repository. **Publication/update:** November 2023; repository deposit 2024 is not publication date. **Edition/build:** Proceedings of the ACM on Human-Computer Interaction 7, CHI PLAY, Article 424; 22-page PDF.
**DOI:** `10.1145/3611070`; the inspected access route is linked above.
**Type:** Original controlled game experiment. **Locators inspected:** PDF p. 8 (424:8), §3.2 baseline measurement and §4.1 conditions; pp. 9–10 §§4.2–4.4; p. 11 results/Figure 5; p. 18 §6.5 limitations. Text and methods/results page images inspected; repeated p. 18 screenshot route failed, but its text was accessible.
**Claims using this record:** C-01, C-04, C-07. **Limits:** 36 participants, mostly students; matched stationary mouse aiming/shooting tasks across three perspectives. Zero or 150 ms added delay, not zero end-to-end latency. Baseline mean 47.75 ms, SD 13.12, from 20 captures. Not a jitter study, all-device comparison or universal acceptable-latency threshold.
**Independence/deduplication:** Separate experiment from other empirical records. Its use of input buffering to add delay differs from source 003’s early-intent retention; this is terminology, not a contradictory result.
**Rights:** CC BY 4.0 in institutional record. No PDF or figures redistributed.


## Open questions and change history

| Subtopic | Researched coverage | Unresolved question |
| --- | --- | --- |
| Audiovisual/haptic response | Two inspected feedback experiments plus current vendor access guidance. | How do actual events and hardware change interpretation and preference? |
| Impact and state clarity | State-to-response synthesis; evidence challenges unqualified amplification. | Does outcome-specific feedback improve the chosen task independently of intensity? |
| Latency | One controlled added-input-delay study, with actual baseline distinguished. | No universal cross-modal onset or intentional-pause setting; which endpoint causes the problem? |
| Sensory load | Configurable audio/haptics/motion guidance and empirical implementation limits. | No validated universal load score, long-session dose or comfort boundary. |

**Missing dependencies:** actual parent-reviewed P01 visual/camera/accessibility bytes and corrected numerical-scope wording; reviewed animation/art-direction guidance; Foundations action/movement/challenge and onboarding; Worlds action staging. Only the supplied P02 candidate identities are linked; absent IDs are not guessed.

**Contradictions:** `P02-CON-01` concerns “stronger is always better” versus context-specific effects. `P02-CON-05` records source 011’s Model B population-label inconsistency. The draft does not rely on resolving that discrepancy to prescribe success-dependent feedback.

**History:** 2026-10-10, 0.1.0, `initial-draft-1`; initial P02 candidate, no predecessor/supersession. Author self-review only; no independent approval or release. [Review packet](../reviews/full-run-20261010-p02-review-packet.md). Next decision: independent review of causal wording, access-preserving reductions and the proposed outcome-specific feedback child question.
