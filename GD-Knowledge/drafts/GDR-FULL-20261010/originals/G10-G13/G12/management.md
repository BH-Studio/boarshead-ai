---
id: GDR-CAND-20261010-G12-GEN-02
kind: genre
title: Management
version: 0.1.0
status: draft
candidate_revision: initial-author-draft-1
attempt_identity: G12-authoring-01
run_id: GDR-FULL-20261010
batch_id: G12
id_scope: run-scoped-temporary
owner_project: BH-GDR-Genres
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; dispatch and Los Angeles work date 2026-10-10 retained in run identity
coverage_status: open
aliases:
- management game
- operations management
tags:
- allocation
- scheduling
- delegation
- recovery
- feedback-delay
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G12-PAT-01
- GDR-CAND-20261010-G12-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G12-GEN-01
- GDR-CAND-20261010-G12-GEN-03
source_ids:
- GDR-SRC-20261010-G12-003
- GDR-SRC-20261010-G12-005
- GDR-SRC-20261010-G12-006
- GDR-SRC-20261010-G12-007
- GDR-SRC-20261010-G12-009
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial G12 bounded research draft; previous batch identities and queues are not reset.
hash_record: ../reviews/full-run-20261010-g12-integrity-receipt.md
---

# Management

**Draft, coverage open.** This entry concerns repeated decisions about resources, capacity, schedules and delegated action. It does not equate good management with unlimited growth, maximum profit, constant intervention or the least possible player input. The definition and recommendations are provisional, not studio-approved design choices. [C-01, C-08]

## Definition and boundaries

For this file, **management** is sustained allocation and coordination under constraints, with consequences that must be diagnosed and revised across time. **Allocation** decides what receives scarce means; **scheduling** decides when and in what order work uses capacity; **delegation** decides which choices another actor or rule may make; **diagnosis** distinguishes why outcomes differ from intentions. The managed entity may be an organization, service, production system or invented process. Human workers are not assumed to be interchangeable machines. [C-01, C-10]

A [simulation](simulation.md) may foreground operating or exploring a process without managing a scarce portfolio. A [city builder](city-builder.md) adds settlement-scale spatial interactions and public consequences. A timed optimization puzzle may end after one schedule rather than require continuing stewardship; a sandbox can remove scarcity; an incremental hybrid can emphasize watching accumulation instead of allocating. These are conditional distinctions, not exclusions imposed on store tags. Colony simulation and other neighbor entries remain unavailable dependencies; this file does not stand in for them. [C-01]

## Custom research instructions

Research the **decision horizon and intervention burden**, not only the production chain. Identify stocks, inflows/outflows, usable capacity, committed work, constraints, delays, uncertainties and the actor authorized to intervene. Determine whether the player is short of materials, processing capacity, transport, information, permissions or a desired tradeoff. Do not rename every delay a bottleneck: a planned reserve or rest interval can serve a chosen objective. [C-02, C-08]

Compare direct assignment, queue priorities, schedules, rules, delegated agents and deliberate nonintervention. In automation accounts, inspect exception handling and stop semantics, not just the automation’s happy path. Distinguish an author’s intended reduction in administrative burden from evidence that players prefer the change. Examine implementations with meaningful maintenance, contraction and recovery, alongside growth-oriented examples. [C-03–C-06, C-09]

Seek scheduling documentation, original production explanations, observable failure/recovery sequences and participant studies of feedback reasoning. The present source range is stronger for logistics and abstract feedback than for staffing, caregiving, labor relations or service work. Future research should include these missing contexts rather than generalize factory conventions to all organizations. Challenge “more workers fixes every shortage,” “automation is an upgrade,” “fewer clicks prove agency,” “bailouts always help,” and “a profitable organization necessarily represents its people ethically.” [C-02, C-07–C-10]

## Player promises and varied audiences

Possible promises include making a coherent plan, diagnosing an interacting system, nurturing an organization, surviving a disruption, or expressing values through competing priorities. These are hypotheses about useful design directions, not observed audience proportions. A player seeking scheduling mastery may resent an automatic optimizer; one seeking high-level planning may resent reauthorizing identical actions. Neither preference establishes the “correct” amount of micromanagement. [C-08, C-09]

Specify what the player remains responsible for after an unlock or automation change. A new interface can make the same decision accessible without removing it, while an optimizer can remove the decision even when it adds configuration work. Evaluate both authority and effort. Avoid treating every manual intervention as a failure: choosing an exception can be the point of management. [C-09, C-11]

## Characteristic loops and structures

The working loop is **set a goal → allocate or authorize → schedule/delegate → observe work and commitments → diagnose a deviation → sustain, recover or revise**. A session can center on a planning interval, a disruption or a review of delegated performance. Longer structures can introduce new dependencies, obligations, constituencies or constraints rather than merely larger quantities. These are analytical options, not defining mechanics every management game needs. [C-01, C-08]

### Stocks, flows, queues and feedback delay

An empty store, a late delivery and insufficient production capacity describe different states. Treating all three as “need more” can commit resources without addressing the cause. The historical investment experiment supplies a caution about dynamic reasoning, not a demonstration that a particular display fixes it. **Application bridge:** investigate whether the player can identify existing commitments before recommending additional capacity; also test whether the existing commitments actually meet the required horizon. A terse “pending” count can be inadequate when its work is blocked. [C-02, C-07; GDR-SRC-20261010-G12-003]

### Scheduling and bottlenecks

Wube’s robot scheduling account describes moving beyond nearest-idle assignment toward queues and arrival-time estimates, with engineering approximations. **Application bridge:** consider downstream waiting and completion, not just the next locally attractive assignment. This does not prove an automatic scheduler should replace player-authored priorities. An alternative is to expose the reason a job waits and let the player change a coarse priority; a simpler stable rule can be preferable to an opaque optimizer. [C-03, C-09; GDR-SRC-20261010-G12-005]

### Delegation and stop semantics

The inspected Factorio account distinguishes disabling future requester deliveries from stopping deliveries already underway; the OpenTTD manual documents conditional order branches. **Application bridge:** an automation control should state its scope and consequences, especially what stopping does *not* reverse. Use a retained policy decision and inspectable exceptions when supervision is intended. Do not infer that adding conditional logic makes a system understandable or enjoyable. [C-04, C-05, C-11; GDR-SRC-20261010-G12-006, GDR-SRC-20261010-G12-007]

### Sustainable recovery and safeguards

The Cities: Skylines II economy revision provides a historical creator account of reconsidering a hidden subsidy. It is evidence of a design change and rationale, not proof that removing recovery support improves experience. **Application bridge:** decide whether assistance is an explicit mode, temporary recovery, insurance, a budgeted service or an undisclosed balancing rule. Preserve meaningful choices about reducing commitments, borrowing future capacity, changing service levels or ending a failing operation when these fit the promise. Constant expansion is only one objective. [C-06, C-08; GDR-SRC-20261010-G12-009]

## Conditional application process

**Diagnose the valued decisions.** Name which choices deserve attention and which repeated actions are administrative execution. Record feasible objectives, including stability and recovery. Explain why a delayed outcome should remain uncertain, or why the player is entitled to inspect it. Do not infer intention from a low efficiency score. [C-08–C-10]

**Construct an obligation view.** For one task, distinguish available means, reservations, queued work, work in progress, blocked work and fulfilled obligations. Define units and the time horizon. A material unit, a worker-hour and a customer request are not interchangeable. Prefer an inspectable small model over a dashboard containing every possible metric. [C-02, C-11]

**Choose control granularity.** Compare individual commands, category priorities, schedules, conditional rules and delegated policies. Specify who handles exceptions and what remains manual. Offer a simpler alternative when policy configuration costs more attention than it saves. Accessibility may require a different control route even when the underlying decision is retained. [C-09, C-11, C-12]

**Expose recovery and authority boundaries.** Before commitment, show relevant opportunity costs and the difference between canceling a new instruction, stopping work and reversing its consequences. Make the treatment of current jobs, spent materials and future costs explicit. Do not promise undo where the model cannot provide it. [C-04, C-08, C-11]

**Evaluate diagnosis, preference and burden independently.** Later tests should compare the stated objective with actual consequences, then ask why the player acted. A deliberately redundant order might buy resilience; an apparently idle employee might be a chosen reserve. Revise the rules, presentation or objective separately according to the failure identified. [C-10, C-13]

### Illustrative worked example: repair cooperative

**Synthetic.** A cooperative receives repair requests and can spend a limited parts budget, schedule benches and authorize deliveries. The morning view shows unfilled requests. Three possible causes are deliberately distinguishable: parts are already en route, a bench is unavailable, or completed repairs await transport. Hiring another technician addresses none of the first or third causes and only helps the second when tools and space are available. This follows the example’s stated model, not a general claim about real repair shops. [C-02, C-10]

A proposed interface displays the selected request’s next blocking condition and relevant committed work, with drill-down rather than a compulsory enterprise dashboard. The player chooses whether to pay for expedited delivery, reschedule low-priority work or renegotiate the service target. That preserves a values-based choice instead of presenting a single efficiency-maximizing answer. [C-08, C-11]

A later rule may replenish common parts, but it excludes a protected reserve and requires review when a supplier changes. Stopping the rule prevents new orders; it does not erase deliveries already paid for. The player can inspect those commitments separately. The comparison is not “manual bad, automatic good”: in a scheduling-focused mode, those same repeated assignments may be the desired activity. [C-04, C-09, C-11]

**Recovery counterexample:** an unlimited invisible grant could keep the cooperative operating while making budgeting irrelevant. Conversely, abrupt irreversible closure can undermine a nurturing/learning goal. An explicitly selected forgiving mode, a visible one-time intervention, a smaller stable operation or a restart are alternatives with different meanings. No option is proven superior by the cited economy diary. [C-06, C-08]

## Applying shared topics

**Decision design — `GDR-CAND-20261010-F02-TOP-01`.** In management, opportunity costs often concern capacity already promised to later work. Preserve the distinction between feasible prediction and preferred priority. Avoid an optimization score that assumes the objective players are supposed to choose. [C-08, C-10]

**Interface and accessibility — `GDR-CAND-20261010-P01-TOP-02` and `GDR-CAND-20261010-P01-TOP-03`.** Management needs truthful freshness, ordering, exception and commitment states across dense screens. Review the complete cycle of selecting a job, understanding a constraint, changing authority and confirming the result. P01’s reviewed numerical scope remains intact; this file supplies no universal target or text size. [C-11, C-12]

**Learning/transfer and evaluation — `GDR-CAND-20261010-F01-TOP-03`, `GDR-CAND-20261010-F01-PAT-01`, `GDR-CAND-20261010-F07-TOP-01`.** Use scenarios with different correct diagnoses, not a repeated “order less” lesson. Preserve accommodations, separate forecast accuracy from preference, and distinguish model arithmetic from player outcomes. [C-07, C-13]

**Ethics — `GDR-CAND-20261010-F07-TOP-02`.** Management’s rules determine whether affected people have needs, voice, alternatives and consequences beyond output. Model those choices explicitly when relevant rather than append ethical language to an unchanged profit-only objective. [C-10]

**Missing economics dependency.** Original F03 packet inventory was inspected for identity only: `GDR-CAND-20261010-F03-TOP-02` and `GDR-CAND-20261010-F03-PAT-02` exist there, but their selected reviewed contents were not inspected. No conversion-loop-budget recipe or economy guidance is transferred. The shared simulation topic also remains unavailable. These are cross-owner dependencies, not licenses to duplicate them.

## Pattern selection and adaptations

[Pending-work reconciliation](../patterns/pending-work-reconciliation.md), `GDR-CAND-20261010-G12-PAT-01`, fits delayed work when the player needs to distinguish a present shortage from a future commitment. Use it locally at a decision point; avoid forcing accounting tasks that do not serve the chosen promise. [Bounded delegation contract](../patterns/bounded-delegation-contract.md), `GDR-CAND-20261010-G12-PAT-02`, fits policy supervision when execution can be delegated without taking away the desired decision. Its configuration and exception overhead must be evaluated. [C-11]

In a management/city-builder hybrid, account for locality and affected neighborhoods rather than optimizing a single global total. In a management/simulation hybrid, do not delegate the procedure a learning objective is meant to assess. In a crisis hybrid, pausing or automating consequences can change the pressure being designed; alternative access may preserve deliberation without requiring faster input. These are conditional adaptations, not inherited rules about every hybrid. [C-09, C-12]

## Accessibility, ethical representation, localization and production

Proposed access checks include non-color status distinctions, adjustable time pressure, reliable keyboard/controller traversal, grouped alerts with an inspectable history, and a way to reorient after absence. Review whether choosing a priority requires dragging, precise timing, memorizing an off-screen number or reading a transient warning. Use text that differentiates blocked, paused, canceled and completed; these states must remain distinct in translation. [C-12]

A “worker” is not ethically represented simply because it has a portrait. Where people are modeled, ask what the rules say about rest, autonomy, skill, relationships and burdens, and which consequences the player is permitted to ignore. These are review questions, not a claim that a specific representation improves real-world welfare. Avoid diagnostic, cultural or demographic stereotypes in invented efficiency modifiers. [C-10]

Production costs include reliable order identities, state histories, policy explainability, saved-rule migration, exception authoring and localization of causes. These obligations can make a modest fixed rule preferable to an elaborate automation language. Aggregate histories where useful, but do not aggregate away the very failure the player must diagnose. [C-11, C-12]

## Research questions and validation

**Proposed only; not performed.** Recruit the intended range of planning experience and access needs; do not use expert throughput as the sole target. Set study size and project-specific decision margins before testing. [C-13]

| Comparison | Procedure and measures | Confounds and rejection condition |
|---|---|---|
| Current stock view versus a focused commitment view | Present matched cases with transit, processing and authorization failures; ask for a diagnosis and a chosen response separately. Record unintended duplicate commitments, missed obligations, explanation quality and effort. | Prior arithmetic/logistics expertise, density and practice can explain differences. Reject a blanket view recommendation if accurate counts do not improve diagnosis or overload outweighs its value. |
| Manual execution versus simple automation versus bounded delegation | Hold the available goals/resources constant; let players configure, interrupt and recover a policy. Measure valued decisions retained, correction burden and understanding of in-flight work. | Fewer inputs are not a sufficient success measure. Reject delegation where the desired decisions disappear or configuration dominates play. |
| Visible forgiving recovery versus stricter consequences | Make mode differences explicit; introduce a comparable disruption; assess recovery choices, fairness interpretation and continued interest. | Carryover, attachment and knowledge of failure differ. Reject a claimed universal recovery rule when benefits reverse by intended promise or population. |

## Coverage, contradictions and review history

**Researched:** allocation/scheduling/delegation distinctions; delayed feedback; bottleneck diagnosis; commitment/stop semantics; recovery alternatives; ethical review questions; hybrid and access implications. **Open:** staffing/service-sector empirical evidence, long sessions, collective governance, comparative automation studies, executable version verification and selected reviewed economics/simulation dependencies. [C-01–C-13]

Relevant contradictions: **G12-CON-01** (visibility is not understanding), **G12-CON-03** (delegation can remove desired work), **G12-CON-06** (safeguards versus agency). Initial revision `initial-author-draft-1`; predecessor/supersession null. Author self-review rejected “automate all repetition” and “recovery must be punishing.” Independent content review, actual-host testing and release remain pending.

## Claim ledger

Claim IDs are local to this artifact. Bare three-digit source numbers in a ledger expand to `GDR-SRC-20261010-G12-`; DEP labels resolve in Reviewed dependency provenance. Family abbreviations such as G12-PAT-01 expand to `GDR-CAND-20261010-` plus that family suffix. Confidence concerns the stated claim, not a general endorsement. Recommendations and synthetic examples are not studio-approved decisions. No unperformed test is evidence.

| Claim | Precise claim | Class | Source and locator / reasoning | Confidence and applicability | Unresolved question |
|---|---|---|---|---|---|
| C-01 | Use management for recurring allocation, scheduling, delegation and diagnosis rather than any game displaying resources. | inference | G12 decision question; comparative framing of 005/007/009; TAXONOMY roster. | Moderate analytical utility; no universal classification claim. | Where do service, colony and incremental neighbors require different guidance? |
| C-02 | Distinguish material shortages, processing capacity, transit and prior commitments before choosing a remedy. | inference | 003 supply-line formulation, printed p.26; 005 scheduling context; illustrative cooperative assumptions. | Moderate system reasoning; player-facing benefit untested. | Does a concise distinction improve useful diagnosis in the actual model? |
| C-03 | The Wube scheduling account describes queues and arrival estimates with simplifying engineering choices. | practitioner-heuristic | GDR-SRC-20261010-G12-005, Smarter robots discussion. | High for documented production account; no general optimizer benefit. | Is a similar scheduling problem central or incidental to this game? |
| C-04 | The Factorio development account states that disabling a requester stops new orders while existing deliveries finish. | observed-example | GDR-SRC-20261010-G12-006, Logistic chest enable/disable; documented behavior, not runtime observation. | High for this historical text; current executable unknown. | Does the target model permit cancellation of current commitments? |
| C-05 | The OpenTTD manual describes conditional branching within vehicle orders. | observed-example | GDR-SRC-20261010-G12-007, Steps and Effect of order explained; manual artifact. | High for manual content; page revision and executable not verified. | Can players explain its conditions, limits and branches? |
| C-06 | The economy-revision account explains changing a hidden safeguard but does not establish that removing assistance improves experience. | practitioner-heuristic | GDR-SRC-20261010-G12-009, introduction and THE ECONOMY. | Moderate for creator rationale; no controlled effect claim. | What safeguard supports the selected promise rather than obscures it? |
| C-07 | Historical dynamic-task failures warrant a diagnosis question, not a claim that more state visibility is sufficient. | empirical-evidence | GDR-SRC-20261010-G12-003, METHOD/Discussion, printed pp.22–24,27–28. | Moderate within the historical experiment; no genre-wide prevalence estimate. | Do players misread commitments, misunderstand feedback, or choose another objective? |
| C-08 | Recovery, reserves, contraction and assistance should be evaluated against explicit player goals rather than universal growth or punishment requirements. | hypothesis | DEP-DECISION; 009 as a conditional design case; cooperative illustration. | Low for outcome benefits; multiple coherent alternatives exist. | Which forms of recovery preserve the intended stakes? |
| C-09 | Delegation is useful only conditionally: it can reduce execution burden or remove desired decisions and add configuration work. | hypothesis | 005 scheduling account; 006 Reactor circuit connection countercase; G12-PAT-02. | Moderate rationale, low causal confidence for G12 application. | Which decisions and costs actually change? |
| C-10 | Objective choice and affected people’s constraints should remain distinct from a single efficiency score. | inference | DEP-DECISION opportunity cost; DEP-ETHICS rules/agency; synthetic cooperative. | Moderate normative/analytical rationale; no welfare effect established. | Whose costs, agency and alternatives are excluded? |
| C-11 | Focused commitment views and explicit delegation contracts are testable alternatives, not validated best practices. | hypothesis | G12-PAT-01/02; DEP-UI; 006/007 mechanism examples. | Low: no G12 comparative player study. | Do they improve chosen decisions without imposing disproportionate administration? |
| C-12 | Access, localization, history and policy-maintenance costs require complete-workflow checks. | hypothesis | DEP-ACCESS scoped access chain; DEP-UI; conditional production reasoning. | Low for particular implementations; no universal numerical thresholds. | Which workflow blocks the intended population? |
| C-13 | Proposed tests should separate diagnosis, preference, authority and burden, using changed-answer cases and preserved accommodations. | hypothesis | DEP-TRANSFER corrected recipe/example; DEP-EVALUATION; this file’s test table. | Moderate construct rationale; no executed protocol or outcomes. | What measured result would make the team reject each candidate technique? |

## References

Observer: the G12 authoring assistant, through document inspection, not game execution. Access/check date: **2026-10-11 UTC**. Source IDs are temporary run-scoped identities, reused within G12. Cross-batch canonical URL/DOI/edition deduplication remains pending. `relevant-excerpt` does not mean the full work, runtime or linked material was inspected.

### GDR-SRC-20261010-G12-003

**John D. Sterman. _Misperceptions of Feedback in Dynamic Decision Making_.** Publication/update: 1989. Publisher: International System Dynamics Conference proceedings; condensed reprint of an Academic Press journal article. [Inspected source route](https://proceedings.systemdynamics.org/1989/proceed/plenary-pdf/sterm021.pdf).

**Claims supported or used as an inference/hypothesis premise:** C-02/C-07. **Edition/build:** Eleven-page proceedings scan, printed pp. 21–31; first-page footnote identifies condensed reprint from Organizational Behavior and Human Decision Processes 43 (June 1989), original pp. 301–335; DOI 10.1016/0749-5978(89)90041-1 identifies original, not a separately inspected text. **Access:** `relevant-excerpt`. **Type:** Original empirical research, accessed through author conference reprint. **Exact locator:** PDF pp. 1–4, 6–8 (printed pp. 21–24, 26–28): title/footnote; METHOD; representative trajectories/Fig. 3; supply-line formulation; Discussion and Fig. 5. These pages were visually inspected using web screenshots.

**Rights:** Academic Press copyright noted; paraphrase only, no scans or figures redistributed. **Limits and independence:** N=49 selected fluent-English students/professionals in a capital-investment task, not a game-audience sample. Full state/history available, no time limit. Reported oscillatory performance does not identify the effect of a new dashboard. Fig. 5 is model simulation, not a second human experiment. Full journal, raw data and uninspected tables not used; no effect size, confidence interval or replication claim transferred. Distinct from Sterman’s 1989 Management Science beer-distribution paper. Author overlap with 004 does not create replication.

### GDR-SRC-20261010-G12-005

**kovarex; Oxyd; Klonan. _Friday Facts #374 – Smarter robots_.** Publication/update: 2023-09-01. Publisher: Wube Software / Factorio development blog. [Inspected source route](https://www.factorio.com/blog/post/fff-374).

**Claims supported or used as an inference/hypothesis premise:** C-03; premise for C-09. **Edition/build:** Development account contrasting Factorio 1.1 with work toward 2.0; exact executable build unknown. **Access:** `relevant-excerpt`. **Type:** Firsthand development account. **Exact locator:** “Smarter robots” discussion of closest-idle assignment, per-robot queues, estimated arrival time and simplifying recharge/queue processing.

**Rights:** Copyrighted blog; paraphrase only; animations and code not reproduced. **Limits and independence:** Creator explanation of scheduling changes and engineering tradeoffs, not controlled player evidence. Same Wube production line as 006. Embedded animations were not analyzed as build observations.

### GDR-SRC-20261010-G12-006

**Klonan. _Friday Facts #428 – Reactor & Logistics circuit control_.** Publication/update: 2024-09-13. Publisher: Wube Software / Factorio development blog. [Inspected source route](https://www.factorio.com/blog/post/fff-428).

**Claims supported or used as an inference/hypothesis premise:** C-04; countercase for C-09/C-11. **Edition/build:** Pre-2.0 development description; executable build unknown. **Access:** `relevant-excerpt`. **Type:** Firsthand development account. **Exact locator:** “Reactor circuit connection”; “Roboport circuit improvements”; “Logistic chest enable/disable”.

**Rights:** Copyrighted blog; paraphrase only. **Limits and independence:** Reports direct reactor signals, tracking limits and disabling new requester orders while existing deliveries finish. Does not validate agency or accessibility effects. LAN-party feedback is an author account, not an inspected controlled dataset; same production line as 005.

### GDR-SRC-20261010-G12-007

**OpenTTD project wiki contributors; individual page authors not established. _Conditional Orders_.** Publication/update: unknown. Publisher: OpenTTD official project-hosted wiki. [Inspected source route](https://wiki.openttd.org/en/Manual/Conditional%20Orders).

**Claims supported or used as an inference/hypothesis premise:** C-05; premise for C-11. **Edition/build:** Mutable community-maintained manual; page revision and executable version unknown. **Access:** `relevant-excerpt`. **Type:** First-party-hosted, community-authored technical manual. **Exact locator:** “Using the interface”; “Steps”; “Effect of order explained”.

**Rights:** GNU Free Documentation License as displayed; paraphrase only; no tutorial images or code reproduced. **Limits and independence:** Documents conditional branching in vehicle orders. Procedure not executed; project hosting does not make it a player experiment or establish individual author expertise.

### GDR-SRC-20261010-G12-009

**Colossal Order. _Dev Diary: Economy 2.0 – Part One_.** Publication/update: 2024-06-03. Publisher: Paradox Interactive / Cities: Skylines II. [Inspected source route](https://www.paradoxinteractive.com/games/cities-skylines-ii/news/dev-diary-economy-part-one).

**Claims supported or used as an inference/hypothesis premise:** C-06; context for C-08. **Edition/build:** Announced Economy 2.0 changes; not a verified installed patch or current build. **Access:** `relevant-excerpt`. **Type:** Firsthand development explanation and reported feedback. **Exact locator:** Introduction; “THE ECONOMY”; “CITY SERVICES”; “DEMAND”.

**Rights:** Copyrighted publisher/developer page; paraphrase only. **Limits and independence:** Explains removal of a hidden subsidy and changes to costs/control. Creator rationale and reported feedback do not prove that fewer safeguards cause greater enjoyment or welfare. Same production line as 008; explicitly historical.

## Reviewed dependency provenance

These are inspected **parent-selected reviewed drafts**, not released references and not new G12 sources. Their underlying cited papers were not automatically re-inspected. Only the named passages are transferred as qualified research guidance. Exact bytes came from the materialized waves 1–2 archive; they are not copied into this output. Full archive and gap receipts are in the [batch dependency record](../reviews/full-run-20261010-g12-review-packet.md#reviewed-dependencies).

**DEP-TRANSFER: `GDR-CAND-20261010-F01-PAT-01`**, version `0.1.0`, `draft`, candidate revision `independent-review-correction-1`. Archive path `selected-drafts/patterns/supported-attempt-and-transfer-check.md`. Inspected: Recipe; corrected Worked examples, lines 96–127: vary the correct feasibility answer, retain accommodations, separate preference from rule prediction. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`.

**DEP-LEARNING: `GDR-CAND-20261010-F01-TOP-03`**, version `0.1.0`, `draft`, candidate revision `field absent; not inferred`. Archive path `selected-drafts/topics/learning-and-onboarding.md`. Inspected: Core explanation/mechanisms and application process, approximately lines 55–140: rule knowledge, access, feedback, re-entry and transfer. SHA-256 `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598`.

**DEP-UI: `GDR-CAND-20261010-P01-TOP-02`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/interface-and-information.md`. Inspected: Task information contract and availability-to-recovery diagnostic, lines 55–85. SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`.

**DEP-ACCESS: `GDR-CAND-20261010-P01-TOP-03`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/accessibility-and-inclusive-interaction.md`. Inspected: Applicability/scope and access chain, lines 56–103; P01 CORRECTION_RECEIPT.md. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`.

**DEP-DECISION: `GDR-CAND-20261010-F02-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/decision-design.md`. Inspected: Entitled information, uncertainty, opportunity cost and reversibility, lines 63–104. SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`.

**DEP-EVALUATION: `GDR-CAND-20261010-F07-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/evaluation-and-balancing.md`. Inspected: Evidence-to-question distinctions, lines 65–94: correctness checks do not measure enjoyment. SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`.

**DEP-ETHICS: `GDR-CAND-20261010-F07-TOP-02`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/ethical-and-sustainable-design.md`. Inspected: Representation and production obligations, lines 70–104: rules and agency are part of representation. SHA-256 `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0`.

**Transfer boundary:** preserve source/candidate identities as recorded. No universal UI pixel, contrast, timing, difficulty or sample-size rule is imported. F01’s corrected feasibility/transfer discrimination is retained; access supports are not faded as tutorial prompts. Later reviewed simulation/economy/spatial-topic bytes remain missing unless explicitly identified in the packet.

