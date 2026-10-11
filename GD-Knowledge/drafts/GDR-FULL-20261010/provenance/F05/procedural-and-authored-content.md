---
id: GDR-CAND-20261010-F05-TOP-02
kind: topic
title: Procedural and authored content
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
- procedural content generation
- mixed-initiative authoring
- generative constraints
- seed reproducibility
- content variation and repetition
tags:
- procedural-content
- authored-content
- constraints
- validation
- curation
- reproducibility
- authoring-cost
- coverage-open
related_topics:
- GDR-CAND-20261010-F05-TOP-01
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F05-PAT-02
- GDR-CAND-20261010-F05-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F05-005
- GDR-SRC-20261010-F05-006
- GDR-SRC-20261010-F05-007
- GDR-SRC-20261010-F05-008
- GDR-SRC-20261010-F05-009
- GDR-SRC-20261010-F05-010
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial F05 submission; no prior F05 candidate bytes observed in this conversation; no
  permanent identity allocation.
hash_record: ../reviews/full-run-20261010-f05-integrity.md
---

# Procedural and authored content

> **Draft research candidate — not released, independently reviewed, or approved for implementation.** Version `0.1.0`; revision `initial-research-1`. Application procedures and numerical illustrations are proposals, not adopted studio decisions. No F05 game execution, prototype, participant study or playtest occurred.

## Decision and scope

This entry helps decide **what to author directly, what to generate, what to keep under human control, and how to judge the content that actually reaches a player**. It covers fixed authored material, modular assembly, grammar/rule construction, stochastic selection/search and mixed human–generator workflows. It includes constraints, validation, variation, repetition, seeds, curation and total authoring cost. It does not assume that generation is random, that handcrafted work is inflexible, or that generating more outputs creates more valuable experience. [C-01, C-07, C-13]

A **generative constraint** limits the outputs or construction steps a process may use. A **validator** checks a specified property under a stated model. **Controllability** is the designer’s ability to obtain or preserve intended properties, not merely the presence of many settings. **Variation** can describe different artifacts or different available decisions; **experienced novelty** is a player outcome that those artifact differences do not establish. These are working analytic definitions rather than universal terminology standards. [C-01, C-05, C-07, C-14]

The relevant production choice includes offline generation and curation, runtime generation, and no generation. A reversible working assumption is that an owner can name required properties and distinguish them from preferences. When that distinction is disputed, resolving it is part of design—not something a solver can decide on behalf of the team. Spatial and narrative composition must be coordinated with Worlds and Characters. [C-01, C-14, C-19]

## Core explanation and mechanisms

### Authored and procedural are allocations of work, not opposing quality labels

A generated room may contain carefully authored modules. An authored level may be built using procedural placement. A grammar is itself authored, and an interactive editor can preserve manually placed elements while constructing around them. Tanagra provides an inspectable example of such mixed initiative, but its technical design is not a controlled demonstration that production becomes cheaper. [C-01, C-03, C-13, C-14]

The key questions are who selects the representation, who sets admissible relationships, who makes the final selection, and who owns exceptions. A setting named “variety” is not a substitute for these choices. A compact authored set may be preferable when every instance must carry specific meaning, when repetition is desirable practice, or when the expected content volume does not repay tooling and review costs. [C-01, C-07, C-13]

### What validation can and cannot certify

Gumin’s WFC README defines local pattern conditions and acknowledges possible contradictions. Those local conditions are not a whole-game specification. Tanagra’s represented movement and geometry support stronger reachability reasoning, but still within that model; pinned designer constraints can also leave no solution. These are different guarantees and failure modes, not evidence that one algorithm universally dominates another. [C-02, C-03, C-05]

Use a property ladder to make the scope explicit. The following ladder is a proposed review structure, not a formal standard and not a claim that every project needs every layer. [C-05]

| Property under review | What a matching check could establish | What remains outside that check |
|---|---|---|
| Syntactic or local structural validity | Required fields exist; compatible modules touch; declared local patterns are permitted | An entrance connects to an objective; the objective is meaningful |
| Spatial feasibility | A route exists for a represented movement capability and state | A real player can identify or execute it; inventory or time makes it affordable |
| Task/state feasibility | A path through modeled objectives, keys, resources and irreversible transitions exists | All relevant states were modeled; every optional choice should remain recoverable |
| Rule/content integrity | Required entities, references and declared persistence relationships survive the checked transition | The authored meaning or causal explanation remains understandable |
| Access and presentation coverage | Required messages and controls have specified representations under named configurations | Actual usability, emotional equivalence, comfort or cultural interpretation |
| Experiential and creative fit | A human review can give contextual judgments under a stated brief | Universal fun, durable novelty, population-wide suitability or guaranteed commercial value |

A solver result is conditional on the model and the correctness of the constraint/validation implementation. An automated check may be sound for a narrow property yet irrelevant to the intended decision. Conversely, a validator can reject a legitimate unusual solution because its representation is too restrictive. Include false rejection as well as false acceptance in review. [C-05, C-18]

### Separate dependency structure from its realization

Dormans’s 2010 proposal distinguishes mission dependencies and spatial arrangement, coupling their generation instead of assuming one representation handles both. The transferable principle is narrower than the paper’s genre judgments: **relationships that must hold need an explicit representation, even when layout varies**. It does not follow that every game needs a mission graph or that one ordering should dominate every hybrid experience. [C-04, C-19]

A generated layout may have a geometric route to a goal while placing the only required tool behind the obstacle that requires it. An inventory-aware model may catch that case. It may still miss that an optional action consumes the tool irreversibly, that an agent can destroy it, or that the only available cue is inaccessible. Each addition changes what is being checked, not merely the strictness of an undifferentiated “quality” score. [C-05, C-15, C-17]

### Output distributions are the relevant object, not the seed count

Smith and Whitehead analyze a Launchpad corpus using geometry-derived metrics. In their particular comparison, regular rhythms span more of those metrics than swing/random rhythms. Their leniency measure is not a participant measure of experienced difficulty. The useful contrary case is that increasing apparent randomness need not increase realized variety along the dimensions being evaluated. [C-06, C-07]

The application is to define meaningful output descriptors and inspect the accepted distribution, including clusters, holes and extremes. Then test whether those descriptors correspond to experienced differences. Different texture placements or byte hashes may leave the same decision repeated; repeated geometry may support different decisions because state or goals differ. Neither conclusion can be read directly from a uniqueness counter. [C-07, C-20]

Filtering also changes the distribution. As a purely mathematical illustration, let `X` be a generated candidate and `A` its acceptance event. For a candidate category `B` with `P(A) > 0`, the delivered share after rejection is `P(X in B | A)`, not necessarily `P(X in B)`. If a fallback is delivered with share `f`, the final distribution additionally mixes in that fallback’s distribution. This identity does not assume independent retries or provide an acceptance rate. It explains why the audit should include rejected, repaired, accepted and fallback content rather than looking only at initial weights. [C-08]

**Counterexample to maximum novelty:** a recurring form can support recognition, deliberate practice, comparison or thematic cohesion. Novelty is not an unconditional quality target. A generator that removes every recognizable structure may make learning or interpretation harder; that consequence is a hypothesis to test, not a measured result in this batch. [C-07, C-20]

### Controllability, repair and bounded failure

Tanagra’s handling of user-placed geometry gives a concrete reason to distinguish protected choices from adjustable material. An unsatisfied request should not be quietly “fixed” by discarding a protected authored condition. Tessera’s version-6 guidance describes backtracking, step limits/retries and constraint-related performance concerns; these mechanisms do not, by themselves, guarantee a total completion deadline. [C-03, C-09, C-14]

The proposed [Constraint-gated generation with bounded fallback](../patterns/constraint-gated-generation-with-bounded-fallback.md) therefore adds an end-to-end policy: protect hard requirements, identify permitted repairs, bound the whole generation/validation/retry process, and use an applicable validated fallback or stop. This is a synthesis, not an observed off-the-shelf guarantee. A fallback has to meet the current contract; a familiar static room is not automatically valid for the current movement capability, inventory or access settings. [C-10, C-15]

An important opposing case is a contract that excludes the most interesting content. Preserve that disagreement instead of treating successful constraint satisfaction as evidence that the requirements were wise. During authoring, explain conflicting constraints and let the authorized designer revise the brief; do not silently weaken a hard requirement at runtime. [C-05, C-14]

### Seeds are labels inside a reproduction contract

Factorio’s historical concurrency account shows that generation behavior can depend on more than a seed and settings displayed to a player. The inferred requirement is a **reproduction bundle**: generator and content versions, relevant configuration, initial state, random-stream policy and ordering, repair/fallback policy, and any platform or dependency condition known to affect the result. Record the actual produced artifact when exact historical recovery matters and policy permits it. [C-11, C-12]

A seed alone is not proof that two people saw identical content, and identical content is not proof that they experienced the same task. Different abilities, prior information, systemic state or presentation can change what is possible. Separate content reproducibility, simulation replay and equivalent player opportunity. None is certified by this entry. [C-12, C-15, C-17]

### Authoring cost must include displaced work

A proposed total-cost comparison includes representation/tool development, reusable assets, constraints, debugging, generation compute, validation, curation, access/localization review, integration, support and maintenance after rule changes. Authored work also has reuse and tooling costs; compare matched output requirements rather than an unassisted manual baseline against a heavily supported generator. [C-13]

The inspected papers and developer accounts describe capabilities and engineering tradeoffs. This batch did not inspect a controlled end-to-end productivity comparison establishing a universal saving. A claim that a generator saves time must state the workload, personnel, quality bar, amortization horizon and maintenance obligations. Reduced placement effort can coexist with increased review or exception work. [C-13, C-14]

## Design choices and alternatives

| Workflow | Where it may fit | Control, cost and contrary case |
|---|---|---|
| Directly authored instances | Specific staging, meaning, predictable exposure or modest content volume | High instance control, recurring editing cost; a reusable authored set may outperform a generator for the actual brief. |
| Modular authored assembly | Repeated structural needs with known compatible pieces | Control rests in modules and interfaces; repetition or awkward seams may dominate. Fewer modules with stronger contextual differences can be preferable to many cosmetic variants. |
| Grammar/rule generation | Dependencies and transformation rules can be represented explicitly | Expressivity is shaped by authored rules; exceptions can become difficult. A graph method is unnecessary when a small curated sequence suffices. |
| Stochastic selection or search | Many acceptable outputs exist and variation/search is worth its cost | Output bias, rejection and extremes need analysis. More random input does not guarantee more experienced novelty. |
| Mixed-initiative construction | Designers need to preserve selected choices while exploring alternatives | Protected decisions, conflict reporting and undo/revision require design effort. Repeated negotiation with a solver can be slower than direct editing. |
| Offline generation plus curation | Runtime certainty and human review matter more than unlimited fresh output | Storage, curation and distribution still cost; an authored fallback must remain compatible with later rules. |
| Runtime generation with validation | New configurations serve a clear experience and failures have acceptable handling | Requires bounded complete processing, valid fallback/stop behavior and an exposure audit. Do not adopt merely because generation itself is fast. |

These are proposed conditional choices, not comparative rankings. A hybrid can use different workflows at different content layers while keeping a single declared ownership and validation contract. [C-01, C-05, C-07, C-10, C-13, C-14]

## Application process

**Frame the required experience and content unit.** State what must vary, what should repeat, what must remain authored and what a valid instance means. Distinguish a room, a session, a task chain and an evolving world; a validator for one does not silently cover the others. Compare with a smaller curated/authored alternative. [C-01, C-05, C-13]

**Specify hard requirements, preferences and protected choices.** A required route, a desired degree of variety and a pinned story event should not be treated as interchangeable numeric scores. Mark the context in which each requirement applies and who may change it. Include contradictions rather than assuming a solution always exists. [C-05, C-14]

**Choose the representation and control surface.** Expose settings that have a demonstrable relation to meaningful output properties. Retain the ability to inspect and revise unexpected interactions. When a designer cannot explain which requirement caused rejection, treat that as a tool/authoring issue, not proof that the desired content is impossible. [C-04, C-07, C-14]

**Plan validation and failure handling together.** Use checks appropriate to state, abilities, resources and permitted mutations. Bound generation, repairs, validation and retries collectively. Specify what happens when no candidate or compatible fallback can satisfy the contract; a safe refusal to generate can be preferable to an invalid forced output. No universal time or retry limit is supplied. [C-05, C-09, C-10, C-15]

**Inspect the content distribution actually delivered.** Keep the distinction between attempted, rejected, repaired, curated and fallback instances. Examine rare conditions and frequent clusters, then compare player-facing decision structures rather than only geometric or byte uniqueness. Account for session history where repetition matters. [C-06–C-08, C-20]

**Evaluate experience and full production cost separately.** Prepare player comparisons of comprehension, opportunities, repetition and fit; prepare author comparisons of time, errors, rework and maintenance. Neither content validity nor an author’s excitement at a tool demonstrates the other outcomes. Revise the contract or return to authored/curated content when the benefit fails to appear. [C-13, C-17, C-18]

## Patterns and genre adaptations

`GDR-CAND-20261010-F05-PAT-02`, [Constraint-gated generation with bounded fallback](../patterns/constraint-gated-generation-with-bounded-fallback.md), is the primary reusable technique. `GDR-CAND-20261010-F05-PAT-01`, [Bounded causal probe](../patterns/bounded-causal-probe.md), can matter when generated situations must allow players to learn stable system relations, but is not required for every generator. The companion [Simulation and systemic behavior](simulation-and-systemic-behavior.md) addresses changes after construction.

The reviewed F02/F07 methodological limits and F01/P01/P02 corrections are recorded in the [dependency ledger](../reviews/full-run-20261010-f05-review-packet.md#reviewed-dependency-inspection). W03’s exploration/composition topic bodies and F03’s resource/progression bodies were not inspected; their packet inventories are contextual dependency information only. This entry does not substitute for those domains. No genre file is generated; one-file-per-genre adaptations remain separate work, and this topic does not transfer the older papers’ broad genre-value judgments. [C-16, C-19]

## Examples and counterexamples

### Illustrative worked example: a generated relay route

A fictional task asks the player to restore a relay. The authored contract requires an exit route and at least one feasible completion from the starting state using an accessible tool. The generator may vary geometry and optional rewards, but the required tool and an authored information panel are protected. This is an invented specification, not an approved studio rule. [C-05, C-14]

Consider three **synthetic labels, not executed seeds**. `relay-alpha` puts the tool before its locked gate and leaves enough charge to activate the relay. `relay-beta` has connected corridors but puts the tool behind the gate it opens. `relay-gamma` puts the tool in reach, yet an optional machine can consume the only charge needed for completion. These examples show why spatial connectivity, dependency feasibility and later state viability are distinct questions. [C-05, C-15]

`relay-beta` violates the stated initial-completion contract. `relay-gamma` may or may not violate it: the initial task is solvable, but a later choice can make it unsolvable. The team must decide whether the promise is “a solution exists initially,” “an informed player can avoid failure,” or “completion remains recoverable after every permitted optional expenditure.” These are materially different constraints. Do not insert the third as an invisible universal requirement. [C-05, C-15]

Possible responses include reserving charge for the objective, adding a visible recovery source, disclosing the opportunity cost and allowing terminal failure, or removing the optional machine. These alter agency, scarcity, authorship and implementation burden differently. A generic repair that moves the protected information panel is not authorized just because it improves a numeric score. [C-10, C-14, C-15]

The proposed fallback is a curated relay layout reviewed under the same capability/resource/access contract, selected before the runtime budget expires. If a later rules update makes that layout invalid, the fallback is stale and must not be assumed safe. If the same layout appears repeatedly, assess the resulting experience rather than counting every generation request as unique content. [C-08, C-10, C-12, C-20]

### Strongest counterexample: the validator erases a valuable possibility

Suppose the intended experience values improvised physical solutions. A route validator recognizes only the designer’s expected walking route and rejects a layout that permits a legitimate object-based solution. More aggressive validation could then reduce useful variety. The correction is to reconcile the representation with the intended contract, or permit an explicit human review path during authoring—not to claim the content was intrinsically invalid. This is an illustrative falsifying case, not a measured frequency of validator error. [C-05, C-18]

A second counterexample is a short, tightly authored experience whose impact depends on exact placement and recurrence. A generator and fallback system might be more work while weakening its intended structure. Authored content is a legitimate endpoint, not a failed procedural prototype. [C-01, C-13, C-19]

## Failure modes and constraints

**Local validity mistaken for global fit.** Adjacent pieces can be compatible while objectives, supplies or needed information are unreachable. Conversely, a coarse whole-level score may penalize intentional asymmetry. Write the property and its scope alongside every claim of validity. [C-02–C-05]

**Hidden distribution collapse.** Repair rules and fallback selection can repeatedly lead to the same decision structure. Sampling only attractive handpicked outputs hides this failure. Record exposure categories and history, but do not declare a corpus representative merely because it is large. [C-07, C-08, C-20]

**Adaptive generation that mistakes behavior for preference.** Repeated combat, cautious movement or fast completion can have several explanations. Dormans’s adaptation discussion is a proposal, not proof of an enjoyment classifier; the reviewed F02/F07 distinctions are retained. Prefer explicit control or narrowly justified adaptation, and do not infer wellbeing, consent or motivation from a convenient proxy. [C-16]

**Accessibility, localization and semantic validity.** Generated content can vary the amount and timing of reading, motor precision, navigation load and cue ambiguity. Test combinations that the product actually intends to support, including translated labels and descriptions with context-sensitive grammar. Do not treat a solver’s movement model as representing all players. Human review must examine culturally loaded combinations and the meaning of what is generated, not just token presence. These are proposed obligations without a cross-cultural efficacy dataset in this batch. [C-17]

**Production and rights.** Inputs, reusable modules, generated combinations and curator corrections need provenance and an authorized owner. Do not assume a public example, supplied image or model output grants distribution rights. This entry does not evaluate generative-AI training/data licensing, legal compliance or open-ended text/image generation; those are explicit research gaps, not silently covered by tile-generation evidence. [C-13, C-17, C-19]

**Simulation and maintenance.** A valid initial world can become invalid through destruction, agent actions, inventory loss or rule/version changes. Decide what persists, what can be regenerated and what must remain an authored historical fact. Do not regenerate away a player’s commitment or stored construction without an explicit product-level decision. [C-12, C-15, C-19]

## Playtest and validation

**Proposed only — no seeds were executed, outputs generated, players recruited or author productivity tests run.** Local Markdown checks reported in the packet are not content-generator validation. [C-18]

| Question | Proposed comparison and controls | Measures and falsifying outcome |
|---|---|---|
| Does the validator match the required property? | Use independently reviewed known-valid, known-invalid and disputed cases; include stateful tool/charge cases and alternative legitimate solutions. A separate implementation team must later execute them. | Track false acceptance, false rejection and unknown/unmodeled cases separately. Reject a “complete validator” claim when a required state or legitimate solution is omitted. |
| Does generated variation produce different useful decisions? | Compare matched authored, uncurated and curated/generated sets with similar presentation and task demands. Control prior exposure and avoid revealing seed labels. | Examine plans and alternatives, repetition judgments, comprehension and intended experience. Narrow the novelty claim if only cosmetic differences or extra task burden change. |
| Does fallback preserve acceptable experience and bounded cost? | Include ordinary success, repair, exhaustion and stale-fallback conditions under named capability/access profiles. Test the entire process, not only construction time. | Record completion latency, invalid delivery, fallback exposure and lost opportunities. Reject deployment when the contract cannot be met or fallback repetition defeats the brief. |
| Does the workflow save author effort at matched quality? | Compare experienced authors and less-experienced authors under equivalent briefs, assets and quality review; include later rule changes and rework. | Count setup, iteration, rejected output, curation, localization/access review and maintenance. Withdraw savings claims when costs are merely shifted or the accepted quality bar differs. |

Choose participants, tasks, stopping rules and meaningful thresholds prospectively for the actual use. Include people affected by the movement, sensory, language or cognitive demands under study; do not claim population coverage from unspecified samples. Record adverse and null findings. More generated artifacts are not a substitute for independent assessment of what their measures mean. [C-17, C-18]

## Claim ledger

Claim IDs are scoped to this artifact. Confidence is confidence in the precise bounded statement, not in a universal player benefit. A hypothesis remains untested even when its technical premises are well supported.

| Claim | Exact material claim and class | Evidence / precise locator | Applicability, confidence reason and unresolved issue |
|---|---|---|---|
| C-01 | `inference` — Authored, modular, grammar, stochastic and mixed workflows allocate different decisions; no workflow has an unconditional quality advantage. | GDR-SRC-20261010-F05-007, mission/space method; GDR-SRC-20261010-F05-008, §§III/V; analytic definitions in this entry. | Moderate for the distinction; comparative value and volume needs are local and untested. |
| C-02 | `observed-example` — The inspected WFC README specifies local pattern conditions and allows contradiction/failure, not a complete game-validity contract. | GDR-SRC-20261010-F05-009, C1/weak C2, contradiction paragraph and Algorithm. | High for documented scope; no code/build execution or verification of commercial uses. |
| C-03 | `observed-example` — Tanagra’s represented movement/geometry and protected designer choices define its constraint solution space, which can be unsatisfiable. | GDR-SRC-20261010-F05-008, §III p. 203; §V p. 205; §VIII pp. 210–211; §§X–XI. | High for the inspected system description; not every player’s capabilities or a human productivity result. |
| C-04 | `observed-example` — Dormans’s 2010 method distinguishes mission dependencies from spatial realization and couples their generation. | GDR-SRC-20261010-F05-007, §2 and §§4–6; PDF p. 6 Figures 8–9. | High for the illustrated method; not a universal requirement for all genres/content units. |
| C-05 | `inference` — A validation result covers only its specified property, represented states and implementation assumptions; both false acceptance and false rejection matter. | GDR-SRC-20261010-F05-008, represented movement and constraint search; GDR-SRC-20261010-F05-009, local conditions; explicit logical scope analysis. | High for scope limit; the proposed property ladder is not a formal standard or complete verification method. |
| C-06 | `empirical-evidence` — Launchpad’s sampled expressive range differs by rhythm/critic settings; regular rhythms span more of the selected metrics in the reported comparison. | GDR-SRC-20261010-F05-006, §§4.3–4.5, PDF pp. 4/6, Figures 6/7/11. | High for the reported computational corpus, not human novelty or difficulty. Metric-specific; authors’ mechanism explanations remain hypotheses. |
| C-07 | `inference` — Artifact counts, random inputs and geometric metrics do not themselves establish useful decision variety or experienced novelty. | GDR-SRC-20261010-F05-006, §2 and §5; metric/experience distinction; reviewed F07 measurement cautions. | High for non-equivalence; a validated mapping to player experience remains missing. |
| C-08 | `inference` — Acceptance, repair and fallback alter the delivered distribution; initial sampling weights alone do not describe exposure. | GDR-SRC-20261010-F05-006, §4.5; conditional-probability illustration in this entry. | High for the conditional identity; no empirical acceptance rate, independence assumption or recommended quota. |
| C-09 | `practitioner-heuristic` — Tessera 6 guidance describes backtracking, step-limit retries and constraint-related costs, not a bound on a complete game pipeline. | GDR-SRC-20261010-F05-010, Backtracking, Errors, Performance. | Moderate for the maintainer’s context; no independent benchmark, universal speedup or deployment recommendation. |
| C-10 | `hypothesis` — An end-to-end generation/validation/retry budget with an applicable validated fallback or stop may reduce invalid delivery without indefinite waiting. | GDR-SRC-20261010-F05-008, no-solution cases; GDR-SRC-20261010-F05-009, contradictions; GDR-SRC-20261010-F05-010, retry guidance. | Low for full player/production benefit; requires correctly scoped validators and a valid fallback. No system built or measured. |
| C-11 | `practitioner-heuristic` — Factorio’s 2024 account describes a multi-condition generation determinism fault involving differing core counts. | GDR-SRC-20261010-F05-005, Deterministic multithreading. | Moderate historical firsthand report; no claim the defect remains or that F05 reproduced it. |
| C-12 | `inference` — Reproduction needs a declared version/state/configuration/order contract; seed equality alone does not establish identical content or opportunity. | GDR-SRC-20261010-F05-005, historical defect; GDR-SRC-20261010-F05-008, model scope; explicit reasoning. | High for logical distinction, moderate for proposed bundle adequacy. Exact requirements depend on implementation. |
| C-13 | `hypothesis` — Compare full lifecycle authoring costs at matched requirements; generation may move work rather than reduce it. | GDR-SRC-20261010-F05-008, system/limitations; GDR-SRC-20261010-F05-010, debugging/performance guidance; proposed accounting comparison. | Low for savings in any application: no controlled total-cost comparison inspected. Cost categories are proposed, not an audited studio budget. |
| C-14 | `hypothesis` — Separate protected choices from preferences and explain conflicts; more controls alone need not improve effective author control. | GDR-SRC-20261010-F05-008, §VIII and §§X–XI; GDR-SRC-20261010-F05-007, grammar representation. | Moderate technical rationale, low human workflow evidence. Negotiation/rework may exceed direct authoring. |
| C-15 | `hypothesis` — Define validity over the intended state horizon, including allowed systemic changes, instead of silently promising perpetual recoverability. | GDR-SRC-20261010-F05-007, dependency structure; GDR-SRC-20261010-F05-008, model scope; companion simulation topic C-09/C-12. | Low for any protection policy; logical distinction is strong. Initial solvability and all-state recoverability differ. |
| C-16 | `hypothesis` — Do not infer preference or wellbeing from performance alone when adapting content; consider explicit controls and discriminating evidence. | GDR-SRC-20261010-F05-007, §7 adaptation proposal; reviewed F02 challenge and F07 evaluation/ethics distinctions. | Low for any adaptive policy; no player-preference classifier validated in this batch. |
| C-17 | `hypothesis` — Evaluate generated combinations under relevant access, language and cultural contexts; formal content checks do not establish human suitability. | Reviewed P01 corrected scope, P02 cue-alternative recipe and F07 ethical/evaluation candidates; proposed F05 reviews. | Low for particular accommodations or outcomes; no conformance, cross-cultural validation or legal determination. |
| C-18 | `hypothesis` — Discriminating tests should include false rejections, runtime exhaustion, repeated exposure and matched-quality author comparisons. | GDR-SRC-20261010-F05-006, expressive-range method; GDR-SRC-20261010-F05-008–GDR-SRC-20261010-F05-010, constraint/failure context; reviewed F07 method. | Low for unperformed tests; no universal sample, latency target or effect guarantee. |
| C-19 | `inference` — Generation rules do not authorize changes to narrative meaning, stored player commitments, genre guidance or implementation ownership. | Inspected TAXONOMY/profile and dispatch; W03/F03 packets used only for missing-body/ownership context. | Moderate workflow inference; actual design adoption and interdomain agreements remain unapproved. |
| C-20 | `hypothesis` — Curation should examine exposure and meaningful repetition rather than maximize uniqueness; distribution-aware curation merits separate follow-up. | GDR-SRC-20261010-F05-006, §§2/4.5/5; proposed experience bridge. | Low for player benefit; repetition may be desirable. Additional pattern work is queued, not released or silently expanded. |

## References

All listed sources were inspected on 2026-10-10 to the stated extent. This is bounded research, not an exhaustive search. Source titles and locators identify historical editions; mutable documentation must be rechecked before implementation. Source repetition across entries does not add independent evidence.

### GDR-SRC-20261010-F05-005

**Rseding / Wube Software. [Friday Facts #415 — Fix, Improve, Optimize](https://www.factorio.com/blog/post/fff-415).** Factorio development blog. Publication/update: 2024-06-14.

**Edition / access:** Factorio 1.1 and then-in-development 2.0 account; not verification of present behavior. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand technical development report.

**Inspected locators:** Deterministic multithreading; Robot task performance (rendered lines 25–39 and 49–63).

**Claims supported or informing hypotheses in this entry:** C-11/C-12.

**Limits / independence:** Reported multi-condition defect and optimization reasoning, not reproduced here. Future-tense fixes in the article are not current verified state. No general speedup or deterministic guarantee inferred.

**Rights:** Public developer article; paraphrased; no code/images redistributed.

### GDR-SRC-20261010-F05-006

**Gillian Smith and Jim Whitehead. [Analyzing the Expressive Range of a Level Generator](https://www.pcgworkshop.com/archive/smith2010analyzing.pdf).** ACM, PCGames 2010 workshop, Monterey. Publication/update: 2010-06-18.

**Edition / access:** 2010 workshop paper; Launchpad generator. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original computational evaluation/method paper.
DOI: `10.1145/1814256.1814260`.

**Inspected locators:** §2 Analytical Approach; §3 Launchpad; §§4.1–4.5, especially PDF pp. 4 and 6, Figures 6, 7 and 11; §5 Discussion. Screenshots of PDF pp. 4 and 6 inspected.

**Claims supported or informing hypotheses in this entry:** C-06; reasoning and hypotheses C-07/C-08/C-18/C-20.

**Limits / independence:** Generated-level corpus, with 10,000 levels per plotted sample unless otherwise stated; geometry-derived metrics, not participants or validated experienced difficulty. Same research lineage as source 008; no independent human replication.

**Rights:** ACM copyright notice inspected; paraphrase and bibliographic reference only; PDF/figures not redistributed.

### GDR-SRC-20261010-F05-007

**Joris Dormans. [Adventures in Level Design: Generating Missions and Spaces for Action Adventure Games](https://www.pcgworkshop.com/archive/dormans2010adventures.pdf).** ACM, PCGames 2010 workshop, Monterey. Publication/update: 2010-06-18.

**Edition / access:** 2010 workshop paper; proposed mission/space grammar workflow. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original generative-method paper.

**Inspected locators:** §2 Missions and Spaces; §§4–6 graph/shape grammar construction and coupling; §7 discussion of adaptation; §8 Conclusions; PDF pp. 2, 4–8. Screenshot of PDF p. 6, Figures 8–9, inspected.

**Claims supported or informing hypotheses in this entry:** C-04; context C-01/C-14/C-15/C-16.

**Limits / independence:** Method and illustrated structures, not evidence of universal genre quality, automatic preference recognition or reduced total authoring cost. Same author as the reused 2011 source, a distinct paper rather than independent replication.

**Rights:** ACM copyright notice inspected; paraphrase only; no source figures or full paper redistributed.

### GDR-SRC-20261010-F05-008

**Gillian Smith, Jim Whitehead and Michael Mateas. [Tanagra: Reactive Planning and Constraint Solving for Mixed-Initiative Level Design](https://www.researchgate.net/publication/224242275_Tanagra_Reactive_Planning_and_Constraint_Solving_for_Mixed-Initiative_Level_Design).** IEEE Transactions on Computational Intelligence and AI in Games 3(3), 201–215. Publication/update: Printed issue: 2011-09; printed publication date: 2011-09-14.

**Edition / access:** 2011 journal article, author-uploaded full text (page identifies Gillian Smith upload, 2014-09-06); not the distinct 2010 Tanagra paper. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original mixed-initiative system/expressivity paper.
DOI: `10.1109/TCIAIG.2011.2159716`.

**Inspected locators:** §III Level Representation, p. 203; §V System Overview, p. 205; §VIII constraint search, pp. 210–211; §§IX–XI, pp. 211–214, on expressivity and limitations. Text inspected, not figure pixels.

**Claims supported or informing hypotheses in this entry:** C-03/C-05; context C-01/C-10/C-12/C-13/C-14/C-15/C-18.

**Limits / independence:** Institutional PDF route failed; recovered author-uploaded article text matches title/authors/printed issue/DOI, but publisher-byte equivalence was not verified. Landing metadata says October 2011; printed issue says September. Playability is relative to represented movement/geometry, not all player abilities or human productivity evidence.

**Rights:** IEEE copyrighted article; no full text, figures or screenshots redistributed.

### GDR-SRC-20261010-F05-009

**Maxim Gumin. [WaveFunctionCollapse — repository README](https://github.com/mxgmn/WaveFunctionCollapse).** Author’s public GitHub repository mxgmn/WaveFunctionCollapse. Publication/update: Publication/update date unknown.

**Edition / access:** Mutable master-branch README inspected on the access date; commit hash not captured. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Creator-maintained technical documentation.

**Inspected locators:** README opening: local-similarity C1 and weak C2; contradiction paragraph; Algorithm; Tilemap generation (rendered lines 212–247).

**Claims supported or informing hypotheses in this entry:** C-02/C-05; context C-10/C-18.

**Limits / independence:** README inspection, not source-code execution or independent verification of listed commercial uses. Claims concern documented local constraints and failure possibility, not whole-game solvability. Tessera shares this algorithmic lineage.

**Rights:** Repository code/assets licensing not audited; no code, assets or screenshots copied; documentation paraphrased.

### GDR-SRC-20261010-F05-010

**BorisTheBrave / Tessera documentation maintainer. [Quality, Performance and Debugging](https://www.boristhebrave.com/docs/tessera/6/articles/quality.html).** Tessera official documentation. Publication/update: Publication/update date unknown.

**Edition / access:** Documentation version 6 URL; exact minor release and commit unknown. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand tool guidance.

**Inspected locators:** Backtracking; Errors; Performance, especially Step Limit/retry, fixed-seed diagnosis and path-constraint advice (rendered lines 9–49).

**Claims supported or informing hypotheses in this entry:** C-09; context C-10/C-13/C-18.

**Limits / independence:** Vendor guidance, not an end-to-end latency benchmark or universal authoring-cost result. Debug advice to relax constraints is not permission to remove a game’s required properties. WFC derivative family, not an independent replication.

**Rights:** Public documentation; licensing not separately audited; paraphrase only.

## Open questions, coverage and change history

| Assigned subtopic | Treatment achieved | Evidence gap / next discriminating question |
|---|---|---|
| Generative constraints | Local rules, mission/state requirements, protected choices and unsatisfiable cases | Which constraints encode real requirements, and which unnecessarily suppress legitimate solutions? |
| Validation | Property-specific scope and state horizon; false acceptance/rejection | No validator executed or end-to-end guarantee certified. Which omitted state invalidates the current model? |
| Variation and repetition | Sampled expressive range, accepted/fallback distributions, meaningful recurrence | No direct longitudinal novelty or repetition study. Which measured content differences matter to players? |
| Controllability | Mixed-initiative pinning, preferences, conflict explanation and alternatives | No controlled author study for these proposed controls. Does negotiation with the tool cost more than manual work? |
| Seed reproducibility | Version/state/order bundle, historical concurrency countercase | Exact current generator/tool builds and cross-platform replay are not verified. What bundle is sufficient for the actual implementation? |
| Curation and generated extremes | Proposed bounded failure/fallback and exposure review | No measured fallback suitability or bias; false rejection may exclude valuable extremes. |
| Authoring cost | Matched-requirement lifecycle comparison | No demonstrated universal saving; setup/maintenance and access/localization costs need measurement. |
| Authored/procedural mixtures | Distinct workflow choices and explicit human ownership | W03 composition and F03 resource bodies missing; modern open-ended generative AI and automated cultural review not researched. |

All subtopics remain **coverage-open**. Packet-local issues `F05-CON-03` through `F05-CON-06` remain visible. Further distribution-aware curation and mission-to-space work is queued subject to ownership/child-key allocation, not included as additional patterns.

**History:** 2026-10-10 — initial research submission, version `0.1.0`, revision `initial-research-1`; predecessor and supersession null. Author self-review only; independent F05 review and actual-host retrieval tests remain pending. Exact bytes are recorded in the detached integrity receipt. No canonical/repository/Project-source change or release occurred.
