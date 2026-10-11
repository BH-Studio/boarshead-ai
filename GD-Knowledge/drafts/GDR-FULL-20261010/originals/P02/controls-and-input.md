---
id: GDR-CAND-20261010-P02-TOP-01
kind: topic
title: Controls and input
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
- input mapping
- control remapping
- input buffering
- device parity
tags:
- input
- mapping
- remapping
- responsiveness
- buffering
- alternative-input
- accessibility
related_topics:
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-P02-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P02-001
- GDR-SRC-20261010-P02-002
- GDR-SRC-20261010-P02-003
- GDR-SRC-20261010-P02-004
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

# Controls and input

**Draft research candidate — not released guidance, implementation approval or a validated recipe.** This is P02 only. The current dispatch authorizes this research; the parent’s first-wave review receipt is retained without importing unseen corrected content. Its later reconciliation supersedes the dispatch’s earlier “P01 unreviewed” sentence. P01 is parent-reported reviewed, not released; its bytes remain a missing dependency here.

**Evidence boundary:** inspected public documents and the supplied Project snapshot; no project/engine code, game build, participant study or host-retrieval test was run. Definitions and synthetic scenarios are proposed analytic tools, not formal standards. [C-12]

## Decision and scope

**Decision:** Which action mappings, activation rules and timing policies let intended players express the intended actions on supported devices without unnecessary physical demands, stale actions or loss of recovery? Evaluate functional access, intentionality, comprehensibility and task performance separately; identical button counts or sensitivity values do not establish parity. [C-01, C-09]

This topic owns input-side intent recognition and its contract with gameplay. It does not own movement/combat balance, onboarding curricula, server authority or engine integration. Those dependencies are not supplied as reviewed bytes. Platform examples are evidence about documented mechanisms, not an instruction to install Steam Input or PlayMaker. [C-03, C-04, C-12]

### Working distinctions

| Term | Proposed meaning | Do not confuse with |
| --- | --- | --- |
| Action | A player-facing intention such as select, move or interact. | A particular physical button. |
| Binding | The relation between a device control and an action in a context. | Whether that action is presently allowed. |
| Activation rule | Press, release, hold, toggle, repeat, chord or sequence recognition. | A remappable location alone. |
| Responsiveness | A profile of accepted intent, delay, consistency and intelligible response. | One universal latency number or merely a high frame rate. |
| Early-intent buffer | Retention of a recent action request until an eligible state, subject to expiry and consumption. | Deliberately delaying every input, network jitter buffering or storing raw event history. |
| Device parity | A stated comparison of reachable functions and task demands across devices. | Identical mechanics, effort, trajectories or competitive results. |

These are analytic definitions for this candidate, not a standard taxonomy. In particular, sources 003 and 014 use “buffering” for different operations. [C-01]

### Context to declare before application

Record actual platform/build, input device and any simultaneous devices, preferred hand/use method, supported assistive input, display and listening context, action deadlines, ability to pause, multiplayer commitments and remapping persistence. Separate digital navigation, continuous pointing/steering and timing-dependent actions. A seated keyboard/mouse test does not establish switch, touch, eye-tracking, controller or VR access. The intended audience includes people whose preferred activation, reach or sustained-input capacity differs; do not assign a universal scheme based on a diagnostic label. [C-02, C-09–C-11]

## Core explanation and mechanisms

### Change the demand, not only its location

Microsoft's input guidance separates speed, complexity and duration barriers and recommends action-based remapping and alternatives to demanding activation patterns. Moving a difficult sustained hold to another key leaves its duration demand intact. The proposed application is to inspect the entire action transaction: acquisition, recognition, eligibility and cancellation, then change the relevant demand. That reasoning does not establish that every hold should become a toggle; a persistent toggle can itself create forgotten-state errors. [C-02, C-07, C-10]

The suggested causal chain is **reachable physical operation → recognized action → permitted game transition → understandable confirmation and recovery**. Remapping directly changes the first link; it does not prove the later links. A correctly bound action may remain inaccessible because it must be combined with another control, issued under an unchanged deadline, or confirmed in an inaccessible menu. [C-07, C-10]

### Preserve distinctions along the timing path

Diagnose separately: when the device event is acquired; when an activation rule recognizes it; when gameplay permits it; and when visual/audio/haptic output communicates the result. Source 014 is evidence about adding delay to a narrow mouse-aiming task, not about an optimal hold duration or early-input window. Source 003 documents retaining an unconsumed press inside a time window. Keeping an early request available may avoid a rejected action, but does not make the hardware event arrive earlier. [C-01, C-04, C-05, C-08]

A proposed early buffer therefore needs **ownership and validity**, not just a duration: which action owns the request, whether its target/context remains valid, which transition may consume it, and which events cancel it. “Execute the newest buffered command whenever possible” can fire after the player has changed goals. Conversely, dropping every early press can demand needless repetition. The benefit of either policy in an actual task remains a local test question. [C-08]

### Preserve input semantics across devices

Valve documents separate mouse-like and joystick-like action representations and action-origin queries. This supports treating relative displacement, continuously held direction and a digital selection as different semantic inputs. It does not prove one response curve for all devices. **Proposed parity audit:** compare whether each required task is reachable, whether the action produces the expected kind of change, what sustained effort/timing it requires, and whether the player can recover. Competitive assistance and matchmaking policy remain separate design decisions, not consequences of a remapping setting. [C-03, C-09]

## Design choices and alternatives

| Choice | Appropriate question and potential value | Cost, risk and simpler alternative |
| --- | --- | --- |
| Fixed scheme with accessible presets | Is a small, stable action set better served by understandable alternatives? | Presets may miss combinations of needs. Do not present them as universal access; permit additional configuration where practical. |
| Action-based remapping | Can the player move an action without changing its meaning, and see the new label everywhere? | Context conflicts, tutorial prompts, save migration and restore paths require verification. A label-only change is not a remap. |
| Press/hold/toggle alternatives | Is activation duration or simultaneous effort the actual barrier? | Toggle persistence and unintended repeat need visible state and cancellation. Retain a deliberate hold when essential to the chosen task, with a justified alternative where possible. |
| Short-lived eligible-action request | Are valid early intentions being discarded before an upcoming transition? | Stale targets, double consumption and post-pause execution are failure cases. Start with one named action and compare no buffering. |
| No early buffering | Is fresh intent essential, or does the state change the meaning of the action? | May require repeated presses. Prefer it for irreversible confirmations when a queued prior press would misrepresent consent. |
| Per-device interpretation | Are absolute/relative/held inputs genuinely different? | Additional configuration and test combinations. Avoid identical numeric settings merely to claim fairness. |
| Reduced action complexity or assisted operation | Would removing a chord, repeated tap or continuous steering demand preserve the intended decision? | May change challenge, agency or competitive policy. Treat as a separately evaluated alternative, not an invisible remap. |

This table is a set of conditional design inferences and hypotheses, not a ranked list of proven solutions. [C-07–C-11]

### Standards boundary

For **web content**, WCAG 2.2 SC 2.1.1 (Level A) requires keyboard-interface operation without specific keystroke timing, with an exception for functionality genuinely dependent on an input path. SC 2.5.2 (Level A) provides alternative ways to support single-pointer cancellation, including up-event completion with abort/undo or an essential down-event exception. Preserve those exceptions; do not restate either clause as a blanket native-game rule or certification result. [C-06]

## Application process

1. **Diagnose the action contract.** List required and optional actions, relevant states, timing/effort demands, failures and reversibility. Observe whether a reported miss is an unreachable binding, recognition failure, invalid state, delayed output or misunderstood result. Do not solve all of these by lengthening a buffer. [C-01, C-07, C-08]
2. **Choose a bounded change.** Select mapping, activation alternative, eligible-action retention, reduced complexity or no change. State the intended benefit and countercase before authoring. Preserve function rather than a particular motor gesture unless that gesture is genuinely the task. [C-07, C-10]
3. **Specify a recoverable configuration.** Stage changes, identify conflicts by context, update prompts, provide an accessible test and restore route, and distinguish account/device persistence. Follow the linked remapping pattern for the detailed recipe. [C-07]
4. **Specify timing semantics without a universal number.** Define request creation, expiry, consume-once behavior, eligibility and cancellation. Values must be local prototype variables; neither the PlayMaker examples nor the latency experiment supplies the correct window. [C-04, C-05, C-08]
5. **Prototype only under later implementation authorization.** Instrument device receipt, recognized action, state acceptance and output separately. Test on actual target devices at the intended display and access settings; record measurement method and uncertainty. [C-11, C-12]
6. **Evaluate and revise.** Keep changes that address the diagnosed barrier without unacceptable accidental actions, recovery loss or effort. An inconclusive small test is not proof of equivalent schemes. Remove or narrow a buffer when stale intent outweighs the benefit. [C-08–C-11]

## Patterns and genre adaptations

[Recoverable action remapping](../patterns/recoverable-action-remapping.md) — `GDR-CAND-20261010-P02-PAT-01` — owns the conditional configuration/restore recipe. [Feedback and game feel](feedback-and-game-feel.md) owns outcome confirmation; [Multimodal communication](multimodal-communication.md) owns access to prompts and state facts.

No genre entry is created or imported. **Illustrative conditional differences:** a deliberative selection may tolerate a confirmation step that would interrupt continuous steering; a short reaction deadline raises different questions than a persistent construction command. A hybrid should specify the current action contract instead of mechanically applying a genre label. These are examples, not genre evidence. [C-11]

## Examples and counterexamples

### Illustrative example — an inspection action with limited sustained input

A player navigates a space, chooses an object and inspects it. The default uses a held control while another control changes the view. First separate “keep inspection open” from “move view.” Offer a toggle alternative for the former and a separately adjustable view action; map both to the player's usable device controls. Show the current inspection state, update the prompt to the actual action origin and keep cancel/restore reachable during the mapping test. [C-07, C-10, C-11]

An early inspect request could be retained while a brief existing transition finishes, but only for the originally selected object and only while that object remains eligible. Leaving the object, opening a menu or cancelling clears that proposed request. A later object entering focus must not inherit it. Compare this with fresh-press-only operation; do not assume the buffered version is better. **This is an unimplemented, untested illustration.** [C-08, C-11]

### Strong counterexample — irreversible confirmation

A player presses a control while closing a settings panel. The next panel offers a destructive confirmation on the same control. A broad buffer could convert the earlier press into unintended confirmation. In this case, require a fresh eligible action or an explicit reversible transaction rather than retaining intent across the context boundary. The counterexample challenges a universal “buffer every action” rule; it is not an observed incident. [C-08, C-11]

### Documented example, not observed gameplay

Steam Input’s documented action-origin lookup is a concrete route for displaying the player's assigned control rather than a hard-coded button image. The documentation verifies the available concept, not that a particular game updates every prompt correctly. [C-03]

## Failure modes and constraints

| Failure sign to investigate | Proposed interpretation | Candidate response |
| --- | --- | --- |
| New binding works in play but not in menus | Context ownership or fallback differs. | Test the full navigation/restore path, not only the headline action. |
| The right action occurs after the player has left | Stale retained intent or unclear toggle state. | Narrow eligibility, clear requests at relevant boundaries, expose/cancel persistent states. |
| Remapping requires the unavailable default button | Recovery/bootstrap access was not designed. | Offer a genuinely reachable alternative route before accepting changes. |
| Cursor motion feels unlike continuous stick motion | Input semantics were forced into one transfer function. | Re-evaluate the appropriate representation and device-specific controls. |
| Fewer buttons but more accidental actions | Context multiplexing or activation ambiguity increased. | Separate actions or simplify the task rather than adding opaque timing rules. |
| Successful task but exhausting repeated input | Completion was mistaken for sustainable access. | Evaluate effort and chosen activation alternatives across a realistic session. |

These are prospective diagnostic cases, not measured failures in a build. Production work includes all prompts, input-state transitions, saves, disconnected devices, updated bindings and localization of action names. Cost magnitude is unknown. Do not collect raw voice, gaze or device-identifying traces merely because an alternative input is being evaluated; justify necessary data and consent separately. Multiplayer assistance policy and anti-cheat compatibility require their own owners. [C-07–C-11]

## Playtest and validation

**PROPOSED — NOT RUN.** No prototype, recruitment, participant session, latency measurement or statistical reanalysis occurred. The following is a research design, not permission to execute. [C-11, C-12]

**Comparison A — remapping and activation.** Compare an existing accessible preset, action-only remapping and remapping with the relevant activation alternative. Use the same required decisions and targets. Recruit people who actually use the relevant devices/activation methods, including people who need an alternative to the default; do not use a reviewer with an artificially constrained hand as a substitute. Counterbalance comparable tasks where feasible and log practice and chosen settings. Require an accessible baseline; never force a known painful configuration for a control condition.

**Measures:** independent completion of required actions; incorrect/accidental activations; ability to name and locate the mapped action; restore/cancel success; retries; task time; perceived effort, control and confidence, reported separately. Define a critical failure as loss of an essential action or recovery route in the exercised configuration. Any such failure blocks advancement of that configuration regardless of average speed. A preference advantage without recovery/access evidence does not validate the recipe.

**Comparison B — early intent retention.** Compare fresh-press-only input with a named action’s expiring, consume-once request policy. Choose candidate windows from the actual action transition and instrumented receipt distribution, not a generic standard. Include early valid presses, repeated presses, target changes, cancellation, menu transitions, pause/resume and unavailable states. Distinguish technical end-to-end delay from the number of intentions accepted.

**Falsification:** reject or narrow retention when it executes an action after intent/context is invalid, duplicates a one-shot request, or adds no useful reduction in failed intended actions while increasing mistakes. Improved acceptance does not prove lower hardware latency. If benefit depends on practice, one device or a particular action, retain that limit. Do not infer equivalence from a non-significant result.

**Sample and decision policy:** plan formative coverage by required device/access/context combinations, not an arbitrary representative sample size. Before a confirmatory study, choose the primary outcome, acceptable regression, precision/power rationale and stopping rule using local variability; none is approved here. Report observed cases and uncertainty rather than a single parity score. Participants may pause, adjust settings or stop without penalty. All procedures and proposed stop rules remain hypotheses. [C-11]

## Claim ledger

Claim IDs are local to this entry. Confidence concerns the stated scope, not source prestige. An inference is not a validated outcome; repeated references are not independent corroboration.

### C-01

**Claim:** Mapping, activation, intent retention and output delay are distinct design decisions; a universal responsiveness number would hide those distinctions.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, Background; GDR-SRC-20261010-P02-002, action representations; GDR-SRC-20261010-P02-003, How it works; GDR-SRC-20261010-P02-014, §4.1.
**Applicability and contrary limits:** Definitions organize diagnosis. Different uses of “buffering” must not be pooled as one mechanism.
**Confidence:** Moderate: distinctions follow the inspected mechanisms; the analytic vocabulary is proposed.
**Unresolved:** Which stage causes the actual reported failure?

### C-02

**Claim:** Microsoft recommends addressing speed, complexity and duration demands as well as action-based remapping and updated input labels.
**Class:** `practitioner-heuristic`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, Background and Implementation guidelines.
**Applicability and contrary limits:** Official access guidance; remapping alone does not establish usability or eliminate timing demands.
**Confidence:** High for accurate attribution; individual effectiveness remains untested.
**Unresolved:** Which demand prevents the intended player from performing the action?

### C-03

**Claim:** Steam Input documentation distinguishes mouse-like and joystick-like action data and provides action-origin information for assigned controls.
**Class:** `observed-example`. **Evidence and exact locator:** GDR-SRC-20261010-P02-002, absolute_mouse versus joystick_move; Step 3.1, action origins.
**Applicability and contrary limits:** Observed documentation artifact, not tested API behavior or shipped-game observation. No all-platform claim.
**Confidence:** High for documented concepts; runtime verification not performed.
**Unresolved:** Does a later implementation preserve the intended semantics and update every prompt?

### C-04

**Claim:** The inspected PlayMaker documentation describes buffered presses using a timestamp, a time window and consumption state.
**Class:** `observed-example`. **Evidence and exact locator:** GDR-SRC-20261010-P02-003, How it works and buffer/check/consume action descriptions.
**Applicability and contrary limits:** Documentation mechanism only. It supplies no established optimum window or universal accessibility benefit.
**Confidence:** High for the documented mechanism, not implementation correctness.
**Unresolved:** What expiry and eligibility policy fits the intended action?

### C-05

**Claim:** In a controlled mouse-aiming game, adding delay worsened measured performance; its settings are experimental conditions, not acceptable-latency thresholds.
**Class:** `empirical-evidence`. **Evidence and exact locator:** GDR-SRC-20261010-P02-014, PDF pp. 8–11 §§3.2, 4.1–4.4 and results; p. 18 §6.5.
**Applicability and contrary limits:** 36 participants, mostly students; matched stationary aiming across three perspectives; zero or 150 ms added to a nonzero baseline. Baseline mean 47.75 ms (SD 13.12) was estimated from 20 captures. Not a jitter or device-parity study.
**Confidence:** Moderate for the narrow experiment; no universal sensitivity rule follows.
**Unresolved:** Transfer to other actions, devices, latency distributions and participant groups.

### C-06

**Claim:** WCAG 2.2 specifies keyboard access and pointer-cancellation criteria for applicable web content, with explicit exceptions.
**Class:** `formal-standard`. **Evidence and exact locator:** GDR-SRC-20261010-P02-004, dated Recommendation 2024-12-12, SC 2.1.1 and 2.5.2, both Level A.
**Applicability and contrary limits:** Web-content conformance scope only. Preserve path-dependent-functionality and essential-down-event exceptions; not native-game certification.
**Confidence:** High for the clauses; applicability requires an actual product assessment.
**Unresolved:** Which portions of a future product fall within the claimed web conformance scope?

### C-07

**Claim:** Stage remapping changes with reachable testing, conflict resolution, updated prompts and recovery before treating a configuration as usable.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, action remapping/labels; GDR-SRC-20261010-P02-002, action origins; GDR-SRC-20261010-P02-004, cancellation as a web-scoped precedent.
**Applicability and contrary limits:** Bridge: moving an action is insufficient if the player cannot identify, test or undo the new configuration. Transactional recipe is a synthesis, not a source-mandated implementation.
**Confidence:** Moderate for the risk-control rationale; no comparative recipe study.
**Unresolved:** Can the least complex accessible configuration offer the same recovery with less burden?

### C-08

**Claim:** An early-intent buffer may reduce rejected intended actions, but requires context validity, expiry and single consumption to avoid stale execution.
**Class:** `hypothesis`. **Evidence and exact locator:** GDR-SRC-20261010-P02-003, timestamp/window/consumption mechanism; contextual validity and reject policies are original P02 proposals.
**Applicability and contrary limits:** Not a universal prescription; fresh intent can be preferable for destructive or context-changing actions. No buffer efficacy study inspected.
**Confidence:** Low for net player benefit; mechanism does not establish optimal policy.
**Unresolved:** Does the proposed action-specific policy reduce misses without increasing unintended actions?

### C-09

**Claim:** Evaluate device parity as explicit function/task comparisons rather than identical curves or presumed competitive equivalence.
**Class:** `inference`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, alternate inputs; GDR-SRC-20261010-P02-002, distinct action representations; GDR-SRC-20261010-P02-014, narrow input/task sample.
**Applicability and contrary limits:** Different devices and assists can change effort, precision and policy. Reachable functionality does not prove identical outcomes.
**Confidence:** Moderate for the reasoning; empirical cross-device parity remains untested.
**Unresolved:** Which task costs and competitive constraints matter in the actual product?

### C-10

**Claim:** Alternative activation and simplified action structures should be evaluated with users of those methods, not assumed effective from remapping alone.
**Class:** `hypothesis`. **Evidence and exact locator:** GDR-SRC-20261010-P02-001, alternative input demands; GDR-SRC-20261010-P02-004, keyboard path exception as a scoped boundary.
**Applicability and contrary limits:** The proposed toggle, switch, dwell or other adaptation must preserve the intended decision and have a usable cancel/restore path. No universal device prescription.
**Confidence:** Low for a particular alternative’s benefit; guidance supports the question, not an outcome.
**Unresolved:** Does the adaptation reduce the actual barrier without unacceptable accidental action or agency cost?

### C-11

**Claim:** The examples, diagnostic workflow, cost categories and playtests are proposed local applications, not observed game behavior or validated protocols.
**Class:** `hypothesis`. **Evidence and exact locator:** Original P02 synthesis under the supplied dispatch, lines 8–12 and 22–24; source bridges are identified in C-01–C-10.
**Applicability and contrary limits:** All implementation and participant tests are NOT RUN. No fixed sample, timing window or success percentage is a studio-approved setting.
**Confidence:** Low for predictive validity; practical feasibility remains to be tested.
**Unresolved:** Study-owner review, actual device/access coverage, measurement validity and production cost.

### C-12

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
**Claims using this record:** C-01, C-02, C-07, C-09, C-10. **Limits:** Recommendations, not a normative standard or a verified certification obligation. No device or remapping interface was tested here; numerical suggestions are not adopted.
**Independence/deduplication:** Same issuer and guideline family as sources 005–010; not independent empirical corroboration.
**Rights:** Publisher terms; reuse license not independently audited. Paraphrase only; no example images reproduced.

### GDR-SRC-20261010-P02-002

Valve. [Getting Started for Developers](https://partner.steamgames.com/doc/features/steam_controller/getting_started_for_devs?l=english). **Publisher:** Steamworks documentation. **Publication/update:** publication/update unknown. **Edition/build:** Unnumbered live Steam Input documentation; SDK/build not specified.
**Type:** Official platform technical documentation. **Locators inspected:** Step 1: in-game actions; discussion of absolute_mouse versus joystick_move (retrieved lines 458–468); Step 3.1: API overview, action sets, action data and action origins (lines 509–525).
**Claims using this record:** C-01, C-03, C-07, C-09. **Limits:** Describes Steam Input, not every operating system. No SDK, controller, sensitivity curve or runtime behavior was exercised.
**Independence/deduplication:** Separate issuer from Microsoft. Canonical deduplication key is the same URL without the language query; this is one document, not two sources.
**Rights:** Publisher terms; no reuse license audited. Paraphrase only.

### GDR-SRC-20261010-P02-003

Hutong Games. [Buffered Input](https://docs.hutonggames.com/actions/input-actions/buffered-input/). **Publisher:** Hutong Games documentation. **Publication/update:** publication/update unknown. **Edition/build:** Unnumbered PlayMaker documentation; package version unknown.
**Type:** Official tool technical documentation. **Locators inspected:** Buffered Input; How it works; action descriptions for buffering/checking/consuming input; timestamp, time window and consumed state (retrieved lines 91–171).
**Claims using this record:** C-01, C-04, C-08. **Limits:** Explains an early-intent retention mechanism. Does not establish an optimal window or measured player benefit. Suggested timing values in the documentation are deliberately not promoted to library defaults.
**Independence/deduplication:** Independent tool documentation; not an experiment and not evidence of a Unity implementation in this task.
**Rights:** Publisher terms; no reuse license audited. Paraphrase only.

### GDR-SRC-20261010-P02-004

World Wide Web Consortium (W3C). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). **Publisher:** W3C. **Publication/update:** 2024-12-12. **Edition/build:** W3C Recommendation, dated 12 December 2024; not asserted to be the latest edition.
**Type:** Normative web-content accessibility recommendation. **Locators inspected:** Success Criteria 1.2.2 Captions (Prerecorded), Level A; 1.3.3 Sensory Characteristics, Level A; 2.1.1 Keyboard, Level A; 2.5.2 Pointer Cancellation, Level A. Header establishes dated edition.
**Claims using this record:** C-06, C-07, C-10. **Limits:** Normative statements retain web-content scope and their exceptions. Not a blanket native-game requirement, legal opinion, console certification rule or guarantee of accessibility. No complete conformance assessment performed.
**Independence/deduplication:** Independent normative issuer; related understanding/technique documents were not all inspected.
**Rights:** W3C publisher terms; license detail not separately audited. Only brief attributed paraphrases; no reproduced document.

### GDR-SRC-20261010-P02-014

David Halbhuber, Philipp Schauhuber, Valentin Schwind and Niels Henze. [The Effects of Latency and In-Game Perspective on Player Performance and Game Experience](https://epub.uni-regensburg.de/55325/1/3611070.pdf). **Publisher:** ACM; University of Regensburg repository. **Publication/update:** November 2023; repository deposit 2024 is not publication date. **Edition/build:** Proceedings of the ACM on Human-Computer Interaction 7, CHI PLAY, Article 424; 22-page PDF.
**DOI:** `10.1145/3611070`; the inspected access route is linked above.
**Type:** Original controlled game experiment. **Locators inspected:** PDF p. 8 (424:8), §3.2 baseline measurement and §4.1 conditions; pp. 9–10 §§4.2–4.4; p. 11 results/Figure 5; p. 18 §6.5 limitations. Text and methods/results page images inspected; repeated p. 18 screenshot route failed, but its text was accessible.
**Claims using this record:** C-01, C-05, C-09. **Limits:** 36 participants, mostly students; matched stationary mouse aiming/shooting tasks across three perspectives. Zero or 150 ms added delay, not zero end-to-end latency. Baseline mean 47.75 ms, SD 13.12, from 20 captures. Not a jitter study, all-device comparison or universal acceptable-latency threshold.
**Independence/deduplication:** Separate experiment from other empirical records. Its use of input buffering to add delay differs from source 003’s early-intent retention; this is terminology, not a contradictory result.
**Rights:** CC BY 4.0 in institutional record. No PDF or figures redistributed.


## Open questions and change history

| Subtopic | Researched coverage | Remaining gap and next discriminating question |
| --- | --- | --- |
| Mapping and remapping | Current vendor guidance and documented semantic action representations. | No actual remapping usability comparison; does recovery remain reachable after context/device changes? |
| Responsiveness | Distinct timing stages and one narrow controlled latency experiment. | No jitter, console/touch/VR or long-session threshold study; which stage dominates this task? |
| Buffering | Documented early-input mechanism, contrasted with artificial-delay usage. | No tested optimal window; which eligible intentions should survive which transitions? |
| Device parity | Functional/task framework and platform semantic differences. | No measured equality or competitive-policy finding; what comparison is actually promised? |
| Alternative inputs | Access-demand rationale and conditional adaptations. | No direct switch/eye/voice device study in this corpus; can actual users operate and recover? |

**Missing dependencies:** parent-reviewed P01 bytes and exact corrected numerical scope; Foundations learning/onboarding and movement/traversal; Worlds action staging; current canonical index and pending allocations. IDs for unseen entries are not invented. Related P02 entries are draft companions, not reviewed shared rules.

**Contradictions:** packet `P02-CON-03` owns the apparent buffering/timing conflict. It is primarily a definition/context difference, with local performance tradeoffs unresolved.

**History:** 2026-10-10, version 0.1.0, candidate revision `initial-draft-1`; no predecessor P02 artifact observed. No conceptual ID replacement, release or approval. Author self-review is recorded in the [P02 packet](../reviews/full-run-20261010-p02-review-packet.md). Next decision: independent review of the claims and recovery/buffering boundaries, then Coordination reconciliation against actual reviewed dependency bytes.
