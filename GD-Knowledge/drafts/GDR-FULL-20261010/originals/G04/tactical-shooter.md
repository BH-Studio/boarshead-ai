---
id: GDR-CAND-20261010-G04-GEN-02
kind: genre
title: Tactical shooter
version: 0.1.0
candidate_revision: initial-capture-1
status: draft
run_id: GDR-FULL-20261010
batch_key: G04
attempt_id: G04-authoring-01
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- tactical FPS
- tactical shooting
- cooperative tactical shooter
tags:
- planning
- information-uncertainty
- role-coordination
- recoverability
- lethality
- genre-boundaries
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
- GDR-CAND-20261010-G04-PAT-01
- GDR-CAND-20261010-G04-PAT-02
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G04-GEN-01
- GDR-CAND-20261010-G04-GEN-03
source_ids:
- GDR-SRC-20261010-G04-001
- GDR-SRC-20261010-G04-015
- GDR-SRC-20261010-G04-006
- GDR-SRC-20261010-G04-007
- GDR-SRC-20261010-G04-002
- GDR-SRC-20261010-G04-013
- GDR-SRC-20261010-P02-001
- GDR-SRC-20261010-P02-005
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G04 capture; no prior G04 candidate superseded.
byte_hash_record: ../reviews/full-run-20261010-g04-integrity-receipt.md
coverage_state: bounded-research-completed-coverage-open
independent_review: not-performed-for-G04
---

# Tactical shooter

**Version 0.1.0 · initial-capture-1 · draft · coverage open.** This entry supplies conditional genre guidance, not real-world tactical training, a realism standard or a fixed lethality recipe. No game scenario, player recording or participant session was inspected or performed.

## Definition and contested boundaries

Here, **tactical shooter** identifies a shooting-centered mode in which acquiring and interpreting information, preparing a commitment, coordinating complementary actions or managing consequential failure materially shapes the player’s options. It is a proposed working boundary. Slow movement, military uniforms, complex equipment menus and short time-to-kill do not by themselves establish tactical decision quality. A tactical decision is evaluated relative to the goal, available evidence, feasible alternatives and cost—not simply whether it wins. [C-01, C-02]

The [shooter parent](shooter.md) owns shared aiming and hit-feedback concerns. This file adds information asymmetry, preparation, role interdependence and recovery analysis; it does not repeat a generic weapon survey. An arena shooter can have deep tactics without being marketed as this subgenre. A simulation can prioritize authored procedures or fidelity over competitive symmetry. An [extraction hybrid](extraction-game.md) adds retention across excursions, but tactical classification does not require persistent inventory loss. [C-01, C-10]

First/third-person view, cooperative versus competitive mode, solo command and realistic-styled presentation remain facets. “Realistic” is a claim requiring a reference and scope: visual plausibility, ballistics, procedural representation and AI behavior are different propositions. This packet verifies none as a real-world fidelity standard. [C-01, C-04, C-12]

## Custom research instructions

Use an **identified mode or scenario**, not a game title, as the comparison unit. Record the objective, force composition, teammate control, known and hidden information, action commitments, error consequences, recovery routes, communication channels and exact build. A moderated cooperative scenario and a competitive round do not share all relevant invariants. [C-03, C-04, C-10]

For each claimed tactical choice, reconstruct what the player knew before acting. Identify at least one plausible alternative and the evidence that would favor it. Separate a sound decision that fails execution from a poor decision that succeeds through execution, surprise or chance. Riot’s tac-cycle account is useful practitioner framing, not evidence that every game must pause through four named stages. [C-02]

Investigate realistic-styled cooperative/simulation contexts alongside stylized competitive rounds. Challenge comparisons that equate low time-to-kill with more thinking, high equipment complexity with meaningful preparation, frequent communication with useful coordination, or punishing failure with fair commitment. Seek contrary cases where an extra planning burden adds no consequential choice or where an ostensibly “slower” setting gives a player less opportunity to respond. [C-01, C-05–C-08]

For mechanics use official rules, versioned changes and reproducible scenario evidence. For effects on cooperation, disengagement or exclusion, require observed tasks with relevant participants, not promotional statements or spectator intuition. This batch has documented production contrasts but **no controlled tactical-TTK or nonvoice-team-effectiveness study**. Those effects remain hypotheses. [C-04, C-06, C-07, C-11]

## Player promises and varied audiences

Candidate promises include making preparation matter, coordinating without redundant roles, reading an uncertain situation, executing a deliberate commitment and understanding why a plan failed. Some groups instead emphasize authenticity, social role play, competitive mastery or cooperative problem solving. These are elicitation categories, not demonstrated universal expectations of tactical-shooter players. [C-01, C-08]

A solo player commanding AI, an established voice squad and a mixed-language public team face different social demands. Avoid treating microphone access, rapid speech, hearing acuity, military vocabulary or willingness to follow a stranger’s command as a prerequisite shared by all intended players. The proposed design question is whether the player can contribute to the important decisions through a supported route. It is not whether every route can produce identical performance. [C-07, C-08, C-12]

## Characteristic loops and structures

At encounter scale, analyze information gathering → provisional plan → committed action → reassessment. These can overlap, repeat or be compressed into moments. Preparation is valuable only conditionally: if the obtained information or selected equipment cannot change a feasible action, the phase may be ceremony rather than a tactical choice. [C-01, C-02, C-08]

At session scale distinguish a round with an elimination/reset structure, a cooperative mission with objectives and teammate recovery, and a scenario whose rules are controlled by an author or moderator. Riot’s support description, Arma’s scenario overview and VOID’s cooperative mission positioning provide these different contexts; none supplies a universal commitment duration. [C-03, C-04]

At longer horizons explicitly enumerate what persists: learned map knowledge, a campaign consequence, a role unlock, a shared stockpile or nothing beyond a score. Persistence within a round is not persistent character loss; persistent character loss is not necessarily account-level economic disadvantage. F03 owns detailed resource/progression treatment, and no unreviewed F03 claim is imported here. [C-10]

## Characteristic decisions and conditional application

### Lethality, reaction and recoverability

Define **time-to-kill** before using it: damage model and starting state, weapon/target combination, hit assumptions and measured interval. Do not conflate it with time to recognize a threat, select an action, execute movement, recover an ally or regain participation after failure. Under otherwise fixed conditions, a shorter interval to elimination leaves less room for post-contact correction. The design consequence is conditional: reliable advance information and viable cover may make preparation matter; absent alternatives may instead make contact functionally unanswerable. [C-05]

Therefore inspect the whole sequence: evidence before contact; opportunity to decline or reposition; intelligibility of the commitment; actions still possible after contact; recovery after failure. Changing only health can change some intervals while leaving an unfair sightline, misleading cue or inaccessible input untouched. No millisecond, hit-count or movement-speed default is justified by this research. [C-05, C-12]

**Competing hypotheses:** strong consequences may reward careful coordination, but may also make waiting, avoidance or disengagement the locally sensible choice. Neither reaction is inherently irrational. Evaluate whether those choices fit the intended mission and voluntary player goals; do not “fix” disengagement solely by making exit more punitive. [C-06]

### Information uncertainty without sensory exclusion

Distinguish information intentionally unavailable to everyone from information available through a channel some intended players cannot use. Keep uncertainty about the unseen opponent when that is part of the task; do not require exclusive hearing of a key cue as its only representation. For a ping or caption, specify what is known, its source, reference frame, certainty and expiration. A cue alternative must not covertly upgrade an ambiguous sound into exact enemy identity. [C-07]

An action wheel, prewritten message, shared marker or accessible text/speech route may replace parts of voice coordination, but complex negotiation is not automatically reduced to a ping. If an essential coordinated action has no timely usable communication path, revise the action, offer an appropriate mode or narrow the claimed support explicitly. Do not describe a menu’s mere existence as successful inclusion. [C-07, C-12]

### Roles, preparation and consequences

| Design choice | Use when / evidence-to-application bridge | Alternative and failure signal |
|---|---|---|
| Specialist roles | Distinct information or action capabilities can create reasons to coordinate. Specify how each changes a feasible plan. | A “support” role that only waits for others is not meaningful by definition. Permit alternative participation or revise the interdependence. Benefit remains a hypothesis. [C-08] |
| Pre-mission loadout | Preparation matters when equipment changes route, identification, protection, utility or recovery options under known constraints. | Excess inventory detail can obscure the actual choice. A simpler default may fit a session whose main promise is execution. [C-02, C-08] |
| Solo command versus human team | Decide which orders must be authored and understood, who can refuse or revise, and what happens when AI or teammates cannot comply. | Do not evaluate solo command friction as a player’s low motor skill. Do not silently replace human negotiation with perfect AI information. [C-04, C-07, C-08] |
| Identification / restraint | When neutral or protected entities matter, the player needs legitimate evidence for the required distinction and an intelligible rule for acting. | Do not use racial, linguistic or clothing stereotypes as a substitute for rule-relevant signals. Ambiguity may be intentional, but its cost must be examined rather than called realism. [C-09] |
| Mission or campaign persistence | Retained consequences can make a decision extend beyond the current exchange. Specify whose future options are affected. | A fresh round or reversible training scenario may better support experimentation. Persistence is optional, not a quality certificate. [C-10] |

### Application process

First choose the intended decision and the information contract. Next diagram the commitment and recovery states for each role, including a declined action, late message and missing teammate. Choose a single intervention against a diagnosed obstruction: cue meaning, action demand, route availability, role capability or consequence scope. Then compare decisions made with equivalent available evidence, keeping successful execution distinct from understanding. Reject or revise when the intervention merely makes a number easier while leaving the intended tactical choice inaccessible or dominated. [C-02, C-05, C-07, C-08, C-11]

## Applying shared topics and patterns

F02 changes the tactical review from “did the team win?” to “was the choice reasonable given available evidence, feasible alternatives and costs?” Its challenge topic requires separating perception, planning, motor and social demands. P02 changes coordination review from “is there voice/text?” to “what fact arrived in time through the configured route?” F07 adds affected teammates, consent, stopping and appropriate interacting-player measurement. These are **inspected draft transfers**, not inherited empirical proof. [C-DEP]

Use [Provisional-versus-confirmed impact feedback](../patterns/provisional-versus-confirmed-impact-feedback.md), `GDR-CAND-20261010-G04-PAT-01`, only where attempts can be mistaken for confirmed results. It is not a tool for revealing hidden hit locations. Use P02’s fact-preserving cue alternatives for uncertain location reports and commands; that existing pattern remains separately owned. [C-07, C-12]

Use [Viable baseline re-entry loadout](../patterns/viable-baseline-re-entry-loadout.md), `GDR-CAND-20261010-G04-PAT-02`, only for a persistent-resource hybrid that can lose access to a meaningful next attempt. A self-contained competitive round may not need it. The inspected F07 safe-exit pattern concerns voluntary participation, not an entitlement to survive a contested mission or abandon teammates without consequences. [C-10, C-DEP]

## Representative and negative cases

| Case and evidence route | Useful contrast | Restriction on inference |
|---|---|---|
| VALORANT, official support and designer account | Stylized abilities and a central round format can coexist with a tactical framing. | No finding that fantasy abilities inherently improve depth or that every playlist shares the guide’s format. [C-02, C-03] |
| Arma 3, official multiplayer overview | Cooperative, authored/moderated and community scenario contexts require scenario-level analysis. | No commanding-manual or actual scenario verification; legacy page is not a live rules specification. [C-04] |
| Ready or Not, developer storefront text | Cooperative mission context explicitly includes identification and consequential mission framing. | Promotional “realistic” and “true tactical” claims are not independent validation; detailed scoring and nonlethal behavior remain unverified. [C-04, C-09] |

**Illustrative worked case — relay recovery.** A fictional squad must retrieve a signal module without disabling neutral maintenance drones. One role can interpret a temporary route status, another can move the module, and any player can request a regroup. The status message says only “east route obstructed,” not the identity of an unseen cause. An established voice team can negotiate; a nonvoice team has route markers, an acknowledgment and a “not ready” signal. No shipped game is being described. [C-07, C-08, C-11]

Before changing lethality, inspect whether the module carrier received the obstruction fact and had a feasible alternate route. If not, a health change does not demonstrate improved decision quality. In a proposed comparison, change the route condition so that the previously sensible plan is no longer favored; retain access supports. Ask what each player predicts, which plan they prefer and why. A deliberately cautious refusal is not a learning failure. If the nonvoice route cannot support the required negotiation in time, revise the coordination demand instead of describing players as uncooperative. [C-05, C-07, C-11]

**Strong negative cases:** a low-health corridor with an unavoidable unseen shot provides little tactical choice regardless of realistic presentation. Conversely, a fast exchange can still involve meaningful information and commitment. A cooperative group may knowingly prefer extensive procedure to competitive efficiency; that preference is not disproved by a longer completion time. These are conditional analytic counterexamples, not observed participant results. [C-01, C-05, C-06]

## Accessibility, ethics, localization and production

Separate target acquisition from repeated presses, long holds, command-menu navigation and communication demands. Test remapped labels and activation options with the actual combination of movement, aiming and orders. Microsoft’s guidance supports accessible input and communication pathways but supplies no evidence that one generic command wheel works for every encounter. [C-07, C-12]

Localize concise status, uncertainty and cancellation semantics, not only item names. Check direction frames when teammates face different ways, text expansion, speech recognition errors and message obsolescence. A mistranslated or stale command can change the apparent plan; do not compensate by exposing more hidden state in only one language. [C-07, C-12]

Production review must include AI obedience and failure reporting, replay/trace interpretability, network correction, combinations of equipment and role abilities, safe handling of disconnects, and the authoring cost of alternative communication. A realistic-styled surface can raise research obligations without proving the underlying systems meet them. Depictions of policing, civilians and violence need separate contextual and representation review; fictional tactical efficacy is not ethical justification. [C-09, C-12]

## Research questions and validation — proposed, not performed

**T-A: What actually makes contact recoverable?** In a consent-based fictional scenario, vary one lethality condition while holding objectives, knowledge, routes and targeting behavior constant; then separately compare an information/route intervention. Record evidence available before contact, feasible actions, recognition, attempted response, outcome, waiting and voluntary decline. Include relevant input/access configurations and experience levels. A result in which players still lack actionable evidence or routes rejects the claim that the lethality setting alone fixed the problem. Do not infer tactics from win rate. [C-05, C-06, C-11]

**T-B: Can the role’s important facts be coordinated without mandatory voice?** Compare supported communication configurations with the same legitimate information. Evaluate intact squads or appropriately modeled interacting groups, not each callout as an independent player. Measure misinterpreted state, late/obsolete messages, participation, role ownership, burden and chosen strategies. Record familiarity, language and pre-existing teamwork as confounds. Reject claimed coverage when one route cannot communicate a necessary fact in time, even if average success appears similar. No equivalence margin is assumed. [C-07, C-08, C-11]

**T-C: Is a preparation choice consequential rather than ceremonial?** Present cases where different mission facts change which equipment or plan is advantageous. Ask prediction, rationale and preference separately, preserving the F01 changed-answer correction. Reject the design claim when informed players cannot identify any feasible consequence of their choice, or when only hidden author knowledge makes the “correct” plan sensible. [C-02, C-08, C-11]

## Coverage, gaps and review history

Researched: contested boundaries; competitive/cooperative/scenario contrast; planning versus execution; conditional lethality/recovery reasoning; information/voice access; role and persistence distinctions. Open: direct lethality/disengagement evidence, representative nonvoice squad studies, current Arma commanding bytes, detailed Ready or Not scoring/AI behavior, particular weapons/builds, long-term campaign effects and player populations beyond official descriptions. Combat/traversal, multiplayer systems, encounter geometry and economy ownership links need coordination; no missing candidate IDs are fabricated. [C-01–C-12, C-DEP]

This is initial capture, not a correction or a replacement of earlier batches. Author self-review is in the packet; independent G04 review and release remain pending. Static file checks are not host retrieval tests or gameplay validation. [C-DEP]
## Inspected shared guidance and dependency status

These are parent-selected **0.1.0 draft** dependencies, not released references. Relevant bytes were inspected in the cumulative archive; no earlier batch is resubmitted. This transfers scoped reasoning, not the empirical findings of unopened underlying papers. Full identity/hash receipt and the exact missing-source list are in the [review packet](../reviews/full-run-20261010-g04-review-packet.md#reviewed-dependencies).

| Selected candidate | Revision and precise local locator | Conditional transfer |
|---|---|---|
| `GDR-CAND-20261010-F02-TOP-01` | `initial-capture-1`; archive `selected-drafts/topics/decision-design.md`, lines 53–75; 95–128 | Decision quality versus outcome, legitimate uncertainty, reversibility and opportunity cost. |
| `GDR-CAND-20261010-F02-TOP-02` | `independent-review-correction-1`; archive `selected-drafts/topics/challenge-and-difficulty.md`, lines 55–77; 125–137 | Demand decomposition, recovery as a viable state, affected parties and invariants. |
| `GDR-CAND-20261010-P02-TOP-01` | `review-correction-1`; archive `selected-drafts/topics/controls-and-input.md`, lines 60–105; 109–120 | Action/binding/activation distinctions, physical demand and device parity limits. |
| `GDR-CAND-20261010-P02-TOP-02` | `review-correction-1`; archive `selected-drafts/topics/feedback-and-game-feel.md`, lines 77–89 | Attempt, acceptance, pending and outcome are different facts; no fixed cue quota. |
| `GDR-CAND-20261010-P02-TOP-03` | `review-correction-1`; archive `selected-drafts/topics/multimodal-communication.md`, lines 84–96; 119–130 | Alternative cues preserve known facts, uncertainty and decision timing. |
| `GDR-CAND-20261010-P02-PAT-02` | `review-correction-1`; archive `selected-drafts/patterns/fact-preserving-cue-alternatives.md`, lines 50–107 | Information contracts, configured alternatives, and rejection when timely meaning is lost. |
| `GDR-CAND-20261010-F07-TOP-01` | `initial-capture-1`; archive `selected-drafts/topics/evaluation-and-balancing.md`, lines 67–93; 123–133 | Denominators, qualitative explanation and interacting-player units. |
| `GDR-CAND-20261010-F07-TOP-02` | `initial-capture-1`; archive `selected-drafts/topics/ethical-and-sustainable-design.md`, lines 62–90; 106–128; 156–172 | Voluntary challenge differs from coercion; refusal, stop, return and harm guardrails. |
| `GDR-CAND-20261010-F07-PAT-02` | `initial-capture-1`; archive `selected-drafts/patterns/legible-commitment-and-safe-exit.md`, lines 50–104 | Informed participation and bounded exit; not guaranteed in-game victory or costless abandonment. |
| `GDR-CAND-20261010-F01-PAT-01` | `independent-review-correction-1`; archive `selected-drafts/patterns/supported-attempt-and-transfer-check.md`, lines 98–120 | Changed-answer transfer cases; separate understanding from preference; retain access support. |
| `GDR-CAND-20261010-P01-TOP-03` | `review-correction-1`; archive `selected-drafts/topics/accessibility-and-inclusive-interaction.md`, lines 60–102; corrections/P01/CORRECTION_RECEIPT.md | CSS-pixel pointer scope, rendered text-body height, scaling and platform context must not be collapsed. |

F03 progression/economy and F04 combat/traversal outputs are **unreviewed running/queued dependencies without inspected bytes here**. No exact candidate ID or path is invented. Current canonical index/pending allocations and the live recovery ledger are missing. Shared ownership links remain proposals. The supplied audio pilot is hypothesis context only, never a requirement for this genre or recipe. [C-DEP]

## Claim ledger

Claim classes describe support, not certainty. `observed-example` refers only to the identified document when no game observation is stated. Confidence applies to the narrowly worded claim.

| Claim | Precise claim | Class | Sources and locators | Confidence and reason | Limits / unresolved question |
|---|---|---|---|---|---|
| C-01 | Tactical shooter is a useful conditional label when shooting outcomes depend materially on information, preparation, coordinated action or consequential commitment; slowness and realism are not sufficient tests. | inference | Dispatch §Domain questions; GDR-SRC-20261010-G04-001: tac cycle; GDR-SRC-20261010-G04-006: Co-op/Zeus; GDR-SRC-20261010-G04-007: Features | Moderate for a working distinction across the documented cases, not universal taxonomy. | A fast arena encounter can contain tactics without adopting this genre label. |
| C-02 | Riot describes an intel–plan–execute cycle and acknowledges planning and execution can come apart. | practitioner-heuristic | GDR-SRC-20261010-G04-001: Balance Do’s and Don’ts | Moderate: firsthand design model, no isolated causal test. | Not a mandatory phase sequence for every tactical game. |
| C-03 | The inspected VALORANT support page describes a team, round-based, central one-life format. | observed-example | GDR-SRC-20261010-G04-015: So what is VALORANT? | High for the support description only. | Do not generalize to every mode, ability exception or current build. |
| C-04 | Cooperative/scenario and simulated-policing examples create different comparison contexts from a competitive round. | observed-example | GDR-SRC-20261010-G04-006: Co-op/Zeus/Community Content; GDR-SRC-20261010-G04-007: Features and Take Command | High for stated product positioning and listed features. | No Arma scenario or Ready or Not mission was played; realistic/tactical marketing is not validated quality. |
| C-05 | Short damage-to-elimination time reduces post-contact opportunities under otherwise fixed conditions, but does not determine total recoverability or tactical quality. | inference | F02-C demand/recovery analysis; C-02/C-03; explicit conditional timing reasoning below | Moderate for the conditional logic; low for any population-level effect. | Changing information, geometry, movement, armor, objectives or respawn rules changes the comparison. |
| C-06 | Low lethality tolerance can encourage either deliberate preparation or disengagement depending on available counterplay and stakes. | hypothesis | C-05 causal alternatives; no direct comparative dataset inspected | Low: competing explanations, not an established behavioral effect. | No fixed TTK recipe, ideal engagement rate or universal risk-aversion rule. |
| C-07 | Information alternatives should preserve legitimate uncertainty while making required team decisions accessible without mandatory voice. | inference | GDR-SRC-20261010-G04-013: communication participation; GDR-SRC-20261010-P02-005: Goal/Overview; inspected P02-M/P02-A | Moderate as a design inference grounded in guidance. | Neither automatic transcription nor a ping guarantees timely equivalent communication. |
| C-08 | Role design should provide consequential contributions and a fallback for missing or differently configured teammates. | hypothesis | C-02/C-04/C-07; inspected F02-D/F02-C | Low for the proposed role method, though constraints are explicit. | Role equality is not identical actions or identical performance; group preferences can differ. |
| C-09 | Rules of engagement and identification costs should be evaluated from available evidence rather than presentation stereotypes. | inference | GDR-SRC-20261010-G04-007: Take Command/True Tactical Gameplay; inspected F02-D/P02-M | Moderate as an ethical/readability consequence of identification tasks. | The guide does not validate cultural authenticity, nonlethal reliability or fair NPC signaling. |
| C-10 | Persistence should be identified at round, mission, campaign and account scales instead of inferred from tactical branding. | inference | C-03/C-04 plus explicit state-scope analysis | Moderate as an analytic distinction, not a market prevalence estimate. | Exact campaign loss and economic rules remain build-specific gaps. |
| C-11 | The worked scenarios and proposed comparisons test decision quality separately from winning and preserve access supports. | hypothesis | Inspected F01-T/F07-E/F07-S; designs in this entry | Low until locally tested; no participants or gameplay tests occurred. | Teammates/opponents are interacting units, not independent observations. |
| C-12 | State clarity, input demand, localization and representation require their own review even when presentation aims at realism. | inference | GDR-SRC-20261010-G04-002: Correctness vs Clarity; GDR-SRC-20261010-P02-001; GDR-SRC-20261010-G04-013; inspected P01-A/P02-I/P02-F | Moderate for an applicability constraint; no numerical standard follows. | No real-world tactical training or implementation instruction is supplied. |
| C-DEP | Reviewed shared transfers use inspected selected bytes; missing or unreviewed dependencies remain unresolved. | observed-example | G04 review packet, reviewed-dependencies receipt | High for recorded byte identity and scope only. | No canonical or independent G04 approval is implied. |
## References

All access dates are 2026-10-10. In relationship notes, `G04-NNN` abbreviates `GDR-SRC-20261010-G04-NNN`; it is not another source identity. Observation route: assistant inspection of the identified public document, not game play, a match recording or participant observation. All excerpts are paraphrased; copyright remains with the rights holders. No source text, media or paper is redistributed. Dates refer to the named document unless explicitly identified as a game release.

### GDR-SRC-20261010-G04-001

David Cole, game designer, Riot Games. **[How We Balance VALORANT](https://playvalorant.com/en-us/news/dev/how-we-balance-valorant/)**. Date: 2020-06-26. Publisher: Riot Games. Edition/build: Historical 2020 developer account; not a current-build specification. Access: `relevant-excerpt`. Type: practitioner account.

**Precise locator:** “Balance Do’s and Don’ts,” especially tac cycle; “Balance Radar”; “Case Study: Raze”. **Claims supported here:** C-01, C-02. **Limits:** Design philosophy and a multi-change case, not an isolated causal experiment. **Independence:** Same developer as G04-002 and G04-015; not independent corroboration of their effects. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-015

whatacoolwitch, Riot Games support. **[Welcome to VALORANT](https://support.riotgames.com/en-us/valorant/gameplay/welcome-to-valorant/)**. Date: 2024-04-17. Publisher: Riot Games Support. Edition/build: Support page, no build identified. Access: `relevant-excerpt`. Type: first-party support description.

**Precise locator:** “So what is VALORANT?”. **Claims supported here:** C-03, C-10. **Limits:** Describes its central round-based format; not every playlist or respawn/revival exception. **Independence:** Same Riot group as G04-001/002; rules description is not causal confirmation. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-006

Bohemia Interactive. **[Multiplayer | Arma 3](https://arma3.com/features/multiplayer)**. Date: unknown. Publisher: Arma 3 official site. Edition/build: Legacy unversioned product overview, with future-tense passages; not current server rules. Access: `relevant-excerpt`. Type: first-party product description.

**Precise locator:** “Co-op”; “End Game”; “Arma 3 Zeus”; “Community Content”. **Claims supported here:** C-01, C-04. **Limits:** Supports scenario/mode variety only; commanding manual was inaccessible and no scenario was played. **Independence:** Independent production context from Riot/VOID; still promotional description. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-007

VOID Interactive. **[Ready or Not](https://store.steampowered.com/app/1144200/Ready_or_Not/)**. Date: page update unknown; listed game release 2023-12-13. Publisher: Developer/publisher storefront copy hosted by Steam. Edition/build: Store description inspected 2026-10-10; no executable/build verified. Access: `relevant-excerpt`. Type: first-party product description.

**Precise locator:** Developer/publisher metadata; “Features”; “Take Command”; “The Weight of the Badge”; “True Tactical Gameplay”. **Claims supported here:** C-04, C-09. **Limits:** Realism and tactical-quality language is marketing, not verification of real-world fidelity or decision quality. User reviews/tags not used as research. **Independence:** VOID supplies the description; Steam hosting does not add an independent source. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-002

Kevin Lee, game systems software engineer, Riot Games. **[The State of Hit Registration](https://playvalorant.com/en-us/news/dev/the-state-of-hit-registration/)**. Date: 2020-08-06. Publisher: Riot Games. Edition/build: 2020 account, including beta 0.50 context; proposed improvements are not verified current features. Access: `relevant-excerpt`. Type: firsthand development explanation.

**Precise locator:** “Correctness vs Clarity”; “From Click to Headshot”; “Case Study 2: Crouching into Shot VFX”; “Planned Clarity Improvements”. **Claims supported here:** C-12. **Limits:** Text inspected; embedded recordings not watched. Does not measure benefit of the G04 recipe. **Independence:** Same Riot provenance group as G04-001/015; P02 feedback transfers are not additional experiments. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-013

Microsoft. **[Xbox Accessibility Guideline 120: Communication experiences](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/120)**. Date: updated 2026-03-04. Publisher: Microsoft Learn. Edition/build: Unnumbered web guidance revision; checked 2026-10-10. Access: `relevant-excerpt`. Type: platform accessibility guidance.

**Precise locator:** “Goal”; communication participation guidance; prewritten messages, speech/text alternatives, mute/block/report and access scenarios. **Claims supported here:** C-07, C-12. **Limits:** Guidance, not a formal standard or a measured guarantee of real-time callout equivalence. No legal compliance conclusion. **Independence:** Same issuer as reused P02-001 and P02-005; not three independent studies. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-P02-001

Microsoft. **[Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107)**. Date: updated 2026-03-04. Publisher: Microsoft Learn. Edition/build: Unnumbered web guidance revision; reopened for G04. Access: `relevant-excerpt`. Type: platform accessibility guidance.

**Precise locator:** “Background and foundational information”; remapping and activation-demand guidelines, including speed, complexity, duration. **Claims supported here:** C-12. **Limits:** No universal timing value, competitive parity guarantee or formal-standard classification. **Independence:** Identity reused from inspected P02 source record; no new G04 allocation for the same source. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-P02-005

Microsoft. **[Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103)**. Date: updated 2026-03-04. Publisher: Microsoft Learn. Edition/build: Unnumbered web guidance revision; reopened for G04. Access: `relevant-excerpt`. Type: platform accessibility guidance.

**Precise locator:** “Goal”; “Overview”; “Scoping questions”; multisensory communication options. **Claims supported here:** C-07. **Limits:** No inference that simultaneous cue multiplication improves all performance; preserves meaning rather than promising equal experience. **Independence:** Identity reused from inspected P02 source record; same Microsoft guidance family as P02-001 and G04-013. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.
