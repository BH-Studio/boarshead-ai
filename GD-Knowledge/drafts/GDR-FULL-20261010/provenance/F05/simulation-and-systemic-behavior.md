---
id: GDR-CAND-20261010-F05-TOP-01
kind: topic
title: Simulation and systemic behavior
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
- systemic simulation
- emergent rule interactions
- ecological game systems
- agent coherence
- simulation boundaries
tags:
- simulation
- emergence
- causal-inference
- agents
- ecology
- physics
- accessibility
- production-cost
- coverage-open
related_topics:
- GDR-CAND-20261010-F05-TOP-02
- GDR-CAND-20261010-F01-TOP-02
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F05-PAT-01
- GDR-CAND-20261010-F05-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-F05-001
- GDR-SRC-20261010-F05-002
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

# Simulation and systemic behavior

> **Draft research candidate — not released, independently reviewed, or approved for implementation.** Version `0.1.0`; revision `initial-research-1`. Application procedures and numerical illustrations are proposals, not adopted studio decisions. No F05 game execution, prototype, participant study or playtest occurred.

## Decision and scope

This entry helps decide **which parts of a world should respond through interacting rules, what the player needs to infer about those rules, and which interactions must be constrained or recoverable**. It covers physical behavior, ecology-like resource relations, agent behavior, cross-system cascades and simulation cost. It does not choose an engine, prescribe a realistic world model, or supply genre-specific balance. Spatial/narrative orchestration belongs with Worlds and Characters; sensory communication belongs with Presentation and Interaction. [C-01, C-18]

Working definitions are deliberately separate. **Model fidelity** describes what a model represents relative to a chosen target; the target need not be real-world physics. **Perceived coherence** concerns whether players can form sufficiently consistent expectations from what is available to them. **Useful decisions** concern whether acting on those expectations serves the intended experience. **Emergence** here means larger-scale behavior arising from interacting rules without individually authoring each resulting event. These are analytic distinctions, not independently validated scales or a hierarchy in which more simulation is always better. [C-01]

A reversible research assumption is that the designer can state a small set of intended causal affordances and failure boundaries. Where a project instead promises unknowable forces, exact staging or uncompromising irreversible failure, the application must change or be omitted; uncertainty is not automatically a defect. [C-01, C-11, C-12]

## Core explanation and mechanisms

### Fidelity, coherence and decision value are different questions

Reynolds’s steering paper deliberately works with an idealized locomotion model. Nintendo’s interview describes coherent object-property choices and deliberate exceptions in support of player expectations. These are specific technical/design accounts, not a comparison showing that realism improves play. The application bridge is to begin with the consequences players should be able to anticipate, then ask which state and rules must exist to sustain those consequences. More represented detail is justified only when it changes a relevant decision or fulfills an explicitly accepted expressive goal. [C-01, C-05, C-07]

For example, a door can use a binary open/closed rule, a scripted sweep, a constrained physical hinge, or a much richer material simulation. The design question is whether timing, wedging, force, sound or damage should matter. A richer model that introduces unexplained obstruction may be worse for a precise interaction; a fixed animation may be worse where improvised physical interference is the intended possibility. This comparison is illustrative reasoning, not an engine benchmark. [C-01, C-18]

**Deterministic does not mean understandable.** An unseen temperature, update order or accumulated resource can change an apparently identical action. Conversely, a stochastic response can have learnable conditions without a knowable individual outcome. Separate the rule the player may infer, the state they can observe, and the uncertainty intentionally left unresolved. Do not expose all hidden information merely to make the simulation legible. [C-02, C-14]

### Interactions require explicit state and boundary assumptions

Describe an interaction as an action meeting a state-dependent condition, causing a transition, possibly with a delay or feedback effect. Then connect transitions: the output of one rule can alter the conditions of another. A bounded model can reveal loops, bottlenecks and absorbing states, but its omissions remain omissions. Dormans’s SimWar paper reports scripted-policy simulations and explicitly limits transfer from its reduced model to actual tactical/spatial play. That supports using models to generate questions, not declaring a whole game balanced. [C-08, C-09]

The practical audit asks what can accumulate, leave the modeled region, become reserved, or stop circulating. Koster’s retrospective distinguishes expensive agent searches/pathfinding from an ecology/resource failure associated with hoarding. His later correction is the same witness, not a second independent experiment. The safe transfer is a question: **what happens when participants retain resources, ignore the assumed role, or change which regions are active?** It is not the historical slogan that players inevitably destroy simulated ecosystems. [C-03, C-04]

In an illustrative power–pump–fuel chain, a pump extracts the fuel needed by its own power supply. If usable stock reaches zero and no alternative input exists, the system may enter an absorbing failure state under those defined rules. Whether to allow that outcome is a design choice. A protected restart reserve, manual bypass, external trade or explicit terminal outcome are different proposed contracts—not interchangeable fixes. A free unlimited bypass might remove the scarcity decision the simulation exists to create. [C-04, C-12, C-13]

### Agent behavior: choose the problem before choosing sophistication

Reynolds distinguishes action selection, steering and locomotion, while treating pathfinding as related but separate. This is a useful decomposition for asking whether an agent selected an unsuitable goal, failed to find a route, reacted poorly to nearby obstacles, or could not perform the required movement. It is not a universal architecture or a claim that these three layers produce believable characters. [C-05]

The same paper discusses blending and prioritizing behaviors; weighted influences can oppose each other. A stationary agent can therefore signal a coordination conflict rather than an absent navigation path. The design implication is to author what should win when “approach,” “avoid,” “protect,” or “stay with group” conflict, and what visible behavior should accompany that conflict. The exact arbitration method, weights and update policy remain implementation choices requiring local evaluation. [C-06, C-18]

Agent detail also has an information cost. A rich internal preference model is not necessarily useful when its consequences cannot be distinguished from random behavior. Conversely, revealing an agent’s entire objective stack may destroy deception or discovery. The proposed requirement is interpretable consequences at the level the experience promises, not complete transparency into simulated minds. [C-01, C-02, C-14]

### Observability and bounded intervention

The [Bounded causal probe](../patterns/bounded-causal-probe.md) proposes giving players a limited opportunity to change a relevant condition and inspect the consequence while preserving the real rule. Its causal chain is explicitly incomplete: a contrast can discriminate explanations in a model; people must still notice it, interpret it, transfer it and find the resulting decisions worthwhile. None of those player benefits was demonstrated by this F05 batch. [C-11, C-17]

The inspected F01 correction matters here. Prediction questions must sometimes require different answers, including boundary cases. Repeating a successful action or a refusal does not establish rule understanding. Predicting what is permitted must also be separated from preferring that action. Ordinary state information and access accommodations remain available; only answer-leading prompts may be changed in a separately justified learning design. [C-14; reviewed dependency `GDR-CAND-20261010-F01-PAT-01`, Worked examples]

### Performance policy can alter the simulated world

Factorio’s dated developer account describes a determinism defect requiring a specific combination of generation/mod operations and different core counts. It is not proof that Factorio currently has that defect. It is a concrete warning against treating a seed as a complete description of a concurrent computation. [C-10]

For this topic, the inferred design consequence is broader than debugging: offscreen aggregation, less frequent agent decisions, streaming boundaries, save/resume and overload handling can change outcomes players care about. Specify which relationships must remain equivalent and which may intentionally change. “Offscreen behavior is approximate” is not sufficient if leaving a room makes an exploit possible or removes another player’s recovery path. Performance equivalence across these boundaries is a proposed acceptance question, not a verified implementation technique. [C-15]

## Design choices and alternatives

| Choice | Appropriate question and possible benefit | Cost, failure risk and simpler alternative |
|---|---|---|
| Authored event or compact state machine | Is a small set of outcomes sufficient, or is exact staging central? | Exceptions must be maintained; improvisation may be unavailable. This can be preferable to simulating detail with no useful decision. |
| Rule interaction over explicit state | Do players need to combine a manageable set of affordances in new ways? | Higher-order interactions require boundary and exploit analysis. Reduce the interacting set before adding hidden exceptions. |
| Physical simulation for selected objects | Does force, contact, momentum or placement materially affect action? | Fidelity, stability, presentation and control can disagree. Use constrained or kinematic behavior for parts whose physical freedom adds no intended value. |
| Ecology-like resource model | Do consumption, regeneration, migration or competition create intended choices? | A closed model can stall under storage or offscreen policies; real ecological validity is not established by using animal labels. Abstract stocks/flows may suffice. |
| Rich autonomous agents | Are alternative agent goals and reactions visible and useful? | Arbitration, navigation, debugging and explanation costs may exceed the value. Authored roles or constrained policies can be clearer. |
| Aggregate or intermittent simulation | Which outcomes must survive a change in observation/update scale? | Boundary artifacts and missed interactions may change the rules. Limit fidelity intentionally and audit the transition, rather than treating it as invisible optimization. |

These are conditional inferences or hypotheses, not ranked best practices. Their support is the model/context distinction and the inspected technical accounts; their player and production benefits remain local questions. [C-01, C-04–C-07, C-15, C-18]

## Application process

**Diagnose the promised decision.** Write what an informed player should be able to attempt, what remains uncertain and what outcomes are deliberately outside the promise. Compare against an authored-only baseline. If a new simulated variable changes neither a useful action nor an accepted expressive goal, consider omitting it. [C-01]

**Map the relevant state and interactions.** Record stocks, attributes, ownership, transformations, agents, delays, spatial boundaries and information visibility. Include zero-stock, saturation, simultaneous-action and absent-player cases. Trace multi-rule consequences rather than checking components only in isolation. Treat the diagram as a bounded hypothesis about the implementation, not its proof. [C-04, C-09]

**Choose failure and recovery contracts.** Distinguish welcome surprise, accepted loss, recoverable disruption and prohibited failure. Name whose resources a recovery action may consume and who can trigger it. Preserve an intentional terminal outcome when that is the accepted experience; do not secretly create one in a supposedly recoverable loop. [C-12, C-13, C-16]

**Specify observability without supplying answers.** Identify the facts needed for the actual decision, not every internal field. Preserve unknown causes and uncertain identity across alternative cues. Test language, timing and information load with Presentation and Interaction; do not import numerical accessibility defaults from a different platform. [C-14]

**Prepare a discriminating prototype specification.** Compare the compact/authored alternative with the interacting-rule proposal. Separate simulation correctness, communicated state, permitted interventions and experienced value. Specify varied-answer and boundary probes before collecting outcomes. This paragraph specifies future work; no prototype has been built. [C-11, C-17]

**Evaluate and revise at the right boundary.** Investigate confusing rules, poor cue design, an unhelpful decision, and an expensive implementation as different problems. Narrow or remove the technique when its benefits do not survive the simpler comparison. Changes to models, state persistence or concurrency require fresh implementation authorization and review. [C-15, C-17, C-18]

## Patterns and genre adaptations

`GDR-CAND-20261010-F05-PAT-01`, [Bounded causal probe](../patterns/bounded-causal-probe.md), addresses player-led causal inquiry. `GDR-CAND-20261010-F05-PAT-02`, [Constraint-gated generation with bounded fallback](../patterns/constraint-gated-generation-with-bounded-fallback.md), applies when generated initial conditions can violate a simulation’s declared contract. The companion [Procedural and authored content](procedural-and-authored-content.md) addresses constructing and filtering those conditions.

Reviewed F01/F02/F07 guidance was inspected as recorded in the [dependency ledger](../reviews/full-run-20261010-f05-review-packet.md#reviewed-dependency-inspection). F03’s economy/pattern inventory and W03’s spatial/exploration inventory are unreviewed-context packet reads, not inspected topic bodies or transferred findings. F04 combat/traversal is author-running context only. The inspected F02 costed-probe/rehearsal queue overlaps the causal-probe candidate and remains pending ownership reconciliation, not silently completed by F05. No genre-specific file is supplied or silently substituted; later genre adaptations must state which consequences, uncertainty and failure costs the genre’s actual promise changes. [C-18]

## Examples and counterexamples

### Illustrative worked example: heat, moisture and fuel

A fictional material ignites only when it is dry, contains fuel, and reaches a heat value of at least **3**. This number is an invented local rule for explanation, not a realistic ignition threshold or recommended game setting. The player can inspect dryness and remaining fuel and can add a known amount of heat in a bounded test area. [C-11, C-14]

A useful contrast includes dry fuel at heat 2 (no ignition), dry fuel at heat 3 (ignition), wet fuel at heat 3 (no ignition), and dry empty material at heat 3 (no ignition). The correct answer changes. To test more than memorized labels, use a new material appearance while preserving the stated properties, then change a relevant property while preserving the appearance. Ask what is possible before asking which action the player prefers. These are logical consequences of the illustrative rule, **not executed experiments**. [C-11, C-17]

Now connect ignition to heat transfer and a nearby container. A single isolated result does not establish behavior during concurrent heating, extinguishing, delayed drying or resource consumption. Add those situations only when their decisions matter. A local reset must restore the named state consistently or explain the residual change; resetting visible fire while retaining invisible heat would confound the probe. [C-09, C-12, C-15]

**Counterexample:** a scene whose purpose is costly investigation of an unknown phenomenon may be harmed by a safe reusable test bench. Use one consequential observation, a constrained evidence trail, or no probe. A mystery is not defective merely because it does not reveal the full transition rule. Access to the available evidence remains necessary, but an accommodation need not reveal the solution. [C-11, C-14]

### Creator-account contrasts, not reproduced gameplay

The UO accounts distinguish computational and resource-circulation failures; the Nintendo interview discusses preserving intuitive object affordances while constraining selected properties. Neither establishes that realism, openness or restrictions are universally superior. These are contrasting production problems that motivate testing the actual promise and boundary of a proposed system. [C-03, C-07]

A similarly bounded simulation can correctly expose a stock bottleneck yet miss the tactic that lets a real player avoid it. The SimWar paper’s stated omissions are the strongest counterexample to treating a valid model result as a final balance verdict. [C-08, C-09]

## Failure modes and constraints

**Incentives and exploitation.** A repeated gain is not automatically an exploit; creative production may be the intended loop. The relevant test is whether it violates a declared resource, ownership, fairness or cost contract. Check cycling state through transformations, leaving/re-entering regions, agent distraction, save boundaries and optional expenditure of a mandatory resource. F03 owns economy-specific reconciliation; its actual topic/pattern bodies remain an unresolved dependency. [C-13, C-15, C-18]

**Cascades and shared costs.** A local mistake may be acceptable while a chain that irreversibly consumes someone else’s world is not. Proposed safeguards include bounded propagation, protected shared resources, permission limits and legible responsibility; none is certified for multiplayer here. Recovery can itself be griefed or become a dominant free action. Costs and ownership must be evaluated alongside apparent safety. [C-12, C-16]

**Accessibility and learning demand.** Simultaneous reactions, subtle property cues, memory of delayed causes and rapid interventions can create distinct access demands. A state history, slower opportunity, repeatable explanation or alternative representation may help, but each changes information or time. Preserve equivalent decision facts and intended uncertainty where possible; evaluate with people using the intended routes. No universal text size, cue duration or agent reaction window is proposed. [C-14, C-17]

**Representation, language and ethics.** A simulated preference or social/ecological category is an authored abstraction, not evidence about real populations. Avoid treating culturally loaded group labels as unquestioned behavioral laws. Make causal terms and state descriptions localizable rather than relying on one metaphor or grammatical construction. These are proposed review questions; this batch contains no cross-cultural validation or ethical certification. [C-16]

**Production scope.** Record who owns rule interactions, exceptional states, persistence, debugging explanations and regression review. Model detail creates commitments even when rarely visible. Concurrency and engine-level fidelity require separate technical investigation; this entry supplies requirements to discuss, not a runtime design or performance budget. [C-15, C-18]

## Playtest and validation

**All work below is proposed, not performed.** The inspected F07 evaluation candidate supports separating measurements from constructs; it does not supply F05 results. [C-17]

| Discriminating question | Comparison and procedure | Measures, confounds and decision rule |
|---|---|---|
| Does the probe improve causal inference rather than answer copying? | Compare matched state/cue information with and without an optional bounded intervention. Use changed-answer, boundary and delayed new-context tasks; distinguish prediction from preference. | Record explanations, predictions and choices separately. Counterbalance familiarity and task order; keep accommodations. Narrow/reject if gains occur only on repeated answers or remove desired uncertainty. |
| Does added simulation create useful decisions? | Compare a compact authored model and a richer interacting model under the same intended task and presentation quality. | Examine alternative plans actually used, perceived agency/coherence and unwanted failure, not action count alone. Reject added detail if it changes cost/confusion without the intended value. |
| Does recovery contain harm without erasing stakes? | Contrast declared recovery policies under ordinary mistakes and deliberate misuse, including other affected actors where relevant. | Separate recovery success, resource loss, agency and perceived stakes. Reject a policy that externalizes cost or becomes a dominant costless escape. |
| Do update boundaries preserve the contract? | A separately authorized technical study would replay named cases across streaming, pause/resume, save/load and scheduling variants. | Compare required state relationships and player-visible consequences, not seed equality alone. A divergence may falsify equivalence; a finite passing corpus cannot prove all states. |

Recruitment, sample size, accessibility representation, compensation and consent require a separate study plan. Include people with relevant experience and the access needs actually affected; do not call a convenience sample representative. Before data collection, define acceptable differences from the project’s stated stakes and cost budget rather than inventing a universal threshold. Null or adverse results remain evidence to narrow the proposal. [C-17]

## Claim ledger

Claim IDs are scoped to this artifact. Confidence is confidence in the precise bounded statement, not in a universal player benefit. A hypothesis remains untested even when its technical premises are well supported.

| Claim | Exact material claim and class | Evidence / precise locator | Applicability, confidence reason and unresolved issue |
|---|---|---|---|
| C-01 | `inference` — Fidelity, perceived coherence and useful decisions are separable; extra simulation is not presumptively better. | GDR-SRC-20261010-F05-003, Locomotion/A Simple Vehicle Model; GDR-SRC-20261010-F05-004, object-affordance discussion. | Moderate: defensible conceptual separation, not a comparative efficacy result. Which detail earns its cost is local. |
| C-02 | `inference` — Determinism does not itself make causal structure observable; stable conditional uncertainty can remain intentional. | GDR-SRC-20261010-F05-003, behavior composition; GDR-SRC-20261010-F05-005, Deterministic multithreading; explicit reasoning about hidden state. | Moderate for distinction; no measured player learnability advantage. Needed information depends on the promised decision. |
| C-03 | `practitioner-heuristic` — Koster distinguishes AI search/pathfinding cost from resource-circulation failure under hoarding in UO’s early system. | GDR-SRC-20261010-F05-001, article failure discussion; GDR-SRC-20261010-F05-002, notes 1, 4–5. | Moderate for this firsthand account, not independently reconstructed history. Same author twice; competing recollections not adjudicated. |
| C-04 | `inference` — A systemic audit should include accumulation, sequestration, regeneration and boundary conditions, not only intended circulation. | GDR-SRC-20261010-F05-001–GDR-SRC-20261010-F05-002, failure accounts; GDR-SRC-20261010-F01-08, model construction/discussion. | Moderate as a mechanism-driven audit; completeness and benefit of any particular model remain unknown. |
| C-05 | `observed-example` — Reynolds’s inspected paper separates action selection, steering and locomotion and demonstrates steering using an idealized vehicle model. | GDR-SRC-20261010-F05-003, Introduction; Locomotion; A Simple Vehicle Model. | High for the inspected technical artifact, not a live game observation or universal architecture. |
| C-06 | `practitioner-heuristic` — Reynolds identifies behavior-combination conflicts and discusses blending and prioritization alternatives. | GDR-SRC-20261010-F05-003, Combining Behaviors. | High for reported design reasoning; best arbitration, tuning and player effect remain context-specific. |
| C-07 | `practitioner-heuristic` — Nintendo’s developers describe consistent affordances and selected restrictions intended to meet player expectations. | GDR-SRC-20261010-F05-004, Part 5 object-property and unexpected-solution discussion. | Moderate: creator rationale with identifiable context; comparative understanding or satisfaction not measured here. |
| C-08 | `empirical-evidence` — The 2011 SimWar paper reports reduced-model sessions under artificial policies, while identifying omitted tactical/spatial gameplay. | GDR-SRC-20261010-F01-08, printed pp. 6–7; model/trace figures on printed p. 6. | High for the paper’s computational setting and stated limitation; no human participants, independent replication or real-game balance conclusion. |
| C-09 | `inference` — A model result concerns represented states and policies; it does not certify unmodeled tactics, interactions or enjoyment. | GDR-SRC-20261010-F01-08, Discussion and Conclusion, p. 7. | High for the logical scope limit; adequacy of a proposed model requires discriminating observation. |
| C-10 | `practitioner-heuristic` — Factorio’s dated report describes a generation determinism defect dependent on operations and differing core counts. | GDR-SRC-20261010-F05-005, Deterministic multithreading. | Moderate: firsthand historical technical report, not reproduced or asserted to persist in the current build. |
| C-11 | `hypothesis` — Optional bounded intervention may help players infer a useful causal relation without a complete answer reveal. | GDR-SRC-20261010-F05-003–GDR-SRC-20261010-F05-004 supply mechanism context; reviewed F01 corrected transfer pattern supplies diagnostic cautions, not efficacy. | Low: no matched player study of this recipe. Deliberate uncertainty or irreversibility can make it inappropriate. |
| C-12 | `hypothesis` — Explicit recovery boundaries may contain harmful cascades without removing intended stakes. | GDR-SRC-20261010-F05-001–GDR-SRC-20261010-F05-002 failure context; reviewed F02 challenge and F07 ethical candidate cautions; proposed mechanism. | Low for player/shared-system benefit. Recovery can be exploited or erase the intended decision. |
| C-13 | `inference` — Classify emergent gains against declared resource/ownership/cost contracts rather than treating all repeated gain as exploit. | GDR-SRC-20261010-F01-08, bounded model; explicit design-contract reasoning. F03 packet is overlap context only. | Moderate for distinction; desired contracts are unapproved and economy-specific reconciliation remains open. |
| C-14 | `hypothesis` — Preserve required state facts and access supports while using varied-answer probes and uncertainty-preserving cue alternatives. | Reviewed F01-PAT-01, Worked examples; P01 corrected numerical-scope passages; P02-PAT-02, Recipe §§1–6; exact dependency ledger in packet. | Low for F05 benefit; no standards conformance or cue equivalence certified. Accessibility support is not an answer-leading prompt. |
| C-15 | `hypothesis` — Audit state and consequence equivalence across offscreen aggregation, update, persistence and overload boundaries. | GDR-SRC-20261010-F05-001, cost/workaround discussion; GDR-SRC-20261010-F05-005, determinism and task performance. | Moderate technical rationale, low evidence for a universal audit recipe. No runtime tests performed. |
| C-16 | `hypothesis` — Review shared costs, representation, coercive pressure, language and maintainability alongside systemic opportunity. | Reviewed F07 ethical candidate, scope and refusal/representation distinctions; local proposal, not imported study findings. | Low for particular interventions; relevant populations and shared-world cases untested. |
| C-17 | `hypothesis` — Discriminating comparisons should separate correctness, causal understanding, choice, experience and production cost. | Reviewed F07-TOP-01, measurement/model limits; F01 changed-answer correction; proposed protocols in this entry. | Low for unperformed tests and expected outcomes; moderate methodological rationale. No universal sample or pass threshold. |
| C-18 | `inference` — Specify design behavior and ownership before choosing implementation; genre, spatial, sensory and economy interfaces require their own context. | GDR-SRC-20261010-F05-003, layered technical distinctions; inspected TAXONOMY and domain profile. | Moderate organizational inference; no integration compatibility or adoption approval. Missing dependent bodies remain listed. |

## References

All listed sources were inspected on 2026-10-10 to the stated extent. This is bounded research, not an exhaustive search. Source titles and locators identify historical editions; mutable documentation must be rechecked before implementation. Source repetition across entries does not add independent evidence.

### GDR-SRC-20261010-F05-001

**Raph Koster. [UO’s resource system, part 2](https://www.raphkoster.com/2006/06/04/uos-resource-system-part-2/).** Raph Koster’s author site. Publication/update: 2006-06-04; page also displays 2018-08-06 without a substantive revision explanation.

**Edition / access:** Retrospective account of Ultima Online development/alpha–beta; no current retail build verified. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand retrospective development account.

**Inspected locators:** Article body: paragraphs beginning “First, a bunch of technical details”; “What drove most everything”; and “There were two big problems” (rendered article lines 19–57). Comments and the quoted promotional scenario are not independent observations.

**Claims supported or informing hypotheses in this entry:** C-03; mechanism context C-04/C-12/C-15.

**Limits / independence:** Self-report without recovered telemetry or build reproduction. Source 002 is the same author revisiting the same system, not independent corroboration.

**Rights:** Public copyrighted article; paraphrased; no article text or images redistributed.

### GDR-SRC-20261010-F05-002

**Raph Koster. [Did players destroy the UO ecology?](https://www.raphkoster.com/games/snippets/did-players-destroy-the-uo-ecology/).** Raph Koster’s author site. Publication/update: Original date unknown; updated 2024-08-28.

**Edition / access:** Dated retrospective correction; references alpha/beta-era UO. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand historical correction/practitioner account.

**Inspected locators:** Numbered notes 1, 4, 5 and 8; page updated-date header.

**Claims supported or informing hypotheses in this entry:** C-03; context C-04/C-12.

**Limits / independence:** Same underlying witness as source 001. The Garriott video, derivative article and Simpson economic analysis discussed here were not independently inspected. Historical disagreement is not independently adjudicated.

**Rights:** Public copyrighted text; paraphrase only.

### GDR-SRC-20261010-F05-003

**Craig W. Reynolds. [Steering Behaviors For Autonomous Characters](https://www.red3d.com/cwr/steer/gdc99/).** Game Developers Conference paper, author-hosted HTML. Publication/update: 1999.

**Edition / access:** GDC 1999 paper; not a current engine specification. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original technical/practitioner paper.

**Inspected locators:** Introduction; Locomotion; A Simple Vehicle Model; Combining Behaviors (especially blending/cancellation and prioritization). HTML lines 19–31, 52–80 and 218–231.

**Claims supported or informing hypotheses in this entry:** C-05/C-06; reasoning context C-01/C-02/C-11/C-18.

**Limits / independence:** Algorithmic decomposition and practitioner reasoning, not human-player efficacy evidence or a requirement to use three layers. Referenced earlier studies were not separately inspected.

**Rights:** Author-hosted copyrighted paper; no figures, algorithms or code reproduced verbatim.

### GDR-SRC-20261010-F05-004

**Nintendo; relevant interview speakers Hidemaro Fujibayashi and Takuhiro Dohta. [Ask the Developer Vol. 9, The Legend of Zelda: Tears of the Kingdom — Part 5](https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-part-5/).** Nintendo. Publication/update: 2023-05-09.

**Edition / access:** Prelaunch Nintendo Switch development interview; English translation of Japanese interview; no later patch audit. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand developer interview.

**Inspected locators:** Part 5 discussion of unexpected solutions, what players expect to be possible, movable/fixed objects, and lids on jars; rendered lines 69–87.

**Claims supported or informing hypotheses in this entry:** C-07; reasoning context C-01/C-11.

**Limits / independence:** Creator account of design choices and intended understanding/satisfaction, not a controlled comparison or a hands-on gameplay observation. Other interview parts not imported.

**Rights:** Nintendo copyrighted interview/images; paraphrase only; no media reproduced.

### GDR-SRC-20261010-F05-005

**Rseding / Wube Software. [Friday Facts #415 — Fix, Improve, Optimize](https://www.factorio.com/blog/post/fff-415).** Factorio development blog. Publication/update: 2024-06-14.

**Edition / access:** Factorio 1.1 and then-in-development 2.0 account; not verification of present behavior. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand technical development report.

**Inspected locators:** Deterministic multithreading; Robot task performance (rendered lines 25–39 and 49–63).

**Claims supported or informing hypotheses in this entry:** C-10; reasoning context C-02/C-15.

**Limits / independence:** Reported multi-condition defect and optimization reasoning, not reproduced here. Future-tense fixes in the article are not current verified state. No general speedup or deterministic guarantee inferred.

**Rights:** Public developer article; paraphrased; no code/images redistributed.

### GDR-SRC-20261010-F01-08

**Joris Dormans. [Simulating Mechanics to Study Emergence in Games](https://ojs.aaai.org/index.php/AIIDE/article/download/12477/12336/16005).** Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment 7(3), 2–7; WS-11-19. Publication/update: 2011-10-09.

**Edition / access:** 2011 paper; Machinations / SimWar model, not a playable-build evaluation. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original modeling method and computational simulation report.
DOI: `10.1609/aiide.v7i3.12477`.

**Inspected locators:** Printed pp. 2–4 on model notation and construction; printed p. 6 on scripted-policy simulations; Discussion and Conclusion, p. 7. Screenshot of PDF p. 5 (printed p. 6), Figures 4–7, inspected.

**Claims supported or informing hypotheses in this entry:** C-08/C-09; reasoning context C-04/C-13.

**Limits / independence:** Artificial policies and a reduced resource model omit tactical/spatial gameplay. The 1,000-session simulation setting is the paper’s, not an F05 test or recommended sample. Existing same-work mapping F03-007 ↔ F01-08 remains pending central deduplication.

**Rights:** Publisher-hosted research paper; license scope not independently audited; paraphrase only; paper/figures not redistributed.

## Open questions, coverage and change history

| Assigned subtopic | Treatment achieved | Evidence gap / next discriminating question |
|---|---|---|
| Rule interactions and cascading state | Bounded state/transition and loop analysis; model limits | Which higher-order interaction breaks the declared contract under adversarial input? |
| Ecology | Historical resource circulation, hoarding and agent-cost accounts | No validated biological/ecological model or independent reconstruction of UO history. Which regeneration and storage assumptions fit the proposed decisions? |
| Physical simulation | Fidelity/coherence distinction; simplified locomotion and selective affordances | No solver, collision, deformable-body, fluid or cross-engine benchmark. Which physical degrees of freedom actually improve the intended choice? |
| Agent behavior | Goal/route/steering/locomotion separation and arbitration | No broad cognition, social-agent or population-believability study. What visible evidence distinguishes an intentional priority from a fault? |
| Predictability and emergence | Conditional observability, uncertainty and optional causal probes | No direct player-efficacy study; probe may undermine mystery or commitment. |
| Exploit loops and recovery | Contract-based classification and bounded recovery proposals | F03 economy and F04 action bodies not inspected; shared-world safeguards unvalidated. |
| Simulation cost | Dated implementation constraints; proposed boundary equivalence audit | No measured F05 runtime/memory budget or production saving. When is simpler authored behavior sufficient? |

All rows remain **coverage-open**. Packet-local contradictions `F05-CON-01`, `F05-CON-02`, `F05-CON-04` and `F05-CON-06` remain unresolved or context-dependent. No numerical recommendation is released.

**History:** 2026-10-10 — initial research submission, `0.1.0` / `initial-research-1`; predecessor and supersession null. Author self-review recorded in the packet; independent F05 review not performed. Exact bytes are identified by the detached integrity receipt. Latest canonical IDs, pending allocations and current recovery ledger were not available; no permanent allocation or release is implied.
