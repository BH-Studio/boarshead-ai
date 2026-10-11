---
id: GDR-CAND-20261010-G02-GEN-01
kind: genre
title: Platformer
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
- platform game
- jump-and-run
- traversal-led platforming
tags:
- traversal
- spatial-affordance
- momentum
- route-expression
- checkpoints
- genre-boundary
related_topics: []
related_patterns:
- GDR-CAND-20261010-G02-PAT-01
- GDR-CAND-20261010-G02-PAT-02
related_genres:
- GDR-CAND-20261010-G02-GEN-02
- GDR-CAND-20261010-G02-GEN-03
source_ids:
- GDR-SRC-20261010-G02-001
- GDR-SRC-20261010-G02-002
- GDR-SRC-20261010-G02-003
- GDR-SRC-20261010-G02-004
- GDR-SRC-20261010-G02-005
- GDR-SRC-20261010-G02-006
- GDR-SRC-20261010-G02-009
- GDR-SRC-20261010-G02-011
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

# Platformer

> **Draft research candidate, not released guidance.** Version 0.1.0; candidate revision `initial-1`; independent review not performed. Definitions and proposed adaptations below are bounded inferences or hypotheses, not an approved studio design. No game build, gameplay recording, prototype or player test was run in this batch.

The supplied G02 dispatch authorizes this batch and supersedes old starter-phase sequencing restrictions only. Its final parent reconciliation records completed, independently reviewed first-wave drafts, but those reviewed bytes were not retrieved here. No unseen F01/P01 wording or numerical settings are inherited. No reviewed shared guidance is transferred in this entry. [Workflow basis: supplied `Pasted text.txt`, Assigned outputs; Genre-specific questions; Parent review reconciliation.]

## Definition and boundaries

**Working definition:** a platformer makes controlled traversal among surfaces, trajectories, obstacles or landing opportunities a recurring consequential activity. Jumping is a common expression, not a sufficient classification test by itself. The useful boundary is what the player repeatedly reads, chooses and executes—not the presence of a jump button, a side-on camera or a storefront tag. This is this candidate's operational definition, not a formal taxonomy or approved studio decision. [C-01]

[Precision platformer](precision-platformer.md), `GDR-CAND-20261010-G02-GEN-02`, is a conditional specialization when repeatable execution is foregrounded. [Metroidvania](metroidvania.md), `GDR-CAND-20261010-G02-GEN-03`, foregrounds persistent-world reinterpretation through capabilities; it can overlap with platforming without making every crossing an execution examination. Dimensionality, camera arrangement, cooperative play, tone and device are facets. An adventure with occasional jumping may need movement guidance without platformer-led pacing. [C-01]

The distinction changes design work: a demanding optional shortcut can coexist with an accommodating required route; a beautiful vista can invite exploration rather than serve as a timing test. Nintendo's account of advanced movement and the creator description of A Short Hike supply contrasting intended uses, not evidence that either arrangement satisfies every player. [C-02; GDR-SRC-20261010-G02-003; GDR-SRC-20261010-G02-011]

## Custom research instructions

Investigate **how a player forms and revises a prediction of a traversal action**. Separate recognition of a usable surface, selection of a route, control of takeoff/momentum, in-flight adjustment and interpretation of landing or failure. Do not classify every miss as poor execution before checking visibility, input interpretation and starting state. [C-03]

For subsequent research, retain a representative matrix rather than an iconic-game checklist: 2D courses and 3D spaces; fixed and player-controlled cameras; discrete jumps and momentum-led movement; mandatory basic traversal and optional expressive routes; exploration-led and execution-led goals. Seek original studies with their actual tasks, creator accounts with production limitations, and build-identified observations. The present case set is purposive and mostly commercially visible; it cannot estimate genre-wide prevalence or audience preferences. [C-10]

Challenge these comparisons explicitly: completion speed as the only expression of competence; all-platformer conclusions from a single precision game; failure totals without opportunities to fail; easier geometry conflated with clearer geometry; stereoscopic readability exported to ordinary displays; and commercial success treated as causal validation. Ask what changes when a player cannot comfortably hold an input, distinguish a surface, use binocular depth, or operate movement and camera controls together. [C-03; C-06; GDR-SRC-20261010-G02-002; GDR-SRC-20261010-G02-006]

## Player promises and varied audiences

Treat promises as **candidate experience contracts**, not demographic facts. Possible priorities are readable traversal, route expression, discovery, improvisation, mastery of a movement vocabulary or sustained performance. A project should name its primary contract and the role of optional challenges before interpreting a playtest. A player may want precise control without wanting a timer, and may want difficult routes without accepting a long replay cost. These are hypotheses to investigate through recruitment and interviews, not measured audience segments in this batch. [C-02; C-09]

A Short Hike's creator storefront describes self-paced hiking, climbing and soaring; that is a documented alternative to treating all platformer-tagged work as time-trial instruction. The source is a stated promise, not a direct observation that play is relaxing. Nintendo's advanced-movement discussion describes Roll/Long Jump and faster route possibilities alongside the ordinary course. Neither source establishes a universally optimal route hierarchy. [C-02; GDR-SRC-20261010-G02-011; GDR-SRC-20261010-G02-003]

## Characteristic loops and structures

Use three analytical horizons. At the **action horizon**, a player perceives a reachable state, acts and interprets the result. At the **local route horizon**, actions combine around hazards, landing spaces and recovery positions. At the **session horizon**, courses, hubs or regions determine whether repetition serves rehearsal, exploration or an integrated performance. These are proposed analytical units, not mandatory architecture. [C-03]

Momentum changes the relation between horizons: a platform reached with useful speed is not necessarily equivalent to the same platform reached from rest. A checkpoint that reproduces position but not the approach can therefore alter the challenge being practised. Camera transitions and input carried through respawn likewise belong in a start-state review. This follows from the dependency of later actions on earlier state; it is not a measured claim about every engine. [C-04]

Obstacle distribution should be reasoned from the intended decision. A gap can test prediction; a moving target adds temporal estimation; a branching route adds selection; a constrained landing adds recovery planning. Combining these demands can be intentional, but a failure then needs a diagnostic explanation. Counting hazards or narrowing every platform cannot identify which demand became harder. [C-03; C-04]

## Design choices and conditional application process

### Diagnose before adjusting jump tolerance

Ask the player to indicate the intended landing and anticipated path before an attempt, then compare that account with the resulting action. If the target or reachable route was misidentified, first change presentation or provide a reversible view—not an invisible movement correction. If the route was understood but command timing falls just outside a stable eligibility boundary, trial a bounded grace rule. If an early command triggers an unwanted later action, shorten or cancel the pending action instead. This diagnostic sequence is a proposed comparison method, not a validated way to read intention from telemetry alone. [C-03; C-05]

Nintendo's 3D Land account describes adapting reference-plane/camera presentation and adding positional shadows for play with stereoscopy disabled. The transferable issue is availability of usable depth information; the exact 3DS view configuration is not a prescription for another display. A shadow, silhouette, landing indicator or optional camera adjustment must still be tested in the local scene. [C-03; GDR-SRC-20261010-G02-002]

### Choose a route contract

| Local goal | Candidate arrangement | What it may preserve | Cost or reason to choose another arrangement |
|---|---|---|---|
| Basic traversal with expression | Required route using introduced actions; optional shortcut using combinations | Completion without requiring every advanced technique | Optional rewards may make the shortcut feel compulsory; additional route QA |
| Momentum-led movement | Approach space and readable continuation; recovery that preserves or deliberately resets speed | Planning across consecutive actions | A stop-start checkpoint may destroy the intended sequence |
| Explorative platforming | Safe observation positions and more than one useful route or return opportunity | Route choice rather than repeated execution as the dominant task | Excessive explicit direction can remove the local discovery question |
| Integrated performance | Longer linked sequence, with separately offered rehearsal where appropriate | Whole-sequence execution as a stated goal | Replay cost and interruption barriers require explicit review |

These are conditional design hypotheses. Select among them using the intended contract and local evidence; none follows automatically from a genre label. [C-04; C-09]

### Separate challenge from replay cost

Record what failure loses: immediate position, accumulated route progress, resources, information or session time. A local checkpoint and a wider landing solve different problems. Consider optional practice or a shorter return before flattening an intended manoeuvre, but do not assume fast retries always produce learning or a better experience. The inspected checkpoint/break experiment is summarized, with its sample and limits, in [precision platformer, C-04](precision-platformer.md#research-evidence-progress-is-not-learning); it is not a source of universal checkpoint spacing. [C-04; GDR-SRC-20261010-G02-004]

### Evaluate the same promise across input and presentation conditions

Compare the required route with the actual remapped controls, target display and camera mode. Check whether changing prompts, hold/toggle behavior or movement speed creates a new unreachable state or unintended shortcut. Microsoft XAG 107 is a non-normative source for considering speed, complexity and duration of input; it does not supply a universal collision-box, buffer or sensitivity value for this entry. [C-06; GDR-SRC-20261010-G02-005; GDR-SRC-20261010-G02-006]

## Applying shared topics

**Reviewed shared guidance transferred: none.** The following are dependency requests, not links to nonexistent or unseen canonical files. `related_topics` remains empty deliberately.

| Dependency and domain | What this genre adds | Current treatment |
|---|---|---|
| F04 movement/traversal; Foundations and Systems | Takeoff/landing state, momentum across surfaces, permissive versus exact eligibility | Missing topic bytes and approved links; use only this candidate's limited analysis |
| F03 progression; Foundations and Systems | Movement unlock versus optional expressive technique; route obligations after unlocking | Missing bytes/IDs; do not assume a reward schedule |
| W03 spatial/exploration; Worlds and Characters | Landing affordances, observation positions, course versus hub routing | Missing bytes/IDs; shared spatial principles are not reconstructed here |
| P02/P03 input/camera; Presentation and Interaction | Camera-input coupling, remapping, landing visibility and display context | Missing reviewed bytes/links; recheck platform guidance before implementation |
| F01/P01 first-wave reviewed drafts | Learning/transfer and presentation-accessibility boundaries | Parent review receipt exists; corrected content bytes not retrieved; no numerical transfer |

The supplied dispatch controls these availability statements. Audio tension research is neither a prerequisite nor evidence that a platformer needs tension.

## Pattern selection and adaptations

[Bounded action grace](../patterns/bounded-action-grace.md), `GDR-CAND-20261010-G02-PAT-01`, is a draft candidate when failures arise at a well-defined command/state boundary. Its expiry, consumption and cancellation rules matter more than an inherited timing number. Do not use it to hide a misleading camera or to execute a command the player has already cancelled. [C-05; GDR-SRC-20261010-G02-001]

[Recoverable ability-gate loop](../patterns/recoverable-ability-gate-loop.md), `GDR-CAND-20261010-G02-PAT-02`, is relevant only when acquired capabilities change previously encountered routes. A linear course with no meaningful return need not adopt it. In a hybrid, make explicit whether a newly unlocked route tests recognition, execution or both; an exploration breakthrough can become a repeated motor barrier if an essential return requires an unpractised manoeuvre. [C-08]

Landing/depth-cue authoring and challenge-local retry/practice are additional pattern work requests in the review packet. They are not silently supplied as released techniques or squeezed into this packet's two-pattern limit.

## Representative cases and negative cases

All named cases below are **reported examples or directly inspected text artifacts**, not played or video-observed sequences. Their source locators are reproducible evidence routes; they are not invented game-scene timestamps.

| Case and platform/build context | Inspected route and bounded contribution | What is not established |
|---|---|---|
| Super Mario 3D Land, Nintendo 3DS; build unspecified | GDR-SRC-20261010-G02-002 §4; GDR-SRC-20261010-G02-003 §7: creator reasoning about visibility and advanced actions | Relative efficacy of each aid, universal difficulty expectations, current implementation behavior |
| Celeste; GDR-SRC-20261010-G02-001 does not identify platform/build | Creator article items 1–2 and conclusion: forgiving input-state timing is compatible with an intended demanding game | An optimal grace duration or proof that forgiveness caused commercial or learning outcomes |
| A Short Hike; creator desktop listings, versions in GDR-SRC-20261010-G02-011 reference | Opening description, feature bullets and creator genre labels | Measured comfort, an exclusive genre classification, actual player behavior |
| Getting Over It; Steam desktop description, executable uninspected | GDR-SRC-20261010-G02-016 About This Game explicitly frames repeated progress loss as part of its offer | That punishment is necessary for platformers, or that every precision player wants it |

The last case is a **contrary stated contract**, not a recommendation to impose punishment. It shows why a proposed reduction in replay cost can conflict with a deliberately chosen experience. A requirement for that experience would still need player-facing communication and ethical review. [C-09; GDR-SRC-20261010-G02-016]

### Illustrative worked example: a branching rooftop route

**Illustrative, not a shipped game or a performed test.** A fictional course starts on a broad roof facing a gap. The required route reaches a lower balcony, then a stationary lift; an optional route carries running speed to an upper roof. The prototype designer declares that completion tests basic trajectory reading, while the upper route offers expressive chaining. No particular dimensions or timings are prescribed. [C-07]

In the first condition, both routes share similar materials and the camera hides the lower balcony until takeoff. A miss cannot be interpreted as inadequate jump skill because the intended target may never have been readable. The proposed revision exposes the required landing from a safe stance and distinguishes traversable surfaces without relying on color alone. It leaves the optional trajectory intact. In a second comparison, retain the presentation and vary only the early-press eligibility rule. This separates a visual explanation from an input-boundary explanation. [C-03; C-07]

Place a proposed retry position before the decision with an explicit resting state. For the speed route, also offer an approach that can reproduce the needed momentum; merely spawning on the lip would change the task. Ask whether the optional reward is effectively mandatory for progression. If it is, either teach its required action on the main route or revise the reward dependency. [C-04; C-07]

**Counterexample:** a continuous downhill course whose primary contract is carrying momentum may be damaged by safe stops before every obstacle. Preserve an uninterrupted main route and compare a separate rehearsal mode rather than mechanically inserting the rooftop recipe. A secret platform intentionally concealed by perspective is also a different information contract; distinguish optional discovery from an essential blind jump. [C-04; C-09]

## Accessibility, ethics, localization and production implications

A workable access review distinguishes seeing the opportunity, issuing the action and maintaining it. Alternatives can include remapped commands, reduced simultaneous inputs, toggles for sustained actions, route assistance or altered movement speed. Each changes something different; do not present a single difficulty slider as covering all needs. XAG guidance motivates the questions, but the complete route must be evaluated with intended users and devices. [C-06; GDR-SRC-20261010-G02-006]

For this genre, a proposed production checklist includes testing silhouettes against moving backgrounds, verifying information when stereoscopy or optional effects are absent, and checking camera demands alongside movement demands. These are applications of the visibility and input issues above, not numerical accessibility standards. Localized instructions should refer to the actual bound action, allow text expansion, and avoid requiring a directional metaphor that conflicts with the displayed camera. A control remap needs correspondingly accurate prompts. [C-06; GDR-SRC-20261010-G02-002; GDR-SRC-20261010-G02-006]

Ethically, describe which assist changes execution, navigation or progress loss without humiliation or a hidden status penalty. Do not force players to repeatedly demonstrate inability before making an access option discoverable. That is a proposed research stance and product decision for review, not an approved studio policy. In production, route variants, moving surfaces, checkpoint-state combinations and input modes expand the QA matrix; prioritize essential traversal before optional perfection goals. No engineering cost or performance estimate was measured here. [C-06; C-10]

## Research questions and validation

**All tests below are proposed and not performed.** Recruit separately for familiarity with the specific movement grammar, input device and relevant sensory/motor access needs; do not substitute total hours of gaming for those characteristics. Obtain consent, allow breaks/withdrawal and do not expose participants to avoidable sensory discomfort. No sample-size, success-rate or timing threshold is authorized by this draft. [C-10]

| Question | Comparison and procedure | Measures and confounds | Result that would change the recommendation |
|---|---|---|---|
| Is the obstacle misread or misexecuted? | Same physics; vary target visibility. Ask for a predicted landing before acting; use matched, counterbalanced layouts | Target identification, actual landing, stated cause; verbalization and prior layout exposure can change behavior | Better recognition without better intended-route execution rejects visibility as the sufficient remedy |
| Does optional expression remain optional? | Required route alone versus required-plus-shortcut, with rewards controlled | Completion route, felt obligation, exploration and perceived competence; speed incentives may dominate | Main-route players feel penalized or cannot progress without the advanced move |
| Does a retry position preserve the movement problem? | Identical obstacle with reproducible resting and approach states | Entry velocity/state, recovery burden, repeated errors, later novel-layout performance | A nearer checkpoint teaches a state unavailable in the actual route, or burdensome replay contributes no desired integration |
| Does an aid improve access without unwanted actions? | Compare presentation aid, input aid and combined condition separately | Intended versus accidental activations, fatigue, comprehension, perceived control | An aid raises completion while undermining chosen actions or leaving the essential demand inaccessible |

For transfer, use a **new arrangement requiring the same rule**, not a remembered course, an easier jump or a novel-looking but mechanically different task. A delayed return to the trained course measures a different mixture of retention and familiarity. This discrimination is explicit because the parent brief reports an F01 correction on transfer examples; no unseen corrected text is quoted. [C-10]

## Claim ledger

Confidence applies to the claim's stated scope, not the popularity of its examples. Conflict labels below are local to this packet; none is a permanent register allocation.

| ID | Material claim and class | Support, locator and applicability | Confidence, alternatives and unresolved limit |
|---|---|---|---|
| C-01 | The operational boundary is recurring consequential traversal, with precision and capability-exploration as overlapping emphases. `inference` | Supplied TAXONOMY genre/facet distinction; contrasting GDR-SRC-20261010-G02-003 §7, GDR-SRC-20261010-G02-011 description, GDR-SRC-20261010-G02-009 §§4–5 | Moderate as a useful research partition, low as a universal classification; contested by hybrids. Not approved taxonomy |
| C-02 | Platformer-related offers can foreground optional expression or self-paced exploration rather than time trials alone. `observed-example` | Inspected creator statements/product text: GDR-SRC-20261010-G02-003 §7; GDR-SRC-20261010-G02-011 description and tags | High that these texts make distinct offers; audience response unknown. Genre prevalence not inferred |
| C-03 | Diagnose affordance reading separately from command execution before selecting a remedy. `inference` | GDR-SRC-20261010-G02-002 §4 illustrates presentation reasoning; GDR-SRC-20261010-G02-006 Background identifies multiple input demands | Moderate rationale; local diagnostic method unvalidated. Telemetry alone cannot identify intention |
| C-04 | Checkpoint and route choices should preserve the intended start state and distinguish execution from replay cost. `inference` | GDR-SRC-20261010-G02-004 §§4–7 is narrow empirical context; GDR-SRC-20261010-G02-003 §7 motivates route variety; state-dependence reasoning | Moderate logical bridge; no universal spacing. G02-CON-02 concerns retry/break tradeoffs |
| C-05 | Bounded grace is a candidate response to eligible boundary misses, not a general fix for unreadable space. `hypothesis` | GDR-SRC-20261010-G02-001 items 1–2, conclusion; detailed candidate PAT-01 | Low for local efficacy until tested; unintended activation can reverse benefit. G02-CON-01 |
| C-06 | Input, display and localized-prompt adaptations need separate, contextual checks; no imported numerical universal applies. `inference` | GDR-SRC-20261010-G02-005 Introduction; GDR-SRC-20261010-G02-006 Goal/Background/remapping; GDR-SRC-20261010-G02-002 §4 | Moderate for review priorities; no completeness or legal-compliance claim. G02-CON-05 |
| C-07 | The rooftop comparison can distinguish visibility, action-boundary and momentum explanations. `hypothesis` | Illustrative construction from C-03–C-05, not external observed behavior | Low until the proposed comparisons discriminate causes; layout/order confounds remain |
| C-08 | Capability-driven return structures are optional for platformers and can conflict with mandatory motor barriers. `inference` | GDR-SRC-20261010-G02-009 §§4–5; local GEN-03/PAT-02 synthesis | Moderate conditional reasoning; does not require every platformer to backtrack |
| C-09 | Replay loss can be a deliberately offered contract, but cannot be assumed a genre necessity. `inference` | GDR-SRC-20261010-G02-016 About This Game is the opposing creator-described offer; GDR-SRC-20261010-G02-011 is contrasting context | Moderate that goals differ; no measured preference distribution. G02-CON-01/02 |
| C-10 | Proposed comparisons must distinguish novelty, access needs and local objectives rather than infer learning from completion. `hypothesis` | Methodological proposal; GDR-SRC-20261010-G02-004 §§4–7 provides bounded comparison context; supplied G02/F01 correction receipt | Low for particular test sensitivity; no study here; experienced-source selection limits generalization |

## Coverage checkpoint, review and history

| Researched subtopic | Evidence coverage and remaining gap | Next discriminating question |
|---|---|---|
| Jump reading and basic/advanced actions | Creator accounts inspected; no build observation or novice comparison | Which errors remain after target information is made available? |
| Momentum, obstacles, routes and checkpoints | Conditional synthesis plus one platformer experiment; no local state audit | Which reset state preserves the intended movement task? |
| Expressive versus explorative play | Contrasting creator offers; audience prevalence unknown | Do rewards preserve genuine route choice for different goals? |
| Access and production | Current input guidance and older presentation account; no representative access testing | Which mandatory demand remains after remapping or visual changes? |
| Hybrid boundaries | Working distinction only; shared topic bytes missing | Does the project's primary bottleneck concern traversal, execution or world reinterpretation? |

**Author self-review:** the strongest recommendation—fix a misread affordance before adding movement forgiveness—could itself over-separate perception and action. A forgiving action may help a player discover a rule, and a prediction interview can change play. Accordingly, compare combined and isolated interventions; do not impose a diagnostic sequence as a gate that withholds assistance. No independent review has occurred.

Version `0.1.0`, candidate revision `initial-1`, initial G02 submission. Predecessor and supersession are null. Exact byte identity is recorded in the [review packet](../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity). Gate C independent evidence/content review is pending; Gate D host/retrieval testing and Gate E release are not passed. This file is complete as a bounded draft, not complete research coverage of the genre.

## References

### GDR-SRC-20261010-G02-001

**Maddy Thorson. [Celeste & Forgiveness](https://www.maddymakesgames.com/articles/celeste_and_forgiveness/index.html).** Maddy Makes Games. Publication/update: unknown; page identifies an earlier Twitter thread but supplies no publication date.

Edition/build: Undated creator article; Celeste build/platform not specified. Accessed **2026-10-10**; access: `full`; type: Primary creator explanation.

**Inspected locator:** Numbered items 1–10 and final paragraph; text inspected, embedded animations not observed.

**Claims supported here:** C-05; creator case. **Limits:** Documents described techniques and creator interpretation, not measured player effects or portable timing constants. **Independence:** Same Celeste production context as GDR-SRC-20261010-G02-008; not independent corroboration. **Rights:** Copyrighted creator text; paraphrase only, no animations redistributed.

### GDR-SRC-20261010-G02-002

**Satoru Iwata interviewing Hayashida, Motokura and colleagues. [Iwata Asks: SUPER MARIO 3D LAND, Vol. 1, §4, It’s So High I’m Scared!](https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-SUPER-MARIO-3D-LAND/Vol-1-SUPER-MARIO-3D-LAND/4-It-s-So-High-I-m-Scared-/4-It-s-So-High-I-m-Scared--216999.html).** Nintendo UK. Publication/update: unknown on inspected page; discussion explicitly concerns 2011 Nintendo 3DS production.

Edition/build: English UK interview, Nintendo 3DS; no executable build identified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary developer interview.

**Inspected locator:** §4: Hayashida/Motokura exchange on the reference plane, depth slider and object/player shadows; final exchange on Tanooki Mario.

**Claims supported here:** C-03, C-06. **Limits:** Reported production decisions and informal tester impressions, not a controlled depth-cue experiment. **Independence:** Same interview/production as GDR-SRC-20261010-G02-003; US page is an alternate route, not another independent source. **Rights:** Nintendo interview copyright; short paraphrase only.

### GDR-SRC-20261010-G02-003

**Satoru Iwata interviewing Hayashida and Motokura. [Iwata Asks: SUPER MARIO 3D LAND, Vol. 1, §7, Advanced Players Do the Long Jump](https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-SUPER-MARIO-3D-LAND/Vol-1-SUPER-MARIO-3D-LAND/7-Advanced-Players-Do-the-Long-Jump/7-Advanced-Players-Do-the-Long-Jump-217120.html).** Nintendo UK. Publication/update: unknown on inspected page; September 2011 event referenced in text.

Edition/build: English UK interview; Nintendo 3DS production, build unspecified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary developer interview.

**Inspected locator:** §7: opening standing/running-jump discussion; Motokura on Roll and Long Jump, Time Attack; closing discussion of skipping course content.

**Claims supported here:** C-01, C-02, C-04. **Limits:** Creator account, not evidence that optional advanced movement benefits every audience. **Independence:** Same underlying interview as GDR-SRC-20261010-G02-002, not a second team or study. **Rights:** Nintendo interview copyright; paraphrase only.

### GDR-SRC-20261010-G02-004

**Colby Johanson; Brandon Piller; Carl Gutwin; Regan L. Mandryk. [If at First You Don’t Succeed: Helping Players Make Progress in Games with Breaks and Checkpoints](https://www.cjohanson.net/downloads/publications/2023%20-%20If%20at%20First%20You%20Dont%20Succeed.pdf).** ACM, Proceedings of the ACM on Human-Computer Interaction 7, CHI PLAY, Article 387, 27 pages. Publication/update: 2023-11 (publication date printed in paper). DOI: [10.1145/3611033](https://doi.org/10.1145/3611033).

Edition/build: Author-hosted publisher-formatted PDF; bespoke browser-based 2D platformer, executable version unspecified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Original empirical study.

**Inspected locator:** §§4.1–4.6, pp. 387:6–12; §§5.1–5.3, pp. 387:12–14; Table 1/Figure 4, p. 387:13; §6.2.1, pp. 387:15–16; §7.4, p. 387:23. PDF pages 8, 12 and 13 rendered/inspected; page-14 screenshot failed, corresponding prose read.

**Claims supported here:** C-04, C-10; study details delegated to sibling GEN-02. **Limits:** Full design, participant filtering and interpretation limits are summarized in precision-platformer C-04; raw data and software were not reanalysed. **Independence:** One study and research group; ResearchGate and indexing records refer to the same DOI, not replications. **Rights:** 2023 copyright held by owner/authors; publication rights licensed to ACM; paraphrase and citation only, no PDF/screenshots redistributed.

### GDR-SRC-20261010-G02-005

**Microsoft Xbox accessibility team. [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).** Microsoft Learn. Publication/update: V3.2 published 2023-06-08; inspected page last updated 2026-08-14.

Edition/build: V3.2 hub as served 2026-10-10; page date is distinct from guideline-set version. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative platform guidance.

**Inspected locator:** Introduction; Overview of XAG components → Example content; version heading and last-updated footer.

**Claims supported here:** C-06. **Limits:** The introduction explicitly excludes compliance/legal-checklist status; no formal-standard claim is made. **Independence:** Common guidance family with GDR-SRC-20261010-G02-006 and GDR-SRC-20261010-G02-007; not independent empirical studies. **Rights:** Microsoft documentation; paraphrase only, example images not redistributed.

### GDR-SRC-20261010-G02-006

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page.

Edition/build: XAG 107 page within V3.2 set; live page snapshot checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility/input guidance.

**Inspected locator:** Goal; Overview; Background and foundational information → Speed, Complexity, Duration and proposed alternatives; Implementation guidelines → remapping and updated prompts; mobile-input section reviewed for scope only.

**Claims supported here:** C-03, C-06. **Limits:** No game-independent timing, sensitivity, target-size or compliance requirement is inferred; core article text was accessible despite an authorization banner. **Independence:** Same XAG guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-007; cited third-party examples are not additional observations. **Rights:** Microsoft documentation; paraphrase only; embedded example media not inspected as gameplay.

### GDR-SRC-20261010-G02-009

**Nintendo; attributed Metroid Dread development-team transmissions. [Metroid Dread Report Vol. 3: Seven points that define the 2D saga](https://www.nintendo.com/en-gb/News/2021/July/Metroid-Dread-Report-Vol-3-Seven-points-that-define-the-2D-saga-2007780.html).** Nintendo UK. Publication/update: 2021-07-15.

Edition/build: English pre-release report for Nintendo Switch; executable build unspecified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary publisher explanation with creator-attributed intent.

**Inspected locator:** §4 Exploration → Icon Highlight, Marker, Zoom, Hidden item hints and development-team transmission; §5 Arsenal and abilities and following transmission.

**Claims supported here:** C-01, C-08. **Limits:** Describes planned affordances and intent, not observed post-release navigation success, exact topology or universal genre definition. **Independence:** One Nintendo/Metroid account; later reports are related, not independent confirmation. **Rights:** Nintendo copyright; paraphrase only, maps/images not redistributed.

### GDR-SRC-20261010-G02-011

**adamgryu (Adam Robinson-Yu). [A Short Hike](https://adamgryu.itch.io/a-short-hike).** Creator storefront on itch.io. Publication/update: Publication unknown; displayed page update 2026-09-16; listed game release 2019-07-30.

Edition/build: Windows/macOS/Linux creator page; listed downloads differ by platform (Windows/Linux 1.10.1_patched, macOS 1.12.2); none downloaded. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary creator product-description artifact.

**Inspected locator:** Opening description and feature bullets; More information → Genre, Platforms; download version labels.

**Claims supported here:** C-01, C-02, C-09. **Limits:** Evidence of a stated low-pressure exploration promise and creator platformer/adventure labels, not universal audience expectations. **Independence:** Distinct developer context; storefront tags and marketing are not a player-experience study. **Rights:** Creator copyright; paraphrase only, no media redistributed.

### GDR-SRC-20261010-G02-016

**Bennett Foddy (developer and publisher fields). [Getting Over It with Bennett Foddy](https://store.steampowered.com/app/240720/Getting_Over_It_with_Bennett_Foddy/).** Creator-supplied Steam storefront. Publication/update: Page publication/update unknown; listed Steam release 2017-12-06.

Edition/build: Steam desktop description; executable build not inspected. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary creator description artifact.

**Inspected locator:** About This Game → opening climbing description and bullet about repeated loss of progress; developer/publisher fields.

**Claims supported here:** C-09. **Limits:** Evidence of an explicitly punishing stated promise, not measured frustration or proof of precision-platformer genre membership. **Independence:** Independent creator context from Celeste. Foddy’s own website was only a route to this description. **Rights:** Creator/storefront copyright; paraphrase only; satirical numerical language not reproduced as research data.
