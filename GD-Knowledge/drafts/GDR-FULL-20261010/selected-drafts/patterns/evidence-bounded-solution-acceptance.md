---
id: GDR-CAND-20261010-G10-PAT-01
kind: pattern
title: Evidence-bounded solution acceptance
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_identity: GDR-FULL-20261010/G10/initial-generation
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G10 synthesis; no prior G10 artifact replaced.
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G10
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles; corresponding UTC session date 2026-10-11
coverage_state: coverage-open
aliases:
- equivalent-answer acceptance
- observation-equivalent answers
- bounded answer validation
tags:
- answer-validation
- equivalence
- uncertainty
- information-contract
- recognition
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-02
related_patterns:
- GDR-CAND-20261010-W02-PAT-02
- GDR-CAND-20261010-G03-PAT-02
- GDR-CAND-20261010-W03-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G10-GEN-01
- GDR-CAND-20261010-G10-GEN-02
source_ids:
- GDR-SRC-20261010-G10-003
- GDR-SRC-20261010-G10-004
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G10
author_self_review: completed; see batch packet
integrity_record: ../reviews/full-run-20261010-g10-integrity.md
---

# Evidence-bounded solution acceptance

**Provisional reusable pattern — not released or validated.** `GDR-CAND-20261010-G10-PAT-01`, version `0.1.0`, revision `initial-draft-1`. This is G10’s sole new pattern. Its domain home remains subject to Library Coordination: answer validity intersects Foundations decision design and Worlds objective contracts. It does not duplicate G03’s hint pattern or W03’s spatial-evidence pattern.

## Purpose

Help a designer decide **what counts as an accepted answer when more than one representation or hidden state may satisfy the declared task**. The intended benefit is to avoid rejecting legitimate alternatives merely because they differ from a private answer key, without turning every plausible guess into established truth. The structural distinction is well defined under explicit assumptions; improvements in trust, satisfaction or reasoning remain hypotheses. [C-01, C-05, C-08]

## Context and prerequisites

Apply only when the team can state the task’s answer contract, relevant world rules, permitted evidence and supported response forms. The strongest fit is a finite or otherwise verifiable reasoning system. It may also help audit a bounded narrative answer form. It does not supply a truth oracle for unrestricted natural-language explanations. [C-04, C-06]

The designer needs a stable task instance or an explicitly time-indexed history; a way to enumerate or otherwise justify the relevant alternatives; a reliable distinction between an answer and its wording; and the production capacity to review false acceptance as well as false rejection. A permitted probe must actually be available under the task’s conditions, including its access requirements. Merely existing in an author’s debug view does not make evidence available to players. [C-04, C-06]

**Exit before adopting the pattern** when the team cannot bound the alternatives, cannot distinguish identical wording from distinct claims, cannot supply the evidence needed by the advertised task, or cannot explain what completion means without overclaiming truth. Use a narrower answer vocabulary, a different completion contract, explicit uncertainty or an authored revision instead. An arbitrary language-model confidence score is not a substitute for a validated contract. [C-06, C-07]

## Mechanism and inspected evidence

The Black Box manual describes checking probe-result equivalence rather than exact hidden placement, and distinguishes a guess inconsistent with known observations from one refuted by an additional possible probe. Pope’s Obra Dinn development account describes accommodating alternative fate formulations. These illustrate two different problems—observational equivalence and expression recognition—and do not validate a general-purpose adjudicator. [C-02, C-03; GDR-SRC-20261010-G10-003; GDR-SRC-20261010-G10-004]

### Four concepts that must not be merged

**Equivalent expression:** different wording denotes the same task-relevant claim. “Sent to the receiving office” and “transferred to receiving” may denote the same event in a deliberately restricted vocabulary. The designer must specify that equivalence rather than assuming all paraphrases preserve who did what. [C-03, C-04]

**Multiple valid constructions:** different end states satisfy a public predicate such as meeting all constraints. There may be no private hidden answer at all. An ordinary constraint validator may be simpler than this pattern’s hidden-state equivalence machinery. [C-04, C-07]

**Observational equivalence:** distinct permitted hidden states cannot be distinguished by any inquiry the contract admits. In the simple deterministic case, let `H` be the admitted hypotheses, `h*` the selected hidden state, `Q` the complete allowed inquiry set, and `R(h,q)` the response predicted by the model. Then `h` is equivalent to `h*` exactly when `R(h,q) = R(h*,q)` for every `q` in `Q`. For state-changing investigations, `q` must represent a permitted inquiry sequence with its relevant history, not just an isolated button press. Stochastic or noisy observations need a separately justified uncertainty model; one matching sample is not deterministic equivalence and this draft supplies no statistical acceptance threshold. [C-04, C-06]

**Consistency with evidence encountered so far:** an answer fits the particular observations already obtained. This is weaker than equivalence over `Q`. A still-unperformed but available discriminator may invalidate it. A narrative explanation can also depend on unsupported premises outside the admitted model. “Not yet refuted” does not entail “a complete solution” or “what actually happened.” [C-04, C-05]

Even when two hidden states are observationally equivalent, one may still be the fictional history. Accepting an equivalence class as completion is a **declared design choice about the task**, not a scientific finding that both histories occurred. If exact historical recovery is indispensable to the advertised task, add a legitimate discriminator or acknowledge that the task is underdetermined. Do not quietly redefine the objective after an answer is submitted. [C-05, C-06]

### Causal support and limits by link

| Proposed link | What supports it | What remains unestablished |
|---|---|---|
| An explicit contract makes allowed answer distinctions inspectable. | Logical consequence of recording the predicate, inquiry set and response meaning; documentary examples motivate the need. [C-01–C-04] | Whether a given team’s contract captures every intended distinction. |
| A correct classifier can distinguish permitted alternatives from contradictions. | Conditional formal argument within the declared model, not evidence that an implementation is correct. [C-04] | Completeness, runtime correctness, state/version integrity and equivalence across access routes. |
| Accepting a genuinely valid alternative avoids that particular private-key false rejection. | Direct conditional implication: the alternative is accepted rather than rejected. [C-05] | Whether other invalid answers are accidentally admitted or an essential distinction was lost. |
| A scoped explanation can make the acceptance boundary understandable. | Existing documented feedback alternatives and the inspected G03 help pattern motivate testing. [C-02, C-07] | It may instead reveal the solution, confuse players or become an answer oracle. |
| Better recognition improves trust, enjoyment or independent reasoning. | Hypothesis only. [C-08] | No full-pattern experiment, player outcome or causal estimate was inspected or produced. |

## Recipe

1. **Write the completion promise.** State whether the task demands an exact recoverable truth, any valid construction, a class of indistinguishable models, a supported provisional explanation, or a consequential decision under uncertainty. State what the checker’s response means. Distinguish an institution accepting a report from the world establishing it as true. Stop when stakeholders disagree about this contract; do not hide the disagreement in answer code. [C-05, C-06]

2. **Separate semantic claims from response forms.** Record the event, relation, actor or constraint the answer asserts, then the approved expressions that denote it. Keep a provisional list of potentially ambiguous expressions for human review. Grammatical variation is not permission to change a culprit, chronology or causal relation. If recognition is unreliable, narrow the response language or acknowledge interpretive rather than factual adjudication. [C-03, C-06]

3. **Bound the evidence and the alternatives.** Specify `H`, the legal inquiry set `Q`, relevant initial state and history, and what responses each hypothesis predicts. For a narrative case, record explicit premises and unresolved assumptions rather than pretending a complete formal model exists. Do not remove inconvenient probes from `Q` merely because a player has not tried them. Conversely, do not count inaccessible debug knowledge as legitimate evidence. [C-04, C-06]

4. **Classify a proposed answer at the correct level.** Check expression recognition separately from constraint satisfaction. Identify contradiction, provisional consistency, full equivalence under the task, or a valid construction under a public predicate. When a discriminator exists, record it. When the model is insufficient, retain an unresolved state instead of inventing a confident verdict. This is a proposed design audit, not executed code. [C-04, C-05]

5. **Choose feedback independently of validation.** A checker may internally know the discriminator without revealing it immediately. Choose acknowledgment, a statement of incomplete support, a requested counterexample, or a direct answer according to the task and the player’s help request. Apply the existing G03 hint pattern; do not require an automatic hint ladder. Audit repeated queries for answer leakage. [C-07]

6. **Review boundary cases before integration.** Include alternative wording for the same claim, a valid but unexpected construction, a genuinely indistinguishable state, a currently consistent but distinguishable state, a contradictory state, an inaccessible discriminator, an old save, and a localization change. Review false acceptance and false rejection separately. If the checker’s answer cannot be justified, hold the candidate rather than expanding acceptance until complaints stop. [C-06, C-09]

7. **Evaluate experience separately and retain an exit.** Compare appropriate contract alternatives with fresh content and the intended audience. Keep claim class and observed outcome separate. Simplify or remove the pattern when it imposes unnecessary machinery, destroys intended uncertainty, grants undeserved factual certainty, or fails to improve the locally stated problem. A technically correct validator does not by itself justify the experiential recommendation. [C-07–C-09]

### Adjustable variables

| Variable | What may be adjusted | Boundary to preserve |
|---|---|---|
| Answer granularity | A whole model, a relation, a constructed artifact, or one report field. | Smaller units can disclose the decomposition of the intended reasoning. |
| Semantic vocabulary | Fixed terms, approved aliases, a constrained statement form, or explicitly interpretive text. | Do not advertise unrestricted recognition without evidence of it. |
| Inquiry set | Which observations or sequences the task permits, with costs and prerequisites. | The set must follow the advertised contract, not be retrofitted to force uniqueness. |
| Acceptance meaning | Complete, provisionally consistent, institutionally accepted, unresolved, or contradicted. | These terms are not synonyms for truth. |
| Feedback timing and detail | Immediate acknowledgment, delayed verdict, requested discriminator, requested answer. | No universal delay, bundle size or wrong-slot count is recommended. |
| Recovery | Edit a report, replay a case, review evidence, or accept disclosed consequences. | Restoring state does not erase revealed knowledge. |
| Localization/access route | Alternative terms, input and evidence representations. | Preserve the task-relevant distinctions and uncertainty; experiential parity remains a question. |

## Worked example 1: a sealed two-cell instrument

**Illustrative formal example, not a game implementation or performed test.** Two hidden cells each contain either zero or one unit. The admitted states are `(0,0)`, `(0,1)`, `(1,0)` and `(1,1)`. In Contract A, the sole permitted inquiry returns the total. The task is explicitly to submit any arrangement indistinguishable through the permitted inquiry. [C-04, C-09]

For a total of one, `(0,1)` and `(1,0)` are equivalent under Contract A. A checker demanding only its private arrangement would reject an answer the contract explicitly permits. The correct acceptance class contains both; it excludes the states whose totals are zero and two. The following table follows by arithmetic from the illustrative definitions, not empirical observation.

| Submitted state | Total response | Contract A, selected state `(1,0)` |
|---|---|---|
| `(0,0)` | 0 | Contradicted. |
| `(0,1)` | 1 | Equivalent and accepted under the stated task. |
| `(1,0)` | 1 | Equivalent and accepted. |
| `(1,1)` | 2 | Contradicted. |

In **Contract B**, an additional legal inquiry reveals the left cell. Now `(0,1)` and `(1,0)` are distinguishable. A player who has asked only for the total has provisional consistency, not full equivalence. The task could require the exact arrangement and provide access to the second inquiry. Do not mark `(0,1)` as a complete solution merely because it matches the evidence sampled so far. [C-04, C-05]

The feedback decision is separate. The interface can acknowledge a recognized answer, report insufficient support, or offer the unused discriminator on request. Automatically revealing the left cell may be acceptable for an explicitly requested answer but may defeat a desired investigation. If an access mode prevents the left inquiry, repair the access route or change the task transparently; do not count the inaccessible evidence as if everyone had it. [C-06, C-07]

## Worked example 2: a bounded investigation report

**Illustrative narrative adaptation.** A case establishes that an object reached a receiving office but leaves who authorized the transfer unresolved. “The object was transferred to receiving” and an approved synonymous phrase can denote the same limited claim. “The guard stole the object” is a different claim; it does not become acceptable merely because both explain the absence. [C-03–C-06]

Separate report fields can record the object’s location, whether authorization is established and whether the mover is identified. The practical task may end when the object is recovered while the historical questions remain open. If the player is required to identify a mover, the design must either provide a legitimate discriminator under its stated fictional rules or acknowledge underdetermination. An NPC agreeing with an accusation is a consequence, not necessarily proof. [C-05, C-06]

This is where the pattern must stop short of unrestricted truth adjudication. It can help specify supported answer forms and unresolved states. It cannot prove an explanation solely because it sounds coherent or has not yet been disproved. For broader interpretation, use an explicitly interpretive outcome and retain the unresolved disagreement. [C-06, C-07]

## Tradeoffs and alternatives

An equivalence-aware checker may avoid a narrow false rejection while increasing the burden of defining, testing and explaining answer classes. Over-broad equivalence can erase a meaningful causal distinction. Under-broad equivalence can recreate the original private-key defect under a more complex name. A synonym list can help expression but is not a solution to incomplete world modeling. [C-05–C-07]

Use **exact matching** when the answer really is unique under accessible evidence and the accepted expression is appropriately clear. Use **constraint satisfaction** for open construction when hidden-state equivalence adds nothing. Use **explicit uncertainty** when several explanations remain live. Use **an additional discriminator** when exact historical recovery is the intended task. Use **a declared interpretive response** when closure is deliberately artistic rather than adjudicable. These alternatives can be simpler and more honest than a general-purpose validator. [C-06, C-07]

The pattern interacts with help and accessibility but does not own them. A requested counterexample can be a hint. A caption or notebook label can unintentionally collapse two otherwise equivalent states by revealing hidden identity. Conversely, stripping a legitimate distinguishing fact from an access route can make the task underdetermined for that player. Audit the contract jointly with Presentation rather than claiming universal parity. [C-06, C-07]

## Failure cases and observable warning signs

| Failure | Warning sign to investigate | Correction or exit |
|---|---|---|
| Consistency mistaken for equivalence | A rejected answer fits seen evidence but an untried legal query would distinguish it. | Retain the provisional state; review disclosure of further inquiry rather than automatically accepting it. |
| Private key disguised as fairness | Two states have identical complete legal response signatures, yet one is rejected without explanation. | Revise the contract or acceptance class; do not call the distinction inferable. |
| Equivalent wording treated as a different event | Changing a harmless expression flips the verdict. | Review semantic normalization separately from causal truth. |
| Different events merged by vague language | A broad phrase is accepted despite changing an actor, time or authorization claim. | Narrow response forms, expose uncertainty or return to human review. |
| Mutable truth | Reloading or submitting a new guess changes which earlier evidence is supposedly true. | Preserve versioned instance/history or openly define a different generative contract. |
| Answer oracle | Repeated submissions converge without the intended investigation. | Reassess information released and the experience goal; do not assume that delay alone solves it. |
| Access-dependent validity | One route omits or adds a decisive distinction. | Repair evidence access and rerun the contract audit; withdraw parity claims. |
| Model overreach | The system confidently judges unrestricted narratives outside its represented premises. | Stop automatic factual adjudication; narrow the task or explicitly mark interpretation. |

These are proposed diagnostics derived from the contract analysis, not observed failure rates. [C-04–C-07, C-09]

## Counterexamples and do-not-use conditions

Do not use broad alternative acceptance when the submitted answer has an available contradiction, when the task deliberately requires a particular method, or when a historical distinction is both recoverable and central. Do not use it to hide missing clues in a supposedly unique-solution case. Do not force factual closure on an intentionally ambiguous story. Do not call an accepted fictional accusation a transferable real-world evidential judgment. [C-05–C-07]

A single unambiguous keypad answer with clear input may need none of this machinery. An expressive narrative discussion may need no truth checker. An open construction task may require only an ordinary validity predicate. These counterexamples challenge the strongest version of the pattern: more sophisticated acceptance logic is not inherently better design. [C-07]

## Proposed playtest and validation

**Not performed.** No implementation, benchmark, player study or host retrieval test was run for this pattern. A formal table in this document is a worked derivation, not evidence of a functioning game. [C-09]

First review the contract independently of player outcomes. Use known alternative expressions, equivalence classes, distinguishable candidates and contradictory candidates. Verify that each predicted verdict follows from the specified model. A player’s satisfaction cannot repair a false acceptance; a passing formal audit cannot establish enjoyment. No arbitrary instance count certifies correctness. [C-04, C-09]

For experience evaluation, compare an appropriate exact-key design, the bounded-acceptance design and an explicit-uncertainty alternative using matched fresh tasks. Include participants whose vocabulary, access routes and prior genre knowledge could expose recognition or evidence asymmetries. Avoid exposing the same hidden solution twice and treating the second exposure as independent reasoning. [C-08, C-09]

Record rejected-valid and accepted-invalid submissions relative to the contract, reasons players give for their answers, whether they understand what acceptance means, repeated-query strategies, unwanted revelations and the relevant self-reported experience. Separate technical classification errors from misunderstanding of feedback. Do not treat faster completion alone as improved reasoning or trust. [C-08, C-09]

Predeclare the local decision rule before testing. Any demonstrated mismatch with the stated validity contract requires correction or withdrawal of the correctness claim. Reject the proposed experience benefit when proper recognition adds no useful value for the stated task, increases unwarranted certainty, removes the desired distinction, or costs more than a simpler alternative without meeting the project’s goal. Sample planning and an uncertainty analysis require a separate reviewed protocol. [C-08, C-09]

## Claim ledger

| ID | Precise claim / classification | Support and limits | Confidence |
|---|---|---|---|
| C-01 | The pattern targets false rejection of contract-valid alternatives without granting arbitrary plausibility the status of truth. `inference` | Derived design problem; 003 documents one specific alternative acceptance approach. | Moderate applicability; no universal need for the pattern. |
| C-02 | Black Box documentation distinguishes result-equivalent layouts and counterprobes beyond already-observed evidence. `observed-example` | 003 Chapter 19 and §19.1, documentation version 20260923.616da16. No runtime observation. | High for the inspected text only. |
| C-03 | Pope’s development account permits multiple fate formulations, a narrower issue than multiple distinct histories. `practitioner-heuristic` | 004 #734 SVO Fates; unknown executable build. | Moderate contextual support; not unrestricted semantic equivalence. |
| C-04 | Under an explicit deterministic model, equivalence over all legal inquiries is stronger than consistency over a sampled subset. `inference` | Formal definition and illustrative enumeration; motivated by 003. Stateful tasks require inquiry histories. | High under stated assumptions; no implementation proof. |
| C-05 | Correctly accepting an alternative that satisfies the declared contract avoids that specific private-key false rejection, but does not establish multiple historical truths. `inference` | Conditional logic; D: W02 objective/acceptance distinction; C-04. | High conditional claim, not a measured user benefit. |
| C-06 | Unbounded semantics, unavailable evidence or a disputed contract require narrowing, explicit uncertainty or exit. `inference` | Limits of C-04/C-05; D: P01/P02 access and W02 contracts. | Moderate design safeguard; effects and production burden untested. |
| C-07 | Validation and feedback can be separated; simpler alternatives may better preserve the task. `inference` | 003 feedback; 004 #740 analytical objection; D: G03 hint pattern. | Moderate recommendation; no optimal feedback schedule established. |
| C-08 | Bounded acceptance may improve perceived recognition, trust or reasoning relative to appropriate alternatives. `hypothesis` | Proposed application bridge, not borrowed from game success. | Low; no direct full-pattern efficacy evidence. |
| C-09 | The recipe, boundary cases and proposed evaluation could detect contract and experience failures. `hypothesis` | Explicit falsifiers and formal example; not executed tests. | Low for the complete workflow; independent protocol review needed. |

## Related entries, overlap and history

Applies conditionally to [Puzzle](../genres/puzzle.md), `GDR-CAND-20261010-G10-GEN-01`, and [Detective and mystery](../genres/detective-and-mystery.md), `GDR-CAND-20261010-G10-GEN-02`. It is reusable outside both when answer validity and evidence equivalence are genuine design questions.

The inspected dependencies are identified in the [review packet](../reviews/full-run-20261010-g10-review-packet.md#reviewed-dependency-ledger): corrected `GDR-CAND-20261010-W02-PAT-02` owns objective/acceptance contracts; `GDR-CAND-20261010-G03-PAT-02` owns player-requested help; `GDR-CAND-20261010-W03-PAT-01` owns staging evidence for inference; corrected `GDR-CAND-20261010-P02-PAT-02` owns fact-preserving cue alternatives. This pattern adds a bounded acceptance-class audit rather than a second implementation of those techniques. Coordination must still decide the permanent home and overlap.

Local contradiction links: `G10-CON-01`, `G10-CON-02`, `G10-CON-03` and `G10-CON-07`. Initial draft, no predecessor, no superseded artifact, no independent G10 reviewer or approval. All content remains `0.1.0 draft`. The [integrity receipt](../reviews/full-run-20261010-g10-integrity.md) holds final byte hashes outside the files being hashed. Additional candidate pattern work is queued, not silently discarded or assigned permanent identities.

## References

All access dates: **2026-10-10, America/Los_Angeles** (retrieval session falls on 2026-10-11 UTC). Section names are portable locators; line ranges describe the inspected web-text rendering, not immutable publisher numbering. `observed-example` claims concern a documentation artifact unless explicitly stated otherwise. No game build was run. Source aliases are temporary; global deduplication is pending.

### GDR-SRC-20261010-G10-003

**Simon Tatham and contributors; Black Box contribution credited to James Harvey. [Black Box, Chapter 19](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/blackbox.html).** Simon Tatham’s Portable Puzzle Collection. Date: Publication/update date unknown.

**Edition/build:** Documentation footer 20260923.616da16; no binary or board-game edition played. **Access:** `relevant-excerpt`. **Type:** Primary product documentation. **Inspected locator:** Chapter 19, non-unique layouts and acceptance paragraph; §19.1, check feedback and distinguishing untried beams; §19.2, permitted ball-count variations. Retrieved lines 29–55, 63, 66.

**Limits and independence:** Documentary example only. Matching already-observed probes is not enough when another legal probe distinguishes the layouts. No efficacy experiment. Source family: Tatham. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-004

**Lucas Pope; separately attributed reader reply by mtarini. [TIGSource — August 2017: Return of the Obra Dinn development log](https://dukope.com/devlogs/obra-dinn/tig-30/).** Development Logs by Lucas Pope; creator-hosted mirror of TIGSource. Date: Pope post #734: 2017-08-11; mtarini reply #740: 2017-08-21.

**Edition/build:** Development snapshot; exact executable build unknown, not evidence of every retail version. **Access:** `relevant-excerpt`. **Type:** Firsthand developer account with a separately identified analytical reader objection. **Inspected locator:** Post #734: Fate Validation and SVO Fates; problem/fix discussion preceding them. Reply #740: cycling a third answer after two known ones. Retrieved lines 20–103 and 146–160.

**Limits and independence:** Small informal observations, no exposed comparative dataset. Group validation is not proof against guessing. Alternative descriptions concern accepted fate formulations, not unrestricted alternative histories. Source family: Pope. Mirror and original discussion are one underlying account, not two independent sources. The reader objection is not attributed to Pope and is not a performed exploit test.

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

