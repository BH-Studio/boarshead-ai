---
id: GDR-CAND-20261010-G08-GEN-02
kind: genre
title: Real-time strategy
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_id: G08-authoring-01
run_id: GDR-FULL-20261010
batch_id: G08
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles
coverage_state: open
aliases:
- RTS
- concurrent strategic control
tags:
- concurrency
- attention
- reconnaissance
- control-access
- automation
- pause
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G08-PAT-01
- GDR-CAND-20261010-G08-PAT-02
related_genres:
- GDR-CAND-20261010-G08-GEN-01
- GDR-CAND-20261010-G08-GEN-03
source_ids:
- GDR-SRC-20261010-G08-006
- GDR-SRC-20261010-G08-002
- GDR-SRC-20261010-G08-003
- GDR-SRC-20261010-G08-004
- GDR-SRC-20261010-G08-005
- GDR-SRC-20261010-G08-010
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G08
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G08 candidate; no predecessor or release claimed.
hash_record: ../reviews/full-run-20261010-g08-integrity-receipt.md
---

> **Draft research, not released guidance.** Version 0.1.0; candidate revision `initial-draft-1`. Independent G08 review, gameplay testing and human acceptance have not occurred. Recommendations labeled `hypothesis` are proposed for evaluation, not established effects. All examples labeled *illustrative* are invented and untested. Dates use America/Los_Angeles; the run ID is unchanged.

# Real-time strategy

## Definition and boundaries

**Working usage:** Real-time strategy (RTS) combines consequential planning/allocation with relevant world-state progression while players can issue decisions. “Real-time” describes the timing relationship, not an obligation to maximize clicks, prohibit pausing, include base construction, use military conquest, or require competitive multiplayer. Pause, adjustable speed and assistance change particular demands; they do not by themselves settle the entire game’s genre. This definition is an analytical proposal, not a formal standard. [C-01]

Keep four quantities separate: simulation advancement, opportunities to issue or revise a command, command-to-result delay, and the player’s available attention. A fixed simulation rate does not imply a fixed decision rate. A queue can keep actors working while a player observes elsewhere, but it can also commit them to a now-inappropriate plan. A real-time tactics encounter without production can share these concerns while remaining within G07’s unresolved tactics scope. [C-01; C-05; C-07]

The [Strategy parent](strategy.md) supplies goal/commitment analysis. This file specializes concurrency, attention scheduling, reconnaissance and the interaction between ongoing processes. The [TBS sibling](turn-based-strategy.md) specializes turn budgets and commitment/resolution phases. In a hybrid, specify which layer advances during planning, which resources cross layers and what commitments survive the transition. A multiplayer or controller facet does not automatically require another genre file. [C-01; C-10]

## Custom research instructions

Start with a **timeline of competing demands**, not a target actions-per-minute figure. Record what continues without attention; how a player learns that intervention matters; the last meaningful intervention opportunity; and which decisions become unavailable if attention shifts elsewhere. Distinguish a deliberate plan to neglect one front from a missed cue, inaccessible control, misunderstood state or failed command. Gather actual timing from a specified build only when separately authorized; no timing measurements were made here. [C-05; C-07; C-11]

For economy/unit/territory designs, reconstruct the causal connections rather than assume a compulsory triangle. Does control grant resource access, deny a route, supply information or merely award points? Does production alter future responses at a cost to present action? Does reconnaissance reveal a current fact or support a fallible forecast? Retain exceptions: economic competition without military unit control, real-time tactics without base growth, and cooperative system management. The missing F03/W03 bodies constrain shared integration; this file does not certify their models. [C-02; C-03; C-05]

Compare manual command, command grouping, queued orders, standing policies, slowed simulation and pause as **different interventions**. Ask exactly which player decision each retains or removes. In competitive settings, inspect the agreed rules and information access; in single-player, investigate the player’s preferred pacing and control; in cooperation, investigate who can pause or alter another person’s commitments. Do not infer cheating, fairness or accessibility merely from the presence of automation. [C-04; C-06; C-07]

Seek firsthand failed iterations and demand tradeoffs. Johnson’s account is valuable because it describes deliberately reducing unit-selection work, but it is not independent evidence that all RTS games should remove it. Compare the creator’s goal with actual task demands, rather than treating criticism of a competing design tradition as a universal finding. [C-03; C-06]

## Player promises and varied audiences

Possible promises include adapting a developing plan, maintaining several interacting processes, reading an adversary and choosing where to intervene. For some intended audiences, rapid execution and divided attention may be valued skills; for others, those demands may obstruct the desired planning activity. These are hypotheses for local audience work. The inspected sources do not define a universal RTS player or an acceptable motor/attention threshold. [C-05; C-06]

The right diagnostic is not “can the player keep up?” alone. Ask whether they can express the intended policy, perceive its consequences and make a valued intervention. A player who correctly predicts a threat but cannot select a required actor has a different problem from one who intentionally accepts losses elsewhere to complete a stronger objective. Assistance that makes both outcomes look like success can hide that distinction. [C-05; DEP-F02-D; DEP-F02-H]

## Characteristic loops and structures

A common **conditional** structure is to commit resources to future capacity, observe changing opportunities, and choose between further investment and immediate response. Where territory affects supply, travel or observation, its value depends on those connections rather than on raw area. Where actors specialize, the currently feasible response depends on both their roles and the time to reposition or produce them. These are analytical possibilities, not defining requirements for every RTS. [C-02; C-05]

The 2021 *Age of Empires IV* official article links scouting to resource locations, bottlenecks and opposing production; it also documents advance worker assignments through rally points and grouped production control. That is evidence for documented interactions and assistance in a particular launch-era context, not proof that its advice always wins or a complete current rule table. [C-02; source 003]

An attention cost is strategically meaningful only relative to an intended decision. A deadline may make the choice between two fronts consequential; repeated acknowledgement of an unchanged policy may instead be maintenance. Removing the latter can expose the former, or remove a skill the audience deliberately values. The difference must be investigated rather than decided from a genre label or command count. [C-05; C-06]

### Concurrent decision contract

| Layer to specify | Design question | Failure to distinguish |
|---|---|---|
| World advancement | Which jobs, travel, hazards and opponents keep progressing? | A visual pause is mistaken for suspended consequences. |
| Command eligibility | Can a player redirect, queue, cancel or replace a task, and when? | A displayed destination is mistaken for an accepted instruction. |
| Resolution and cost | When are resources reserved, consumed, refunded or irrevocably revealed? | A canceled movement is assumed to undo information already gained. |
| Information age | Which facts are current, last seen, forecast or unknown? | Old reconnaissance is displayed as present certainty. |
| Attention and feedback | Which changes demand intervention; which can be inspected later? | Every update becomes an urgent interruption, concealing the important exception. |
| Social timing | Who may pause or change pace; what happens during disconnect or absence? | One player’s convenience silently becomes everyone else’s imposed waiting. |

This original design contract transfers reviewed F02/P02/F07 distinctions into concurrent situations; it is not a verified runtime architecture. [C-05; C-07; C-10]

## Applying shared topics

See the [dependency transfer receipt](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer) for exact selected versions and hashes. Only these named passages, not their entire underlying bibliographies, were inspected for G08.

**F02 Decision design and Challenge and difficulty** (`GDR-CAND-20261010-F02-TOP-01/02`) change the diagnosis: missed deadlines, motor access, incomplete information and strategic sacrifice must not collapse into one difficulty score. Do not make an adaptive opponent easier because a player intentionally traded local losses for another goal. No adaptive system is implemented or endorsed here. [C-05; C-11]

**P02 Controls and input, Feedback and game feel, Multimodal communication** (`GDR-CAND-20261010-P02-TOP-01/02/03`) require a distinction among received, queued, accepted, executed, interrupted and canceled commands. The reviewed cue guidance preserves relevant facts and uncertainty across channels; it does not promise identical sensory experience or that more simultaneous output always helps. Keep necessary access supports when testing strategy comprehension. [C-07]

**W02 Quests and objectives** (`GDR-CAND-20261010-W02-TOP-02`) changes how “defend,” “control,” “survive” and “supply” are specified. A briefly occupied point, continuous control and an uninterrupted route are different completion conditions. These are illustrative alternatives, not imported rules of a named game. **F07 evaluation and ethics** (`GDR-CAND-20261010-F07-TOP-01/02`) require separate measurement of execution, comprehension, experience, group burden and viable stopping. [C-10; C-11]

F03 economy and W03 spatial topic bodies are unavailable; their identities and under-review packet status are recorded but no reviewed model is transferred. F04/F05/F06 shared combat/simulation/social/session guidance and G07 boundaries must be reconciled against actual selected artifacts before integrated guidance is accepted. The missing dependencies are not permission to duplicate their general theory in this genre file. [C-10]

## Design choices, pattern selection and adaptations

### Direct control, assistance and player-selected policy

Johnson’s *Offworld Trading Company* retrospective describes automatic shipping with override commands and a move away from unit selection. It explicitly acknowledges losing some route-level pirate avoidance. His desired emphasis on economic adaptation over dexterity is practitioner intent, not a measured universal accessibility result. It supports a design alternative and a concrete cost, not a verdict that direct control is obsolete. [C-03; source 002]

[Bounded standing orders](../patterns/bounded-standing-orders.md), `GDR-CAND-20261010-G08-PAT-02`, is the main candidate pattern here. A player chooses the policy, scope and exceptions; routine execution remains subordinate to that commitment. Use it for genuinely recurring intent, not as a hidden optimizer that knows undiscovered enemy locations or silently chooses strategic targets. [C-06; C-07]

The Zero-K documentation supplies another implementation vocabulary: per-unit states, direct-order interactions and repeated queues. Its retreat documentation also makes a missing retreat zone consequential. Such manuals show that policy controls and exceptions can be specified; they do not establish that a particular set of controls is easy to understand or desirable for every player. [C-08; sources 005–006; pattern source ledger]

[Shared activation budget](../patterns/shared-activation-budget.md), `GDR-CAND-20261010-G08-PAT-01`, is an optional hybrid extension. A replenishing command resource could limit bursts of activity, but that would add a new budget to a concurrent system, not simply slow the game. It can create waiting, stockpiling and dominant burst schedules. No inspected source establishes the comparative efficacy of that RTS adaptation. [C-06]

### Pause and speed

The Feral *Company of Heroes 2* Mac/Steam manual specifically documents pausing to issue orders in **single-player**. That is a narrow counterexample to the claim that RTS cannot support planning pause. It does not establish multiplayer permissions, cross-platform equivalence or measured access benefits. [C-04; source 004]

A proposed comparison should distinguish slower world advancement, pause with command issuance, pause without commands, optional exception-triggered pause and unchanged pacing with better controls. Each changes a different constraint. Slowing simulation need not simplify the number of decisions or make a map readable; pause can preserve a large memory/planning burden. In competitive play, changing clocks, pause rights or automated actions changes the agreed contest and requires explicit mode rules. Cooperative pause also requires clear authority and resumption, not an assumption of unanimous preference. [C-04; C-06; C-10]

## Representative cases, evidence and counterexamples

**Scoped experimental evidence.** Glass, Maddox and Love randomized 72 low-gaming female undergraduates to two modified *StarCraft* training conditions or *The Sims 2*, with 40 hours over seven weeks. They reported aggregate cognitive-flexibility transfer, but the direct comparison between the two RTS conditions did not provide strong evidence of a difference. “SC-2” denotes the study’s condition, **not StarCraft II**. The battery and population do not establish enjoyment, durable benefit for every audience, or a prescribed training dose. [C-09; source 010]

**Illustrative worked example — three ongoing projects.** A real-time harbor scenario has a repair crew, a transport crew and a survey crew. Travel and weather continue while commands are issued. The player intends to prioritize an exposed crossing, but recurrent transport requests draw attention away. First determine whether those transport decisions actually differ. If the desired policy remains “move approved cargo while preserving the emergency reserve,” repeated clicks could be delegated under a visible reserve and stop condition. [C-05; C-06]

The exception matters: after a newly observed route closure, automatic transport must not silently use a dangerous substitute merely because it shortens travel. Present the blocked reason, retain the player’s destination, and require the policy’s authorized alternative or a new decision. Report the current reserve, not a forecast as certainty. This is an illustrative design proposal, not a claimed behavior in a shipped game. [C-07]

**Counterexample.** In a scenario deliberately about hand-routing a vulnerable convoy while anticipating an adversary, automatic route selection could remove the valued decision. Here direct control, clearer group selection or fewer simultaneous actors may fit better than standing orders. Conversely, preserving every repetitive click to maintain a genre’s supposed purity would not justify an access barrier unrelated to the chosen contest. Both cases prevent treating automation or manual control as universally superior. [C-03; C-06]

## Accessibility, ethics, localization and production

Assess input effort, precision, command vocabulary, map interpretation, competing narration and temporal opportunity separately. Remapping can improve access to an action without increasing the time available to choose it. Narrating every event sequentially can fail to deliver a relevant fact before its decision window even when every word exists. Alternative routes need equivalent useful facts and explicit uncertainty, not an identical interface or a hidden advantage. These are conditional analysis points, not measured G08 outcomes. [C-07; DEP-P02-C; DEP-P02-M]

Preserve P01’s scope correction: no universal target size, label height, contrast number or reaction threshold is prescribed. Localize state distinctions and cancellations, not only unit names. Test a long translated exception message without making it an uninterruptible bottleneck; keep a persistent route to inspect details after an alert. Consider simultaneous hearing, vision or motor constraints as actual participant requirements, not a checklist satisfied by adding one mode. [C-07]

Production planning should budget for action arbitration, selection scope, stale queues, changing ownership, pause/resume, replayable explanations and interrupted saves. This is a state-case inventory, not an engine design, network protocol recommendation or measured cost estimate. Automation can move work from repetitive player action to interface and QA complexity. Multiplayer pause, delegation and role permissions also create moderation and social questions whose F06 dependency remains unverified here. [C-10]

## Research questions and validation

**Proposed, not performed.** Compare manual commands against the same scenario with bounded standing orders, first at a fixed simulation pace. A separate pace comparison can then examine whether any effect came from extra decision time rather than policy delegation. Keep known information, resources and opponent behavior matched where feasible; record unavoidable interaction changes. Counterbalance scenarios and account for prior command-interface familiarity. Do not withdraw assistive inputs or ordinary feedback to manufacture a control condition. [C-11]

Include participants relevant to the planned mode, with a range of RTS familiarity and actual access requirements. Record expressed policy, completed/blocked actions, unwanted automatic acts, missed exceptions, reversal attempts, time spent configuring, and whether the person still owns the intended strategic decisions. Interview perceived control and burden separately from wins, action counts or idle time. No universal APM cutoff, participant count or timing window follows from the sources. [C-05; C-07; C-11]

Reject or narrow standing orders when they repeatedly substitute an unintended priority, leak protected information, conceal failure or remove valued manual tactics. If strategic choices improve only because the tool supplies an answer, it is not evidence that reducing repetitive execution preserved the original decision. If pace helps but policy assistance does not, prefer the simpler pace intervention when appropriate to the mode. Same-rule transfer and changed-rule adaptation must be reported separately; a correct refusal is not a learning failure. [C-06; C-11]

### Coverage checkpoint

Researched: timing layers; attention versus choice; conditional economy/unit/territory interactions; reconnaissance; documented grouping/policy/pause alternatives; one limited training study; access and production tradeoffs. Open: actual command latency, current game builds, controller/touch comparisons, competitive policy parity, long-session fatigue, group-pause consent, network/disconnect handling, and missing shared bodies. The next discriminating question is **which specific repeated activity can be delegated without deciding the strategic commitment it was meant to express?**

## Claim ledger

Local C-identities belong only to this file. Confidence concerns the precisely scoped claim, not the whole genre. A source’s description of a mechanic does not establish its benefit. `DEP` references mean inspected reviewed-candidate passages, not newly inspected underlying studies; see the [dependency receipt](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer).

### C-01

**Claim:** RTS is treated as strategic commitment under relevant concurrent world progression, not as a universal APM, construction or no-pause requirement.

**Class:** `inference`. **Support and precise locator:** Working definition; sources 002 shipping/scanning account and 004 General controls supply contrasting documented structures. **Confidence:** moderate for analytical usefulness, not an official genre standard. **Applicability, contrary case and unresolved issue:** Real-time tactics and hybrid boundaries remain contested; mode-specific pause does not settle every genre label.

### C-02

**Claim:** The inspected 2021 Age of Empires IV article connects scouting, resources, opposing production and assisted commands in its launch-era advice.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-003, Scout!, Rally Point Resources, Group Assignments and When to Age Up. **Confidence:** high for documentary content; no runtime observation. **Applicability, contrary case and unresolved issue:** Not a current complete counter matrix or universal RTS economy structure; no causal success claim.

### C-03

**Claim:** Johnson describes removing unit-selection work to emphasize economic decisions and explicitly identifies a lost route-level control opportunity.

**Class:** `practitioner-heuristic`. **Support and precise locator:** GDR-SRC-20261010-G08-002, automatic shipping/overrides and pirates paragraphs. **Confidence:** high for the reported rationale; low for generalized benefits. **Applicability, contrary case and unresolved issue:** Same creator as Old World account, no independent measurement; manual routing can be a valued goal.

### C-04

**Claim:** The inspected Company of Heroes 2 manual scopes pause-and-issue-orders to single-player on its Mac/Steam documentation route.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-004, General controls, manual page 5. **Confidence:** high for the narrow document statement. **Applicability, contrary case and unresolved issue:** No current executable, multiplayer-pause right, other platform behavior or efficacy verified.

### C-05

**Claim:** Classifying concurrent failures by information, opportunity, control and intended sacrifice is more informative than treating every loss or missed action as poor strategy.

**Class:** `inference`. **Support and precise locator:** DEP-F02-D lines 53–103; DEP-F02-H lines 53–110; G08 concurrent decision contract. **Confidence:** moderate; follows distinct causal possibilities. **Applicability, contrary case and unresolved issue:** A diagnosis requires evidence from the actual player/task. The taxonomy of possible causes does not identify any case automatically.

### C-06

**Claim:** Bounded delegation or changed pace may expose valued planning, but may also remove valued execution, add configuration burden or alter the agreed contest.

**Class:** `hypothesis`. **Support and precise locator:** Source 002 tradeoff account; source 004 documented alternative; PAT-02 causal ledger; PAT-01 real-time adaptation explicitly original. **Confidence:** low for comparative benefit; plausible mechanism and countercase, no local test. **Applicability, contrary case and unresolved issue:** Do not classify assistance by purity or promise accessibility. Reject when it chooses priorities, masks failures or undermines the intended challenge.

### C-07

**Claim:** Command receipt, queued intent, accepted action and executed result require distinct information contracts, including uncertainty-preserving alternative channels.

**Class:** `inference`. **Support and precise locator:** DEP-P02-C lines 83–145; DEP-P02-F lines 104–123; DEP-P02-M lines 58–108; DEP-P01-A lines 89–110. **Confidence:** moderate for state distinction; actual comprehension and access untested. **Applicability, contrary case and unresolved issue:** No universal native-game numeric threshold; no hidden-information leakage, false success feedback or removal of needed supports.

### C-08

**Claim:** Zero-K documentation specifies configurable unit states and a retreat behavior dependent on a retreat zone.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-005, opening/Fire State/Move State/Repeat; source 006 used in linked PAT-02, Retreat no-zone paragraph. **Confidence:** high for the inspected documentation, not current runtime. **Applicability, contrary case and unresolved issue:** Same project’s pages are not independent evidence of usability. Build/revision unresolved; no reproduced bug or benefit.

### C-09

**Claim:** The inspected randomized RTS training study supports a scoped aggregate transfer result, not a demonstrated difference between its RTS variants or a genre-wide benefit.

**Class:** `empirical-evidence`. **Support and precise locator:** GDR-SRC-20261010-G08-010, Methods training/sample; Results aggregate flexibility and direct condition comparison. **Confidence:** moderate for the published scoped finding; no reanalysis. **Applicability, contrary case and unresolved issue:** Modified tasks, selected sample and battery constrain transfer. Neither significance versus control nor a condition name establishes a between-RTS effect or StarCraft II use.

### C-10

**Claim:** RTS integration must account for supported objectives, shared pause/delegation authority, persistent state cases and missing shared economy/spatial/social bodies.

**Class:** `inference`. **Support and precise locator:** DEP-W02-Q lines 53–108; DEP-F07-E lines 57–77, 92–104; G08 dispatch dependency receipt. **Confidence:** moderate for risk and ownership analysis. **Applicability, contrary case and unresolved issue:** No current implementation, network design or independent review of unavailable F03/W03/F04/F05/F06/G07 bodies.

### C-11

**Claim:** A future evaluation should isolate policy assistance from pace, preserve access supports and compare intended choices with execution and experience.

**Class:** `hypothesis`. **Support and precise locator:** DEP-F07-V lines 57–98; DEP-F01-T lines 98–116; DEP-W02-M line 148; proposed G08 study. **Confidence:** low for comparative design effects; high for stating that no study occurred. **Applicability, contrary case and unresolved issue:** Sampling/margins await a local question; wins or action counts alone cannot establish preserved agency. No tests performed.

## References

Source IDs are temporary run-scoped identities, reused throughout G08. Access means the named passages were inspected, not that a game was run. Cross-batch URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G08-002

Soren Johnson. **[OTC Designer Notes #1: Unit Selection](https://www.designer-notes.com/otc-designer-notes-1-unit-selection/)**. Designer Notes. Publication/update: 2016-04-15. Edition/build: Prelaunch Offworld Trading Company design account. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Main article, paragraphs on automatic shipping, override commands, engineers and scout/scan redesign. **Type:** Firsthand developer account. **Limits/independence:** Intent and production tradeoffs, not independent usability measurements. Same author as source 001; broader rhetoric is not adopted. **Rights:** Copyright holder retains rights; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-003

AoE Official. **[Age of Empires IV: Tips to Help Get Your Army Up to Speed](https://www.ageofempires.com/news/age-of-empires-iv-tips-to-help-you-get-started/)**. Age of Empires / World’s Edge. Publication/update: 2021-11-03. Edition/build: Launch-era PC advice; no current patch or game execution verified. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Rally Point Resources; When to Age Up; Scout!; The Power of Counters; Group Assignments. **Type:** Official gameplay documentation and practitioner advice. **Limits/independence:** Documented options and advice, not causal effectiveness or a complete counter table. Independent production context from sources 001–002. **Rights:** Microsoft rights retained; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-004

Feral Interactive. **[Company of Heroes 2 — manual](https://www.feralinteractive.com/en/manuals/companyofheroes2/latest/steam/)**. Feral Interactive. Publication/update: unknown. Edition/build: Mutable Mac/Steam HTML manual at latest route; build number unknown. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** General controls, manual page 5: Pause and issue orders, single-player games only. **Type:** Official platform-specific manual. **Limits/independence:** Narrow documented mode/platform behavior; no hands-on validation, current all-platform claim or multiplayer-pause inference. **Rights:** Rights retained by respective owners; no manual reproduced. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-005

Zero-K project documentation contributors; individual authors unknown. **[Unit states](https://zero-k.info/mediawiki/Unit_states)**. Zero-K project wiki. Publication/update: unknown. Edition/build: Mutable documentation snapshot; page revision/build not established. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Opening state/inheritance notes; Fire State; Move State; Repeat. **Type:** Project-hosted rule/interface documentation. **Limits/independence:** Describes configurable behavior, not verified runtime, performance or universal access outcomes. Same documentation ecosystem as source 006. **Rights:** Specific page reuse license not established; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-010

Brian D. Glass; W. Todd Maddox; Bradley C. Love. **[Real-Time Strategy Game Training: Emergence of a Cognitive Flexibility Trait](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0070350)**. PLOS ONE 8(8), e70350. Publication/update: 2013-08-07. Edition/build: Published article, DOI 10.1371/journal.pone.0070350. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Materials and Methods: participants/training; Results: composite flexibility and direct SC-1/SC-2 comparison; Discussion. **Type:** Original randomized training study. **Limits/independence:** Selected undergraduate sample, modified tasks and aggregate transfer battery; no genre-wide benefit or engagement test. Supplements/raw data not reanalyzed. **Rights:** CC BY; paraphrased with attribution. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-006

Zero-K project documentation contributors; individual authors unknown. **[Retreat](https://zero-k.info/mediawiki/Retreat)**. Zero-K project wiki. Publication/update: unknown. Edition/build: Mutable documentation snapshot; page revision/build not established. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Retreat-zone placement, no-zone condition, repair/resume behavior, manual cancellation. **Type:** Project-hosted rule/interface documentation. **Limits/independence:** A documented exception and recovery sequence, not a reproduced bug or independent study. Related to source 005. **Rights:** Specific page reuse license not established; paraphrase only. Claims using this source are identified in this entry’s ledger.

## Review and history

2026-10-10 — first genre draft in G08, `initial-draft-1`, attempt `G08-authoring-01`. Candidate ID persists through corrections. Predecessor and supersession are null; exact delivered hashes are recorded outside this file to avoid self-reference. No canonical receipt, Library upload or independent G08 approval is claimed.

Evidence and heading coverage remain open. The [review packet](../reviews/full-run-20261010-g08-review-packet.md) records contradictions, missing bodies, complete inventory, proposed index rows and queued child work. Additional research must retain existing identities; child keys require Library Coordination registration before submission. The next decision is independent content review of these conditional recommendations and boundaries, not implementation or release.
