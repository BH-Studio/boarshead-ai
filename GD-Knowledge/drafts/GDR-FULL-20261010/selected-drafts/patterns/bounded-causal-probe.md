---
id: GDR-CAND-20261010-F05-PAT-01
kind: pattern
title: Bounded causal probe
version: 0.1.0
status: draft
candidate_revision: initial-research-1
attempt_id: F05-authoring-01
run_id: GDR-FULL-20261010
batch_id: F05
identity_scope: temporary-run-scoped
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- bounded systemic experiment
- causal affordance probe
- optional rule investigation
tags:
- simulation
- causal-inference
- optional-learning
- uncertainty
- recovery
- pattern-candidate
- coverage-open
related_topics:
- GDR-CAND-20261010-F05-TOP-01
- GDR-CAND-20261010-F05-TOP-02
related_patterns:
- GDR-CAND-20261010-F05-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F05-003
- GDR-SRC-20261010-F05-004
- GDR-SRC-20261010-F05-005
- GDR-SRC-20261010-F01-08
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial F05 submission; no prior F05 candidate bytes observed in this conversation; no
  permanent identity allocation.
hash_record: ../reviews/full-run-20261010-f05-integrity.md
---

# Bounded causal probe

> **Draft research candidate — not released, independently reviewed, or approved for implementation.** Version `0.1.0`; revision `initial-research-1`. Application procedures and numerical illustrations are proposals, not adopted studio decisions. No F05 game execution, prototype, participant study or playtest occurred.

## Purpose

Give a player a **bounded, optional opportunity to investigate a causal relation through action**, rather than requiring blind repetition or revealing the entire rule. The intended benefit is better-grounded planning while retaining meaningful uncertainty and stakes. That benefit is a **hypothesis**; this pattern is not an empirically validated learning intervention. [C-01]

This technique is not the F01 Supported attempt and transfer check pattern renamed. F01 addresses supported learning and diagnostic transfer. This pattern addresses the conditions under which a player’s own intervention can discriminate between competing causal explanations inside a systemic world. It may use F01’s corrected changed-answer diagnostic as a later evaluation method without requiring prompt fading. It is also distinct from F07’s researcher-facing Triangulated balance diagnosis and F03’s unreviewed Conversion-loop budget inventory. The inspected F02 packet already queues **Q-01 Costed information probe** and **Q-04 Commitment-aware rehearsal**. Potential overlap is unresolved: F05 provisionally owns discriminating an interacting rule through intervention; F02’s questions concern the price of information and the boundary of commitment. Coordination must decide whether these are separate techniques, adaptations or a merge. F05 does not consume those queue items or allocate their child keys. [C-02, C-08]

## Context and prerequisites

Use it only when causal inquiry is a legitimate part of the intended experience, a relevant relation is sufficiently stable, and the player can observe the facts needed to compare explanations. The environment must support an intervention whose local cost and side effects are understood by the design team. A reset is optional; an informative irreversible probe can be valid, but its cost must not be misrepresented as reversible. [C-02–C-04]

The player need not know the rule in advance. They do need usable access to the relevant action and observation. Required ordinary state information, alternative input and sensory accommodations remain available. A probe that functions only by removing an accommodation is not this pattern. [C-05]

Prerequisites also include an owner for unintended consequences, a way to identify uncontrolled state changes, and a simpler alternative such as an authored demonstration, clearer state description or no special probe. If the surrounding simulation changes too quickly to support the intended comparison, narrow the question, provide a deliberately controlled context, or omit the technique. No particular engine architecture is prescribed. [C-03, C-07]

## Mechanism and evidence

| Causal link | What supports it | What is not established |
|---|---|---|
| Define competing explanations and an intervention that gives different predicted outcomes | Logical discrimination within a stated model; the inspected modeling and technical accounts supply bounded examples | That the chosen model contains every relevant cause |
| Preserve state facts and identify changed conditions | Reproduction/scope reasoning; reviewed F01 and P02 cautions | That a player notices, remembers or interprets all relevant facts |
| Observe a consequence that favors one explanation | Valid only under the declared rule/state assumptions | That one outcome identifies a stochastic cause, or rules out hidden confounds |
| Transfer the relation to a changed case | Proposed diagnostic informed by the corrected F01 pattern | Durable learning, mastery or gameplay benefit |
| Use that knowledge in a valued decision | Creator rationale motivates the question; local hypothesis | Improved satisfaction, accessibility, agency or retention |

Reynolds provides inspectable technical decompositions, Nintendo describes intended affordance consistency, and Dormans explicitly bounds simulation conclusions. They do not constitute trials of this complete pattern. Factorio’s historical concurrency report additionally cautions against assuming that a visible starting configuration fully specifies a result. [C-01–C-03, C-06]

## Recipe

### 1. Name the causal question and competing explanations

Write a question in player-action terms: “Does opening this connection permit transfer, or is storage capacity the limiting condition?” Identify at least the explanations the proposed contrast is meant to discriminate; this is not a universal required number of alternatives. If all candidate explanations predict the same observation, choose a different intervention or accept that the probe cannot answer that question. [C-02]

**Exit:** do not add a test area solely because the system is complicated. If causal inquiry adds no intended decision value, prefer direct communication or a simpler rule. [C-01, C-07]

### 2. Declare what is held stable and what may change

Identify source state, destination state, delays, agent interventions, hidden-but-intentional variables and environmental changes that can confound the contrast. Record which state is reset or persists after an attempt. A repeatable seed is not sufficient evidence of an identical state. In a shared or live world, do not imply isolation that does not exist. [C-02, C-03]

**Exit:** if relevant uncontrolled changes cannot be made apparent or meaningfully bounded, present the result as uncertain evidence, not a clean experiment. Avoid teaching an incorrect deterministic rule from one stochastic outcome. [C-03, C-06]

### 3. Choose an intervention and a cost boundary

Choose an action that changes the relevant condition with limited incidental change. Specify resource expenditure, propagation range, consequences for other actors and any retained information. A local reset should restore only what it promises; restoring stock while leaving heat, reputation or another participant’s loss unchanged must be visible in the contract. A costless replay also cannot erase what the player has learned. [C-03, C-04]

**Exit:** remove or redesign the probe when it transfers costs to someone who did not choose it, becomes an unlimited resource source, or nullifies a central commitment. Local recovery is not automatically ethical or strategically neutral. [C-04, C-07]

### 4. Provide observation without supplying the preferred action

Expose the facts the task makes available through usable routes. Preserve intended uncertainty: an observation can say that transfer failed without naming an unknown cause. Conversely, do not hide a required capacity value merely to keep one sensory channel special. Coordinate labels, reference frames, history, persistence and language with Presentation and Interaction. No universal icon set, reaction window or text size is part of the recipe. [C-05]

### 5. Let the player inspect the consequence

Keep the causal trace intelligible at the level required for the question: what changed, what did not and what remains unknown. This could be an observable state, a concise history or a repeatable description rather than an explicit formula. Do not force an explanatory screen that destroys a deliberately implicit experience. If multiple rules acted, allow the trace to communicate that limit rather than falsely attributing the result to a single cause. [C-03, C-05, C-06]

### 6. Evaluate changed cases, not repeated answers

For a separately authorized evaluation, change a relevant condition so the correct prediction changes; include an exact boundary when the rule has one. Also change irrelevant presentation while preserving the rule. Ask whether an action is permitted before asking whether the participant chooses it. Keep access supports and ordinary information unchanged. Do not mistake button familiarity, repeated refusal or an answer-leading visual cue for causal understanding. [C-08]

### 7. Retain, narrow or remove

Retain only when the proposed benefit survives the simpler comparison and the probe does not erase the intended uncertainty, cost or social contract. Narrow it to optional assistance, a particular early context or a smaller causal relation when transfer is weak or the information burden is too high. Stop when ordinary communication or authored demonstration does the job better. These are future decision rules, not an approval of any local implementation. [C-01, C-07, C-08]

### Adjustable variables

| Variable | Design question | Boundary to preserve |
|---|---|---|
| Intervention scope | One property, interacting properties, or a whole local subsystem? | Do not imply causal isolation that the world does not provide. |
| Persistence/reset | What state and information survive? | A reset promise must not conceal retained consequences. |
| Cost and propagation | Who pays, how far can effects travel, and how often can it be repeated? | No unexamined shared loss or free production loop. |
| Observation granularity | State change, short explanation, history, or optional detail? | Keep required facts without necessarily revealing hidden causes. |
| Time and response demands | Can the player inspect before acting or revisit the evidence? | Evaluate access and stakes together rather than using a universal time window. |
| Optionality | Is the probe discoverable, offered as assistance, or absent? | Do not turn optional learning into an undisclosed progression requirement. |

These are proposed variables, not prescribed numerical settings. [C-04–C-08]

## Worked examples

### Illustrative example: a capacity-limited connection

A fictional transfer rule moves material only while a valve is open, the source has stock, and the destination has spare capacity. Transfer is limited by available source stock and destination space. For illustration, capacity is **5 units**; the source contains **3**. These are invented arithmetic settings, not empirical tuning values. No model was executed. [C-02]

With the valve open and destination stock **4**, at most **1** unit transfers. At destination stock **5**, none transfers. At destination stock **2**, all **3** units can transfer, exactly filling capacity. Closing the valve prevents transfer even when space exists. These cases distinguish valve state and capacity from a blanket “transfer always works” or “transfer always fails” answer. They are consequences of the stipulated rule, not participant results. [C-02, C-08]

The bounded probe permits inspecting the two stocks and opening or closing a local valve without changing anyone else’s storage. After an attempt, the player can see the resulting stocks. A proposed reset restores both containers, not merely the displayed number at one end. Later cases change the available capacity and presentation. Ask what amount is possible separately from whether transferring it is strategically desirable. [C-03–C-05, C-08]

**Alternative:** explain the capacity rule directly in an accessible interface. If the experience is about planning a larger network rather than discovering local mechanics, that may be better than requiring a series of experiments. Do not impose inquiry because the pattern exists. [C-07]

### Illustrative counterexample: a costly revelation

An interaction deliberately reveals information that changes a relationship irreversibly. A reset that restores a numerical state cannot restore the player’s ignorance. A free repeatable probe would alter the commitment itself. Provide understandable available evidence and a clear decision boundary instead; do not claim “safe experimentation” when the defining cost is knowledge. This is a plausible disconfirming context, not an observed game study. [C-03, C-04, C-07]

## Tradeoffs and alternatives

A bounded probe can create extra state, content, UI, explanation and testing obligations. It may privilege a player who enjoys analytic inquiry or expose rules that another player would prefer to infer implicitly. A safe context can reduce the pressure needed to interpret a relation, yet also remove the uncertainty or stakes that made the relation interesting. These competing effects are hypotheses for the local experience. [C-01, C-04, C-07]

Alternatives include clearer ordinary feedback, an authored demonstration, optional explanation, direct rule disclosure, a simpler system, a single consequential observation, or leaving the relation uncertain. Choose according to the intended decision and access needs, not a supposed universal progression from tutorial to independence. Needed accommodations do not become temporary training wheels. [C-05, C-07]

## Failure cases

**False causal lesson:** an unrecorded agent action or delayed state change produces a different outcome. Warning sign: participants form a rule that fits the probe but fails in equivalent-looking situations. Correct the state/observation contract or narrow the claim; adding more repetitions of the same confounded example is insufficient. [C-03, C-06]

**Rote success:** participants predict the same answer across changed cases or rely on a special indicator unavailable elsewhere. Vary the correct outcome, inspect explanations and distinguish prediction from preference. Do not remove required state information to make the test harder. [C-05, C-08]

**Probe exploitation or erased stakes:** the reset creates resources, bypasses a consequential choice, or allows one player to impose costs on others. Restrict the contract, substitute a demonstration or remove the probe. Mere completion does not indicate acceptable incentive effects. [C-04, C-07]

**Inaccessible evidence or overload:** participants cannot perceive the relevant change, track several delayed causes or perform the bounded action with their selected controls. Rework representation and action demands with the owning domain; an extra caption or longer duration is a proposal to evaluate, not automatically equivalent access. [C-05, C-08]

## Counterexamples and do not use conditions

Do not use this recipe as a mandatory feature where exact dramatic staging, deliberately irreducible uncertainty, costly information or shared competitive secrecy is central. Do not use it where repeatability is falsely claimed, the probe cannot stay within accepted cost boundaries, or the proposed test only confirms a rule already explicitly supplied. A simple rule does not need an experimental apparatus merely because it could support one. [C-03, C-07]

The strongest challenge is that ordinary feedback may already support inference while a special probe adds workload and advertises the system’s solution. The burden is to demonstrate the added benefit in the relevant context; lack of evidence is not permission to market the pattern as established. [C-01, C-08]

## Playtest

**Proposed — not performed.** Compare ordinary feedback alone with the same feedback plus an optional bounded intervention, and optionally a direct explanation alternative when that is compatible with the experience. Hold underlying rules, ordinary information, access supports and task stakes constant where possible. Record unavoidable differences rather than presenting them as controlled. [C-08]

Use initial, changed-answer, exact-boundary and later unfamiliar-context cases. Separate predicted transition, explanation, preferred action, actual action and intended experience. Include relevant experience levels and participants who use affected sensory/input/cognitive supports; plan recruitment, consent and sample size separately. Counterbalance order and account for learning carryover, probe self-selection, prior knowledge, UI cues and stochastic outcomes. [C-05, C-08]

Narrow or reject the pattern when success does not transfer beyond repeated answers, ordinary feedback performs similarly with less burden, relevant uncertainty is lost, or intervention costs violate the intended experience. A numerical non-inferiority margin or effect target must be set for the actual project before data collection, not invented here. No player benefit or test pass has been observed in F05. [C-08]

## Claim ledger and sources

Claim IDs are scoped to this artifact. Confidence is confidence in the precise bounded statement, not in a universal player benefit. A hypothesis remains untested even when its technical premises are well supported.

| Claim | Exact material claim and class | Evidence / precise locator | Applicability, confidence reason and unresolved issue |
|---|---|---|---|
| C-01 | `hypothesis` — An optional bounded causal intervention may improve useful planning without revealing the entire system. | GDR-SRC-20261010-F05-004, creator affordance rationale; GDR-SRC-20261010-F01-08, bounded-model context; proposed synthesis. | Low: no matched player-efficacy study of the complete pattern. It may expose the solution or add unnecessary burden. |
| C-02 | `inference` — Within a declared rule model, a contrast is discriminating only when competing explanations predict different outcomes. | GDR-SRC-20261010-F01-08, model representation/limits; explicit logic and the illustrative transfer rule. | High for logical discrimination under assumptions; not proof that all real causes were modeled or learned. |
| C-03 | `inference` — Repeated-looking attempts need not have identical causal state, and reset cannot erase acquired information. | GDR-SRC-20261010-F05-005, historical concurrency case; reviewed F02 decision candidate, commitment/information distinction. | Moderate for applying scope/reproduction reasoning; complete local state requirements remain untested. |
| C-04 | `hypothesis` — Explicit intervention, persistence and ownership boundaries may contain harm while retaining intended costs. | Reviewed F02 challenge and F07 ethical candidates; proposed mechanism, not imported efficacy results. | Low: exploitation, shared costs and the value of irreversibility require local evaluation. |
| C-05 | `hypothesis` — Preserve ordinary state facts and accommodations while offering uncertainty-preserving observation routes. | Reviewed F01 corrected pattern and P02 fact-preserving cue alternatives, Recipe §§1–6; P01 scope corrections. | Low for F05 access/learning benefit; no numeric standard or conformance claim. Sensory parity is not certified. |
| C-06 | `inference` — Technical coherence provides a possible basis for inquiry, but one result does not establish a causal rule or a player benefit. | GDR-SRC-20261010-F05-003, behavior combination; GDR-SRC-20261010-F05-004, intent; GDR-SRC-20261010-F01-08, Discussion. | Moderate bridge with explicit alternatives; uncontrolled state and stochasticity can defeat the contrast. |
| C-07 | `hypothesis` — Prefer simpler communication or omit the probe when it undermines uncertainty, commitment, accessibility or useful work. | Counterexamples and proposed comparison in this pattern; reviewed F02/F07 cautions. | Low for comparative superiority; use conditions are proposed, not approved game decisions. |
| C-08 | `hypothesis` — Changed-answer and later-context comparisons may distinguish useful inference from memorized responses or preference. | Reviewed F01-PAT-01, corrected Worked examples; F07-TOP-01 measurement limits; proposed Playtest above. | Low for unperformed diagnostic validity and outcomes. Independent study design and actual observations remain required. |

## References

All listed sources were inspected on 2026-10-10 to the stated extent. This is bounded research, not an exhaustive search. Source titles and locators identify historical editions; mutable documentation must be rechecked before implementation. Source repetition across entries does not add independent evidence.

### GDR-SRC-20261010-F05-003

**Craig W. Reynolds. [Steering Behaviors For Autonomous Characters](https://www.red3d.com/cwr/steer/gdc99/).** Game Developers Conference paper, author-hosted HTML. Publication/update: 1999.

**Edition / access:** GDC 1999 paper; not a current engine specification. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original technical/practitioner paper.

**Inspected locators:** Introduction; Locomotion; A Simple Vehicle Model; Combining Behaviors (especially blending/cancellation and prioritization). HTML lines 19–31, 52–80 and 218–231.

**Claims supported or informing hypotheses in this entry:** C-06 technical context only.

**Limits / independence:** Algorithmic decomposition and practitioner reasoning, not human-player efficacy evidence or a requirement to use three layers. Referenced earlier studies were not separately inspected.

**Rights:** Author-hosted copyrighted paper; no figures, algorithms or code reproduced verbatim.

### GDR-SRC-20261010-F05-004

**Nintendo; relevant interview speakers Hidemaro Fujibayashi and Takuhiro Dohta. [Ask the Developer Vol. 9, The Legend of Zelda: Tears of the Kingdom — Part 5](https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-part-5/).** Nintendo. Publication/update: 2023-05-09.

**Edition / access:** Prelaunch Nintendo Switch development interview; English translation of Japanese interview; no later patch audit. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand developer interview.

**Inspected locators:** Part 5 discussion of unexpected solutions, what players expect to be possible, movable/fixed objects, and lids on jars; rendered lines 69–87.

**Claims supported or informing hypotheses in this entry:** C-01/C-06 creator rationale, not efficacy.

**Limits / independence:** Creator account of design choices and intended understanding/satisfaction, not a controlled comparison or a hands-on gameplay observation. Other interview parts not imported.

**Rights:** Nintendo copyrighted interview/images; paraphrase only; no media reproduced.

### GDR-SRC-20261010-F05-005

**Rseding / Wube Software. [Friday Facts #415 — Fix, Improve, Optimize](https://www.factorio.com/blog/post/fff-415).** Factorio development blog. Publication/update: 2024-06-14.

**Edition / access:** Factorio 1.1 and then-in-development 2.0 account; not verification of present behavior. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand technical development report.

**Inspected locators:** Deterministic multithreading; Robot task performance (rendered lines 25–39 and 49–63).

**Claims supported or informing hypotheses in this entry:** C-03 reproduction-scope reasoning.

**Limits / independence:** Reported multi-condition defect and optimization reasoning, not reproduced here. Future-tense fixes in the article are not current verified state. No general speedup or deterministic guarantee inferred.

**Rights:** Public developer article; paraphrased; no code/images redistributed.

### GDR-SRC-20261010-F01-08

**Joris Dormans. [Simulating Mechanics to Study Emergence in Games](https://ojs.aaai.org/index.php/AIIDE/article/download/12477/12336/16005).** Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment 7(3), 2–7; WS-11-19. Publication/update: 2011-10-09.

**Edition / access:** 2011 paper; Machinations / SimWar model, not a playable-build evaluation. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original modeling method and computational simulation report.
DOI: `10.1609/aiide.v7i3.12477`.

**Inspected locators:** Printed pp. 2–4 on model notation and construction; printed p. 6 on scripted-policy simulations; Discussion and Conclusion, p. 7. Screenshot of PDF p. 5 (printed p. 6), Figures 4–7, inspected.

**Claims supported or informing hypotheses in this entry:** C-02/C-06; C-01 mechanism context.

**Limits / independence:** Artificial policies and a reduced resource model omit tactical/spatial gameplay. The 1,000-session simulation setting is the paper’s, not an F05 test or recommended sample. Existing same-work mapping F03-007 ↔ F01-08 remains pending central deduplication.

**Rights:** Publisher-hosted research paper; license scope not independently audited; paraphrase only; paper/figures not redistributed.

## Related entries and history

Parent: [Simulation and systemic behavior](../topics/simulation-and-systemic-behavior.md), `GDR-CAND-20261010-F05-TOP-01`. Complement: [Constraint-gated generation with bounded fallback](constraint-gated-generation-with-bounded-fallback.md), `GDR-CAND-20261010-F05-PAT-02`, when an initial situation must satisfy declared inquiry conditions.

The corrected F01 pattern supplies evaluation distinctions, not a duplicate purpose or evidence of efficacy. The [packet dependency ledger](../reviews/full-run-20261010-f05-review-packet.md#reviewed-dependency-inspection) records selected revision/hash/locators for F01/F02/F07/P01/P02. F03 Conversion-loop budget is an unreviewed-context inventory entry; its body was not inspected or silently incorporated. No genre adaptation or implementation accompanies this artifact.

Open issues: player efficacy, stochastic causal inference, protected shared-state costs, accessibility and cultural interpretation, and whether ordinary feedback is sufficient. Related packet-local issues: `F05-CON-01`, `F05-CON-04`, `F05-CON-06`. No hypothesis is resolved by this file’s existence.

2026-10-10: first submission, `0.1.0` / `initial-research-1`; predecessor/supersession null; author self-review only. Exact byte identity is in the detached integrity receipt. No independent F05 review, actual player test, permanent ID, approval or release.
