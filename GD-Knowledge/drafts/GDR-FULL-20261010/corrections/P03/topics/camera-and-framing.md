---
id: GDR-CAND-20261010-P03-TOP-01
kind: topic
title: Camera and framing
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
- camera control
- camera framing
- camera-motion comfort
- view occlusion
tags:
- camera
- framing
- visibility
- motion
- comfort
- input
- xr
- cinematic-transitions
related_topics:
- GDR-CAND-20261010-P03-TOP-02
related_patterns:
- GDR-CAND-20261010-P03-PAT-01
- GDR-CAND-20261010-P03-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P03-001
- GDR-SRC-20261010-P03-002
- GDR-SRC-20261010-P03-003
- GDR-SRC-20261010-P03-004
- GDR-SRC-20261010-P03-005
- GDR-SRC-20261010-P03-006
- GDR-SRC-20261010-P03-007
- GDR-SRC-20261010-P03-008
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: 1d8190f17bea0b384df54b564c55cfb77a5220e9418de5af96b048aa71c60a83
supersedes: null
change_summary: Independent precision review; see local correction history and receipt.
hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
---

# Camera and framing

**Draft 0.1.0, candidate revision `review-correction-1`; not released guidance.** This entry owns the allocation and presentation of the view. [Platform and display context](platform-and-display-context.md) owns the conditions in which that view is seen and controlled. The principal recommendation is a conditional design inference, not an experimentally established camera policy. Research authorization does not authorize implementation or player testing. [C-10, C-14, C-17]

## Decision and scope

Choose who controls the view, what it must make available, and how it changes when visibility, staging, control effort and tolerability compete. Included: fixed and player-controlled views; 2D/3D framing; target and environmental occlusion; follow behavior; optional camera assistance; nonessential motion; cinematic transitions; and bounded VR/AR distinctions. Excluded: an engine implementation, an optical-calibration standard, a medical explanation or treatment, an exhaustive cinematography survey, and any declaration that one viewpoint suits a genre or disability. [C-01, C-13, C-17]

**Working decision rule:** begin with the least intervention that satisfies the scene's information and interaction requirements, then compare more assistance or more staging only for an explicit benefit. “Least intervention” means the least unwanted interference with the player's chosen way of operating, not invariably the fewest automatic movements. A player-selected assisted camera can demand less effort than an entirely manual one. Removing all assistance is therefore not a neutral accessibility default. [C-03, C-10, C-14]

### Working vocabulary and assumptions

These are analytic conventions for this draft, not formal definitions imposed on all games. [C-01]

| Term | Meaning used here | Important boundary |
|---|---|---|
| Camera authority | Who or what determines position, orientation, lens/framing and timing in a particular state. | Authority can differ by axis or state; optional help does not require unrestricted manual control. |
| Composition | Selection and arrangement of visible subjects and relationships for the current task or intended interpretation. | An aesthetically successful frame need not communicate a usable action. |
| Geometric visibility | An unobstructed projected representation exists. | Visibility is not sufficient size, contrast, attention, comprehension or permission to know. |
| Occlusion | A relevant representation is obscured by scene geometry or an overlay. | Camera collision, target occlusion, UI overlap and deliberate concealment are different problems. |
| Authored camera motion | View motion produced by follow, reorientation, effects, cinematics or virtual locomotion. | Physical head tracking in an HMD is not an optional decorative shake channel. |
| Field of view | A specified projection angle or displayed region. | Record horizontal/vertical convention, aspect ratio and presentation mode. A peripheral mask is not identical to changing a projection lens. |
| Recovery | An available route to restore a usable view and the chosen interaction state. | A “reset” that changes assistance preferences or reveals prohibited information is not a successful recovery. |
| Cinematic handoff | A transition of view and possibly interaction authority into, within or out of a staged sequence. | A smooth blend and a valid input/state handoff are separate achievements. |

Before choosing a camera, record the actual display/window and aspect ratio, viewing distance and posture where relevant, input and available remapping, preferred assistance, text/caption presentation, relevant access needs, task timing, and whether the experience is a flat screen, an HMD-contained window or an immersive tracked world. Record the audience and exposure history rather than borrowing the author's own monitor, headset or motor ability as a default. Children, broad access populations and every headset are not represented by this batch's empirical sources. [C-13, C-15, C-16]

## Core explanation and mechanisms

### Separate the causal links

A camera policy can successfully solve geometry and still fail the player. The following decomposition identifies where the recommendation stops being directly supported. [C-10, C-11, C-14, C-18]

| Link | Evidence available | What still needs evaluation |
|---|---|---|
| Choose manual, fixed or assisted authority to match the task and available input. | Vendor options and a firsthand assistance account are recorded in C-02/C-03. | Whether a particular player can operate the chosen policy and still make intended choices. |
| Reframe or move so the relevant subject is not obstructed. | Documented engineering mechanisms in C-04/C-05. | Whether movement is predictable, collision handling stable and permitted knowledge preserved. |
| Notice and interpret the now-visible information. | C-07/C-08 provide narrow attention/search evidence, not a camera-policy test. | Task-fact comprehension, missed peripheral information, competing UI and alternative sensory access. |
| Act with a recoverable control state. | C-10/C-12 are design synthesis, not measured effects. | Input-state continuity, orientation errors, assistance cancellation and restart behavior. |
| Obtain the intended experience without unacceptable burden. | No source validates the complete chain. | Separate agency, comfort, task performance and intended emotion; do not substitute one for another. |

### Control is a distribution of work, not a binary virtue

A useful policy specifies what happens during ordinary movement, inspection, aiming or selection, an obstruction, a story reveal, and a return from menus or cinematics. In each state, identify the authority owner and how the player can understand or change it. The strongest challenge to “always leave the camera to the player” is that it can transfer a second simultaneous control task to someone who did not choose or cannot comfortably perform it. The strongest challenge to automatic assistance is that it can fight the player, disclose a solution or redirect attention away from an intentional investigation. These are different failure modes; the response is conditional choice and recovery rather than selecting a universal winner. [C-03, C-10]

### Visibility is not an instruction to reveal everything

First specify which facts are required now, which are discoverable through an intended action, and which must remain unknown. A silhouette through a wall can rescue an already-known teammate's location while also, in a different task, destroying an intended hidden-object inference. A distant target may be technically unobstructed yet illegible. An enlarged interface may cover a route that was visible at its original size. These are illustrative design conflicts, not observed player results. [C-11]

Possible repairs include changing the scene or interaction point, providing an accessible inspection action, relocating the view, selectively changing an obstruction's rendering, or presenting a permitted state fact elsewhere. Do not assume each obstruction requires camera movement. Unity's `Transparent Layers` property is an obstruction-query distinction, not a promise that geometry is visually faded; rendering changes are a separate proposed design alternative. Engineering shot-quality scores likewise do not measure understanding, emotion or comfort. [C-05, C-11]

### Motion and attention do not collapse into one optimum

The empirical records below concern specific HMD attention and visual-search tasks. They do not establish one central fixation rule, vignette setting, field of view, or preferred amount of peripheral detail. A strategy intended to reduce visual motion can remove information used by a search task; retaining that information can introduce distraction. Treat both outcomes as possible rather than explaining away whichever conflicts with the preferred technique. [C-07, C-08, C-13]

Motion reduction should be specified by channel: nonessential bob or shake, automatic reorientation, lens changes, transition motion, object motion, and the motion necessary to represent an ongoing action. Preserve a usable alternative for the actual task; do not interpret a reduced-motion choice as permission to freeze physical tracking or secretly remove an assistance setting on which the player relies. The latter distinction is an application inference, not a verified headset implementation. [C-02, C-09, C-10, C-13]

## Design choices and alternatives

The conditions below are proposed decision aids. They are not rankings established by comparative experiments. [C-10–C-15]

| Policy | Consider when | Costs, alternatives and exit conditions |
|---|---|---|
| Fixed or authored room view | The task benefits from a stable spatial reference and all required facts can be made available. | Can conceal the next action or require costly per-room staging. Add inspectable views or revise geometry; leave the policy when required information cannot be obtained without guessing. |
| Follow camera with bounded framing region | Movement should remain readable without requiring constant view input. | Small adjustments may be unnecessary; delayed tracking can hide upcoming space. Compare a stable region, direct follow and directional lookahead; evaluate reversals rather than only forward travel. |
| Player-controlled view | Looking itself is an intended action and the active input/access route supports it. | Adds control work; automatic centering can fight inspection. Provide optional recovery/assistance or a different interaction layout rather than assuming practice will solve access barriers. |
| Player-chosen assist or requested reveal | Camera work competes with another required action, or a player explicitly asks to orient toward a known goal. | Can oversteer or disclose intent. Bound axes, trigger and knowledge; provide a compatible way to cancel, change or restore help. |
| Staged transition or cinematic | A particular relationship must be presented and the interruption is justified by the scene. | Can break orientation and held-input expectations. Compare a static reveal, player-triggered inspect action, contextual cue or omission of the interruption. |
| Contained virtual window | An immersive device presents content that does not need to occupy the whole surrounding view. | Window placement, reading and head motion require their own checks; a flat-screen camera policy is not automatically appropriate when enlarged into a surrounding world. |
| Tracked immersive or augmented view | Physical looking is part of the interaction and virtual content has a defined relation to the real environment. | Keep head pose, virtual locomotion and content anchoring distinct. Real-world visibility, tracking limitations and accessible reach/view requirements need platform-specific review. No certification follows from this topic. |

**2D versus 3D:** in a 2D task, lookahead may disclose upcoming space but change visibility differently on a narrow window or after a direction reversal. In 3D, an obstacle-avoidance move also changes apparent relationships, perspective and sometimes movement direction. In either case, decide whether movement is character-relative, camera-relative or another explicit mapping; P02 and F04 remain missing substantive dependencies. Do not infer those mappings from the camera component selected. [C-04, C-05, C-10, C-11]

**Hybrid experience conflicts:** deliberate restricted sight, cinematic staging and accessible inspection may conflict in a particular scene. State what information remains legitimately uncertain and what recovery is allowed. Do not resolve the conflict by calling one genre more authoritative. No genre-owned findings or genre files are created here. [C-11, C-15]

## Application process

1. **Diagnose the failure.** Identify whether the player lacks a required fact, cannot operate the view, loses orientation, dislikes an effect, or is being interrupted without benefit. An author wanting a more dramatic shot is a different problem from a player missing an action.
2. **Write the information and authority contract.** For each meaningful state, identify necessary facts, prohibited disclosures, who controls each view dimension, active inputs, assistance options and recovery. Record what continues to simulate during a transition.
3. **Choose the simplest viable policy and comparator.** Compare a geometry/layout repair with view movement where appropriate. Prefer a requested reveal over an involuntary one when the task permits it; retain automatic assistance when that is the player's chosen operating route.
4. **Specify motion and occlusion branches.** State the trigger, priority among competing targets, allowed path, response to reversal or obstruction, and fallback when no acceptable view exists. Source technical assumptions separately from intended player effects.
5. **Specify the handoff.** Record incoming orientation and meaningful state; disclose authority change through usable presentation; define skip/cancel behavior; return to an intelligible control state. Test a held directional input across entry and exit. Do not adopt a universal blend duration.
6. **Prototype and evaluate only under later authorization.** Use the falsifying comparisons below. When a complex solver or transition adds no relevant benefit, remove or narrow it rather than counting implementation effort as evidence.

These are proposed steps, not an implementation performed in this batch. [C-10–C-17]

### What is needed before numerical calibration

| Variable | Required measurement or preference | Unsupported shortcut to reject |
|---|---|---|
| Field of view or masking | Projection convention, aspect ratio, physical viewing context, information loss, task outcomes and individual preference. | One degree setting for flat screen, immersive VR and a virtual window. |
| Shake, bob and effects | Which channel moves, direction/amplitude/time profile, legibility during the effect, selectable off/reduced route and tolerability. | A universal intensity percentage or an assurance that a small slider value is comfortable. |
| Follow and recenter | Input mapping, reversal behavior, obstruction traces, correction effort and reacquisition outcomes. | A fixed damping value transferred between engines, units or movement speeds. |
| Cinematic transition | View displacement, scene motion, authority transfer, skip behavior and orientation/action outcomes. | Every cut is bad, every smooth blend is good, or one duration is safe. |
| Framerate and response | Actual display/render path, frame-time behavior and end-to-end response in the intended workload. | A nominal average framerate proves comfort or that a camera feels responsive. |

The calibration plan is an inference from the different tasks, devices and documented mechanisms, not a new technical standard. [C-13]

## Patterns and genre adaptations

[Recoverable camera assistance — GDR-CAND-20261010-P03-PAT-01](../patterns/recoverable-camera-assistance.md) owns the proposed authority/intervention/recovery recipe. [Task-preserving context profiles — GDR-CAND-20261010-P03-PAT-02](../patterns/task-preserving-context-profiles.md) owns device/context changes that affect the view. Neither is independent evidence for this topic. [C-14]

The inspected first-wave P01 candidates retain corrected numerical scope and the distinction between an available representation and an accessible information route. Their files are external dependencies, not copied into this packet. Relevant P01 IDs and hashes are in the [review packet](../reviews/full-run-20261010-p03-review-packet.md#dependency-and-correction-transfer). Genre adaptation remains illustrative: inspection, precise timing, dramatic restriction and restful observation can require different choices even inside the same genre label. No genre rule is asserted. [C-11, C-15]

## Examples and counterexamples

### Illustrative worked case: a covered inspection point

A player guides an avatar to a machine beneath an overhang. They need to read its state, choose between two marked controls and retain awareness of a known exit. The cause of a distant disturbance is deliberately unknown. This is invented to make the decision concrete, not a shipped-game observation. [C-11, C-14, C-16]

A candidate specification first tries a stable interaction framing region and a permitted textual state display. If the avatar or controls remain blocked, offer an inspect action or the player's chosen assist; moving the camera is a later branch, not the only repair. A requested reorientation targets the known machine, never the hidden disturbance. The player can leave inspection using the current input route; a return pose must still expose the known exit or an equivalent navigational reference. A reduced-motion preference disables decorative shake without removing the requested assistance. [C-10–C-14]

Compare this with an always-on orbit solver and with a simple relocation of the interaction point. If the relocation communicates the required state with less effort and no staging loss that matters to the design, extra camera logic has no demonstrated justification. If the assist unexpectedly reveals the disturbance, the information contract fails even if navigation becomes faster. If fully manual inspection is inaccessible to a participant, that is a policy failure, not evidence of low player skill. These are proposed decision outcomes. [C-11, C-14, C-16]

### Documented production countercase

Gallant's account explicitly describes optional automatic camera reorientation for difficulties with simultaneous sticks. That is a counterexample to treating automation itself as inherently anti-accessibility, but it does not establish the effectiveness of the complete recipe proposed here. The underlying game was not played or watched in this batch. [C-03]

### Illustrative negative case: reveal would solve the task

A scene asks the player to infer which visible structure contains a signal source. An unsolicited camera turn toward the correct structure can supply the answer instead of helping the player examine the evidence. Prefer view assistance that supports inspection without selecting the answer, or explicitly define the assistance as a chosen solution hint. Removing mystery and increasing accessibility are not necessarily the same intervention. [C-10, C-11]

## Failure modes and constraints

| Warning sign in a future evaluation | Competing explanation to investigate | Proposed response |
|---|---|---|
| Repeated corrective input against automatic movement | Authority policy conflicts with inspection or input noise triggers recentering. | Offer requested/axis-limited help, revise trigger, or remove the intervention. |
| Target becomes visible but necessary action is still missed | Scale, contrast, cue competition, reading or semantic problem rather than obstruction. | Revisit presentation and information routes; do not keep moving the camera. |
| Rapid switches between acceptable positions | Competing targets or boundary instability. | Reduce priorities, test stable fallback and revise scene; do not assume more smoothing resolves the cause. |
| Correct orientation but unintended movement after a cut | Held-input mapping or control-state handoff. | Define return mapping and recovery; coordinate with movement/input owners. |
| Better search time but worse tolerability or unacceptable distraction | Different outcomes optimized by the same camera change. | Preserve separate findings and the user's choice; do not hide losses inside a single score. |
| An alternative view discloses hidden facts | Accessibility repair changed the intended knowledge state. | Reauthor the task or make the disclosure an explicit assistance choice. |
| Preferred assistance disappears after loading or a device change | Preference and runtime-state lifecycle confused. | Restore intended preference and evaluate the new device-specific realization. |

These warning signs and repairs are hypotheses for evaluation, not events observed here. [C-11, C-12, C-14, C-16]

**Accessibility and localization:** account for limited simultaneous input, reduced-motion preference, magnified/captioned layouts, reading direction and language expansion. A caption at a fixed screen edge and a critical target can compete even when neither overlaps. Do not mirror world directions simply because the interface reading direction changes; confirm the semantic relation being communicated. Avoid requiring sustained head movement merely to read ordinary settings. These are design inferences, not claims that one placement works for all people. [C-09, C-11, C-15]

**Ethics and production:** preserve a usable refusal/exit from optional intensity or assistance experiments. Never infer a diagnosis from camera corrections or silently increase motion because someone completed a task. Camera modes multiply authored states, transition paths, collision cases, language/layout tests and maintenance work; the magnitude is unmeasured. Where resources cannot support a complex policy, reduce modes or redesign the task rather than claim untested parity. Multiplayer/shared views may distribute control unfairly; this batch did not inspect a comparative shared-camera study. [C-15, C-16]

## Playtest and validation

**PROPOSED — NOT RUN.** No prototype, game/engine code, participants, instrument readings or statistical reanalysis occurred. This protocol outline needs separate study approval, accessible recruitment and an analysis plan. No participant count or numerical pass threshold is invented. [C-16, C-17]

**Question:** does a recoverable, player-chosen camera policy improve the specified task/control problem over the least complex feasible alternative without unacceptable information, orientation or comfort failures?

**Conditions:** use matched scenes with (A) the viable baseline, (B) the proposed assistance and recovery policy, and, only when relevant, (C) a simpler scene/layout repair. The baseline must be operable by the intended participants; an inaccessible manual policy is not a fair “control.” Hold required facts, available actions and consequences constant. If a mode necessarily changes knowledge or task difficulty, record that as a strategy comparison rather than a pure camera effect. Counterbalance scene/order and examine both first use and later revisits. [C-16]

**Contexts and participants:** sample the actual intended input/viewing contexts, including people who use the relevant assistance, magnification or motion preferences. Plan sample size from the question, resources and defensible local variability/precision needs, not an arbitrary universal minimum. Do not ask participants to disable accommodations to simulate another group. HMD work needs a separately scoped protocol and cannot be validated by flat-screen sessions. [C-16]

**Measures kept separate:** required-fact comprehension, wrong-action reasons, time or attempts to obtain the intended view, corrective camera actions, orientation after transitions, information leaks, assistance/cancel use, perceived control, tolerability and the specifically intended experience. Log active settings, frame-time conditions and any interrupted trials. Completion is neither mastery nor approval of the camera; a choice to decline an action can coexist with correct understanding. This preserves the inspected F01 correction's discrimination principle without treating its proposed probes as validated tests. [C-16, C-18]

**Disconfirming outcomes:** reject or revise the candidate when the assist cannot be reliably declined/changed, required facts become inaccessible, an unpermitted answer is revealed, or return-to-control produces consequential unintended actions. Narrow a benefit confined to one input or exposure context. If added complexity brings no locally meaningful benefit over the simple alternative, prefer simplification; a small inconclusive comparison is not proof of equivalence. The later study owner must specify meaningful margins and analysis before data collection. Any request to stop ends exposure; adverse or abandoned trials remain part of the record rather than disappearing as inconvenient outliers. [C-16]

## Claim ledger

Claim classes describe evidence type, not approval. Confidence concerns the exact bounded claim. `C-10` onward is original synthesis, not a result that the cited documents measured.

### C-01
**Claim:** The distinctions in the working vocabulary prevent different camera problems from being treated as one variable. **Class:** `inference`. **Confidence:** moderate for analytic usefulness, unvalidated as a taxonomy. **Basis/locators:** original synthesis of the assigned P03 scope; component distinctions in GDR-SRC-20261010-P03-003/004, introductions. **Limit:** not standardized terminology. **Unresolved:** whether the decomposition supports reliable diagnosis in real design reviews.

### C-02
**Claim:** XAG 117 recommends configurable nonessential visual motion and camera-related options. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-001, Implementation guidelines. **Confidence:** high for attribution, not a comfort effect. **Applicability:** official accessibility guidance adapted to the actual task. **Limit:** not all background motion is forbidden whenever text appears. **Unresolved:** the effective and usable configuration for a particular player.

### C-03
**Claim:** Naughty Dog reports an optional reorientation assist intended for players who find simultaneous stick use difficult. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-002, Alternate Controls → Assistance → Camera Assist. **Confidence:** high for the published account; player effect unmeasured here. **Limit:** historical, single production, exact build unobserved. **Unresolved:** comparative effort, agency and tolerability in the proposed context.

### C-04
**Claim:** Position Composer documents positional framing, lookahead and damping; its lookahead warning distinguishes jitter amplification from smoothing-related lag. **Class:** `practitioner-heuristic` (documented technical behavior). **Source/locator:** GDR-SRC-20261010-P03-004, introduction and Properties. **Confidence:** high for version-specific documentation, not runtime verification. **Limit:** no useful universal parameter values. **Unresolved:** actual task/animation interaction.

### C-05
**Claim:** Deoccluder documents target-sightline strategies and obstruction-query controls, not a player-comprehension guarantee. **Class:** `practitioner-heuristic` (documented technical behavior). **Source/locator:** GDR-SRC-20261010-P03-003, introduction and Properties. **Confidence:** high for attribution. **Limits:** collider/raycast dependencies, unmeasured cost; Transparent Layers is not a rendering-fade feature. **Unresolved:** whether moving the camera is preferable to another repair.

### C-06
**Claim:** WCAG 2.2 SC 2.3.3, Level AAA, requires that interaction-triggered motion animation can be disabled unless essential to functionality or the information conveyed. **Class:** `formal-standard`. **Issuer/edition/locator:** W3C Recommendation, 2024-12-12, GDR-SRC-20261010-P03-005, SC 2.3.3. **Confidence:** high for that scoped requirement. **Limits:** web conformance scope; not a blanket native-game or HMD certification claim. **Unresolved:** actual product applicability and any essential-motion exception.

### C-07
**Claim:** Attention manipulation had different results across Yip and Saunders' two HMD experiments. **Class:** `empirical-evidence`. **Source/locators:** GDR-SRC-20261010-P03-006, both experiments' methods/results. **Study:** experiment 1 used 16 people aged 21–24, active seated navigation and outlined attention regions; no significant condition difference was reported, and only seven completed the full exposure. Experiment 2 used 40 people aged 18–23, passive rollercoaster viewing and a dot-probe task; central attention yielded lower reported discomfort (MISC paired effect dz=.693; p<.001). Thirty-one completed all blocks. **Confidence:** moderate for these reported comparisons. **Limits:** young convenience samples with normal/corrected vision and stated health exclusions; different motion, tasks and cues; a central reference appeared only in the central condition of experiment 2. Experiment 1 stopped at the first sequential interim. Null results do not establish equivalence. **Unresolved:** mechanism and transfer to ordinary camera control. No data reanalysis or direct replication inspected.

### C-08
**Claim:** Selected granulated-rest-frame configurations outperformed a field-of-view restrictor on visual search, without establishing sickness mitigation. **Class:** `empirical-evidence`. **Source/locators:** GDR-SRC-20261010-P03-007, Methods, Results, Discussion. **Study:** 20 participants from one institution, seated Oculus Rift CV1/gamepad; within-participant comparison of nine granulated configurations and a restricted-view condition on target counting in a static scene. Text reports faster search for selected configurations; five participants preferred the restrictor because granulation distracted them. **Confidence:** moderate, narrowly scoped. **Limits:** not all variants superior; sickness mitigation explicitly remained future work; some equations/statistics were not legibly extracted from HTML, so no effect-size reconstruction is offered. **Unresolved:** comfort, sustained play and task transfer. No raw-data or figure analysis performed.

### C-09
**Claim:** Apple's WWDC23 transcript recommends stable spatial presentation and conditional alternatives to head-locked content and abrupt virtual-camera motion. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-008, motion and virtual-window transcript sections. **Confidence:** high for historical attribution, not guaranteed outcomes. **Limit:** current HIG text was inaccessible; transcript is not a current versioned platform standard. **Unresolved:** appropriate anchoring and motion for a specific headset/access route.

### C-10
**Claim:** Explicit authority, optional assistance and an operable recovery route are preferable hypotheses to either compulsory manual control or compulsory automation. **Class:** `inference`. **Bridge:** C-02 permits customization; C-03 supplies a reason automation can be useful; neither resolves unwanted interference. **Sources:** 001 Implementation guidelines; 002 Camera Assist. **Confidence:** moderate as conditional decision logic. **Limit:** not an established effect size or proof every view must be free. **Unresolved:** local policy benefit.

### C-11
**Claim:** Repair visibility while preserving the required and permitted information, not geometric visibility alone. **Class:** `inference`. **Bridge:** a geometry repair does not establish readable or legitimate information. **Sources:** 003 introduction/Properties; inspected P01 visual/interface and redundant-critical-state-cues candidates, selected revision `review-correction-1`, relevant mechanisms and claim ledgers. **Confidence:** moderate for the distinction. **Limit:** no direct information-leak experiment. **Unresolved:** which facts are legitimately hidden and accessible in each scene.

### C-12
**Claim:** Treat cinematic entry, cancellation and return as an authority-and-input handoff, not just a blend. **Class:** `hypothesis`. **Basis:** original synthesis of the current brief's transition scope and C-10/C-11. **Confidence:** low for comparative benefit; no inspected handoff experiment. **Applicability:** staged views or mode changes with meaningful interaction. **Unresolved:** best return mapping and required explanation; P02/F04 evidence unavailable.

### C-13
**Claim:** Calibrate projection, motion and response using explicit device/task units and user preference rather than a universal numerical setting. **Class:** `inference`. **Bridge:** C-04/C-05 expose distinct engineering parameters; C-07/C-08 concern different tasks; C-09 is device-context advice. **Confidence:** moderate for the limit on transfer, not optimal values. **Limit:** no latency/display benchmark supplied. **Unresolved:** local measurement plan and acceptable tradeoffs.

### C-14
**Claim:** The complete authority → intervention → recovery policy may improve operation without unacceptable losses relative to a simpler alternative. **Class:** `hypothesis`. **Basis:** C-02–C-05 motivate components, not the whole chain. **Confidence:** low; no direct comparison inspected. **Applicability:** an explicit task/control problem with a usable recovery route. **Unresolved:** benefit, burden and alternatives; this is the owning claim for the pattern recipe.

### C-15
**Claim:** Access, localization, privacy and state/transition maintenance are part of camera-policy selection. **Class:** `inference`. **Bridge:** an intervention and its alternatives require usable presentation and authoring across affected states; these obligations do not follow from a shot score. **Sources:** C-02/C-09 and inspected P01 candidate constraints. **Confidence:** moderate for identified work categories; magnitudes unknown. **Unresolved:** supported contexts, maintenance cost and shared-camera needs.

### C-16
**Claim:** Worked cases, failure branches and validation procedures are proposed specifications, not performed tests. **Class:** `hypothesis`. **Basis:** original P03 synthesis; F01 correction diff's distinction between understanding and chosen action is retained as review context. **Confidence:** low for future diagnostic validity. **Limits:** no sample, instrument, margin or protocol approved. **Unresolved:** study-owner review, feasibility and representative evaluation.

### C-17
**Claim:** Doug authorized bounded P03 research and draft delivery, excluding implementation, tests and release. **Class:** `studio-decision`. **Owner/date/source:** Doug, 2026-10-10; supplied complete brief, Authorization Update, Assigned Outputs and execution limits. **Confidence:** high for this explicit scope. **Limit:** no evidence approval or canonical allocation. **Unresolved:** later evidence and human review.

### C-18
**Claim:** Intended staging, comprehension, task performance, tolerability and agency must remain distinct outcomes in this evaluation. **Class:** `inference`. **Bridge:** C-07/C-08 measure different tasks/outcomes; the proposed camera policy can trade them off. **Confidence:** moderate as measurement discipline. **Limit:** no validated combined index is offered. **Unresolved:** locally appropriate measures and meaningful differences.

## References

All source identities below are run-scoped candidates. Access was `relevant-excerpt` on 2026-10-10: actual public HTML/text or transcript passages, not merely search summaries. Repeated records support standalone reading, not corroboration.

### GDR-SRC-20261010-P03-001

Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). Microsoft Learn. **Date:** Updated 2026-03-04; original publication unknown. **Edition:** Unnumbered live revision. **Type:** Official vendor guidance. **Locators:** Goal; Overview; Implementation guidelines → camera movement, field of view, sensitivity, automatic movement, nonessential effects, background motion while reading. **Limits:** Recommendations, not a formal standard, medical guarantee or efficacy comparison. **Relationship:** Same issuer as 011/012; URL matches P01-10, central reconciliation pending. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-002

Matthew Gallant, Lead Systems Designer, Naughty Dog. [The Last of Us Part II: Accessibility features detailed](https://blog.playstation.com/2020/06/09/the-last-of-us-part-ii-accessibility-features-detailed/). PlayStation Blog. **Date:** 2020-06-09; page also displays 2020-06-10. **Edition:** Historical launch-era account; exact game build not inspected. **Type:** Firsthand creator account. **Locators:** Accessibility Presets; Alternate Controls → Assistance → Camera Assist; Navigation and Traversal → Navigation Assistance; Motion Sickness. **Limits:** Reported features and intent; no played build, controlled outcomes or measured comfort benefit. **Relationship:** One production account, independent of Microsoft documentation; not a replication. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-003

Unity Technologies. [Cinemachine Deoccluder](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineDeoccluder.html). Unity package documentation. **Date:** Publication/update unknown; generated 2026-06-09. **Edition:** Served package metadata 3.1.7 under the 3.1 route. **Type:** Official technical documentation. **Locators:** Introduction; Properties → Transparent Layers, Avoid Obstacles, Strategy, Minimum Occlusion Time, Smoothing Time, Damping; HTML package metadata. **Limits:** Describes a component, not tested runtime behavior here or measured readability/comfort. **Relationship:** Same package/issuer as 004; one engineering documentation family. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-004

Unity Technologies. [Position Composer](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachinePositionComposer.html). Unity package documentation. **Date:** Publication/update unknown; generated 2026-06-09. **Edition:** Served package metadata 3.1.7 under the 3.1 route. **Type:** Official technical documentation. **Locators:** Introduction; Properties → Lookahead, Damping, Screen Position, Dead Zone; HTML package metadata. **Limits:** No runtime test or player-outcome comparison. Parameter names are not optimal settings. **Relationship:** Same package/issuer as 003; not independent corroboration. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-005

World Wide Web Consortium (W3C). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). W3C. **Date:** W3C Recommendation 2024-12-12. **Edition:** WCAG 2.2; dated edition identified in retrieved header. **Type:** Normative web accessibility Recommendation. **Locators:** Success Criterion 2.3.3 Animation from Interactions, Level AAA; document status and conformance framing. **Limits:** Scope is web content and relevant conformance level; not a native-game certification or universal motion setting. **Relationship:** Same edition/URL family as P01-01; central deduplication pending. **Rights:** W3C document rights apply; no figures or substantial verbatim text reproduced. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-006

Sai Ho Yip and Jeffrey Allen Saunders. [Restricting the distribution of visual attention reduces cybersickness](https://link.springer.com/article/10.1186/s41235-023-00466-1). Springer Nature. **Date:** 2023-03-16. **Edition:** Cognitive Research: Principles and Implications 8, article 18; DOI 10.1186/s41235-023-00466-1. **Type:** Original empirical study. **Locators:** Experiment 1 → Method, Results, Discussion; Experiment 2 → Participants, Design and procedure, Results; General discussion. **Limits:** Two different tasks/manipulations; young convenience samples, early stopping/attrition; no game-camera setting validated. **Relationship:** PMC mirror blocked; publisher HTML inspected. Same paper, not two sources; distinct authors/cohort from 007. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-007

Zekun Cao, Jeronimo Grandi and Regis Kopper. [Granulated Rest Frames Outperform Field of View Restrictors on Visual Search Performance](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2021.604889/full). Frontiers. **Date:** 2021-05-31. **Edition:** Frontiers in Virtual Reality 2:604889; DOI 10.3389/frvir.2021.604889. **Type:** Original empirical study. **Locators:** Methods → Participants, Apparatus, Procedure; Results; Discussion → user preference and limitations/future VIMS evaluation. **Limits:** Visual-search findings; sickness mitigation not established. Some HTML mathematics was not legibly extracted; no reconstructed effect sizes. **Relationship:** Distinct cohort from 006; cites Fernandes/Feiner but does not substitute for inspecting that paper. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

### GDR-SRC-20261010-P03-008

Manda Paul (Apple Vision Science) and Herman Damveld (Apple research scientist). [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078/). Apple Developer. **Date:** 2023, WWDC23; exact publication day unknown. **Edition:** WWDC23 session 10078, historical transcript. **Type:** Official specialist presentation. **Locators:** Transcript: content size/contrast/depth and extended reading; motion section beginning “The first scenario”; world/head-locked views; camera motion in a virtual window; closing Reduce Motion discussion. **Limits:** Transcript inspected; video not watched. Historical advice, not current visionOS-version verification or participant results. **Relationship:** One Apple session; current HIG Motion page remained JavaScript-only. **Rights:** License not separately audited; attributed paraphrase only. No source media or code redistributed. Claim bindings are in this entry's ledger.

## Open questions and change history

| Scope item | Researched coverage | Remaining question and dependency | Review state |
|---|---|---|---|
| Control/assistance | Official options and firsthand rationale; conditional authority model. | Who benefits from which policy? P02 controls/input and F04 movement bytes missing. | Author draft; independent P03 review pending. |
| Composition/2D and 3D | Framing mechanisms, scene/task alternatives and worked countercases. | Comparative composition/affective evidence and task-specific lookahead; W03 spatial design missing. | Bounded, not complete cinematography coverage. |
| Visibility/occlusion | Current engine documentation and permitted-information distinction. | Dynamic obstruction tests, multi-target cases, rendering alternatives and content leaks. | Engineering description only; no runtime or player validation. |
| Motion/comfort | Current XAG, scoped web requirement, two original HMD studies, historical Apple transcript. | Broader populations, direct flat-screen camera trials and actual current headset guidance. | Conditional evidence; no medical/compliance conclusion. |
| Cinematic transitions | Explicit hypothetical handoff recipe and negative case. | Comparative cut/blend/skip/return evidence; input and spatial dependencies. | Evidence gap remains; not a validated pattern. |
| VR/AR | Distinguishes physical looking, content anchoring, contained windows and authored motion. | Current AR occlusion/tracking/access evidence and representative testing. | Historical guidance plus inference; incomplete. |

Conflicts `P03-CON-01` through `P03-CON-04` are batch-local records in the [review packet](../reviews/full-run-20261010-p03-review-packet.md#contradictions-and-boundary-conflicts), not global register allocations. Additional occlusion, lookahead and peripheral-filter work is queued there without assigning child keys.

**History — 2026-10-10:** initial P03 candidate, `initial-1`, 0.1.0 draft. No earlier P03 submission found among the available bytes; predecessor and supersedes remain null. Selected P01 corrections were actually inspected, not inferred from memory. Earlier batches and source files remain unchanged and are not redelivered. Author self-review is recorded in the packet; independent review and acceptance remain outstanding.

**Next decision:** Library Coordination should review the qualified camera policy and its evidence gaps, especially the handoff hypothesis and competing access needs, before any adoption or separately authorized validation. No numerical default is approved by this artifact.

## Independent local review — 2026-10-11

This separate review produced candidate revision review-correction-1 from the exact initial-1 predecessor recorded above. Clarified WCAG 2.3.3 disable capability rather than mandatory off state; pinned dated normative URL. Made the static-scene boundary of the GRF search study explicit; no new effect size or comfort claim. Original author-session review and missing-input statements describe its earlier snapshot. P02 corrected drafts and review are now available to this reviewer: controls/input, feedback/game feel, multimodal communication, and the two associated patterns. This does not supply direct evidence of camera handoff or profile efficacy. Their canonical/dependency integration remains pending. F04/W03/P05 and current XR gaps are not closed by this review. IDs, version 0.1.0, draft status and null reviewer/approval fields remain unchanged. Formal Gate C acceptance, host/player tests and release are not claimed.
