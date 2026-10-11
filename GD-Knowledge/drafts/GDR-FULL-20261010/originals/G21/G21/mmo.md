---
id: GDR-CAND-20261010-G21-GEN-01
kind: genre
title: MMO
version: 0.1.0
status: draft
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G21
candidate_revision: initial-authoring-1
attempt_id: G21-authoring-01
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: coverage-open
independent_review: not-performed
aliases:
- massively multiplayer online
- persistent shared world
tags:
- persistence
- social-roles
- asynchronous-exchange
- re-entry
- economy
- coverage-open
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-G21-PAT-01
- GDR-CAND-20261010-G21-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G21-GEN-02
- GDR-CAND-20261010-G21-GEN-03
source_ids:
- GDR-SRC-20261010-G21-001
- GDR-SRC-20261010-G21-002
- GDR-SRC-20261010-G21-003
- GDR-SRC-20261010-G21-004
- GDR-SRC-20261010-G21-005
- GDR-SRC-20261010-G21-019
- GDR-SRC-20261010-G21-020
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
hash_record: ../reviews/full-run-20261010-g21-review-packet.md
---

# MMO

**Research candidate, not released knowledge.** This entry helps choose the form of persistence, social dependence and return experience in a shared world. It does not prescribe an MMO architecture, business model, population target, content schedule or moderation implementation. Definitions and recommendations are provisional inferences or hypotheses, not approved studio design choices.

## Definition and contested boundaries

For this entry, **MMO** means a game organized around a continuing shared world or society in which a player’s activity can matter beyond a fixed encounter party and a single session. Persistence may concern people, possessions, institutions, territory, markets or authored world history. This is an operational research definition, not an official standard. A large concurrent audience alone is insufficient; a small visible instance can still participate in a broader persistent world. An account level and a chat lobby alone do not establish that world relationship. [C-01]

MMO and MMORPG are not interchangeable. Palia’s 2023 design account centers community simulation; Illyriad describes persistent browser strategy and a market with standing offers. These are useful boundary challenges to a combat-and-raid-only account, without establishing that every advertised MMO meets one universally agreed definition. EVE’s documented offline skill training is an asynchronous subsystem, not proof that the whole game is turn-based or asynchronous. [C-02; C-03; C-04]

Separate **world continuity** from **uninterrupted co-presence**. Players can influence the same economy at different times. Conversely, two players can occupy the same place without wanting to group. Shards, instances, resets and seasons require explicit treatment: what survives, which relationships remain possible, and what the player reasonably expects to carry forward? A season reset is not automatically disqualifying, but “persistent” must not conceal the destruction of valued state. The usefulness of this boundary remains open to taxonomy review. [C-01; C-05]

## Custom research instructions

Investigate the actual persistence unit before counting players. Trace one contribution across logout, ownership transfer, population decline and a content update. Ask whether the same rules apply to individuals, groups, territory and inventories. Record shard, server, region, platform and patch for any future gameplay observation. [C-06]

Sample materially different participation: co-present independent play, small-party collaboration, guild organization, economic specialization, contested territory, community simulation and asynchronous exchange. Treat role labels as jobs with dependencies, not player personalities. Challenge the comparisons “more mandatory grouping means more community,” “offline accumulation removes time pressure,” and “scarcity restores meaning.” The sources here do not establish those generalizations. [C-05; C-07; C-08]

For empirical work, distinguish characters from people, active players from returners, guild members from nonguild members, and observed attendance from preferred attendance. Seek original longitudinal work and contrary cases involving departing players and people unable to meet schedules. For creator accounts, locate what actually shipped separately from what was intended. Audit less combat-centered and asynchronous designs without assuming they are socially safe, inexpensive to maintain or automatically accessible. [C-06; C-17]

## Player promises and varied audiences

Candidate promises include continuity of identity, recognizable contribution, social presence, collaborative achievement, economic agency and consequential conflict. They are research hypotheses, not universal reasons to play. A trader may value a reliable market without wanting a combat role; a friend group may prioritize staying together over optimized matchmaking; a returning player may value continuity but reject an obligation to recover months of missed rewards. Test these separately rather than collapse them into “engagement.” [C-07]

The historical *Alone Together?* study combined participation with census observations of 129,372 characters across five World of Warcraft servers beginning in 2005. Its grouping and progression observations distinguish co-presence from formal grouping; they neither identify all unique people nor show that compulsory grouping causes satisfaction. That distinction motivates offering different social entry points, not the claim that solo play is always superior. [C-05; GDR-SRC-20261010-G21-001]

## Characteristic loops and mechanisms

### Persistent state creates opportunities and obligations

An action can change a shared condition; that condition can outlast the actor’s session; a later participant can benefit, respond or lose access. The state transition is logically possible once persistence is implemented. Whether it produces belonging, anxiety or meaningful consequence is unvalidated here. Before selecting it, specify who can change the state, whose consent is needed, what is recoverable and how affected players learn what happened. [C-06]

**Proposed application:** map player-owned, group-owned and world-owned state separately. Compare reversible contribution, durable contribution and destructive interference. Choose the least irreversible structure that still supports the intended experience. A territorial conflict game may deliberately select irreversible losses; a community garden may preserve personal work while allowing shared additions. Neither choice should be smuggled in through an undifferentiated “MMO persistence” requirement. [C-06; C-17]

### Roles: useful interdependence versus attendance bottlenecks

A contribution becomes socially legible when another person can recognize how it changes an opportunity. Requiring a unique role can create coordination, but can also make everyone wait for one person. These are mechanism hypotheses, not measured effects. Diagnose whether the desired job is complementary expertise, logistical preparation, emotional leadership or merely a mandatory unlock. [C-07]

For a synchronous challenge, compare fixed specialist slots with substitutable capabilities, adjustable tasks or preparation performed earlier. For asynchronous exchange, describe delivery, reservation, expiry, cancellation and attribution. A public contribution ledger can clarify ownership but also become a surveillance or status-ranking device. Do not expose attendance patterns or private reasons for absence merely to prove contribution. [C-07; C-17]

Illyriad’s official trade overview documents standing buy/sell offers and later acceptance; its philosophy calls for a world that continues after logout. Together these provide a concrete asynchronous interaction route, not evidence that its participants feel less pressure. Scheduled encounters and separate-time contributions answer different coordination problems and should not be substituted without examining what players value. [C-04]

### Progression and economy: test the distribution of opportunity

EVE documents real-time training independent of login. This separates training progress from continuous execution, but does not demonstrate equal access, equal opportunity or relief from obligation. Consider what a returner can actually do with others, not only whether a number increased. Horizontal specialization, vertical growth, catch-up access and temporary scaling each redistribute opportunities and costs; none is a universal MMO default. [C-03; C-08]

CCP’s 2020 redistribution account proposed differentiated mineral supply and expected changes in activity while acknowledging a painful transition. Its stated economic goal is not validation that increasing scarcity benefits every player. The applicable question is distributional: whose replacement costs rise, who controls supply, and who still has a viable route into meaningful participation? [C-09; GDR-SRC-20261010-G21-004]

Before recommending a sink or bottleneck, distinguish stocks, flows, transport access, transaction friction, substitute goods and ownership concentration. Compare reduced supply against improved access, alternative production or less dependence on replacement equipment. A design can create trade by making people mutually useful, but can also create a gate controlled by incumbents. Price changes alone cannot distinguish those experiences. No live-economy adjustment is proposed or performed. [C-10]

### Onboarding, re-entry and content cadence

The inspected EVE return guide treats return as more than remembering controls: account access, assets and changed circumstances are part of the problem. The reviewed F01 guidance suggests reconstructing the player’s intention, relevant state, changes and a safe next action. Transferring that hypothesis to an MMO requires first checking whether the old intention is still possible. [C-11]

Use a **same-rule** understanding probe only when the rule really is unchanged. Vary cases so both permitted and prohibited actions occur, and separate correct prediction from choosing to take an action. When an update changes the rule, explain the change before evaluating understanding; do not classify a correct old-rule answer as evidence of forgetting. Preserve captions, input accommodations, state displays and optional help while reducing only answer-leading prompts. These are retained F01 review corrections, not newly validated learning effects. [C-12]

For cadence, inventory the recurring work behind each promise: authoring, economy migration, localization, access testing, abuse handling, support and retirement. Compare recurring authored events with systemic variation and finite, revisit-able chapters. An attendance deadline may coordinate a festival, but can also exclude people in other time zones or with variable availability. Do not infer that logged-in time establishes value, that more content is necessary, or that player-created content transfers the operator’s responsibilities away. [C-13; C-17]

## Practical application: from question to reversible candidate

1. **Diagnose continuity.** Write what continues after logout and whose action can alter it. Identify irreversible harm and the real unit of consent. [C-06]
2. **Choose participation contracts.** Offer or deliberately exclude synchronous, asynchronous and independent participation for stated reasons. Record who must wait, who bears failure and whether the invitation is actually optional. [C-07]
3. **Map access and economy.** Follow a newcomer, a returner and a specialist through the same goal. Identify information, skill, wealth, relationship and permission gates separately. Compare at least one lower-dependency alternative. [C-08; C-10]
4. **Prototype on paper before operating a world.** Walk through absence, scarcity, a rule update, a missing specialist and a contested contribution. Log contradictions rather than invent server capacity estimates. [C-18]
5. **Evaluate the chosen promise.** Seek evidence of comprehension, viable participation and experienced obligation, not just session length. Stop or narrow the feature when the operator cannot support its continuing obligations. All tests below are proposed, not performed. [C-13; C-18]

## Applying shared topics

The following are adaptations of **inspected, parent-selected reviewed drafts**, still unreleased. Exact selected hashes and excerpt locators are in the [dependency receipt](../reviews/full-run-20261010-g21-review-packet.md#inspected-reviewed-dependencies). Upstream studies cited inside those drafts were not thereby reinspected here.

| Shared identity | What this genre changes |
|---|---|
| `GDR-CAND-20261010-F01-TOP-03`, learning and onboarding | Re-entry must reconcile persistent permissions, possessions and changed rules, not automatically replay a beginner tutorial. |
| `GDR-CAND-20261010-F02-TOP-01`, decision design | An information contract extends across absence, counterparties and differing access to world knowledge. Do not expose hidden plans through support tools. |
| `GDR-CAND-20261010-F07-TOP-01`, evaluation and balancing | Use population and participation denominators; a guild raid census cannot represent everyone with an account. |
| `GDR-CAND-20261010-F07-TOP-02`, ethical and sustainable design | Price continuing support and refusal costs, including dependence on unpaid leaders or moderators. |
| `GDR-CAND-20261010-P01-TOP-03`, accessibility and inclusive interaction | Evaluate persistent navigation, communication and administration as well as momentary combat. No universal native-game size/timing threshold is transferred. |
| `GDR-CAND-20261010-P02-TOP-03`, multimodal communication | Make legitimate state and invitations available through usable channels without revealing private activity or hidden opponents. |

Missing selected guidance remains missing: F03 progression/economies, F06 multiplayer/session systems, W03 world/spatial structure and relevant P03/P05 platform/localization material. Their proposed relationships are recorded in the packet, not presented as inspected accepted guidance. [C-19]

## Pattern selection, hybrid conflicts and alternatives

The inspected `GDR-CAND-20261010-F01-PAT-01` supports the qualified re-entry adaptation above. `GDR-CAND-20261010-F07-PAT-02` asks how commitment, refusal, interruption and return work; it does not promise loss-free departure from an already agreed shared encounter. `GDR-CAND-20261010-P02-PAT-02` supplies fact-preserving cue alternatives rather than sensory equivalence. [C-12; C-14; C-15]

The new [Public pressure, private position](../patterns/public-pressure-private-position.md), `GDR-CAND-20261010-G21-PAT-01`, is applicable only when an MMO activity deliberately has public deadlines and hidden competing positions. It is unnecessary for an unpressured persistent market or private garden. [Bounded return before final elimination](../patterns/bounded-return-before-final-elimination.md), `GDR-CAND-20261010-G21-PAT-02`, belongs only to a bounded activity with a real terminal result; it is not a substitute for defining persistent character death. Both are untested candidates. [C-16]

An MMO–MOBA hybrid must reconcile persistent equipment advantage with match-local role learning and comparable starting opportunities. An MMO–battle-royale hybrid must specify whether defeat ends only the match or destroys durable possessions. A community-simulation hybrid may reject destructive competition while retaining shared production. These are conflicts to resolve explicitly, not promises that all three can be optimized simultaneously. [C-16]

## Representative cases, negative cases and worked example

**Documented range.** Palia supplies a less combat-centered design intention; EVE supplies offline progression and a changing economy; Illyriad supplies persistent strategy and standing exchanges; historical World of Warcraft observations challenge mandatory-grouping assumptions. These cases were chosen for structural contrast, not market success, and are not a representative sample of all MMOs. [C-02–C-05; C-09]

**Illustrative worked example — canal restoration.** A fictional shared-world settlement needs repairs. One player surveys a route during an active session, another leaves a materials offer, and a third performs construction later. Each can see an authorized task state, what is reserved and what remains useful. The repair is optional; refusing it does not remove personal housing. Credit records contributions without publishing absence or real-world availability. This is invented design material, not a shipped case or test result. [C-07; C-17]

Walk the edge cases before choosing it: a donor cancels before acceptance; several builders reserve the same material; the survey expires after a flood; a new player arrives after all visible work is complete. Alternatives include personal commissions, refreshed optional tasks or simply allowing observation. If the only way to make the settlement feel populated is to require daily repair labor, reject the community promise or redesign the task. A persistent war scenario could legitimately choose attackable supply lines instead, but must state that different contract. [C-06; C-10; C-18]

**Strong counterexample.** A group seeking mutual dependence and reliable appointments may dislike substitutable roles or anytime contribution. The recommendation is therefore not to remove obligation universally; it is to make the obligation discoverable and test whether that audience actually chooses it. Likewise, a fully instanced cooperative game may satisfy the social goal more cheaply than maintaining a persistent world. [C-07; C-13]

## Accessibility, ethics, localization and production

Treat low-vision navigation, hearing differences, communication preferences, variable attention, fatigue, motor demands and interrupted availability as task constraints to investigate, not interchangeable diagnosis labels. A player may need long-term inventory/market access even when combat is accessible. Optional voice requires workable text or structured communication routes; icons require language and context testing. A slower asynchronous interaction can still exclude someone through short expiry or inaccessible administration. [C-15; C-17]

Separate rule-permitted rivalry from harassment, exclusion and off-platform abuse. Poor performance, unfamiliarity or declining a channel is not itself evidence of malicious intent. Proposed safeguards include comprehensible conduct boundaries, usable reporting, contextual review and an appeal route, with staffing and privacy costs budgeted. These are review hypotheses; this packet neither verifies a live moderation system nor declares legal compliance. [C-17]

Account lifecycle, regional scheduling, translation maintenance and retirement communication are production dependencies, not optional post-launch decorations. No current hosting cost, network capacity, geographic latency target, monetization rule or universally safe session duration is established here. [C-13; C-19]

## Research questions and proposed validation

**All procedures below are proposed and not performed.** Obtain separate approval for recruitment, incentives, participant privacy and any prototype. Decide sample size and stopping rules from the local question and observed variation; no universal sample guarantee is supplied. [C-18]

| Discriminating question | Comparison and participants | Measures, confounds and rejection rule |
|---|---|---|
| Does optional asynchronous contribution preserve recognition without unwanted obligation? | Same fictional project with appointment-only versus separated-time tasks; include time-constrained participants, established groups and nongrouped players. | Track correctly understood contribution state, missed opportunities, chosen participation and reported obligation. Prior friendship and task value confound comparisons. Reject the adaptation if recognition remains poor or the nominally optional route still pressures attendance. |
| Does a changed-world recap help returning players? | State/change recap versus full tutorial replay, with unchanged-rule and changed-rule cases separated. Preserve equivalent access support. | Record legitimate next-action prediction, permission errors, unsupported assumptions and unwanted information leaks. Old build knowledge and prior account status matter. Reject automatic recap benefits if its advantage is absent or it obscures changed rules. |
| Does scarcity open trade or close participation? | Paper economy scenarios with alternative supply/access changes, holding goals explicit. Include newcomers, low-wealth participants and incumbent specialists. | Examine viable routes, dependency concentration, replacement burden and stated value. No live prices or purchases. Reject a scarcity recommendation if apparent activity rises while relevant groups lose all reasonable routes. |

## Claim ledger

Confidence concerns the precise claim, not whether the genre is “proven.” Dependency references below point to the exact selected draft receipt, not unseen canonical guidance.

| Claim | Precise proposition / class | Support and locator | Confidence and unresolved limit |
|---|---|---|---|
| C-01 | Operational MMO boundary centers continuing shared relationships; `inference`. | `GDR-SRC-20261010-G21-002` main account; `GDR-SRC-20261010-G21-019` trade; `GDR-SRC-20261010-G21-020` Persistence. | Moderate for a useful distinction; genre membership and seasonal boundaries remain contested. |
| C-02 | Palia’s account is community-simulation-centered; `observed-example` of a document. | `GDR-SRC-20261010-G21-002`, main article. | High for stated design framing, not shipped efficacy. |
| C-03 | Offline skill training is an asynchronous subsystem; `observed-example` of documentation. | `GDR-SRC-20261010-G21-003`, Skill Training. | High for the page, current build and wellbeing unverified. |
| C-04 | Illyriad documents standing offers and a persistence intention; `observed-example` of documents. The separated-action adaptation is C-07. | `GDR-SRC-20261010-G21-019`, marketplace paragraph; `GDR-SRC-20261010-G21-020`, Persistence. | High documentary confidence; moderate inference; whole-game asynchrony not claimed. |
| C-05 | Co-presence is not equivalent to formal grouping; `empirical-evidence`. | `GDR-SRC-20261010-G21-001`, preprint pp. 2–4, 9. | Moderate: large historical character census, selection and causal limits. |
| C-06 | Map persistence, authority and reversibility before selecting consequences; `hypothesis`. | C-01/C-04 plus inspected F02 information-contract excerpt. | Low for player benefit; logical dependency is clearer than its experiential effect. |
| C-07 | Offer participation contracts matched to desired dependence; `hypothesis`. | C-04/C-05; reviewed F07 commitment/refusal guidance. | Low; compulsory cooperation may be valued by a selected audience. |
| C-08 | Offline or vertical progression does not establish usable social access; `inference`. | `GDR-SRC-20261010-G21-003` mechanics versus proposed access-path analysis. | Moderate for non-equivalence; no comparative progression study here. |
| C-09 | CCP’s scarcity rationale is intent, not validated benefit; `practitioner-heuristic`. | `GDR-SRC-20261010-G21-004`, opening and Closing Notes. | High attribution, low generalized effect confidence. |
| C-10 | Inspect distribution of opportunity before scarcity changes; `hypothesis`. | C-09; `GDR-SRC-20261010-G21-019` standing exchange; F02 decision-contract reasoning. | Low; no live-economy experiment performed. |
| C-11 | EVE’s support scope includes changed circumstances, not only memory; `observed-example` of a document. The proposed learning adaptation is C-12. | `GDR-SRC-20261010-G21-005`, main article; F01 topic re-entry. | Moderate; recap effectiveness remains untested. |
| C-12 | Same-rule transfer and changed-rule teaching must be distinguished; `inference`. | Selected F01 pattern, corrected worked example and application limits. | High for preserving the reviewed distinction; low for G21 learning benefit. |
| C-13 | Cost recurring obligations and compare less content-intensive alternatives; `hypothesis`. | F07 ethical topic, sustaining-a-promise excerpt. | Low benefit confidence; no workload or retention study conducted here. |
| C-14 | Exit design must disclose teammate consequences rather than erase all stakes; `inference`. | Selected F07 safe-exit pattern, commitment/refusal/return. | Moderate reasoning, implementation-specific. |
| C-15 | Access alternatives should preserve authorized facts; `inference`. | Selected P01 accessibility and P02 cue/multimodal excerpts. | Moderate scoped guidance; no native numeric threshold or equivalent experience claimed. |
| C-16 | Pattern use and hybrid compromises depend on the actual activity; `hypothesis`. | G21 PAT-01/PAT-02 and genre definitions. | Low; genre tags alone do not establish fit. |
| C-17 | Investigate social pressure, abuse and privacy without diagnosing from participation; `hypothesis`. | F07 ethical/commitment excerpts; limits of C-05. | Low mechanism confidence; no moderation efficacy or legal conclusion. |
| C-18 | Proposed comparisons can discriminate the stated alternatives; `hypothesis`. | C-06–C-17; reviewed F07 evaluation excerpt. | Low until method review and execution; no participant results. |
| C-19 | Listed later selected dependencies were not inspected here; `observed-example` of research access. | G21 review packet, missing dependency register. | High for this session’s access, not global availability. |

## Coverage, contradictions and review history

Research covers persistence boundaries, varied participation, asynchronous exchange/progression, economy decisions, re-entry and operating obligations. Coverage remains open for current runtime observations, persistent-world shutdowns, cross-platform population structure, modern causal social studies, region-specific access and moderation outcomes. MMO-specific conflict records are `G21-CON-01` and `G21-CON-02`; see the [review packet](../reviews/full-run-20261010-g21-review-packet.md#contradictions-and-tensions).

`0.1.0`, `initial-authoring-1`: new bounded G21 candidate; no known predecessor bytes or supersession. Author self-review is in the packet; independent review has not occurred. Candidate hash is external to this file to avoid a self-referential checksum. Next decision: review the operational boundary and the participation-contract recommendation, including the strongest case for deliberately mandatory collaboration.

## References

All sources were inspected on **2026-10-10, America/Los_Angeles session date**. Access describes the material actually read, not the availability of an entire website. No game client or recording was observed; game examples below are observations of official documentary artifacts. No third-party pages linked by these documents are implicitly inspected. Source identities are run-scoped; central URL/DOI/edition deduplication remains pending. Rights: copyrighted material is paraphrased; no screenshots, substantial quotations, chat logs or source PDFs are redistributed. No reuse license is assumed.

### GDR-SRC-20261010-G21-001

Nicolas Ducheneaut, Nicholas Yee, Eric Nickell and Robert J. Moore. *“Alone Together?” Exploring the Social Dynamics of Massively Multiplayer Online Games*. 2006. ACM, CHI 2006. [Inspected source](https://www.nickyee.com/pubs/Ducheneaut,%20Yee,%20Nickell,%20Moore%20-%20Alone%20Together%20(2006).pdf). DOI: `10.1145/1124772.1124834`.

**Version/build:** Author-hosted preprint, printed pp. 1–10; proceedings pp. 407–416; historical World of Warcraft observations, client build unknown. **Access:** `relevant-excerpt`; Preprint pp. 2–4, methods and grouping; p. 9 discussion. PDF pages 1, 3, 4 and 9 also visually inspected. **Type:** original empirical paper. **Supports:** C-05. **Limits and independence:** Census characters are not unique people; historical servers and observational associations, not randomized grouping effects. Author-hosted copy of the ACM paper, not a second study.

### GDR-SRC-20261010-G21-002

Singularity 6. *Building a Cozy Sim MMO*. 2023-08-01. Palia / Singularity 6. [Inspected source](https://palia.com/news/building-a-cozy-sim-mmo).

**Version/build:** Pre-closed-beta design account; runtime build unverified. **Access:** `relevant-excerpt`; Main article, paragraphs on community simulation, solo/friends and connected play; retrieved lines 17–59. **Type:** firsthand developer account. **Supports:** C-01/C-02. **Limits and independence:** Intent and positioning, not measured community or wellbeing benefit. Contemporary website navigation does not update the 2023 account.

### GDR-SRC-20261010-G21-003

Lead GM Carbon / CCP Games. *Skill Training*. updated 2024-07-01. EVE Online Help Center. [Inspected source](https://support.eveonline.com/hc/en-us/articles/203217062-Skill-Training).

**Version/build:** Support-page revision; runtime build unknown. **Access:** `relevant-excerpt`; Main article, real-time/offline training and skill prerequisites; retrieved lines 29–44. **Type:** official mechanics documentation. **Supports:** C-03/C-08. **Limits and independence:** Documents asynchronous progression, not an entirely asynchronous game or equal progression opportunities. Same production source family as 004 and 005.

### GDR-SRC-20261010-G21-004

EVE Development Team. *Resource Distribution Update*. 2020-09-25. CCP Games. [Inspected source](https://www.eveonline.com/news/view/resource-distribution-update).

**Version/build:** 2020 redistribution proposal/update account; subsequent balance not inferred. **Access:** `relevant-excerpt`; Opening; Redistribution Phase; Closing Notes. Ore tables not used as balance evidence. **Type:** firsthand developer account. **Supports:** C-09/C-10. **Limits and independence:** Expected economy changes and acknowledged pain are not an evaluated welfare outcome. Same CCP family as 003/005; linked ecosystem blog and stream not inspected.

### GDR-SRC-20261010-G21-005

Lead GM Carbon / CCP Games. *Returning to EVE Online*. updated 2026-06-23. EVE Online Help Center. [Inspected source](https://support.eveonline.com/hc/en-us/articles/6387243601180-Returning-to-EVE-Online).

**Version/build:** 2026 support revision; runtime build unknown. **Access:** `relevant-excerpt`; Main article: account access, assets and changes; retrieved lines 25–61. **Type:** official support documentation. **Supports:** C-11. **Limits and independence:** Support routing rather than a controlled re-entry study. Linked subsidiary articles were not inspected; same CCP family as 003/004.

### GDR-SRC-20261010-G21-019

Illyriad Games Ltd.. *Trade in Illyriad*. unknown. Illyriad. [Inspected source](https://www.illyriad.co.uk/GameInformation/Trade).

**Version/build:** Undated browser-game documentation; runtime version unknown. **Access:** `relevant-excerpt`; Amass Wealth in a Player-Driven Economy, paragraphs 1–4; retrieved lines 38–45. **Type:** official mechanics overview. **Supports:** C-01/C-04/C-10. **Limits and independence:** Persistent offers support separated transaction actions; no inspected study of asynchronous social benefit, population size or current prices. Same developer as 020.

### GDR-SRC-20261010-G21-020

Illyriad Games Ltd.. *Illyriad’s Guiding Principles*. unknown. Illyriad. [Inspected source](https://illyriad.co.uk/GameInformation/Principles).

**Version/build:** Undated design philosophy for persistent browser strategy. **Access:** `relevant-excerpt`; Persistence; Participation; Platforms; Playerbase; retrieved lines 44–82. **Type:** firsthand design philosophy. **Supports:** C-01/C-04. **Limits and independence:** Persistence is creator intent; broad claims about player-created content and community are not adopted as proven. Same production account family as 019.

