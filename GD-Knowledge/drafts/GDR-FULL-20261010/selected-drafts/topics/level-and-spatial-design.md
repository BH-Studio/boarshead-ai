---
id: GDR-CAND-20261010-W03-TOP-02
kind: topic
title: Level and spatial design
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
- level topology
- wayfinding
- spatial legibility
- landmarks
tags:
- paths
- sightlines
- gating
- flow
- spatial-literacy
related_topics:
- GDR-CAND-20261010-W03-TOP-01
- GDR-CAND-20261010-W03-TOP-03
related_patterns:
- GDR-CAND-20261010-W03-PAT-01
- GDR-CAND-20261010-W03-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-W03-004
- GDR-SRC-20261010-W03-005
- GDR-SRC-20261010-W03-006
- GDR-SRC-20261010-W03-007
- GDR-SRC-20261010-W03-010
- GDR-SRC-20261010-W03-011
reviewer: null
approved_by: null
approved_date: null
predecessor_hash: null
supersedes: null
change_summary: Initial bounded W03 submission; no prior batch artifacts reissued.
hash_receipt: ../reviews/full-run-20261010-w03-artifact-receipt.md
---

# Level and spatial design

> **Research candidate, not released guidance.** Version 0.1.0, candidate revision `initial-1`. Author self-review only; independent evidence review has not occurred. All worked designs and validation protocols below are illustrative or proposed. No W03 game build, prototype, participant session or playtest was executed. External creator accounts are not observations performed by this workspace.

## Decision and scope

**Decision:** how should routes, visible relationships and access conditions make a space understandable enough for its intended choices while preserving any deliberate uncertainty?

This candidate separates **topology** (places and connections), **geometry** (their shape and arrangement), **information exposure** (what is available from a viewpoint or access mode), and **spatial literacy** (what the player can usefully recognize, predict or reconstruct). A loop on a diagram is a descriptive fact. It is not evidence that players recognize the loop, know which direction to take, or enjoy its use. These are working analytic distinctions, not a standard spatial-design taxonomy. [C-01]

A **path** is a traversable connection under specified conditions. A **sightline** is an opportunity to see across space, not necessarily to travel through it. A **landmark** is a reference that a player can distinguish and use; an expensive distinctive asset is only a candidate landmark until that use is established. A **gate** changes access under a condition. **Flow** is used here for the intended rhythm of movement, attention and choice, not as a synonym for maximum speed or for a validated psychological flow state. [C-01; C-08; C-11]

Included: local topology, sightlines, landmarks, paths, conditional gating, route selection and spatial learning. Excluded: locomotion tuning, combat balance, camera implementation, platform compliance, real-building safety and engine architecture. [Environmental storytelling](environmental-storytelling.md) owns the interpretation of traces; [World structure and exploration](world-structure-and-exploration.md) owns region-level discovery and return structure. Foundations movement/progression and Presentation camera/platform/input references are dependencies, not silently imported guidance.

## Core explanation and mechanisms

### A readable connection is more than a line on a map

The following model is a W03 synthesis for diagnosing a design, not an empirically validated sequence. [C-01; C-07; C-08; C-12]

| Proposed link | What the designer can specify | What still needs evidence |
|---|---|---|
| Connection exists | Reachability from a specified start and state. | Whether players perceive the connection or understand its directionality. |
| A reference is distinguishable | Location, form, name and alternate presentation. | Whether it is recognized under actual viewing/access conditions and remembered later. |
| Reference implies a useful relation | Which path approaches it, which fork it identifies, what destination it labels. | Whether the player infers the intended relationship rather than an equally plausible one. |
| Player can select a route | Information about destination, cost or uncertainty relevant to a goal. | Whether the selection reflects the goal rather than salience, habit or random choice. |
| Learning supports later use | Opportunities to return or choose from a new start. | Whether route familiarity generalizes to orientation or relations among places. |

A distant tower might help identify a broad direction but fail to reveal an accessible entrance. A nearby sculpture might identify a turn while offering no useful bearing after the player leaves the room. These are **illustrative roles**, not claims that distal or local landmarks are universally superior. The relevant question is what relationship the player must use at this moment. [C-01; C-07]

### Empirical support is narrower than “landmarks work”

Sharma et al. recruited 35 adults, predominantly male engineering students aged 21–30; five withdrew because of immersive-maze discomfort and 30 continued. The task used an Oculus DK2, joystick and available map. Results identify lower repeated-path proportion and lower average map-view time in the landmark condition. Table 1 does not mark total navigation time as significantly different. Do not upgrade the abstract's broader wording into a demonstrated significant total-speed benefit. The funding corrigendum adds no new behavioral evidence. [C-02; C-03; GDR-SRC-20261010-W03-004; GDR-SRC-20261010-W03-005]

Cheng et al. analyzed 48 of 49 recruits aged 18–35 in map-assisted VR navigation. The manipulation was three, five or seven landmarks **distributed along a route**, with map consultation events—not that many world landmarks visible at once. The reported recognition/route-learning gains did not continue significantly from five to seven; navigation time and the survey-knowledge task did not show significant differences. One route-result confidence interval does not contain its reported coefficient, so W03 does not use that line as precise effect-size support. [C-04; GDR-SRC-20261010-W03-006]

**Application bridge:** these studies justify distinguishing navigation behaviors and kinds of spatial learning, and investigating whether reference cues help a local task. They do not choose a universal landmark count or show that better route memory improves mystery, exploration, accessibility or enjoyment. They also do not establish equivalence between landmarks physically placed in a maze and landmarks represented during map events. Absence of a significant difference is not proof that an effect is absent. [C-05]

### Legibility and uncertainty can concern different information

Beachum's 2016 development account motivates a narrower intervention: signaling the destination of a path where curiosity-motivated choice was the goal. The account anticipates broader testing rather than proving the change worked in a released game. W03's proposed separation is between **where a route goes**, **what effort or condition it requires**, and **what will be understood on arrival**. Revealing one does not logically require revealing all three. Whether that separation preserves mystery is an untested design hypothesis. [C-06; C-07; GDR-SRC-20261010-W03-007]

### Gating is a player-facing conditional relation

For each proposed gate, record its current access state, the condition that can change access, and the grounds the player has for predicting that condition. A visible stair behind glass is not a traversable connection. A door opened from the far side is a directional connection before it becomes a shortcut. A destination reached through understanding an existing route differs from one requiring a new capability. Keep these distinctions in conceptual diagrams and design notes; the actual mechanical rule belongs with Foundations. [C-08]

## Design choices and alternatives

The table presents proposed tradeoffs rather than universally ranked options. [C-01; C-07; C-08; C-11]

| Option | Conditional purpose | Cost or failure to test | Alternative / when to omit |
|---|---|---|---|
| Directed sequence | Encounter order matters or early route decisions would add irrelevant work. | Can feel restrictive; sequence alone does not make the route comprehensible. | A short loop or a meaningful optional spur. |
| Branches that rejoin | Offer a local route choice without permanently separating later content. | Choice can feel cosmetic when route differences do not matter to the intended goal. | One stronger route rather than several nominal choices. |
| Loop | Support recognition, a new approach or later reuse. | Players may fail to notice reconnection; repeated passage can become compulsory labor. | A clear return connection or remote revisit. |
| Distal reference | Support broad orientation or anticipation of a destination. | Viewpoint, occlusion and perceived reachability can invalidate the implied route. | A local reference, map, naming system or optional guidance. |
| Local decision cue | Identify a fork or access condition at the point of choice. | Too late for planning; similar cues can be confused across areas. | Earlier destination information with confirmation at the fork. |
| Conditional gate | Organize access around a meaningful changed condition. | Players may misread permanent closure as “not yet,” or vice versa. | Remove the gate, explain the state, or provide an alternate route. |
| Deliberate disorientation | Not knowing one's route is itself part of the intended challenge. | May test unavailable sensory access or impose costs outside the agreed challenge. | Preserve uncertainty about outcomes while offering optional orientation. |

## Application process

This procedure is proposed; no level prototype or graph execution was performed. [C-01; C-07; C-08; C-11; C-12]

1. **Name the intended route decision.** Is the player finding an exit, choosing a destination, learning a loop, scouting a risk, or deliberately getting lost? Identify what should be uncertain and what should not.
2. **Describe connectivity independently of the picture.** List areas, connections, directionality and access conditions. Check the return path as well as the outward path. Do not infer connection from visible proximity.
3. **Describe information from actual approaches.** For each choice point, note what can be seen or otherwise perceived, when the destination can be recognized, and which detail identifies the correct relation. Include opposite approaches and altered states.
4. **Choose the minimum useful reference.** Select a cue for a specific job: locating oneself, selecting a destination, remembering a turn or understanding a gate. Avoid adding landmarks merely to satisfy a count.
5. **Audit cue implications.** Does a visible structure imply a direct route that does not exist? Does a bright doorway suggest access that is permanently absent? Correct the implication or make the distinction learnable.
6. **Provide an appropriate access route.** Coordinate alternate channels and optional assistance. A guidance mode should state its target and should not silently decide which optional goal the player ought to pursue.
7. **Propose tests that separate performance from learning.** A first completion, return from a different start, and orientation after interruption address different outcomes. Pair them with the intended subjective experience instead of presuming speed is success.
8. **Revise or simplify.** When a route is consistently misread, choose among changing topology, exposure, vocabulary, gate information or assistance. Abandon a clever layout when maintaining its premise is costlier than the player-facing value it creates.

## Patterns and genre adaptations

[Destination-signaled route choice](../patterns/destination-signaled-route-choice.md), `GDR-CAND-20261010-W03-PAT-02`, addresses a fork whose alternatives should be chosen intentionally. It does not apply automatically when discovery of the route's destination is the intended puzzle. [Corroborated spatial inference](../patterns/corroborated-spatial-inference.md), `GDR-CAND-20261010-W03-PAT-01`, is relevant only when a route also exposes evidence about events or relationships.

No genre-specific file or numeric camera/input recommendation is imported. Genre guidance and P03 camera/platform bytes are unavailable; G02 submitted genre work is not inspected shared knowledge. A goal of reliable transport, a goal of uncertainty and a goal of spatial mastery may require different information. Resolve their conflict in the local design, not by declaring one genre label dominant. [C-07; C-11]

## Examples and counterexamples

### Illustrative worked layout: the tidal archive

**Invented, not a built level.** A public courtyard connects to an upper reading room by an exposed stair and to a service gallery by a sheltered ramp. The reading-room windows overlook the courtyard, but they are not entrances. The service gallery later connects to the reading room through a door that opens from the reading-room side. A maintenance closure can block the ramp. [C-01; C-08]

The initial conceptual record distinguishes the existing routes from the visible but impassable window and from the future shortcut. At the courtyard fork, a recognizable roof identifies the reading room while a tactile/visual directory and optional spoken description identify the destinations of both routes. The ramp notice describes the current closure, not a generic lock icon that could mean any prerequisite. The route choice remains about exposure, shelter and destination; nothing tells the player what a document upstairs contains. [C-07; C-09]

At the upper landing, the courtyard below can help recognize reconnection, but that is only a hypothesis. A new arrival through the service route may not recognize the view. The proposed test therefore includes both approaches and an interruption before returning. A bad revision adds several unrelated towers to make the skyline “more readable.” Another makes the roof brighter while leaving the entrance relationship misleading. A simpler revision moves the directory to where both route entrances can be understood. [C-05; C-12]

### Counterexample: a deliberately unnamed passage

**Illustrative.** The local question is whether a player will investigate a passage whose destination is unknown. Labeling it with the answer removes the question. Instead, communicate that entering is reversible and distinguish it from an inaccessible wall, while withholding the destination. This rejects full destination signaling without requiring an inaccessible or arbitrary interface. [C-07; C-08]

### Documented alternative, not measured efficacy

Naughty Dog's 2020 feature account supplies a concrete alternative to relying only on environmental sightlines: navigation assistance can target story progression or, with Enhanced Listen Mode, a recently scanned item or enemy. This is an official feature description, not a W03 observation, a blanket optional-destination interface, or proof that such assistance preserves every game's exploration goal. [C-10; GDR-SRC-20261010-W03-010]

## Failure modes and constraints

**Access and presentation.** Color differences, small details and distal silhouettes are not equivalent access channels. XAG 103 motivates alternate delivery of important information; it does not select this project's distances, contrast values, audio parameters or camera settings. Coordinate sensory, motor and cognitive access with Presentation. Do not treat route assistance as a reward withheld until repeated failure. That last recommendation is a proposed agency-oriented choice, not a formal compliance rule. [C-09; C-12; GDR-SRC-20261010-W03-011]

**Localization and naming.** A name must support the distinction it is used for. A destination's translated name, sign, map entry and spoken reference should identify the same place. Avoid depending on a wordplay or reading direction that changes the route implication in another language. Names can support reference while increasing reading demand; non-text recognition can support reference while depending on cultural familiarity. Evaluate rather than assume either is universal. [C-12]

**Production and state coverage.** Viewpoint, lighting conditions, unlocked shortcuts and changed traversal abilities can change cue usefulness without changing the apparent map. Reused landmark assets can introduce aliasing. These are risks to review, not claims that any specific runtime system causes them. The handoff should specify player-visible access and recognition requirements; camera implementation and locomotion constraints remain unresolved dependencies. [C-01; C-08; C-12]

**False measures of success.** Fast arrival may reflect following an instruction, not learning the layout. Taking a detour may be deliberate investigation, not error. A sketch map can capture a relationship without accurately depicting metric distance. Define the required outcome before interpreting a measure. The inspected studies' differing memory and time outcomes make substituting one for another especially unwarranted. [C-01; C-05; C-11]

## Playtest and validation

**Status: proposed; not performed.** No participants, prototype or results. These are separate candidate tests, not an executed factorial study or a sample-size recommendation.

**Test A — destination information.** Compare a fork with destination-relevant information against a matched fork without it; keep destination content, paths, travel effort and cue visibility otherwise stable. A third, more explicit cue can probe spoiler cost. Use novel layouts or fresh participants to avoid remembered destinations. Before departure, obtain a non-leading account of the intended destination and expected route, then compare the actual choice with that intent. Record uncertainty, surprise and interest after arrival. Reject C-07 locally when signaling improves neither intentional selection nor the desired experience, or makes discovery unacceptably predictable.

**Test B — spatial learning rather than completion.** After an initial route, ask participants to return from another approach or describe relations among places. Separate turn recognition, route choice and survey-like judgments. Match exposure time and avoid rewarding the shortest route unless that is the intended goal. Record assistance use and the reason for detours; do not score purposeful exploration as failure. Reject an inference of general spatial literacy when only the practiced turn sequence improves. [C-01; C-05]

**Test C — conditional access and re-entry.** Present a changed gate state and a return after a locally meaningful interruption. Ask what is reachable now, what would change that, and what evidence supports the answer. Include opposite approaches and relevant access modes. Correct the design when reasonable readings imply the wrong prerequisite or when the necessary relationship is unavailable in an access mode. [C-08; C-12]

**Participants, measures and confounds.** Plan for the actual devices and audience, including navigation experience, motion tolerance, vision/hearing access, chosen assistance and language. Measure warranted route predictions, unintentional reversals, time only where meaningful, recall after interruption and player-defined value of wandering. Camera comfort, motor effort, novelty, signage literacy and attractive scenery are confounds. Set a locally meaningful success/rejection threshold and review adverse outcomes before recruitment; no numerical universal is supplied. No claim about all players may be inferred from the narrow young-adult samples in the inspected studies.

## Claim ledger

Claim IDs are local to this file. Confidence refers to the specified claim, not to universal effectiveness. “None” in the evidence column means an explicitly proposed design hypothesis, not an omitted citation.

| Claim | Precise claim / class | Evidence and contrary context | Scope, confidence and unresolved question |
|---|---|---|---|
| <a id="c-01"></a>C-01 | **`inference`** — A connectivity description, its spatial realization, the information available from a viewpoint, and a player’s learned understanding are different objects of analysis. | W03 analytic distinction. Sources GDR-SRC-20261010-W03-004 and GDR-SRC-20261010-W03-006 motivate separate performance/memory measures; neither validates every graph measure as a comprehension proxy. | High for the logical distinction; low for predicting comprehension from map structure alone. |
| <a id="c-02"></a>C-02 | **`empirical-evidence`** — In Sharma et al.’s virtual maze, reported significant behavioral differences favoring landmarks concern repeated-path proportion and average map-view time, not a demonstrated significant reduction in total navigation time. | GDR-SRC-20261010-W03-004, Methods: Behavioral Measures; Results: Behavioral Outcome and Table 1. Thirty of 35 recruits continued after five discomfort withdrawals. | Moderate for the narrow reported pattern. Initial groups 17/18 precede attrition; final group sizes are not supplied in the passages used. Map aid existed in both conditions; enjoyment was not measured. |
| <a id="c-03"></a>C-03 | **`empirical-evidence`** — The inspected 2017 corrigendum adds a funding attribution and states that conclusions are unchanged; it contains no new outcome data. | GDR-SRC-20261010-W03-005, correction paragraph; linked to GDR-SRC-20261010-W03-004. | High for the correction’s content. It is neither replication nor independent verification of the statistical results. |
| <a id="c-04"></a>C-04 | **`empirical-evidence`** — Cheng et al. report improved landmark/route learning from three to five route-distributed map landmarks, no further significant gain from five to seven, and no significant navigation-time or survey-task main effect. | GDR-SRC-20261010-W03-006, §§2.1–2.7; §3 opening and §3.1. 49 recruited, 48 analyzed. | Moderate for the reported task-specific pattern; low for transfer to game-world density. §3.1 contains a route coefficient/interval mismatch, so exact effect precision is not used. |
| <a id="c-05"></a>C-05 | **`inference`** — Neither study establishes a universal landmark count, that quicker route completion is always desirable, or that route learning demonstrates free-exploration enjoyment. | GDR-SRC-20261010-W03-004, task and outcome scope; GDR-SRC-20261010-W03-006, task, null outcomes and §4.4 limitations. | High for these evidential exclusions. Non-significance is not proof of no effect, and the two interventions are not equivalent. |
| <a id="c-06"></a>C-06 | **`practitioner-heuristic`** — Alex Beachum describes changing path information to better support curiosity-motivated choices, while acknowledging broader free-roaming tests were still upcoming. | GDR-SRC-20261010-W03-007, opening pathing Q&A and final answer. | High for attribution, low for causal efficacy. In-development 2016 account; no exact retail build or test dataset inspected. |
| <a id="c-07"></a>C-07 | **`hypothesis`** — Where the intended problem is choosing between destinations rather than guessing a corridor, sufficient destination information may increase reasoned route selection without requiring disclosure of the destination’s solution. | Design bridge from GDR-SRC-20261010-W03-007; distinct from landmark-presence effects in GDR-SRC-20261010-W03-004 and map-memory effects in GDR-SRC-20261010-W03-006. | Low for the combined recipe. Information can instead spoil discovery, constrain wandering or create false certainty. |
| <a id="c-08"></a>C-08 | **`inference`** — A gate should be described separately by current reachability, the condition that could change it, and what the player has grounds to believe about that condition. | W03 conditional-graph reasoning; no comparative gate experiment inspected. Foundations owns the actual ability/resource rules. | Moderate as an authoring tool; unknown benefit for particular players, genres or gate types. |
| <a id="c-09"></a>C-09 | **`practitioner-heuristic`** — XAG 103 recommends alternate channels for important information; distinct colors or shapes alone do not establish nonvisual access. | GDR-SRC-20261010-W03-011, Implementation guidelines on critical cues, shapes/location and color. | High for document content; not a formal standard, certification or quantitative prescription. |
| <a id="c-10"></a>C-10 | **`practitioner-heuristic`** — Naughty Dog’s 2020 feature account describes navigation assistance for story progression and, in an alternate mode, the most recently scanned item or enemy. | GDR-SRC-20261010-W03-010, Navigation and Traversal introduction and Navigation Assistance row. | High for the documented feature account, not an observed gameplay outcome. Do not infer unrestricted player-selected destination support or all-clue narration. |
| <a id="c-11"></a>C-11 | **`hypothesis`** — Flow should be evaluated against the intended movement, decision and attention rhythm, rather than only minimizing traversal time. | W03 proposed evaluation stance; motivated by the differing outcomes in GDR-SRC-20261010-W03-004/GDR-SRC-20261010-W03-006 and destination-choice goal in GDR-SRC-20261010-W03-007. | Low for an optimal pacing recipe; no player-benefit threshold specified. |
| <a id="c-12"></a>C-12 | **`inference`** — Spatial validation should cover approach direction, gate state, access mode and re-entry, because a valid route description can omit the information available in those conditions. | W03 analysis from C-01/C-08, with access constraints from GDR-SRC-20261010-W03-011. | Moderate logical confidence; actual representative validation and camera/platform dependency review remain missing. |

## References

All source identities below are temporary W03 identities. Access date: **2026-10-10**. URL/DOI/edition deduplication across batches is pending Library Coordination. Source access does not imply game observation or evidence approval.

### GDR-SRC-20261010-W03-004

**Greeshma Sharma, Yash Kaushal, Sushil Chandra, Vijander Singh, Alok P. Mittal and Varun Dutt.** *Influence of Landmarks on Wayfinding and Brain Connectivity in Immersive Virtual Reality Environment*. Frontiers in Psychology 8:1220. Publication/update: 2017-07-20; current HTML reports an applied correction.

- Verified source: [Influence of Landmarks on Wayfinding and Brain Connectivity in Immersive Virtual Reality Environment](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01220/full).
- DOI: [10.3389/fpsyg.2017.01220](https://doi.org/10.3389/fpsyg.2017.01220).
- Edition/build: Publisher HTML with correction link; unnumbered current rendering. Access: `relevant-excerpt`.
- Precise inspected locators: Materials and Methods: Participants, Virtual-Maze Task, Behavioral Measures, Procedure; Results: Behavioral Outcome and Table 1; Discussion/Conclusion for comparison with reported behavioral results.
- Type and independence: Primary empirical study; randomized landmark-present versus landmark-absent virtual-maze task. Source 005 is its funding corrigendum, not replication. Separate participants and task from source 006.
- Claims in this entry: C-01, C-02, C-03, C-05, C-07, C-11.
- Limits: 35 recruited, five stopped because of immersive-maze discomfort, 30 continued; initial sample predominantly male engineering students aged 21–30. Maps available in both conditions. No game-enjoyment or broad accessibility outcome.
- Rights: Publisher identifies CC BY; attributed paraphrase and study metadata only.

### GDR-SRC-20261010-W03-005

**Greeshma Sharma, Yash Kaushal, Sushil Chandra, Vijander Singh, Alok P. Mittal and Varun Dutt.** *Corrigendum: Influence of Landmarks on Wayfinding and Brain Connectivity in Immersive Virtual Reality Environment*. Frontiers in Psychology 8:1514. Publication/update: 2017-09-04.

- Verified source: [Corrigendum: Influence of Landmarks on Wayfinding and Brain Connectivity in Immersive Virtual Reality Environment](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01514/full).
- DOI: [10.3389/fpsyg.2017.01514](https://doi.org/10.3389/fpsyg.2017.01514).
- Edition/build: Publisher HTML corrigendum. Access: `full`.
- Precise inspected locators: Correction paragraph immediately after “A corrigendum on”; publication and copyright fields.
- Type and independence: Primary publication correction; no new experimental dataset. Corrects funding attribution for source 004; same study and authors; not independent support.
- Claims in this entry: C-03.
- Limits: Authors state conclusions unchanged. This is not a statistical reanalysis or validation of any wider design recommendation.
- Rights: CC BY identified by publisher; attributed paraphrase only.

### GDR-SRC-20261010-W03-006

**Bingjie Cheng, Anna Wunderlich, Klaus Gramann, Enru Lin and Sara I. Fabrikant.** *The effect of landmark visualization in mobile maps on brain activity during navigation: A virtual reality study*. Frontiers in Virtual Reality 3:981625. Publication/update: 2022-11-15.

- Verified source: [The effect of landmark visualization in mobile maps on brain activity during navigation: A virtual reality study](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2022.981625/full).
- DOI: [10.3389/frvir.2022.981625](https://doi.org/10.3389/frvir.2022.981625).
- Edition/build: Publisher HTML, unnumbered current rendering. Access: `relevant-excerpt`.
- Precise inspected locators: §§2.1–2.7 task, map conditions and participants; §3 opening, §3.1 spatial learning, §3.2 mixed EEG results; §4.4 limitations.
- Type and independence: Primary empirical within-participant VR map-assisted navigation study. Independent dataset from source 004 but a different intervention and task, not a direct replication.
- Claims in this entry: C-01, C-04, C-05, C-07, C-11.
- Limits: 49 recruited, 48 analyzed; ages 18–35. Three/five/seven landmarks along a route, not simultaneously visible world-POI counts. Map events interrupted navigation. Published §3.1 route coefficient/interval mismatch retained as an unresolved reporting issue; raw data and supplements not inspected.
- Rights: Publisher open-access article; no figures or supplementary files reproduced; limited paraphrase.

### GDR-SRC-20261010-W03-007

**Mobius Digital; interview with creative director Alex Beachum, interviewer uncredited.** *The Intentionality of Wandering*. Mobius Digital development blog. Publication/update: 2016-08-18.

- Verified source: [The Intentionality of Wandering](https://www.mobiusdigitalgames.com/news/the-intentionality-of-wandering).
- Edition/build: HTML Q&A about in-development Outer Wilds; no exact build identified. Access: `full`.
- Precise inspected locators: Article Q&A only: opening pathing reassessment; “What in the course of production or playtesting…”; “So how do you balance…”; final “Now that we’re finetuning design…”; unrelated comments excluded.
- Type and independence: Firsthand creator interview about design changes and anticipated testing. One studio account. Any later Outer Wilds talks are not additional inspected support in this packet.
- Claims in this entry: C-06, C-07, C-11.
- Limits: 2016 development context, not an observed 2019 retail build; reported playtesting has no methods/sample/effect data here; broad free-roaming tests are described as upcoming.
- Rights: Copyrighted developer post; paraphrase only; no images or comments copied.

### GDR-SRC-20261010-W03-010

**Matthew Dunnerstick / Naughty Dog.** *The Last of Us Part II: Accessibility Features Detailed*. Naughty Dog. Publication/update: 2020-06-09.

- Verified source: [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed).
- Edition/build: 2020 release-context feature article; Navigation and Traversal rows; no current remaster parity asserted. Access: `relevant-excerpt`.
- Precise inspected locators: Navigation and Traversal introduction; Navigation Assistance and Enhanced Listen Mode rows.
- Type and independence: Official developer feature account, not a W03 game observation or efficacy study. One first-party feature account; not empirical corroboration of source 011.
- Claims in this entry: C-10.
- Limits: Specific documented option behavior only. No numerical configuration advice transferred, no assurance that other games or every clue support equivalent assistance.
- Rights: Copyrighted developer article; no images or settings tables copied.

### GDR-SRC-20261010-W03-011

**Microsoft.** *Xbox Accessibility Guideline 103: Additional channels for visual and audio cues*. Microsoft Learn. Publication/update: Last updated 2026-03-04; checked 2026-10-10.

- Verified source: [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).
- Edition/build: Unnumbered current web guideline; old /gaming/ path redirects to /xbox/. Access: `relevant-excerpt`.
- Precise inspected locators: Goal; Overview; Implementation guidelines on important visual/audio information, shapes/location, and color; last-updated footer.
- Type and independence: Official platform accessibility guideline; classified practitioner-heuristic here, not a formal standard or legal mandate. Guideline, not an independent player dataset. External linked guidance not treated as inspected.
- Claims in this entry: C-09, C-12.
- Limits: Full relevant public text accessible despite authorization chrome. Does not certify a design or supply universal size/contrast settings; recheck before platform implementation.
- Rights: Microsoft content; limited paraphrase, no embedded images; redistribution terms not separately audited.

## Coverage, open questions and change history

| Assigned subtopic | Coverage in this draft | Unresolved / next discriminating question | Review state |
|---|---|---|---|
| Topology and paths | Conditional connections, loops, branches, one-way access and return. | No comparative player study of these structures inspected. Which relation is misread in the target layout? | Author draft; independent review pending. |
| Sightlines and landmarks | Cue roles, approach/viewpoint caveats and two narrow empirical datasets. | No universal placement/count rule. Does the player recognize a route relation, not just an object? | Same. |
| Gating | Current access, change condition and player grounds distinguished. | Foundations movement/progression rules and W02 objective dependencies missing. | Same. |
| Flow | Separates movement, decision and attention outcomes. | No optimum pace or proof that faster traversal is better. | Same. |
| Spatial literacy | Separates route performance, route memory and relational understanding. | Long-term learning, children, older adults and representative access populations not established. | Same. |
| Access/localization/platform | Official guideline and a scoped developer feature account. | Actual shared P01/P02/P03 bytes and representative testing missing. | Same. |

Missing dependencies: Foundations movement/traversal, F03 progression/resources, W02 quests/objectives, reviewed Presentation visual communication/accessibility, P02 controls/multimodal and P03 camera/platform. Their content and IDs are not invented. See the [review packet](../reviews/full-run-20261010-w03-review-packet.md), especially `W03-CON-01`, `W03-CON-03` and `W03-CON-07` (local dispute labels).

**History:** 2026-10-10 — initial 0.1.0 / `initial-1`. The draft records the 2017 study's five discomfort withdrawals rather than treating all 35 recruits as the analyzed sample. No predecessor, supersession, independent reviewer or approval. The [artifact receipt](../reviews/full-run-20261010-w03-artifact-receipt.md) identifies exact bytes.

**Next decision:** independent Gate C review should audit C-02/C-04 against the Methods and Results, then challenge the transfer from those tasks to C-07. The published route coefficient/interval inconsistency remains unresolved; it must not become a precise design parameter.
