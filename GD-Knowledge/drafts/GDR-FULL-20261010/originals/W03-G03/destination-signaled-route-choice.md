---
id: GDR-CAND-20261010-W03-PAT-02
kind: pattern
title: Destination-signaled route choice
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
- informed route fork
- destination telegraphing
- intentional path choice
tags:
- route-choice
- legibility
- curiosity
- optional-guidance
related_topics:
- GDR-CAND-20261010-W03-TOP-01
- GDR-CAND-20261010-W03-TOP-02
- GDR-CAND-20261010-W03-TOP-03
related_patterns:
- GDR-CAND-20261010-W03-PAT-01
related_genres: []
source_ids:
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

# Destination-signaled route choice

> **Research candidate, not released guidance.** Version 0.1.0, candidate revision `initial-1`. Author self-review only; independent evidence review has not occurred. All worked designs and validation protocols below are illustrative or proposed. No W03 game build, prototype, participant session or playtest was executed. External creator accounts are not observations performed by this workspace.

## Purpose

Support a player who is meant to **choose where to investigate**, rather than choose an indistinguishable corridor and learn its destination only afterward. Supply enough relevant information to make the choice express an intention, while withholding information that the player is meant to discover on arrival. [C-01]

The pattern is a W03 synthesis motivated by Alex Beachum's 2016 account of pathing work on Outer Wilds. It is not a source-authored named pattern, an observation of a released build, or a proven way to increase curiosity. [C-01; C-02; GDR-SRC-20261010-W03-007]

## Context and prerequisites

Use where destinations differ in ways that are meaningful to the intended choice, and where at least some route information can be separated from the discovery itself. The player needs a usable way to identify those differences: names, reference features, observations, or appropriate alternate information. No specific sensory modality or universal landmark count is required. [C-03; C-04]

The route must actually support the implication its signal creates in the relevant state. A sign can identify a destination without promising direct access, but the distinction matters. A route that becomes unavailable requires a player-facing explanation or an appropriately uncertain signal; a remembered cue should not quietly become a false guarantee. [C-07]

Do not apply by default when the destination's identity is the intended mystery, when spontaneous uncommitted wandering is the goal, or when no meaningful destination choice exists. A directed path or a deliberately unnamed opening may be preferable. The pattern is not a requirement to label every optional route. [C-08]

## Mechanism and evidence

| Proposed link | Evidence/support | Limit or disconfirming possibility |
|---|---|---|
| The player can perceive a route distinction before commitment. | Accessibility guidance motivates access; availability is a logical prerequisite. [C-04] | A signal can be present but unavailable from the actual approach or access mode. |
| The distinction indicates a destination or relevant route condition. | Creator account motivates signaling path destinations; W03 separates information types. [C-02, C-03] | Salience may be interpreted as “mandatory” rather than as information about an option. |
| The player relates it to a current intention. | Central hypothesis of this recipe. [C-01] | The player may prefer an unknown destination or may not yet have a stable intention. |
| The selected route matches that intention. | Testable prediction, not established outcome. [C-01, C-07] | Perceived connection, actual access and destination identity may disagree. |
| Meaningful discovery remains on arrival. | Proposed information boundary, not an observed causal benefit. [C-03, C-08] | Any destination label may reveal too much in a particular design. |

The 2016 creator account is a source for the design problem and reported response, not for a universal optimum. The same-packet [spatial topic](../topics/level-and-spatial-design.md) examines narrower empirical landmark studies; those studies do not test this complete destination-choice recipe. Faster travel, stronger route memory and preserved curiosity must not be treated as interchangeable outcomes. [C-01; C-08]

## Recipe

Proposed recipe; not prototyped or tested in W03.

1. **Name the choice.** Specify what the player should be choosing among: a known destination, a broad kind of opportunity, a route condition or a deliberately unknown place. Record what should remain undisclosed. If no meaningful option differs, simplify the route rather than manufacture signs. [C-01, C-03]
2. **Separate information layers.** Write three columns: destination identity, route/commitment information and discovery content. Choose the minimum layer needed for this decision. A broad description may suffice; an explicit name is not mandatory. [C-03]
3. **Identify the commitment point.** Establish where the player can still compare or reverse options without an unintended cost. Make the needed distinction available before that point, not only after an irreversible move. Intended costly uncertainty is a different design and may require omitting this pattern. [C-01, C-07, C-08]
4. **Connect signal to route.** Check that an entrance, reference feature or description identifies the actual connection, not merely the visible bearing of the destination. A distant object behind an impassable barrier must not accidentally promise a direct path. [C-07]
5. **Make options comparable, not equally loud.** Communicate the distinctions relevant to the choice without implying all destinations offer identical value or require identical effort. Avoid using attention dominance as the only indication that one destination exists. Test whether salience is being mistaken for obligation. [C-01, C-03]
6. **Provide appropriate alternate access and chosen-target assistance.** Coordinate the information needed to distinguish options. An optional guidance mode should make its target clear; preserve a player-selected goal where that is the intended activity. Direct main-route guidance is legitimate when selected for that purpose, not as a silent substitute for all exploration. [C-04–C-06]
7. **Check changed states and reverse approaches.** Confirm what the player has grounds to infer after a gate closes, a shortcut opens or an area is approached from the other side. Describe these conditions conceptually; do not prescribe camera behavior or runtime ownership. [C-07]
8. **Compare information specificity.** Propose a minimal signal, no destination signal and a more explicit signal, keeping routes and discovery content stable. Identify where increased knowledge improves the chosen outcome and where it spoils it. [C-08]
9. **Exit or narrow.** Remove the signal when it answers the intended mystery, adds no useful choice, cannot accurately describe the connection, or creates disproportionate reading/access burden. Retain orientation help without destination disclosure when that better serves the goal. [C-03, C-07, C-08]

### Adjustable variables

| Variable | Possible adjustment | Failure to watch |
|---|---|---|
| Specificity | Unnamed opportunity, destination category, place name or explicit content. | Spoiler leakage at the high end; indistinguishable options at the low end. |
| Timing | Earlier overview, choice-point information, later confirmation. | Information after commitment, or an early cue forgotten before use. |
| Route implication | Bearing only, known path, approximate approach or confirmed access. | A visible target falsely interpreted as directly reachable. |
| Channel | Environmental form, label, map, spoken description or other appropriate aid. | One access mode gets less information or substantially more of the answer. |
| Optional assistance | None required, player-requested reminder, guidance to a chosen known target. | Assistance silently chooses a goal instead of helping pursue it. |
| Commitment | Easy reversal through deliberate irreversible entry. | Hidden cost invalidates the apparently informed choice. |
| Uncertainty | What is known, uncertain or conditional about the route. | Confidence presented by the cue exceeds the world information available. |

These are design variables; no standard sign spacing, camera angle, marker count or numerical accessibility setting is proposed. [C-01; C-03–C-08]

## Worked examples

### Illustrative: the highland junction

**Invented; no level or player test.** At a shelter, the player may visit an old weather station, descend toward a ferry landing, or inspect an unnamed side passage. The station is a known place; what caused its signal to stop is unknown. The ferry is a transport option; its current operation is uncertain. The side passage is deliberately unexplained. [C-01, C-03]

The station's roof is visible, but the direct slope is not the walking route. A local route description identifies the switchback entrance and its destination rather than simply pointing at the roof. A second description identifies the ferry path while preserving uncertainty about service. The side passage is identified as traversable and reversible without revealing its destination. Each option supplies a different appropriate level of information instead of forcing full destination disclosure. [C-03, C-07]

Equivalent access presents these same distinctions: station via the switchback, route toward the ferry with service unknown, and unnamed passage. It does not identify the signal's cause or choose the station automatically. An optional reminder can repeat the player's selected destination; a player who selects general forward guidance can instead be told what that mode will target. This is proposed behavior, not a claim about a specific product's current features. [C-04, C-06]

A **bad revision** points a bright arrow at the roof without indicating the switchback, making a visible bearing appear to be a direct route. Another names the side passage's secret, removing its intended question. A third supplies only the station in the nonvisual description, making the other choices effectively unavailable. Corrections are to describe the connection, reduce specificity or restore equivalent grounds for choice—not simply add more markers. [C-03, C-04, C-07, C-08]

### Illustrative transfer and simpler alternative

The same decision structure can apply to rooms in a compact building or destinations across a region: it requires distinguishable options and information relevant before commitment, not a mountain, skyline or open-world label. A linear passage with no desired route choice does not benefit merely by adding a second nominal path. A single clear direction can be the simpler correct design for that context. [C-01, C-08]

## Tradeoffs and alternatives

Destination signals can make choice more intentional while making the world feel catalogued. Diegetic signs can fit a place while creating translation and reading costs. A visible reference can reduce wording while failing under occlusion or nonvisual access. Maps and guidance can support orientation while taking attention away from the environment or selecting a goal too aggressively. These are hypothesized tradeoffs to evaluate, not universal preferences. [C-01, C-03, C-04, C-06]

Alternatives include a deliberate unknown route, exploratory movement with easy reversal, one directed route, a player-authored marker, an optional description or guidance to an explicitly chosen known destination. Naughty Dog's feature account offers a scoped example of assistance with differing targets, not proof that a generic destination-selection design is already available or appropriate everywhere. [C-05, C-06; GDR-SRC-20261010-W03-010]

## Failure cases

| Warning sign | Candidate diagnosis | Revision to consider |
|---|---|---|
| A player follows the most salient route but cannot say where it goes. | Attention capture mistaken for informed choice. | Change the informational relation; compare against a less salient but informative cue. |
| A visible destination draws repeated attempts at an impassable approach. | Bearing confused with connection. | Explain the route entrance or explicitly limit the cue's promise. |
| Every sign is interpreted as the main objective. | The presentation implies obligation. | Distinguish optional information from the player's selected objective. |
| Arrival contains no valued surprise. | The signal disclosed the intended discovery. | Reduce specificity, or omit destination signaling. |
| Assistance sends the player away from a self-chosen goal. | Guidance target is implicit or incompatible. | State/let the player choose the target appropriate to the local design. |
| Return approaches invalidate earlier directions. | Cue vocabulary or access information assumes one approach/state. | Review reverse approaches and conditional access; use unambiguous place relations. |

These are proposed diagnostics, not observed failures from this batch. [C-01; C-03; C-06–C-08]

## Counterexamples and do not use conditions

The strongest counterexample is a route whose destination is itself the desired unknown. “Helpful” signage can erase the choice to explore uncertainty. An equally strong boundary is a place intended for purposeless wandering: demanding an articulated goal can misread a valued experience as deficient. The pattern must not redefine the design's success criterion merely to demonstrate its own usefulness. [C-08]

Do not use destination clarity to justify withholding basic access support, hiding irreversible costs, or disclosing solutions in only one access mode. Do not impose universal landmark counts from unrelated studies, or assume a creator account validates this recipe across scales and audiences. [C-01, C-04, C-07, C-08]

## Playtest

**Proposed / not performed.** Compare no destination signal, the minimum proposed signal and a more explicit signal in otherwise matched versions. Keep route connectivity, effort, available choices and content on arrival stable. Use fresh participants or equivalent unfamiliar spaces so the destination is not already known. [C-01, C-08]

Allow exploration without requiring a goal first; afterward ask whether there was a destination intention and what information supported it. In a separately defined intentional-choice task, elicit the goal before commitment without naming an unchosen preferred destination. These answer different questions and should not be pooled as one outcome. Record intentional choice, warranted prediction, unexpected commitment, confusion between bearing and access, valued surprise and satisfaction with wandering.

Include the actual devices, camera conditions, language and access modes, along with people who prefer different levels of guidance. Test optional assistance without treating its use as failure. Recognize that labels can change reading demand and landmarks can change salience; a matched appearance is not necessarily a matched information burden.

Reject or reduce the pattern when it fails to increase goal-consistent selection where that is wanted, spoils the discovery, impairs equivalent choice in relevant access modes, or adds burden without valued agency. Retain deliberate unknowns where participants value them. Define meaningful local differences and unacceptable costs before a future test. No playtest, effect size, universal threshold or participant recruitment occurred. [C-03, C-04, C-06–C-08]

## Claim ledger

Claim IDs are local to this file. Confidence refers to the specified claim, not to universal effectiveness. “None” in the evidence column means an explicitly proposed design hypothesis, not an omitted citation.

| Claim | Precise claim / class | Evidence and contrary context | Scope, confidence and unresolved question |
|---|---|---|---|
| <a id="c-01"></a>C-01 | **`hypothesis`** — At a route choice intended to express destination preference, a relevant signal about where a path leads may support a reasoned choice without necessarily revealing what will be discovered there. | New W03 synthesis motivated by GDR-SRC-20261010-W03-007, opening pathing and clue-specificity Q&A; not the source’s named pattern. | Low causal confidence. The full recipe has no directly inspected comparative test. |
| <a id="c-02"></a>C-02 | **`practitioner-heuristic`** — Beachum’s 2016 account reports a pathing reassessment around curiosity-driven destination choices, with broader free-roaming tests still prospective. | GDR-SRC-20261010-W03-007, first and final Q&A. | High for attribution, low for outcomes. In-development account, not a verified retail behavior or published player dataset. |
| <a id="c-03"></a>C-03 | **`inference`** — Destination identity, route/commitment conditions and the answer found on arrival are separable information choices; a cue need not disclose all three. | W03 analysis of clue specificity in GDR-SRC-20261010-W03-007. | Moderate logical confidence; low confidence that every setting permits a useful separation or preserves mystery. |
| <a id="c-04"></a>C-04 | **`practitioner-heuristic`** — XAG 103 recommends additional channels for important cues; the accessibility of a route distinction cannot be inferred from a visible signal alone. | GDR-SRC-20261010-W03-011, Goal / Implementation guidelines. | High for document content, not measured accessibility of this pattern or a formal standard. |
| <a id="c-05"></a>C-05 | **`practitioner-heuristic`** — The documented Naughty Dog assistance example has different targets for story progression versus a recently scanned item/enemy. | GDR-SRC-20261010-W03-010, Navigation and Traversal, Navigation Assistance row. | High for the narrow official feature description; no generic all-destination selection claim or current version parity. |
| <a id="c-06"></a>C-06 | **`hypothesis`** — Optional guidance should preserve the player’s chosen destination where destination choice matters; automatically steering toward the authored main route may defeat that purpose. | W03 goal-based bridge from GDR-SRC-20261010-W03-007, with a scoped alternative-target example in GDR-SRC-20261010-W03-010. | Low comparative confidence; direct main-route guidance can instead be appropriate when the player chooses that goal. |
| <a id="c-07"></a>C-07 | **`inference`** — Signals should be reviewed under changed access and reverse approaches because visible direction is not equivalent to traversable connection. | W03 conceptual connectivity reasoning; no causal experiment inspected. | High for the distinction, moderate for the proposed review method; no runtime or camera setting prescribed. |
| <a id="c-08"></a>C-08 | **`hypothesis`** — Reject or narrow destination signaling when it removes a valued unknown, does not improve intentional choice, or merely substitutes reading/assistance burden for route uncertainty. | W03 falsification proposal from C-01/C-03/C-06; no test performed. | Low outcome confidence. Local goals and access costs must determine the rejection rule. |

## References

All source identities below are temporary W03 identities. Access date: **2026-10-10**. URL/DOI/edition deduplication across batches is pending Library Coordination. Source access does not imply game observation or evidence approval.

### GDR-SRC-20261010-W03-007

**Mobius Digital; interview with creative director Alex Beachum, interviewer uncredited.** *The Intentionality of Wandering*. Mobius Digital development blog. Publication/update: 2016-08-18.

- Verified source: [The Intentionality of Wandering](https://www.mobiusdigitalgames.com/news/the-intentionality-of-wandering).
- Edition/build: HTML Q&A about in-development Outer Wilds; no exact build identified. Access: `full`.
- Precise inspected locators: Article Q&A only: opening pathing reassessment; “What in the course of production or playtesting…”; “So how do you balance…”; final “Now that we’re finetuning design…”; unrelated comments excluded.
- Type and independence: Firsthand creator interview about design changes and anticipated testing. One studio account. Any later Outer Wilds talks are not additional inspected support in this packet.
- Claims in this entry: C-01, C-02, C-03, C-06.
- Limits: 2016 development context, not an observed 2019 retail build; reported playtesting has no methods/sample/effect data here; broad free-roaming tests are described as upcoming.
- Rights: Copyrighted developer post; paraphrase only; no images or comments copied.

### GDR-SRC-20261010-W03-010

**Matthew Dunnerstick / Naughty Dog.** *The Last of Us Part II: Accessibility Features Detailed*. Naughty Dog. Publication/update: 2020-06-09.

- Verified source: [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed).
- Edition/build: 2020 release-context feature article; Navigation and Traversal rows; no current remaster parity asserted. Access: `relevant-excerpt`.
- Precise inspected locators: Navigation and Traversal introduction; Navigation Assistance and Enhanced Listen Mode rows.
- Type and independence: Official developer feature account, not a W03 game observation or efficacy study. One first-party feature account; not empirical corroboration of source 011.
- Claims in this entry: C-05, C-06.
- Limits: Specific documented option behavior only. No numerical configuration advice transferred, no assurance that other games or every clue support equivalent assistance.
- Rights: Copyrighted developer article; no images or settings tables copied.

### GDR-SRC-20261010-W03-011

**Microsoft.** *Xbox Accessibility Guideline 103: Additional channels for visual and audio cues*. Microsoft Learn. Publication/update: Last updated 2026-03-04; checked 2026-10-10.

- Verified source: [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).
- Edition/build: Unnumbered current web guideline; old /gaming/ path redirects to /xbox/. Access: `relevant-excerpt`.
- Precise inspected locators: Goal; Overview; Implementation guidelines on important visual/audio information, shapes/location, and color; last-updated footer.
- Type and independence: Official platform accessibility guideline; classified practitioner-heuristic here, not a formal standard or legal mandate. Guideline, not an independent player dataset. External linked guidance not treated as inspected.
- Claims in this entry: C-04.
- Limits: Full relevant public text accessible despite authorization chrome. Does not certify a design or supply universal size/contrast settings; recheck before platform implementation.
- Rights: Microsoft content; limited paraphrase, no embedded images; redistribution terms not separately audited.

## Related entries and history

Related topics: [Level and spatial design](../topics/level-and-spatial-design.md), `GDR-CAND-20261010-W03-TOP-02`; [World structure and exploration](../topics/world-structure-and-exploration.md), `GDR-CAND-20261010-W03-TOP-03`; [Environmental storytelling](../topics/environmental-storytelling.md), `GDR-CAND-20261010-W03-TOP-01`. Same-packet drafts are not independent corroboration. Complementary [Corroborated spatial inference](corroborated-spatial-inference.md) concerns interpretation at a destination.

Missing dependencies: W02 objective/quest tracking; Foundations traversal/progression; Presentation controls, maps, multimodal access and P03 camera/platform; applicable genre guidance. No absent file links or fabricated entry IDs substitute for those bytes. Relevant disputes `W03-CON-01` and `W03-CON-03` are in the [review packet](../reviews/full-run-20261010-w03-review-packet.md).

**Coverage:** choice framing, information specificity, routes versus bearings, conditional recipe, exit conditions, assistance, counterexamples and proposed testing drafted. The creator account lacks a published comparative dataset; broad accessibility, lasting spatial literacy and preserved curiosity remain unproven. Next discriminating question: does the minimum signal improve a wanted choice without erasing the wanted unknown?

**History:** initial W03 candidate, 2026-10-10, version 0.1.0 / `initial-1`; predecessor/supersession null. Author self-review is recorded in the packet; independent review and approval absent. Exact hash in the [artifact receipt](../reviews/full-run-20261010-w03-artifact-receipt.md). Next decision: independent Gate C assessment of C-01/C-08 before any adoption or release.
