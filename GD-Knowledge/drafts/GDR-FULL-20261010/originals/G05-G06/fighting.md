---
id: GDR-CAND-20261010-G05-GEN-01
kind: genre
title: Fighting
version: 0.1.0
status: draft
candidate_revision: author-self-review-1
attempt_id: G05-initial-capture
identity_scope: temporary-run-scoped
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_state: open
aliases:
- fighting game
- fighter
- versus fighter
tags:
- spacing
- commitment
- move sets
- input alternatives
- training
- competitive and noncompetitive play
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-G05-PAT-01
- GDR-CAND-20261010-G05-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G05-GEN-02
source_ids:
- GDR-SRC-20261010-G05-001
- GDR-SRC-20261010-G05-002
- GDR-SRC-20261010-G05-003
- GDR-SRC-20261010-G05-004
- GDR-SRC-20261010-G05-005
- GDR-SRC-20261010-G05-006
- GDR-SRC-20261010-G05-007
- GDR-SRC-20261010-G05-008
- GDR-SRC-20261010-G05-009
- GDR-SRC-20261010-G05-014
- GDR-SRC-20261010-G05-015
- GDR-SRC-20261010-G05-016
- GDR-SRC-20261010-G05-017
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: c4eda980dfccb3e0f3517341cabc371bef54a9288046934c50915f71089259f2
supersedes: sha256:c4eda980dfccb3e0f3517341cabc371bef54a9288046934c50915f71089259f2
integrity_record: ../reviews/full-run-20261010-g05-integrity-receipt.md
---

# Fighting

**Draft research candidate, not released guidance.** Definitions and application recommendations below are working inferences or hypotheses, not approved studio choices or universal genre requirements. Source-supported descriptions, creator intentions, and empirical results are separated in the claim ledger. No game was played, no recording was analyzed, and no prototype or player test was run for G05. Public game cases are observations of documentation artifacts, not firsthand observations of their executable behavior.

The [G05 review packet](../reviews/full-run-20261010-g05-review-packet.md) records the inspected input snapshot, selected dependency hashes, source relationships, open coverage, and gates. Existing reviewed dependencies remain unreleased and are not repackaged here. A link to a packet dependency record does not pretend that its underlying topic is included in this four-candidate set.

## Definition and boundaries

This entry uses **fighting** for modes in which a character's differentiated action repertoire, position, and commitments are central to contesting another combatant's options across repeated exchanges. That is a useful working boundary, not a formal classification standard. Neither one-on-one play, fists, a side-on camera, competitive ranking, nor difficult command execution is mandatory. An AI opponent can support the structure; multiplayer and competitive status are facets. Evaluate the configured mode rather than inferring its structure from a franchise label. [C-01]

| Variant or neighboring structure | What changes the design question | Boundary and counterexample |
|---|---|---|
| Head-to-head, largely planar contest | Reach, facing, contact timing, defensive alternatives, and adaptation between two active opponents | A long move list is not itself a fighting structure; frequent melee attacks inside an exploration game need not define its main mode. |
| Weapon-based or three-dimensional contest | Lateral alignment and weapon reach can change what counts as a threatened space | A weapon does not make a separate genre mandatory; a purely planar weapon contest still needs a different spatial analysis from free movement. |
| Platform variant | Position relative to exits and recovery routes can matter alongside damage | Launching an opponent off-stage is a documented Smash objective; do not substitute a health-depletion-only analysis. |
| Multi-actor or arena contest | Target selection, third-party intervention, camera coverage, and temporary alliances may disrupt a two-person timing model | Being advantaged against one opponent says nothing sufficient about another actor's opportunity. Arena camera alone does not establish the genre. |
| Tag, squad, round, and custom-rule formats | Available repertoire, substitutions, information carried between contests, and commitment length | Sequential squad selection is not the same problem as simultaneous extra fighters. |
| Crowd-combat or action-adventure hybrid | Encounter composition, traversable space, resources, and route continuity may become the organizing structure | Route the crowd/attrition problem to [Beat-em-up](beat-em-up.md), rather than relabeling every wave as a duel. |

These distinctions are analytical inferences. Nintendo's official modes page supplies a useful configured-mode countercase: multiplayer/custom rules, sequential Squad Strike, and Mob Smash waves coexist under one title. Its separate overview describes off-stage elimination. These documents do not prove how every audience categorizes the game. [C-01, C-02; GDR-SRC-20261010-G05-007; GDR-SRC-20261010-G05-017]

## Custom research instructions

For subsequent fighting research, first identify the ruleset, platform, build, mode, number of simultaneously active actors, input configuration, and evidence route. Keep the following decision questions distinct rather than using “depth” or “fairness” as unexplained aggregate scores. [C-04, C-05, C-14]

1. **Which decisions create the intended contest?** Map spacing, move selection, observation, prediction, execution, resource use, and adaptation. Ask whether reducing one demand removes a barrier to the desired contest or removes a valued part of it. Include players seeking expression, social play, mastery, story, or spectacle rather than presuming a tournament audience.
2. **Which facts can players acquire, and when?** Compare in-match signals, move descriptions, training displays, and replay explanations. Investigate misconceptions about hit, block, whiff, range, facing, cancel availability, and state-dependent interactions. Do not require advance memorization merely because a data table exists.
3. **What does a failed commitment cost?** Separate animation recovery, lost health, resource expenditure, a round loss, forfeiture, and a settings mistake. Investigate legitimate competitive consequences and usable re-entry without promising that every action is reversible.
4. **Which source could distinguish the explanations?** Use official build-specific rules for implementation claims, creators for intention, original evaluations for outcomes, and reproducible observations for behavior. Seek unsuccessful adaptations and boundary cases. Archive/version-sensitive replay claims require stronger provenance than a promotional feature description.
5. **What comparison would be misleading?** Do not infer a control scheme's strategic equivalence from fewer button presses, a device's equivalence from a nonsignificant result, balance from aggregate win rate alone, or access from a successful demonstration by a practiced player. Do not make a selected title's frame rate or latency a universal threshold.

Research should cover weapon and platform variants, multi-actor intervention, non-ranked and AI contexts, varied prior experience, assistive configurations, and more than one language. Those are outstanding coverage obligations, not populations already sampled here. [C-14–C-16]

## Player promises and varied audiences

Candidate promises include recognizing and exploiting an opening, expressing a preferred character style, testing an opponent model, performing an execution sequence, learning a difficult matchup, or enjoying a social bout. Treat each as a **hypothesis about a particular audience and mode**, not an expectation inherent in the label. A player may value strategic prediction while disliking repeated circular inputs; another may regard rehearsed execution as a central accomplishment. Neither preference establishes genre worth. [C-05, C-16]

A practical design brief should name the decisions it wants to preserve and the burdens it is willing to alter. “Accessible but deep” is insufficient unless it identifies whose access, which decisions, and which evidence could show a loss. Making an execution alternative optional also does not establish parity: its action-selection policy, timing, unavailable options, and player-facing explanation still need examination. [C-05, C-15]

## Characteristic loops and structures

### Exchange: range, timing, information, and commitment

A useful analytical loop is **perceive a state → estimate an opponent's possibilities → choose and execute → observe the actual outcome → revise the model**. It is not a mandated sequence of conscious thoughts. Reactive actions, prepared sequences, and prediction can overlap; a visible success alone does not reveal which process produced it. [C-04]

The Fantasy Strike guide describes startup, active, and recovery phases, relative recovery timing, contact-dependent advantage, and reach as a condition on a response. These are documentation observations, not current frame-data verification. The guide's listed values and hypothetical examples should not be fused into a build-authoritative move table. Its legacy Basics page still has pre-alpha framing. [C-03; GDR-SRC-20261010-G05-002; GDR-SRC-20261010-G05-016]

For reasoning within a specified ruleset, choose a shared reference event and define `t_you` and `t_other` as the earliest times each actor can take the relevant next action. Define advantage conventionally as `A = t_other − t_you`: positive means you become available earlier. This is a stated analysis convention, not a prescribed implementation. It does **not** by itself answer whether an attack reaches, whether another action is legal, whether a defensive property applies, or whether a third actor can intervene. Separate outcomes on hit, block, and whiff; separate a move's displayed animation duration from its actual commitment if lawful transitions differ. [C-04]

The resulting recommendation is to teach **conditional action opportunities**, not “positive means attack” or “negative means guaranteed punishment.” A useful explanation connects a visible event with the relevant state and a feasible next action. Detailed frame displays may support diagnosis, while a simpler range/availability explanation may better answer a learner's current question. Both can fail if their state is inaccurate. [C-04, C-09]

### Move sets and input alternatives

Use an **action-contract comparison**, not a command-count comparison. For each alternative, document the selectable actions, required preparatory state, activation timing, context sensitivity, resource cost, failure behavior, and information needed to choose it. Then ask which differences are intentional. Reducing finger travel while retaining the same choices differs from automatically selecting a contextual response; removing a preparatory requirement can alter when an option becomes credible. These are possible mechanisms to test, not claims about an uninspected game's Modern mode. [C-05]

PlayStation's SF6 FAQ distinguishes Classic, Modern, and offline-limited Dynamic control availability. This is documentation evidence, not a control-parity evaluation. [C-06; GDR-SRC-20261010-G05-001]

Sirlin's 2015 account argues for reducing execution overhead to foreground decisions. SOULCALIBUR VI's producer frames Reversal Edge as an entry aid, while a subsequent team Q&A acknowledges rhythm costs from repeated use. These are situated practitioner accounts. [C-18; GDR-SRC-20261010-G05-003; GDR-SRC-20261010-G05-008; GDR-SRC-20261010-G05-009]

The pacing response is not a controlled refutation of simplification: it concerns a particular mechanic that also changes the exchange structure. [C-05]

**Conditional choice:** when the intended promise centers on selecting responses, try reducing an unrelated motor barrier while keeping selection and counterplay inspectable. When the promise includes execution under pressure, offer a clearly described alternate contract or another mode rather than declaring the difference immaterial. Avoid stigmatizing labels. Do not compensate automatically with an invented damage penalty or assume that one balancing knob preserves every matchup. Omitting an automatic action selector may be preferable when its decisions cannot be explained or its maintenance burden is unacceptable. [C-05, C-15]

**Empirical boundary:** Zaman and MacKenzie's 2013 Study II tested 12 expertise-screened participants on a Nexus One/TigerArcade setup using Street Fighter Zero 3, three input methods, and restricted special-move attempts. The device effect was not statistically significant; the move effect was. Interruptions were handled specially and other actions were restricted. This does not establish device equivalence, novice access, disability inclusion, ordinary-match performance, or strategic preservation under simplified commands. The paper's stronger similarity language is not adopted as an equivalence result. [C-07; GDR-SRC-20261010-G05-015]

### Training, hidden rules, and causal information

Diagnose what the learner cannot yet distinguish. Did input fail to register, was the action unavailable, did it miss spatially, or did an opposing property determine the result? A generic “try faster” hint conflates these explanations. Provide the least intrusive evidence that differentiates them; optional detail can expose deeper rules without making every live exchange a reading task. [C-09; reviewed P02 transfer]

TEKKEN 8's documentation offers replay tips, practice, and a bounded retry feature; its historical v1.08.01 notes also document loss of compatibility with earlier replays. Fantasy Strike documents a dummy default that omits a defense present under corresponding real-match inactivity. Together these support checking replay version and training-state assumptions, not a claim that replay practice improves durable learning. [C-08; GDR-SRC-20261010-G05-005; GDR-SRC-20261010-G05-006; GDR-SRC-20261010-G05-002]

Use [Replay-to-variant practice](../patterns/replay-to-variant-practice.md), `GDR-CAND-20261010-G05-PAT-01`, when a recorded situation can be meaningfully reconstructed. Mark a branch as an experiment against a specified continuation, not “what the opponent would really have done.” Change a condition that discriminates the learned rule, and preserve accommodations. Training that reveals a hidden opponent choice can be appropriate after a completed contest yet inappropriate as live advice; define that information boundary explicitly. [C-09, C-15]

### Recovery, rounds, matches, and long-term play

TEKKEN 8's system documentation describes a recoverable health state with specified regain and removal conditions. That is not an undo command. Keep **damage recovery**, **animation recovery**, **resource refund**, **replay retry**, and **session re-entry** separate in design and language. [C-10, C-11; GDR-SRC-20261010-G05-004]

Round resets can create repeated opportunities to reconsider an opponent model, while longer uninterrupted contests can preserve resource and positional consequences. Character switches may broaden adaptation but also change matchup demands. These are conditional consequences of the chosen rules, not universal prescriptions for rounds, time limits, or set lengths. Record what resets, what persists, what players can inspect, and what an interruption costs. A single brief encounter, a party rotation, and a ranked set can legitimately need different structures. [C-11, C-17]

A recovery mechanic that protects one player's agency may compromise another's earned outcome. Provide recoverable configuration changes and understandable interruption policies without assuming an unrestricted match undo or costless forfeiture. Conversely, do not treat unrelated progress loss as necessary simply to discourage leaving. These are proportionality questions transferred from reviewed F02/F07 guidance, not legal judgments or settled policy for a service. [C-11, C-14]

### Online context and presentation

GGPO's official overview describes prediction/speculative execution and correction as a networking approach. It does not provide an end-to-end “no latency” guarantee. [C-12; GDR-SRC-20261010-G05-014]

For a candidate design, distinguish intended action commitment and presentation pauses from input-device delay, display delay, network uncertainty, and correction. They may feel related but changing one does not automatically fix another. Evaluate whether a displayed contact or cue can later be contradicted, and how that uncertainty is explained. Avoid adding decorative certainty to an unconfirmed outcome. No universal acceptable delay, rollback depth, or response-window value is recommended here. Implementation feasibility and current integration behavior belong to a separately authorized technical review. [C-13]

## Applying shared topics

All transfers below are **inferences from inspected, parent-selected, reviewed drafts**, not fresh verification of those drafts' original external sources. Exact revisions, hashes, and inspected passages are in the linked packet records. [C-14, C-15]

| Shared entry and inspected identity | Fighting-specific application | Limit retained |
|---|---|---|
| [F02 Decision design](../reviews/full-run-20261010-g05-review-packet.md#dep-f02-decision), `GDR-CAND-20261010-F02-TOP-01` | Separate knowing a response is available from choosing to risk it; identify the information contract of a matchup. | A favorable outcome does not prove a well-understood decision. |
| [F02 Challenge and difficulty](../reviews/full-run-20261010-g05-review-packet.md#dep-f02-challenge), `GDR-CAND-20261010-F02-TOP-02` | Separate execution, perception, opponent-model, and resource demands before changing assistance. | Assistance is not a substitute for access; automatic adaptation is not universally suitable for a comparative contest. |
| [P02 Controls and input](../reviews/full-run-20261010-g05-review-packet.md#dep-p02-controls), `GDR-CAND-20261010-P02-TOP-01` | Audit mapping, activation, preparatory states, and input eligibility independently. | No inherited buffer length or device-parity guarantee. |
| [P02 Feedback](../reviews/full-run-20261010-g05-review-packet.md#dep-p02-feedback), `GDR-CAND-20261010-P02-TOP-02` | Distinguish accepted input, whiff, block, hit, and uncertain outcome; make optional flourish removable. | Intensity is not correctness, timing, or proof of “feel.” |
| [P02 Multimodal communication](../reviews/full-run-20261010-g05-review-packet.md#dep-p02-multimodal), `GDR-CAND-20261010-P02-TOP-03` | Alternative cues should preserve actionable state and legitimate opponent uncertainty. | Do not import the unresolved Moon et al. table-label interpretation or claim emotional equivalence. |
| [F07 Evaluation](../reviews/full-run-20261010-g05-review-packet.md#dep-f07-evaluation), `GDR-CAND-20261010-F07-TOP-01` | Diagnose an unused option through knowledge, execution, availability, preference, and payoff before buffing it. | Win rate and selection rate do not identify cause; sampling and denominators remain explicit. |
| [F07 Ethics](../reviews/full-run-20261010-g05-review-packet.md#dep-f07-ethics), `GDR-CAND-20261010-F07-TOP-02` | Examine accessible refusal/re-entry alongside costs imposed on an opponent or partner. | No blanket costless exit and no inferred implementation or legal approval. |
| [P01 Accessibility](../reviews/full-run-20261010-g05-review-packet.md#dep-p01-accessibility), `GDR-CAND-20261010-P01-TOP-03` | Assess motor activation, sensory facts, comprehension, and settings access separately. | WCAG's web scope, informative cross-context guidance, and vendor recommendations remain distinct; no native-game frame or control threshold is imported. |

F04 combat/traversal and G04 shooters were identified by the dispatch as running, unreviewed dependencies; their bytes were not inspected. Camera, animation, multiplayer, and encounter-owner guidance has not been transferred from unseen later work. This entry does not infer a completed review from a conversation or packet pointer.

## Pattern selection and adaptations

[Replay-to-variant practice](../patterns/replay-to-variant-practice.md) owns replay provenance and branch validity. The inspected [F01 Supported attempt and transfer check](../reviews/full-run-20261010-g05-review-packet.md#dep-f01-transfer), `GDR-CAND-20261010-F01-PAT-01`, owns the broader instructional comparison: change a discriminating condition, distinguish rule knowledge from preferred choice, and retain useful assistance. Do not demand prompt removal as evidence of mastery. [C-09, C-15]

[Recoverable expenditure window](../patterns/recoverable-expenditure-window.md), `GDR-CAND-20261010-G05-PAT-02`, is **not** a recommendation to copy TEKKEN's injury recovery or to refund every failed attack. Consider it only for an intentionally spent resource with an explicit recovery contract and meaningful remaining commitment. In a competitive mode, check whether recovery creates an unwanted dominant loop or denies the opponent's earned consequence. [C-11]

The reviewed [P02 remapping](../reviews/full-run-20261010-g05-review-packet.md#dep-p02-remapping) and [cue-alternative](../reviews/full-run-20261010-g05-review-packet.md#dep-p02-cues) patterns address configuration and communication, not automatic combat decisions. Their recoverability does not authorize reversing a match result. [C-14, C-15]

## Representative cases and negative cases

The source-supported cases above deliberately include a control-mode overview, a simplified-input creator position, a reported pacing cost, a weapon/3D design account, a platform/multi-mode countercase, training documentation, historical replay compatibility, and one narrow empirical device study. They are **not** a best-games list, exhaustive historical account, popularity ranking, or causal sample. Official documentation favors features worth advertising; community-response articles select questions; creator interviews explain intended mechanisms rather than independently measured outcomes. [C-02, C-06–C-08]

**Illustrative worked case — “punishable” but out of reach.** A learner sees an opponent finish later and repeatedly selects a short attack. In state A, both actors are close and the response reaches; in state B, the same temporal relation occurs after greater separation and the response misses. The proposed lesson asks the learner to predict *availability and reach* before choosing among a short attack, movement, or waiting. State C changes availability rather than distance. A correct prediction paired with a deliberately conservative choice is not a knowledge failure. These are hypothetical states, not observed game data or numeric tuning recommendations. [C-04, C-09]

**Countercase:** a multi-actor arena allows a third actor to strike while the two participants in that lesson are committed. The two-person advantage explanation remains a narrow description but is insufficient decision advice. A more elaborate frame chart would not repair the omitted actor. [C-01, C-04]

## Accessibility and production implications

Keep remapping, reachable settings, and restore paths usable outside and inside the intended mode. Examine simultaneous presses, repeated presses, hold duration, motion precision, and fatigue separately. A simplified input that chooses the wrong context-sensitive action can exchange a motor problem for a comprehension or agency problem. Localize explanations of facing, relative direction, state, and resource terminology; do not rely solely on untranslated community shorthand. These are proposed audits grounded in reviewed P01/P02, not an assertion that every listed accommodation is implemented or sufficient. [C-15]

Offer optional numerical or slowed inspection without requiring players to consume it during an exchange. Preserve required facts when flashes, shake, or strong sound effects are reduced. Avoid labeling a configuration as shameful or presenting an assistance setting as proof that results are illegitimate. Where different rulesets matter to a contest, explain their actual differences rather than substituting an audience hierarchy. [C-15]

Production cost includes maintaining command descriptions, state explanations, localization, test cases, and training/replay compatibility as rules change. A rich replay tool can be unjustified if a verified fixed scenario answers the question at lower cost. Player-facing advice that survives a patch but no longer matches the rules is a maintenance failure to detect, not additional evidence that a player needs practice. [C-08, C-09, C-13]

## Research questions and validation

**All tests below are proposed and not performed.** Study execution, participant recruitment, instrumentation, and implementation require separate authorization. Choose participants and sample-size reasoning for the actual decision; no universal sample, frame, delay, or success threshold is supplied. Retain the reviewed F07 distinction between detecting a problem and estimating prevalence or establishing equivalence. [C-16]

| Discriminating question | Proposed contrast and procedure | Measures, confounds, and rejection condition |
|---|---|---|
| Does input reduction preserve the intended contest? | Compare specified action contracts in matched situations and then adaptive play; stratify relevant prior experience and access configurations. Ask players to predict what action will occur before acting. | Track unintended selections, available responses, comprehension, execution, counterplay, and valued expression separately. Familiarity and auto-selection are confounds. Reject a parity claim if relevant choices or timing commitments differ without an accepted design rationale. |
| Does replay-supported diagnosis transfer? | Compare ordinary review or an explained fixed drill with replay-to-variant practice. Counterbalance where learning carryover permits; test a changed distance/state and later an adaptive opponent. | Distinguish explanation, permitted-response prediction, chosen tactic, and execution. Reject the claimed transfer mechanism if gains remain tied to the saved continuation or to revealed information unavailable in the target context. |
| Does recovery retain meaningful commitment? | Compare a declared recovery contract with fixed consequences under the same objective; inspect intentional loss/leave/retry cases separately. | Track risk choices, opponent opportunity, comprehension, exploit loops, and re-entry costs. Reject the candidate if its benefit relies on obscured forfeiture or erases an explicitly valued competitive consequence. |
| Do online cues communicate the state players must act on? | After technical feasibility review, compare permitted network conditions and cue treatments while recording actual state/cue consistency. | Separate delay, correction, input error, and designed commitment. Do not explain every loss with connection quality. Reject a cue treatment that systematically signals certainty where relevant state is still uncertain. |
| Which session contract fits this mode? | Compare openly described short and long commitments, reset policies, and re-entry routes with appropriate partners/opponents. | Examine learning opportunity, unwanted waiting, interruption costs, and preference. A more frequently selected format is not automatically more ethical or better for every audience. |

## Claim ledger

Claim IDs are local to this file. Confidence describes the specified claim, not approval or genre completeness. `DEP-*` references are inspected internal draft dependencies recorded in the packet; their external evidence has not been re-audited here.

| ID | Material claim and class | Support, locator, and contrary condition | Confidence and unresolved question |
|---|---|---|---|
| C-01 | Working genre and variant boundary — `inference` | 007 Game modes; 008 weapon/movement account; 017 opening; comparison with crowd structure in companion entry | Moderate as a useful distinction; taxonomy acceptance and other market usages remain open. |
| C-02 | The inspected Nintendo documents contain distinct configured modes and an off-stage objective — `observed-example` | 007 modes paragraphs; 017 opening; documentation route only | High for inspected wording, not for every build or audience classification. |
| C-03 | The inspected guide explains phased attacks and conditional relative recovery — `observed-example` | 002 timing sections; 016 historical status is a freshness caution | High for document contents; exact current tuning deliberately unresolved. |
| C-04 | Timing advantage must be interpreted with reach, legal actions, information, and other actors — `inference` | 002 Frame Advantage; DEP-F02-Decision; explicitly defined analysis convention | Moderate: reasoning fits stated rules; exceptional properties require a build-specific audit. |
| C-05 | Fewer inputs do not by themselves establish preservation of action structure or execution identity — `inference` | 001 control distinctions; 003 creator position; 008/009 contrasting costs; DEP-P02-Controls | Moderate logical/design distinction; which differences an audience values remains untested. |
| C-06 | The official SF6 overview documents distinct control options and availability — `observed-example` | 001 control-type FAQ; documentation route only | High for the inspected wording, not current move availability or control parity. |
| C-07 | Historical Study II found no significant device effect on its restricted task; this is not equivalence evidence — `empirical-evidence` | 015 §7–8; limitations and inference boundary stated above | Moderate for narrow reported result; small selected sample, old hardware, and task exclusions constrain transfer. |
| C-08 | Replay/training descriptions and historical compatibility/default differences justify provenance checks — `observed-example` | 005 feature page; 006 replay transition; 002 dummy settings | High for documented facts; current state fidelity and efficacy not verified. |
| C-09 | State-matched replay plus discriminating variants may improve usable diagnosis — `hypothesis` | C-08; DEP-F01-Transfer; G05 PAT-01 causal-link ledger | Low for learning benefit; fixed continuation, information leakage, and repeated exposure may explain improvement. |
| C-10 | The official system page describes a recoverable health state — `observed-example` | 004 Recoverable Gauge; the undo distinction is separately classified under C-11 | High for document description; unknown current build and effects. |
| C-11 | Recovery should be analyzed by what is restored, retained, and imposed on others — `inference` | 004; DEP-F02-Decision/Challenge; DEP-F07-Ethics/Safe-Exit | Moderate conditional analysis; no particular competitive policy approved. |
| C-12 | GGPO describes prediction/speculative execution, not a measured absence of end-to-end delay — `observed-example` | 014 “How does it work?”; official technical documentation route | High for the narrow description; no version or integration audit. |
| C-13 | Timing and uncertainty require separate technical/presentation diagnosis — `hypothesis` for proposed design tests | C-12; DEP-P02-Controls/Feedback; replay-maintenance example 006 | Moderate rationale, low efficacy confidence; actual implementation conditions missing. |
| C-14 | Reviewed shared guidance can be conditionally transferred without converting metrics or review into success proof — `inference` | F02/P02/F07 records and application table | Moderate; original external evidence not re-inspected for this transfer. |
| C-15 | Accommodations, semantic cue facts, and valid transfer probes must survive genre adaptation — `inference` | Corrected F01/P01 and P02 pattern records | Moderate rationale; populations, languages, and complete configurations untested. |
| C-16 | Candidate audience promises and proposed comparisons could discriminate competing explanations — `hypothesis` | DEP-F07-Evaluation/Diagnosis; explicit proposals, no outcomes | Low until studied; scope, recruitment, tolerable uncertainty, and acceptance rules need local approval. |
| C-17 | Reset, substitution, and session policies change the opportunities and costs of adaptation — `inference` | 007 configured mode differences; DEP-F02-Decision; DEP-F07-Safe-Exit | Moderate conditional reasoning; no universally preferred format inferred. |
| C-18 | Creators propose execution simplification/entry aids and report a specific pacing cost — `practitioner-heuristic` | 003 design position; 008 Reversal Edge intention; 009 pacing response | Moderate as situated practitioner evidence; no controlled benefit, general failure, or complaint prevalence established. |

No formal standard or approved studio design decision is asserted. Observed documentation, practitioner rationale, and subsequent inference have separate ledger rows.

## Coverage, review, and history

**Researched:** working boundaries; representative planar, weapon/3D, platform/multi-actor, and crowd-mode contrasts; move timing concepts; input alternatives; causal information and replay limitations; recovery distinctions; session choices; online conceptual context; accessibility, localization, and production implications.

**Still open:** executable/build verification; current move data and control-mode parity; multi-actor/arena-specific empirical work; disabled and novice populations; long-term replay transfer; current network integration; representative regional/language differences; matchmaking/moderation; broader historical coverage. Capcom manual access failed; a tutorial-design paper remains a lead. These gaps are not closed by the number of source records.

`initial-capture-1`, version `0.1.0`, 2026-10-10: first local capture. `author-self-review-1`, same version and identity: split control-option observation from creator rationale (C-06/C-18) and isolate the health-rule observation from its recovery inference (C-10/C-11). This author-only correction supersedes local predecessor SHA-256 `c4eda980dfccb3e0f3517341cabc371bef54a9288046934c50915f71089259f2`; it is not an independent review or a repeat batch submission. Author self-review is recorded in the packet; independent G05 review has not occurred. Gate C pending; static packaging checks are not overall Gate D; Gate E/release not approved. Additional pattern questions are queued without allocating child keys. Reopen the timing/input/replay claims when an actual target build changes.

## References

All records below were accessed on **2026-10-10 (America/Los_Angeles)**. Access is `relevant-excerpt`: the identified HTML text was inspected, not linked videos, executables, or a presumed current build. Web-text line locators describe this retrieval and are paired with stable section descriptions. Copyright remains with the respective rights holders; no redistribution license was inferred. This artifact paraphrases source text and embeds no third-party images. Source identities are provisional, reused within G05; cross-batch URL/edition deduplication remains pending.

### GDR-SRC-20261010-G05-001
**Sony Interactive Entertainment / PlayStation editorial. [Everything you need to know about Street Fighter 6](https://www.playstation.com/en-us/games/street-fighter-6/everything-you-need-to-know-about-street-fighter-6/).** Date: Publication/update unknown. Publisher/host: www.playstation.com. Edition/build: Official SF6 overview; launch/Year 1 framing; build unpinned. Source type: Official platform product documentation. Access: `relevant-excerpt`.
**Locator:** Control-type FAQ and training paragraph; inspected web-text lines 249–272. **Claims:** C-05/C-06. **Limits:** Supports the documented control-mode distinctions, not current damage modifiers, move-set equivalence, or accessibility efficacy. Capcom manual routes were inaccessible. **Independence:** SF6 / official platform presentation.

### GDR-SRC-20261010-G05-002
**Sirlin Games. [Guide: Practice Mode](https://www.fantasystrike.com/practice-mode).** Date: Publication/update unknown. Publisher/host: www.fantasystrike.com. Edition/build: Unversioned Fantasy Strike guide; build unpinned. Source type: Developer-authored game documentation. Access: `relevant-excerpt`.
**Locator:** “Controlling the Dummy”; “Understanding Frames”; “Frame Advantage”; “Frame Step Mode”; inspected lines 45–101. **Claims:** C-03/C-04/C-08. **Limits:** Documents practice settings and timing concepts. Named values and hypothetical calculations must not be merged into a current frame table; this batch did not inspect the executable or establish its current tuning. **Independence:** Fantasy Strike; same production origin as 003 and 016.

### GDR-SRC-20261010-G05-003
**David Sirlin, game designer. [A New Era of Fighting Games](https://www.sirlin.net/posts/a-new-era-of-fighting-games).** Date: 2015-07-22. Publisher/host: www.sirlin.net. Edition/build: Pre-release design account. Source type: Firsthand practitioner account. Access: `relevant-excerpt`.
**Locator:** Discussion of simpler controls and focus on decisions; inspected lines 23–56, especially 43–51. **Claims:** C-05/C-18. **Limits:** Creator rationale and informal anecdote, not a controlled comparison or a representative player study. **Independence:** Fantasy Strike; same production origin as 002 and 016.

### GDR-SRC-20261010-G05-004
**Bandai Namco Entertainment. [TEKKEN 8 — Battle System](https://tk8.tekken-official.jp/en/battle/system.php).** Date: Publication/update unknown. Publisher/host: tk8.tekken-official.jp. Edition/build: Official unversioned system overview; exact game build unpinned. Source type: Official developer/publisher game documentation. Access: `relevant-excerpt`.
**Locator:** “Recoverable Gauge” / recovery discussion, lines 108–125; Rage Art interaction, 148–150. **Claims:** C-10/C-11. **Limits:** Supports the described health-state contract, not the current balance of all moves, a universal aggression benefit, or an equivalence with voluntary resource expenditure. **Independence:** TEKKEN 8; shared publisher with 005, 006, 008, 009.

### GDR-SRC-20261010-G05-005
**Bandai Namco Entertainment. [TEKKEN 8 — My Replays & Tips](https://tk8.tekken-official.jp/en/mode/replay.php).** Date: Publication/update unknown. Publisher/host: tk8.tekken-official.jp. Edition/build: Official unversioned mode overview; exact game build unpinned. Source type: Official developer/publisher game documentation. Access: `relevant-excerpt`.
**Locator:** “My Replays & Tips,” “Tips,” “Practice,” and replay retry description; inspected lines 38–62. **Claims:** C-08/C-09. **Limits:** Feature description, not an evaluation of learning, long-term transfer, opponent adaptation, or complete replay-state fidelity. **Independence:** TEKKEN 8; same production origin as 004 and 006.

### GDR-SRC-20261010-G05-006
**Bandai Namco Entertainment. [TEKKEN 8 — Patch Notes v1.08](https://www.bandainamcoent.com/news/tekken-8-patch-notes-v1-08).** Date: 2024-09-30. Publisher/host: www.bandainamcoent.com. Edition/build: Game patch v1.08.01; historical, not asserted latest. Source type: Official patch record. Access: `relevant-excerpt`.
**Locator:** Update consequences for replays, lines 28–37; practice display and Special Style changes, 153–180. **Claims:** C-08/C-13. **Limits:** The article heading and specified patch suffix differ in granularity, not identity. Replay incompatibility is this documented transition, not a claim that every update invalidates every replay. **Independence:** TEKKEN 8; same production origin as 004 and 005.

### GDR-SRC-20261010-G05-007
**Nintendo. [Super Smash Bros. Ultimate — Game modes](https://www.smashbros.com/en_US/howtoplay/mode.html).** Date: Publication/update unknown. Publisher/host: www.smashbros.com. Edition/build: Nintendo Switch promotional guide; build unpinned; development-footage disclaimer. Source type: Official developer/publisher game documentation. Access: `relevant-excerpt`.
**Locator:** Multiplayer/custom rules, Squad Strike, training, and Mob Smash; inspected lines 28–93; disclaimer near 185–186. **Claims:** C-01/C-02/C-17. **Limits:** Configured modes provide boundary cases. Marketing statements do not establish universal audience access or tournament rules. No linked footage was watched. **Independence:** Nintendo / Super Smash Bros. Ultimate; same origin as 017.

### GDR-SRC-20261010-G05-008
**Motohiro Okubo, producer; Bandai Namco Entertainment. [SOULCALIBUR VI — Update from Producer Motohiro Okubo](https://www.bandainamcoent.com/news/soulcalibur-vi-update-from-producer-motohiro-okubo).** Date: 2018-07-20. Publisher/host: www.bandainamcoent.com. Edition/build: Pre-release SOULCALIBUR VI account. Source type: Firsthand practitioner account. Access: `relevant-excerpt`.
**Locator:** Weapon/8-way movement discussion, lines 11–12; Reversal Edge explanation, 19–35. **Claims:** C-01/C-18. **Limits:** Reports design intention, not measured learning or pacing outcomes. **Independence:** SOULCALIBUR VI; same production origin as 009; publisher overlap with TEKKEN sources.

### GDR-SRC-20261010-G05-009
**SOULCALIBUR VI development team; Bandai Namco Entertainment. [Community Questions Follow-up 1](https://www.bandainamcoent.com/news/community-questions-follow-up-1).** Date: 2019-06-26. Publisher/host: www.bandainamcoent.com. Edition/build: Historical Q&A; page label Ver.1.02 and discussion of game versions 1.30/1.40/1.42 are not treated as one build. Source type: Firsthand development/community response. Access: `relevant-excerpt`.
**Locator:** Reversal Edge pacing response, lines 70–76; historical balance discussion, 20–68 and 84–99. **Claims:** C-05/C-18. **Limits:** Acknowledges a cost and reports feedback; no representative complaint rate or causal experiment. Version labels are preserved rather than silently reconciled. **Independence:** SOULCALIBUR VI; same underlying feature/account family as 008.

### GDR-SRC-20261010-G05-014
**GGPO project. [GGPO — Good Game Peace Out](https://www.ggpo.net/).** Date: Publication/update unknown. Publisher/host: www.ggpo.net. Edition/build: Unversioned official SDK overview; no release/tag inspected. Source type: Official technical project overview. Access: `relevant-excerpt`.
**Locator:** “How does it work?”; inspected lines 12–17. **Claims:** C-12/C-13. **Limits:** Input prediction and speculative execution are documented. Marketing about latency is not an end-to-end latency measurement; no current integration/version audit or engine recommendation. **Independence:** GGPO technical project; not an independent comparative game evaluation.

### GDR-SRC-20261010-G05-015
**Loutfouz Zaman and I. Scott MacKenzie. [Evaluation of Nano-stick, Foam Buttons, and Other Input Methods for Gameplay on Touchscreen Phones](https://www.yorku.ca/mack/mhci2013a.html).** Date: 2013. Publisher/host: www.yorku.ca. Edition/build: Proceedings of MHCI 2013, pp. 69.1–69.8; International ASET; author-hosted HTML. Source type: Original empirical paper. Access: `relevant-excerpt`.
**Locator:** §7 User Study II (Participants, Apparatus, Procedure, Design); §8 Results and Discussion; text lines 138–200; hardware in preceding apparatus section. **Claims:** C-07. **Limits:** Small expertise-screened historical device task; restricted special-move attempts, not normal matches or a control-scheme simplification trial. Null device effect is not equivalence. Study I is not transferred into beat-em-up guidance. **Independence:** Independent academic study; its cited earlier work was not independently inspected here.

### GDR-SRC-20261010-G05-016
**Sirlin Games. [Guide: Basics, Part 1](https://www.fantasystrike.com/part1).** Date: Publication/update unknown. Publisher/host: www.fantasystrike.com. Edition/build: Page explicitly retains pre-alpha framing; not a current rules authority. Source type: Developer-authored historical documentation. Access: `relevant-excerpt`.
**Locator:** Pre-alpha status and introductory controls; inspected lines 39–121. **Claims:** C-03 freshness limit. **Limits:** Used as a freshness warning, not current numerical guidance. No attempt to reconcile its tuning with another page or an unseen build. **Independence:** Fantasy Strike; same production origin as 002 and 003.

### GDR-SRC-20261010-G05-017
**Nintendo. [Super Smash Bros. Ultimate — How to Smash](https://www.smashbros.com/en_US/howtoplay/index.html).** Date: Publication/update unknown; footer copyright 2018 is not a publication date. Publisher/host: www.smashbros.com. Edition/build: Nintendo Switch official overview; development-footage disclaimer. Source type: Official developer/publisher game documentation. Access: `relevant-excerpt`.
**Locator:** Opening description, line 19; version/footage caveat, lines 61–63. **Claims:** C-01/C-02. **Limits:** Narrow support for an off-stage victory objective; not all platform-fighter rules or actual gameplay observation. **Independence:** Nintendo / Super Smash Bros. Ultimate; same production origin as 007.
