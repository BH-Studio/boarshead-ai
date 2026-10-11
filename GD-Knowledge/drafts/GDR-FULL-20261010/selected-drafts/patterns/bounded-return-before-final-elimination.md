---
id: GDR-CAND-20261010-G21-PAT-02
kind: pattern
title: Bounded return before final elimination
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
- conditional return with terminal cutoff
- recoverable team elimination
tags:
- recovery
- terminal-state
- team-dependence
- session-contract
- untested-pattern
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-G21-PAT-01
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G21-GEN-01
- GDR-CAND-20261010-G21-GEN-02
- GDR-CAND-20261010-G21-GEN-03
source_ids:
- GDR-SRC-20261010-G21-013
- GDR-SRC-20261010-G21-014
- GDR-SRC-20261010-G21-015
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
hash_record: ../reviews/full-run-20261010-g21-review-packet.md
---

# Bounded return before final elimination

**Untested reusable pattern candidate.** Give a temporarily defeated participant a conditional route back to meaningful participation while keeping the terminal result explicit. This is not a universal recovery rule, a retention intervention or a promise that more return opportunities are better. Proposed canonical ownership is Foundations/social-session systems, pending Coordination and duplication review.

## Purpose

Address the mismatch between temporary defeat and a group activity that continues without the defeated participant. The intended outcome is not more time logged. It is an intelligible opportunity to resume a valued role without concealing the risk, waiting, teammate burden or final cutoff. Strict elimination remains a valid alternative. [C-01]

## Context and prerequisites

Use only when the activity has a defined terminal unit and result, useful play remains after a possible return, and the audience’s intended experience permits some temporary defeats to be recoverable. The unit may be a team in an elimination contest or a group in a bounded mission. A persistent avatar that always revives in an open world does not automatically fit this pattern. [C-02]

Required inputs are defeat states, eligibility conditions, return opportunities, finality conditions, re-entry capabilities and the participant’s actual exit options. “Bounded” means the rule gives an intelligible limit or terminating event; it does not imply a universal wall-clock duration or a guaranteed return. Do not display a guaranteed countdown when an undisclosed dependency can cancel it. [C-02; C-04]

**Exit without adding return** when strict finality is central, when meaningful participation cannot be restored, when return creates unavoidable repeated defeat, or when the operator cannot explain or support the edge cases. Compare a shorter round, optional spectating, a separate next activity or simple terminal elimination instead. [C-02; C-05]

## Mechanism and evidence, link by link

| Link | Inspected support | Evidence limit |
|---|---|---|
| Temporary defeat need not immediately end terminal team eligibility. | Official Reload rules and historical PUBG Recall describe this distinction. [C-03] | Documentary mechanics, not direct client observation. |
| A conditional route can make re-entry possible. | PUBG 23.2’s recovery/registration/transport chain; Reload’s different surviving-team contract. [C-03] | Possibility is not useful participation or a positive experience. |
| Exposing prerequisites and finality may improve understanding. | Reviewed F01 state/rule reasoning, P02 fact preservation and F07 commitment/return framing. [C-04] | No G21 test of comprehension or transfer. |
| Shorter or clearer waiting may restore more valued decisions. | PUBG 32.1 documents a later design response to waiting and landing feedback. [C-06] | Developer rationale, not an independent causal evaluation; exact effects unestablished. |
| Benefit can outweigh loss of stakes and teammate burden. | Pattern hypothesis only. [C-05] | Could fail even with perfect technical execution and accurate disclosure. |

PUBG’s versions are one production lineage. Epic provides a separate implementation account, not a replication study. No participant, telemetry or moderation test was performed. [C-03; C-05]

## Recipe

1. **Declare the terminal unit and stakes.** State whose final defeat ends eligibility and what is lost outside the activity, if anything. Separate individual incapacity from team finality. Reject vague language such as “you can always come back.” [C-02]
2. **Specify states before rewards.** Write active, incapacitated, defeated-but-eligible, prerequisite-met, return-pending, returned, and finally-out where applicable. A simpler mode may omit intermediate states. Define which actions and information are available in each. [C-02; C-04]
3. **Choose one primary recovery dependency.** Compare self-recovery, teammate intervention, scheduled return conditional on team survival, or no return. Explain what risk is moved from the defeated player to others and whether they may decline. Avoid combining several dependencies merely to make waiting appear earned. [C-05]
4. **Define the bound and failure transitions.** Specify the last eligible phase/event, cancellation conditions, last-survivor defeat and what happens when a player disconnects or chooses to leave. If waiting depends on another action, show that dependency rather than imply an inevitable return time. [C-04]
5. **Specify useful re-entry.** Choose location, information, capabilities and vulnerability with the remaining activity in mind. Compare the opportunity to participate with the advantage imposed on opponents. Stop if return is merely another immediate defeat or an unexplained free attack. [C-05]
6. **Communicate eligibility separately from intention.** Show what is possible, what an ally is attempting, what has been completed and what remains uncertain. A request for rescue is not proof that rescue is safe or obligatory. Use factual state descriptions across channels, not only color or celebratory animation. [C-04]
7. **Walk all terminal and interruption cases.** In a paper review, include the last ally lost during a pending return, the cutoff crossed during an interaction, departure after registration, a changed re-entry area and a disconnected returning player. Resolve contradictory promises before a prototype. No engine code is authorized. [C-04; C-07]
8. **Compare with strict elimination and stop when necessary.** Test valued participation, waiting, comprehension, earnedness and teammate pressure independently. Omit the pattern if it preserves none of the intended stakes without imposing unwanted burden. [C-05; C-07]

## Example state contract — illustrative, not a shipped rule

| Current state | Relevant event | Next state and required explanation |
|---|---|---|
| Active | Temporary incapacity | Incapacitated; distinguish immediate help from the later return system. |
| Incapacitated | Immediate recovery fails | Defeated-but-eligible only if the return conditions still hold; otherwise finally-out. |
| Defeated-but-eligible | Ally chooses and completes the prerequisite | Return-pending; show what remains, not a success claim about actual participation. |
| Return-pending | Scheduled opportunity occurs while eligibility remains valid | Returned; explain location, capability and current activity state. |
| Any eligible/pending state | Terminal team condition or return cutoff occurs | Finally-out; cancel obsolete instructions and explain why. |
| Defeated/pending | Participant chooses departure | End their participation under the disclosed contract; explain effects on allies without moralizing. |
| Any nonterminal state | Connection interruption | Apply a separately specified reconnect policy; do not silently classify interruption as misconduct. |

This table is an illustrative hypothesis about specification clarity. It does not prescribe a particular game’s disconnect or penalty policy. [C-02; C-04]

## Adjustable variables

Choose locally: the winning unit; allowed number or phase of return opportunities; prerequisite actor; risk and cost; time/event bound; re-entry location; restored capabilities; opponent warning; spectator information; return eligibility after disconnect; and the player’s choice to leave. These variables interact. A safer location can restore agency while enabling an unfair flank; shorter waiting can reduce exclusion while weakening elimination stakes. [C-05]

Do not copy an example’s timers, phase numbers, team count or equipment grants as defaults. Official descriptions can change by patch and platform; a mode-specific configuration is not a genre law. [C-03; C-06]

## Worked examples

### Illustrative team mission: recovery transport

A fictional team is attempting a bounded rescue mission. A temporarily defeated member can return if a teammate completes a recovery interaction before the final transport departs. The teammate chooses whether to incur that risk. Successful interaction creates a pending return, not instant participation. The returning player is told the current team objective and what their restored equipment permits. [C-02; C-04]

Apply the edge-case walk: if the last eligible teammate is lost before transport, end eligibility and cancel the return prompt; if the defeated participant leaves, tell the remaining team so they do not perform a pointless task; if the only return location is now inaccessible, the supposed recovery fails the useful-participation prerequisite. Compare a different insertion, shorter mission or no return rather than hide the defect with a timer. This example is invented and has not been playtested. [C-04; C-05]

### Documentary alternatives

PUBG’s 23.2 and 32.1 records show that a teammate-dependent return can be redesigned over time. Reload’s announcement describes a different survival-and-cutoff contract. These alternatives justify investigating the design space; they do not establish that either is better, less frustrating or transferable to the fictional mission. See the full versions and locators below. [C-03; C-06]

## Tradeoffs and simpler alternatives

Return can give a defeated participant another decision while making opponents’ victories less final. Teammate-mediated recovery can create an objective but also a coercive demand. Automatic return can remove rescue labor while encouraging risk-taking that the intended experience does not value. Perfectly accurate status can still describe an unwanted wait. [C-05]

Compare strict elimination with a shorter next round, optional spectator roles, post-match debrief, or ordinary non-elimination respawning. A spectator contribution must be wanted and must not leak prohibited information; it is not “participation” merely because someone remains connected. The inspected F07 safe-exit pattern remains a separate commitment/return audit; this pattern adds the recovery-and-terminal-state design, not a generic exit checklist. [C-04; C-05]

## Failure cases, counterexamples and do-not-use conditions

**False return promise:** a timer continues after eligibility ends. Correct the state authority and message. **Repeated defeat:** return happens but offers no useful action. Change re-entry or reject the pattern. **Rescue coercion:** the surviving player is pressured to take an unwanted risk; assess the social contract, not just rescue frequency. **Stakes collapse:** opponents cannot convert a valued success into progress; preserve a terminal limit or prefer strict elimination. **State explosion:** every map, item and interruption creates a new exception; simplify dependencies before adding content. [C-04; C-05]

The strongest opposing case is a strict last-survivor experience whose meaning depends on individual finality. A recovery rule can directly harm its central promise even when many other games use one. A second counterexample is a very short round where the recovery procedure lasts longer and is less useful than beginning again. No universal duration separates those cases. [C-05]

Do not use the pattern to conceal an attendance requirement, increase session statistics, require a purchase to avoid an unwanted wait, or imply a safety/wellbeing guarantee. These are proposed ethical limits for review, not claims of legal compliance. [C-05]

## Proposed falsifying playtest — not performed

**Question:** does conditional return restore valued decisions without unacceptable waiting pressure, lost stakes or misleading eligibility? Compare strict elimination, one conditional-return contract and a simpler return alternative. Keep initial defeat, remaining objectives and opponent capability comparable; disclose all participation and exit conditions. [C-07]

Include people who prefer strict finality, friend groups, unfamiliar teams, early-eliminated participants and relevant access needs. Do not recruit only players who already like recovery modes. Gather predicted eligibility before outcomes, actual chosen rescue/leave decisions in the prototype, active versus waiting time, immediate repeat-defeat frequency, perceived earnedness and teammate burden. No real harassment or punitive live-account experiment is proposed. [C-07]

Falsify the benefit claim if extra logged time is the only improvement, if return creates no valued decision, if understanding depends on an inaccessible cue, or if preserving one audience’s stakes requires conditions another intended audience cannot reasonably accept. A mixed result calls for a narrower mode/audience claim, not averaging away the conflict. Determine sample size and meaningful-change thresholds through a separate local method review. [C-07]

## Claim ledger

| Claim | Proposition / class | Support and locator | Confidence and limit |
|---|---|---|---|
| C-01 | Temporary defeat and continuing group activity can create a participation mismatch; `inference`. | `GDR-SRC-20261010-G21-013`/`GDR-SRC-20261010-G21-015` documentary structures. | Moderate conceptual distinction; not every defeated player wants to return. |
| C-02 | Explicit terminal and recovery states are prerequisites for this recipe; `hypothesis`. | C-01 plus state-contract reasoning. | Low benefit confidence; may be unnecessary for simple strict elimination. |
| C-03 | Scoped return structures exist in the inspected official accounts; `observed-example` of documents. | `GDR-SRC-20261010-G21-013`, Recall Process/More Info; `GDR-SRC-20261010-G21-015`, reboot/cutoff. | High historical description confidence; no played-build or causal proof. |
| C-04 | Communicate prerequisites, uncertainty and finality separately; `inference`. | F01 corrected learning, P02 fact preservation and F07 safe-exit excerpts. | Moderate reasoning; actual comprehension remains untested. |
| C-05 | The recipe may restore valued participation with acceptable costs; `hypothesis`. | C-01–C-04 and explicit counterexamples. | Low; no intervention study, wellbeing or retention guarantee. |
| C-06 | A later PUBG update revises return timing/presentation with feedback rationale; `practitioner-heuristic`. | `GDR-SRC-20261010-G21-014`, Recall and Dev’s Comment. | High attribution; same source lineage, no independent outcome evaluation. |
| C-07 | Proposed comparisons could reject or narrow the pattern; `hypothesis`. | C-02/C-05 and F07 evaluation excerpt. | Low until method review and execution; no tests performed. |

## Related entries, ownership and history

Adaptations: [battle royale](../genres/battle-royale.md), [MOBA](../genres/moba.md) only for appropriate elimination variants, and [MMO](../genres/mmo.md) only for bounded activities rather than persistent character life generally. Complement: [Public pressure, private position](public-pressure-private-position.md) when return eligibility depends on a public phase.

Inspected related identities: `GDR-CAND-20261010-F01-TOP-03`, `GDR-CAND-20261010-F01-PAT-01`, `GDR-CAND-20261010-F07-TOP-01`, `GDR-CAND-20261010-F07-PAT-02`, and `GDR-CAND-20261010-P02-PAT-02`; see [exact dependency receipt](../reviews/full-run-20261010-g21-review-packet.md#inspected-reviewed-dependencies). F06 social/session selected bytes are still missing. Novelty review must distinguish this terminal-state recipe from existing safe-exit and recovery work before canonical allocation.

Conflicts: `G21-CON-06`, `G21-CON-07` and `G21-CON-08`. `0.1.0`, `initial-authoring-1`; no predecessor or supersession. Author self-review only. Exact hash is external in the packet. Source and coverage remain open, and any pattern beyond this packet’s two candidates is queued separately rather than assigned an unregistered child key.

## References

All sources were inspected on **2026-10-10, America/Los_Angeles session date**. Access describes the material actually read, not the availability of an entire website. No game client or recording was observed; game examples below are observations of official documentary artifacts. No third-party pages linked by these documents are implicitly inspected. Source identities are run-scoped; central URL/DOI/edition deduplication remains pending. Rights: copyrighted material is paraphrased; no screenshots, substantial quotations, chat logs or source PDFs are redistributed. No reuse license is assumed.

### GDR-SRC-20261010-G21-013

PUBG: BATTLEGROUNDS Team / KRAFTON. *Patch Notes — Update 23.2*. 2023-05-10. PUBG official site. [Inspected source](https://pubg.com/en/news/6292).

**Version/build:** Update 23.2, PC/console schedules and mode/map limits as documented; not current runtime. **Access:** `relevant-excerpt`; New System: Recall; Blue Chip Tower/Transmitter; Recall Process; More Info; Dev’s Comment; retrieved lines 94–176. **Type:** official patch documentation and developer rationale. **Supports:** C-01/C-03. **Limits and independence:** Historical phase-based return; later 32.1 changes timing. “No cap” prose is qualified by explicit phase/flight constraints. Same production lineage, not independent corroboration.

### GDR-SRC-20261010-G21-014

PUBG: BATTLEGROUNDS Team / KRAFTON. *Patch Notes — Update 32.1*. 2024-10-09. PUBG official site. [Inspected source](https://pubg.com/en/news/7810).

**Version/build:** Update 32.1; documented PC October 10 / console October 17 maintenance; runtime unverified. **Access:** `relevant-excerpt`; Recall and adjacent Dev’s Comment, retrieved lines 193–221; publication header and maintenance scope. **Type:** official patch documentation and developer rationale. **Supports:** C-06. **Limits and independence:** Later account changes 23.2 return timing and route information. Feedback rationale is not an outcome evaluation. Same source family as 013; preserve version distinction.

### GDR-SRC-20261010-G21-015

The Fortnite Team / Epic Games. *Squad Up for Fortnite Reload!*. 2024-06-22; update 2024-06-27. Fortnite. [Inspected source](https://www.fortnite.com/news/squad-up-for-fortnite-reload).

**Version/build:** Reload launch announcement plus dated update; not all Fortnite modes. **Access:** `relevant-excerpt`; Opening; reboot rules and late-match cutoff; squad win condition; retrieved lines 1–66. **Type:** official mode announcement. **Supports:** C-01/C-03. **Limits and independence:** Recoverable individual elimination coexists with a terminal squad result. No measured retention or frustration benefit; linked mode-specific timing changes not independently inspected.

