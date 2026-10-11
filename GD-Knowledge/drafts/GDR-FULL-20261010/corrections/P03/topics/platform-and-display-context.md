---
id: GDR-CAND-20261010-P03-TOP-02
kind: topic
title: Platform and display context
version: 0.1.0
candidate_revision: review-correction-1
status: draft
id_scope: run-scoped-temporary
run_id: GDR-FULL-20261010
batch_id: P03
attempt_id: P03-authoring-20261010-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-11'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus inspected selected first-wave reviewed drafts; archive SHA-256 e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef
aliases:
- device context
- couch play
- small-screen presentation
- cross-device presentation
tags:
- platform
- display
- input
- audio
- accessibility
- xr
- context-switching
- localization
related_topics:
- GDR-CAND-20261010-P03-TOP-01
related_patterns:
- GDR-CAND-20261010-P03-PAT-01
- GDR-CAND-20261010-P03-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P03-008
- GDR-SRC-20261010-P03-009
- GDR-SRC-20261010-P03-010
- GDR-SRC-20261010-P03-011
- GDR-SRC-20261010-P03-012
- GDR-SRC-20261010-P03-013
- GDR-SRC-20261010-P03-014
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: 4d7ab18d1d7da204bbc9ee15a3f92a6828cee31440c77ed489b641e3a488e4b0
supersedes: null
change_summary: Independent precision review; see local correction history and receipt.
hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
---

# Platform and display context

**Draft 0.1.0, candidate revision `review-correction-1`; not released knowledge or a compatibility certificate.** This entry helps adapt presentation to the actual viewing, listening and interaction situation. [Camera and framing](camera-and-framing.md) owns view authority, composition and authored camera motion; this entry owns the surrounding conditions and transitions that change whether those choices remain usable. No platform is treated as a genre. [C-01, C-12, C-16]

## Decision and scope

Decide which aspects of a game can remain constant across contexts, which need a different presentation or interaction route, and which contexts are not yet supported. Included: small screens and handheld use; couch viewing; changing windows/aspect ratios and display cutouts; touch, controllers and mixed input; VR/AR presentation distinctions; sound-off/noisy environments; and conceptual performance/response constraints. Excluded: engine integrations, platform submission, a complete input or audio topic, medical advice, optical calibration, and numerical requirements for every display or population. [C-01, C-12, C-16]

**Working recommendation:** preserve the intended task, necessary information and the player's access choices, while allowing context-specific presentation and device-local technical settings. Preserve meaning rather than insisting on identical pixels or identical gestures. Conversely, do not silently change game rules, reveal extra knowledge or remove the player's choices merely because the display or active input changed. This is an application inference; the complete adaptation process is not empirically validated by the inspected sources. [C-09, C-10, C-12]

### Working vocabulary

The definitions are proposed analytic conventions, not a formal platform standard. [C-01]

| Term | Working meaning | Why it is kept separate |
|---|---|---|
| Platform | A hardware/software environment with particular capabilities and distribution constraints. | A platform name does not identify the current screen, input, listening route or access requirements. |
| Presentation context | The actual display/window, posture/distance, input routes, listening situation, preferences and workload at a given time. | One device can have several contexts within one session. |
| Native/display resolution | The display's output pixel structure or configured output mode. | It need not equal the game's internal render resolution or the text's final rendered size. |
| Effective content region | The region available after windowing, aspect treatment, cutouts, overlays and chosen layout. | Scaling a full-frame mock-up does not test obstruction or usable focus navigation. |
| Available versus active input | A device can be connected or supported without being the input currently used. | Mixed input is possible; an incidental event need not justify removing another route. |
| Access intent | A player's meaningful preference, such as readable text, reduced decorative motion or a chosen information route. | A copied numeric value may not realize the same intent on another screen. |
| Context profile | A proposed collection of presentation choices for a named situation, with visible overrides and recovery. | It is not a diagnosis, a mandatory mode, or permission to change game rules. |
| Response and frame timing | Response concerns an action-to-visible-result path; frame timing concerns the sequence of displayed updates. | A nominal framerate alone does not identify that whole response path. |

For a later application, name the supported contexts and the evidence available for each. “PC,” “mobile,” “console” and “XR” alone are incomplete specifications. State what is unknown rather than filling it with the studio's current equipment or a generic adult desk setup. [C-01, C-11]

## Core explanation and mechanisms

### The reusable chain is task → representation → usable action → recoverable transition

The same event might be presented in a different location, at a different scale, through a different input prompt or in another information route without changing its meaning. That possibility is not proof the adaptation succeeds. Check each link rather than treating a responsive layout as completion. [C-09, C-10, C-12]

| Link | Existing support | Unresolved applied question |
|---|---|---|
| Identify the actual context and input capabilities. | Current platform recommendations and documented input distinctions, C-02/C-07. | Which changes matter to this task, and which can be ignored without hiding a failure? |
| Select a presentation that fits the content region and chosen access intent. | Scoped text/cutout guidance, C-04/C-08; inspected P01 corrections. | Can the player read, navigate and act, including with expanded/localized content? |
| Retain the necessary information when a channel is unavailable or unwanted. | Audio options in C-05 and reviewed P01 cue-equivalence framing. | Is the alternative usable under the actual attention demands, not merely technically present? |
| Change context without losing meaningful state or the usable control route. | C-02/C-07 motivate the need; the full state-preservation policy is original synthesis. | Are selection, task progress, preferences and recovery preserved through the transition? |
| Deliver a useful experience without unacceptable cost. | No inspected source tests this complete chain. | Does the profile add value over a simpler flexible layout and explicit settings? |

### Guidance numbers are not interchangeable

The following comparison deliberately preserves units, scope and authority. It is not a proposed shared minimum. [C-03, C-04, C-13]

| Source and authority | Exact bounded example | What it does not justify |
|---|---|---|
| Valve compatibility-program criteria, not a general accessibility standard | The Deck-specific text test describes no less than 9 pixels of font-character height at 1280×800 and a 12-inch/30-cm viewing distance; it recommends 12 pixels where possible. | A couch-play text target, a guarantee for low-vision users, or a rule for every handheld. The page says Steam Machine display tests are not performed because displays vary. |
| Microsoft XAG 101, official accessibility guidance | Console launch defaults are described using body height: at least 26 pixels at 1080p and 52 at 4K. Player-controlled scaling is separate. | Nominal font-point size, WCAG CSS pixels, a maximum, or the physical/angular size needed on every HMD. |
| Inspected corrected P01 shared candidates | Normative web provisions retain their individual conformance levels, units and exceptions. XAG rendered body height remains a different measure. | Importing a web pointer-target or contrast provision into native gameplay without checking its applicability. |

A difference between two numbers is not automatically a contradiction: the authority, test population, measurement and purpose may differ. A vendor badge process can be narrower than a project's accessibility goals. Do not erase the lower or higher number, average them, or choose whichever is cheaper. Identify the applicable program separately from the local usability decision. [C-13]

### Display and attention are part of the interaction budget

A design can make text larger yet require more scrolling, hide an adjacent control or cover the world event it explains. Moving every alert toward the middle can preserve noticeability while blocking the action the player needs to see. These are plausible tradeoffs to test, not a universal finding that central or peripheral placement is better. The camera topic records the inspected HMD attention/search studies and their incompatible task demands; they must not be used as a general mandate for central interfaces. [C-09, C-11; camera C-07/C-08]

Likewise, touch can occupy the same visible region used for a decision, while a distant controller context can make a previously reachable touchscreen irrelevant. The key decision is not whether a device technically has touch. It is whether the current player can use the intended action route while obtaining the necessary information. This is a task-based inference from the documented mixed-input possibilities, not an argument that all touch or controller layouts are equivalent. [C-07, C-09]

## Design choices and alternatives

The context matrix is a set of conditional design proposals. Each row identifies a comparison and a failure condition; it does not assign a stereotyped user to a device. [C-09–C-12]

| Context | Candidate adaptation | Cheaper or different alternative | Failure/exit condition |
|---|---|---|---|
| Small handheld display | Reduce simultaneous information, allow text/layout scaling and keep essential controls clear of obscured regions. | A stable single-column or paged presentation with the same task facts. | Enlargement removes a required action, creates a reading/navigation trap or needs inaccessible touch. |
| Couch play on a distant display | Evaluate actual reading and focus navigation; retain controller-only access to settings and text entry where supported. | A user-selected readable preset rather than inferred distance. | Readability depends on moving closer, or a launcher/keyboard step cannot be operated from the chosen route. |
| Windowed, ultrawide or changed aspect ratio | Distinguish scene framing from UI layout; preserve intended information at each region shape. | Stable content bounds with an explicit aspect treatment, after checking unused space and scale. | Wider or narrower view changes permitted knowledge or crops important content without review. |
| Touch with controller/keyboard available | Keep supported routes usable; respond to actual input and avoid destructive prompt/layout oscillation. | An explicit user-selected prompt/layout mode while accepting other inputs. | One incidental input event removes the route needed to recover or changes the action meaning. |
| Sound off, quiet listening or environmental noise | Offer independent audio choices and usable non-audio access to essential facts; retain chosen narration/captions. | Reduce nonessential competition rather than increasing overall level. | Essential information depends on an unavailable channel or an alternative cannot be interpreted while acting. |
| Immersive HMD | Treat physical tracking, virtual motion, readable content placement and optional locomotion separately. | A contained presentation or an alternate interaction when it serves the task. | Assumptions from a flat screen are transferred without actual headset/access evaluation. |
| AR or passthrough environment | Consider real-world visibility, content anchoring and obstruction as additional constraints. | Smaller or less intrusive presentation where appropriate, or explicit unsupported-context disclosure. | Task content prevents necessary awareness or requires unverified tracking/occlusion behavior. |
| Constrained or varying performance | Test the final presentation/response under representative workload; reduce nonessential cost without deleting required information. | Simplify scene/effects or bound supported configurations. | Nominal averages hide unusable moments, or a fallback breaks feedback/readability/access intent. |

### Small screens and couch distance

Physical size, content area, viewing distance, glare, character rendering and reading needs should be recorded together. Do not prescribe a universal distance or simply multiply every element until it fits. Evaluate what remains simultaneously available and which actions require scrolling or a mode change. A mock-up on a large desktop monitor is a design artifact, not evidence that the handheld or couch task is usable. These proposed checks extend the source guidance; they are not measurements already obtained. [C-04, C-09, C-11]

A menu with many choices may benefit from progressive disclosure, but fewer visible choices can also hide relevant comparisons. Preserve a route to the necessary information and an understandable return location. P01 owns interface hierarchy; this topic owns whether its chosen realization still works in the context. [C-09]

### VR, AR and flat-screen boundaries

A head-mounted display can present a small virtual window, a surrounding virtual world, or augmented content tied to a real environment. These should not inherit the same framing and placement recipe. The historical Apple transcript is pertinent to stable spatial content and motion in a virtual window; it is not an inspected current specification for every VR/AR device. The current Apple HIG Motion page could not be read beyond its JavaScript requirement, so that freshness gap remains explicit. [C-06]

For later design, distinguish platform tracking behavior from authored movement and decorative effects. Do not infer that a “reduced motion” preference means immobilizing the world relative to the head. Record whether the player can comfortably reach, see and read the necessary content in their chosen posture; where that is not known, narrow support claims and evaluate an alternative. Precise placement distances, angles, brightness, refresh rates and tolerable latency require device/task-specific evidence, not numbers borrowed from an adjacent screen guideline. [C-06, C-11]

### Listening environment and optional channels

Source guidance supports separate category controls, mono options and protection of assistive speech. The platform decision is what happens when those choices combine with the current display and task. A readable caption may preserve a fact while drawing gaze away from an action; a haptic indication may be unavailable or insufficiently specific; an audio-only alternative may be appropriate for one user and unusable for another. Required information and intended emotional response remain separate. [C-05, C-09]

Do not respond to environmental noise by universally recommending louder output. Offer the player's chosen information routes and inspect competing content first. Automatically recording a microphone or inferring a hearing condition is not required by this recipe and is not authorized here. A user-selected listening profile is a less intrusive candidate to compare, not a guaranteed solution. [C-10, C-12]

### Hardware performance without invented thresholds

Record the actual output mode, internal rendering, presentation of UI/text, frame-time trace, input path and workload before making a claim about response. Consider first launch, normal activity, crowded or effects-heavy scenes, sustained sessions and transition states as proposed test cases. No benchmark, thermal behavior, battery result, frame-time distribution or end-to-end latency was measured in P03. [C-11, C-15]

A platform's stated compatibility-performance criterion is a submission-context rule, not proof of pleasant motion, responsiveness or representative usability. This topic does not turn that rule into an engine setting. When performance is inadequate, the proposed priority is to compare nonessential cost reductions against the task/access requirements, not to delete the only readable cue or disable the player's assistance without notice. The exact priority order requires the later game's own decision. [C-03, C-11]

## Application process

1. **Describe the task and minimum information.** Identify facts, actions, allowed uncertainty and the state that must survive a change. Keep desired emotion separate from necessary information.
2. **Create a bounded context inventory.** For each supported case, record display/content region, input routes, posture/viewing assumptions, listening route, access choices, language and workload. Mark unverified cases explicitly.
3. **Separate preferences from local realization.** Retain the player's meaningful choices; keep device-specific graphics settings separate where the platform recommends this. Do not assume copying one scale value preserves readability, or that a new device authorizes resetting assistance.
4. **Choose the minimum adaptation.** Compare flexible layout/explicit settings with a named profile. Make profile selection and overrides accessible. Use supported/active inputs rather than a device stereotype to decide prompts.
5. **Define context-change behavior.** Decide which state persists, what must be reevaluated, whether a safe interruption is possible, and how the player can recover. In a live shared session, do not promise a global pause that the design cannot provide.
6. **Evaluate on the declared contexts after separate authorization.** Test the final rendered result and active input route. Revise or narrow support when the task or a chosen access preference cannot be maintained.

All steps are proposed application guidance. They do not authorize code, device configuration, telemetry collection, player studies or platform submission. [C-09–C-16]

### Calibration record before adopting any value

| Choice | What to record | What a later decision needs |
|---|---|---|
| Text and controls | Final rendered measurement and unit; physical/content region; viewing context; language/font; chosen scale; focus and input route. | Evidence that required information/actions remain usable, not merely that a pixel minimum is met. |
| Scene field of view | Projection convention, aspect treatment, display mode, information revealed and camera-control policy. | A task-specific preference/visibility comparison; no universal lens or vignette value. |
| Performance | Representative scene/workload, display and render paths, frame-time variation and measured action-to-feedback path. | Locally justified response/quality tradeoffs, including access features at chosen settings. |
| Listening presentation | Chosen categories, output route, captions/narration, environmental assumptions and essential event meanings. | Usable information under acceptable listening conditions, not a universal decibel target or presumed emotional parity. |
| Profile switching | Trigger, prompt behavior, preserved semantic state, changed local settings and recovery route. | Evidence that the change does not strand the player or override preferences. |

These are measurement questions, not measurement results or approved acceptance thresholds. [C-11, C-15]

## Patterns and genre adaptations

[Task-preserving context profiles — GDR-CAND-20261010-P03-PAT-02](../patterns/task-preserving-context-profiles.md) turns the transition decision into a proposed recipe. [Recoverable camera assistance — GDR-CAND-20261010-P03-PAT-01](../patterns/recoverable-camera-assistance.md) applies when the chosen profile changes view control or motion options. Neither validates this topic. [C-12]

The inspected P01 pattern `GDR-CAND-20261010-P01-PAT-01`, Redundant critical-state cues, owns cue encoding and usable information alternatives. P03 does not create a duplicate pattern: it owns preservation and recovery across context changes. P02 controls, feedback and multimodal candidates remain uninspected submitted work. Genre adaptations are illustrative only; a timed precision task and an untimed comparison task can need different layouts even on the same platform. `related_genres` remains empty. [C-09, C-12]

## Examples and counterexamples

### Illustrative worked example: a handheld inspection becomes couch play

A player compares two equipment items, with one selected and a description expanded. They dock a handheld to a television and use a controller. The intended task, comparison values, selected item and access choices are unchanged; the display area, viewing context and active inputs differ. This is a synthetic scenario, not a recorded game session. [C-12, C-15]

The proposed profile retains comparison state, presents controller-operable focus and text entry, and offers a couch-oriented layout that can be adjusted or declined. It does not assume that the handheld touchscreen remains reachable. Graphics choices are device-local where appropriate; a readable-text preference is carried as intent and verified in the new realization rather than copying its prior numeric scale. During the change, the player must have an intelligible way to resume the comparison or return to a stable screen. [C-02, C-07, C-10, C-12]

Compare this with a single flexible layout that already works in both contexts. If no meaningful task/access failure occurs and the profile adds configuration burden, omit the extra profile. If a controller prompt updates but focus disappears, the transition fails even though the right button glyph is now visible. If larger text hides the decisive comparison property, the adaptation has not preserved the task. [C-09, C-12, C-15]

### Illustrative worked example: an important event during sound-off play

A player receives notice that a device has finished processing. The required fact is completion and the action available next; the intended ambience is optional. A non-audio representation preserves those facts at the current text/layout settings. It need not claim to reproduce the same atmosphere or disclose an unknown cause. A headset or haptic channel is not assumed available. The proposed comparison checks interpretation during the actual task rather than asking only whether a tester could find the caption in a paused screenshot. [C-05, C-09, C-15]

### Strong counterexample: inferred profiles that keep changing

A player intentionally mixes a keyboard shortcut with a controller. An automatic “keyboard mode” hides controller prompts and rearranges focus, then switches back on the next stick movement. Another player uses a touch event only to dismiss an overlay while still relying on a controller. A rule that treats the last event as total context knowledge can make both situations worse. Consider a stable layout, delayed prompt switching or an explicit preference while accepting supported inputs. The exact trigger policy is untested, not a universal debounce duration. [C-07, C-10, C-12]

### Documentary boundary case

The current Valve text criterion is explicitly Deck-specific, whereas the page declines a comparable Steam Machine display test because output displays vary. That is evidence of a program boundary, not proof that couch interfaces need no assessment. The recommendation to evaluate couch readability is a local inference, not an assertion that Valve certified it. [C-03, C-13]

## Failure modes and constraints

| Failure sign for a later test | What might be wrong | Proposed repair or limit |
|---|---|---|
| Text nominally meets a guideline but the comparison cannot be completed | Wrong measurement, context, rendering or attention assumptions. | Measure final output; evaluate the actual task and chosen scale. |
| Options cannot be reached before play | Startup route relies on an unavailable input or inaccessible presentation. | Provide an operable initial route; do not make later configurability an excuse. |
| A cutout, touch region or overlay covers a critical control | Full-frame mock-up mistaken for effective content area. | Reflow the relevant content and recheck focus/action coordinates. |
| Input prompts oscillate or an alternate route disappears | Availability and activity confused, or adaptation too aggressive. | Use stable prompts/explicit choice; accept mixed input where supported. |
| New device restores unwanted motion or disables captions | Technical settings and personal preferences were bundled together. | Separate intent, local realization and transient state; expose recovery. |
| Mono/sound-off play loses a required direction or event | The chosen alternative does not preserve the task facts. | Reauthor a usable representation, not just a decorative icon. |
| A performance fallback erases a critical effect or UI element | Cost reduction treated as independent of information design. | Protect the required information or narrow supported workload/context. |
| Profile works in one language but clips or changes meaning in another | Layout tested without representative expansion, script and direction. | Evaluate the final localized task; avoid assuming all text can be shortened. |

These are proposed failure cases, not observed P03 results. [C-09–C-15]

**Accessibility:** consult people who use the actual alternatives; toggling sound off or using a controller as an author is not equivalent to representative access evaluation. Preserve preferred combinations rather than treating a named accessibility preset as a population label. The inspected P01 correction also prevents a native touch or controller target from inheriting a WCAG CSS-pixel threshold without its scope and exceptions. [C-09, C-13, C-15]

**Localization and culture:** evaluate expanded strings, supported scripts, reading direction, controller naming, text entry and nontext meanings in context. Do not change world-relative directions merely by mirroring an interface. A caption or voice alternative may alter interpretation; preserving a fact does not guarantee emotional equivalence. Detailed localization and audio design remain P05 dependencies. [C-09, C-14]

**Ethics and production:** a useful profile should reduce effort rather than create an obligation to disclose disability, grant microphone access or submit behavioral telemetry. Limit unsupported claims honestly. The context matrix can grow combinatorially; prioritize high-consequence transitions and representative combinations while logging what remains untested. The necessary test effort, energy use and performance cost were not measured. Fewer supported contexts with a clear boundary can be more responsible than unverified universal support. [C-10, C-14, C-15]

## Playtest and validation

**PROPOSED — NOT RUN.** No device benchmark, engine code, participant session, sound recording, physiological measure, remote telemetry or certification test occurred. A later owner must approve the protocol, settings, participant safety, inclusion/accommodations and analysis. [C-15, C-16]

**Primary question:** does the proposed adaptation preserve the task and chosen access intent across declared contexts better than the simplest viable shared presentation?

**Comparison:** (A) a baseline flexible layout with ordinary explicit settings; (B) the proposed profile with accessible overrides and recovery. Use the same content, task facts and actions. Test cold start separately from context switching, and separate first exposure from later switching. Dock/undock, change window shape, attach/detach inputs, mix inputs, use larger text/localized content and select sound-off or preferred listening modes where they are legitimate supported cases. No participant is required to accept an uncomfortable intensity or relinquish necessary assistance for a control condition. [C-15]

**Control confounds:** hardware performance, familiarity with the device, reading language, device-switch order, task complexity and assistance can all explain a difference. Record them rather than attributing every outcome to the profile. Use matched tasks with changed values/locations where appropriate and inspect comprehension separately from the chosen action. Avoid turning the “test” into an answer-leading demonstration. Sample and meaningful margins must follow the local question and uncertainty, not a generic default count. [C-15]

**Measures:** completion of the intended comparison/action; essential-fact interpretation; loss of focus/selection/progress; recovery success; preference retention; incorrect prompt/action association; reading/navigation effort; missed events; reported control and tolerability; separately measured frame/response behavior when a technical test is later authorized. Report access failures and individual context differences rather than only a grand average. [C-11, C-15]

**Reject or narrow:** block adoption of a version that strands a player without a supported route, loses necessary task information, silently resets a chosen accommodation, or cannot recover from a declared context change. If the simple presentation performs as well within a predeclared meaningful margin and uses less maintenance effort, prefer it; an underpowered null difference does not prove equivalence. A benefit on one device or one language is not universal support. Any distress or request to stop ends the relevant exposure. No results are implied by these rules. [C-15]

## Claim ledger

### C-01
**Claim:** A platform label is insufficient to specify the actual presentation context. **Class:** `inference`. **Sources/locators:** GDR-SRC-20261010-P03-009, Input/Game Features; 013, Additional considerations; original vocabulary synthesis. **Bridge:** both documents describe multiple configurations or inputs within one device family. **Confidence:** moderate for the distinction. **Limit:** not a complete device taxonomy. **Unresolved:** minimum useful context record for a particular task.

### C-02
**Claim:** Valve recommends mixed-input support and device-local graphics settings rather than cloud-synchronizing those settings. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-009, Input and Game Features. **Confidence:** high for current attribution. **Limits:** not a universal mandate about every preference and not verified runtime behavior. **Unresolved:** which preferences require a separate cross-device representation.

### C-03
**Claim:** Valve's compatibility criteria include controller access/text entry and a specifically scoped Deck display test. **Class:** `practitioner-heuristic`, with **platform-program requirements** distinguished from optional advice. **Source/locator:** GDR-SRC-20261010-P03-010, Compatibility Checklist and Steam Deck Specific Requirements. **Confidence:** high for the document's current wording. **Limits:** badge criteria, not a formal accessibility standard; exact numeric text example is in the scope table above. **Unresolved:** actual product submission applicability and additional accessibility needs; no certification performed.

### C-04
**Claim:** XAG 101 distinguishes rendered body height, platform-dependent launch defaults and player scaling. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-011, Text size/Text scaling. **Confidence:** high for attribution. **Limits:** body height includes ascender, x-height and descender space; not CSS pixels or a universal HMD angular measure. **Unresolved:** actual final rendering and usability at preferred settings. P01's reviewed numerical correction is preserved, not reverted.

### C-05
**Claim:** XAG 105 recommends independent audio categories, a stereo-to-mono option and protecting assistive speech from competing game audio. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-012, Implementation guidelines. **Confidence:** high for attribution. **Limits:** no loudness prescription or demonstrated emotional equivalence. **Unresolved:** usability of a chosen combination during the actual task.

### C-06
**Claim:** Apple's WWDC23 spatial-motion advice is historical specialist guidance, not verified current all-XR requirements. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-008, transcript sections on reading, anchoring and virtual-window motion. **Confidence:** high for that provenance boundary. **Limits:** video not watched; current HIG Motion page inaccessible. **Unresolved:** current device-specific requirements and broader populations.

### C-07
**Claim:** Android guidance distinguishes available/active inputs and recommends accommodating mixed use, including avoiding rapid hint switching. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-013, Additional considerations/How to respond to user input. **Confidence:** high for current attribution. **Limit:** no universal delay or engine-specific implementation certified. **Unresolved:** best trigger and stable fallback for the actual interaction.

### C-08
**Claim:** Android Views cutout guidance advises keeping critical and fine-touch content clear and using the actual inset/coordinate context. **Class:** `practitioner-heuristic` (documented technical guidance). **Source/locator:** GDR-SRC-20261010-P03-014, Best practices. **Confidence:** high for attribution. **Limits:** target-version-dependent behavior and native-engine integration untested. **Unresolved:** actual content-region handling and task usability on supported devices.

### C-09
**Claim:** Preserve required information and operable actions across presentation changes, not identical pixels or gestures. **Class:** `inference`. **Bridge:** C-04/C-05/C-07/C-08 identify context-sensitive routes; an adaptation succeeds only if the task remains intelligible. **Sources:** 011 Text scaling; 012 Implementation guidelines; 013 active-input guidance; inspected P01 interface/accessibility and redundant-critical-state-cues candidates. **Confidence:** moderate for decision logic. **Limit:** no universal equivalence or optimum placement. **Unresolved:** actual comprehension and attention costs.

### C-10
**Claim:** Separate player access intent, device-local realization and temporary interaction state; do not infer a diagnosis or force a mode from one device/input event. **Class:** `inference`. **Sources:** 009 graphics-settings advice; 013 mixed-input considerations. **Bridge:** technical settings can depend on hardware without making the player's preferences disposable. **Confidence:** moderate, not a validated profile architecture. **Unresolved:** how to preserve intent without overcomplicated settings or privacy intrusion.

### C-11
**Claim:** Calibrate display, viewing, response and listening choices using explicit final-context measurements and preferences. **Class:** `inference`. **Sources:** 010 scoped display test; 011 measurement distinctions; 008 historical spatial context; camera topic C-13. **Confidence:** moderate for rejecting unsupported transfer. **Limits:** no hardware benchmark, latency threshold, physical-distance optimum or safe-listening claim. **Unresolved:** local workload, meaningful margins and actual output.

### C-12
**Claim:** A recoverable context profile may preserve operation with less burden than repeated manual reconfiguration or one inflexible presentation. **Class:** `hypothesis`. **Basis:** original synthesis of C-01–C-11. **Confidence:** low; no inspected comparison validates the entire process. **Applicability:** recurring, consequential context changes. **Unresolved:** superiority to a simple flexible layout; this owns the proposed pattern's efficacy claim.

### C-13
**Claim:** Platform badge criteria, vendor recommendations and scoped formal web provisions must not be blended into a universal numerical rule. **Class:** `inference`. **Sources/locators:** 010 Compatibility Checklist; 011 Text size; inspected P01 correction receipt and selected visual/accessibility claim ledgers. **Confidence:** high for keeping authorities/units distinct, not an accessibility certification. **Limits:** underlying P01 normative provisions are shared-candidate context unless independently inspected here. **Unresolved:** product-specific applicability.

### C-14
**Claim:** Localization, privacy and production coverage constrain the usefulness of context profiles. **Class:** `inference`. **Basis:** original dependency/maintenance analysis; C-04/C-07 and P01 access/context distinctions. **Confidence:** moderate for categories of work, unknown cost/effect. **Limits:** not a complete localization or sustainability study. **Unresolved:** language coverage, profile proliferation, maintenance capacity and unmet access needs.

### C-15
**Claim:** The worked situations, failure checks and comparisons are proposed, not executed or validated. **Class:** `hypothesis`. **Basis:** original P03 synthesis under the attached brief; F01's reviewed prediction-versus-action distinction retained as a methodological caution. **Confidence:** low for diagnostic validity. **Limits:** no approved sample/margins, measurements or tests. **Unresolved:** feasibility and study-owner review.

### C-16
**Claim:** The current authorization is research and draft delivery only. **Class:** `studio-decision`. **Owner/date/source:** Doug, 2026-10-10, supplied complete P03 brief, Authorization Update/Assigned Outputs/execution exclusions. **Confidence:** high for explicit scope. **Limit:** not adoption, source installation, repository change, implementation, certification or release. **Unresolved:** evidence review and later human decisions.

## References

All source identities below are run-scoped candidates. Access was `relevant-excerpt` on 2026-10-10: actual public HTML/text or transcript passages, not merely search summaries. Repeated records support standalone reading, not corroboration.

### GDR-SRC-20261010-P03-008

Manda Paul (Apple Vision Science) and Herman Damveld (Apple research scientist). [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078/). Apple Developer. **Date:** 2023, WWDC23; exact publication day unknown. **Edition:** WWDC23 session 10078, historical transcript. **Type:** Official specialist presentation. **Locators:** Transcript: content size/contrast/depth and extended reading; motion section beginning “The first scenario”; world/head-locked views; camera motion in a virtual window; closing Reduce Motion discussion. **Limits:** Transcript inspected; video not watched. Historical advice, not current visionOS-version verification or participant results. **Relationship:** One Apple session; current HIG Motion page remained JavaScript-only. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-009

Valve. [Getting your game ready for Steam Deck and Steam Machine](https://partner.steamgames.com/doc/steamhardware/recommendations). Steamworks Documentation. **Date:** Publication/update unknown. **Edition:** Unnumbered current Steamworks web revision. **Type:** Official platform recommendations. **Locators:** Input → controller and mixed mouse/gamepad input; Game Features → graphics settings and supported resolutions/aspect ratios. **Limits:** Not a formal standard, benchmark or verified game implementation. **Relationship:** Old /steamdeck/recommendations route redirects here; same issuer/program family as 010. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-010

Valve. [Steam Deck and Steam Machine Compatibility Review](https://partner.steamgames.com/doc/steamhardware/compat?l=english). Steamworks Documentation. **Date:** Publication/update unknown. **Edition:** Unnumbered current compatibility-program revision. **Type:** Official platform-program requirements. **Locators:** Compatibility Checklist; Requirements for Steam Deck and Steam Machine → Input; Steam Deck Specific Requirements → Display, Text Legibility. **Limits:** Binding to the described badge process, not a universal accessibility or comfort standard. No certification performed. **Relationship:** Same issuer as 009; current page includes Steam Machine, unlike the older route name. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-011

Microsoft. [Xbox Accessibility Guideline 101: Text display](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101). Microsoft Learn. **Date:** Updated 2026-03-04; original publication unknown. **Edition:** Unnumbered live revision. **Type:** Official vendor guidance. **Locators:** Implementation guidelines → Text size (body height, launch defaults, console/PC/VR/mobile contexts), Text scaling; Overview. **Limits:** Body-height pixels are not CSS pixels, point size or an all-headset angular threshold; usability not certified. **Relationship:** Same URL/revision family as inspected P01-04; same issuer as 001/012. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-012

Microsoft. [Xbox Accessibility Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105). Microsoft Learn. **Date:** Updated 2026-03-04; original publication unknown. **Edition:** Unnumbered live revision. **Type:** Official vendor guidance. **Locators:** Implementation guidelines → independent audio categories, stereo-to-mono, lowering game audio during assistive speech; Potential player impact. **Limits:** No numerical loudness or hearing-safety threshold; not emotional-equivalence evidence. **Relationship:** URL matches audio pilot SRC-0007; that identity remains snapshot-scoped pending coordination. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-013

Google. [Enable natural input on all form factors](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors). Android Developers. **Date:** Updated 2026-09-24 UTC; original publication unknown. **Edition:** Current Android game-development web revision. **Type:** Official platform/technical guidance. **Locators:** Keyboard input → configuration change; Gamepad input; Additional considerations; How to respond to user input. **Limits:** General Android support advice; exact engine/device behavior untested here. **Relationship:** Same issuer as 014; neither is a participant study. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-014

Google. [Support display cutouts](https://developer.android.com/develop/ui/views/layout/display-cutout). Android Developers. **Date:** Updated 2026-09-22 UTC; original publication unknown. **Edition:** Android Views guidance; target-version-dependent behavior. **Type:** Official technical guidance. **Locators:** Best practices → critical UI, fine-touch areas, window insets and coordinate spaces; Test how your app renders content. **Limits:** Native-engine integration and target SDK behavior require separate checks; no device test performed. **Relationship:** Same issuer as 013; distinct document, not independent evidence of usability. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

## Open questions and change history

| Scope item | Inspected coverage | Unresolved work / dependency | State |
|---|---|---|---|
| Small screens/couch play | Current Valve program distinction, XAG text scopes and correction transfer. | Actual physical viewing, low-vision, localized reading and focus studies. | Bounded vendor guidance plus inference. |
| Touch/controllers/mixed input | Current Google/Valve guidance; explicit transition cases. | P02 actual drafts and review; device-specific motor/access evaluation. | Dependency missing, not accepted input guidance. |
| Display region/aspect/cutouts | Current Google Views guidance and platform framing implications. | Exact target SDK/engine route, window transitions and competitive information effects. | No implementation or device tests. |
| VR/AR | Historical Apple specialist transcript and camera-topic evidence boundaries. | Current HIG text, platform-specific tracking/occlusion/access evidence and representative populations. | Partial; no broad XR certification. |
| Listening/noise | Current XAG audio controls and shared P01 task-information distinction. | P02 multimodal evidence, full P05 audio/localization; actual listening/attention comparison. | Not a complete audio or emotional-equivalence study. |
| Hardware/performance | Program criteria separated from local measurement questions. | Measured frame/response workload, streaming, sustained-use and power/thermal evidence. | Conceptual coverage only; no benchmark. |
| Context transitions | Original profile specification, countercases and falsifying tests. | Whether added profiles outperform a simple flexible presentation. | Low-confidence process hypothesis. |

The [review packet](../reviews/full-run-20261010-p03-review-packet.md) owns exact dependency IDs, source-access limits, the batch-local conflict records and queued child work. A file covering a heading does not certify every subtopic complete.

**History — 2026-10-10:** initial P03 `initial-1`, version 0.1.0 draft. P01's selected review-correction-1 bytes and receipt were inspected; numerical scope is retained. P02 submitted work was not available as inspected evidence. No prior batch, source file, canonical index, approval or repository was changed. Independent P03 review has not occurred.

**Next decision:** review whether the context inventory and profile hypothesis are sufficiently discriminating and whether missing P02/P05 and current XR evidence require narrower claims or later child research. No platform adoption, test execution or release follows automatically.

## Independent local review — 2026-10-11

This separate review produced candidate revision review-correction-1 from the exact initial-1 predecessor recorded above. Substantive guidance retained; metadata and this note identify the reviewed local snapshot. Original author-session review and missing-input statements describe its earlier snapshot. P02 corrected drafts and review are now available to this reviewer: controls/input, feedback/game feel, multimodal communication, and the two associated patterns. This does not supply direct evidence of camera handoff or profile efficacy. Their canonical/dependency integration remains pending. F04/W03/P05 and current XR gaps are not closed by this review. IDs, version 0.1.0, draft status and null reviewer/approval fields remain unchanged. Formal Gate C acceptance, host/player tests and release are not claimed.
