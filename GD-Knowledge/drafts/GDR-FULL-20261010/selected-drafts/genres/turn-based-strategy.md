---
id: GDR-CAND-20261010-G08-GEN-03
kind: genre
title: Turn-based strategy
version: 0.1.0
status: draft
candidate_revision: independent-review-correction-1
attempt_id: G08-authoring-01
run_id: GDR-FULL-20261010
batch_id: G08
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles
coverage_state: open
aliases:
- TBS
- turn budgets
- simultaneous-turn strategy
tags:
- turn-structure
- initiative
- deliberation
- downtime
- hidden-information
- action-budget
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-W02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G08-PAT-01
- GDR-CAND-20261010-G08-PAT-02
related_genres:
- GDR-CAND-20261010-G08-GEN-01
- GDR-CAND-20261010-G08-GEN-02
source_ids:
- GDR-SRC-20261010-G08-001
- GDR-SRC-20261010-G08-007
- GDR-SRC-20261010-G08-009
- GDR-SRC-20261010-G08-011
- GDR-SRC-20261010-G08-012
reviewer: null
approved_by: null
approved_date: null
independent_review: separate-assistant-review-completed; acceptance-pending
predecessor_sha256: 34143a00b5139987561a7722fa844b0b345ba45d2bd5cf103e66e15094f8d5af
supersedes: initial-draft-1
change_summary: Correct source 007 mutable-page provenance; legacy beta URL does not establish a beta-era snapshot.
hash_record: ../reviews/G08-CORRECTION-RECEIPT.md
---

> **Draft research, not released guidance.** Version 0.1.0; candidate revision `independent-review-correction-1`. A separate assistant content review has occurred; gameplay testing and human acceptance have not occurred. Recommendations labeled `hypothesis` are proposed for evaluation, not established effects. All examples labeled *illustrative* are invented and untested. Dates use America/Los_Angeles; the run ID is unchanged.

# Turn-based strategy

## Definition and boundaries

**Working usage:** Turn-based strategy (TBS) organizes consequential decisions through discrete permissions, commitments or resolution phases. A turn can belong to a player, actor or group; participants may plan sequentially or concurrently. A pause between decisions does not guarantee unlimited thinking time, perfect information, an accessible interface or a thoughtful experience. These are separate design variables. [C-01]

Distinguish **permission to act**, **the budget of actions**, **commitment of a plan**, **resolution of interacting actions**, and **the external thinking clock**. “Simultaneous turns” can mean simultaneous planning, simultaneous commitment or jointly resolved consequences; those are not interchangeable. In this file, *sequential* means one participant’s relevant commitment/resolution precedes the next; *simultaneous planning* means planning opportunities overlap; *WEGO* denotes a plan-then-resolve arrangement, with exact conflict rules still requiring inspection. These are operational distinctions, not universal terminology. [C-01; C-03]

The [Strategy parent](strategy.md) owns the broad planning and goal-conflict questions. This file specializes discrete opportunity budgets, initiative, information revealed between turns, delayed consequences and waiting. The [RTS sibling](real-time-strategy.md) specializes decisions under continuing simulation. A campaign can use turns while encounters run continuously; a paused real-time game does not necessarily adopt turn budgets. Tactics, tactical RPG and 4X remain separate roster entries, not alternate names for this file. G07’s selected boundaries are not available for transfer. [C-01; C-10]

## Custom research instructions

Reconstruct the exact **turn contract** for each source: who may decide; what can be reconsidered; what consumes an action; whether unused capacity expires or carries; what other players can observe before committing; how conflicts and ties resolve; and what happens when a participant is absent. Record both the rule and the information available to understand it. Never infer these from “turn-based” on a store page. [C-01; C-05]

Compare at least four genuinely different structures when relevant: a single move alternating between opponents; a player turn that activates several actors; a shared activity pool competing across actors; and simultaneous plans with later resolution. A cooperative phase may add joint negotiation and independent sub-decisions. Do not treat changing turn order as a cosmetic variant: it can change who learns what before committing. [C-02; C-03; C-05]

Seek measured evidence for claims about thinking time, exhaustion, access or analysis paralysis. Do not call a long turn pathological just because it lasts longer than the designer expected. Operationalize the concern as a participant’s unwanted inability to conclude, repeated unproductive reconsideration, disproportionate burden, or another specified outcome. Test those separately from careful planning, reading an unfamiliar language, using assistive input or enjoying a difficult position. No universal turn-duration cutoff is supported here. [C-06; C-07; C-11]

Investigate contrary cases: clocked abstract play; cooperative simultaneous planning with conflicts; deliberately hidden plans; a simple action budget with rich consequences; and a sprawling turn that adds upkeep rather than valued deliberation. Use developer sources for intent, actual rule artifacts for permissions, and relevant participants for claimed experience. A tactical publisher label and a “simple UI” marketing claim are not an accessibility study. [C-02; C-03; C-09]

## Player promises and varied audiences

Possible promises include time to inspect a position, ability to compare plans before committing, anticipation of another participant’s response, or a legible account of a joint resolution. These are conditional design goals to validate, not empirical expectations of all TBS players. Some groups value brisk commitment and uncertainty; others value extended discussion or solitary reflection. A slower schedule can permit thought while still imposing memory, reading, social or sustained-attention demands. [C-06; C-07]

Deliberation should not become a moral ranking. A fast correct choice can reflect familiarity; a long choice can reflect interest, ambiguity, difficulty or an inaccessible representation. Likewise, a legal move that avoids the engine’s preferred line may express a different legitimate objective in an open-ended game. “Thoughtful” must be translated into the actual intended experience before selecting a measure. [C-06; C-09]

## Characteristic loops and structures

A proposed analytical loop is inspect the available state → allocate current opportunities → commit → resolve intervening actions → interpret changes → revise the plan. The important TBS distinction is where information or feasibility changes between those stages. Some structures allow continuous replanning within a turn; others lock an entire plan. Neither is categorically deeper or fairer. [C-01; C-05]

The 2023 FIDE rules reproduction provides a clear historical distinction between alternating moves and clock handling. Slitherine’s *Frozen Synapse* description instead separates planning/testing orders from simultaneous execution. These are documented temporal arrangements, not two equivalent experiments in strategic quality. [C-02; C-03; sources 009, 012]

### Action budgets, initiative and delayed consequences

| Choice to specify | Potential purpose | Cost, alternative or contrary case |
|---|---|---|
| Independent allowance for each actor | Ensure every actor has a recurring opportunity. | Larger rosters can increase routine activation. A shared budget changes the decision, rather than merely shortening the turn. |
| Shared activation pool | Make choosing which projects/actors act compete directly. | More orderings and combinations can increase planning burden; one compulsory job or dominant actor can crowd out everything else. |
| Alternating individual activations | Let participants respond between commitments. | Adds frequent interaction and may fragment coherent multi-actor plans. |
| Whole-side sequential turns | Support planning several related actions together. | The inactive side may wait; first-mover and information effects require explicit analysis. |
| Simultaneous hidden plans | Preserve uncertainty at commitment and overlapping planning opportunities. | Conflicts, ties, invalidated targets and information leaks need rules; visible animations do not explain resolution by themselves. |
| Cooperative planning phase | Allow participants to coordinate shared outcomes. | A more experienced person may take over; private planning, role authority and consent are alternatives to unlimited open discussion. |
| External clock or deadline | Bound a session or create a chosen timing challenge. | Changes the demand profile; can disadvantage reading, access or decision styles without addressing the actual source of delay. |

All comparative benefits in this table are hypotheses or design possibilities. No universal initiative advantage, turn length, actor count, order budget or fairness formula is inferred. [C-05; C-06; C-07; C-08]

A delayed consequence is useful to planning only when the player can form a relevant model of it or deliberately accept that uncertainty. State whether a displayed cost is paid now, reserved until resolution or conditional on success. Define whether a failed action refunds its cost and whether its failure reveals new information. This is especially important when players can revise orders after discovering another action’s result. An undo that restores resources may still retain informational advantage. [C-05; C-08; DEP-F02-D]

## Applying shared topics

Exact inspected dependencies are documented in the [reviewed dependency transfer](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer). They remain parent-selected reviewed drafts, not released research.

**F02 Decision design** (`GDR-CAND-20261010-F02-TOP-01`) specializes here into commitment/knowledge boundaries: an unused action, a refundable resource and an unrevealed plan are not interchangeable forms of reversibility. **F02 Challenge and difficulty** (`GDR-CAND-20261010-F02-TOP-02`) prevents treating the removal of a reflex deadline as removal of reading, memory, planning or social demands. [C-05; C-07]

**W02 Quests and objectives** (`GDR-CAND-20261010-W02-TOP-02`) specializes into clear phase-end and scenario-end predicates. An objective might require a condition at turn end, continuously across a round, or at a particular event; the wording and resolution must agree. The reviewed `multi-route-objective-contract` (`GDR-CAND-20261010-W02-PAT-02`) also distinguishes method-essential objectives from flexible outcomes. [C-05; C-10]

**P02 Controls, Feedback and Multimodal communication** (`GDR-CAND-20261010-P02-TOP-01/02/03`) specialize into inspection without accidental commitment, reversible drafting where permitted, explicit ready/committed/resolved states, and an accessible account of what changed. Alternative channels must not disclose a hidden rival order simply because the visual route does not. **F07 evaluation and ethics** (`GDR-CAND-20261010-F07-TOP-01/02`) keep burden, contribution, stopping and outcomes separate. [C-07; C-08; C-11]

F03 economy and W03 spatial topic identities are known but bodies were not retrieved. Current simulation, multiplayer/session and G07 tactics integration also remains unverified. Turn-state analysis below is an explicitly local hypothesis, not substitute approved shared guidance. [C-10]

## Pattern selection and adaptations

### Shared activity versus moving everyone

Johnson’s *Old World* account describes a common Orders resource competing across activities and recounts fatigue/Force March decisions after unrestricted movement proved undesirable to the team. The useful evidence is the intended cross-actor allocation and the reported need for limits, not the stronger rhetoric that other turn structures provide only illusory choice. No controlled player comparison is supplied. [C-04; source 001]

[Shared activation budget](../patterns/shared-activation-budget.md), `GDR-CAND-20261010-G08-PAT-01`, extracts a conditional recipe. Define eligible actions, available/reserved/spent budget, per-actor restrictions and refresh rules before choosing values. Couple it with the already existing F02 visible-opportunity-cost pattern only where an actual feasible alternative is lost. Avoid a common pool when its main effect is preventing teammates from contributing or forcing continuous compulsory upkeep. [C-05; C-06]

[Bounded standing orders](../patterns/bounded-standing-orders.md), `GDR-CAND-20261010-G08-PAT-02`, may help with repeated city or actor intentions, but each new turn can change the policy’s assumptions. A standing action should not consume the fresh pool ahead of newly chosen priorities unless the player knowingly authorized that ordering. The interaction between automatic orders, scarce activations and newly revealed information is an original hypothesis requiring evaluation. [C-05; C-08]

### Simultaneous does not mean conflict-free

Handelabra’s mutable *Spirit Island* multiplayer page, served at a legacy beta URL, describes simultaneous planning/power activity while serializing actions that affect the same land or spirit; it also limits undo after new information. This is a concrete warning against equating overlapping input with conflict-free resolution. It is not a current tabletop rule audit or evidence that concurrency eliminates downtime. [C-08; source 007]

In a proposed cooperative design, distinguish **ownership of a choice** from **permission to execute a shared effect**. Showing every player’s options to the whole group can aid coordination but can also allow one person to decide for everyone. A private draft followed by a consent-based shared commitment may preserve contribution, but could make interaction slower or reduce desired conversation. No group-process intervention was tested here; retain these as alternatives, not proven fixes. [C-06; C-08]

## Thinking time, burden and contrary empirical evidence

Sunde, Zegners and Strittmatter analyze over 215,000 moves from roughly 3,600 professional chess games, excluding opening moves and comparing play with an engine benchmark. Longer **spent decision time** is negatively associated with measured quality under their controls, while more **remaining time** is positively associated conditional on decision time. The timing is not randomized; harder subjective decisions and endogenous stopping remain explanations. These selected professional data do not show that forcing faster moves improves decisions, or that long turns harm enjoyment. [C-09; source 011]

The implication for this draft is methodological, not a speed prescription: measure available time, time actually used, the decision’s difficulty and the desired outcome separately. A time limit may suppress repeated searching, but it may instead terminate a productive line of thought or an assistive-input process. More available time may support deliberation without obliging everyone to use it. No result here establishes an optimum timer or a universal “analysis paralysis” mechanism. [C-06; C-07; C-09]

## Worked example and strongest counterexample

**Illustrative — a ferry-and-depot planning round.** A council has five action tokens this round. A ferry transfer costs two, repairing a crossing costs three, and surveying a route costs one. These are invented local settings for explanation, not recommended balance values. With no reservations, transfer plus repair exactly uses the pool. Adding survey makes that combination infeasible. A player choosing survey and repair may understand the transfer’s value and still prioritize knowledge and access. That preference is not a rule error. [C-05; C-11]

Specify resolution before asking for a plan. In a sequential version, the survey can reveal information before later actions are chosen. In a simultaneous-commitment version, the council must decide whether it is committing conditional orders, whether survey results can revise the draft, and what happens if a target becomes unavailable. The same numerical pool does not create the same decision in both versions. [C-01; C-05; C-08]

For a cooperative version, one participant owns the ferry’s destination and another the repair priority. Shared tokens do not automatically create shared authority. A team could explicitly agree on reservations and keep a ready-state confirmation, or use separate guaranteed allowances. Neither arrangement is declared superior until contribution and burden are evaluated. [C-06; C-08]

**Counterexample.** If every actor has an urgent mandatory repair each round, a shared pool smaller than total compulsory cost may produce an arbitrary rotating failure rather than valued prioritization. Conversely, independent allowances may be desirable when the promise is to exercise every role. A very small budget can still induce exhaustive search over many sequences, so fewer activations do not logically guarantee shorter or easier turns. [C-05; C-06]

## Accessibility, localization and production implications

A stopped simulation can make an inspection opportunity possible while leaving its content inaccessible. Review keyboard/controller/switch navigation, focus order, narration of legal targets, comparison of multiple plans, and the ability to correct an uncommitted selection. Retain the actual information policy: narration of “no target” must not reveal an undiscovered unit that the visual route cannot detect. No P01 numerical example is adopted as a native-game default. [C-07]

A phase change may invalidate a screen, caption, narrated summary or drafted action. Offer a clear distinction among “proposed,” “ready,” “committed,” “resolved” and “blocked” where those states exist. Translate conditional and temporal wording explicitly; “until your next turn” and “until the round ends” are not the same contract. These are design-analysis requirements, not measured localization effects. [C-05; C-07]

Allowing interruption raises decisions about saving uncommitted plans, replaying already observed consequences, asynchronous reminders and authority after a participant leaves. Adding a mandatory task during another player’s turn can reduce apparent idle time while increasing obligation or stealing attention from the shared event. Doing nothing while observing, reflecting or resting can be acceptable; the goal is not to eliminate every inactive second. These are proposed ethical/session distinctions awaiting the shared dependency and participant evidence. [C-06; C-10]

Production must cover joint commitments, conflict resolution, deterministic explanations where applicable, stale conditional orders and state migration through saves. A logical plan validator is not proof of an understandable resolution. No engine code, network simulation, replay harness or participant test was executed. [C-10; C-11]

## Research questions and validation

**Proposed, not performed.** Compare an independent-allowance version with a common-pool version of the same small scenario. Separately compare generous optional thinking time with a locally justified clock; do not change both allocation and timing and attribute the outcome to turns alone. Include solitary and cooperative conditions only when each matches the intended use; group interaction is a confound, not free extra evidence. [C-11]

Measure legal-action understanding, actual foregone alternatives, plan revisions after new information, unwanted waiting, voluntarily used time, reported exhaustion and participant contribution. Preserve input/access supports and offer an alternative response to verbal explanation when language would confound understanding. Record what the player intended, not just the engine-evaluated outcome. Recruit relevant skill, access and language profiles; specify sampling and practical margins before testing. [C-07; C-11]

Use affordable, unaffordable and exact-budget cases with varied correct answers; keep ability to execute a legal action separate from desire to do it. Transfer probes change surface details while preserving the rule; changed refill or reservation rules are separately labeled adaptation/discrimination. Confounds include memorized openings, coaching, prior interface familiarity, turn-order advantage and asymmetric roles. [C-11]

Reject or narrow the pooled budget when reduced activations create more unwanted search without more valued choice, when compulsory costs dominate, or when participation becomes routinely concentrated in one person. Reject a timer as the remedy when it mainly interrupts access or productive thought without addressing the measured burden. A longer or shorter average turn alone cannot pass the proposal. [C-06; C-07; C-11]

### Coverage checkpoint

Researched: turn/clock distinctions; action pools; initiative and information; sequential/simultaneous examples; undo/knowledge boundaries; delayed consequences; deliberation versus time pressure; access, contribution and production risks. Open: initiative balance by actual rule set, representative fatigue/analysis-paralysis evidence, asynchronous return, current cooperative builds, comparative controller/nonvisual access, the core *Spirit Island* tabletop rules PDF and shared social/session/spatial/economy integration. The next discriminating question is **whether a turn contract preserves a valued opportunity to think and contribute, rather than merely increasing the time or work before commitment**.

## Claim ledger

Local C-identities belong only to this file. Confidence concerns the precisely scoped claim, not the whole genre. A source’s description of a mechanic does not establish its benefit. `DEP` references mean inspected reviewed-candidate passages, not newly inspected underlying studies; see the [dependency receipt](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer).

### C-01

**Claim:** Turn permission, action allowance, commitment, resolution and external thinking clocks are analytically distinct, including in simultaneous-turn structures.

**Class:** `inference`. **Support and precise locator:** GDR-SRC-20261010-G08-009 opening/Game Specs; 012 Articles 1/6; original G08 turn contract. **Confidence:** moderate-high for the distinction; terminology remains operational. **Applicability, contrary case and unresolved issue:** Not a formal universal genre definition; a stopped simulation and a turn budget are not identical.

### C-02

**Claim:** The historical 2023 over-the-board chess rules specify alternating moves and clock handling as separate rules.

**Class:** `formal-standard`. **Support and precise locator:** GDR-SRC-20261010-G08-012, Introduction 0.1, Articles 1.2–1.3 and 6.1–6.2.1. **Confidence:** moderate-high for reproduced normative wording; original FIDE bytes unavailable. **Applicability, contrary case and unresolved issue:** OTB chess only; no claim of latest regulation, general accessibility or a prescribed digital-game timer.

### C-03

**Claim:** Frozen Synapse is documented as allowing planning/testing before simultaneous execution, with Tactical/Turn-Based WEGO catalog labels.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-009, opening and Game Specs. **Confidence:** high for the publisher document, not observed play. **Applicability, contrary case and unresolved issue:** Marketing claims of superior tactics always winning and intuitive UI are not adopted; service/build freshness unknown.

### C-04

**Claim:** Johnson describes common Orders allocation and iterative limits on repeated unit movement in Old World.

**Class:** `practitioner-heuristic`. **Support and precise locator:** GDR-SRC-20261010-G08-001, main Orders/fatigue/Force March paragraphs. **Confidence:** high for the account; low for comparative player benefits. **Applicability, contrary case and unresolved issue:** Internal judgments lack disclosed comparative measurements; independent actor allowances are not proven illusory.

### C-05

**Claim:** A turn budget must state eligibility, reservation, spending, refresh, information release and conflict rules because these determine feasible commitments.

**Class:** `inference`. **Support and precise locator:** Source 001 mechanism account; DEP-F02-D lines 53–103; G08 illustrative ferry arithmetic and turn contract. **Confidence:** high for explicitly conditional budget logic; interface effectiveness untested. **Applicability, contrary case and unresolved issue:** Pooled activity can add sequence combinations or mandatory scarcity; fewer actions do not guarantee less thinking burden.

### C-06

**Claim:** Additional thinking opportunity or shared allocation may aid a chosen deliberative goal but can also create unwanted search, waiting or unequal contribution.

**Class:** `hypothesis`. **Support and precise locator:** G08 proposed audience/application alternatives; 001 is rationale only; DEP-F07-V/E. **Confidence:** low for comparative benefit; no representative TBS burden study inspected. **Applicability, contrary case and unresolved issue:** Long turns can be valued, access-related or difficult; no universal pathology threshold or timer recommendation.

### C-07

**Claim:** Turns do not automatically remove sensory, motor, reading, memory, social or sustained-attention barriers.

**Class:** `inference`. **Support and precise locator:** DEP-F02-H lines 53–110; DEP-P02-C/M; DEP-P01-A lines 89–110; source 012 Appendix D for a scoped rule example. **Confidence:** high for the logical non-equivalence, not a quantified access effect. **Applicability, contrary case and unresolved issue:** Necessary supports remain; an alternate interface must preserve permitted facts/uncertainty, not leak answers.

### C-08

**Claim:** The inspected Spirit Island digital multiplayer description combines concurrent activity with conflict locking and an undo boundary at new information.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-007, multiplayer gameplay notes. **Confidence:** high for documented feature statements; page says multiplayer is fully launched, but current build behavior is unverified. **Applicability, contrary case and unresolved issue:** Not a tabletop rule claim or proof of eliminated waiting; cooperative authority and budget interactions are original hypotheses.

### C-09

**Claim:** Professional chess observations distinguish remaining time from time spent deciding; their associations do not show that forced haste improves quality.

**Class:** `empirical-evidence`. **Support and precise locator:** GDR-SRC-20261010-G08-011, Basic Results/Table 1, Discussion, Materials and Methods: Data and Measurement. **Confidence:** moderate for the scoped published observational result. **Applicability, contrary case and unresolved issue:** Selected professional games; Stockfish 17 depth-22 benchmark; endogenous timing and subjective difficulty; no causal timer or enjoyment conclusion, raw data not reanalyzed.

### C-10

**Claim:** Turn-state, save/re-entry, supported-objective and social-authority decisions require integration with actual shared guidance, not inferred approval from missing bodies.

**Class:** `inference`. **Support and precise locator:** DEP-W02-Q lines 53–108; DEP-F07-E lines 57–77, 92–104; G08 dependency receipt. **Confidence:** moderate as scope/risk analysis. **Applicability, contrary case and unresolved issue:** F03/W03 bodies and applicable F04/F05/F06/G07 review content remain unverified; no implementation prescription.

### C-11

**Claim:** A useful proposed comparison distinguishes budget structure from time limits and understanding from preference, while preserving same-rule transfer versus changed-rule adaptation.

**Class:** `hypothesis`. **Support and precise locator:** DEP-F07-V lines 57–98; DEP-F01-T lines 98–116; DEP-W02-M line 148; original G08 study design. **Confidence:** low for intervention effects; no study performed. **Applicability, contrary case and unresolved issue:** No sample-size or turn-duration guarantee. Burden, contribution, comprehension and access must not be reduced to one completion statistic.

## References

Source IDs are temporary run-scoped identities, reused throughout G08. Access means the named passages were inspected, not that a game was run. Cross-batch URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G08-001

Soren Johnson. **[Old World Designer Notes #1: Orders](https://www.designer-notes.com/old-world-designer-notes-1-orders/)**. Designer Notes. Publication/update: 2021-07-26. Edition/build: Historical design retrospective; no executable build inspected. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Main article, paragraphs on shared Orders, rejected prototypes, fatigue and Force March; author comment on unit caps. **Type:** Firsthand developer account. **Limits/independence:** Designer rationale and internal iteration, not a measured player-benefit study. Same author as source 002. **Rights:** Copyright holder retains rights; paraphrased, no source payload redistributed. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-007

Handelabra Games. **[Spirit Island Multiplayer](https://www.handelabra.com/spirit-island-beta)**. Handelabra Games. Publication/update: unknown. Edition/build: Mutable multiplayer feature page at a legacy beta URL; inspected page says multiplayer is fully launched. Exact build, original publication date and update date unknown. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Multiplayer gameplay notes: Spirit Phase undo, simultaneous phases, shared land/spirit locking and group decisions. **Type:** First-party digital-adaptation description. **Limits/independence:** Mutable digital feature documentation, not an authenticated beta-era snapshot, current retail audit or tabletop rulebook. Same game property as source 013, different implementation context. **Rights:** Rights retained; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-009

Slitherine; developer identified as Mode 7 Games. **[Frozen Synapse](https://www6.slitherine.com/game/frozen-synapse)**. Slitherine. Publication/update: unknown; catalog identifies original release 2011-05-25. Edition/build: Historical PC catalog; installer listing v1.00 is metadata, not an inspected executable. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Opening description; Game Specs: Tactical / Turn-Based WEGO; Info paragraph on plan/test/execute. **Type:** Publisher-provided game description. **Limits/independence:** Documented temporal structure, not proof that tactics always wins, intuitive access, current services or actual play results. **Rights:** Slitherine/Mode 7 rights retained; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-011

Uwe Sunde; Dainis Zegners; Anthony Strittmatter. **[Speed and quality of complex strategic decisions](https://pmc.ncbi.nlm.nih.gov/articles/PMC13187726/)**. PNAS 123(20), e2531472123; PMC full-text route. Publication/update: 2026-05-13; issue date 2026-05-19. Edition/build: Published article, DOI 10.1073/pnas.2531472123. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Basic Results/Table 1; Discussion on endogenous decision time; Materials and Methods: Data and Measurement. **Type:** Original observational professional-chess analysis. **Limits/independence:** Nonrandom decision times and selected professionals; engine-based outcome, not enjoyment. Supersedes the 2022 working paper, not a separate replication; no raw-data reanalysis. **Rights:** CC BY 4.0; paraphrased with attribution. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-012

FIDE, issuing body; English reproduction hosted by IPCA. **[Laws of Chess 2023](https://ipcachess.org/laws-of-chess-2023/)**. International Physically Disabled Chess Association (IPCA). Publication/update: Effective 2023-01-01; approval displayed as 07/08/2022. Edition/build: 2023 over-the-board Laws; historical edition, not certified latest. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Introduction 0.1; Articles 1.1–1.3, 6.1–6.2.1; Appendix D.1, D.2.1 and D.2.6. **Type:** Normative sport rules reproduced by a FIDE-affiliated association. **Limits/independence:** FIDE handbook/PDF routes failed; wording inspected through IPCA, byte equivalence unverified. Applicability is specified over-the-board chess, not a game-design or digital-accessibility standard. **Rights:** Rights retained; short paraphrase, no full rules reproduced. Claims using this source are identified in this entry’s ledger.

## Review and history

2026-10-10 — first genre draft in G08, `initial-draft-1`, attempt `G08-authoring-01`, preserved separately. 2026-10-11 UTC (2026-10-10 America/Los_Angeles) — separate assistant review correction `independent-review-correction-1`: source 007 is a mutable multiplayer page at a legacy beta URL and explicitly states full launch; no authenticated beta snapshot was inspected in this review. Candidate identity and version 0.1.0 persist; predecessor is the original candidate hash. Review does not grant human acceptance, canonical status or release.

Evidence and heading coverage remain open. The [review packet](../reviews/full-run-20261010-g08-review-packet.md) records contradictions, missing bodies, complete inventory, proposed index rows and queued child work. Additional research must retain existing identities; child keys require Library Coordination registration before submission. The next decisions are acceptance of these conditional recommendations, dependency reconciliation and ownership review; implementation and release remain separate.
