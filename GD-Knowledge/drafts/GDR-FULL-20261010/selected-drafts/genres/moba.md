---
id: GDR-CAND-20261010-G21-GEN-02
kind: genre
title: MOBA
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
- multiplayer online battle arena
- team action strategy
tags:
- team-roles
- lanes
- objectives
- asymmetric-information
- match-progression
- communication
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
- GDR-CAND-20261010-G21-GEN-01
- GDR-CAND-20261010-G21-GEN-03
source_ids:
- GDR-SRC-20261010-G21-006
- GDR-SRC-20261010-G21-007
- GDR-SRC-20261010-G21-008
- GDR-SRC-20261010-G21-009
- GDR-SRC-20261010-G21-010
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
hash_record: ../reviews/full-run-20261010-g21-review-packet.md
---

# MOBA

**Research candidate, not released knowledge.** This entry helps choose team responsibilities, spatial objectives, match-local progression, information and recovery. It does not supply a universal format, balance target, role composition, surrender threshold or toxicity model.

## Definition and contested boundaries

Here **MOBA** denotes a family of competitive team games organized around differentiated controllable agents, repeated spatial/objective decisions and interactions between momentary execution and match-scale development. This is a working analytical boundary, not a formal standard. The literal expansion, “multiplayer online battle arena,” is too broad to settle membership: not every multiplayer arena fight presents the same design problems. [C-01]

League’s official introduction describes base destruction, lanes, jungle objectives and individual gold/experience in its principal illustrated mode. Blizzard’s Heroes introduction instead describes shared experience, talents and unusual control arrangements. Pokémon UNITE’s overview culminates in scoring rather than destroying a Nexus-like base. These differences make a single shop, lane count, control arrangement or terminal objective an unreliable universal definition. [C-02; C-03; C-04]

Treat MOBA, action strategy, hero shooter and team brawler as neighboring labels whose usefulness depends on the decisions being analyzed. A hero roster alone does not make a shooter a MOBA. A score-based objective does not automatically remove MOBA-like resource and rotation decisions. Record which structures are present before borrowing a rule; do not declare an uncontested taxonomy from these examples. [C-01]

## Custom research instructions

Start from the **win condition and resource flow**, not an assumed map. Identify who controls which agents, where power comes from, whether resources are individual or shared, what knowledge is hidden, what structures or objectives change future opportunities, and how a match can end. Separate enforced rules, developer-recommended positions and learned community conventions. [C-05]

Research at least contrasting base-destruction, shared-progression and score-ending formats. Examine jobs beyond damage: information gathering, protection, resource access, wave control, interception and objective conversion. Challenge “shared experience removes blame,” “one weak teammate causes every loss,” “more comeback aid is fairer,” and “voice is necessary for teamwork.” Neither a developer description nor a report dataset establishes those propositions. [C-05; C-08; C-10]

For each empirical source, record the actual region/server, season, mode, skill range, party familiarity, communication channels and unit of observation. Distinguish observed reports from independently established misconduct. Seek losing and winning cases, failed interventions, muted players, newcomers and non-English-language populations. Regional comparisons must not become stereotypes about national character. [C-10; C-11]

## Player promises and varied audiences

Candidate promises include contributing through a differentiated role, recognizing a consequential tactical choice, learning interactions, coordinating with allies and finding a meaningful next decision after a setback. These promises are hypotheses. A practiced team may want strict dependencies and rich communication; a mixed-skill friend group may prioritize staying together; a newcomer may need a comprehensible job before optimal resource efficiency matters. [C-06]

Do not equate enjoyment with winning, mastery with high action rate, or team contribution with a single score column. A support action can prevent an event that never appears in a kill tally; conversely, a claimed “support” role may actually have no useful influence in the chosen rules. Investigate both possibilities through task opportunities and decisions, not role branding. [C-06; C-16]

## Characteristic loops and causal questions

### Jobs, lanes and objective conversion

A useful role specification describes an opportunity and a dependency: secure a route so an ally can reach an objective; gather information so the team can distinguish contesting from trading elsewhere; preserve a resource so it is available for a later engagement. The value of that job is a hypothesis until the surrounding rules make the consequence possible and players can recognize it. [C-05; C-06]

Begin by writing the terminal objective and work backward through the actions that can advance it. In a base-destruction format, local success must be convertible into structural or positional opportunity. In a score-ending format, an advantageous fight may be worthless if it prevents timely scoring. In a shared-progression format, “give this player the resource” can become a different decision from individual purchase timing. These are conditional deductions from the documented structural differences, not demonstrations of superior design. [C-02–C-05]

The League guide’s lane positions are recommendations in that guide, not an instruction that every game must enforce identical roles. A designer considering hard role queues should compare compositional reliability against mixed-party access, waiting and flexibility. No queue duration or population threshold is established by this packet. [C-02; C-06]

### Resource, skill and escalation

Execution can affect access to resources; resources can change available actions; those actions can affect later control. This feedback chain is a proposed model to inspect, not an empirical law of snowballing. Identify each actual conversion and its delay. Separate execution advantage from item knowledge, information, team coordination and the opportunity to act. [C-07]

Choose progression deliberately. Individual spendable resources can support allocation and specialization but make ownership disputes salient. Shared progression can reduce that particular allocation decision while preserving other dependence and blame. Talent choices can change capabilities without a shop. None of these systems, by itself, proves that roles are equally useful or that players will understand why a team gained power. [C-03; C-07]

For recovery, write what the trailing team can still decide. A defensive objective, a trade on another route, a temporary advantage or a deliberate concession can create a meaningful response without restoring equal odds. Compare these with no special recovery assistance. Reject a proposed aid when it makes earlier achievements irrelevant for the intended audience or merely prolongs a result with no valued decisions. There is no universal comeback percentage or ideal win-rate target here. [C-08]

### Asymmetric information without inaccessible public state

Partition information into public rules/state, own-team information, sightings or estimates, and truly hidden opponent intentions. A timer for a public objective need not reveal whether an enemy is approaching it. A missing-agent alert is not verified current position. The reviewed F02 and P02 guidance supports preserving this distinction; its application to a particular competitive map remains a hypothesis. [C-09]

Represent a report’s provenance and age where they matter. Keep uncertainty when converting audio, animation or minimap events into another accessible channel. Otherwise an accommodation could inadvertently provide a fact that nobody legitimately knows, while an overcautious implementation could withhold an already-public fact. Correct the information contract first rather than treating one sensory channel as inherently more authentic. [C-09; C-15]

### Team communication is a design surface, not a conduct verdict

Riot’s Smart Ping page documents transient terrain/minimap signals and objective-intent voting. These provide an inspectable alternative to free text for some intentions, not evidence that pings replace all communication or reduce abuse. Familiar icon meaning cannot be presumed across languages and audiences. [C-12]

The proposed design choice is a layered communication system: task-relevant state is available without a live microphone; structured intentions handle common actions; optional richer discussion handles negotiation. Provide practical ways to suppress unwanted messages without concealing system-generated essential state. Test rate, ambiguity, repetition and the work imposed on recipients. Pings can also be misused; adding a wheel is not a moderation policy. [C-13]

Poor performance, a nonstandard but permitted strategy, unfamiliarity and declining voice are distinct from deliberately prohibited behavior. Game rules define what can happen; conduct policies define prohibited treatment of others; enforcement requires contextual evidence rather than automatically treating a lost match as proof of intent. This is a proposed ethical review distinction, not a statement about every current publisher’s policy. [C-10; C-13]

### What the empirical reporting evidence actually supports

Kwak, Blackburn and Han analyzed April 2013 Tribunal records covering 1,460,344 accused-player records, 6,016,046 matches and 10,898,958 reports across NA, EUW and KR. These were selected reported cases, not a census of all players or all abuse. Their outcome/reporting association does not establish that losing causes misconduct, and friendship and before/after behavior were unavailable. [C-10; GDR-SRC-20261010-G21-009]

The paper’s H4.2 predicted a higher pardon proportion for accused players on losing teams; the reported result was the opposite. Preserve that failed prediction. It does not justify treating losers as guilty, nor does the study validate a universal moderation intervention or a causal cultural explanation. [C-11]

## Practical application process

1. **Specify the ending.** State what wins, what merely contributes and what persists outside the match. Test whether a new player can distinguish these. [C-05]
2. **Map jobs and conversions.** For each intended role, identify its opportunities before, during and after a contested objective. Remove roles that are names without decisions; compare flexible versus enforced assignments. [C-06; C-07]
3. **Audit knowledge.** Mark public facts, team reports and hidden state. Prototype one decision using equivalent legitimate information across input/display options, not automatically more information. [C-09; C-15]
4. **Walk through a loss.** Trace remaining decisions, communication exposure, return after temporary defeat, surrender/exit implications and the terminal result. Disclose actual commitment rather than promise an exit without consequences. [C-08; C-14]
5. **Evaluate locally.** Separate comprehension, opportunity, coordination, conduct and satisfaction. A change can improve one and worsen another. Hold or revise it when the intended job disappears or a subgroup cannot participate. No player experiment was run. [C-16; C-18]

## Applying inspected shared topics and patterns

See the [selected dependency receipt](../reviews/full-run-20261010-g21-review-packet.md#inspected-reviewed-dependencies) for exact hashes, candidate identities and inspected sections. These references remain unreleased drafts; their underlying primary sources are not counted as G21 reinspection.

| Shared identity | Conditional MOBA adaptation |
|---|---|
| `GDR-CAND-20261010-F01-TOP-03` and `GDR-CAND-20261010-F01-PAT-01` | Teach a role’s decision rule using varied legal/illegal or effective/ineffective opportunities, not a single memorized lane route. A changed patch rule requires explanation, not a “failed transfer” label. Separate permission prediction from player preference; retain accommodations. |
| `GDR-CAND-20261010-F02-TOP-01` | Separate resource, opponent and future-state uncertainty; avoid calling all uncertainty poor readability. |
| `GDR-CAND-20261010-F07-TOP-01` | Evaluate roles with actual opportunity denominators, party and opponent context, not pick frequency alone. |
| `GDR-CAND-20261010-F07-TOP-02` and `GDR-CAND-20261010-F07-PAT-02` | Evaluate refusal, interruption and teammate costs before queue commitment; do not infer wellbeing from another completed match. |
| `GDR-CAND-20261010-P01-TOP-03`, `GDR-CAND-20261010-P02-TOP-03` and `GDR-CAND-20261010-P02-PAT-02` | Preserve authorized objective/ally state in accessible channels; test simultaneous minimap, combat and communication demands. No WCAG web number is imported as a universal native-game target. |

F03 progression/economy, F04 combat/movement, F06 social/session and W03 spatial guidance are missing as selected reviewed inputs here. P03 camera/platform and P05 localization/audio remain unresolved dependencies. Local genre hypotheses must not masquerade as their accepted shared guidance. [C-17]

The new [Public pressure, private position](../patterns/public-pressure-private-position.md), `GDR-CAND-20261010-G21-PAT-01`, can structure a public objective window while preserving enemy-position uncertainty. Do not apply its deadline recipe where discovering the event itself is the intended skill. [Bounded return before final elimination](../patterns/bounded-return-before-final-elimination.md), `GDR-CAND-20261010-G21-PAT-02`, is relevant only to an elimination variant; an ordinary temporary respawn within a continuing match is not automatically that pattern. [C-19]

## Representative cases, counterexamples and worked applications

**Documented structural contrast.** League’s principal illustrated mode has a base objective and individual purchases. Heroes documents shared progression and no item shop, including cases where agent control is not one player to one embodied hero. UNITE documents score conversion. These are document observations, not played-build observations, audience rankings or causal comparisons. [C-02–C-04]

**Illustrative application — contest or trade.** In a fictional lane-objective game, a team knows a public objective will become available. One ally has an old enemy sighting; another knows a side route is undefended only as of their last observation. Offer intentions to contest, delay or trade elsewhere, preserving the age of those observations. Measure whether players can state their uncertainty and the consequence of each option. Do not score every decision to contest as “correct”: preference, risk and information can justify another choice. [C-05; C-09; C-18]

**Illustrative contrasting application — score ending.** With limited scoring time remaining, the same team may prefer escorting a carrier to a fight that offers no useful score conversion. A tutorial copied from base-destruction play could reward the wrong objective. Author the practice around actual conversion rules and include a case in which declining the fight is sensible. The example is invented; no timing, team size or scoring balance is prescribed. [C-04; C-05; C-18]

**Strong counterexample.** A highly coordinated premade team may want deeper communication and stricter role commitments than structured pings or flexible roles support. Another format may deliberately emphasize individual allocation and accept that tension. The proposed communication layer must supplement rather than mechanically flatten those experiences. Conversely, adding shared XP does not remove opportunities to blame a teammate over positioning, drafting or objectives. That possible failure is not an observed outcome of the Heroes source. [C-07; C-13]

## Accessibility, cultural and production implications

Test simultaneous control, target selection, state reading and communication on the intended devices. Touch, controller and pointer interfaces impose different mapping choices, but no platform is intrinsically a simpler audience. Assistance must be evaluated against the intended task and information contract; latency, camera and assist differences need separate technical and competitive review before implementation. No universal reaction window or device-parity guarantee is established. [C-15]

Localize intentions and conduct examples, not just labels. “Retreat,” “missing” and a repeated warning can communicate strategy, uncertainty or blame depending on use. Include local speakers and people who avoid voice in future research; a regional server is not a reliable proxy for nationality or culture. Do not infer conduct from accent, disability, control method or chosen communication channel. [C-10; C-13; C-15]

Roster growth multiplies interactions that need readable feedback, counterplay, localization and regression review. Treat a proposed additional role as an operating cost and a potential access barrier, not automatically more strategic variety. Moderation capacity, reconnect behavior, reporting evidence and appeals need owner review; this draft does not design or operate enforcement automation. [C-16; C-17]

## Proposed validation, not performed

All studies need separate permission, participant safeguards and a locally justified sampling/analysis plan. Match or team observations are not independent simply because every player generates a row. [C-18]

| Question | Comparison and context | Measures, confounds and falsifying result |
|---|---|---|
| Can a role make useful decisions across match phases? | Paper/prototype objective scenarios with specialist versus substitutable jobs; mixed experience and premade versus unfamiliar teams. | Opportunity to influence, understood consequence, participation and preference. Team familiarity and opponent response confound success. Reject a role model when the job has no meaningful opportunity or only a hidden mandatory chore. |
| Does public objective information improve choice without leaking enemy state? | Equivalent scenarios with public-state channels varied; keep actual hidden information unchanged. | Public-rule understanding, erroneous opponent certainty, option diversity and access failures. Counterbalance familiarity. Reject if the aid teaches false certainty or only works for one sensory/input group. |
| Does a recovery rule preserve valued decisions? | Locally controlled lead states with/without one recovery mechanism; no universal comeback target. | Remaining chosen actions, understandability of advantage, perceived earnedness and willingness to continue. Skill and prior expectation matter. Reject if it mainly prolongs unwanted play or invalidates valued earlier choices. |
| Can nonvoice communication support the selected tasks? | Structured intentions with optional discussion versus existing interaction, without exposing participants to real harassment. | Correct interpretation, missed coordination, recipient workload and ability to suppress repetition. Language familiarity matters. Reject the proposed layer if essential jobs remain infeasible without mandatory voice. |

## Claim ledger

| Claim | Proposition / class | Support and locator | Confidence and limit |
|---|---|---|---|
| C-01 | A decision-family definition is more useful here than one universal format; `inference`. | `GDR-SRC-20261010-G21-006`–`GDR-SRC-20261010-G21-008` structural comparison. | Moderate analytical usefulness; membership contested. |
| C-02 | League’s guide documents a scoped base/lane/resource format; `observed-example` of a document. | `GDR-SRC-20261010-G21-006`, named guide sections. | High for documentation; patch and actual play unverified. |
| C-03 | Heroes documents shared XP, talents and nonstandard hero control; `observed-example` of a document. | `GDR-SRC-20261010-G21-007`, core concepts. | High scoped description, not benefit/current roster. |
| C-04 | UNITE’s overview describes point scoring as its ending criterion; `observed-example` of a document. | `GDR-SRC-20261010-G21-008`, Unite Battles. | High documentary scope; not all modes. |
| C-05 | Derive role decisions from actual victory/resource conversion; `hypothesis`. | C-02–C-04 plus F02 decision excerpt. | Low efficacy; structurally reasoned rather than experimentally validated. |
| C-06 | Role jobs should be examined through opportunities and dependencies; `hypothesis`. | C-05; F07 evaluation and commitment excerpts. | Low; strict dependence may suit a selected group. |
| C-07 | Resource-sharing choices move rather than automatically remove coordination costs; `inference`. | C-02/C-03; alternative dependency reasoning. | Moderate non-equivalence; no comparative effect study. |
| C-08 | Evaluate meaningful trailing-team decisions, not automatic odds restoration; `hypothesis`. | F02 decision and F07 evaluation excerpts. | Low; no balance guarantee. |
| C-09 | Preserve hidden-state uncertainty while communicating legitimate facts; `inference`. | F02 information contract and P02 selected cue pattern. | Moderate scoped logic; no universal disclosure level. |
| C-10 | Historical reports/outcome associations do not prove misconduct causation or prevalence; `empirical-evidence`. | `GDR-SRC-20261010-G21-009`, sections 3.2–4, Table 1, 6.4, 7.1. | Moderate historical evidence; selected cases and missing relationships. |
| C-11 | The study’s H4.2 was not supported; `empirical-evidence`. | `GDR-SRC-20261010-G21-009`, section 6.4 final paragraph. | High for reported negative result; no individual guilt inference. |
| C-12 | Smart Ping provides documented transient signals and intent voting; `observed-example` of a document. | `GDR-SRC-20261010-G21-010`, wheel/visuals/voting. | High page confidence; no tested behavior benefit. |
| C-13 | Provide layered, suppressible communication without equating silence with misconduct; `hypothesis`. | C-09/C-10/C-12; F07 ethical guidance. | Low efficacy; moderation policy and local access review needed. |
| C-14 | Commitment includes interruption and teammate consequences; `inference`. | F07 selected safe-exit pattern. | Moderate reasoning; game-specific exit rules still needed. |
| C-15 | Evaluate equivalent legitimate information across access options; `inference`. | P01 corrected accessibility; P02 cue/multimodal excerpts. | Moderate scope; no universal numerical standard imported. |
| C-16 | Separate contribution, coordination, behavior and satisfaction measures; `hypothesis`. | F07 evaluation excerpt; limitations of C-10. | Low until local validation; no telemetry-as-wellbeing claim. |
| C-17 | Later selected dependencies and runtime evidence are missing here; `observed-example` of access. | Batch dependency/gap register. | High session-local confidence; not a global absence claim. |
| C-18 | Proposed comparisons could falsify these adaptations; `hypothesis`. | C-05–C-16 and reviewed evaluation framing. | Low; tests not performed and clustering requires review. |
| C-19 | G21 patterns require objective-window or terminal-elimination prerequisites; `hypothesis`. | G21 PAT-01/PAT-02. | Low fit confidence; no tag-based adoption. |

## Coverage, contradictions and history

Covered decisions include objective formats, roles, resources, information, communication, loss/recovery and behavior-evidence interpretation. Open coverage includes direct runtime inspection, cross-input fairness, contemporary intervention studies, underrepresented language populations, draft/ban systems, esports-specific rules and role-queue population effects. See `G21-CON-03`, `G21-CON-04` and `G21-CON-08` in the [review packet](../reviews/full-run-20261010-g21-review-packet.md#contradictions-and-tensions).

`0.1.0`, `initial-authoring-1`: new candidate, no predecessor or supersession asserted. Author self-review does not constitute independent review. Next decision: review the boundary and test whether the layered-communication recommendation preserves the needs of deliberately high-coordination play. Exact hash appears in the review packet.

## References

All sources were inspected on **2026-10-10, America/Los_Angeles session date**. Access describes the material actually read, not the availability of an entire website. No game client or recording was observed; game examples below are observations of official documentary artifacts. No third-party pages linked by these documents are implicitly inspected. Source identities are run-scoped; central URL/DOI/edition deduplication remains pending. Rights: copyrighted material is paraphrased; no screenshots, substantial quotations, chat logs or source PDFs are redistributed. No reuse license is assumed.

### GDR-SRC-20261010-G21-006

Riot Games. *How to Play*. unknown. League of Legends. [Inspected source](https://www.leagueoflegends.com/en-us/how-to-play/).

**Version/build:** Undated web guide, predominantly Summoner’s Rift; runtime patch unknown. **Access:** `relevant-excerpt`; What is League of Legends; Destroy the Base; Clear the Path; Take on the Jungle; Choose Your Lane; Power Up Your Champ; retrieved lines 12–92. **Type:** official game guide. **Supports:** C-01/C-02/C-05. **Limits and independence:** Recommended positions and this mode’s objectives are not universal MOBA rules. Same developer as 010; descriptions are not effect validation.

### GDR-SRC-20261010-G21-007

Blizzard Entertainment. *Core Concepts: Introduction to Heroes of the Storm*. unknown in inspected page. Blizzard News. [Inspected source](https://news.blizzard.com/en-us/article/20720242/core-concepts-introduction-to-heroes-of-the-storm).

**Version/build:** Historical introductory account, patch unspecified; older role terms not treated as current. **Access:** `relevant-excerpt`; Main article: shared leveling, talents, unusual hero control arrangements and battleground variation; retrieved lines 5–71. **Type:** official developer guide. **Supports:** C-01/C-03/C-07. **Limits and independence:** No comparative evidence that shared experience or absence of a shop improves fairness or behavior. Do not infer present roster or balance.

### GDR-SRC-20261010-G21-008

The Pokémon Company International / Pokémon UNITE. *Pokémon UNITE Overview*. unknown. Official Pokémon UNITE site. [Inspected source](https://unite.pokemon.com/en-us/overview/).

**Version/build:** Launch-style web overview, exact update and runtime build unknown. **Access:** `relevant-excerpt`; Unite Battles, temporary growth, gathering Aeos energy and scoring in opponent goals; retrieved lines 48–119. **Type:** official game overview. **Supports:** C-01/C-04/C-05. **Limits and independence:** Score-ending comparison only; not a claim that all modes, schedules or current balance match this snapshot. Footer copyright is not publication date.

### GDR-SRC-20261010-G21-009

Haewoon Kwak, Jeremy Blackburn and Seungyeop Han. *Exploring Cyberbullying and Other Toxic Behavior in Team Competition Online Games*. 2015; arXiv v1 2015-04-09. ACM CHI 2015; author manuscript via arXiv. [Inspected source](https://arxiv.org/html/1504.02305). DOI: `10.1145/2702123.2702529`.

**Version/build:** Inspected arXiv:1504.02305v1 HTML rendition; April 2013 League of Legends Tribunal data. **Access:** `relevant-excerpt`; Sections 3.2–4 and Table 1; section 6.4 including rejected H4.2; section 7.1. **Type:** original empirical paper. **Supports:** C-10/C-11. **Limits and independence:** Reported/accused-case selection, unknown completeness, absent friendship and longitudinal records; no causal intervention. Regional associations do not establish cultural causation. Proceedings and arXiv are the same study.

### GDR-SRC-20261010-G21-010

Laserface / Riot Games. *Smart Ping*. 2025-02-18. League of Legends Support. [Inspected source](https://support.riotgames.com/en-us/league-of-legends/gameplay/smart-ping).

**Version/build:** Support revision, runtime patch unknown. **Access:** `relevant-excerpt`; Smart Ping Wheel; Terrain and Mini-Map Visuals; Objective Voting; retrieved lines 27–87. **Type:** official mechanics documentation. **Supports:** C-12/C-13. **Limits and independence:** Documents communication options; faster/safer language is developer advice, not tested comparative benefit. Same Riot family as 006.

