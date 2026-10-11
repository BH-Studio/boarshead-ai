# F05 independent bounded review

Date 2026-10-11. Disposition: retain four provisional research drafts with two narrow clarifications and open evidence/integration conditions. This is not release, human approval, canonical allocation, implementation authority or overall Gate D/E clearance.

## Findings and selection

Complete Library reads recovered all four candidates, packet and integrity receipt. All six byte counts match Library metadata; independently recomputed SHA-256 for the four candidates and packet matches the receipt and handoff inventory. All candidate text was reviewed across the simulation/causal-probe and procedural/algorithm passes. Full packet scope, claim ledgers, source records, coverage, conflicts and history inspected. Inventories preserve Library identities and original hashes.

Select two corrected files and two unchanged originals:
- corrected/topics/procedural-and-authored-content.md
- corrected/patterns/constraint-gated-generation-with-bounded-fallback.md
- simulation-and-systemic-behavior.md (unchanged)
- bounded-causal-probe.md (unchanged)

Corrections:
1. The fallback example previously exhausted the overall budget before starting fallback work, contradicting its own complete-budget requirement. It now exhausts only candidate work while preserving a reserve for fallback validation/selection and delivery or stopping. Recipe explicitly reserves that work and does not claim an already-missed total deadline is met.
2. `P(X in B | A)` describes accepted candidates from a specified candidate pool. It does not automatically describe one delivered result per request under heterogeneous contexts, retry ordering, repair or selection. The topic now states the sampling unit and distinguishes actual non-fallback/fallback delivery distributions. No independent-retry assumption or empirical distribution is invented.

Both are reasoning/illustration corrections, not changes to primary-source findings. Stable IDs, version 0.1.0, draft and null approvals retained. New revision/predecessor metadata and appended history identify selected bytes. Original packet/receipt remain unchanged historical snapshots. New selection receipt governs corrected hashes.

## Source scope and calibration

Independent primary spot checks:
- [Koster, UO ecology correction](https://www.raphkoster.com/games/snippets/did-players-destroy-the-uo-ecology/), notes 1, 4–5: supports the author's distinction between agent computational cost and hoarding-induced resource circulation failure. F05 correctly treats the two Koster records as one witness and does not independently settle competing historical recollections.
- [Reynolds, Steering Behaviors](https://www.red3d.com/cwr/steer/gdc99/), Introduction, Locomotion and Combining Behaviors: supports the layered motion discussion and cancellation/prioritization rationale. It is a scoped technical account, not universal agent architecture or player-efficacy evidence.
- [Wube, Friday Facts 415](https://www.factorio.com/blog/post/fff-415), Deterministic multithreading: the defect depends on multiple generation/mod operations and differing core counts. F05 correctly treats this as historical reported behavior, not a reproduced/current defect or proof of every proposed reproduction-bundle field.
- The algorithm pass independently checked [WFC README](https://github.com/mxgmn/WaveFunctionCollapse), [Tessera v6 guidance](https://www.boristhebrave.com/docs/tessera/6/articles/quality.html), [Tanagra author-uploaded paper](https://www.researchgate.net/publication/224242275_Tanagra_Reactive_Planning_and_Constraint_Solving_for_Mixed-Initiative_Level_Design), and [Smith/Whitehead expressive-range paper](https://www.pcgworkshop.com/archive/smith2010analyzing.pdf). Their local-constraint, protected-geometry, retry-limit and metric-specific corpus claims support the bounded wording. See ALGORITHM_REVIEW.md for precise locators and limitations when included.

Nintendo/Dormans context was assessed against candidate source bindings and earlier reviewed source scope; not every primary passage independently rechecked in this pass. No source game, generator, solver, raw corpus or runtime was executed. Mutable documentation has no captured commit guarantee. This remains source spot-checking, not exhaustive claim authentication.

The 55 claims distinguish technical/documentary observation, computational reports, inference, practitioner reasoning and hypotheses. Modeling results and sampled output metrics do not establish player enjoyment, useful novelty, accessibility or savings. Both complete patterns remain low-confidence benefit hypotheses, with credible simpler alternatives and conditions for rejecting them. No fabricated playtests, generator runs, empirical acceptance rates or deployment results found.

## Logic, arithmetic and practical constraints

Independently asserted the invented transfer cases: capacity 5, source 3, destinations 4/5/2 allow 1/0/3 units; closed valve permits zero. Ignition cases obey the stated conjunction of dryness, fuel and heat at least 3. These are synthetic arithmetic/Boolean checks, not simulations or participant evidence.

Causal probe distinguishes changed answers, presentation changes, prediction/preference, ordinary information and needed accommodations. It explicitly limits inference from stochastic outcomes, uncontrolled state and resets that preserve hidden consequences. Neither a correct response nor repeated intervention proves durable causal understanding. F02 concept overlap remains open rather than silently consumed.

Generation separates local compatibility, represented movement, task/resource feasibility and human suitability. Initial solvability is not universal recoverability. False rejection and legitimate unexpected solutions are substantive counterexamples. Protected author/player choices cannot be silently overridden. Work counts are not wall-clock guarantees; full processing and safe stopping remain implementation obligations, not claims established by these documents. The corrected probability example retains the need to inspect actual exposure rather than seed counts.

## Taxonomy subfacet / claim / disposition map

T1 = simulation; T2 = procedural; claim IDs local to each artifact.

| Required facet | Claims and practical treatment | Disposition / remaining gap |
|---|---|---|
| Rule interactions | T1 C04,C08,C09,C12,C15; causal probe C02–C04 | Bounded state/loops/reset treatment; higher-order and adversarial coverage incomplete |
| Ecology | T1 C03,C04 | Historical circulation/cost accounts; no biological validity or independent historical reconstruction |
| Physical simulation | T1 C01,C05,C07 | Fidelity/affordance scope clear; no solver/fluids/deformation/engine comparison |
| Agent behavior | T1 C05,C06,C18 | Selection/steering/locomotion/arbitration concrete; rich cognition/social believability untested |
| Predictability | T1 C02,C11,C14,C17; PAT01 | Determinism, observation and inference separated; no validated player-learning intervention |
| Emergence | T1 C08,C09,C12,C13 | Reduced-model and contract reasoning; real tactics/shared cascades unverified |
| Generative constraints | T2 C02–C05,C14,C15; PAT02 | Represented requirements/protected choices substantive; completeness and disputed constraints open |
| Validation | T2 C05,C10,C18; PAT02 C02–C05 | Pass/fail/unknown, false acceptance/rejection; deadline illustration corrected; no implementation tested |
| Variation | T2 C06–C08,C20 | Metric-specific computational context; candidate-versus-delivery correction; meaningful novelty unmeasured |
| Repetition | T2 C07,C08,C20; PAT02 C09 | Recurrence can be useful; fallback exposure risks explicit; longitudinal effects open |
| Controllability | T2 C03,C04,C14 | Mixed initiative and protected edits concrete; author workflow benefit unmeasured |
| Authoring cost | T2 C13,C18 | Lifecycle/matched-quality accounting; no general savings or calibrated budget |

Access, ethics, localization, cultural interpretation, ownership, persistence and production receive explicit proposed checks. Complete files do not mean exhaustive taxonomy coverage. Generative-AI licensing/open-ended generation and unstudied simulation modalities remain outside scope.

## Dependency reconciliation

F01 corrected varying-answer/permission-versus-preference principles remain intact. F02/F07 proxy, intervention, commitment and retained-access cautions are consistent. F03 is now separately reviewed: full enabling-state accounting, intended productive loops and actor/state-relative resources strengthen the interpretation of probes/resets and generation feasibility. They do not validate F05 efficacy. F04 is now separately reviewed: a found sequence is only a witness for its stipulated trajectory; hidden/branching environments need information-valid policies and explicit outcome quantifiers. An unsuccessful search is not infeasibility proof. Apply these boundaries when implementing F05 task feasibility; F05 does not currently claim an exhaustive solver for unseen states.

F03/F04/W03 availability statements in originals describe their authoring snapshot. They are not overwritten as if later review had occurred then. This review reconciles available Foundations concepts without certifying all later Worlds/Presentation bodies. Current selected snapshots and review receipts should govern integration. F02 Q01/Q04 overlap with causal probe remains a central concept decision. Reused Dormans F01-08/F03-007 mapping is preserved; no canonical source ID allocated. Existing queues are neither completed nor canceled by this review.

Open: source passages not independently spot-checked, complete current cross-domain integration, canonical/queue reconciliation, representative and longitudinal evidence, actual validator/pipeline behavior and tail latency, input/rights audit, preserved relative hierarchy and real host retrieval. No release approval.
