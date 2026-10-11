---
id: GDR-CAND-20261010-G18-GEN-01
kind: genre
title: Racing
version: 0.1.0
status: draft
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G18
candidate_revision: initial-author-draft-1
attempt_identity: G18-current-dispatch-1
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; run identifier retains dispatch date 2026-10-10
coverage_status: open
independent_review: not-performed
aliases:
- racing game
- driving competition
- time-trial racing
tags:
- trajectory
- speed-control
- vehicle-model
- assistance
- competition-context
- accessibility
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G18-PAT-01
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-P02-PAT-01
- GDR-CAND-20261010-F02-PAT-02
related_genres:
- GDR-CAND-20261010-G18-GEN-02
source_ids:
- GDR-SRC-20261010-G18-001
- GDR-SRC-20261010-G18-004
- GDR-SRC-20261010-G18-005
- GDR-SRC-20261010-G18-006
- GDR-SRC-20261010-G18-014
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial G18 draft; no earlier G18 candidate bytes identified in this
  execution.
byte_identity: Exact SHA-256 is recorded in the accompanying integrity receipt; no
  self-hash is embedded.
---

# Racing

**Draft research candidate, not released knowledge.** This entry addresses racing decisions, not every simulation, vehicle game or motorsport rulebook. It contains documentary examples, two narrowly applicable empirical sources, reviewed-but-unreleased shared dependencies, and explicitly proposed design hypotheses. No game build was played, prototype executed or participant tested for G18. The exact [review packet](../reviews/full-run-20261010-g18-review-packet.md) and [integrity receipt](../reviews/full-run-20261010-g18-integrity-receipt.md) identify this snapshot.

## Definition and boundaries

For this library, **racing** means a game structure in which traversing a constrained course or route, and the resulting time, completion order or comparable traversal result, organizes the principal competitive objective. This is a working **inference**, not a universal industry definition. Vehicles are a common design context of the inspected examples, not a membership requirement. The definition deliberately includes isolated time trials and shared races while leaving their demands distinct. [R-C01]

A useful boundary test is: *What changes the winner, and which decisions does that make consequential?* A game may depict fast cars yet reward ball control, elimination or delivery planning rather than traversal performance. Such play does not become racing merely through its camera, vehicle asset or brand. Conversely, a fictional movement model can support racing without reproducing real automobile behavior. These are classification decisions proposed for this library, not approved taxonomy changes. [R-C01]

[Racing and sports](sports.md) overlap where a motorsport competition also has sporting rules, officiating, roles and seasons. Keep this file for route/trajectory, speed-control, vehicle-model and race-comparison decisions. Use the sports file for role abstraction, team authority, sporting rules and match/season structure. Neither file owns general controller design or simulation architecture. A vehicle-combat race may retain racing as its organizing goal while introducing interference and recovery decisions; an elimination-only vehicle arena may not. Evaluate the mode rather than assigning every mode of a title one label. [R-C01; R-C09]

“Simulation,” “arcade,” “realistic,” “accessible” and “competitive” are insufficient decision specifications on their own. Separate at least the modeled relation between input and motion; the actions left to the player; the information available before commitment; the consequences of mistakes; and the comparison used to declare success. Calling a model realistic does not establish its enjoyment, learnability, accessibility or competitive suitability. [R-C04; R-C06]

## Custom research instructions

Future extensions must begin with a **particular racing decision**: choosing a line, controlling entry speed, preserving exit options, overtaking, recovering, selecting a vehicle, configuring assistance or comparing attempts. Identify the task and intended audience before searching for an optimal handling or assistance setting. Frame competing explanations for a poor result: incomplete route information, misunderstood vehicle response, an inaccessible control action, an opponent interaction, a rules violation, a preference for a different goal, or ordinary performance variation. Do not diagnose all of them from one lap time. [R-C06; reviewed dependencies D03, D04, D06]

Inspect a representative range rather than treating one realistic car title as the whole genre: isolated hot laps; shared circuits; route discovery or rally-like information demands; arcade steering/boost rules; contact-heavy competition; motorcycle or non-car models; alternative inputs; and re-entry after interruption. **Only part of that range was directly documented in this batch.** Rally communication, motorcycle dynamics, force-feedback calibration, weather-model validity, opponent-policy effects and networked collision adjudication remain evidence gaps. They must not be filled from familiarity with named games.

Use official build notes and rules for behavior; original papers for measured player effects; first-person development accounts for intent; and reproducible versioned captures for game observations. Record track, route direction, surface/weather, vehicle configuration, assistance, session mode and opponent conditions where relevant. A handling comparison without those conditions may answer a different question from the advertised one. Do not substitute a manufacturer’s feature announcement for disabled-player evaluation, or an AI benchmark for human enjoyment. [R-C08; R-C10]

Challenge misleading comparisons explicitly: controller novices against wheel enthusiasts; a familiar car against an unfamiliar one; a patched physics model against its predecessor; a ghost against an interfering opponent; a player’s previous best against their typical performance; and removing an accommodation while calling the task unchanged. No universal reaction-time, braking-distance, lap-improvement, steering-angle, controller-buffer or rank threshold is established here. [R-C06; R-C08; R-C12]

## Player promises and varied audiences

The following are **candidate experience targets**, not claims that all racing players want them: discovering a controllable trajectory, sustaining a sensation of speed, improving repeatability, solving setup problems, making tactical passes, competing socially, or enjoying a fictional driving fantasy. Select a promise and specify what the player must actually decide. Someone seeking tactical contest can reasonably retain automatic shifting; someone seeking a clutch-operation challenge can reasonably prioritize that action. Treat those as different local design contracts rather than stages on one mandatory ladder. [R-C05; R-C06]

A person may want the same strategic challenge with less sustained actuation, clearer orientation information or a different input device. Another may prefer extensive automation and focus on route selection or participation. These are proposed distinctions for eliciting preferences; this batch does not estimate their population prevalence. Ask about the experience and access route, not a medical diagnosis or an assumed “beginner” identity. [R-C05; R-C12]

### What the empirical material actually permits

The FM4 paper analyzes **220,000 player IDs and 24.5 million race entries, October 2011–July 2013**; entries include abandonment. Sampling used every twentieth database ID. Its “successful” assist removal means staying disabled within observation, not directly demonstrated mastery or enjoyment. Some assistance persisted or was repeatedly restored. This is observational, developer-affiliated evidence, without input-device/view or steering-assist telemetry; it does not justify compulsory removal. [R-C02; GDR-SRC-20261010-G18-001, PDF pp. 3, 5, 7]

Skalski and colleagues’ racing study used **78 students aged 18–25**, ten-minute PC *Need for Speed Underground 2* sessions and four controller conditions; the race could not be completed. Naturalness favored the wheel, but the presence–enjoyment result depended on analysis/model. These are not long-term learning, assist-policy or access findings. [R-C03; GDR-SRC-20261010-G18-014, pp. 234–238]

The design implication is narrower than either “assists prevent mastery” or “a natural wheel makes racing fun.” Keep **operational control, learning, performance, perceived naturalness and enjoyment as separate outcomes**. The studies justify challenging a bundled assumption, not choosing one device or assistance policy for every player. [R-C04]

## Characteristic loops and structures

### Moment-to-moment: trajectory under a chosen movement rule

A practical design model is **read the situation → predict motion → commit input → observe response → revise**. The decisive question is what information permits prediction and what remains controllable after commitment. Under one fictional model, slowing before a bend preserves an exit trajectory; under another, drifting charges a resource and deliberately trades stability for a later burst. Neither relation is required by the genre. The designer must make the selected relation inspectable and test whether the player can distinguish its useful and harmful cases. [R-C06]

For route design, separate the **legal corridor**, the **currently feasible trajectory** and the **preferred trajectory for a goal**. They need not coincide. A clearly marked legal inside lane may be poor for a following corner; a fast solo line may be inappropriate beside another vehicle. A guide that collapses these into one authoritative line can conceal why a choice changes. This is a reasoned design risk, not a measured universal effect. A simpler alternative is to teach one relation with a stable vehicle before adding route alternatives. [R-C06]

### Attempt/session: finish, compare, recover and choose again

A time trial isolates repeatable traversal more readily than a live contest, but cannot by itself evaluate yielding, defense or collision recovery because those actions require another agent. This is an inference about task contents, not evidence that time trials are superior training. A shared race adds decisions about other participants and their uncertainty; it also changes what a slow segment can mean. Yielding safely may be an intended decision rather than failed speed control. [R-C07]

Recovery policy is a design variable: restart the segment, restore the full attempt, continue with lost position, or allow a bounded rewind in a declared mode. Each changes the stakes and the unit of comparison. When a retry resumes with a different entry speed, tire state or rival position, a second attempt may no longer test the same relation. Preserve enough context to explain the difference, or describe the session as exploration rather than a controlled comparison. [R-C07; R-C08]

### Long horizon: mastery, access and progression

Separate **learning a relation**, **earning equipment**, **unlocking places**, **tuning a vehicle** and **advancing a championship**. These are candidate structures, not empirically validated retention recipes. Increasing available power can improve a recorded time without establishing better control; an unfamiliar unlock can initially worsen it. A rental/equal-configuration practice option is therefore a plausible alternative when the learning question should be separated from ownership. It is not automatically the right economy for an exploration or collection game. [R-C11]

Long-horizon goals need not demand successively fewer assists. A player could seek more consistent lines, more considered passes, broader route competence or a personal championship under a chosen assistance profile. Those goals remain hypotheses about useful progression framing; the FM4 record cannot decide which one players will value in a new game. [R-C05; R-C11]

## Design choices and evidence-to-application bridges

| Decision | Conditional approach and proposed benefit | Costs, failure cases and alternative |
|---|---|---|
| Vehicle-model fidelity | Choose the response relations essential to the intended decisions; expose their consequences before adding more variables. A stable simplified model may serve a route-learning goal. [R-C06] | More modeled systems add tuning and explanation work. Simplification can remove the very relation an operational-simulation audience seeks. Test the intended task, not a “realism” label. |
| Guidance versus action automation | Diagnose missing information separately from inaccessible execution or unwanted operational load. Offer the corresponding kind of support rather than treating all support as one difficulty level. [R-C05] | A line or cue may reveal a decision the game intended to leave uncertain. Automation may remove a desired action. A settings preview and reversible trial are simpler than hidden adaptation. |
| Isolated versus shared competition | Use isolated attempts to investigate a repeatable route-control question; add opponents when interaction is part of the claim. [R-C07] | Solo performance is not racecraft proof. Opponent behavior, contact and network effects complicate attribution. Keep both evaluation questions when both promises matter. |
| Error consequences | Decide whether the design tests consistency over a whole attempt or repeated exploration of a local relation. Declare what a restart restores. [R-C07] | Severe consequences can prevent access to the practice opportunity. Very permissive resets can undermine an endurance or commitment goal. Neither outcome is universal. |
| Result comparison | Use the minimal context needed to support the stated performance claim; flag relevant unknowns. [R-C08] | Excessive profiles fragment participation and turn ordinary settings into stigma. Do not separate results for an irrelevant caption or narration preference. |
| Opponent adjustment | Consider a disclosed, bounded lever only after a diagnosis relevant to the intended contest. Preserve manual control and access supports. [R-C10; D10] | A secret catch-up rule may confound a claim of consistent opposition. Static opponents, selectable events or an openly handicapped social mode may better match the promise. |

### Assistance: distinguish the mechanism before selecting a policy

Turn 10’s 2023 account distinguishes information-oriented **Blind Driving Assists** from **One Touch Driving** automation and describes co-design participation and an audio learning curve. It is a firsthand feature/intent account, not independent evidence that either configuration works for every player. [R-C05; GDR-SRC-20261010-G18-005, named sections]

For a candidate design, identify whether support changes perception, input actuation, motion stabilization, decision selection, failure consequences or opposition. Then name the intended retained decision. For example, an orientation cue might preserve the choice of where to steer; automatic steering might deliberately delegate it. Test that distinction rather than asserting that all assistance preserves the same challenge. A player’s stated preference matters alongside observable performance. [R-C05]

Do not automatically fade a support because a person has completed several laps. A reversible reduction of an **instructional prompt** can be appropriate in an explicit learning test, but it is not the same as withdrawing orientation information or an accessible control route. When uncertain, keep the support, ask about the goal and compare explanations before changing the task. [R-C05; R-C12; D01, D02, D07]

### Comparison: rules and builds are part of the task

GT7 update **1.68** documents Balance of Performance (BoP) availability in Time Trials with stated exclusions, and practice-session ghost/retry changes in Power Pack. This is evidence of version-specific comparison conditions, not evidence that BoP makes all vehicles equivalent. [R-C08; GDR-SRC-20261010-G18-004, Other Improvements and Adjustments §§2, 4]

The proposed [Versioned Performance Comparison](../patterns/versioned-performance-comparison.md) pattern records only context relevant to the advertised claim. A personal history may retain unlike attempts with clear labels; a particular competition may require a declared shared configuration. Do not silently normalize a faster time into proof of greater skill. Equally, do not assume that every accessibility setting creates an unfair advantage and deserves a separate queue. Both conclusions require a specific task and evidence. [R-C08; R-C12]

## Applying shared topics without duplicating them

The selected dependency bytes were inspected from the parent-reviewed waves 1–2 archive. They remain **unreleased candidates**; their original source identities are preserved in the packet. The dependency links below lead to exact paths, IDs, revisions, hashes and inspected locators, not to unseen files or invented canonical references.

| Shared entry | Racing-specific adaptation |
|---|---|
| [Learning and onboarding — D01](../reviews/full-run-20261010-g18-review-packet.md#d01) | Test trajectory predictions across genuinely discriminating same-rule cases. An altered handling model is a rule-change orientation task, not automatically a transfer test. |
| [Accessibility and inclusive interaction — D02](../reviews/full-run-20261010-g18-review-packet.md#d02) | Test the route from boot/configuration through driving, recovery and continuation. Do not translate scoped web target-size guidance into steering, timing or native display thresholds. |
| [Challenge and difficulty — D03](../reviews/full-run-20261010-g18-review-packet.md#d03) | Separate route knowledge, input demands, consequence severity and rival behavior before diagnosing a slow lap. |
| [Controls and input — D04](../reviews/full-run-20261010-g18-review-packet.md#d04) | Distinguish a pressed brake action, an accepted command, the modeled response and visible feedback. Test sustained throttle, simultaneous actions and remap recovery separately. |
| [Multimodal communication — D05](../reviews/full-run-20261010-g18-review-packet.md#d05) | Preserve direction, urgency, reference frame and uncertainty of a racing fact; do not promise equal sensation from every modality. |
| [Evaluation and balancing — D06](../reviews/full-run-20261010-g18-review-packet.md#d06) | State whether the outcome is repeatability, best time, decision accuracy, successful access or enjoyment; keep relevant opponent/build context. |

Reviewed F01 discrimination and P01 numerical-scope corrections are retained. The package did not supply selected reviewed bodies for broader movement/traversal, simulation, progression/economies, camera, localization, or multiplayer/session guidance. The discussion here is G18 synthesis, not a transfer from those missing dependencies. [R-C12; packet dependency register]

## Pattern selection and adaptations

Use [Supported Attempt and Transfer Check — D07](../reviews/full-run-20261010-g18-review-packet.md#d07) when the question is learning an identifiable relation, not whether a player should abandon an assist. Preserve required cues; vary cases so that “always use the inside line” and “prepare the next exit” predict different outcomes. Ask separately for the prediction and preferred action. A player can knowingly choose a risky pass. [R-C12]

Use [Fact-Preserving Cue Alternatives — D08](../reviews/full-run-20261010-g18-review-packet.md#d08) for critical orientation, turn or warning information. Keep the reference frame clear: left of the current vehicle is not necessarily west on a map. Avoid making every available fact speak simultaneously. Its possible overlap with the earlier P01 critical-cue pattern remains a coordination issue, not two independent confirmations. [R-C12]

Use [Recoverable Action Remapping — D09](../reviews/full-run-20261010-g18-review-packet.md#d09) when changing brake, throttle, shift or recovery inputs. A successful menu binding is insufficient if the race requires an inaccessible hold or a now-conflicting recovery action. Use [Bounded Disclosed Difficulty Adaptation — D10](../reviews/full-run-20261010-g18-review-packet.md#d10) only for a clearly scoped adaptive mode. It does not authorize invisible interference with a claimed fixed time-trial benchmark. [R-C10; R-C12]

The sole newly extracted G18 pattern is [Versioned Performance Comparison](../patterns/versioned-performance-comparison.md), candidate `GDR-CAND-20261010-G18-PAT-01`. It is a conditional hypothesis, not an endorsed tournament standard. Additional potentially useful work is queued in the packet rather than exceeding the packet cap.

## Representative and negative cases

| Inspected case | What it establishes | What it does not establish |
|---|---|---|
| FM4 telemetry paper, Xbox 360 historical dataset | One operational account of assist-setting behavior. [R-C02] | A universal progression ladder, a participant accessibility profile or a causal effect of removing an assist. |
| Forza 2023 pre-release accessibility account | Distinct informational and automation intentions in a racing context. [R-C05] | Independent usability, released-build completeness or equal experience across sensory modalities. |
| Nintendo’s MK8 Deluxe page | Smart Steering is described as preventing off-track driving; a separate time-trial option is documented. [R-C09; GDR-SRC-20261010-G18-006, Perfect for beginners / Compete to beat your best] | Proof that assistance prevents mastery, or that “beginner” means one shared ability profile. |
| GT7 1.68 release note | A version-pinned change relevant to comparison. [R-C08] | General BoP equivalence or a verified current full ruleset. |
| Original controller study | A bounded challenge to equating natural input with enjoyment. [R-C03] | A recommendation to require wheels or reject gamepads. |

These cases favor commercially visible car games and accessible English-language sources. They are deliberately not a success-based proof set. Negative cases also include a hypothetical endurance design where repeated segment resets remove the intended whole-attempt challenge, and a social handicap race where equal vehicle performance is explicitly not the promise. Those are **illustrative counterexamples**, not observed player outcomes. [R-C07; R-C08]

### Worked example: two bends and an honest transfer check — illustrative, not performed

Assume a fictional vehicle model with a known braking response and two linked bends. The learning target is **predicting how the exit from one bend constrains the next**, not operating a real automobile. The player can see the route, use their usual orientation and input supports, and try the same vehicle repeatedly. [R-C13]

First present a practice case where a wide exit from the first bend leaves enough room for the next. Ask where the vehicle is likely to be after the transition and let the player select a line. Show the resulting position and the relevant earlier commitment, rather than declaring any unsuccessful lap a reaction-time failure. Next present a same-model case where the second bend turns the other way and the same wide exit is disadvantageous. Include a third case with enough intervening straight that it is again viable. These cases separate a relational prediction from blindly copying one trajectory. Exact geometry and vehicle values must be authored and checked locally; none are prescribed by this research. [R-C13; D07]

Compare an always-on ideal-line display with an optional orientation/route cue that leaves the trajectory decision to the player. This is a **proposed comparison**, not a recommendation to remove the former from people who prefer it. Ask for both prediction and chosen action: deliberately defending a position or avoiding contact may justify a different line from a solo best-time route. Record successful configuration, mistaken predictions, lost-control events, return to practice, perceived agency and enjoyment separately. [R-C13]

If the prototype changes tire response between trials, announce and teach that new rule. Do not count the resulting confusion as failure to transfer the old rule. If a participant cannot access the directional information, fix the access route before interpreting the result as a learning problem. Stop the learning comparison if the supposed alternatives do not actually produce distinguishable outcomes under the prototype’s response model. [R-C12; R-C13]

### Worked example: shared racing is not a hot-lap exam — illustrative, not performed

A second prototype uses the same route with a rival beside the player. One instruction asks for the fastest legal completion; another asks for a safe pass without contact. A slower segment may satisfy the second goal. Record the declared goal, opponent trajectory and available information before judging the maneuver. An assist that stabilizes the vehicle can coexist with a difficult overtaking decision; an automatic pass selector can instead delegate that decision. The evaluation must identify which occurred. [R-C07; R-C13]

An openly handicapped social event could grant different starting conditions to support a close contest. It should not then market the finish order as an equal-condition skill ranking. Conversely, a tightly specified record attempt should not silently change rival pressure or traction assistance to maintain excitement. These are distinctions in the meaning of the contest, not proof that either format is more enjoyable. [R-C08; R-C10]

## Accessibility, ethics, localization and production

**Access route.** Test configuration and recovery as well as cornering. Candidate checks include navigating assists without inaccessible defaults; previewing audio cues; maintaining steering while accelerating; recovering from a bad binding; identifying penalties without color alone; and pausing or returning after fatigue. These are proposed checks, not a certificate or a universal device specification. Do not use the P01 numerical correction as a source for a minimum racing HUD size or permitted reaction time. [R-C12; D02, D04, D05]

**Information integrity.** A nonvisual route cue should not unintentionally disclose a hidden rival or remove uncertainty that another mode is explicitly testing. Equally, visual presentation should not be treated as the definition of the game state merely because it was implemented first. Specify the needed fact and allowed uncertainty, then test whether the route is usable with the relevant sensory and input conditions. Multiple simultaneous modalities can also become competing work; selectable channels are an alternative. These are conditional hypotheses for evaluation. [R-C12; D05, D08]

**Ethics and participation.** Do not infer medical information from assist selection, require players to justify accommodations, or describe a result as lesser merely because it used an approved access route. When assistance affects a particular comparison, disclose the relevant gameplay behavior rather than a disability label. Monetized or earned vehicle differences require careful claims about what rankings measure; this entry does not approve a commercial model or assert a jurisdiction-specific legal rule. [R-C08; R-C11; R-C12]

**Localization.** Treat turn direction, route naming, timing vocabulary, units and warnings as part of the interaction. A spoken instruction can arrive too late after localization even when translated literally; the deadline must be tested in context rather than solved with an unsourced maximum word count. Do not assume right/left cues retain meaning across different camera reference frames. No multilingual driving experiment was inspected here. [R-C12]

**Production.** Every consequential configuration multiplies the behavior that needs explanation and verification. Limit the first prototype to the model relations and comparison fields needed for the decision. Budget for reset-state validation, assistance interactions, device configuration, replay/build compatibility, penalties, re-entry, and testing with actual relevant access routes. Deterministic replay, network fairness or specific engine behavior is not established by this packet. Prefer a small inspectable comparison over an elaborate inferred “skill score” with unknown inputs. [R-C08; R-C12]

## Research questions and proposed validation

**All tests below are proposed and not performed.** Participant numbers, meaningful differences and analysis methods require a local design and uncertainty estimate. No default count or universal improvement threshold is supplied. The relevant population includes the intended skill range, familiar and unfamiliar input users, and participants who use the access routes being evaluated; do not treat one student sample or device group as representative of all racers. [R-C14; D06]

| Question and comparison | Procedure and measures | Confounds, rejection or adaptation rule |
|---|---|---|
| Does the chosen cue preserve a useful trajectory decision? Compare a full route solution, a fact-preserving cue and the current accessible baseline. | Counterbalance familiarization; keep the model and route relation fixed. Measure prediction, action, course completion, assistance preference and enjoyment separately. | Reject the claimed decision-preserving mechanism if the cue simply supplies the answer or leaves the relation inaccessible. Do not infer a preference from time alone. |
| Do players understand the rule beyond one memorized line? | Use the discriminating linked-bend cases above and record predictions before action. Keep essential supports. | If competing incorrect strategies make the same prediction, redesign the probes. A changed physics model requires a separate orientation condition. |
| Does a comparison profile improve interpretation without exclusion? | Present matched, mismatched and genuinely unknown attempt pairs using the new pattern’s test. Ask what each pair supports. | Reject or simplify if labels do not improve interpretation, falsely imply skill, or unnecessarily block participation. Check misunderstanding and exclusion, not just label visibility. |
| Does solo practice address a shared-race goal? | Compare a specified maneuver in isolated and interactive contexts with controlled rival behavior where feasible. | Opponent interference and intentionally yielding confound raw time. No solo advantage licenses a claim about etiquette or social enjoyment. |
| Does the configured access route remain usable through recovery? | Include setup, attempted action, remap error, retry and return to play. Collect voluntary explanations, not medical labels. | Stop and repair inaccessible steps; do not classify non-completion as low skill or pressure someone to remove support. |

The strongest unresolved causal question is whether the proposed assistance distinctions and minimal comparison context improve understanding or agency enough to justify their complexity. An equally plausible alternative is that a small set of well-explained presets and an uncomplicated personal history achieves the goal with less burden. The packet’s author self-review preserves that opposing case. [R-C14]

## Coverage and remaining gaps

Route/trajectory, speed-control tradeoffs, assistance mechanisms, isolated/shared competition and progression **received bounded synthesis**. Current handling calibration, real-world driving transfer, racing-line optimality, opponent AI, network adjudication, weather/surface models, force feedback, motorcycles, rally communication, hardware-specific accessibility and longitudinal enjoyment did not receive adequate direct evidence. The inaccessible GT7 manuals, Chalmers thesis, Sophy paper and additional controller/track studies remain leads in the packet, not concealed support.

Broader reviewed dependencies for movement, simulation, economies, multiplayer, camera and localization are missing here. Their absence limits cross-domain integration, not permission to invent results. Next discriminating work should establish which player decisions and access routes a particular prototype preserves, rather than expand a generic realism checklist. Coverage remains open; independent content review has not occurred for G18.

## Claim ledger

Confidence concerns the stated claim, not the prestige of a source. “High, narrow” documentary confidence never means proven benefit. Design proposals below are not approved studio decisions.

| Claim | Precise claim and class | Support / locator | Confidence, applicability and unresolved question |
|---|---|---|---|
| R-C01 | Traversal-oriented scoring is a useful working boundary; vehicle imagery alone is insufficient. **inference** | G18 framing; documentary cases R-C08/R-C09; sports S-C07 supplies an adjacent negative case. | Moderate conceptual clarity, not validated market taxonomy. Parent approval and overlap review remain pending. |
| R-C02 | FM4 assist persistence is an observed behavior, not a direct mastery/enjoyment measure. **empirical-evidence** | GDR-SRC-20261010-G18-001, PDF pp. 3, 5, 7. | High for reported operationalization; low for generalizing reasons or causal effects. Historical player IDs and race entries, no random assist-removal treatment. |
| R-C03 | Natural-controller evidence does not establish a universal enjoyment advantage. **empirical-evidence** | GDR-SRC-20261010-G18-014, Study Two pp. 234–238. | Moderate within study; analysis dependence and narrow task/population limit transfer. See G18-CON-02. |
| R-C04 | Separate fidelity, operation, performance, access and enjoyment before choosing a control model. **inference** | R-C02/R-C03 and D03/D06. | Moderate diagnostic reasoning; no optimum configuration or causal efficacy demonstrated. |
| R-C05 | Distinguish informational assistance from action delegation and make retained decisions explicit. **hypothesis**; documented feature distinction is **practitioner-heuristic** | GDR-SRC-20261010-G18-005, Blind Driving Assists / One Touch Driving; D02/D04. | High that the account describes different intentions, low for proposed benefits or universal usability. See G18-CON-01. |
| R-C06 | Route information, movement rules and action commitments define different candidate racing demands. **inference** | Explicit G18 design model; D03/D04. | Moderate as analysis of a declared model; not a physics law, reaction threshold or empirical preference finding. |
| R-C07 | Shared-race decisions cannot be inferred solely from an isolated time-trial result. **inference** | Difference in the defined tasks; D06. | High logical limitation; low confidence about any particular training-transfer effect. |
| R-C08 | Relevant version/configuration context is needed for a specific performance interpretation. **inference**; historical version change is **observed-example** | GDR-SRC-20261010-G18-004, Other Improvements §§2,4; D06; PAT-01. | High for the documented change and logical confounding risk; low for proposed UI/policy benefits. See G18-CON-03/04. |
| R-C09 | Official MK8 Deluxe documentation includes steering support and time trials. **observed-example** | GDR-SRC-20261010-G18-006, named product-page sections. | High for inspected description; build and causal effects unknown. |
| R-C10 | A bounded disclosed adaptive mode is an alternative to hidden opposition changes, not an automatic requirement. **hypothesis** | D10, recipe/invariants/exit conditions; G18 adaptation. | Low for racing-specific benefit; no opponent-policy experiment inspected. |
| R-C11 | Separate equipment progression from inference about control mastery. **inference** | Different variables in the proposed task; D06; missing progression/economy reference disclosed. | Moderate logical scope; low for progression/retention effects. |
| R-C12 | Preserve access, uncertainty and corrected transfer/numerical scope in racing adaptations. **inference** | D01–D10, exact selected locators in packet. | Moderate for conditional application; reviewed dependencies are unreleased and their external evidence was not automatically reverified. |
| R-C13 | The worked examples could discriminate specific model predictions without mandatory assist withdrawal. **hypothesis** | Illustrative designs plus corrected D07 recipe. | Low until actual model validation and participant testing. No experiment performed. |
| R-C14 | Proposed tests can challenge the entry’s strongest claims when locally operationalized. **hypothesis** | D06 and declared comparisons/confounds above. | Low for eventual results; no power, effect size or acceptance outcome established. |

## Review and history

Version `0.1.0`; candidate revision `initial-author-draft-1`; predecessor and supersession: null. Run date remains 2026-10-10; research access date is 2026-10-11 UTC. This is the first G18 output generated in this execution, not a revision or resubmission of a previously completed batch. Exact bytes are identified by the external integrity receipt, avoiding a self-referential hash.

Author self-review is recorded in the packet; it is **not independent review**. Gate C remains pending independent source/content review; Gate D is limited to recorded local packaging checks, with host retrieval unperformed; Gate E/release is not approved. Next decision: review the definition boundary, evidence-to-assistance bridge and minimal-comparison pattern before accepting any guidance or commissioning registered child work.

## References

All access dates are **2026-10-11 UTC**. Source IDs are temporary run-scoped identities. Cross-batch canonical URL/DOI/edition deduplication is pending. Public material is paraphrased; no source article, image or screenshot is redistributed. Unless an explicit license is established, rights are treated as reserved; public access is not a redistribution license. “Documentary observed example” means the named official artifact was inspected by the G18 author, not that a game was played.

### GDR-SRC-20261010-G18-001

Thomas Debeauvais, Thomas Zimmermann, Nachiappan Nagappan, Kevin Carter, Ryan Cooper, Dan Greenawalt and Tyson Solberg. *Off With Their Assists: An Empirical Study of Driving Skill in Forza Motorsport 4*. Foundations of Digital Games; original paper hosted by Microsoft Research. Publication/update: 2014. [Inspected route or disclosed lead](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/debeauvais-fdg-2014.pdf).

Edition/build: Eight-page conference paper; Forza Motorsport 4, Xbox 360; gameplay patch unknown. Access: `full`. Type: Original empirical paper; observational telemetry. Locator: PDF p. 3, Data and sampling footnote; p. 5, Assist transitions; p. 7, Discussion. Claims in this artifact: R-C02. Limits/provenance: Outcome labels operationalize assist-setting persistence, not directly measured enjoyment or independent mastery. Device/view and steering-assist telemetry are absent. Developer-affiliated authors; not independent of the Forza production context in 005. PDF p. 3 visually inspected; failed later-page screenshots are not used for graph-derived numerical claims.

### GDR-SRC-20261010-G18-004

Polyphony Digital / Sony Interactive Entertainment. *Update Notice (1.68)*. Gran Turismo official site. Publication/update: 2026-03-12. [Inspected route or disclosed lead](https://www.gran-turismo.com/us/gt7/news/00_8497133.html).

Edition/build: Gran Turismo 7 update 1.68; historical release note, not a latest-build certification. Access: `relevant-excerpt`. Type: Official release note; documentary observed example. Locator: Other Improvements and Adjustments, 2. World Circuits and 4. Power Pack. Claims in this artifact: R-C08. Limits/provenance: Documentation establishes a stated version change, not measured competitive equality, current compatibility, or player benefit. Same production family as leads 002 and 003.

### GDR-SRC-20261010-G18-005

Turn 10 Studios / Xbox Wire. *From Blind Driving Assists to One Touch Driving, Meet The Most Accessible Forza Motorsport Ever*. Xbox Wire. Publication/update: 2023-04-27. [Inspected route or disclosed lead](https://news.xbox.com/en-us/2023/04/27/forza-motorsport-accessibility-features-blind-driving/).

Edition/build: Pre-release announcement for Forza Motorsport (2023); shipped patch not verified. Access: `relevant-excerpt`. Type: Firsthand developer account and feature documentation. Locator: Blind Driving Assists; One Touch Driving; Screen Narration. Claims in this artifact: R-C05. Limits/provenance: Reported design intent and development involvement are not independent accessibility or efficacy trials. The headline is promotional and is not adopted as a finding. Developer ecosystem overlaps 001; mirrored announcements are not additional evidence.

### GDR-SRC-20261010-G18-006

Nintendo. *Mario Kart 8 Deluxe*. Nintendo UK. Publication/update: unknown; product page inspected 2026-10-11. [Inspected route or disclosed lead](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-games/Mario-Kart-8-Deluxe-1173281.html).

Edition/build: Nintendo Switch product page; game patch unknown. Access: `relevant-excerpt`. Type: Official product documentation; documentary observed example. Locator: Perfect for beginners; Compete to beat your best. Claims in this artifact: R-C09. Limits/provenance: Smart Steering and time-trial descriptions inspected, not usability or skill effects. Promotional beginner claims do not describe every audience. Nintendo sources 006 and 011 are organizationally related.

### GDR-SRC-20261010-G18-014

Paul Skalski, Ron Tamborini, Ashleigh Shelton, Michael Buncher and Pete Lindmark. *Mapping the road to fun: Natural video game controllers, presence, and game enjoyment*. New Media & Society 13(2), 224–242, SAGE. Publication/update: 2011 issue; OnlineFirst 2010-10-12. [Inspected route or disclosed lead](https://www.researchgate.net/publication/258173311_Mapping_the_road_to_fun_Natural_video_game_controllers_presence_and_game_enjoyment). DOI: `10.1177/1461444810370949`.

Edition/build: Original article text; coauthor Ashleigh Shelton upload dated 2015-08-29. Access: `relevant-excerpt`. Type: Original empirical article; coauthor-uploaded full-text route. Locator: Study One methods/results, pp. 230–234; Study Two methods/results, pp. 234–238. Claims in this artifact: R-C03. Limits/provenance: Original article body inspected, not later ResearchGate recommendations or citing-paper excerpts. Short student sessions; control/platform/posture differences and model-dependent enjoyment results constrain transfer. Publisher/CiteSeerX PDF routes did not yield inspected PDF bytes. Independent of the game-publisher announcements here.
