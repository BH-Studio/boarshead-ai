---
id: GDR-CAND-20261010-W03-TOP-03
kind: topic
title: World structure and exploration
version: 0.1.0
status: draft
candidate_revision: initial-1
run_id: GDR-FULL-20261010
batch: W03
attempt_id: W03-attempt-1
owner_project: BH-GDR-Worlds-and-Characters
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- world layout
- open-world exploration
- hubs and regions
- backtracking
- re-entry
tags:
- density
- discovery
- revisitation
- optional-routes
- world-structure
related_topics:
- GDR-CAND-20261010-W03-TOP-01
- GDR-CAND-20261010-W03-TOP-02
related_patterns:
- GDR-CAND-20261010-W03-PAT-01
- GDR-CAND-20261010-W03-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-W03-001
- GDR-SRC-20261010-W03-002
- GDR-SRC-20261010-W03-003
- GDR-SRC-20261010-W03-007
- GDR-SRC-20261010-W03-008
- GDR-SRC-20261010-W03-009
- GDR-SRC-20261010-W03-011
reviewer: null
approved_by: null
approved_date: null
predecessor_hash: null
supersedes: null
change_summary: Initial bounded W03 submission; no prior batch artifacts reissued.
hash_receipt: ../reviews/full-run-20261010-w03-artifact-receipt.md
---

# World structure and exploration

> **Research candidate, not released guidance.** Version 0.1.0, candidate revision `initial-1`. Author self-review only; independent evidence review has not occurred. All worked designs and validation protocols below are illustrative or proposed. No W03 game build, prototype, participant session or playtest was executed. External creator accounts are not observations performed by this workspace.

## Decision and scope

**Decision:** how should a world organize destinations, routes, discovery and return so that the scale and travel demands serve the intended experience rather than simply increase its volume?

A **hub** is a place that repeatedly connects activities or routes; a **region** is an area grouped for a meaningful spatial, functional or experiential distinction. An **open world** is treated here as a world with substantial player-directed route or destination choice, not as a required area, content count or absence of all gates. These are working terms for analysis. A small world can offer route choice, and a large world can constrain it; neither description alone establishes quality. [C-01]

**Discovery** can concern noticing a place, reaching it, understanding it or finding a new use for it. **Revisitation** is a return to a previously encountered place; **backtracking** emphasizes retraversing a route. **Re-entry** is resuming after an interruption or absence. Distinguishing these events prevents a newly understood old room from being counted only as recycled content, and prevents a long walk to an unchanged marker from being counted automatically as meaningful exploration. These are analytic possibilities, not measured effects. [C-06; C-07; C-08]

Included: hubs, regions, open-world organization, density, destination choice, optional routes, discovery, return and re-entry. Excluded: progression curves, resource economies, movement tuning, quest-state ownership, streaming, save architecture and game-specific canon. [Level and spatial design](level-and-spatial-design.md) owns local connectivity and legibility; [Environmental storytelling](environmental-storytelling.md) owns interpreting spatial traces. W01, W02, F03 and P03 shared bytes remain missing dependencies.

## Core explanation and mechanisms

### Separate organizational structure from experience

A hub-and-spoke description predicts that several journeys pass through a shared place; it does not predict whether returning is reassuring or tedious. Connected regions may expose multiple destination choices while still requiring a particular condition for a crossing. A broadly open surface can hide a restrictive sequence of meaningful activities. Assess what the player can choose and understand at the relevant moment rather than granting a quality label to a map shape. [C-01; C-07]

The proposed causal chain is **available choices → interpretable possibilities → self-selected investigation → discovery or reconsideration → a valued reason to continue or stop**. The inspected creator sources support the existence of these design concerns. They do not establish every link, and particularly do not demonstrate that this chain is better for every audience than directed progression or unguided wandering. [C-05]

### Density is several questions, not one prescription

The following decomposition is W03's proposed comparison method. It is not a validated index, nor a formula for an optimum. [C-02]

| Dimension | What to describe | Why it changes the decision |
|---|---|---|
| Spatial distribution | Where candidate destinations and activities are placed relative to one another. | Concentration can create choice or obscure differences; distance alone does not say what the journey contains. |
| Travel-adjusted exposure | What a player encounters during an actual route with the chosen movement/access mode. | Equal map spacing may entail very different effort and attention demands. |
| Simultaneous decision demand | How many unresolved possibilities compete at a choice point. | Many available locations need not mean many legible choices. |
| Semantic novelty | Whether a discovery changes a question, relationship or usable understanding. | Repeated activities can add count without adding this kind of novelty. |
| Perceptual load | What competes for perception in the scene or its information displays. | A sparse activity map can still be visually or aurally busy. |

Nintendo's development interview reports that adding sky islands produced clutter, while Robinson-Yu describes a deliberately small world with off-path possibilities. These are counterexamples to a simple production doctrine of maximizing content or area, not evidence that smaller or sparser always wins. The two projects differ substantially; their juxtaposition is not a controlled comparison. [C-03; C-04; GDR-SRC-20261010-W03-008; GDR-SRC-20261010-W03-009]

**Evidence-to-application bridge:** count what matters to the design decision before changing density. A problem of unclear destination identity may call for fewer competing signals, not fewer destinations. A problem of repetitive activities may call for different consequences, not a larger map. A valued long journey may need no extra event. Each is a testable local explanation rather than a library rule. [C-02; C-05; C-11]

### Discovery can change knowledge without changing geography

Record separately what is reachable, what the player has noticed, what the player understands, and what the player currently wants to pursue. A route may have existed throughout but only later become recognizable as useful. Conversely, a visible destination may be correctly understood but not yet reachable. Treating these as the same “unlock” hides different authoring and comprehension questions. This is a conceptual distinction; the missing F03 progression material cannot be silently replaced by this topic. [C-07]

An open question can supply a reason to choose a destination, but not every choice needs a stated question. Some players or local designs may value spontaneous wandering or revisiting a familiar view. Avoid converting all curiosity into a task list or treating every detour as a failure to pursue the authored question. [C-05; C-11]

### Return should be evaluated, not excused by reuse

The proposed return-value question is: **what, for this player in this state, makes returning preferable to a shorter alternative or to stopping?** Candidate reasons include changed access, reinterpreted evidence, changed relationships, recognition from another viewpoint, or pleasure in practiced movement. These are hypotheses. An unchanged passage can be valuable; a changed reward icon can fail to justify a compulsory long trip. [C-06; C-11]

Smith/Worch's suggestion of circular spaces or looking back and Fernández-Vara's treatment of player traces motivate considering revisitation. They do not show that mandatory backtracking outperforms a shortcut or remote review. A local comparison should preserve alternatives rather than define the travel as meaningful by authorial decree. [C-06; GDR-SRC-20261010-W03-002; GDR-SRC-20261010-W03-003]

### Re-entry is a separate information problem

After absence, a player may remember a place but not an intention, or remember an objective but not the route. The proposed aid is a distinction among **observed**, **inferred**, **unresolved** and **chosen next** information, not an automatic solution. A recap that upgrades an uncertain clue into fact creates a continuity error; a map that selects the nearest marker may erase the player's prior goal. Equivalent recovery through the world itself can be preferable when remembering is part of the intended play. [C-08; C-09]

## Design choices and alternatives

These are conditional proposals under C-01/C-02/C-05–C-11, not a ranking of world formats.

| Structure or feature | Useful when | Tradeoff to test | Alternative / omission case |
|---|---|---|---|
| Recurring hub | A common place supports orientation, relationships or choosing among journeys. | Repeated returns can become a service chore or bottleneck. | Distributed services, multiple access points, or no mandatory hub return. |
| Distinct connected regions | Different areas pose understandable choices or traversal conditions. | Boundaries can become arbitrary partitions; similar tasks can flatten distinctions. | A smaller unified world with fewer but meaningful contrasts. |
| Broad destination freedom | Self-direction is a central intended experience. | Arrival order and unresolved possibilities increase authoring uncertainty. | Bounded open areas joined by directed transitions. |
| Compact world | Scope and traversal effort are constrained; revisiting relations matters. | High local competition or repeated views can still overload or fatigue. | More spacing or fewer simultaneous possibilities, not necessarily more content. |
| Extensive low-density world | Travel, distance or solitude may be part of the intended value. | Empty travel can impose unwanted time and access costs. | Optional travel reduction or a shorter world; test rather than rationalize. |
| Return after change | The change is perceivable and relevant to a current or renewed interest. | A new state may not compensate for repeated travel. | Shortcut, remote observation or optional return. |
| Optional branches | Declining a destination is a legitimate choice. | Rewards or completion pressure can make “optional” nominal only. | Clear stopping points and locally honest statements of what can be missed. |
| Re-entry aid | Interruption otherwise requires unwanted reconstruction. | Can reveal a solution or impose an intention the player never chose. | Player notes, environmental reacquaintance or a less explicit recap. |

## Application process

Proposed design/review sequence; no prototype or player test was performed. [C-02; C-05; C-06; C-07; C-08; C-10]

1. **Specify the experience and stopping conditions.** State what makes an excursion worth undertaking and what counts as a satisfying decision to return, change goals or stop. Do not substitute total playtime for value.
2. **Describe the world at the relevant scale.** Identify destinations, routes, hubs, region relationships and conditional access. Use a state description only where it changes a player-facing choice; do not prescribe engine data structures.
3. **Record information states separately.** For each important discovery, distinguish noticed, reachable, understood and selected. Check arriving before the expected context, revisiting after another discovery and skipping an optional area.
4. **Diagnose density.** Determine whether the concern is travel effort, competing choices, perceptual clutter, repeated activity or lack of meaningful questions. Change that dimension rather than adding destinations indiscriminately.
5. **Describe each proposed return's value and cost.** Record what could change and what might make the trip worthwhile even without change. Compare a shorter route, remote review or voluntary omission. Do not assume an extrinsic reward is the only relevant value.
6. **Make optionality and recovery honest.** Describe what is currently known about risk, commitment and return. Design re-entry information that preserves uncertain evidence and player intentions. Coordinate objective tracking and progression with their domain owners.
7. **Propose order-sensitive evaluation.** Use different arrival orders and interruptions where those are part of the actual target context. Keep navigation, comprehension, enjoyment and willingness to continue separate.
8. **Reduce unsupported scope.** Remove a region, return obligation or information system when its maintenance cost exceeds the demonstrated or deliberately chosen value. An approved local aesthetic choice can later justify a tradeoff; this draft itself approves none.

## Patterns and genre adaptations

[Destination-signaled route choice](../patterns/destination-signaled-route-choice.md), `GDR-CAND-20261010-W03-PAT-02`, may support choosing among world destinations without disclosing their contents. [Corroborated spatial inference](../patterns/corroborated-spatial-inference.md), `GDR-CAND-20261010-W03-PAT-01`, may support reconsidering a place when new evidence becomes available. Neither is a complete world-structure recipe.

A separate **changed-context return** pattern is justified as queued child research, not delivered as a third pattern. It needs a decision about mandatory versus optional return, memory and movement dependencies, and a comparison against shorter alternatives. Child key and candidate ID allocation remain pending in coordination.

No genre rules are asserted. “Open-world” is treated as an organizational facet rather than automatically creating a genre file. Applicable genre guidance and the genre template are missing. The same geography could serve very different promises about pace, danger, interpretation or ease of stopping; hybrid conflicts require explicit local decisions rather than an automatic genre winner. [C-01; C-11]

## Examples and counterexamples

### Illustrative worked world: an estuary survey

**Invented for this candidate; no game canon, prototype or participant results.** A ferry shelter connects a reed basin, a hill observatory and a former waterworks. The initial possibilities are identifying the origin of a seasonal stain, inspecting an unusual signal and following an unexplained maintenance route. The player may leave an unresolved question and choose another. [C-05; C-07]

A first trip to the observatory exposes a view of a gate near the waterworks. Seeing the gate does not mean the player knows its purpose or can reach it from that bank. The conceptual world record distinguishes all three. After inspecting the reed basin, the player may recognize the stain at the waterworks as related—or may still regard that relation as uncertain. No automatic record converts the inference into fact.

A later tide change exposes a path. That does not by itself justify forcing a return. The proposed comparison offers a ferry stop nearer the waterworks, a remote view of the newly exposed route, or the original journey. It asks whether participants value the return's changed perspective or simply tolerate it to reach the new information. A player who chooses the familiar long route for its view is not scored as inefficient. [C-06; C-11]

The shelter's optional recap records observations and the player's previously chosen next destination. It does not supply an unvisited solution. After a longer absence, the player can instead walk a familiar short route to reacquaint themselves. Whether either option improves re-entry must be tested. [C-08; C-09]

A **bad expansion** doubles the number of sites but repeats the same clue role at each. Another puts every available site on a single busy display, increasing decision demand without explaining the differences. A smaller revision clarifies the distinction between the existing questions and removes a compulsory service return. These are proposed alternatives, not proven improvements. [C-02; C-05]

### Contrary cases

**Illustrative:** a journey intended to make distance palpable may be weakened by frequent discoveries or automatic travel skipping. A familiar circuit undertaken for practiced movement may not need a new narrative state. Conversely, a repeated route that requires no interesting action may not be rescued by one new collectible. These cases prevent C-06 from becoming “all backtracking is good if something changes” and C-05 from becoming “all empty space is bad.” [C-06; C-11]

The creator accounts provide narrower real-world context: the compact-world rationale is a reported design choice, and the sky-clutter problem is a reported production tension. W03 did not play these builds, compare their maps or measure their audiences; their commercial visibility is not causal evidence. [C-03; C-04]

## Failure modes and constraints

**Overload disguised as freedom.** A world can offer many destinations while withholding the grounds for choosing among them. The opposite error is labeling everything so completely that investigation becomes merely following a menu. Offer the information relevant to the intended choice, and test both insufficient information and excessive disclosure. [C-02; C-05]

**Access and time burden.** A route's cost differs with movement and access modes. Do not assume that a scenic but effortful return has equal value for everyone, or that a visual overview provides all needed world information. Alternate presentation should preserve relevant choices without declaring one of them the proper choice. XAG 103 supports the general need for access to important cues, not a universal design for exploration. [C-09; GDR-SRC-20261010-W03-011]

**Localization and continuity.** Region names, landmark references and recap descriptions need to remain referentially consistent. Uncertain testimony should remain uncertain in translation. A recap must distinguish what the player observed from what the world author knows. These are proposed review checks; no multilingual re-entry study was inspected. [C-08; C-10]

**Ethics and optionality.** Treat declining a detour and ending an excursion as valid possibilities where the design claims freedom. Do not call a route optional solely because a menu permits omission while the design's essential access depends on completing it. This is a proposed distinction between formal availability and practical consequence, not a universal prohibition on costly choices. Respectful local goals still require explicit studio decisions. [C-07; C-09]

**Production scope.** New places add more than assets when they affect earlier interpretations, routes and arrival orders. The risk review should examine those dependencies without inventing a numerical combinatorial cost estimate. A maintained region with meaningful relationships can be more feasible than a larger one, but feasibility and audience value are separate questions. Runtime responsibilities remain outside W03. [C-10]

## Playtest and validation

**Status: proposed; not performed.** No world build, participants, telemetry or results. The following comparisons are separately scoped options; they are not a claim that a comprehensive experiment has been run or powered.

**Density/discovery comparison.** Compare arrangements with the same important questions but different spacing or simultaneous exposure. Do not change activity novelty, movement effort and map information at the same time unless the goal is explicitly to evaluate the whole package. Obtain participants' reasons for choosing destinations and for stopping. Measure understood options, unanswered questions that still interest them, perceived clutter, unwanted travel and satisfaction with self-selected excursions. Reject C-05 for the local goal when question-oriented organization adds cognitive work without valued agency, or when unstructured wandering is the preferred outcome. [C-02; C-05; C-11]

**Return-value comparison.** Compare unchanged return, a perceptible relevant change and a shorter or remote alternative. Keep later information and reward access comparable. Use fresh participants or counterbalanced analogous places to reduce familiarity confounds. Record voluntary return, what change was recognized, the reason the trip felt worthwhile or wasteful, and whether the shorter option removed valued travel. Reject a mandatory-return recommendation when the same valued understanding is available through a preferred lower-cost alternative. Preserve unchanged travel when participants independently value it; do not assume that novelty is the only success measure. [C-06; C-11]

**Re-entry comparison.** After a locally relevant interruption, compare an observation/intention recap, ordinary environmental reacquaintance and the current baseline. Keep uncertain facts uncertain. Ask the player to resume a self-chosen plan without prompting an optimal answer. Measure recovery of prior intention, mistaken certainty, spoiler exposure, navigation burden and satisfaction with remembering. Reject or simplify the recap when it imposes a plan, reveals solutions or provides no useful recovery. [C-08]

**Participants and decision criteria.** Include the intended session patterns, language backgrounds, navigation experience, access modes and interruption circumstances. Motion tolerance, locomotion preference, reading demand, destination familiarity and attachment to a place can change the result. Predefine a meaningful local improvement and an unacceptable loss in the target experience before testing. Avoid an invented optimal content density, return-time ceiling or universal preference. Unresolved results remain unresolved rather than proving the biggest, smallest, clearest or most populated world best.

## Claim ledger

Claim IDs are local to this file. Confidence refers to the specified claim, not to universal effectiveness. “None” in the evidence column means an explicitly proposed design hypothesis, not an omitted citation.

| Claim | Precise claim / class | Evidence and contrary context | Scope, confidence and unresolved question |
|---|---|---|---|
| <a id="c-01"></a>C-01 | **`inference`** — Hub, region and open-world labels describe aspects of a world’s organization, not guaranteed player experiences or measures of quality. | W03 working definitions; the creator accounts in GDR-SRC-20261010-W03-007/GDR-SRC-20261010-W03-008/GDR-SRC-20261010-W03-009 supply contrasting contexts, not a formal taxonomy. | High for the distinction between description and outcome; proposed vocabulary, not canonical library taxonomy. |
| <a id="c-02"></a>C-02 | **`inference`** — Spatial content density, travel-adjusted exposure, simultaneous decision demand and semantic novelty should be distinguished before comparing worlds. | W03 analytic decomposition. GDR-SRC-20261010-W03-009 motivates a clutter question, but supplies no universal density metric. | Moderate as a decision tool. No validated combined exploration-quality score or optimum density is established. |
| <a id="c-03"></a>C-03 | **`practitioner-heuristic`** — Robinson-Yu describes deliberately building a small open world that accommodates departures from the obvious route, under largely solo production constraints. | GDR-SRC-20261010-W03-008, freedom/off-path paragraphs and “For the most part” paragraph. | High for the creator account; no comparative size experiment, observed player outcome or commercial-causality inference. |
| <a id="c-04"></a>C-04 | **`practitioner-heuristic`** — Nintendo’s interview reports excessive sky-island clutter during development and describes familiar terrain reconsidered through caves. | GDR-SRC-20261010-W03-009, opening world/cave discussion and sky-island question. | High for the reported production tension. Neither optimal density nor improved player exploration is measured by the account. |
| <a id="c-05"></a>C-05 | **`hypothesis`** — A world may support purposeful exploration more effectively by sustaining intelligible open questions than by maximizing discoverable objects or traversable area. | Proposed application bridge from GDR-SRC-20261010-W03-007, pathing goal, and GDR-SRC-20261010-W03-008, compact-world design. No matched experiment inspected. | Low comparative confidence; aimless wandering, spectacle or exhaustive collection may be the intended experience instead. |
| <a id="c-06"></a>C-06 | **`hypothesis`** — A revisit may earn its travel cost when the player can perceive a relevant change in access, knowledge, state, perspective or practiced skill; a new reward is neither necessary nor sufficient. | GDR-SRC-20261010-W03-002, pp.71–74; GDR-SRC-20261010-W03-003, PDF pp.10–11; GDR-SRC-20261010-W03-009, familiar-terrain discussion. These motivate the comparison, not its causal benefit. | Low efficacy confidence. Unchanged travel can be valued; changed travel can still be tedious. Optional shortcuts and remote reconsideration are alternatives. |
| <a id="c-07"></a>C-07 | **`inference`** — Physical access, recognition of an opportunity and understanding how to use it are different discovery states; a knowledge-dependent route is not necessarily a newly unlocked route. | W03 conditional-access reasoning; related conceptual basis in GDR-SRC-20261010-W03-001, Embedded Narratives. F03 progression and W02 objective content remain missing. | Moderate conceptual confidence; no claim that a named game proves a knowledge-gating recipe. |
| <a id="c-08"></a>C-08 | **`hypothesis`** — A re-entry aid that separates observed facts, unresolved questions and chosen intentions may reduce avoidable reconstruction after absence without necessarily revealing solutions. | W03 proposal; conceptual basis in GDR-SRC-20261010-W03-001, Embedded Narratives, and GDR-SRC-20261010-W03-003, player traces. No interrupted-play comparative study inspected. | Low. An aid can spoil discovery, misrepresent uncertain evidence or substitute for a valued act of remembering. |
| <a id="c-09"></a>C-09 | **`inference`** — Exploration choices should remain available through relevant access modes; alternate information delivery and optional assistance should not automatically select the player’s preferred destination. | Application of GDR-SRC-20261010-W03-011, important-cue guidance, to the choice problem in GDR-SRC-20261010-W03-007. | Moderate logical confidence, low for equivalent exploration experience. Not platform certification or an approved local accessibility specification. |
| <a id="c-10"></a>C-10 | **`inference`** — World-structure production review should include combinations of arrival order, changed access and player knowledge, not only count locations and assets. | W03 state/knowledge reasoning from C-06/C-07; GDR-SRC-20261010-W03-007, final question, explicitly leaves broad order effects to future testing. | Moderate as a risk review. No runtime architecture, test-count formula or content-cost multiplier is claimed. |
| <a id="c-11"></a>C-11 | **`hypothesis`** — Low-density or unchanged travel may be worth retaining when the intended value is orientation, solitude, anticipation or practiced movement rather than frequent novelty. | W03 contrary hypothesis to C-05/C-06; no direct empirical support inspected for these outcomes. | Low. Requires local evidence; it must not be used as an unfalsifiable excuse for empty space or imposed repetition. |

## References

All source identities below are temporary W03 identities. Access date: **2026-10-10**. URL/DOI/edition deduplication across batches is pending Library Coordination. Source access does not imply game observation or evidence approval.

### GDR-SRC-20261010-W03-001

**Henry Jenkins.** *Game Design as Narrative Architecture*. electronic book review. Publication/update: 2004-07-10 in the article heading; the page also displays 2004-05-03 in surrounding metadata, unresolved.

- Verified source: [Game Design as Narrative Architecture](https://electronicbookreview.com/publications/game-design-as-narrative-architecture/).
- Edition/build: HTML essay, unnumbered online edition. Access: `relevant-excerpt`.
- Precise inspected locators: Opening qualifications; Spatial Stories and Environmental Storytelling; Embedded Narratives, especially paragraphs beginning “Russian formalist critics”, “Read in this light” and “Within an open-ended”; Emergent Narratives.
- Type and independence: Primary scholarly conceptual argument, not a participant study. Fernández-Vara explicitly engages this conceptual tradition. Works quoted by Jenkins were not thereby inspected; they are not additional sources.
- Claims in this entry: C-07, C-08.
- Limits: Historical theoretical vocabulary and examples do not establish an experimental effect or a universal clue count.
- Rights: Copyrighted essay; limited paraphrase only; no reproduced figures or underlying works.

### GDR-SRC-20261010-W03-002

**Harvey Smith and Matthias Worch.** *What Happened Here? Environmental Storytelling*. Game Developers Conference / GDC Vault. Publication/update: 2010, GDC; exact session day not established.

- Verified source: [What Happened Here? Environmental Storytelling](https://media.gdcvault.com/gdc10/slides/Smith_Harvey_WhatHappenedHereWeb_Notes.pdf).
- Edition/build: 84-page Web Notes PDF; printed page numbers equal 1-based PDF pages. Access: `relevant-excerpt`.
- Precise inspected locators: pp.16–18 definition; pp.28–30 interpretation; p.45 relational staging; pp.57–62 implied interaction; pp.71–74 returning to player traces. Screenshots inspected for pp.16, 28, 30, 45 and 72; p.29 screenshot unavailable, text accessible.
- Type and independence: Firsthand practitioner presentation; affiliations on session materials are Arkane Studios and LucasArts. One joint account, not two independent findings. Fernández-Vara discusses it. The speakers’ attribution to Jordan Thomas is second-hand within this account.
- Claims in this entry: C-06.
- Limits: Advice and speaker interpretations; no participant dataset or measured causal benefit is supplied by the passages used.
- Rights: Copyrighted talk and third-party game imagery; no slides, screenshots or substantial extracts redistributed.

### GDR-SRC-20261010-W03-003

**Clara Fernández-Vara.** *Game Spaces Speak Volumes: Indexical Storytelling*. Proceedings of DiGRA 2011 Conference: Think Design Play. Publication/update: 2011; the catalog’s January 1 date is not treated as a verified presentation day.

- Verified source: [Game Spaces Speak Volumes: Indexical Storytelling](https://dl.digra.org/index.php/dl/article/view/512).
- DOI: [10.26503/dl.v2011i1.512](https://doi.org/10.26503/dl.v2011i1.512).
- Inspected manuscript route: [author-manuscript mirror](https://se4n.org/papers/fernandez-vara.pdf); [MIT provenance metadata](https://dspace.mit.edu/entities/publication/a2925ff9-0a0f-4dba-9ae4-a18173fa9f82).
- Edition/build: Author’s final manuscript with MIT wrapper; 14 PDF pages. Locators below use 1-based PDF pages, including wrapper. Access: `relevant-excerpt`.
- Precise inspected locators: PDF p.3 Environmental Storytelling; p.5 argument before Indexical Storytelling: Definition and that definition; pp.5–6 Indexical Storytelling in Practice; p.8 Interpretation of Remains; pp.10–11 History of the Player: Player’s Traces. PDF p.5 screenshot inspected.
- Type and independence: Primary scholarly conceptual argument in an author-manuscript mirror. Explicitly builds on and critiques Jenkins and Smith/Worch; not independent experimental corroboration. Publisher/MIT metadata inspected; publisher PDF and MIT download routes failed; mirror byte equivalence to repository copy not verified.
- Claims in this entry: C-06, C-08.
- Limits: Text available through a weaker provenance route; analyses of games remain the author’s analyses, not direct W03 gameplay observations.
- Rights: Manuscript states ©2011 authors/DiGRA and permission conditions; only limited attributed paraphrase used, no manuscript or images included.

### GDR-SRC-20261010-W03-007

**Mobius Digital; interview with creative director Alex Beachum, interviewer uncredited.** *The Intentionality of Wandering*. Mobius Digital development blog. Publication/update: 2016-08-18.

- Verified source: [The Intentionality of Wandering](https://www.mobiusdigitalgames.com/news/the-intentionality-of-wandering).
- Edition/build: HTML Q&A about in-development Outer Wilds; no exact build identified. Access: `full`.
- Precise inspected locators: Article Q&A only: opening pathing reassessment; “What in the course of production or playtesting…”; “So how do you balance…”; final “Now that we’re finetuning design…”; unrelated comments excluded.
- Type and independence: Firsthand creator interview about design changes and anticipated testing. One studio account. Any later Outer Wilds talks are not additional inspected support in this packet.
- Claims in this entry: C-01, C-05, C-09, C-10.
- Limits: 2016 development context, not an observed 2019 retail build; reported playtesting has no methods/sample/effect data here; broad free-roaming tests are described as upcoming.
- Rights: Copyrighted developer post; paraphrase only; no images or comments copied.

### GDR-SRC-20261010-W03-008

**Adam Robinson-Yu, developer, Whippoorwill.** *Crafting a tiny open world: A look behind the scenes at the creation of A Short Hike*. PlayStation.Blog. Publication/update: 2021-08-05.

- Verified source: [Crafting a tiny open world: A look behind the scenes at the creation of A Short Hike](https://blog.playstation.com/?p=351732).
- Edition/build: HTML creator article announcing a forthcoming PS4 version; no exact gameplay build inspected. Access: `relevant-excerpt`.
- Precise inspected locators: Paragraph beginning “To help create a sense of freedom”; following off-path activities; paragraph beginning “For the most part” about solo production.
- Type and independence: Firsthand creator account published by platform holder. Different production from Mobius/Nintendo. GDC postmortem not counted as another inspected source.
- Claims in this entry: C-01, C-03, C-05.
- Limits: Intent and production rationale, not independently measured enjoyment, optimal size or player preference.
- Rights: Copyrighted article and media; attributed paraphrase only; embedded video not viewed.

### GDR-SRC-20261010-W03-009

**Nintendo; developer interview, relevant speakers Fujibayashi, Takizawa, Dohta and Aonuma.** *Ask the Developer Vol. 9, The Legend of Zelda: Tears of the Kingdom – Chapter 3*. Nintendo Australia. Publication/update: 2023-05-11.

- Verified source: [Ask the Developer Vol. 9, The Legend of Zelda: Tears of the Kingdom – Chapter 3](https://www.nintendo.com/au/news-and-articles/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-chapter-3/).
- Edition/build: Official English interview translated from Japanese; some displayed material identified as in-development. Access: `relevant-excerpt`.
- Precise inspected locators: Opening questions on reusing the world and cliffside caves; question “Thinking about how to get to the floating sky islands seems fun”, answers on island clutter and scale.
- Type and independence: Firsthand production interview, promotional publisher context. Separate production account from sources 007 and 008; multiple speakers are not independent player experiments.
- Claims in this entry: C-01, C-02, C-04, C-06.
- Limits: Reported design tensions, not controlled density comparison, optimal island count or verified player reinterpretation outcome.
- Rights: Nintendo copyright; no images or audiovisual media reproduced.

### GDR-SRC-20261010-W03-011

**Microsoft.** *Xbox Accessibility Guideline 103: Additional channels for visual and audio cues*. Microsoft Learn. Publication/update: Last updated 2026-03-04; checked 2026-10-10.

- Verified source: [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).
- Edition/build: Unnumbered current web guideline; old /gaming/ path redirects to /xbox/. Access: `relevant-excerpt`.
- Precise inspected locators: Goal; Overview; Implementation guidelines on important visual/audio information, shapes/location, and color; last-updated footer.
- Type and independence: Official platform accessibility guideline; classified practitioner-heuristic here, not a formal standard or legal mandate. Guideline, not an independent player dataset. External linked guidance not treated as inspected.
- Claims in this entry: C-09.
- Limits: Full relevant public text accessible despite authorization chrome. Does not certify a design or supply universal size/contrast settings; recheck before platform implementation.
- Rights: Microsoft content; limited paraphrase, no embedded images; redistribution terms not separately audited.

## Coverage, open questions and change history

| Assigned subtopic | Researched coverage | Unresolved / next discriminating question | Review state |
|---|---|---|---|
| Hubs, regions and open worlds | Working structural distinctions and conditional alternatives. | No directly comparative structural efficacy study inspected. Which choices does the structure actually support? | Author draft; independent review pending. |
| Density | Separates spatial, temporal, decision, semantic and perceptual questions. | Creator clutter account does not establish an optimal count or interval. | Same. |
| Discovery and optional routes | Distinguishes noticed/reachable/understood/chosen; route-choice bridge. | No proof that question-driven exploration always exceeds wandering or directed play. | Same. |
| Revisitation/backtracking | Candidate reasons, contrary unchanged-travel case, shortcut/remote comparisons. | Changed-context return requires child research and missing mechanics/continuity dependencies. | Same. |
| Re-entry | Proposed observation/intention distinction and comparative protocol. | No direct interrupted-play outcome evidence inspected. | Same. |
| Access/localization/production | Risk and dependency review rather than imported settings or architecture. | Relevant reviewed shared guidance and representative validation missing. | Same. |

Missing shared content: W01 narrative/world/character reviewed-candidate bytes; W02 dialogue/quests/lore submissions; F03 progression/resources; movement/traversal and session/re-entry guidance; P03 camera/platform and relevant Presentation access/map guidance. Their statuses are reported only as supplied by the dispatch, not independently reconstructed. Disputes `W03-CON-01`, `W03-CON-04`, `W03-CON-05` are tracked in the [review packet](../reviews/full-run-20261010-w03-review-packet.md).

**History:** 2026-10-10 — initial 0.1.0 / `initial-1`, no predecessor or superseded artifact. No new genre entry, no child namespace allocated, no independent review or release. Exact bytes appear in the [artifact receipt](../reviews/full-run-20261010-w03-artifact-receipt.md).

**Next decision:** independent Gate C review should challenge C-06 using a context that values unchanged travel and a context where changed travel remains tedious. Then decide whether changed-context return warrants a registered child batch rather than expanding this two-pattern packet.
