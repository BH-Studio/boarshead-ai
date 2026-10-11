---
id: GDR-CAND-20261010-G02-GEN-02
kind: genre
title: Precision platformer
version: 0.1.0
status: draft
candidate_revision: initial-1
run_id: GDR-FULL-20261010
batch_id: G02
attempt_id: G02-authoring-attempt-01
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus supplied G02 dispatch
aliases:
- precision platform game
- execution-focused platformer
- technical platforming
tags:
- repeatable-execution
- practice
- retry
- checkpoints
- assists
- transfer
- frustration
related_topics: []
related_patterns:
- GDR-CAND-20261010-G02-PAT-01
- GDR-CAND-20261010-G02-PAT-02
related_genres:
- GDR-CAND-20261010-G02-GEN-01
- GDR-CAND-20261010-G02-GEN-03
source_ids:
- GDR-SRC-20261010-G02-001
- GDR-SRC-20261010-G02-004
- GDR-SRC-20261010-G02-005
- GDR-SRC-20261010-G02-006
- GDR-SRC-20261010-G02-007
- GDR-SRC-20261010-G02-008
- GDR-SRC-20261010-G02-016
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
predecessor_sha256: null
supersedes: null
superseded_by: null
change_summary: Initial G02 candidate; no predecessor submitted
hash_record: ../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity
---

# Precision platformer

> **Draft research candidate, not released guidance.** Version 0.1.0; candidate revision `initial-1`; independent review not performed. Definitions and proposed adaptations below are bounded inferences or hypotheses, not an approved studio design. No game build, gameplay recording, prototype or player test was run in this batch.

The supplied G02 dispatch authorizes this batch and supersedes old starter-phase sequencing restrictions only. Its final parent reconciliation records completed, independently reviewed first-wave drafts, but those reviewed bytes were not retrieved here. No unseen F01/P01 wording or numerical settings are inherited. No reviewed shared guidance is transferred in this entry. [Workflow basis: supplied `Pasted text.txt`, Assigned outputs; Genre-specific questions; Parent review reconciliation.]

## Definition and boundaries

**Working definition:** a precision platformer foregrounds learning and repeatedly executing demanding traversal under sufficiently legible and repeatable rules that refining an action sequence is a central activity. “Precision” describes the intended prominence of execution; it does not specify pixel-sized tolerances, zero forgiveness, a universal death rate or a required penalty. This operational definition is an inference for research, not a formal genre standard. [C-01]

The [platformer parent](platformer.md), `GDR-CAND-20261010-G02-GEN-01`, also includes route expression and exploration-led traversal. This specialization asks a different question: **what does an attempt let the player understand and practise, and what persists between attempts?** A timed route, difficult boss, platform puzzle or punishing climbing game can share relevant problems without necessarily belonging to this subgenre. A [metroidvania hybrid](metroidvania.md) introduces route discovery and capability acquisition; those demands must not be mistaken for execution difficulty alone. [C-01; C-10]

The working boundary deliberately allows demanding play with assistance. Thorson's Celeste article describes timing forgiveness inside a game intended to be difficult. The documented existence of those techniques defeats the narrow assumption that the design must be mechanically unforgiving; it does not establish the best tolerance for another game. [C-02; GDR-SRC-20261010-G02-001]

## Custom research instructions

Begin with the **unit of mastery**: one landing, a linked traversal, a whole room, a long uninterrupted route, or a chosen advanced technique. Describe which demands are intentionally narrow and which barriers are incidental. Inspect takeoff and landing eligibility, momentum, hazards, camera, reset state, checkpoint consequences, available practice, command cancellation and assists. Do not reduce the research to respawn speed. [C-03]

Seek comparisons among different recovery contracts: local retry, segmented practice, longer integrated attempts and deliberate progress loss. Include failure reports and versioned corrections, not only polished demonstrations. The creator of a popular game can explain a decision; that account cannot prove that repetition caused mastery, that all deaths were informative or that all audiences shared the designer's preference. [C-02; C-06; C-09]

For studies, preserve prior experience, filtering, apparatus, assignment, actual treatment and outcome. “Improved progress,” “less frustration,” “more attempts,” “retained performance” and “transfer to a new task” are separate claims. For future observations, capture platform/build, input configuration, room or sequence, reset conditions and timestamps; an expert run with edited failures is not a representative learning trace. [C-04; C-05]

## Player promises and varied audiences

Candidate promises include understandable failure, room to improve, reliable interpretation of chosen actions, a demanding optional ceiling and recognition of a completed performance. These are proposed dimensions, not a survey establishing what precision-platformer players universally expect. A player can pursue mastery while using an input adaptation; a player can want completion rather than the hardest available variant. Assess the actual goal rather than assigning an audience identity from an assist setting. [C-07]

An uninterrupted achievement may be the central chosen goal for some projects. In that case, an inserted checkpoint changes the accomplishment rather than merely removing inconvenience. Conversely, unavoidable repetition of already understood actions may add no intended value. Both are possible design contracts; neither follows from the word “precision.” Getting Over It's creator description provides a nearby explicitly punishing offer, not a warrant to impose its recovery model on this subgenre. [C-09; GDR-SRC-20261010-G02-016]

## Characteristic loops and structures

At attempt scale, the analytical loop is **interpret the situation → select an action sequence → execute → identify the result → choose a revision or rest**. At practice scale, the player tests whether an altered action works consistently. At longer scale, the game may recombine techniques, extend a sequence, present optional variants or permit a return after absence. These are proposed design lenses, not an empirically established mandatory loop. [C-03; C-05]

A repeatable challenge does not require every environmental motion to restart in the same phase. It does require the relevant initial state to be available or inferable. A moving hazard can remain asynchronous when reading its phase is intentional; hiding that phase while expecting an identical memorized input sequence creates a different task. Position alone is therefore an insufficient checkpoint specification. [C-03]

Audit the starting state as a tuple: position, velocity, available actions/resources, hazard phase, camera/framing, facing, pending input and relevant persistence. Decide for each component whether it resets, persists or varies visibly. A held button crossing death/restart needs explicit treatment so a new attempt does not become an involuntary command. This is a conceptual review recipe, not an engine implementation or proven requirement in every game. [C-03; C-06]

## Research evidence: progress is not learning

**Original empirical evidence, narrowly scoped.** Johanson and colleagues studied a browser/keyboard 2D platformer in a 2×2 checkpoint/break design. They analysed 150 filtered experienced adult participants; 117 returned after a week. Assignment filled the smallest group, not a stated random allocation. Training lasted 20 minutes; transfer used new levels for 10 minutes; retention reused trained levels for 10 minutes, with interventions removed in both tests. Breaks varied up to 10 seconds; the comparison still waited one second. Checkpoints increased adjusted training level completion by **3.98 ± 0.64 standard error**. Level-completion effects at transfer/retention were not significant; this is not equivalence or proof of no learning cost. Breaks also aided training progress but waits were often disliked. The combined training interaction was not significant. Filtering for technical/performance criteria and experience, one prototype and attrition constrain generalization, especially to novices and disabled players. [C-04; GDR-SRC-20261010-G02-004, §§4–7, Table 1]

**Evidence-to-application bridge:** this supports investigating recovery structure while measuring outcomes separately. It does not select an optimal delay, justify withholding pauses, establish that voluntary reflection replicates forced breaks, or prove that more attempts mean more learning. A product decision must weigh progress, agency, comfort and the intended achievement—not silently optimize one measure. [C-05]

## Design choices and conditional application process

### Choose the execution demand before the penalty

Write a plain-language completion statement such as “read the moving target and land while retaining the next action,” rather than “die frequently until successful.” Then identify the minimum practice opportunity needed to understand that statement. A local retry may isolate it; a longer route may test integration. Separate rehearsal from an uninterrupted completion attempt when those goals conflict. This is a hypothesis for preserving both access to practice and a chosen performance contract, not a finding that every game needs practice mode. [C-05; C-09]

### Preserve legibility without eliminating discovery

Before narrowing a window, verify that the player can identify safe and unsafe states using available modalities and camera conditions. Introduce a novel hazard where its behavior can be examined, or provide a means to inspect it after failure. Exact rehearsal may be inappropriate when improvisation is intended; instead make the changing state observable. Do not rely on a death total to prove a hazard was readable. [C-03; C-08]

### Select assists by demand, not a single “easy” label

| Demand being changed | Candidate adaptation | What remains to be evaluated |
|---|---|---|
| Command timing at a state boundary | [Bounded action grace](../patterns/bounded-action-grace.md) with explicit expiry and cancellation | Accidental actions, hidden timing dependence and whether the intended manoeuvre remains |
| Sustained or simultaneous input | Remapping, toggle or reduced chord complexity | Menu access, conflicting commands, actual displayed prompts and route feasibility |
| Speed of execution | Adjustable simulation or action pace, where feasible | Hazard relationships, audio/visual timing, camera behavior and any route becoming impossible |
| Length of an integrated attempt | Optional rehearsal segments or configurable recovery | Whether practising fragments teaches the required transitions; honest separation from full-route goals |
| Recognition of hazards | Alternative shapes, motion information or supplementary cues | Clutter, sensory load, meaning without color alone and preservation of necessary uncertainty |

This table is an application hypothesis informed by XAG input/difficulty guidance, not a formal standard or certified solution. Do not copy numerical targets from another XAG context into movement timing. A difficulty option can alter combat while leaving traversal inaccessible, or vice versa. [C-07; GDR-SRC-20261010-G02-005; GDR-SRC-20261010-G02-006; GDR-SRC-20261010-G02-007]

### Treat reset and assist states as authored content

Celeste's official release notes record corrections involving respawn behavior, facing and Dash Assist soft locks, alongside revised controls and assistance presentation. Those notes are inspectable evidence that such combinations required production attention; this batch did not reproduce their behavior. The practical inference is to review every essential route with each supported reset/assist state rather than declare an assist complete when its toggle appears. [C-06; GDR-SRC-20261010-G02-008, V1.3.0.0–V1.4.0.0]

Offer an exit when practice is no longer productive: pause, leave and resume, switch a chosen assist, inspect the rule, or practise a prerequisite. No frustration threshold is prescribed. A design that wants commitment must distinguish meaningful in-game commitment from coercive use of real-world fatigue or inaccessible repetition. These are proposed ethical and product choices, not approved studio policy. [C-07; C-09]

## Applying shared topics

**Reviewed shared guidance transferred: none.** The parent receipt reports reviewed first-wave corrections, but the bytes are missing here. Do not infer permanent IDs or reconstruct their wording.

| Pending dependency | Precision-specific question | Treatment in this draft |
|---|---|---|
| F04 movement/traversal | What actions and reset states make execution repeatable? | Missing shared bytes/links; local conceptual audit only |
| F03 progression | Does an unlock introduce a new rule or merely tighten an existing performance? | Missing shared guidance; no imposed progression curve |
| F02 challenge/decision guidance and F01 learning context | Which error is informative, and which later task actually tests transfer? | No inspected shared candidate bytes; supplied parent correction is a status constraint only |
| P02/P03 input/camera | Does an assist or remap change usable action sequences or hidden state? | Pending shared links; directly inspected XAG sources used narrowly |
| W03 spatial/exploration | Is a route unknown, or known but difficult to execute? | Missing dependency; avoid labelling navigation failures as motor deficits |
| P01 reviewed presentation/accessibility context | Which numerical recommendation belongs to which platform and interaction? | Unseen correction not paraphrased; no numerical accessibility universal imported |

Audio pilot content is not a prerequisite or evidence of a tension requirement.

## Pattern selection and adaptations

[Bounded action grace](../patterns/bounded-action-grace.md), `GDR-CAND-20261010-G02-PAT-01`, applies only where the permitted command is clear and narrowly missed at a state boundary. In a precision-led design, stability of the grace rule and absence of unintended activation are central test questions. It must not become an opaque correction that makes visually identical states behave unpredictably. [C-02; C-08]

[Recoverable ability-gate loop](../patterns/recoverable-ability-gate-loop.md), `GDR-CAND-20261010-G02-PAT-02`, is a conditional option for a capability/exploration hybrid, not a normal requirement for a sequence of challenge rooms. If a necessary exploration reward sits behind a narrow traversal test, specify whether traversal assistance preserves the exploration contract. Do not mechanically let one genre “win.” [C-10]

The review packet queues **challenge-local retry and deliberate re-entry** and **practice/reflection choice** as additional work requests. They require separate evaluation of burden, learning and agency; this file does not claim a released retry pattern exists.

## Representative cases and negative cases

| Evidence route | Platform/build and precise locator | Use and boundary |
|---|---|---|
| Celeste creator article | Platform/build unspecified; GDR-SRC-20261010-G02-001 items 1–2 and conclusion | A creator account against zero-forgiveness necessity; no timing efficacy measurement |
| Celeste production corrections | Versioned notes V1.3.0.0, V1.3.1.0, V1.4.0.0; rollout by platform unverified | Documented implementation/accessibility work and failures; not reproduced gameplay |
| Johanson et al. study | Bespoke browser/keyboard prototype; §§4–7; build unavailable | Measured treatment in a selected sample, not a complete model of commercial precision games |
| Getting Over It creator description | Steam desktop description; About This Game; build uninspected | Deliberate progress-loss offer as an opposing contract, not proven subgenre membership or measured preference |

No game recordings were watched. Source descriptions and release notes remain descriptions even when their publication is official. Their independent and derivative relationships are recorded in References. [C-02; C-04; C-06; C-09]

### Illustrative worked example: crossing a moving carriage

**Illustrative; no prototype or test was performed.** A fictional room asks the player to jump from a moving carriage, touch a refill surface, then expend the restored action to reach an exit. The declared unit of mastery is reading the launch phase and preserving the correct action order, not restarting from an arbitrary hidden velocity. [C-08]

Begin the proposed comparison with a visible resting position from which the carriage can be observed. Document whether it restarts its motion on retry. If it continues, the player can choose when to enter; do not treat a memorized fixed input delay as the only correct strategy. Make the refill state perceptible without relying exclusively on a color change. Before adding grace, distinguish attempts that target the wrong surface from correctly targeted commands near the eligibility boundary. [C-03; C-08]

Offer a proposed practice start before the refill transition, but also test recombination from the ordinary entry. Isolated success cannot show that the player can manage the preceding approach. In a transfer condition, place the same action relationship in a different geometry and reverse an irrelevant visual decoration while preserving the relevant rule; do not merely make the original exit closer. In a retention condition, return later to the original relationship and report familiarity separately. [C-05; C-08]

**Exit conditions:** stop advancing difficulty if the essential initial state is unreadable, a supported input setting makes the sequence impossible, or pending input repeatedly launches the player without a current choice. Revise the state/presentation/control problem before interpreting repeated failure as useful practice. [C-03; C-08]

**Counterexample:** when the core goal is an uninterrupted, openly communicated long-chain performance, a mid-chain completion checkpoint changes the target achievement. Separate rehearsal and access options may be preferable to redefining the completion condition for everyone. Conversely, when the intended goal is explorative travel, insisting on repeated execution of this room may be the wrong priority entirely. [C-09; C-10]

## Accessibility, ethics, localization and production implications

Consider fatigue from repetition independently of whether an individual action is possible. Check sustained holds, rapid reversals, simultaneous commands, visual tracking, memorization and the time available to decide. XAG 107/108 motivate mechanic-specific options; this candidate does not claim that implementing those options covers all disabilities or creates equivalent experience for every player. Recruit for the actual barriers and record remaining exclusions. [C-07; GDR-SRC-20261010-G02-006; GDR-SRC-20261010-G02-007]

Assistance text should describe the changed demand accurately. A localized “restart,” “practice” or “return” label should preserve the intended consequence rather than imply moral failure. Celeste's historical notes provide a production example of revised assistance language and a Dash Assist addition explicitly not yet localized at that point; they do not prove how wording affected players. This makes localization state part of the versioned research/QA record rather than a presumed finished property. [C-06; GDR-SRC-20261010-G02-008]

A proposed QA matrix crosses essential rooms with input schemes, assist states, save/restart transitions and camera conditions. Prioritize unsafe or impossible states before optimizing challenge. Review which distinctions matter for local records or shared competitive comparisons, but do not secretly stigmatize ordinary single-player progress. Telemetry should be minimal, consented and interpreted alongside explanation; do not turn repeated failures into a target engagement metric. These are recommendations for review, not studio policy or implemented systems. [C-07; C-11]

## Research questions and proposed validation

**Not performed.** Define the intended achievement and local rejection criteria before collecting data. Include relevant prior movement familiarity and input/access needs; use a broader sample than the experienced participants in the inspected study when generalizing beyond that context. Let participants pause or withdraw without penalty. [C-11]

| Question | Proposed comparison | Measures and important confounds | Falsifying or revision result |
|---|---|---|---|
| Does recovery isolate useful practice? | Same obstacle and assistance; local recovery versus longer approach; separately test whole-route recombination | Attempts per opportunity, state at entry, repeated error categories, later performance, felt achievement; exposure differs with recovery | Training gains vanish on the intended full sequence, or recovery changes the action being learned |
| Does grace preserve chosen actions? | Matched routes with no grace and a declared bounded rule; retain camera/geometry | Eligible and unintended activations, self-reported command intention, repeated reliability; player adaptation can mask errors | More completion comes with unwanted actions or reduced ability to predict the rule |
| Is reflection valuable without compulsion? | Immediate player-controlled re-entry versus optional pause/review; forced-delay evidence is not assumed equivalent | Voluntary rest, strategy changes, comfort, progress and delayed task performance separately | Reflection choice is unused or burdensome, or changes no relevant outcome; do not infer benefit from time spent waiting |
| Was a rule learned rather than a room memorized? | Unseen layout preserving the rule, with assistance and task demands documented | Rule explanation, action choice, execution; novelty, difficulty and prior exposure are confounds | Success depends on the original geometry or a simpler transfer task rather than reusable understanding |
| Do assists preserve access through a complete sequence? | Essential route across supported input/assist/reset combinations, with relevant participants | Completion feasibility, fatigue, comprehension and unwanted actions; speed changes can affect many systems | Any supported mode creates an essential soft lock or leaves a critical barrier without an acceptable alternative |

Failure frequency is ambiguous without exposure and error type: a condition enabling more attempts can produce more failures while helping progress; a long penalty can suppress attempts without improving understanding. This is measurement reasoning, not a measured outcome of this batch. [C-05]

## Claim ledger

| ID | Material claim and class | Inspected support and applicability | Confidence and unresolved question |
|---|---|---|---|
| C-01 | Execution prominence, not fixed tolerance or punishment, defines this candidate's useful specialization. `inference` | Supplied genre roster/boundary instructions; GDR-SRC-20261010-G02-001 intended difficulty with forgiveness; GDR-SRC-20261010-G02-016 contrasting offer | Moderate research utility, low universal taxonomy; overlapping labels remain. G02-CON-01 |
| C-02 | Celeste's creator describes forgiveness within demanding traversal. `practitioner-heuristic` | GDR-SRC-20261010-G02-001 items 1–2 and conclusion | High for attributed account; low for causal efficacy elsewhere; no optimum or necessity |
| C-03 | Reset state and readable variation should be specified before interpreting repeatability. `inference` | State-dependence reasoning; GDR-SRC-20261010-G02-008 V1.4.0.0 correction context | Moderate logical case; exact state requirements depend on intended task |
| C-04 | The inspected experiment supports a narrow progress result with important sample, treatment and uncertainty limits. `empirical-evidence` | GDR-SRC-20261010-G02-004 §§4–7; Table 1, p.387:13; numerical and method summary above | Moderate within the study; filtered sample, no stated random assignment, attrition and prototype limits. No equivalence inference; G02-CON-02/05 |
| C-05 | Progress, attempt count, transfer, retention and experience must remain separate evaluation targets. `inference` | C-04's design and outcome distinctions; proposed interpretation of exposure/confounds | High logical distinction, not proof of a preferred recovery model |
| C-06 | Official notes record reset/assist issues and evolving controls/wording/localization. `observed-example` | GDR-SRC-20261010-G02-008 V1.3.0.0 UI, V1.3.1.0 additions, V1.4.0.0 options/rebinding/fixes | High for the text artifact; no game reproduction or measured effect |
| C-07 | Adapt individual execution demands and review fatigue, wording and access rather than infer access from one difficulty option. `inference` | GDR-SRC-20261010-G02-005 Introduction; GDR-SRC-20261010-G02-006 Background/implementation; GDR-SRC-20261010-G02-007 mechanic-specific guidance | Moderate design rationale; no formal standard or universal equivalence. G02-CON-05 |
| C-08 | The carriage example and isolated/combined comparisons may discriminate hidden state, recognition and timing problems. `hypothesis` | Synthetic application of C-02/03/05; PAT-01 candidate | Low until tested; combined demands and verbal reports can obscure causes |
| C-09 | Long-chain or progress-loss contracts can justify different recovery choices, but are not genre necessities. `inference` | GDR-SRC-20261010-G02-016 creator description supplies a contrary offer; no audience outcome evidence | Moderate conditional logic; ethical/access tradeoffs unresolved. G02-CON-01/02 |
| C-10 | An exploration hybrid needs separate treatment of finding, unlocking and executing a route. `inference` | GEN-03/PAT-02 candidate synthesis; not transferred reviewed guidance | Moderate conceptual distinction; no validated hybrid priority order |
| C-11 | Proposed tests must evaluate intended actions, whole-sequence feasibility and genuine transfer with suitable participants. `hypothesis` | Candidate validation design, C-04/05/07 context; supplied F01/P01 correction constraints | Low for specific protocol efficacy; no tests performed or power calculation made |

## Coverage checkpoint, review and history

| Researched subtopic | Coverage and gap | Next discriminating question |
|---|---|---|
| Repeatable execution and grace | Creator mechanism account; no build/input recording | Are rejected commands eligible near-boundary actions or deliberate cancellations? |
| Checkpoints, retries and practice | One original study plus conceptual comparison; no independent replication inspected | Which recovery change preserves the intended unit of mastery? |
| Frustration and reflection | Study distinguishes subjective and progress outcomes; voluntary reflection remains untested here | Does a player-controlled pause meet the objective without imposed waiting? |
| Assists and readable hazards | Primary platform guidance and historical production corrections; no representative access study | Which essential route remains inaccessible or becomes unreliable? |
| Transfer and hybrid demands | Explicit proposed discrimination; shared reviewed bytes unavailable | Can a player apply the same rule in a new arrangement without a hidden difficulty change? |

**Author self-review:** the strongest recommendation is to make meaningful practice accessible without equating punishment with mastery. Its opposing case is that isolating fragments can remove endurance, rhythm and transition management from a deliberately integrated performance. The draft therefore preserves full-sequence evaluation and does not make local checkpoints mandatory. It also refuses to infer that a voluntary pause reproduces a forced-break result. This is author challenge, not independent review.

Version `0.1.0`, candidate revision `initial-1`; no predecessor or supersession. Byte identity is in the [review packet](../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity). Gate C independent review is pending; Gate D host tests and Gate E release are not passed. General population, multiplayer, touch, VR and long-session conclusions remain outside inspected coverage.

## References

### GDR-SRC-20261010-G02-001

**Maddy Thorson. [Celeste & Forgiveness](https://www.maddymakesgames.com/articles/celeste_and_forgiveness/index.html).** Maddy Makes Games. Publication/update: unknown; page identifies an earlier Twitter thread but supplies no publication date.

Edition/build: Undated creator article; Celeste build/platform not specified. Accessed **2026-10-10**; access: `full`; type: Primary creator explanation.

**Inspected locator:** Numbered items 1–10 and final paragraph; text inspected, embedded animations not observed.

**Claims supported here:** C-01, C-02. **Limits:** Documents described techniques and creator interpretation, not measured player effects or portable timing constants. **Independence:** Same Celeste production context as GDR-SRC-20261010-G02-008; not independent corroboration. **Rights:** Copyrighted creator text; paraphrase only, no animations redistributed.

### GDR-SRC-20261010-G02-004

**Colby Johanson; Brandon Piller; Carl Gutwin; Regan L. Mandryk. [If at First You Don’t Succeed: Helping Players Make Progress in Games with Breaks and Checkpoints](https://www.cjohanson.net/downloads/publications/2023%20-%20If%20at%20First%20You%20Dont%20Succeed.pdf).** ACM, Proceedings of the ACM on Human-Computer Interaction 7, CHI PLAY, Article 387, 27 pages. Publication/update: 2023-11 (publication date printed in paper). DOI: [10.1145/3611033](https://doi.org/10.1145/3611033).

Edition/build: Author-hosted publisher-formatted PDF; bespoke browser-based 2D platformer, executable version unspecified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Original empirical study.

**Inspected locator:** §§4.1–4.6, pp. 387:6–12; §§5.1–5.3, pp. 387:12–14; Table 1/Figure 4, p. 387:13; §6.2.1, pp. 387:15–16; §7.4, p. 387:23. PDF pages 8, 12 and 13 rendered/inspected; page-14 screenshot failed, corresponding prose read.

**Claims supported here:** C-04; C-05 and C-11 methodological bridge. **Limits:** Full design, participant filtering and interpretation limits are summarized in precision-platformer C-04; raw data and software were not reanalysed. **Independence:** One study and research group; ResearchGate and indexing records refer to the same DOI, not replications. **Rights:** 2023 copyright held by owner/authors; publication rights licensed to ACM; paraphrase and citation only, no PDF/screenshots redistributed.

### GDR-SRC-20261010-G02-005

**Microsoft Xbox accessibility team. [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).** Microsoft Learn. Publication/update: V3.2 published 2023-06-08; inspected page last updated 2026-08-14.

Edition/build: V3.2 hub as served 2026-10-10; page date is distinct from guideline-set version. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative platform guidance.

**Inspected locator:** Introduction; Overview of XAG components → Example content; version heading and last-updated footer.

**Claims supported here:** C-07. **Limits:** The introduction explicitly excludes compliance/legal-checklist status; no formal-standard claim is made. **Independence:** Common guidance family with GDR-SRC-20261010-G02-006 and GDR-SRC-20261010-G02-007; not independent empirical studies. **Rights:** Microsoft documentation; paraphrase only, example images not redistributed.

### GDR-SRC-20261010-G02-006

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page.

Edition/build: XAG 107 page within V3.2 set; live page snapshot checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility/input guidance.

**Inspected locator:** Goal; Overview; Background and foundational information → Speed, Complexity, Duration and proposed alternatives; Implementation guidelines → remapping and updated prompts; mobile-input section reviewed for scope only.

**Claims supported here:** C-07. **Limits:** No game-independent timing, sensitivity, target-size or compliance requirement is inferred; core article text was accessible despite an authorization banner. **Independence:** Same XAG guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-007; cited third-party examples are not additional observations. **Rights:** Microsoft documentation; paraphrase only; embedded example media not inspected as gameplay.

### GDR-SRC-20261010-G02-007

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page; an earlier search result showed another date, not adopted.

Edition/build: XAG 108 page within V3.2 set, checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility guidance.

**Inspected locator:** Goal; Overview; Scoping questions and individual game-mechanic adjustment guidance.

**Claims supported here:** C-07. **Limits:** Options are design guidance, not a guarantee of access for every player or a formal standard; text accessible despite authorization banner. **Independence:** Same guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-006. **Rights:** Microsoft documentation; paraphrase only.

### GDR-SRC-20261010-G02-008

**Celeste development team. [Celeste — Changelog](https://www.celestegame.com/changelog.html).** Celeste official website. Publication/update: unknown for individual entries on page; version labels available.

Edition/build: Page headed V1.4.1.0; cited entries V1.3.0.0, V1.3.1.0 and V1.4.0.0; not a claim about current rollout on every platform. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary versioned production artifact.

**Inspected locator:** V1.3.0.0 → UI Design Changes; V1.3.1.0 → Changes and Additions; V1.4.0.0 → New Options, Control Rebinding and Bug Fixes (Farewell bird respawn, Ch5/Ch9 facing, Dash Assist soft locks).

**Claims supported here:** C-03 context, C-06. **Limits:** Observed release-note content only. No game build was run; fixes and option efficacy were not independently reproduced. **Independence:** Same Celeste production context as GDR-SRC-20261010-G02-001; multiple entries are not independent experiments. **Rights:** Copyrighted release notes; brief paraphrase only; no code or media copied.

### GDR-SRC-20261010-G02-016

**Bennett Foddy (developer and publisher fields). [Getting Over It with Bennett Foddy](https://store.steampowered.com/app/240720/Getting_Over_It_with_Bennett_Foddy/).** Creator-supplied Steam storefront. Publication/update: Page publication/update unknown; listed Steam release 2017-12-06.

Edition/build: Steam desktop description; executable build not inspected. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary creator description artifact.

**Inspected locator:** About This Game → opening climbing description and bullet about repeated loss of progress; developer/publisher fields.

**Claims supported here:** C-01, C-09. **Limits:** Evidence of an explicitly punishing stated promise, not measured frustration or proof of precision-platformer genre membership. **Independence:** Independent creator context from Celeste. Foddy’s own website was only a route to this description. **Rights:** Creator/storefront copyright; paraphrase only; satirical numerical language not reproduced as research data.
