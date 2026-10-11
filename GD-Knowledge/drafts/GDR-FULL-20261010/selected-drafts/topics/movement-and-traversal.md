---
id: GDR-CAND-20261010-F04-TOP-02
kind: topic
title: Movement and traversal
version: 0.1.0
status: draft
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_id: F04
candidate_revision: initial-1
attempt_id: F04-attempt-1
updated: '2026-10-10'
date_basis: America/Los_Angeles; public access crossed 2026-10-11 UTC
evidence_checked: '2026-10-11'
aliases:
- locomotion
- jumping
- momentum
- traversal abilities
- vehicle control
- movement precision
tags:
- navigation-abilities
- movement-costs
- assistance
- precision
- contact
- coverage-open
related_topics:
- GDR-CAND-20261010-F04-TOP-01
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
related_patterns:
- GDR-CAND-20261010-F04-PAT-02
- GDR-CAND-20261010-F04-PAT-01
- GDR-CAND-20261010-G02-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F04-004
- GDR-SRC-20261010-F04-005
- GDR-SRC-20261010-F04-006
- GDR-SRC-20261010-F04-007
- GDR-SRC-20261010-F04-008
- GDR-SRC-20261010-F04-011
- GDR-SRC-20261010-F04-012
- GDR-SRC-20261010-F04-013
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-F04
coverage_status: coverage-open
predecessor_sha256: null
supersedes: null
integrity_receipt: ../reviews/full-run-20261010-f04-integrity-receipt.md
---

# Movement and traversal

**Draft research candidate — not released guidance.** Version 0.1.0; initial candidate revision. Author synthesis and author self-review only: no independent F04 review, game implementation, prototype, gameplay observation, participant recruitment or playtest occurred. Examples explicitly marked illustrative are inventions for analysis.

## Decision and scope

This entry helps a designer choose how movement expresses intention, how capabilities open usable routes, and what precision, commitment and traversal cost demand from the player. **Locomotion** refers here to rules changing motion; **traversal** refers to using those rules and capabilities to reach a goal. Finding a path, executing it and recovering from failure are different tasks. [C-01]

Coverage includes grounded and airborne motion, jumping/climbing, momentum, moving supports, navigation abilities, ground vehicles, assisted traversal, precision and costs. Flight, swimming, six-degree-of-freedom control, VR locomotion, touch and alternative-input specifics are **coverage gaps**, not validated extensions of the ground-vehicle or jumping evidence. They appear only as questions and conditional models where explicitly labeled. [C-01, C-07]

Foundations owns movement rules and their decision costs. Worlds owns route/spatial composition. Presentation owns input realization, camera, animation and sensory communication. The active F03, W03 and P03 outputs have not been retrieved and reviewed here; they cannot be treated as shared established guidance. No Unity/Unreal controller, vehicle simulation or harness change is authorized.

## Core explanation and mechanisms

### Diagnose the failed relationship, not the feeling label alone

“Sluggish,” “slippery” or “imprecise” can refer to different problems: the command arrived late; it was received outside eligibility; the actor accelerated slowly; the direction could not reverse; the camera concealed contact; or a recovery state consumed the next command. First separate command delivery, recognition, validity, motion and feedback. The reviewed P02 correction is retained: buffering cannot reduce hardware delivery latency. [C-02]

Define the decision-relevant movement state. Candidate fields include position, velocity, grounded/support relationship, facing, current action, remaining capability charges, surface condition and allowed interruptions. A simple movement system may need only a few; an elaborate state list is not a requirement. Separate what the actor can physically do from what the player knows and what the camera makes visible. [C-01, C-02, C-07]

### Precision is not one parameter

Fasterholdt and colleagues measured and modeled jumping characteristics across selected games. Their framework is a way of describing motion, not an experimental proof that particular values feel good. Some data provenance is derivative, and the paper’s scope exclusions remain important. [C-03; GDR-SRC-20261010-F04-007]

Distinguish the precision of **starting an action**, selecting a direction, controlling a trajectory, achieving a landing region and stopping within a destination. A movement change can help one while harming another. Faster acceleration can reduce time to reach a ledge but make slow placement harder; stronger air control can enable recovery while reducing the consequence of a takeoff decision. These are proposed design relationships to examine, not universal preference results. [C-04, C-18]

A practical decomposition is launch behavior, held/released-input behavior, acceleration and reversal, braking, air control, contact handling and inherited velocity. Normalizing a measured jump to character height helps a particular comparison; it does not make that number a universal world scale or a target for the receiving game. Do not transplant source pixels, nominal frames, jump heights or reaction windows. [C-03, C-04]

### Momentum and contact are part of the decision

Treat momentum as a commitment to future movement under the actual rules, not merely a visual impression of weight. Ask what happens when input is released, reversed or changed during contact; whether a moving support’s motion is inherited; and what remains after an interruption or landing. A vehicle, airborne actor and climbing actor can expose different choices even at the same speed. [C-04, C-06, C-18]

Thorson’s physics article describes distinct carry, push and squish relationships for moving solids. That account motivates checking contact semantics; F04 does not adopt its integer-coordinate or collision implementation. A promise such as “standing on this lift carries the actor” needs a corresponding answer for wall contact, ceiling contact, loss of support and return from a reset. [C-06; GDR-SRC-20261010-F04-006]

### Four different meanings of “forgiving”

Keep **eligibility grace** separate from **trajectory correction**, **contact tolerance** and **recovery cost**. An early input can be accepted later without changing a jump arc. A wider landing surface changes spatial tolerance without accepting earlier input. A short retry changes the consequence of failure without changing either. Automatic execution can remove an input sequence while leaving route choice intact. [C-05, C-08]

The creator’s Celeste forgiveness account is a narrow production source, not an efficacy study. The reviewed **Bounded action grace** pattern already owns early/recent-state eligibility. F04 reuses that dependency and does not produce another coyote-time or input-buffer pattern. [C-05; GDR-SRC-20261010-F04-005]

Naughty Dog’s documentation distinguishes navigation assistance, simplified traversal and ledge protection. These documentary options motivate asking which part of the task should change; they do not establish that every assist preserves the same skill or suits every player. [C-08; GDR-SRC-20261010-F04-004]

### Abilities create state-conditioned routes

A climb, jump, grapple or mount is not a usable route merely because an entrance is reachable. Record prerequisites, the state on arrival, an exit or continuation, and the resources needed after commitment. The designer may intentionally create a one-way route, but that is different from unintentionally trapping a player who used a legitimately available ability. [C-07]

For climbing, ask whether entry requires a direction, attachment point, stamina reserve or maintained input, and what happens on release or interruption. For a jump, ask what motion can still be changed after takeoff. For a vehicle, ask what mounting, dismounting, damage, refueling or recovery changes. These are conditional questions, not verified claims about all such mechanics. Authored path arrangement remains with Worlds; unlock and resource schedules remain with Foundations’ other topics. [C-07, C-13, C-19]

### Vehicle assistance and the limits of telemetry

The Forza Motorsport 4 study reports 220,000 sampled players and 24.5 million race entries, including abandoned entries. The historical data are observational. Its transition labels operationalize continued assist non-use; they do not directly measure why a person changes settings, independent mastery or wellbeing. Input device and camera view were absent from the reported telemetry. [C-09, C-10; GDR-SRC-20261010-F04-008]

Do not turn an observed setting trajectory into an instruction to withdraw assistance. Treat successful control, chosen challenge, access requirements, assist preference and eventual non-use as different outcomes. In particular, an informational preview, steering automation and changing the physical rules are different interventions even when packaged in one preset. [C-10, C-11, C-17]

For a ground-vehicle task, diagnose steering response, braking/acceleration, shifting demand, contact, course knowledge and recovery separately. The inspected paper does not establish controller/wheel parity, a preferred braking model, or a flight/swimming/VR policy. Those generalizations remain outside the evidence coverage. [C-04, C-09, C-19]

### Traversal costs and the value of repetition

Represent costs through the dimensions relevant to the goal: elapsed time, simultaneous/continuous control effort, expendable capability, exposure, foregone opportunities and the state after failure. Do not collapse those into distance or a single numerical difficulty rating without a reason. An inexpensive route in currency can still demand sustained precision or repeat substantial travel. [C-13]

A recovery option can return the actor to a viable state without erasing all costs. Alternatively, retaining depleted resources after each failure can be an intentional commitment rule. Test whether that rule remains comprehensible and whether an attainable exit exists. “Forgiving” and “meaningful” are not mutually exclusive, but their desirable balance is a local hypothesis. [C-08, C-13, C-18]

## Design choices and alternatives

| Decision | When it may serve the goal | Tradeoff / failure case | Alternative to compare |
|---|---|---|---|
| Direct low-inertia movement | Immediate placement and frequent redirection matter | Can weaken trajectory planning or perceived commitment | Retain inertia only in particular states. [C-04, C-18] |
| Committed acceleration/braking | Anticipation and momentum management are expressive | Missing state information can look like ignored input | Better feedback or local practice before changing physics. [C-02, C-04] |
| Greater mid-action correction | Recovery decisions are part of the intended skill | Can bypass takeoff/route planning | Adjustable correction or clearer pre-commit information. [C-08, C-18] |
| Bounded input grace | Near-boundary requests should count under declared intent rules | Stale commands can execute after context changes | Correct misleading feedback or input mapping instead. [C-02, C-05] |
| Authored assisted traversal | Route choice matters more than a repeated execution sequence | Automation can choose an unwanted destination or conceal exceptions | A simpler interaction, skip option or separate navigation aid. [C-07, C-08] |
| State-conditioned preview | Motion prediction is a specific barrier and the model can remain truthful | Staleness, visual load and lost discovery | Static landmarks, range cues or a voluntary practice space. [C-11, C-12] |
| Costly recovery | Persistent commitment is a declared experience goal | Repeated failure can make the route progressively less viable | Restore a viable baseline, offer withdrawal, or reduce repetition. [C-13, C-18] |

## Application process

1. **State what movement should let the player express.** Separate finding a route, choosing commitment, executing precision and accepting cost. Describe the intended failure and recovery, not only the successful path. [C-01, C-13]
2. **Specify the important states and transitions.** Include starting, stopping, turning, support changes, capability depletion and return after failure. Record the known input/camera/device context. [C-02, C-04, C-06]
3. **Localize the barrier.** Is the information wrong, the input ineligible, the arc difficult, the destination narrow or the retry costly? Avoid changing all five together and attributing the outcome to one intervention. [C-02, C-08]
4. **Choose a minimal alternative.** Compare committed motion, greater correction, bounded grace, assistance, different information or less repetition according to the intended task. Keep required accommodations available. [C-05, C-08, C-17, C-18]
5. **Audit route viability and costs.** Test conceptual arrival/continuation/withdrawal states, including the lowest allowed resource state and changed assistance. This is a specification for later authorized testing, not an engine test performed here. [C-07, C-19]
6. **Evaluate prediction, execution and preference separately.** Use the proposed protocols below. Record when a changed movement rule is a new task rather than improved execution of the original one. [C-17, C-18]
7. **Reconcile with the other owners.** Movement, animation, camera, route geometry and resource pacing can jointly change the task. No unseen W03/P03/F03 approval is implied. [C-07, C-13, C-16]

## Patterns and genre adaptations

[State-conditioned traversal preview](../patterns/state-conditioned-traversal-preview.md), `GDR-CAND-20261010-F04-PAT-02`, is a hypothesis about advisory prediction information. It is not automatic movement, proof of route safety or an assist-removal ladder. [C-11, C-12]

[Combat and conflict systems](combat-and-conflict-systems.md), `GDR-CAND-20261010-F04-TOP-01`, owns movement’s interaction with threats. [Response-feasible threat composition](../patterns/response-feasible-threat-composition.md), `GDR-CAND-20261010-F04-PAT-01`, applies only when a declared conflict goal constrains movement sequences. Existing reviewed **Bounded action grace**, `GDR-CAND-20261010-G02-PAT-01`, owns the distinct input-eligibility technique and is not resent.

Genre-neutral adaptation facets include route discovery versus execution, continuous versus discrete control, fixed versus variable movement state, solo versus shared authority, and sustained versus short-burst interaction. No one-file-per-genre guidance is newly researched or substituted here. A precision-centered task may deliberately preserve commitment that a navigation-centered task removes; that is a conditional difference to test, not a genre label deciding the outcome. [C-18]

## Examples and counterexamples

### Documentary, versioned negative case

Celeste’s V1.4.0.0 release notes report corrections concerning moving-platform momentum, post-respawn behavior and Dash Assist soft locks. The exact locator is that version’s “Physics and Gameplay Changes” and “Bug Fixes,” including the Farewell bird and Ch5/Ch9/cutscene cases. This is direct inspection of a release-note artifact, not reproduction of a game bug. It justifies including state transitions in the review scope; it does not establish how often they fail. [C-15; GDR-SRC-20261010-F04-013]

### Illustrative: arrival is not a usable route

An invented crossing offers a short gap followed by a climb. The actor has one expendable air burst; the far-side climb also requires that burst. Reaching the far ledge consumes it, leaving no onward action. A route indicator based only on the first landing would overstate viability. Possible designs are to preserve a return route, provide an explicitly supported recharge, change the arrival state, or declare a deliberate one-way commitment. Each changes the rule; none is automatically the correct fix. No real game is represented. [C-07, C-12, C-13]

The strong counterexample is an intentional descent into a new area where returning is not promised and onward progress remains available by another capability. A rule requiring immediate reversibility would erase that design. Audit the actual goal and disclosed commitment instead. [C-07, C-18]

### Illustrative: several ways to miss the same landing

A player misses a platform in four invented conditions: the jump request was early and discarded; the request launched correctly but the release rule shortened the arc; the moving platform changed the relative landing region; or the camera concealed the relevant edge. A larger jump impulse might accidentally help one case while worsening another. First identify which relationship failed. The reviewed grace pattern addresses only the applicable eligibility case. [C-02, C-04–C-06, C-08]

### Illustrative: preview is not execution

An advisory braking region can change with speed and braking capacity while leaving steering and brake execution with the player. Automatic braking instead performs a control action. The linked preview pattern supplies a deliberately simplified stopping-distance calculation and conditions where its prediction must be withheld. The calculation is an illustrative model, not actual vehicle tuning or a claim of safety. [C-11, C-12]

## Failure modes and constraints

**Access and platform.** Remapping, hold/toggle changes, reduced simultaneity, navigation cues and automatic execution target different demands. Camera motion and background effects need separate review; XAG 117 offers scoped guidance, not universal speed, FOV, jump height or VR comfort settings. No medical or compliance claim is made. [C-08, C-14, C-16]

**Localization and sensory communication.** A directional phrase may expire while being narrated. “Hold,” “press,” “release,” “attach” and “drop” can imply different control and risk. Preserve the operative rule through translation and alternate cues. Do not adopt CSS-pixel criteria as native rendered-text or physical-display equivalence; the inspected P01 correction remains intact. [C-16]

**Control and information ethics.** Previewing a hidden route can change discovery, and silently steering toward a suggested route can change player intent. Retaining a player-selected accommodation is not a failure of training. Explain assistance scope and exceptional states rather than treating its eventual removal as the desired outcome for everyone. [C-10–C-12, C-17]

**Production and exploitation.** Prediction can diverge from the real controller after a surface, velocity, contact, load or capability change. Respawn can restore position without restoring the same movement state. Proposed exploit cases include repeated momentum inheritance, resource restoration through transitions, escape via collision corrections and stale buffered input after mode changes. These are risk hypotheses, not reproduced defects. [C-06, C-12, C-19]

## Playtest and validation

**Proposed, not performed.** Recruit only after separate authorization. Record the exact implementation build, scene, route, hardware/input, display/camera and active assists. Include relevant motor, visual and cognitive access contexts without inferring diagnoses. Agree on meaningful benefit/harm margins, sample precision and stopping criteria locally. Participants retain required accommodations; comparisons that would remove access are not appropriate. [C-14, C-16, C-17]

| Discriminating question | Comparison, procedure and measures | Confounds / rejection criteria |
|---|---|---|
| Is a failure caused by input eligibility or trajectory control? | Compare baseline with only the relevant grace rule changed, separately from altered trajectory. Record recognized request, eligibility, contact, predicted destination and actual outcome. | Practice, changed camera, frame scheduling. Reject the eligibility explanation if legal inputs still fail for unchanged trajectory reasons. [C-02, C-05] |
| Does greater correction help the intended skill? | Compare committed and more-correctable motion on matched tasks. Ask prediction before movement; measure recovery choices, task outcome and valued expression separately. | Different route feasibility and opportunity costs. Reject “better control” as a complete account if valued planning is removed or preference divides by task. [C-04, C-18] |
| Does a preview inform rather than distract or dictate? | Compare no preview, a simple landmark and state-conditioned information without automation. Include stale-state challenges and answer-varying prediction cases. | Better visibility, reduced task uncertainty and unfamiliarity. Reject the preview if it misleads, hides important cues or adds no useful benefit over the simpler alternative. [C-11, C-12] |
| Are recovery and route costs coherent? | Examine low-resource arrival, interrupted climb, changed support, altered assist, scene transition and re-entry. Record route availability, explanations, repetition and voluntary withdrawal. | Prior route knowledge and local reward changes. Reject route support when promised continuation disappears without a declared commitment consequence. [C-07, C-13, C-19] |
| Do vehicle assist interpretations hold? | Combine task-specific driving performance with voluntary setting choices and reasons. Preserve device/camera context and distinguish access from challenge preference. | Self-selection, experience, vehicle/course mix and absent telemetry fields. Reject readiness inference when assist status fails to track the stated construct. [C-09, C-10, C-17] |

Same-rule transfer requires new surface cases with genuinely different correct predictions. Changed friction under a known friction-dependent rule can be a same-rule case; silently replacing that rule is a separate adaptation test. A correct prediction does not require the player to prefer or execute that action. [C-17]

## Claim ledger

Confidence applies to the stated proposition, not to universal effectiveness. Proposed design models are not formal standards or approved studio decisions. Local claim IDs do not identify claims in another entry.

### C-01

**Claim:** Separate locomotion—the rules changing an actor’s motion—from traversal—the use of capabilities and routes to reach a goal at a cost.

**Class:** `inference`. **Support / contrary case:** F04 working definitions, informed by reviewed F02-decision and the distinction among navigation, input and recovery options in GDR-SRC-20261010-F04-004.

**Applicability:** Genre-neutral analysis; not a mandated engine architecture or universal vocabulary.

**Confidence:** Moderate: useful separation of decisions, with local definitions required.

**Unresolved / discriminating question:** Is the problem route knowledge, movement execution, capability availability or recovery cost?

### C-02

**Claim:** Input delivery, command recognition, action eligibility, resulting motion and displayed feedback are distinct possible causes of a failed movement.

**Class:** `inference`. **Support / contrary case:** Reviewed P02-input and P02-feedback; no primary latency effect estimate imported. GDR-SRC-20261010-F04-012 is lead-only.

**Applicability:** Requires known input/device, action rules and feedback path.

**Confidence:** Moderate for diagnostic separation; no quantitative perception model.

**Unresolved / discriminating question:** Would changing eligibility help when the actual defect is delayed or absent input?

### C-03

**Claim:** Fasterholdt and colleagues operationalize multiple jumping characteristics through artifact measurement; their analysis is not an experiment demonstrating player enjoyment.

**Class:** `empirical-evidence`. **Support / contrary case:** GDR-SRC-20261010-F04-007, PDF pp. 4–7 and 12–13; Table 2 screenshot inspected. Limbo/Super Meat Boy measurements; Mario component uses earlier Aldrich data.

**Applicability:** Comparative jumping analysis with normalization/model limitations; excluded movement cases remain excluded.

**Confidence:** High for the inspected methodological distinction; moderate for generalizing the descriptors.

**Unresolved / discriminating question:** Which measured characteristic, rather than a game title or overall height, explains a local control problem?

### C-04

**Claim:** Treat acceleration, reversal, braking, air control, release behavior and inherited momentum as separately adjustable design variables before inferring a universal movement recipe.

**Class:** `inference`. **Support / contrary case:** Analytical extension of GDR-SRC-20261010-F04-007, measurement framework, and GDR-SRC-20261010-F04-006, Actor Basics/moving-solid behavior.

**Applicability:** Variable independence is conceptual; actual implementations may couple them.

**Confidence:** Moderate for diagnostic utility; no universally preferable settings.

**Unresolved / discriminating question:** Does changing one variable alter desired expressive control or unrelated route feasibility?

### C-05

**Claim:** The creator’s Celeste account distinguishes recent-ground grace and early jump requests from other movement forgiveness mechanisms.

**Class:** `practitioner-heuristic`. **Support / contrary case:** GDR-SRC-20261010-F04-005, numbered items 1–3, 7 and 10; reviewed G02-grace owns the reusable eligibility pattern.

**Applicability:** Historical creator description; no exact runtime build or player experiment.

**Confidence:** High for the distinction in the text; low for a universal learning effect.

**Unresolved / discriminating question:** Is the failure a boundary-eligibility issue, trajectory issue, collision issue or recovery issue?

### C-06

**Claim:** Maddy Thorson’s implementation account distinguishes a moving solid carrying, pushing or squishing an actor, with explicit precedence.

**Class:** `observed-example`. **Support / contrary case:** GDR-SRC-20261010-F04-006, moving-solid sections and The Heavy Lifting. Observation target is the implementation article, not executed code.

**Applicability:** Celeste/TowerFall implementation family; no recommendation to adopt its coordinate or collision conventions.

**Confidence:** High for the account’s structure; operation in a particular build is unverified.

**Unresolved / discriminating question:** Which contact relationship is preserved or invalidated when support moves?

### C-07

**Claim:** A navigation ability changes a usable route only when its prerequisites, entry state, exit state and remaining costs make the route viable.

**Class:** `inference`. **Support / contrary case:** F04 reachability reasoning; reviewed F02-decision commitment and G02-grace validity boundaries. W03/F03 route/economy conclusions unavailable.

**Applicability:** Climb, jump, grapple, swim, mount or other capabilities; topology authored by Worlds remains a dependency.

**Confidence:** Moderate for state-conditioned reachability; low for experience effects.

**Unresolved / discriminating question:** Can the player arrive without the resource or movement state needed to continue or return?

### C-08

**Claim:** Forgiving recovery, input grace, collision tolerance, auto-execution and information assistance change different parts of a traversal problem.

**Class:** `inference`. **Support / contrary case:** GDR-SRC-20261010-F04-004, Navigation and Traversal documentation; reviewed P02-input/F02-difficulty/G02-grace.

**Applicability:** These mechanisms can interact and are not necessarily separable in all implementations.

**Confidence:** Moderate for separating interventions; comparative effects untested.

**Unresolved / discriminating question:** Does the chosen assistance address the intended barrier without silently changing another task?

### C-09

**Claim:** Forza Motorsport 4 telemetry studied assist configurations in 220,000 sampled players and 24.5 million race entries; entries include abandoned as well as finished races.

**Class:** `empirical-evidence`. **Support / contrary case:** GDR-SRC-20261010-F04-008, PDF p. 3 Data and sampling footnote: 5% systematic ID-modulo sample, October 2011–July 2013.

**Applicability:** Historical Xbox 360 observations, not independent trials or a current Forza population.

**Confidence:** High for reported dataset/procedure; representativeness beyond the sampled system is uncertain.

**Unresolved / discriminating question:** How would device, camera, player goal and retained access change the interpretation?

### C-10

**Claim:** The Forza paper’s assist-transition success label concerns continued non-use of an assist, not a direct measurement of independent mastery or wellbeing.

**Class:** `inference`. **Support / contrary case:** GDR-SRC-20261010-F04-008, PDF p. 5 Assist transitions and p. 3 missing input-device/camera fields.

**Applicability:** A critique of construct interpretation, not rejection of the paper’s recorded behavior or models.

**Confidence:** High that the operational outcome differs from those constructs; causes of switching remain uncertain.

**Unresolved / discriminating question:** Would direct task performance and player explanations support the same readiness interpretation?

### C-11

**Claim:** An informational traversal preview can be conceptually separate from automatic braking, steering or input grace.

**Class:** `inference`. **Support / contrary case:** GDR-SRC-20261010-F04-008, p. 2 Assists, distinguishes line assistance from automatic controls; reviewed P02-input supplies control/eligibility boundaries.

**Applicability:** The proposed F04 preview is broader than the documented line feature; its complete design is untested.

**Confidence:** Moderate for the distinction; low for proposed benefits outside that example.

**Unresolved / discriminating question:** Is the player being informed, having an action executed, or receiving a changed physical rule?

### C-12

**Claim:** A state-conditioned preview may improve prediction of a stop, landing or contact only while its model remains sufficiently truthful and its attention cost acceptable.

**Class:** `hypothesis`. **Support / contrary case:** F04-PAT-02 synthesis from C-03, C-04, C-06 and C-11; no direct comparative test of this complete recipe.

**Applicability:** Advisory, explicitly conditional information; excludes guarantees under unmodeled state or hidden facts.

**Confidence:** Low: both comprehension benefits and strategic/attention costs remain untested.

**Unresolved / discriminating question:** Does a simpler landmark work as well, or does the preview mislead after state changes?

### C-13

**Claim:** Traversal costs can be analyzed as time, control effort, expendable resources, exposure, opportunity cost and recovery consequences rather than one scalar distance.

**Class:** `inference`. **Support / contrary case:** Original F04 model using F02-decision opportunity-cost distinctions and C-07. F03 economies are not transferred.

**Applicability:** Choose only dimensions relevant to the actual goal and audience; do not infer equivalent subjective values.

**Confidence:** Moderate for accounting; low for comparative preference predictions.

**Unresolved / discriminating question:** Does the cost create a meaningful route choice, or merely repeat already-mastered work?

### C-14

**Claim:** Microsoft XAG 117 recommends configurable motion-related presentation with scope qualifications; it does not supply a universal traversal comfort setting.

**Class:** `practitioner-heuristic`. **Support / contrary case:** GDR-SRC-20261010-F04-011, implementation guidelines and gameplay-motion note; checked revision dated 2026-03-04.

**Applicability:** Vendor guidance, not a formal standard, medical advice, VR result or game-specific compliance evaluation.

**Confidence:** High for document scope; no verified efficacy for a receiving game.

**Unresolved / discriminating question:** What do the actual display, camera, movement task and audience require?

### C-15

**Claim:** The Celeste V1.4.0.0 release notes report corrections involving moving-platform momentum, post-respawn behavior and Dash Assist soft locks.

**Class:** `observed-example`. **Support / contrary case:** GDR-SRC-20261010-F04-013, V1.4.0.0 Physics and Gameplay Changes / Bug Fixes.

**Applicability:** Observed official change record; no bug reproduction, current build verification or all-platform coverage.

**Confidence:** High for the versioned note; causal mechanism and frequency not established here.

**Unresolved / discriminating question:** Which movement/assistance states must be revalidated after a respawn or scene transition?

### C-16

**Claim:** Localization, sensory alternatives and input configurations should preserve movement-relevant facts, meaningful control and state validity, not just mirror labels.

**Class:** `inference`. **Support / contrary case:** Reviewed P02-multimodal and P01-visual; GDR-SRC-20261010-F04-004, Alternate Controls/Navigation and Traversal; GDR-SRC-20261010-F04-013, V1.3.1.0 localization qualification.

**Applicability:** Local controller, touch, alternative-input and language contexts need separate evidence; no parity guarantee.

**Confidence:** Moderate for identifying review obligations; audience outcomes unmeasured.

**Unresolved / discriminating question:** Does a translated or alternate cue arrive with enough context before its information expires?

### C-17

**Claim:** Assess learning and precision separately from selected assist status, using answer-varying same-rule cases and voluntary comparisons that retain required accommodations.

**Class:** `inference`. **Support / contrary case:** Reviewed F01-transfer corrected recipe; C-09–C-10 and reviewed F02-difficulty.

**Applicability:** Proposed test design, not a result or mandate to remove assistance.

**Confidence:** Moderate for construct separation; no learning effect demonstrated.

**Unresolved / discriminating question:** Can a participant predict a new trajectory without assuming every unfamiliar case should be rejected?

### C-18

**Claim:** Committed motion is a legitimate alternative when predicting and accepting a trajectory is central; increasing correction freedom may change, not simply improve, the task.

**Class:** `hypothesis`. **Support / contrary case:** Rival interpretation of C-04–C-08 and reviewed F02-decision commitment analysis.

**Applicability:** Depends on the intended expression, audience and input context.

**Confidence:** Low for any general preference claim.

**Unresolved / discriminating question:** Does greater correction preserve valued planning and technique or erase them?

### C-19

**Claim:** Movement production review should include contact transitions, state resets, unsupported exits, assist/model divergence and costs after failure, not just a successful clean-room route.

**Class:** `hypothesis`. **Support / contrary case:** Original risk synthesis from C-06–C-08, C-12–C-13 and documentary negative case C-15.

**Applicability:** No engine or gameplay test executed; exact risks depend on rules.

**Confidence:** Moderate for testable risks; low for their occurrence in an unspecified game.

**Unresolved / discriminating question:** Which state invalidates a promised route, preview, recovery or input?

## References

All source IDs are temporary F04 identities. Access date: 2026-10-11 UTC (2026-10-10 in America/Los_Angeles). Locators specify the inspected extent, not an assertion that every linked item was read in full. Public-source bytes were not archived or hash-verified.

### GDR-SRC-20261010-F04-004

Naughty Dog; displayed byline Matthew Dunnerstick. **[The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed)**. Naughty Dog; 2020-06-09. Edition/build: PS4 launch-era feature documentation; page also contains Patch 1.01/1.02 annotations; not a current remaster verification.

**Access:** `relevant-excerpt`. **Type:** Official feature documentation. **Locator:** “Alternate Controls”; “Assistance”; “Navigation and Traversal” rows Navigation Assistance, Traversal Assistance and Ledge Guard; “Combat Accessibility” rows and encounter exceptions. **Limits:** Documents intended options, not measured accessibility, enjoyment, transfer, or efficacy in a verified running build. **Relationships:** Same URL appears in reviewed F02 as GDR-SRC-20261010-F02-011 and W02 as GDR-SRC-20261010-W02-017. Re-inspected here; mapping/deduplication pending, not independent evidence. **Rights:** Copyright Naughty Dog; paraphrase only; no screenshots or videos redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-005

Maddy Thorson. **[Celeste & Forgiveness](https://www.maddymakesgames.com/articles/celeste_and_forgiveness/index.html)**. Maddy Makes Games; unknown. Edition/build: Undated creator article; game build not specified.

**Access:** `relevant-excerpt`. **Type:** Firsthand developer rationale. **Locator:** Numbered items 1–3 (recent-ground grace, early jump request and jump apex); items 7 and 10 (stored platform momentum and stamina-related interpretation). **Limits:** Text inspected, not a game replay or player study. Author-specific values are not portable timing/pixel recommendations. **Relationships:** Same source as reviewed GDR-SRC-20261010-G02-001; same creator/production family as F04-006 and F04-013. Central deduplication pending. **Rights:** Copyright author; paraphrase only; no GIFs redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-006

Maddy Thorson. **[Celeste & TowerFall Physics](https://www.maddymakesgames.com/articles/celeste_and_towerfall_physics/index.html)**. Maddy Makes Games; unknown. Edition/build: Undated implementation article; no precise game build identified.

**Access:** `relevant-excerpt`. **Type:** Firsthand technical implementation account. **Locator:** “Actor Basics”; moving-solid preparation and “The Heavy Lifting,” especially carry/push/squish behavior and push priority. **Limits:** One implementation family, not a recommended universal collision engine or independently validated movement effect. **Relationships:** Same creator as F04-005 and production family as F04-013; not independent corroboration. Central deduplication pending. **Rights:** Copyright author; paraphrase only; code neither reproduced nor executed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-007

Martin Fasterholdt; Martin Pichlmair; Christoffer Holmgård. **[You Say Jump, I Say How High? Operationalising the Game Feel of Jumping](https://dl.digra.org/index.php/dl/article/download/771/771/768)**. DiGRA/FDG 2016; 2016. Edition/build: Conference paper; DOI 10.26503/dl.v2016i1.771; 16-page PDF.

**Access:** `relevant-excerpt`. **Type:** Original comparative artifact-measurement research. **Locator:** PDF pp. 4–6 (measurement/normalization method); p. 7, Table 2 and exclusions beneath it; pp. 12–13 (interpretation/conclusion). Screenshot of PDF p. 7 inspected.. **Limits:** Not a player-preference or enjoyment experiment. Limbo/Super Meat Boy measurements differ in provenance from Mario data drawn from Aldrich. Measurement/model limitations remain. **Relationships:** Mario component is derivative of the cited earlier account, not a third independent new measurement. Underlying raw data and Aldrich source not inspected. Central deduplication pending. **Rights:** Copyright 2016 authors; paper distinguishes permitted personal/classroom use from commercial permissions. Paraphrase only; no paper, tables, figures or source code redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-008

Thomas Debeauvais; Thomas Zimmermann; Nachiappan Nagappan; Kevin Carter; Ryan Cooper; Dan Greenawalt; Tyson Solberg. **[Off With Their Assists: An Empirical Study of Driving Skill in Forza Motorsport 4](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/debeauvais-fdg-2014.pdf)**. FDG 2014; official Microsoft Research copy; 2014-04 (conference record). Edition/build: 8-page paper; Xbox 360 Forza Motorsport 4 telemetry from October 2011–July 2013. PDF title uses “Motorsport”; landing-page title uses “Motorsports.”.

**Access:** `relevant-excerpt`. **Type:** Original observational telemetry research. **Locator:** PDF p. 2 “Assists”; p. 3 “Data” and sampling footnote; p. 5 “Assist transitions”; p. 8 discussion/conclusion. Claims here use prose, not table/figure values.. **Limits:** No raw telemetry obtained. PDF text readable, but screenshot requests for pp. 2 and 5 failed, including a retry. Visual-table verification unavailable. No causal assist-removal recommendation inferred. **Relationships:** University/Microsoft Research/Turn 10 collaboration; not independent of the game producer. Distinct method from vendor guidance, not a replication of it. Central deduplication pending. **Rights:** Copyright authors/publisher; exact redistribution license not established; paraphrase only. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-011

Microsoft. **[Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117)**. Microsoft Learn; last updated 2026-03-04. Edition/build: Live unnumbered web revision checked on access date.

**Access:** `relevant-excerpt`. **Type:** Platform/vendor practitioner guidance, not a formal standard asserted by F04. **Locator:** Implementation guidelines and gameplay-motion scope note; camera movement/shake, motion blur and configurable motion-related presentation. **Limits:** No universal camera/FOV/velocity values, VR efficacy finding, comfort guarantee or medical recommendation. **Relationships:** Same URL as reviewed GDR-SRC-20261010-P02-010 and GDR-SRC-20261010-P01-10. Those historical identity spellings are preserved; central deduplication pending. **Rights:** Microsoft documentation; paraphrase only; no example media redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-012

Normoyle; Guerrero; Jörg (lead metadata only). **[Player Perception of Delays and Jitter in Character Responsiveness](https://people.computing.clemson.edu/~sjoerg/docs/Normoyle14_DelayAndJitter.pdf)**. SAP 2014 / author and institutional routes; 2014 (lead metadata). Edition/build: Lead metadata: DOI 10.1145/2628257.2628263; pp. 117–124; full text inaccessible here.

**Access:** `lead-only`. **Type:** Potential original empirical study; not evidence used by F04. **Locator:** No result passage inspected. Search results/metadata used only to identify the lead.. **Limits:** Author PDF and two University of Pennsylvania repository download routes returned access errors. Local public-source download attempts also failed DNS. No delay/jitter threshold or study result imported. **Relationships:** No support claims assigned. Cross-batch identity check pending. **Rights:** Rights unverified; no text or figures reproduced. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-013

Celeste development team. **[Celeste — Changelog](https://www.celestegame.com/changelog.html)**. Official Celeste website; individual release dates unknown on inspected page. Edition/build: Inspected page headed V1.4.1.0; specific examples scoped to V1.4.0.0 and V1.3.1.0, not all platforms/current runtime.

**Access:** `relevant-excerpt`. **Type:** Observed release-note artifact / official change record. **Locator:** V1.4.0.0: New Options; Physics and Gameplay Changes; Bug Fixes (Farewell bird after respawn, Ch5/Ch9 facing, Dash Assist cutscene/credits soft locks). V1.3.1.0 Changes and Additions (localization qualification).. **Limits:** Observes what the release notes report, not reproduced bugs or a verified current game build. Platform rollout/build hash not established. **Relationships:** Same URL as reviewed GDR-SRC-20261010-G02-008; related production family to F04-005/006. Central deduplication pending. **Rights:** Copyright Celeste developers; paraphrase only; no art/code redistributed. Claim bindings appear in this entry’s ledger.

### Inspected reviewed-candidate dependencies

These are unreleased library candidates, not independent empirical sources. Exact bytes were read from the parent-selected archive; only the stated conceptual distinctions transfer. Their original public empirical findings are not reasserted without fresh source inspection. Missing package-local copies are deliberate: previous batches are not resent.

- **`GDR-CAND-20261010-F02-TOP-01`**, `selected-drafts/topics/decision-design.md`, version `0.1.0`, draft, revision `initial-capture-1`. SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`. Inspected relevance: Decision/scope, mechanisms, choices and claim ledger; decision prediction versus preference; commitment and information.
- **`GDR-CAND-20261010-F02-TOP-02`**, `selected-drafts/topics/challenge-and-difficulty.md`, version `0.1.0`, draft, revision `independent-review-correction-1`. SHA-256 `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1`. Inspected relevance: Mechanisms, assistance, recovery and tests; corrected evidence locator preserved without importing empirical numerical results.
- **`GDR-CAND-20261010-P02-TOP-01`**, `selected-drafts/topics/controls-and-input.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `b9235153ba8b742c6df47e9e23844d9ab5da82e4212ebd22f04e314f6ccce21b`. Inspected relevance: Action recognition/eligibility/outcome; buffering/context validity; remapping versus input-demand changes.
- **`GDR-CAND-20261010-P02-TOP-02`**, `selected-drafts/topics/feedback-and-game-feel.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `6cf571a87946b9b40470cce966862219906f495b50c0b1db04e1ad7677ca4415`. Inspected relevance: Event facts versus ornament; deliberate timing versus system latency; outcome measures not interchangeable.
- **`GDR-CAND-20261010-P02-TOP-03`**, `selected-drafts/topics/multimodal-communication.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c`. Inspected relevance: Fact-preserving alternatives; deadline/context boundaries; competing attention; no modality-equivalence claim.
- **`GDR-CAND-20261010-F01-PAT-01`**, `selected-drafts/patterns/supported-attempt-and-transfer-check.md`, version `0.1.0`, draft, revision `independent-review-correction-1`. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Inspected relevance: Corrected answer-varying examples; same-rule transfer separated from changed-rule adaptation.
- **`GDR-CAND-20261010-P01-TOP-01`**, `selected-drafts/topics/visual-communication.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `b8e23ae234041fa0893295fdd36457eb08e0e77a60cca4229b7a77f0f13844b7`. Inspected relevance: Numerical accessibility scope: CSS/point criteria versus rendered text-body height and platform guidance.
- **`GDR-CAND-20261010-G02-PAT-01`**, `selected-drafts/patterns/bounded-action-grace.md`, version `0.1.0`, draft, revision `initial-1`. SHA-256 `03e0819fc92f1e6fcfe87d84871d2cbb6de337d3bcd57e044e614cb3d2773f1c`. Inspected relevance: Early/recent-state eligibility; single consumption, expiry, cancellation; ownership pending; benefit remains conditional.

Archive receipt, transfer limits and unresolved links: [F04 review packet](../reviews/full-run-20261010-f04-review-packet.md#reviewed-dependency-inspection). No canonical identity or release is implied.

## Open questions and change history

**Coverage remains open.** The source mix includes artifact measurement, historical vehicle telemetry, creator accounts and platform guidance—not a general movement-efficacy experiment. A potentially relevant delay/jitter paper remains lead-only. Forza PDF text was accessible, but page-image requests failed; no table/figure effect value is used. Flight, swimming, VR, touch, alternative-input performance, current platform parity and production-scale collision validation require further research.

The strongest uncertainty is whether better prediction information improves the desired experience rather than replacing discovery or prescribing a route. The second is how to measure the value of assistance without equating non-use with competence. See `F04-CON-05`, `F04-CON-07` and the [review packet](../reviews/full-run-20261010-f04-review-packet.md) for rival explanations and proposed child work.

**History:** version `0.1.0`, candidate revision `initial-1`, attempt `F04-attempt-1`; initial submission, no predecessor or supersession. Hashes are in the [integrity receipt](../reviews/full-run-20261010-f04-integrity-receipt.md). No independent F04 review or approval occurred. Next: independent evidence/content review and central registration of any agreed extensions, not implementation or release.
