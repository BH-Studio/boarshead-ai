---
id: GDR-CAND-20261010-G06-GEN-02
kind: genre
title: Action RPG
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
- ARPG
- action role-playing game
- real-time build interaction
tags:
- real-time-execution
- build-legibility
- equipment
- respecialization
- accessibility
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
- GDR-CAND-20261010-F07-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G06-GEN-01
- GDR-CAND-20261010-G06-GEN-03
source_ids:
- GDR-SRC-20261010-G06-006
- GDR-SRC-20261010-G06-007
- GDR-SRC-20261010-G06-008
- GDR-SRC-20261010-G06-009
- GDR-SRC-20261010-G06-010
- GDR-SRC-20261010-G06-011
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

# Action RPG

> **Draft research candidate, not released guidance.** Research authorization does not approve this definition, any causal claim, a game implementation or publication.

## Definition and boundaries

**Working usage:** action RPG describes an arrangement in which real-time action execution and character/equipment configuration jointly shape a substantial part of conflict and development. “Action” identifies an execution condition; “role-playing” identifies a broader, contested family of role and capability decisions. Neither a loot shower nor a fast animation alone establishes the combination. This is a G06 analytic scope, not a market-label ruling. [C-01]

The [Role-playing](role-playing.md) entry owns the broader distinctions among role enactment, development and recognition. Here the additional question is what happens when a player's action, a configured capability and the current encounter interact under time pressure. Party control, camera, platform, cooperative play and solo play are separate facets. A real-time-with-pause or heavily automated system needs its actual timing and control boundaries described rather than being accepted or excluded by name alone. [C-01; C-16]

An action-adventure can include equipment changes without making character development central; a turn-resolved RPG can describe violent action without requiring continuous player execution. A crawler can combine grid movement and real-time combat while prioritizing route and party decisions. Use the measured or documented decision structure, acknowledge the label dispute, and retrieve the relevant neighboring entry rather than declaring one genre authoritative. [C-01; C-16]

## Custom research instructions

Inspect the chain **command → eligibility → action execution → contact/target resolution → statistical resolution → communicated result** in a specified configuration and encounter. Do not collapse every failed attack into poor responsiveness or every successful attack into player skill. Separate accepted input from weapon reach, targeting, hit/critical rules, resource constraints, mitigation and presentation. Source 010 documents one game's attack/defense and modifier distinctions, not a universal resolution pipeline. [C-02; C-10]

Research builds as dependency sets: capability prerequisites, equipped items, trigger bindings, resource generation/spending and the situations that let them operate. Inspect both a valid configuration and one that stops being valid after a change. Source 011 supplies a concrete prerequisite/trigger/reset example; sources 007–008 supply saved-loadout and missing-warning examples. Their existence does not demonstrate that the proposed G06 pattern improves comprehension. [C-03; C-05; C-06]

Seek evidence against four attractive claims: larger loot volume means deeper choice; more respec friction means meaningful identity; unrestricted switching means agency; and higher output means better access. Compare the same desired role across different execution demands and the same input task across different character power. Record whether a source reports design intent, shipped rules, a fix, an observed sequence or a participant outcome. Preserve date changes: the 2020 Diablo IV respec rationale and the later Armory description are different states of one production, not simultaneous timeless laws. [C-04; C-09–C-14]

Future representative coverage should include low-loot capability development, menu-intensive and streamlined configurations, solo and cooperative conflict, alternative input/targeting routes, and builds that favor sustained positioning rather than rapid repetition. These are sampling dimensions, not assertions that every audience wants each option. This bounded pass does not establish their prevalence or a hierarchy of preferences. [C-14; C-16]

## Player promises and varied audiences

Candidate promises include *my commands are intelligible*, *my chosen configuration changes how I act*, *I can identify why a plan failed*, and *development opens a valued possibility*. A player may instead value fast power growth or following a known build without extensive optimization. No inspected empirical dataset establishes a universal preference for complex builds, difficult execution, surprise drops or permanent specialization. [C-09; C-10; C-12; C-14]

Translate a promise into a testable distinction. “Responsive” might mean the player can distinguish an unrecognized command from an acknowledged but currently illegal action; it does not require every command to bypass deliberate recovery. “Build freedom” might mean several supported approaches remain usable in relevant content, not that every combination must succeed equally. “Accessible” cannot mean only that a menu option exists. These proposed distinctions need actual interaction and audience testing. [C-09; C-10; C-13]

## Characteristic loops and structures

Analyze at least two interacting horizons. Within conflict, players perceive opportunities, issue actions, manage position/resources and interpret consequences. Between conflicts, they inspect capabilities, compare equipment, change a configuration and choose a next challenge. Long-horizon development can affect both loops. These are analytic horizons, not mandated session lengths or a requirement for an endless reward cycle. [C-01; C-09; C-12]

### Execution skill and statistical power are not interchangeable

The diagnostic distinction below is proposed from the inspected control/feedback dependencies and the official Grim Dawn rules. It is not a required engine architecture. [C-02; C-10; C-15]

| Observed problem to distinguish in a future build | Candidate explanation | Discriminating comparison before changing power |
|---|---|---|
| No recognizable action follows a command | Mapping, command acceptance, unavailable action or feedback problem | Inspect command receipt and eligibility separately, retaining the player's input route |
| Action occurs but does not affect the intended target | Target selection, reach, occlusion, timing, immunity or hit resolution | Keep the configuration fixed and vary only the relevant target/position or rule condition |
| Same action has a different effect after equipment changes | Changed modifier scope, dependency, conversion, trigger or resource availability | Compare complete configurations and the explicitly relevant rule, not an unlabeled damage total |
| A nominally strong build is not used | Unavailable parts, misunderstood interaction, unwanted effort, narrow context or preference | Verify access and understanding, then test a representative encounter and ask about the intended role |
| A player wins after a power increase | Statistical margin, altered exposure, learning, assistance or chance | Do not infer mastery without changed cases at controlled capability and access conditions |

A higher damage value can mask an access problem without repairing it. Equally, a deliberately slow attack can be responsive if its acceptance, commitment and recovery are understood. Neither inference supports an unsourced frame target, hitstop duration or input-buffer window. Timing policy and technical delay must be distinguished before choosing numerical settings. [C-10; C-13]

### Meaningful builds versus dominant upgrades

Represent a build by what it enables and requires: target conditions, position, resource cycle, prerequisite items/skills, tolerated interruption and input effort. Compare it across a **declared encounter set and player goals**. A single stationary target test can answer a narrow output question, but cannot establish general usefulness in moving, multi-target or constrained-resource situations. This is a logical limit on what the comparison includes, not a finding about a particular game's balance. [C-09]

A straight upgrade can be appropriate for a power-growth loop. Specialization instead needs circumstances in which the tradeoff matters. Do not multiply affixes to create nominal alternatives that leave the same preferred action in every relevant context. Also do not remove a low-demand build merely because it outperforms a high-demand build for some users; first ask what the intended costs, risks and access conditions are. A chosen lower-effort role is not evidence of less legitimate engagement. [C-09; C-13]

The proposed process is to state each configuration's intended contribution, trace its prerequisites, select contrary encounters, and inspect outcomes plus the player's explanation. Stop balancing from aggregate usage when availability, comprehension or preference remain plausible alternatives. This is a conditional transfer of F07's diagnosis, not a new empirical balance theorem or a third extracted pattern. [C-09; C-15]

### Reversibility, respec and encounter preparation

| Policy option | Intended use to test | Cost or counterexample |
|---|---|---|
| Direct, freely adjustable independent choices | Low-dependency exploration or a minimal action game | Extra save/preview machinery may add more friction than it removes |
| Saved configurations changed at a declared rest point | Repeatable builds with interdependent gear and abilities | Preparation can become a menu ritual; saved plans can become invalid |
| Costed retraining with explicit preserved/lost state | A chosen development/commitment promise | Cost can punish missing information, exclude experimentation or create recovery grind |
| Temporary trial with disclosed scope | Learning an unfamiliar interaction before commitment | A trial that changes enemies/resources or conceals dependencies can mislead |
| Lasting core identity, adjustable execution details | A campaign that values a stable role but allows correction or access support | A false distinction can preserve a trap; protected scope must be explicit |

These are hypotheses, not recommendations to offer every policy. Shely's 2020 account valued both experimentation and increasing commitment; the later Armory describes town-based saved builds and a particular no-Gold Paragon-loadout change. That historical contrast defeats treating one development-era policy as a universal ARPG requirement. It does not isolate which arrangement improves enjoyment or prove that every respec operation is free. [C-04; C-05; C-11]

A saved configuration should not be mistaken for a presently usable one. The new [Dependency-complete loadout switch](../patterns/dependency-complete-loadout-switch.md) addresses that narrower problem. It does not mandate free switching, cooldown resets, inventory duplication, removal of narrative consequences or an implementation transaction model. [C-03; C-05; C-06; C-11]

### Loot, pacing and reading burden

For each reward, ask whether it changes an available action, an enabling condition, a desired identity or merely a magnitude. The proposed benefit of reducing redundant comparison is more attention for chosen play; that benefit remains unmeasured here. More information may be appropriate for an optimization audience, and suppressing details can hide the exact dependency an expert needs. Compare concise summaries with accessible on-demand detail rather than assuming either maximal text or automatic filtering is universally better. [C-12]

Separate reward acquisition from a usable whole. A drop that enables a build only after several inaccessible prerequisites does not immediately deliver that role. F03 progression/economy bodies are missing from the inspected dependency set, so this entry supplies no reward guarantee, drop-rate prescription, currency sink or economic safety claim. Retain the dependency as an open integration question instead of presenting a generic grind recommendation. [C-12; C-15]

## Applying shared topics

All transfers below are from actual selected, parent-reviewed **draft bytes**. The [dependency record](../reviews/full-run-20261010-g06-review-packet.md#reviewed-dependency-bytes) identifies exact revisions and hashes. G06 has not independently repeated their original studies. [C-15]

| Inspected shared candidate | ARPG-specific adaptation |
|---|---|
| `GDR-CAND-20261010-F02-TOP-01` — Decision design | Compare switching cost, preparation, foreknowledge and reversibility; do not equate a large tree with valued choice. |
| `GDR-CAND-20261010-F02-TOP-02` — Challenge and difficulty | Keep execution demands, power, failure cost and assistance distinct. Manual choices are an alternative to uncertain automatic adaptation. |
| `GDR-CAND-20261010-P02-TOP-01` — Controls and input | Distinguish action eligibility, mapping and sustained/repeated input effort from character strength. |
| `GDR-CAND-20261010-P02-TOP-02` — Feedback and game feel | Do not use a success cue for a rejected or missed action; preserve required state facts when intensity is reduced. |
| `GDR-CAND-20261010-P02-TOP-03` — Multimodal communication | Communicate the same known rejection/dependency fact through usable alternatives; extra simultaneous channels are not proof of access. |
| `GDR-CAND-20261010-W02-TOP-02` / `GDR-CAND-20261010-W02-TOP-03` | Configuration changes must not silently satisfy an unperformed quest method or rewrite recognized history. |
| `GDR-CAND-20261010-F07-TOP-01` / `GDR-CAND-20261010-F07-TOP-02` | Diagnose power versus comprehension/availability; examine grind, refusal and stopping without treating retention as wellbeing. |

F01's corrected transfer-check pattern requires changed cases with different correct predictions and keeps preference separate from permission. P01's corrected numerical scope remains intact: web criteria, vendor advice, default launch text and scaling guidance are not interchangeable. G06 imports **no universal UI, timing or sensory values**. F03 and W03 readable author packets supply exact identities and queues, not completed independent review; F04 and F05 body access is unresolved. [C-15]

## Pattern selection and adaptations

Select `GDR-CAND-20261010-G06-PAT-01` only for interdependent loadout changes that the game actually permits. A cosmetic preset or one independent weapon swap may need no bundled validation. An intentional mid-combat stance change is a different timing contract; do not force it through a town-menu recipe. [C-11; C-16]

The inspected `GDR-CAND-20261010-F07-PAT-01`, **Triangulated balance diagnosis**, complements the loadout pattern by distinguishing weak power from misunderstood or unavailable configurations. `GDR-CAND-20261010-F07-PAT-02`, **Legible commitment and safe exit**, supplies a broader commitment review, not permission to erase cooperative consequences. A new build-trial pattern is queued for ownership/overlap review rather than duplicating those recipes. [C-09; C-11; C-15]

## Representative cases and negative cases

The official Grim Dawn combat guide describes statistical attack/defense resolution; its Devotion guide describes affinity dependencies and compatible power bindings. They establish implementable distinctions but not the depth, fairness or accessibility of every build. [C-02; C-03]

Blizzard's Armory announcement and later 2.1.3 fix report form a particularly useful positive/negative pair: an advertised configuration feature did not make every dependency warning work through every access route. The reported absence of a screen-reader warning when a connecting node was refunded is narrow failure evidence. It does not prove the feature is unusable generally or that this proposed G06 recipe is already tested. [C-05; C-06; C-07]

Minecraft Dungeons' launch article describes equipment-based specialization without fixed classes. It challenges fixed-class assumptions in action/build discussion; its stated dungeon-crawler inspiration does not resolve whether a particular audience calls it an RPG or action-adventure. Analyze the configuration and exploration demands rather than correcting the publisher's label. [C-08; C-16]

### Illustrative worked comparison: three configurations, not three damage scores

Consider a fictional real-time conflict system. **Bulwark** protects a short area but commits the character to a slower recovery; **Skirmisher** can reposition readily but depends on available space; **Conductor** uses a marked target to enable an area effect but must establish that condition first. These names, mechanics and contrasts are invented. No recommended timing or damage values are implied. [C-09]

First compare all three in an open moving encounter, a narrow defense and a sequence with interrupted setup. Keep acquired capability and access supports identified. Ask what role each player intended, which prerequisite they predicted, and why an attempt did not work. A narrow defense may make Skirmisher's mobility unnecessary without proving the build globally weak. Conversely, if the supposedly specialized conditions never occur in the intended content, its theoretical advantage is not a meaningful choice there. [C-09; C-10]

Now save Conductor, lend its enabling focus item to a teammate, and attempt to restore the preset. The proposed switch review should identify that missing prerequisite, the unavailable follow-on action and the chosen fallback before committing. It should not silently substitute Bulwark, borrow someone else's item, or clear spent resources. This illustrates the new pattern's dependency problem; it is not a description of Diablo IV's fallback behavior. [C-11]

For the strongest counterexample, replace the system with a single independent attack toggle that can be changed safely at any time. A large preset preview adds unnecessary reading and action cost. Omit the pattern; a direct change with ordinary state feedback can be the better hypothesis. [C-11; C-13]

## Accessibility and production implications

Blizzard's launch-context account describes remapping, toggle/targeting assistance and narration. These are useful feature routes, not evidence that every combination of skills, input devices and access needs works. Its later warning fix underlines why testing the actual dependency transition matters rather than counting settings. [C-06; C-07]

Proposed ARPG access reviews should distinguish sustained holds, repeated presses, simultaneous inputs, aim selection, visual tracking, reading under pressure and feedback tolerance. A lower-input build should still have a comprehensible, useful role under the declared design goals; a damage bonus alone need not resolve an unavailable command or unreadable prerequisite. Do not force users to disable accommodations for a purported mastery check. [C-10; C-13]

Localization must preserve prerequisite direction, conditional triggers, modifier scope and the distinction between saved and active state. A screen-reader summary needs the affected action and reason, not only a generic error sound. In cooperative contexts, also check whose item/role is being changed, who can authorize it and when the group resumes; one user's configuration screen must not silently commit the party. These are untested application proposals with Presentation/Foundations ownership dependencies. [C-11; C-13]

Production review should bound supported combinations and changes in documentation, tooltips and saved plans across revisions. Do not call a known reported fix a complete regression audit. Ethical review should examine whether access to a viable configuration requires an unchosen repetition burden or paid correction; this entry makes no legal determination or claim about a named game's motives. No engine code, telemetry deployment or live-game modification is authorized. [C-12; C-13]

## Research questions and validation

**Proposed, not performed.** Obtain study approval separately; record ruleset, equipment, dependencies, encounter, device/access settings, familiarity, language and exposure. Do not require participants to attempt an inaccessible baseline. [C-14]

| Test question / contrast | Measures and rival explanations | Reject or revise when |
|---|---|---|
| Can a player tell an input problem from a capability constraint? Use matched cases with different actual rejection causes. | Prediction of cause, chosen recovery, erroneous re-input and perceived control; confounds include animation cues, latency and prior rule knowledge. | The diagnostic presentation repeatedly suggests the wrong cause or adds prohibitive interruption. |
| Do configurations offer meaningful alternatives in declared content? Compare representative encounter contrasts rather than one output benchmark. | Feasible contribution, desired role, effort, availability and explanation; predeclare meaningful audience/context distinctions. | One alternative is dominated under all stated goals, or its only advantage relies on inaccessible/absent content. |
| Does bundle preview reduce unintended invalid switches compared with an equally usable direct summary? | Correct prediction of affected actions, unwanted state changes, recovery, inspection burden and later successful use. | Preview gives no worthwhile benefit, obscures usable simple changes, or an access route loses the warning. |
| Does a respec policy improve informed choice without obligatory menu preparation? Compare policies at matched information and capability. | Understood commitment, desired experimentation, unwanted repeated configuration and session interruption; control acquisition cost and encounter foreknowledge. | Apparent benefit is only more menu time, stronger gear or concealed recovery cost. |

No study here establishes an optimal build count, loot rate, respec price or execution window. Researched: action/stat interaction, build dependencies, historical respec tension, configuration warnings, loot-depth distinctions and conditional access/pacing. Open: controlled player effects, low-loot range, final-build observations, cooperative switching and representative access testing; missing F03/F04/F05 bodies; source-version rechecks before any adoption. [C-14–C-16]

## Claim ledger

Every classification applies to the exact scoped statement below. Application proposals remain hypotheses or inferences even where their documented ingredients are well supported. No formal standard or new empirical-effect finding is asserted in this entry.

### C-01

**Statement:** Action RPG is provisionally scoped by the interaction of real-time execution and character/equipment configuration, not loot quantity or a market label alone.

**Class:** `inference`. **Support/locator:** `GDR-SRC-20261010-G06-010`, `GDR-SRC-20261010-G06-011`, `GDR-SRC-20261010-G06-014`; Documented capabilities and equipment-based specialization motivate the working comparison; membership remains contested.

**Confidence:** Moderate for decision usefulness; low for taxonomic consensus. **Limit / next discriminating question:** Does a disputed case require different guidance once actual action and development demands are recorded?

### C-02

**Statement:** The Grim Dawn combat guide distinguishes attack/defense-mediated hit and critical resolution and the scope of damage modifiers.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-010`; Landing Hits and Critical Hits; Flat vs. Percent Damage.

**Confidence:** High for the documented distinction, not verified current-client behavior. **Limit / next discriminating question:** No numerical settings or player-skill conclusions follow.

### C-03

**Statement:** The Devotion guide documents affinity prerequisites, compatible power bindings and limits on removing supporting allocations.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-011`; Unlocking Constellations, Affinity, Celestial Powers and Resetting Devotion Points.

**Confidence:** High for the narrow documented dependency rules. **Limit / next discriminating question:** Other versions and full configuration validity require direct verification.

### C-04

**Statement:** The December 2020 Diablo IV account argues for experimentation alongside increasing respec commitment and describes intended equipment distinctions.

**Class:** `practitioner-heuristic`. **Support/locator:** `GDR-SRC-20261010-G06-006`; Skill Tree, Weapon Types and Item Qualities; not-final caveat retained.

**Confidence:** High for the developer rationale; low for demonstrated benefit. **Limit / next discriminating question:** Do not transplant pre-release intent into current rules or universal identity claims.

### C-05

**Statement:** The later Armory account describes saved configuration bundles, missing-item indication and no Gold for switching differing Paragon loadouts.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-007`; The Armory, retrieved lines 460–467; scope is historical feature documentation.

**Confidence:** High for the described scope, not an observed player outcome. **Limit / next discriminating question:** It does not say all respec actions are free or define every fallback.

### C-06

**Statement:** Diablo IV 2.1.3 reports missing loadout and screen-reader dependency warnings as fixed defects.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-008`; 2.1.3 Build #62672 (2025-03-04), Vessel of Hatred Bug Fixes and Base Game Accessibility.

**Confidence:** High for the developer fix report; no incidence or reproduction established. **Limit / next discriminating question:** A fix announcement is not complete regression or access certification.

### C-07

**Statement:** The Diablo IV accessibility account describes alternative input and narration features, not measured equivalence across access needs.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-009`; Dexterity Assistance and Vision Assistance; contrast source 008 does not negate all described features.

**Confidence:** High for feature description; efficacy unestablished. **Limit / next discriminating question:** Can relevant users employ the specific chosen build and dependency warnings?

### C-08

**Statement:** Minecraft Dungeons is described at launch as having equipment-based specialization without fixed classes.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-014`; Minecraft… what now?, class paragraph; publisher inspiration terminology retained.

**Confidence:** High for the historical account, not taxonomic authority. **Limit / next discriminating question:** Do not infer every RPG supports unrestricted equipment switching.

### C-09

**Statement:** Build usefulness and dominance are conditional on specified goals, costs, enabling encounters and access demands; a single benchmark omits untested contexts.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Conditional comparison logic; inspected F07 evaluation lines 113–121 and diagnostic pattern lines 71–81.

**Confidence:** High for the logical scope limit; low for the experiential value of a particular alternative. **Limit / next discriminating question:** Does changing availability, comprehension or encounter distribution explain apparent weakness?

### C-10

**Statement:** Diagnose command recognition, eligibility, execution and outcome separately before treating statistical power as a responsiveness repair.

**Class:** `hypothesis`. **Support/locator:** `GDR-SRC-20261010-G06-010`; G06 application bridge; inspected P02 controls and feedback lines 77–89 supply the action-receipt/outcome distinction.

**Confidence:** Low for full diagnostic efficacy; moderate for the identifiable rule distinctions. **Limit / next discriminating question:** Do tested users recover more accurately without extra burden or confusing cues?

### C-11

**Statement:** Configuration policy should specify timing, dependencies, preserved state and fallback; unrestricted switching is not universally preferable to informed commitment.

**Class:** `hypothesis`. **Support/locator:** `GDR-SRC-20261010-G06-006`, `GDR-SRC-20261010-G06-007`, `GDR-SRC-20261010-G06-008`, `GDR-SRC-20261010-G06-011`; Historical policy contrast and concrete dependency/failure examples justify testing, not proven agency. New G06 pattern gives the narrower recipe.

**Confidence:** Low for comparative policy benefit. **Limit / next discriminating question:** Does a simpler direct change or stable-role policy better meet the intended promise?

### C-12

**Statement:** Loot count and comparison activity are not themselves evidence of deeper choice; acquisition should be distinguished from a usable configured capability.

**Class:** `hypothesis`. **Support/locator:** No direct public causal evidence; G06 design proposal and logical distinction; F03 author packet is context only, not a transferred reward study.

**Confidence:** Low for any recommendation to reduce comparison burden; definitions alone do not prove enjoyment. **Limit / next discriminating question:** Which reward changes a valued action or decision rather than merely producing more inspection?

### C-13

**Statement:** Access, localization, cooperative authority and maintenance must be tested on actual configuration transitions, not inferred from feature counts or damage output.

**Class:** `hypothesis`. **Support/locator:** `GDR-SRC-20261010-G06-008`, `GDR-SRC-20261010-G06-009`; Narrow warning defect plus feature descriptions; P01 scope and P02 control/fact distinctions support the proposed review questions.

**Confidence:** Low for cross-population outcomes; strong reason not to claim certification from presence alone. **Limit / next discriminating question:** Does any required warning/action become unavailable, mistranslated or imposed on a teammate?

### C-14

**Statement:** All proposed ARPG tests remain unperformed, and the inspected sources establish no universal numerical balance or access settings.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Research method and source-access record; F07 methodological cautions applied conditionally.

**Confidence:** High for reporting scope; no effect estimate exists. **Limit / next discriminating question:** Obtain appropriate interactive evidence and representative access evaluation after separate approval.

### C-15

**Statement:** Shared guidance is transferred from selected reviewed-draft bytes with original limitations; F03/W03 author context and missing F04/F05 bodies remain distinct.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Actual archive selection receipt, inspected topic/pattern passages and readable author-packet excerpts; complete details in the G06 packet.

**Confidence:** High for the recorded local provenance boundary. **Limit / next discriminating question:** Resolve source bodies, reviews and central deduplication before claiming additional dependencies.

### C-16

**Statement:** A hybrid requires resolving execution, role and expedition conflicts explicitly rather than letting one genre label decide.

**Class:** `inference`. **Support/locator:** `GDR-SRC-20261010-G06-014`; Working G06 scopes and publisher dungeon-crawler inspiration; conflicting design goals are stated assumptions.

**Confidence:** Moderate as a useful comparison, not a universal genre hierarchy. **Limit / next discriminating question:** Do preparation and switching policies preserve the actual chosen role and encounter promise?

## References



Source identities are temporary G06 identities. Access was checked on 2026-10-10; unnumbered web pages are not authenticated retail builds. An observed example below means an inspected source artifact, not a played game. Canonical URL/edition deduplication remains pending.



### GDR-SRC-20261010-G06-006

**Joe Shely, Lead Game Designer; Blizzard Entertainment, with Luis Barriga introduction.** *Diablo IV Quarterly Update — December 2020*. Publication/update: 2020-12 (month identified by title; exact day not established).

[Inspected source route](https://news.blizzard.com/en-us/article/23583664/diablo-iv-quarterly-updatedecember-2020). Edition/build: Pre-release design update explicitly subject to change. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Firsthand design rationale.

**Locator:** Skill Tree/respecialization; Weapon Types; Item Qualities; closing not-final caveat (retrieved lines 50–54, 75–102, 124–128). **Claims:** C-04, C-11.

**Limits:** Costed respec and equipment differentiation are intentions at this development date, not current rules or validated benefits. **Independence:** Same production lineage as sources 007–009; temporal change is not an independent replication. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-007

**Blizzard Entertainment.** *Master the Occult in Season of Witchcraft*. Publication/update: unknown publication day; Season of Witchcraft / 2.1 launch context, January 2025.

[Inspected source route](https://news.blizzard.com/en-us/article/24167111/master-the-occult-in-season-of-witchcraft). Edition/build: Historical 2.1 feature announcement; no current-client behavior verified. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary feature announcement.

**Locator:** Eternal Updates: The Armory, and More → The Armory (retrieved lines 460–467). **Claims:** C-05, C-11.

**Limits:** Bundle capture, missing-item indication and the stated no-Gold Paragon-loadout switch are documented. Does not promise all respec operations everywhere are free, or supply usability outcomes. **Independence:** Same studio/game as 006, 008 and 009; feature account and bug notes answer different questions. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-008

**Blizzard Entertainment.** *Diablo IV Patch Notes (2.1)*. Publication/update: 2025-03-04 for the inspected 2.1.3 section.

[Inspected source route](https://news.blizzard.com/en-us/article/24171214/diablo-iv-patch-notes-2-1). Edition/build: 2.1.3 Build #62672, All Platforms; surrounding compilation contains other versions. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary developer defect/fix report.

**Locator:** Vessel of Hatred → Bug Fixes: absent warning for an Armory loadout with more than two Runewords; Base Game → Bug Fixes → Accessibility: screen-reader warning when refunding a connecting Paragon node (retrieved lines 45–63, 154–159). **Claims:** C-06, C-11, C-13.

**Limits:** Reported defects/fixes were not reproduced; no incidence rate, user sample or proof of complete repair is supplied. **Independence:** Same underlying product as 007/009. Negative implementation evidence, not an independent efficacy test. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-009

**Blizzard Entertainment.** *Combatting Demons with Accessibility in Diablo IV*. Publication/update: unknown inspected publication day; original launch-context feature article.

[Inspected source route](https://news.blizzard.com/en-gb/article/23954932/combatting-demons-with-accessibility-in-diablo-iv). Edition/build: Launch-context accessibility description; not current-platform certification. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary accessibility feature account.

**Locator:** Dexterity Assistance; Vision Assistance → audio cues and screen reader (retrieved lines 32–46, 66–86). **Claims:** C-07, C-13.

**Limits:** Remapping, toggle/targeting and narration are feature descriptions, not measured access or equivalent experience; linked video not viewed. **Independence:** Same studio as 006–008. Source 008 supplies a later narrow failure case rather than negating every feature. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-010

**Crate Entertainment.** *Guide — Gameplay — Combat*. Publication/update: unknown.

[Inspected source route](https://www.grimdawn.com/guide/gameplay/combat/). Edition/build: Mutable official Grim Dawn guide; exact game build not supplied. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary game-system documentation.

**Locator:** Landing Hits and Critical Hits; Flat vs. Percent Damage (retrieved lines 136–154). **Claims:** C-01, C-02, C-10.

**Limits:** The documented attack/defense and modifier distinctions support a diagnosis vocabulary, not a numerical prescription or observed client outcome. **Independence:** Same game/documentation family as 011; different production from Blizzard. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-011

**Crate Entertainment.** *Guide — Character — Devotion*. Publication/update: unknown.

[Inspected source route](https://www.grimdawn.com/guide/character/devotion/). Edition/build: Mutable official Grim Dawn guide; exact game build not supplied. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary game-system documentation.

**Locator:** Unlocking Constellations; Affinity; Celestial Powers; Resetting Devotion Points (retrieved lines 154–205). **Claims:** C-01, C-03, C-11.

**Limits:** Prerequisites, valid trigger bindings and refund dependencies are documented. Numerical caps and current expansion parity are not imported. **Independence:** Same documentation family as 010; not two independent player datasets. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-014

**Cristina Anderca / Mojang Studios.** *Minecraft Dungeons is here!*. Publication/update: 2020-05-26.

[Inspected source route](https://www.minecraft.net/en-us/article/minecraft-dungeons-here-). Edition/build: Launch article; no contemporary sequel or current build inferred. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary publisher launch account.

**Locator:** Minecraft… what now? (retrieved lines 518–528); byline/date at 509–512. **Claims:** C-01, C-08, C-16.

**Limits:** No fixed classes, equipment-based specialization and generated levels are described. Dungeon-crawler inspiration is not an authoritative resolution of RPG/action-adventure boundaries. **Independence:** One Mojang production; language mirrors and the current product page are derivative routes, not added corroboration. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



## Unresolved contradictions and tradeoffs

Packet-local records `G06-CON-02`, `G06-CON-03`, `G06-CON-05` remain open in the [contradiction register](../reviews/full-run-20261010-g06-review-packet.md#contradictions-and-competing-explanations). They are not globally allocated CON IDs. A tradeoff is not called an empirical contradiction when the goals, date or system differ.

## Review and history

Version 0.1.0, candidate revision `initial-research-1`, attempt `G06-attempt-1`, first submission. No predecessor or supersession is asserted. Author self-review is recorded in the [G06 review packet](../reviews/full-run-20261010-g06-review-packet.md); it is not independent review. Byte identity is in the detached [integrity receipt](../reviews/full-run-20261010-g06-integrity.md). Coverage remains open. Gate C independent review, Gate D host retrieval and Gate E acceptance/release remain uncompleted. No prototype, participant recruitment or playtest was performed.
