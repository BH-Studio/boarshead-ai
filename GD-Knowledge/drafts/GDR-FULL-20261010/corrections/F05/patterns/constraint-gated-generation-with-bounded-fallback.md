---
id: GDR-CAND-20261010-F05-PAT-02
kind: pattern
title: Constraint-gated generation with bounded fallback
version: 0.1.0
status: draft
candidate_revision: independent-review-correction-1
attempt_id: F05-authoring-01
run_id: GDR-FULL-20261010
batch_id: F05
identity_scope: temporary-run-scoped
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-11'
evidence_checked: '2026-10-10'
aliases:
- validated procedural admission
- bounded generation fallback
- generation failure contract
tags:
- procedural-content
- constraints
- validation
- fallback
- authorship
- runtime-cost
- pattern-candidate
- coverage-open
related_topics:
- GDR-CAND-20261010-F05-TOP-02
- GDR-CAND-20261010-F05-TOP-01
related_patterns:
- GDR-CAND-20261010-F05-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F05-005
- GDR-SRC-20261010-F05-006
- GDR-SRC-20261010-F05-008
- GDR-SRC-20261010-F05-009
- GDR-SRC-20261010-F05-010
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: bd97bc342ee683f4ca228941bcbaac6e8a4626e31cfead500710ad49e5bce8aa
supersedes: null
change_summary: Bounded independent-review clarification; original research scope retained;
  no permanent identity allocation.
hash_record: ../reviews/f05-local-revision-receipt.md
---

# Constraint-gated generation with bounded fallback

> **Draft research candidate — bounded independent review recorded, not released or approved for implementation.** Version `0.1.0`; revision `independent-review-correction-1`. Application procedures and numerical illustrations are proposals, not adopted studio decisions. No F05 game execution, prototype, participant study or playtest occurred.

## Purpose

Prevent a content-generation request from silently delivering an instance that violates its **declared required properties**, while bounding the complete attempt and preserving human authorship over protected choices. When a compatible validated fallback is unavailable, stop or use an explicitly authorized alternative rather than fabricate validity. The proposed player-facing benefit—fewer invalid interruptions without unacceptable repetition or loss of agency—remains a hypothesis. [C-01]

This is a content admission/failure-handling pattern, not a claim that generation is required, that every outcome must be recoverable, or that a validator can certify fun. It is distinct from distribution-aware curation, which is queued as additional work, and from general balance diagnosis. [C-01, C-02, C-09]

## Context and prerequisites

The team must be able to name required properties and their state horizon, distinguish hard requirements from preferences, and identify authored choices the generator may not change. There must be a way to assess relevant properties under a known model and recognize an unknown result rather than relabel it a pass. An initial-solvability promise is different from a promise to preserve recoverability after every permitted action. [C-02, C-03]

For runtime use, the proposed complete processing policy must be enforceable under the target implementation. A step counter is not necessarily a wall-clock bound if one validation operation can block without limit. If generation, validation or fallback selection cannot be interrupted or bounded reliably enough for the experience, use offline generation/curation or direct authored content instead. This is a design requirement for later investigation, not a tested runtime guarantee. [C-04, C-05]

A fallback is optional only when a safe stop or other acceptable outcome exists. Where the product requires continuous valid content, compatible fallback coverage must itself be part of the authorized design. It may not overwrite a protected event, player construction or another actor’s commitment without separate approval. [C-03, C-05, C-07]

## Mechanism and evidence

| Link in the proposed chain | Support | Limit / potential break |
|---|---|---|
| State required properties explicitly | WFC’s local constraints, Tanagra’s movement/geometry model and protected choices show distinct scopes | The requirements can be incomplete or wrong |
| Admit only candidates that satisfy the declared checks | Logical contract reasoning | A faulty or overly restrictive validator may admit invalid content or reject valuable content |
| Repair only declared adjustable material | Tanagra’s protected-user-choice approach supplies a concrete technical example | No human productivity advantage demonstrated; conflicts can have no solution |
| Bound construction, repair, validation and retries together | Tessera documents backtracking and step-limit/retry behavior; extending the bound is F05 inference | Internal limits do not establish total completion latency |
| Deliver a compatible validated fallback or stop | Proposed failure-handling synthesis | Fallback can be stale, repetitive, unsuitable or unavailable |
| Preserve acceptable player experience and production cost | Untested application hypothesis | Repetition, false rejection and extra maintenance may outweigh the benefit |

No single inspected source implements or validates this exact complete recipe. WFC and Tessera share an algorithmic lineage; they do not provide independent trials of this pattern. Tanagra’s technical guarantees apply to its represented model, not every player or content type. [C-01–C-05]

## Recipe

### 1. Write the admission contract

Name the content unit and when it will be judged: before a session, at a new region, after an authored edit, or after systemic changes. For each required property, write the relevant initial state, abilities, resources, time/ownership conditions and allowed future actions. Separate “a completion exists initially” from “every optional choice preserves completion.” Include access/presentation information needed by the promised task. [C-02, C-07]

Classify each condition as **required**, **preferred**, or **protected authored choice**. These categories are proposed workflow labels, not a formal standard. A conflict among required/protected conditions is an unresolved design request, not permission for the generator to pick a hidden winner. [C-03]

**Exit:** if required properties cannot be stated well enough to assess or honestly label unknown, use human curation or directly authored content for that unit. Do not call a local-adjacency check a complete validator. [C-02]

### 2. Capture the reproduction and state context

Associate the request with the generator/content/constraint versions, relevant configuration, initial state, random-stream and ordering policy, and any known platform/dependency sensitivity. Keep the final accepted artifact or a sufficient reconstruction record where appropriate and authorized. Identify which state may change between evaluation and delivery. [C-06]

**Exit:** when the live state invalidates the checked contract before delivery, re-evaluate within the same overall policy or stop. Do not deliver stale content because its original seed passed. A specific synchronization mechanism requires separate technical design. [C-06, C-07]

### 3. Generate and check the candidate at the right level

Apply structural checks to structural requirements, state-aware reachability to state-aware requirements, and human review to properties the available model cannot certify. Keep pass, fail and unknown distinct. Check required dependencies and resources; do not assume tile compatibility, graph connectivity or a solver’s movement model covers all three. [C-02]

Retain enough diagnostic context to explain why a candidate failed and which relevant properties were not assessed. This need not mean storing private player data or a full gameplay recording. Evidence retention must remain proportionate to the authorized use. [C-06, C-08]

### 4. Repair only what is permitted

Repair, backtrack or regenerate declared adjustable material while retaining required and protected conditions. Record the change category and recheck affected properties. Do not satisfy a score by relocating a protected narrative element, replacing a player-owned construction, weakening an access requirement or deleting the resource that makes the task meaningful. [C-03, C-07]

If the current request is inconsistent, return a conflict for authorized authoring review. Diagnostic advice to relax a constraint can help locate a problem; it does not authorize shipping a weakened contract. [C-03, C-04]

### 5. Enforce a complete attempt policy

Allocate a locally justified budget covering construction, repair, validation, retries and fallback validation/selection, including any transition overhead relevant to the player. Track the distinction between work units and elapsed time. Reserve part of the total budget for fallback validation/selection and delivery or the declared stop transition; stop candidate work early enough to preserve that reserve. Choose stopping and cancellation behavior for the actual runtime rather than transplanting a paper’s sample size or a tool’s default. If the full deadline is already exhausted, do not start unbudgeted fallback work or claim the bound was met. [C-04, C-05]

**Exit:** when no enforceable complete policy is available, move generation offline or use a directly authored set. Repeated retries after a per-attempt timeout are not a bounded complete request unless their total is also controlled. [C-05]

### 6. Use a compatible fallback or stop

A fallback must satisfy the applicable current required properties and respect protected choices. It may be a curated instance, a simpler construction or a previously validated family with explicitly stated applicability. Prior validation does not survive arbitrary rules, capability or content updates automatically. [C-02, C-05, C-07]

If no fallback fits, stop with the declared safe outcome or request an authorized change. Do not silently substitute an invalid instance to avoid admitting failure. Do not promise a seamless experience when stopping is the only supported behavior. [C-05]

### 7. Audit what was actually delivered

Distinguish generated, rejected, repaired, accepted, curated and fallback instances. Examine clusters, omissions and frequently repeated decisions in the delivered set, not just initial generator weights or unique seeds. Keep representation metrics separate from experienced novelty, comprehension and fairness. [C-09]

Retain, narrow or remove the runtime workflow when false rejection, fallback repetition, author negotiation or maintenance defeats the intended benefit. Offline curation and authored content remain valid alternatives. This recipe does not authorize collecting telemetry, changing a game or deploying a generator. [C-01, C-08, C-09]

### Adjustable variables and explicit exits

| Variable | Proposed local decision | Exit or review trigger |
|---|---|---|
| Validity horizon | Initial state, specified future mutations, or broader recovery promise | A required state is omitted or the contract changes without review |
| Protected choices | Which authored/player-owned facts are immovable? | A solution requires silently overwriting one |
| Repair permissions | Which geometry, resources, ordering or decoration may change? | Repair alters an unapproved requirement or meaning |
| Processing policy | Work/elapsed limits, cancellation, retry accounting and overhead | A step can block outside the assumed bound |
| Fallback coverage | Which capability/state/context profiles are actually covered? | The available fallback is stale or incompatible |
| Exposure review | Which decisions, motifs, states and fallback shares matter? | Technical validity coexists with unacceptable repetition or reduced opportunity |

No default numerical values, universal retry count or guaranteed savings are specified. [C-02–C-09]

## Worked examples

### Illustrative example: an accessible crossing with a protected stop

A fictional route requires a reachable crossing for the currently declared movement capability, a tool available before its dependent obstacle, and a protected authored information stop. Optional geometry and decoration may vary. The promise is initial feasibility, not success after every later destructive action. These are invented requirements, not approved studio design. [C-02, C-03, C-07]

The following labels are **illustrative candidate names, not executed seeds or generator outputs**.

| Candidate/event | What the proposed check finds | Permitted response |
|---|---|---|
| `crossing-A` | Local connections match, but the required tool is behind the obstacle that needs it | Reject that dependency configuration or move an adjustable tool location; local validity alone is insufficient |
| `crossing-B` | A route exists, but the proposed repair removes the protected information stop | Do not apply that repair; surface the conflict or choose another candidate |
| `crossing-C` | Modeled route and tool order fit; required information has planned representations | Candidate can pass those specified checks, not an unperformed human usability or enjoyment test |
| Candidate-work allowance exhausted; reserved fallback/stop budget remains | No accepted instance remains | Validate/select and deliver a currently compatible curated fallback, or complete the declared stop outcome, within the remaining total budget |
| Fallback rules are stale | The fallback needs a movement ability the current state lacks | Reject the fallback; do not treat “previously validated” as perpetual validity |

After authoring review, the team might relax a preferred route shape while preserving capability, tool order and the information stop. That is an explicit change to an authoring request, not a hidden runtime weakening. Alternatively, author the crossing directly. The generator’s ability to produce many configurations does not settle which choice costs less or feels better. [C-03, C-08]

### Counterexample: the constraint mistakes a novel solution for failure

A physics-based solution is legitimate under the intended rules, but the validator recognizes only a conventional route. Rejecting every such candidate would reduce the very agency the content is meant to support. During authoring, review the disputed cases and repair the model or explicitly narrow the promise. Do not report the validator’s false rejection as proof that those instances are bad. No frequency of this failure has been measured here. [C-02, C-08]

## Tradeoffs and alternatives

The recipe favors declared validity and bounded handling over unconstrained search, but every declaration restricts the space. Richer checking can cost more than generating the candidate; protecting author intent can produce an unsatisfiable request; fallback can concentrate repetition. These are reasons to compare a small authored set, offline curation, simpler generation, or a deliberately narrower contract—not reasons to claim generation always needs a maximal validator. [C-01–C-05, C-08, C-09]

Human curation may be the appropriate authority for semantic fit, cultural meaning, aesthetics or a valuable unusual solution. It is not costless, automatically representative, or available inside a runtime deadline. Allocate that responsibility explicitly instead of presenting a subjective score as machine certification. [C-02, C-08]

## Failure cases

**Validator laundering:** a local or incomplete test is displayed as a general “playable” certificate. Warning sign: defects cluster in resources, state changes or access contexts that the test never represented. Narrow the certificate and add the required model or human review. [C-02, C-07]

**Infinite or unusably long recovery:** retry limits exist per attempt but the request repeatedly restarts; validation or fallback selection blocks. Apply the full processing policy or remove runtime generation. No enforced wall-clock bound was implemented in this batch. [C-04, C-05]

**Silent author override:** repair achieves validity by removing a protected choice. Treat this as a conflict, not a successful generation. Human choice can change a preference; it does not grant a generator blanket authority to rewrite content or player commitments. [C-03, C-07]

**Fallback collapse:** a few convenient instances dominate delivered content. The player may experience repetition even while the generator produces many discarded unique candidates. Review delivered exposure and the meaning of repetition, not uniqueness alone. [C-09]

**Version or state drift:** a checked candidate or fallback is delivered under changed capabilities or rules. Bind validity to its context and recheck relevant changes. Identical seed labels do not cure drift. [C-06, C-07]

## Counterexamples and do not use conditions

Do not introduce this workflow merely for hypothetical scale when a curated set meets the brief. Do not claim runtime guarantees without enforceable limits, valid checks and a supported failure outcome. Do not use hard constraints to settle an unresolved artistic or ethical disagreement invisibly. Where unexpected solutions are central and not representable by the validator, favor author review or narrow certification instead of suppressing them indiscriminately. [C-01, C-02, C-08]

The strongest opposing argument is that the infrastructure costs more than the invalid-content risk it mitigates while reducing useful variation. This is a legitimate falsifying outcome. Keeping the content authored or offline-generated would be a successful design decision, not failure to adopt the pattern. [C-08, C-09]

## Playtest

**Proposed — not performed.** First define a separately reviewed corpus of valid, invalid and intentionally disputed instances, including dependency traps, optional resource expenditure, author-protected conflicts, access variants, state drift and fallback incompatibility. A future technical study must execute the actual pipeline and measure complete processing, not just generation. This document supplies no runnable generator or test harness. [C-08]

For player evaluation, compare an authored/curated baseline with generated content under matched task and presentation requirements. Identify normal, repaired and fallback exposure without revealing those labels to participants. Measure comprehension, available plans, repeated decisions, interruptions and the intended experience separately. Include the access needs and relevant experience profiles affected by the content; plan sampling and consent separately. [C-08, C-09]

For author evaluation, count preparation, conflict negotiation, debugging, rejected instances, curation, access/localization review and later changes. Control asset quality, brief complexity and prior tool expertise. A lower placement time does not establish a lower total cost. Reject or narrow when invalid acceptance persists, valid unusual solutions are suppressed, fallbacks defeat the intended experience, or full lifecycle cost exceeds the matched alternative without sufficient benefit. Numerical budgets and thresholds require local prospective agreement. [C-08]

## Claim ledger and sources

Claim IDs are scoped to this artifact. Confidence is confidence in the precise bounded statement, not in a universal player benefit. A hypothesis remains untested even when its technical premises are well supported.

| Claim | Exact material claim and class | Evidence / precise locator | Applicability, confidence reason and unresolved issue |
|---|---|---|---|
| C-01 | `hypothesis` — Contract-gated generation with bounded complete processing and compatible fallback/stop may reduce invalid delivery at acceptable experience/cost. | GDR-SRC-20261010-F05-008, constraint/no-solution context; GDR-SRC-20261010-F05-009, contradiction; GDR-SRC-20261010-F05-010, retry guidance; proposed synthesis. | Low for complete-pattern efficacy. No integrated implementation, human result or universal saving was inspected. |
| C-02 | `inference` — A check certifies only specified modeled properties; local compatibility, route feasibility and human suitability are distinct. | GDR-SRC-20261010-F05-008, §III/§VIII; GDR-SRC-20261010-F05-009, C1/Algorithm; explicit contract logic. | High for the scope distinction; correctness/completeness of a local validator remains unverified. |
| C-03 | `inference` — Preserve declared protected choices and return conflicts rather than silently treating them as adjustable preferences. | GDR-SRC-20261010-F05-008, §VIII and §§X–XI on human geometry and no solution. | Moderate technical-to-authoring bridge; no comparative productivity result or approved studio contract. |
| C-04 | `practitioner-heuristic` — Tessera 6 guidance describes backtracking and step-limit retries, with constraint-related performance caveats. | GDR-SRC-20261010-F05-010, Backtracking/Errors/Performance. | Moderate firsthand tool guidance; not a total runtime deadline or approval to remove hard game constraints. |
| C-05 | `hypothesis` — Bound all stages and use a current valid fallback or stop; move offline when that policy cannot be enforced. | GDR-SRC-20261010-F05-009, failure possibility; GDR-SRC-20261010-F05-010, retry scope; explicit pipeline reasoning. | Low for actual latency/reliability and player benefit. A noninterruptible check can defeat the proposed bound. |
| C-06 | `inference` — Tie reproduction and validity to the actual version/configuration/state/order context, not seed identity alone. | GDR-SRC-20261010-F05-005, Deterministic multithreading; explicit state/version reasoning. | Moderate application bridge; exact sufficient bundle depends on implementation and was not tested. |
| C-07 | `hypothesis` — State horizon, capability, access and protected commitments should constrain admission and fallback applicability. | GDR-SRC-20261010-F05-008, model scope; reviewed P01/P02/F07 cautions; companion topic examples. | Low for complete contextual coverage. Initial feasibility does not imply all-state recoverability or actual accessibility. |
| C-08 | `hypothesis` — Compare false acceptance/rejection, complete processing and lifecycle author/player costs against a matched simpler alternative. | Reviewed F07-TOP-01 measurement limits; technical sources above; proposed corpus and studies in this pattern. | Low for unperformed tests; independent oracle review, participants and local thresholds remain absent. |
| C-09 | `inference` — Filtering and fallback change delivered exposure; uniqueness and validity do not establish experienced variety. | GDR-SRC-20261010-F05-006, §4.5/§5; companion topic C-08 conditional-distribution argument. | High for distribution/scope distinction, low for novelty benefit. Source 006’s corpus is computational, not a player study. |

## References

All listed sources were inspected on 2026-10-10 to the stated extent. This is bounded research, not an exhaustive search. Source titles and locators identify historical editions; mutable documentation must be rechecked before implementation. Source repetition across entries does not add independent evidence.

### GDR-SRC-20261010-F05-005

**Rseding / Wube Software. [Friday Facts #415 — Fix, Improve, Optimize](https://www.factorio.com/blog/post/fff-415).** Factorio development blog. Publication/update: 2024-06-14.

**Edition / access:** Factorio 1.1 and then-in-development 2.0 account; not verification of present behavior. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand technical development report.

**Inspected locators:** Deterministic multithreading; Robot task performance (rendered lines 25–39 and 49–63).

**Claims supported or informing hypotheses in this entry:** C-06 historical case informing reproduction reasoning.

**Limits / independence:** Reported multi-condition defect and optimization reasoning, not reproduced here. Future-tense fixes in the article are not current verified state. No general speedup or deterministic guarantee inferred.

**Rights:** Public developer article; paraphrased; no code/images redistributed.

### GDR-SRC-20261010-F05-006

**Gillian Smith and Jim Whitehead. [Analyzing the Expressive Range of a Level Generator](https://www.pcgworkshop.com/archive/smith2010analyzing.pdf).** ACM, PCGames 2010 workshop, Monterey. Publication/update: 2010-06-18.

**Edition / access:** 2010 workshop paper; Launchpad generator. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original computational evaluation/method paper.
DOI: `10.1145/1814256.1814260`.

**Inspected locators:** §2 Analytical Approach; §3 Launchpad; §§4.1–4.5, especially PDF pp. 4 and 6, Figures 6, 7 and 11; §5 Discussion. Screenshots of PDF pp. 4 and 6 inspected.

**Claims supported or informing hypotheses in this entry:** C-09 distribution/metric scope.

**Limits / independence:** Generated-level corpus, with 10,000 levels per plotted sample unless otherwise stated; geometry-derived metrics, not participants or validated experienced difficulty. Same research lineage as source 008; no independent human replication.

**Rights:** ACM copyright notice inspected; paraphrase and bibliographic reference only; PDF/figures not redistributed.

### GDR-SRC-20261010-F05-008

**Gillian Smith, Jim Whitehead and Michael Mateas. [Tanagra: Reactive Planning and Constraint Solving for Mixed-Initiative Level Design](https://www.researchgate.net/publication/224242275_Tanagra_Reactive_Planning_and_Constraint_Solving_for_Mixed-Initiative_Level_Design).** IEEE Transactions on Computational Intelligence and AI in Games 3(3), 201–215. Publication/update: Printed issue: 2011-09; printed publication date: 2011-09-14.

**Edition / access:** 2011 journal article, author-uploaded full text (page identifies Gillian Smith upload, 2014-09-06); not the distinct 2010 Tanagra paper. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Original mixed-initiative system/expressivity paper.
DOI: `10.1109/TCIAIG.2011.2159716`.

**Inspected locators:** §III Level Representation, p. 203; §V System Overview, p. 205; §VIII constraint search, pp. 210–211; §§IX–XI, pp. 211–214, on expressivity and limitations. Text inspected, not figure pixels.

**Claims supported or informing hypotheses in this entry:** C-02/C-03; technical context C-01/C-07.

**Limits / independence:** Institutional PDF route failed; recovered author-uploaded article text matches title/authors/printed issue/DOI, but publisher-byte equivalence was not verified. Landing metadata says October 2011; printed issue says September. Playability is relative to represented movement/geometry, not all player abilities or human productivity evidence.

**Rights:** IEEE copyrighted article; no full text, figures or screenshots redistributed.

### GDR-SRC-20261010-F05-009

**Maxim Gumin. [WaveFunctionCollapse — repository README](https://github.com/mxgmn/WaveFunctionCollapse).** Author’s public GitHub repository mxgmn/WaveFunctionCollapse. Publication/update: Publication/update date unknown.

**Edition / access:** Mutable master-branch README inspected on the access date; commit hash not captured. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Creator-maintained technical documentation.

**Inspected locators:** README opening: local-similarity C1 and weak C2; contradiction paragraph; Algorithm; Tilemap generation (rendered lines 212–247).

**Claims supported or informing hypotheses in this entry:** C-02; technical context C-01/C-05.

**Limits / independence:** README inspection, not source-code execution or independent verification of listed commercial uses. Claims concern documented local constraints and failure possibility, not whole-game solvability. Tessera shares this algorithmic lineage.

**Rights:** Repository code/assets licensing not audited; no code, assets or screenshots copied; documentation paraphrased.

### GDR-SRC-20261010-F05-010

**BorisTheBrave / Tessera documentation maintainer. [Quality, Performance and Debugging](https://www.boristhebrave.com/docs/tessera/6/articles/quality.html).** Tessera official documentation. Publication/update: Publication/update date unknown.

**Edition / access:** Documentation version 6 URL; exact minor release and commit unknown. Accessed 2026-10-10; `access: relevant-excerpt`. Type: Firsthand tool guidance.

**Inspected locators:** Backtracking; Errors; Performance, especially Step Limit/retry, fixed-seed diagnosis and path-constraint advice (rendered lines 9–49).

**Claims supported or informing hypotheses in this entry:** C-04; technical context C-01/C-05.

**Limits / independence:** Vendor guidance, not an end-to-end latency benchmark or universal authoring-cost result. Debug advice to relax constraints is not permission to remove a game’s required properties. WFC derivative family, not an independent replication.

**Rights:** Public documentation; licensing not separately audited; paraphrase only.

## Related entries and history

Parent: [Procedural and authored content](../topics/procedural-and-authored-content.md), `GDR-CAND-20261010-F05-TOP-02`. Companion: [Simulation and systemic behavior](../topics/simulation-and-systemic-behavior.md), `GDR-CAND-20261010-F05-TOP-01`; complementary [Bounded causal probe](bounded-causal-probe.md), `GDR-CAND-20261010-F05-PAT-01` when stable inquiry conditions are part of the generation brief.

Open issues: model completeness, false rejection of legitimate solutions, actual bounded execution, stale fallback, repeated exposure, access/localization coverage, and total authoring cost. Packet-local conflicts `F05-CON-03`–`F05-CON-06` remain explicit. Distribution-aware curation and mission-to-space contracting are queued child proposals with no keys allocated here; they are not hidden third/fourth patterns.

2026-10-10: initial `0.1.0` / `initial-research-1` submission, predecessor/supersession null. Author self-review only; no independent F05 review, game implementation, player study, permanent allocation or release. Exact hashes appear in the detached integrity receipt and review packet inventory.


**Local revision, 2026-10-11:** Bounded review clarification recorded in [local revision receipt](../reviews/f05-local-revision-receipt.md). Original initial-submission/no-review history above is historical. Stable provisional ID, version, draft and null approvals retained; no generator, gameplay or participant results added.
