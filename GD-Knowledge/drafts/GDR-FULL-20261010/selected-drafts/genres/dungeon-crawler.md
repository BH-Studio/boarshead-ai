---
id: GDR-CAND-20261010-G06-GEN-03
kind: genre
title: Dungeon crawler
version: 0.1.0
status: draft
candidate_revision: initial-research-1
attempt_id: G06-attempt-1
run_id: GDR-FULL-20261010
batch_id: G06
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- dungeon crawling
- expedition dungeon
- party crawler
tags:
- route-uncertainty
- resource-expedition
- mapping
- room-dependencies
- recovery
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-W02-TOP-02
- GDR-CAND-20261010-W02-TOP-03
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G06-PAT-01
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-W02-PAT-02
related_genres:
- GDR-CAND-20261010-G06-GEN-01
- GDR-CAND-20261010-G06-GEN-02
source_ids:
- GDR-SRC-20261010-G06-012
- GDR-SRC-20261010-G06-013
- GDR-SRC-20261010-G06-014
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
coverage_status: open
predecessor_sha256: null
supersedes: null
change_summary: Initial G06 submission; inspected dependency selections preserved;
  no prior batch reissued.
hash_record: ../reviews/full-run-20261010-g06-integrity.md
---

# Dungeon crawler

> **Draft research candidate, not released guidance.** Research authorization does not approve this definition, any causal claim, a game implementation or publication.

## Definition and boundaries

**Working usage:** a dungeon crawler makes traversal through connected, consequential spaces and the management of encounters, information or expedition resources central to play. The important property is not underground scenery but the relationship among where the player goes, what becomes possible, what is consumed and how they continue or return. This proposed boundary is useful for research routing, not a settled definition of every market use. [C-01]

Do not collapse this file into roguelike, roguelite or action RPG. Procedural generation, permadeath, random loot, a grid, first-person view and a party are **not required by this working definition**. The official Etrian Odyssey account describes mapping, turn-based encounters and a town-return cycle; Legend of Grimrock's description combines grid movement, real-time combat and puzzles; Minecraft Dungeons' launch account describes generated action-oriented levels. This variation motivates conditional guidance, not a universal feature bundle. [C-01–C-04]

The mere existence of a dungeon in an RPG or adventure does not make every decision a crawler problem. Conversely, a ship, building or outdoor ruin can be analyzed with this entry when routes, dependencies and expedition consequences dominate. Such synthetic transfers are inferences, not claims that those settings are officially classed as crawlers. Use [Role-playing](role-playing.md) for role authorship and [Action RPG](action-rpg.md) for continuous execution/build interactions. [C-01; C-15]

## Custom research instructions

Inspect an **outward route, a consequential room or encounter dependency, and the actual continuation/return policy** within one version and mode. Record directed connections, prerequisites, consumed resources, optional objectives, recovery points and what the player knows at each decision. A floor diagram without state is insufficient: an unlocked route may close, an elevator may require a consumable, and a one-way drop may invalidate the outward path as a return path. These are proposed analytical cases, not observations of the named games. [C-05; C-06]

Compare turn-based and real-time variants by what can change while the player inspects or plans; compare one player controlling a party with several people sharing authority. Do not infer decision time, pause policy or workload from the word “party.” In representative future cases, inspect both ordinary and depleted states, an optional branch, a changed return and the same passage approached from the opposite direction. [C-08–C-10]

For mapping, distinguish revealed geometry, recorded observations, inferred connections, current location and a prescribed solution. Source 013 documents an optional automap-disabled mode; it does not prove that absent mapping universally improves exploration. Source 012 documents platform-specific drawing affordances; it does not show that drawing is accessible to every intended player. Test the knowledge decision separately from the physical act of making a map. [C-02; C-03; C-07; C-11]

Seek contrary cases to “more uncertainty is better,” “return trips are padding,” “more rooms mean more exploration,” “every dungeon should be generated,” and “failure must erase the expedition.” State what experience each alternative is intended to protect before comparing it. No retrieved player dataset establishes these universal propositions. Exact death/revival rules, recovery-crystal behavior and generated-layout correctness were not verified in a game or primary manual during G06. [C-06–C-08; C-12; C-14]

## Player promises and varied audiences

Candidate promises include learning enough about an uncertain place to choose deliberately, making preparation matter, managing a party or resource state across encounters, discovering connections, and deciding when an expedition has achieved enough. Another audience may prefer brisk conflict and loot with minimal navigation burden. These are proposed audience distinctions, not a measured segmentation or a claim that manual cartography is the authentic form. [C-06; C-07; C-09; C-14]

A designer should specify the uncertainty they intend: *what lies beyond a door*, *which known route suits the current party*, *whether a limited supply can sustain a return*, or *how two rooms affect one another*. Concealing all four is a different task from preserving one. Reliable location information can coexist with unknown room contents; making location uncertain is also possible, but then the uncertainty itself needs an explicit design purpose and an appropriate access plan. [C-05; C-07]

The contrary case is a deliberately disorienting or terminal expedition. It may intentionally deny assured return. That does not justify claiming a safe return elsewhere, burying actual interaction costs or calling an inaccessible control a navigation puzzle. A hybrid's promises need an explicit disposition: which losses are intended, which information remains uncertain, which supports are available, and what a player can do after interruption. [C-08; C-11; C-15]

## Characteristic loops and structures

A proposed expedition analysis follows **prepare → choose a route → encounter and inspect → update the map/resource/party state → continue, recover or return → revise the next plan**. This is a decision model, not a claim that every crawler requires a town or a persistent metagame. Etrian's official account provides one concrete town-return arrangement; another game may use a camp, a continuous descent, an exit goal or a deliberately finite scenario. Alternatives beyond the inspected examples are illustrative. [C-02; C-06]

### A room is not an independent unit of design

Separate the topology, world state, resource state and the player's justified understanding. “Door opens after the switch” is incomplete until the designer identifies whether the switch stays accessible, whether it remains active, what lies between it and the door, and whether the relation is known or must be discovered. A combat win can consume the capability needed in the next room; an acquired key can make an earlier branch relevant. These are logical possibilities, not evidence that every room needs a dependency puzzle. [C-05]

| Decision object | What to record | Failure a room-by-room description can miss |
|---|---|---|
| Route | Direction, state prerequisites, cost and endpoint | An outward route has no valid return edge |
| Encounter | Entry condition, relevant resources, changed state and exits | A local victory creates an unintended unrecoverable expedition |
| Information | Observed fact, uncertainty, source and persistence | A map marks an inferred or stale route as confirmed |
| Recovery | What is restored, what remains spent, what is replayed | A checkpoint preserves the wrong trapped/depleted state |
| Optional branch | Intended value, cost and interaction with the main goal | “Optional” spending silently prevents the required continuation |

The table is a proposed review instrument. It does not prescribe runtime objects or prove that a large formal model is needed. For a small authored dungeon, an explicit paper state record can reveal a decision that needs review; it cannot certify gameplay quality. [C-05; C-12]

### Resource expeditions and return decisions

Compare the cost of **continuing**, **returning now**, **taking an alternate exit**, and **abandoning a secondary goal** in the state the player actually has. Include the cost of reaching a recovery point, not only the recovery itself. A refill that cannot be reached does not solve a depleted state. A theoretical resource reserve is also not usable if the item is inaccessible, held by an absent teammate or consumed by a prerequisite. These are conditional accounting and reachability distinctions. [C-06; C-08]

Preparation can become meaningful when it changes a reachable decision; it can become compulsory inventory repetition when the same answer is always required and nothing informative changes. Do not infer value from the number of consumables. Compare a smaller set of legible supplies, direct recovery, shorter expeditions or no attrition when those alternatives better match the intended experience. The experiential advantages are hypotheses, not measured findings. [C-06]

Return travel may contain a new decision, reconsideration of an earlier clue or a chosen period of calm. It may also repeat solved motion. Do not require a surprise encounter solely to justify a return, or assume unchanged traversal has no value. W03's queued **Changed-context return** owns a closely related research question; this batch retains that queue rather than extracting a renamed return pattern. [C-06; C-13]

### Readable exploration versus deliberate uncertainty

Choose which information layer assistance may reveal. A useful proposed separation is **known geometry**, **current orientation**, **recorded observations**, **inferred links**, and **unknown solution**. For example, an accessible record can state that a ladder was observed latched without asserting how to open it. A route aid can also intentionally provide more help, but that difference should be explicit rather than falsely described as identical information. No universal map density, landmark count or hint delay is supported here. [C-07; C-11]

Map drawing can be part of the desired reasoning, a recording tool, or an avoidable physical burden. Those are different design goals. Offering automatic recording of observed walls may preserve one reasoning task while removing another. Do not dismiss the changed experience, but do not make removal of a motor barrier contingent on a genre stereotype. Compare the actual intended inference and the player's effort before selecting manual, automatic, assisted or minimal mapping. [C-07; C-11]

### Party, solo and timing variants

A party build can distribute attack, recovery, navigation or information capabilities. Its meaningfulness depends on the encounters and resource states in which those contributions matter, not simply on class count. A single controller managing several characters has different command/inspection demands from several people with separate authority; this follows from the control arrangement, not a claim about enjoyment. [C-09; C-10]

Turn-based combat does not by itself establish that every exploration process pauses. Real-time combat does not establish that every menu leaves the world running. Record each actual clock. Evaluate planning, navigation, inventory and critical feedback under their real timing rules. In cooperative contexts, also identify whether one player's pause, retreat or equipment change commits others. No universal multiplayer pause policy is prescribed. [C-10; C-11]

## Applying shared topics

The [review packet](../reviews/full-run-20261010-g06-review-packet.md#reviewed-dependency-bytes) identifies actual selected bytes. These are parent-reviewed drafts, not released guidance. Imported study numbers and purported optimal settings are deliberately absent. [C-13]

| Inspected shared candidate | Crawler-specific adaptation |
|---|---|
| `GDR-CAND-20261010-F02-TOP-01` — Decision design | Separate route risk, missing map information, known resource cost and informed commitment at a one-way boundary. |
| `GDR-CAND-20261010-F02-TOP-02` — Challenge and difficulty | Review failed encounter, lost supply, replayed route and ended expedition as different consequences; inspect reachable recovery. |
| `GDR-CAND-20261010-W02-TOP-02` — Quests and objectives | Record whether opening a room, finding evidence, interpreting it or returning an object fulfils the objective. |
| `GDR-CAND-20261010-W02-TOP-03` — Lore delivery and continuity | Record observed/inferred/stale spatial facts separately; a journal entry must not silently certify an uncertain interpretation. |
| `GDR-CAND-20261010-P02-TOP-01` / `GDR-CAND-20261010-P02-TOP-02` | Distinguish navigation/interaction commands from their acceptance and outcome, especially when the same input can move or interact. |
| `GDR-CAND-20261010-P02-TOP-03` — Multimodal communication | Preserve intended information and uncertainty in map/narration/cue alternatives; count usable decisions, not channels. |
| `GDR-CAND-20261010-F07-TOP-01` / `GDR-CAND-20261010-F07-TOP-02` | Measure reasoned route choice and unwanted replay separately from completion speed; examine interruption and exit obligations. |

**Relevant but not transferred as reviewed body content:** `GDR-CAND-20261010-W03-TOP-02` (Level and spatial design), `GDR-CAND-20261010-W03-TOP-03` (World structure and exploration), `GDR-CAND-20261010-F03-TOP-01` (Progression and rewards), `GDR-CAND-20261010-F03-TOP-02` (Economies and resources). Their author packets were read selectively; their complete topics were not obtained here, and parent independent review is active. W03 landmark-study claims and counts are not G06 findings. F04 traversal/combat and F05 authored/generated content remain missing local bodies. [C-13]

## Pattern selection and adaptations

Use the inspected F01 **Supported attempt and transfer check**, `GDR-CAND-20261010-F01-PAT-01`, to test a specific relation such as spendable supplies versus reserved return cost. Vary cases so that both feasible and infeasible actions occur; retain baseline state information and access support. A player who knowingly chooses a risky branch has not necessarily misunderstood it. [C-06; C-13; C-14]

Use the inspected W02 **Multi-route objective contract**, `GDR-CAND-20261010-W02-PAT-02`, when rooms offer genuine alternative methods and method-sensitive consequences. A dungeon that explicitly requires repairing a seal may legitimately reject merely reaching its chamber. Do not expand every puzzle into multiple routes solely to satisfy a generic agency preference. [C-05; C-13]

The new [Dependency-complete loadout switch](../patterns/dependency-complete-loadout-switch.md), `GDR-CAND-20261010-G06-PAT-01`, is optional for party/equipment changes at permitted preparation points. In a constrained expedition, the available inventory and stated switching policy remain real dependencies. Omit unrestricted restoration when selecting a party for the whole expedition is the informed intended commitment. Coordinate recovery work with F03's existing queue instead of inventing a third packet pattern. [C-08; C-09; C-13; C-15]

## Representative cases and negative cases

| Inspected case | Specific contrast | What remains unverified |
|---|---|---|
| Etrian Odyssey Origins Collection | Mapping, turn-based encounters, party management and town return are described; platform mapping tools and save options are named. [C-02] | Exact encounter/route, death/revival rule, resource budget and user outcomes. |
| Legend of Grimrock | The official description joins real-time grid play with puzzles and an optional automap-disabled mode. [C-03] | The linked manual was inaccessible; no precise recovery-crystal, food, cooldown or death claim is made. |
| Minecraft Dungeons launch account | Generated action-oriented levels and equipment-defined roles illustrate a different dungeon-inspired arrangement. [C-04] | No layout generation guarantee, route-dependency test or current-build classification. |

These examples establish variation in documented arrangements, not a causal ranking. A linear combat sequence with dungeon scenery is a useful **illustrative negative case**: apply the combat/role guidance first when topology and expedition dependencies do little work. An elaborate maze with no resource attrition is not excluded merely for omitting hunger; analyze its information decisions instead. A survival hybrid can intentionally value uncertain return, but its stakes do not automatically override the access or interruption promise. [C-01; C-15]

### Illustrative worked expedition: the charged lift

This is an invented, small authored layout, not a generated level, a prototype or a shipped-game observation. It demonstrates a resource/route dependency, not a recommended difficulty or economy. [C-05; C-06]

```text
Camp <-> Fork <-> Upper service ledge
             |
             | lift down: one charge
             v
          Lower vault
             |
             | lift up: one charge -> Fork
             | ladder -> Upper service ledge, only after unlatched above
             | optional sample analysis: one charge
```

The party starts with **two charges**. Walking to the fork and service ledge consumes no charge under this example's deliberately limited model. The ladder is initially latched; inspecting it from above reveals that state. Other traversal risks are outside this arithmetic example and would need an explicit budget in a playable scenario. [C-06]

Descending leaves one charge. Spending it on analysis leaves none for the lift return. A prior visit to the service ledge that unlatches the ladder makes a charge-free return available; otherwise, the designer has created a potentially trapped state. “The sample is optional” does not remove the dependency. The intended design must choose whether this is disclosed expedition risk, an unwanted trap, a recoverable abandonment, or a terminal scenario. The example does not silently choose for the game owner. [C-05; C-06; C-08]

One proposed revision is to communicate the known return cost before descent and let the player reserve a charge or open the ladder. Another is a clearly scoped rescue that forfeits the optional sample. A third is to remove the sample cost when it contributes only bookkeeping. These alternatives protect different stakes; none is asserted superior. A rescue could also trivialize intentionally scarce expedition resources, so compare against an informed commitment rather than assuming a safety feature has no cost. [C-06; C-08]

For information access, the record may state *ladder seen, latch closed, operation not yet attempted*. It should not falsely say *safe exit available*. An optional solution-level aid could tell the player to open the ladder, but that is a different help level and should be evaluated as such. Localization and narration must preserve the distinction between observed and inferred route status. [C-07; C-11]

A proposed changed-case test starts with sufficient charges, with insufficient charges, and with the ladder already open. Ask which actions remain feasible under the stated model, then ask what the player prefers. Correct refusal in every case is not successful transfer. These are unvalidated example probes; the conditional arithmetic is not gameplay-efficacy evidence. [C-13; C-14]

## Accessibility and production implications

The crawler-specific access question is whether a person can inspect, record, revisit and use the intended spatial/resource information under the actual controls and clock. Drawing dexterity, map-symbol conventions, spatialized sound, small text, rapid party selection and memory after interruption can be separate demands. Offer and test appropriate alternatives without automatically revealing hidden topology or insisting that every assistance route preserve identical experience. These are proposed review questions, not a clinical or platform-conformance claim. [C-07; C-10; C-11]

Localization review should distinguish room names from relative directions, one-way movement from reversible travel, “unknown” from “blocked,” and an object's presence from the action that makes it usable. A simple translated arrow may not preserve these distinctions. Do not rely on a culture-specific symbol as self-evident evidence of threat, safety or morality. Appropriate language and lived-experience review remain missing. [C-11]

For authored content, trace changed room/route states and reachable recovery. For generated content, the same proposed invariants must be assessed across the output conditions the system actually supports, but G06 does **not** provide a generator algorithm, solver, sample-size guarantee or production validation result. F05 ownership/body access remains unresolved. Authored does not automatically mean valid; generated does not automatically mean varied or replayable. These are scope limits and design hypotheses, not empirical findings. [C-12]

Production cost also includes maintaining records after rule changes and testing approach direction, interruption, party composition and access modes. A bespoke room puzzle can justify that effort; an incidental passage may not. Ethical review should distinguish a voluntarily selected harsh expedition from concealed session obligations, and should not infer wellbeing from long play. No repository, engine, publication or game-adoption action follows from this document. [C-08; C-11–C-13]

## Research questions and validation

**Proposed; not performed.** Begin with the cheapest representation that can answer the question. Paper routes can test conditional feasibility, but not real-time command burden or spatial perception. Obtain separate approval before recruitment or play. Record the specific mode, party authority, input/access route, language, prior mapping familiarity and what state information was provided. [C-14]

| Question / contrast | Measures and confounds | Falsifying or narrowing result |
|---|---|---|
| Does route information support deliberate uncertainty rather than guessing? Compare equally available known-state records with differing solution specificity. | Predictions, reasons for route choice, mistaken certainty, perceived exploration and spoiler reports; control topology, risk and prior map knowledge. | The aid chooses the solution, or uncertainty remains only because required information cannot be used. |
| Does preparation create a meaningful expedition decision? Compare the charged-lift dependency with a simpler cost structure. | Feasible continuation, intended risk, repeat bookkeeping, preference and understanding; distinguish arithmetic from role choice. | Preparation becomes rote with no valued consequence, or produces an unintended trapped state. |
| Does return travel add a desired experience? Compare unchanged return, changed context and a disclosed shorter return. | New decisions, desired calm, repetition burden, interruption and learned state; novelty and extra rewards are confounds. | Claimed benefit disappears when reward/novelty is controlled, or users value the simpler route more. |
| Can the actual party/control arrangement sustain the information task? Compare relevant supported clocks and input routes without forcing inaccessible exposure. | Command errors, inspection opportunities, coordination authority, workload and route understanding. | A nominally available map or recovery command cannot be used in the necessary state. |

Researched subtopics: route uncertainty, room dependencies, expedition resource reasoning, recovery alternatives, party/solo and turn/real-time distinctions, mapping and hybrid tensions. Coverage remains open for exact primary-manual recovery rules, inspected live route sequences, representative access evidence, player effects, generation validation, interrupted-play studies and the missing shared bodies. Next discriminating work should verify a complete named expedition/state transition, not add another undifferentiated list of crawler features. [C-12–C-15]

## Claim ledger

Every classification applies to the exact scoped statement below. Application proposals remain hypotheses or inferences even where their documented ingredients are well supported. No formal standard or new empirical-effect finding is asserted in this entry.

### C-01

**Statement:** The proposed crawler definition concerns interdependent spatial/expedition decisions and does not require procedural generation, permadeath, a grid or a party.

**Class:** `inference`. **Support/locator:** `GDR-SRC-20261010-G06-012`, `GDR-SRC-20261010-G06-013`, `GDR-SRC-20261010-G06-014`; Contrasting documented structures plus G06 working scope; not a necessary-and-sufficient or universally accepted definition.

**Confidence:** Moderate for the useful comparison; low for taxonomic consensus. **Limit / next discriminating question:** Do disputed cases create meaningful route/expedition questions beyond dungeon scenery?

### C-02

**Statement:** Atlus describes mapping, turn-based combat, party management and town return in Origins Collection, with named platform mapping and save options.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-012`; Create Endless Adventure and Key Features, retrieved lines 19–36.

**Confidence:** High for the publisher description; no behavior was reproduced. **Limit / next discriminating question:** Exact death, encounter, economy and access outcomes remain unverified.

### C-03

**Statement:** The official Grimrock description combines real-time grid play and puzzles, and describes an optional automap-disabled Oldschool Mode.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-013`; About This Game and Key Features; ignore user reviews/tags.

**Confidence:** High for the description; low for any claimed benefit of removing the map. **Limit / next discriminating question:** The manual was not retrieved; do not invent recovery or resource settings.

### C-04

**Statement:** Minecraft Dungeons is described at launch as dungeon-crawler-inspired, with generated levels and equipment-based specialization.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-014`; Minecraft… what now?, retrieved lines 518–528.

**Confidence:** High for the historical account; not a tested generation or genre claim. **Limit / next discriminating question:** Generated does not mean every route is meaningful, valid or replayable.

### C-05

**Statement:** Route topology, changing world state, resources and justified player knowledge should be distinguished when inspecting room dependencies.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; G06 conditional state/reachability reasoning, with inspected W02 objective and lore distinctions; illustrative charged-lift case.

**Confidence:** High for possible logical mismatches; no measured benefit of the complete review instrument. **Limit / next discriminating question:** Would the game intentionally value the apparently trapped or uncertain state?

### C-06

**Statement:** Expedition preparation and return costs may create useful decisions, but can instead create rote repetition or inaccessible reserves.

**Class:** `hypothesis`. **Support/locator:** `GDR-SRC-20261010-G06-012`; Town-return arrangement motivates the question; benefits are G06 hypotheses, not observed player effects. F02 recovery distinctions are inspected.

**Confidence:** Low for experience outcomes; arithmetic is high-confidence only within the specified model. **Limit / next discriminating question:** Compare simpler supplies, shorter trips and changed/unchanged return without confounding extra reward.

### C-07

**Statement:** Map assistance should identify which information layer it changes, separating recorded facts, orientation, inference and solution.

**Class:** `hypothesis`. **Support/locator:** `GDR-SRC-20261010-G06-012`, `GDR-SRC-20261010-G06-013`; Documented mapping alternatives plus inspected P02 multimodal fact/uncertainty distinction, lines 84–100.

**Confidence:** Low for proposed cross-audience efficacy. **Limit / next discriminating question:** Does the aid preserve the desired reasoning or unintentionally choose the route/solution?

### C-08

**Statement:** Recovery should be assessed from the actual reachable depleted state and declared stakes; a terminal expedition can be intentional but is not the default obligation.

**Class:** `hypothesis`. **Support/locator:** No direct public causal evidence; Inspected F02 challenge lines 85–112 and F07 safe-exit recipe; charged-lift alternatives are illustrative.

**Confidence:** Low for comparative recovery-policy benefit; high for distinguishing intended stakes from a false promise. **Limit / next discriminating question:** Does the safeguard preserve the chosen expedition decision or remove its reason to exist?

### C-09

**Statement:** Party alternatives are meaningful only relative to the reachable contexts, resources and authority in which their contributions operate.

**Class:** `inference`. **Support/locator:** `GDR-SRC-20261010-G06-012`; Party-management description and conditional comparison logic; no imported F03 balance findings.

**Confidence:** Moderate for design usefulness; player effects unmeasured. **Limit / next discriminating question:** Is a role actually available and desired, or merely present in the class list?

### C-10

**Statement:** One player controlling several characters and several people sharing control differ in authority and command demands; every activity clock must be specified.

**Class:** `inference`. **Support/locator:** `GDR-SRC-20261010-G06-012`, `GDR-SRC-20261010-G06-013`, `GDR-SRC-20261010-G06-014`; Documented turn/real-time/cooperative variants motivate separate facets; exact menu/pause behavior is not inferred.

**Confidence:** High for the logical distinctions; low for any preferred timing policy. **Limit / next discriminating question:** Inspect the actual build before asserting pause, workload or cooperative parity.

### C-11

**Statement:** Spatial access and localization should be checked on actual known/unknown state transitions rather than on map or channel presence alone.

**Class:** `hypothesis`. **Support/locator:** No direct public causal evidence; G06 application of selected P01 scope, P02 controls/multimodal and W02 lore distinctions.

**Confidence:** Low for achieved access; none tested. **Limit / next discriminating question:** Can intended users inspect, record and act without false certainty or unintended extra disclosure?

### C-12

**Statement:** Authored and generated content both require scoped dependency review; G06 establishes no generator correctness or replayability result.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Scope and logical counterexamples; F05 bodies were not obtained.

**Confidence:** High for the evidence limit; no generator efficacy claim. **Limit / next discriminating question:** Inspect the actual generator/authoring rules and outputs under a separately approved technical scope.

### C-13

**Statement:** Only selected reviewed dependency excerpts are transferred; F03/W03 body content and pending queues remain distinct from their readable author packets.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Archive selection/byte inspection and native packet excerpts; exact provenance is in the batch packet.

**Confidence:** High for local access/status reporting. **Limit / next discriminating question:** Resolve current selected topic bodies and child ownership before further extraction.

### C-14

**Statement:** The charged-lift probes and proposed crawler studies are unperformed; correct conditional arithmetic is not evidence of learning or enjoyable exploration.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Illustrative model and corrected F01 pattern lines 98–116; F07 evaluation lines 65–93.

**Confidence:** High for the scope distinction; behavioral efficacy unknown. **Limit / next discriminating question:** Use changed answers and distinguish rule prediction from a knowingly chosen risk.

### C-15

**Statement:** Crawler/role-playing/action/survival conflicts require explicit tradeoffs rather than a winning genre rule.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Assigned G06 scopes and contrasting local examples; no new neighboring genre file is authored.

**Confidence:** Moderate for the design framing; unresolved normative preference. **Limit / next discriminating question:** Which intended promise takes priority at this particular decision, and who approves that choice?

## References



Source identities are temporary G06 identities. Access was checked on 2026-10-10; unnumbered web pages are not authenticated retail builds. An observed example below means an inspected source artifact, not a played game. Canonical URL/edition deduplication remains pending.



### GDR-SRC-20261010-G06-012

**Atlus.** *Etrian Odyssey — Origins Collection*. Publication/update: unknown publication date; page advertises availability 2023-06-01.

[Inspected source route](https://www.atlus.com/etrianorigins/index.html?lang=en). Edition/build: Origins Collection announcement for HD remasters; platform features explicitly differentiated. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary publisher feature description.

**Locator:** Create Endless Adventure; Features → Key Features; Etrian Odyssey HD (retrieved lines 19–43). **Claims:** C-01, C-02, C-06, C-07, C-09, C-10.

**Limits:** Turn-based mapping/party/return cycle and described options only; no exact maze, death rule, party performance or current patch reproduced. **Independence:** One collection and publisher account; three remasters are not three independent usability studies. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-013

**Almost Human, developer/publisher description hosted by Valve Steam.** *Legend of Grimrock — About This Game*. Publication/update: unknown page update date.

[Inspected source route](https://store.steampowered.com/app/207170/Legend_of_Grimrock/). Edition/build: Official product description of Legend of Grimrock; no client build inspected. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary developer-supplied product description.

**Locator:** About This Game and Key Features: grid movement, real-time combat, puzzles, party and optional automap-disabled Oldschool Mode (retrieved lines 124–132). **Claims:** C-01, C-03, C-07, C-10.

**Limits:** Ignore user reviews, ratings and market tags as evidence. Linked manual could not be retrieved; no crystal, food or death-rule detail adopted. **Independence:** Distinct production from Atlus. Hosting platform is not the author of the game-design claims. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-014

**Cristina Anderca / Mojang Studios.** *Minecraft Dungeons is here!*. Publication/update: 2020-05-26.

[Inspected source route](https://www.minecraft.net/en-us/article/minecraft-dungeons-here-). Edition/build: Launch article; no contemporary sequel or current build inferred. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary publisher launch account.

**Locator:** Minecraft… what now? (retrieved lines 518–528); byline/date at 509–512. **Claims:** C-01, C-04, C-10.

**Limits:** No fixed classes, equipment-based specialization and generated levels are described. Dungeon-crawler inspiration is not an authoritative resolution of RPG/action-adventure boundaries. **Independence:** One Mojang production; language mirrors and the current product page are derivative routes, not added corroboration. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



## Unresolved contradictions and tradeoffs

Packet-local records `G06-CON-04`, `G06-CON-05`, `G06-CON-06` remain open in the [contradiction register](../reviews/full-run-20261010-g06-review-packet.md#contradictions-and-competing-explanations). They are not globally allocated CON IDs. A tradeoff is not called an empirical contradiction when the goals, date or system differ.

## Review and history

Version 0.1.0, candidate revision `initial-research-1`, attempt `G06-attempt-1`, first submission. No predecessor or supersession is asserted. Author self-review is recorded in the [G06 review packet](../reviews/full-run-20261010-g06-review-packet.md); it is not independent review. Byte identity is in the detached [integrity receipt](../reviews/full-run-20261010-g06-integrity.md). Coverage remains open. Gate C independent review, Gate D host retrieval and Gate E acceptance/release remain uncompleted. No prototype, participant recruitment or playtest was performed.
