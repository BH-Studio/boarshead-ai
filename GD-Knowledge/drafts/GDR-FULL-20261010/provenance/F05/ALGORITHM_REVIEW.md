# F05 algorithm and bounded-fallback review

Reviewed 2026-10-11. Scope: full reads of `procedural-and-authored-content.md` (342 lines) and `constraint-gated-generation-with-bounded-fallback.md` (292 lines), plus bounded primary-source spotchecks. Originals were not edited. No generator, game, prototype, usability test, or benchmark was executed.

## Disposition

The core algorithm claims and evidence limits are sound. Recommend two narrow corrections before accepting these candidates: disambiguate the candidate-pool probability identity from request-level delivery, and reserve fallback/stop time inside the total processing budget. Neither correction establishes the proposed pattern's efficacy or authorizes implementation. There is no basis here for broad source replacement or a new research pass.

## Required narrow corrections

### A1. Specify the probability population and delivery weighting

Location: topic line 105 and claim C-08 at line 223; inherited by pattern C-09 at line 208.

The conditional identity is mathematically correct for a specified candidate population and its acceptance event. It requires no independent-retry assumption. The present wording calls that conditional share the delivered share without fixing the candidate population or weighting. This becomes ambiguous for adaptive retries, repair, ordering, selection among multiple accepted candidates, or comparisons weighted by requests rather than candidates. A fixed first-proposal distribution conditioned on acceptance is not generally the output law of an arbitrary retry-and-selection pipeline. The fallback mixture remains valid when its component laws are the actual delivery distributions and its denominator excludes stopped requests.

Replace the topic paragraph at line 105 with:

> Filtering can change delivered exposure. As a purely mathematical illustration, let `X` be a candidate drawn from a specified candidate-pool distribution and let `A` be that candidate's acceptance event, with `P(A) > 0`. Among accepted candidates in that same pool and under the same sampling weights, the share belonging to category `B` is `P(X in B | A)`, which need not equal `P(X in B)`. This conditional identity does not require independent retries and does not supply an acceptance rate. It is not, by itself, the per-request delivery law: adaptive retries, ordering, repair and final selection can change that law and the relevant weights. If `f` is the fallback share among delivered instances, their distribution mixes the actual non-fallback delivery distribution with weight `1-f` and the actual fallback delivery distribution with weight `f`. Audit attempted, rejected, repaired, accepted, selected and fallback content, and state whether exposure is weighted by candidates, requests, sessions or players. [C-08]

Replace the exact-material-claim cell of topic C-08 with:

> `inference` — Acceptance, repair, final selection and fallback can alter delivered exposure; candidate-pool conditional probabilities describe that pool and weighting, not arbitrary request-level delivery.

Replace that row's confidence/limit cell with:

> High for the conditional identity and mixture decomposition; per-request exposure requires the actual retry/repair/selection policy and declared weighting. No empirical acceptance rate, independence assumption or recommended quota.

Pattern C-09 can retain its bounded distribution distinction after the companion correction. This is analytic scope repair, not an empirical finding about any inspected generator.

### A2. Trigger fallback before the complete budget is exhausted

Location: pattern step 5 at line 111 and worked-example row at line 153. The topic's line 175 already correctly places fallback selection before runtime-budget expiry.

The policy includes fallback validation/selection and relevant transition overhead inside its complete budget, but the example currently waits for “Overall budget exhausted” before invoking fallback or stop. Those operations can take time too. A complete deadline needs a bounded terminal path and time reserved for it; a timeout cannot authorize starting additional unbudgeted work.

Append to the step-5 paragraph at line 111:

> Reserve enough of that budget for compatible fallback validation/selection and delivery, or for the declared stop transition. End candidate search at an earlier cutoff that preserves this reserve; the fallback or stop outcome must complete within the overall bound.

Replace the worked-example row at line 153 with:

> | Candidate-search cutoff reached | No accepted instance is ready and the reserved fallback/stop budget remains | Complete compatible fallback validation/selection and delivery, or the declared stop transition, within the remaining overall budget |

This is a consistency correction to the proposed policy, not proof that any implementation can enforce it. If terminal handling is not reliably bounded, the existing offline/authored exit remains applicable.

## Algorithm and source checks

- **WFC:** The creator's README supports local-pattern scope, possible propagation contradiction, and a no-output failure path. The topic does not promote that into a global game-solvability guarantee, assume frequency matching is exact, or assert that a failed search proves the entire problem unsatisfiable. No correction needed. [Primary README, opening and Algorithm](https://github.com/mxgmn/WaveFunctionCollapse)
- **Tessera 6:** Official guidance describes backtracking, a step limit that initiates fresh generation, and constraint-related performance concerns. The documents correctly distinguish this from an end-to-end wall-clock bound. They also avoid treating debugging advice to disable constraints as authorization to weaken required properties. [Official version-6 guidance, Backtracking / Errors / Performance](https://www.boristhebrave.com/docs/tessera/6/articles/quality.html)
- **Tanagra:** The 2011 article describes a limited avatar-physics representation, retention of designer constraints during solving, and conflicts for which acceptable connecting geometry is absent. Its model-conditional playability rationale supports the documents' bounded claims, not all-player accessibility or measured author productivity. An additional source nuance is that individual Choco searches are cut off after 50 ms (§V-B, printed p. 208); therefore generic search failure must not be promoted to proof of unsatisfiability. These candidates already distinguish pass, fail and unknown, and do not make that promotion. No new numerical recommendation should be imported. [Author-uploaded primary article, §§III, V-B, VIII and XI](https://www.researchgate.net/publication/224242275_Tanagra_Reactive_Planning_and_Constraint_Solving_for_Mixed-Initiative_Level_Design)
- **Launchpad:** The paper's selected linearity/leniency comparison supports the reported regular-rhythm result, and its corpus is computational. The 10,000-level statement includes the paper's “unless otherwise stated” qualification. Its filtering analysis supports examining a retained subset, not an arbitrary delivery policy. The draft correctly avoids reporting these metrics as participant-rated difficulty or novelty. [Primary paper, §§4.2–4.5](https://www.pcgworkshop.com/archive/smith2010analyzing.pdf)
- **Dormans:** The primary paper separates mission dependencies from spatial structure and describes coupling their generation. The draft properly avoids importing its broad genre-value or productivity assertions as established universal findings. [Primary paper, §§2 and 6–8](https://www.pcgworkshop.com/archive/dormans2010adventures.pdf)
- **Factorio:** The historical report does describe a generation-determinism fault needing several conditions, including differing CPU-core counts. The reproduction-bundle recommendation is explicitly inferred and remains implementation-dependent. The draft does not assert that the historical defect persists. [Firsthand report, Deterministic multithreading](https://www.factorio.com/blog/post/fff-415)

## Arithmetic, proof scope and pattern quality

No erroneous numerical arithmetic was found in these two artifacts. The topic's conditional probability expression is an identity once its population is fixed; A1 corrects scope, not algebra. No unjustified retry-success formula, independence assumption, fixed retry count, runtime benchmark, or universal cost-saving percentage is asserted.

Initial existential feasibility is consistently distinguished from continued recoverability across later optional actions. A compatible fallback is checked against current capability, state and version context. Protected choices and permitted repairs are explicit. The pattern gives observable exits and opposing cases, and identifies complete-pattern efficacy as untested. Human suitability, creative value and experiential novelty are not certified by a solver result. The validity ladder is expressly proposed rather than presented as a formal verification standard.

The resulting review is **accept after these two narrow textual corrections, with all draft/coverage-open and unperformed-validation limits retained**. This is a research-content review only; it is not a deployment, mathematical completeness, accessibility-conformance, or latency certification.

## Corrected-copy verification

After the parent applied revisions, I read the changed probability paragraph in `corrected/topics/procedural-and-authored-content.md` at line 105 and the changed budget paragraph/example in `corrected/patterns/constraint-gated-generation-with-bounded-fallback.md` at lines 111 and 153. Their applied wording resolves A1 and A2. The replacement wording above is review guidance; the corrected copies use equivalent phrasing. Original candidate files remain unedited by this reviewer.
