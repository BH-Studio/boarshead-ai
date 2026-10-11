---
id: GDR-CAND-20261010-F02-TOP-02
kind: topic
title: Challenge and difficulty
version: 0.1.0
status: draft
candidate_revision: independent-review-correction-1
attempt_identity: F02-local-attempt-01
predecessor_sha256: c4cdce1b33661195b9c732b46209729f5db99418a369f1a5af18c429308654e4
supersedes: initial-capture-1 (same candidate or packet; local corrected copy only)
change_summary: Correct source 008 performance-result locator; conclusions and confidence unchanged.
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_key: F02
updated: '2026-10-11'
evidence_checked: '2026-10-10'
aliases:
- difficulty adjustment
- failure and recovery
- assistance
- adaptive difficulty
- fair challenge
tags:
- challenge
- difficulty
- skill-demands
- failure
- recovery
- accessibility
related_topics:
- GDR-CAND-20261010-F02-TOP-01
related_patterns:
- GDR-CAND-20261010-F02-PAT-02
- GDR-CAND-20261010-G01-PAT-01
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F02-006
- GDR-SRC-20261010-F02-007
- GDR-SRC-20261010-F02-008
- GDR-SRC-20261010-F02-009
- GDR-SRC-20261010-F02-011
- GDR-SRC-20261010-F02-012
reviewer: null
approved_by: null
approved_date: null
---

# Challenge and difficulty

**Draft research candidate, not released guidance.** Version 0.1.0; revision independent-review-correction-1. This entry does not prescribe a universal success rate, flow curve, retry count, difficulty scale, assist preset or penalty. Proposed interventions require independent review and local validation before adoption.

## Decision and scope

This entry helps decide **which demand should challenge the player, which barrier should be removed, how failure changes the next attempt, and who controls adjustment**. It covers skill demands, difficulty adjustment, failure, recovery, fairness, frustration and assistance. It does not replace detailed learning research, encounter/spatial composition, multiplayer ranking policy, presentation accessibility or evaluation methodology.

Use these operational distinctions. **Challenge** is the demand being engaged with; **difficulty** is the relationship between that demand and a player’s current capability, knowledge, circumstances and goal. **Failure** is an unmet task condition; its **consequence** is the resulting change in resources, progress, state or opportunity. **Recovery** is the route back to a viable state, not just reloading a location. **Assistance** changes a demand, its communication, or the consequences of not meeting it. These are analytical conventions, not formal standards or a complete theory of experience. [C-01]

Do not infer a global skill deficit from one missed action. An observed failure may concern rule knowledge, state perception, motor execution, attention, resource availability, technical behavior, intentional experimentation or a different player goal. The diagnostic process proposed below treats these as competing explanations. [C-08]

## Core explanation and mechanisms

### Difficulty is a profile, not a single number

Record the intended and incidental demands separately. A general “easy” switch may change many of them, making it hard to determine what helped or what valued activity was removed. The following decomposition is an inference motivated by discrete-mechanic guidance and documented configurable games, not a validated universal dimension set. [C-01; GDR-SRC-20261010-F02-009; GDR-SRC-20261010-F02-011]

| Demand | Diagnostic question | Candidate response and its boundary |
|---|---|---|
| Perception and state tracking | Was required information available through the player’s usable modalities? | Improve accessible communication; this need not simplify the underlying strategy. |
| Rule understanding | Could the player predict what the action would do? | Explain or demonstrate the relation; do not infer learning from a repeated answer. |
| Planning and prioritization | Were competing goals and consequences understood? | Preserve the meaningful tradeoff; offer planning aids rather than silently choose for the player. |
| Timing and motor execution | Did the player know the action but fail to execute it under its timing/input demands? | Adjust the specific demand or offer another input route; additional health may not solve the barrier. |
| Sustained attention and memory | Is the activity taxing tracking or endurance beyond the intended goal? | Permit pause, review, reminders or shorter continuous demands where compatible. |
| Resources and accumulated state | Is the next attempt feasible with the resources that remain? | Repair a recovery trap or disclose the chosen persistent-cost contract. |
| Social coordination | Is difficulty produced by coordination, unequal information or another player’s behavior? | Clarify shared rules and consent; individual hidden adjustments may affect everyone. |

Accessibility is not synonymous with reduced strategic difficulty, and difficulty settings do not by themselves establish accessibility. A player may want a demanding decision without a rapid input requirement, or want narrative access without the central performance test. Determine the requested activity instead of treating either goal as deficient. [C-08, C-12]

### Outcome uncertainty can be attractive without severe punishment

Abuhamdeh and colleagues studied short manipulated Wii contests in two university samples. In Study 2, 33 of 48 participants chose to replay the game they had won narrowly rather than the one won widely. Concern about performance also mattered. These results concern outcome closeness and suspense, not hidden rules, arbitrary penalties or permanent losses; the study does not establish a cultural comparison between its campus populations. [C-02; GDR-SRC-20261010-F02-006]

The conditional bridge is to test **credible outcome uncertainty within an intelligible activity**, when suspense is desired. Increasing execution noise or making the consequences crueler is a different intervention. A player seeking practice, recovery, expression or calm may not value the same uncertainty in the same session. That remains a goal-dependent hypothesis, not a claim that either preference is universal. [C-14]

### Failure and recovery are different tuning decisions

Juul’s preliminary prototype comparison involved nine players and did not indicate the expected preference for energy punishment. A later online sample of 85 played one version; the association between performance groups and ratings was reported at p = .06. These exploratory findings do not establish an optimal failure frequency or prove that inducing failure improves enjoyment. [C-03; GDR-SRC-20261010-F02-007]

Use the distinction, not the chapter’s strongest generalizations: a failed maneuver, a lost resource, a forced replay and a lost campaign are different consequences. Before increasing a penalty, identify what new information or commitment it contributes. A longer return journey may add decisions, but it may also repeat already-solved activity. A failure loop without a viable next attempt cannot be repaired merely by telling the player to improve. These are design hypotheses to test. [C-09]

A useful proposed recovery audit records what persists, what is restored, what the player learned, what must be repeated and what can still be changed. It should also examine whether a checkpoint stores a depleted or trapped state, whether an assist can be reached from that state, and whether the player can leave without forfeiting unrelated progress. Recovery must respect the declared mode’s stakes; an optional persistent-consequence mode can be intentional without becoming the default for every audience. [C-09, C-15]

### Difficulty adaptation affects more than performance

In Denisova and Cairns’ second experiment, 60 participants played short sessions under actual and described adaptation conditions. The manuscript reports main effects on immersion for both, without a significant interaction; its performance analysis did not show the corresponding significant effect. The experiments separate some expectation and system effects but do not establish lasting accessibility, learning or trust benefits. [C-04; GDR-SRC-20261010-F02-008]

This makes a purely mechanical evaluation insufficient. A player’s understanding of adjustment is part of the experience. It does **not** justify deceiving players because a laboratory manipulation used deceptive expectations. The proposed design alternative is bounded, truthful, controllable adjustment, compared with manual settings and a fixed condition. Its superiority has not been demonstrated by the inspected studies. [C-11]

The control problem also contains uncertainty: a poor result may reflect experimentation, distraction, depleted resources or deliberate manipulation rather than a need for easier execution. A controller that reacts to every failure can oscillate or remove evidence of improvement. “Hold the setting and ask” is a legitimate outcome when diagnosis is uncertain. These are inferred failure modes, not results from a deployed controller. [C-08, C-11]

## Design choices and alternatives

Microsoft’s XAG 108 recommends adjustable difficulty and discrete mechanics, descriptive non-denigrating labels and relevant pause/save affordances. Treat that as vendor accessibility guidance, not a formal standard or proof that any number of presets serves every player. Its numeric suggestions are not imported as library defaults. [C-05; GDR-SRC-20261010-F02-009]

| Approach | Conditional purpose | Costs and reasons to prefer an alternative |
|---|---|---|
| Fixed authored demands | Preserve a stable comparison, deliberate pacing or a self-selected challenge. | A single profile can exclude some desired participants. Alternative routes or settings may preserve the activity better than a global reduction. |
| Described presets | Offer a low-effort starting point with understandable effects. | Bundled changes may affect an unwanted dimension. Permit appropriate local overrides and identify incompatible combinations. |
| Granular assistance | Address a specific barrier while retaining other demands. | More settings require discovery, explanation and compatibility testing. A small set of well-motivated options may be preferable to exposing every variable. |
| Player-controlled adjustment during play | Let the player respond to goals or circumstances the system cannot infer. | Changes need understandable scope, persistence and shared-play effects. Do not silently discard progress or transform a ranked contract. |
| Automatic bounded adjustment | Respond to a validated signal without repeated menu work. | Misdiagnosis, oscillation, strategic manipulation and attribution ambiguity. Compare against a simpler manual control. |
| Optional route, skip or consequence change | Preserve access to desired content when the performance task is not desired or attainable. | It may change the activity or shared meaning. Describe that difference truthfully instead of claiming identical experience. |
| Practice with reduced setback | Enable repeated engagement with a target skill or decision. | May teach risk policies inappropriate to a higher-stakes mode. Label scope and re-entry expectations; do not withdraw accommodations on success. |

The alternatives and comparison criteria are inferences [C-08–C-12, C-15]. Reducing damage is not a guaranteed solution to an unreadable warning; a slow-motion option is not equivalent to explaining an unknown rule; a bypass is not the same as mastering the omitted task.

### Fairness and frustration

Treat **fairness** as a set of questions: are rules and exceptions intelligible; can intended participants act through usable means; are outcomes comparable under the declared shared rules; and does the system honor what it told the player? These goals can conflict. Symmetric parameters may still demand unequal effort; asymmetric private help may undermine a ranked comparison. State the applicable criterion and affected parties rather than asserting fairness from one metric. [C-10]

Likewise distinguish temporary frustration during a valued challenge from confusion, loss of trust, fatigue or an unwanted barrier. A repeated attempt can mean engagement, obligation, lack of an exit or a measurement artifact. Ask what the player wanted, whether another attempt remains voluntary, and what would make the activity worth continuing. Do not optimize retries or time spent as a substitute for the approved experience goal. [C-08–C-10]

## Application process

1. **Specify the intended demand and outcome.** Describe what the player should decide, perceive or execute, and what is not the point of the activity. Record whether the goal is mastery, suspense, access, competition or another locally approved aim.
2. **Diagnose before tuning.** Compare observable action, rule prediction and the player’s account. Separate an inaccessible signal, misunderstood rule, execution miss, resource trap and intentionally risky choice. Collect only data needed for that question.
3. **Choose a minimal lever.** Test a clearer signal, focused assistance, consequence change or manual option before assuming automatic adaptation is needed. Preserve unaffected demands explicitly.
4. **Define the contract.** Record what changes, when it applies, whether it persists, how it can be overridden and who else is affected. Define attainable recovery states and any intentionally persistent costs.
5. **Specify a bounded comparison.** Hold encounter logic and communication constant unless they are the chosen intervention. Define success, trust, burden and access measures separately. Source experiments’ durations are not default test settings.
6. **Audit transitions and exploits.** Include save/load, restart, changing an option mid-state, depleted resources, intentional underperformance and conflicting settings. Escalate spatial or narrative effects to the owning domain; do not assume an uninspected encounter design.
7. **Evaluate and choose.** Retain an intervention only for the goal and population the evidence supports. Stop or offer a manual alternative when the diagnosis is unreliable, the experience contract is violated or the production burden is unjustified.

This process is a testable design proposal [C-08–C-13], not performed implementation work.

## Patterns and genre adaptations

[Bounded disclosed difficulty adaptation](../patterns/bounded-disclosed-difficulty-adaptation.md), `GDR-CAND-20261010-F02-PAT-02`, applies only after a specific adjustment signal and player contract can be justified. [Decision design](decision-design.md) owns uncertainty and commitment; the two topics must not conflate “hard to execute” with “hard to choose.”

The inspected first-wave `GDR-CAND-20261010-G01-PAT-01`, **Configurable threat consequences**, already covers retaining an activity while changing threat consequences in its defined context. F02 does not duplicate that pattern or universalize its horror-specific rationale. `GDR-CAND-20261010-F01-PAT-01` supplies corrected learning-check cautions. Relevant P01 scope corrections were inspected; no numerical accessibility defaults are imported. See the [dependency register](../reviews/full-run-20261010-f02-review-packet.md#dependency-register).

No genre file is produced in F02. Competitive comparison, restorative activity and deliberate permanent-stakes play impose different constraints; hybrid designs must name the conflict and the player-selectable or shared contract. A mode promising calm cannot automatically inherit a recommendation to maximize suspense. [C-10, C-14, C-15]

## Examples and counterexamples

### Documented example: independently described difficulty dimensions

Naughty Dog’s 2020 launch-era documentation lists separate Player, Enemies, Allies, Stealth and Resources difficulty categories alongside accessibility settings. This establishes that the documented design exposes several dimensions, not that those dimensions are technically independent in every state or equally beneficial to all players. The source is an inspected developer document, not a game build played in F02. [C-06; GDR-SRC-20261010-F02-011]

### Documented example: death-conditioned assistance

Supergiant’s Hades FAQ describes God Mode as increasing damage resilience, with further resilience after deaths. This is a concrete documented adaptation mechanism; the inspected passage supplies no tuning increment or cap. It does not validate F02’s proposed controller or prove that everyone experiences assisted success the same way. [C-07; GDR-SRC-20261010-F02-012]

### Illustrative diagnosis: one obstacle, different causes

An invented task asks a player to allocate defenses and then respond to a warning. One participant predicts the needed action correctly but cannot complete the timed input; another executes reliably but predicts the rule incorrectly; a third deliberately accepts damage to preserve a resource. Uniformly reducing enemy health confounds three different problems. Test an input/time adjustment for the first, a rule explanation for the second, and no intervention until the third’s goal is understood. These are proposed diagnostic branches, not participant findings. [C-08]

### Illustrative recovery trap

A checkpoint preserves a required item’s absence after a failed attempt, but the only route to obtain the item lies before the checkpoint. Restoring health alone cannot make the next attempt viable. Possible repairs include restoring the prerequisite, permitting a legitimate alternate route, or allowing an explicitly scoped earlier-state recovery. The correct choice depends on the designed persistence contract and narrative/spatial dependencies. No actual checkpoint was inspected or modified. [C-09]

### Strongest counterexamples

A self-selected fixed-rules challenge may lose its central attraction if success triggers hidden opposition increases. An accessible activity may offer no failure state and still sustain valued expression. Conversely, a player may deliberately prefer severe persistent consequences and informed uncertainty. These examples challenge automatic “easier is better” and “harder is meaningful” rules; they do not establish which audience is largest. [C-10, C-14, C-15]

## Failure modes and constraints

**Misdiagnosis and incentives.** An adaptation reward can encourage deliberate failure; a successful player may feel punished if the controller immediately increases demands. A threshold based on completion alone can misread fast bypassing as mastery. Keep an uncertainty state, evaluate likely strategic manipulation and separate access settings from performance-contingent adjustments. [C-08, C-11]

**Access and localization.** Do not turn success into a reason to disable narration, remapping, readable information or another accommodation. Explain settings by their actual effects, using language that survives translation and does not rank people’s worth. Check whether an adjustment alters subtitle reading time, cue availability or menu reachability; those are presentation dependencies, not validated outcomes of F02. [C-05, C-12]

**Technical and production costs.** Interacting settings expand the state space. A damage adjustment can change resource use and pacing; slowing action can affect animation, input, timing-based events or multiplayer synchronization. These are plausible dependencies to audit, not engine-specific findings. A manual option with a documented compatibility limit may be more maintainable than an unvalidated personalized controller. [C-11, C-12]

**Fairness and ethics.** Obtain a legitimate shared-play policy before changing one participant’s demands in ways that affect others. Do not infer disability, psychological vulnerability or consent from telemetry. Do not use difficulty pressure to coerce spending or continued play. These are proposed safeguards and ethical inferences, not claims of legal compliance or approved studio policy. [C-10–C-12]

## Playtest and validation

**PROPOSED — NOT PERFORMED.** No game build, controller, recruitment, prototype, telemetry collection or player trial was run. Select participants for the intended task, experience range, language and relevant access needs. Set sample design and acceptable tradeoffs before data collection; no universal statistical threshold is prescribed here. [C-13]

**Test A: demand diagnosis.** Compare the baseline with one targeted assistance change and one broad difficulty change. Obtain a rule prediction separately from action preference, then observe execution. Maintain each participant’s needed accommodations in every condition. Measure target-demand errors, unwanted assistance, preserved strategic choices, comfort and perceived control. Reject the targeted explanation when it does not address the observed failure, or revise when it removes a valued decision rather than an incidental barrier.

**Test B: adaptation and expectations.** Compare fixed settings, player-adjustable settings and truthful bounded automatic adjustment. Do not deceive participants to reproduce a published expectation manipulation. Record the actual settings and their timing, explanations understood, performance, immersion, trust and voluntary preference. A matched or recorded setting schedule can help separate the controller from the mere amount of assistance, but such schedules may create mismatch for different players; report that limitation rather than claim a perfectly isolated mechanism.

**Test C: failure and recovery.** Hold the task and feedback constant while varying a specified setback cost. Measure what changes in the next attempt, repeated solved activity, resource viability, strategy variety, frustration, sense of commitment and willingness to stop. Include deliberate high-stakes preferences rather than averaging them away. Reject a harsher consequence when its purported benefit is unsupported and it creates the identified harm; reject automatic recovery when it defeats the explicitly selected experience.

**Interpretation safeguards.** Immediate completion is not learning; longer play is not consent; equal average success is not fairness; nonsignificance is not equivalence. Follow-up tasks must change the correct prediction where appropriate and preserve accessibility. Where adaptation continually changes demands, an independent fixed reference task may help assess learning, but its relevance and access fit also require validation. [C-13]

## Claim ledger

| ID | Precise claim and class | Support / contrary evidence and locator | Applicability, confidence and unresolved question |
|---|---|---|---|
| C-01 | A difficulty profile distinguishes demand types, player circumstances and consequences. `inference` | Analytical decomposition; motivated by GDR-SRC-20261010-F02-009 and -011. | Moderate: useful model, not exhaustive or standardized. Which dimensions are locally separable? |
| C-02 | Narrow-win replay preference occurred in the inspected short Wii study. `empirical-evidence` | GDR-SRC-20261010-F02-006, Study 2 Method/Results; Study 1 and discussion supply context. | Moderate within those tasks; does not support arbitrary opacity, permanent punishment or cultural rankings. |
| C-03 | The inspected failure studies do not establish a causal optimum for failure frequency. `empirical-evidence` | GDR-SRC-20261010-F02-007, Offline/Online tests, rating versus performance and appendices. | Moderate for the methodological limit; exploratory evidence is not proof of no effect. |
| C-04 | Actual and described adaptation affected reported immersion in Study 2 without corresponding significant performance evidence. `empirical-evidence` | GDR-SRC-20261010-F02-008, §7.2/Table 3, §7.2.1 (performance), §§7.3 and 8 (discussion). | Moderate: brief controlled context, reporting discrepancies; long-term trust and access untested. |
| C-05 | XAG 108 recommends adjustable/discrete difficulty and descriptive labels. `practitioner-heuristic` | GDR-SRC-20261010-F02-009, Implementation guidelines. | High for attribution, not a universal effect or formal standard. |
| C-06 | The launch-era TLOU Part II document describes several configurable difficulty dimensions. `observed-example` | GDR-SRC-20261010-F02-011, Game Difficulty; document inspected 2026-10-10 by F02 author. | High for document content; no game behavior reproduced or causal efficacy demonstrated. |
| C-07 | Hades FAQ describes death-conditioned resilience through God Mode. `observed-example` | GDR-SRC-20261010-F02-012, difficulty question; document inspected 2026-10-10 by F02 author. | High for attribution; build and numerical tuning unspecified. |
| C-08 | Diagnose perception, knowledge, execution, resources and intent before selecting assistance. `inference` | Bridge from C-01/C-05/C-06; corrected F01 assessment distinction. | Moderate rationale; diagnostic reliability unvalidated. |
| C-09 | Separate failure feedback from setback cost and audit whether recovery states remain viable. `hypothesis` | Source 007 provides distinction; state-feasibility reasoning supplies proposed process. | Moderate rationale; no preferred penalty schedule empirically established. |
| C-10 | Fairness requires an explicit criterion and affected-party contract, not just equal settings or success. `inference` | Analytical conflict between comparison, access and truthful adjustment; C-04/C-05 motivate questions. | Moderate conceptual basis; audience and shared-play legitimacy need separate evidence. |
| C-11 | Bounded disclosed adaptation may preserve control while addressing a diagnosed demand. `hypothesis` | Bridge from GDR-SRC-20261010-F02-008, -009 and -012; full recipe untested. | Low for comparative benefit; manual adjustment may be superior. |
| C-12 | Accommodation persistence, understandable labels and compatibility audits constrain difficulty changes. `inference` | Source 009; inspected P01 scope corrections; model-based dependency analysis. | Moderate: no representative access or engine verification performed. |
| C-13 | Separate performance, learning, preference, trust and fairness measures in proposed comparisons. `hypothesis` | Source 008 separates outcomes; corrected F01 probe discipline; author-designed tests. | Low until executed; carryover, sample coverage and demand effects remain. |
| C-14 | Greater uncertainty or harsher failure is neither a necessary nor sufficient universal recipe for the desired experience. `inference` | Limits of C-02/C-03 and explicit goal-dependent counterexamples. | High for refusing a universal rule; local causal effects remain uncertain. |
| C-15 | Persistent stakes or bypasses can be legitimate conditional alternatives when their consequences and scope are explicit. `hypothesis` | Contrasting goals and consequence models; sources 007/009 motivate alternatives, not universal equivalence. | Low for specific experience outcomes; requires local consent, scope and tests. |

## References

Access date for every record below: **2026-10-10**. These are temporary source candidates. A repeated record is the same evidence, not additional corroboration. “Relevant-excerpt” identifies inspected substantive passages, not merely an abstract and not every linked supplement.

### GDR-SRC-20261010-F02-006

**Sami Abuhamdeh, Mihaly Csikszentmihalyi, and Baland Jalal.** [Enjoying the possibility of defeat: Outcome uncertainty, suspense, and intrinsic motivation](https://www.researchgate.net/publication/266145593_Enjoying_the_possibility_of_defeat_Outcome_uncertainty_suspense_and_intrinsic_motivation). Motivation and Emotion 39, pp. 1–10. **Publication/update:** 2014-09-03 online; 2015 issue. **Edition/version:** 2015 journal paper; author-deposited full-text route.

**DOI:** [10.1007/s11031-014-9425-2](https://doi.org/10.1007/s11031-014-9425-2).

**Access:** relevant-excerpt. **Source type:** original empirical studies. **Inspected locators:** Study 1: Method and Results; Study 2: Participants, Procedure, Results and discussion; General discussion. **Supports local claims:** C-02, C-14

**Limits:** Short manipulated Wii contests in two university samples; outcome closeness also changes challenge. Mediation is not an isolated causal test of suspense; culture was not independently manipulated. **Independence:** Publisher abstract and author-deposited article identify the same work. Recommended articles appended by the host are not part of this evidence. **Rights:** Springer copyright; author-deposited copy paraphrased, not redistributed

### GDR-SRC-20261010-F02-007

**Jesper Juul.** [Fear of Failing? The Many Meanings of Difficulty in Video Games](https://jesperjuul.net/text/fearoffailing/). In Mark J. P. Wolf and Bernard Perron (eds.), The Video Game Theory Reader 2, Routledge, pp. 237–252. **Publication/update:** 2009. **Edition/version:** Author-hosted HTML of 2009 chapter.

**Access:** relevant-excerpt. **Source type:** original exploratory prototype studies and author interpretation. **Inspected locators:** Failure and Punishment; First Test, Offline; Second Test, Online; Game rating vs. performance; Conclusions; Appendices 1–2. **Supports local claims:** C-03, C-09, C-14, C-15

**Limits:** Small preliminary comparison; later performance/rating and attribution associations are not randomized causal effects. The chapter’s stronger generalizations exceed this packet’s interpretation. **Independence:** Firsthand report with Gamelab; cited external production accounts and prior studies were not separately inspected. No independent replication supplied. **Rights:** Routledge/author rights; paraphrase only; no participant quotations or figures redistributed

### GDR-SRC-20261010-F02-008

**Alena Denisova and Paul Cairns.** [Player Experience and Deceptive Expectations of Difficulty Adaptation in Digital Games](https://eprints.whiterose.ac.uk/139704/1/1_s2.0_S1875952118300521_main.pdf). Entertainment Computing 29, pp. 56–68, Elsevier. **Publication/update:** 2018-12 accepted; 2019 journal issue. **Edition/version:** Accepted manuscript with repository cover; not a new 2026 edition.

**DOI:** [10.1016/j.entcom.2018.12.001](https://doi.org/10.1016/j.entcom.2018.12.001).

**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.2.1 performance, manuscript pp. 26–27 (PDF pages 29–30); §§7.3 and 8 discussion. **Supports local claims:** C-04, C-10, C-11, C-13

**Limits:** Brief lab sessions; immersion, performance, competence, accessibility and trust are distinct outcomes. Minor prose/table numeric discrepancies; exact disputed statistics are not propagated. **Independence:** White Rose PDF, City repository metadata and publisher DOI are one work. Expectation manipulation does not authorize deceptive product behavior. **Rights:** Accepted manuscript CC BY-NC-ND 4.0, as repository metadata states; paraphrase only, no altered manuscript distributed

### GDR-SRC-20261010-F02-009

**Microsoft.** [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108). Microsoft Learn. **Publication/update:** 2026-03-04 last updated; original date unknown. **Edition/version:** Live unnumbered guideline page inspected 2026-10-10.

**Access:** relevant-excerpt. **Source type:** official vendor accessibility guidance. **Inspected locators:** Overview; Scoping questions; Implementation guidelines: difficulty adjustment, discrete mechanics, descriptive labels and pausing. **Supports local claims:** C-01, C-05, C-08, C-10, C-12, C-15

**Limits:** Practitioner guidance, not a formal standard, universal tuning prescription, or measured assurance of accessibility. Embedded game demonstrations not reproduced. **Independence:** Same issuer/suite as source 010, not independent empirical corroboration. Linked external resources remain separate, uninspected leads. **Rights:** Reuse terms not separately inspected; paraphrase only; no embedded media copied

### GDR-SRC-20261010-F02-011

**Matthew Dunnerstick / Naughty Dog.** [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed). Naughty Dog. **Publication/update:** 2020-06-09. **Edition/version:** Historical launch-era PS4 documentation; no current build reproduced.

**Access:** relevant-excerpt. **Source type:** first-party design documentation; documentary observed example. **Inspected locators:** Accessibility Presets; Combat Accessibility; Game Difficulty and its Player, Enemies, Allies, Stealth and Resources settings. **Supports local claims:** C-01, C-06, C-08

**Limits:** Documents options and creator descriptions, not measured effects. Observer: F02 author, 2026-10-10, page inspection; no game session or current-platform verification. **Independence:** One developer account; examples on third-party guideline pages would be derivative, not independent outcome evidence. **Rights:** Naughty Dog copyright; no game assets or screenshots redistributed

### GDR-SRC-20261010-F02-012

**Supergiant Games.** [Hades FAQ](https://www.supergiantgames.com/blog/hades-faq/). Supergiant Games. **Publication/update:** 2018-12-07 published; 2025-07-16 updated. **Edition/version:** FAQ revision as inspected; game build number unspecified.

**Access:** relevant-excerpt. **Source type:** first-party game documentation; documentary observed example. **Inspected locators:** Question beginning “Some rogue-likes are brutally difficult…” and its God Mode / challenge-modifier answer. **Supports local claims:** C-07, C-11

**Limits:** Documents death-conditioned resilience; does not supply numerical increment/cap in the used passage or prove long-term experience effects. Observer: F02 author, 2026-10-10, document only. **Independence:** Independent studio from source 011, but another documented example rather than a controlled comparison. **Rights:** Supergiant Games copyright; paraphrase only

## Open questions and change history

All seven assigned subtopics receive a substantive first-pass treatment. Important gaps remain in long-term adaptation, severe persistent failure, shared competitive fairness, representative accessibility and cultural/linguistic variation. The focused dependency on **Worlds encounter/scenario composition evidence is missing**, not supplied by the retrieved first-wave narrative/spatial files. Public-source research here does not certify heading completeness.

2026-10-10 — Initial F02 candidate, version 0.1.0, revision initial-capture-1, no predecessor asserted. Author self-review is recorded in the [review packet](../reviews/full-run-20261010-f02-review-packet.md). Independent F02 review, actual host retrieval tests and release remain pending. No first-wave artifact is resubmitted and no implementation or Project-source change follows from this draft.


**2026-10-11 — independent-review-correction-1, still 0.1.0 draft:** Separate model source spot-check corrected source 008 performance-result locators from §7.3 to §7.2.1, manuscript pp. 26–27 (PDF pages 29–30). §7.3 remains discussion. The substantive empirical conclusion and confidence are unchanged. Original initial-capture history above is preserved; no participant, prototype or host tests were performed and no human approval or release occurred. See the separate correction receipt and independent review for current disposition.
