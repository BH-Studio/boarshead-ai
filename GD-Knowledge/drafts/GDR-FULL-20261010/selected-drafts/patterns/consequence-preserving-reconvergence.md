---
id: GDR-CAND-20261010-W01-PAT-01
kind: pattern
title: Consequence-preserving reconvergence
version: 0.1.0
status: draft
owner_project: BH-GDR-Worlds-and-Characters
run_id: GDR-FULL-20261010
batch: W01
identity_scope: run-scoped-candidate
candidate_revision: initial
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate; nine supplied files; canonical
  commit not supplied
aliases:
- stateful reconvergence
- consequential bottleneck
- branch and bottleneck with consequence
- branch merging without erasure
tags:
- branching
- agency
- continuity
- content-reuse
- consequence
- production-tradeoff
related_topics:
- GDR-CAND-20261010-W01-TOP-01
- GDR-CAND-20261010-W01-TOP-02
- GDR-CAND-20261010-W01-TOP-03
related_patterns: []
related_genres: []
source_ids:
- GDR-SRC-20261010-W01-01
- GDR-SRC-20261010-W01-02
- GDR-SRC-20261010-W01-03
- GDR-SRC-20261010-W01-04
- GDR-SRC-20261010-W01-05
- GDR-SRC-20261010-W01-14
- GDR-SRC-20261010-W01-15
lead_only_source_ids: []
reviewer: null
approved_by: null
approved_date: null
---

# Consequence-preserving reconvergence

**Research candidate — not released guidance.** This file is complete for bounded W01 drafting, not a claim of exhaustive coverage or accepted evidence. Human research authorization does not approve this entry’s conclusions, game adoption, implementation, publication or permanent identity. No prototype, game execution, participant recruitment or player test was performed.

## Purpose

**Consequence-preserving reconvergence** is a conditional authoring technique for sharing a later event while retaining a relevant difference from earlier player action. The desired outcome is a truthful, bounded influence with manageable content reuse—not an illusion that a shared event is a wholly different story. This is a draft adaptation of known branching practices; it is not a new discovery or a proven player-benefit package. [C-01; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05] [C-03; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03] [C-04; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05]

Use it only when the player’s consequential choice concerns something that can still differ at the shared event. A choice of who receives help can survive arrival at the same destination; a promise to prevent that destination’s destruction cannot be fulfilled by a merge that destroys it unconditionally. [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04] [C-08; GDR-SRC-20261010-W01-01]

## Context and prerequisites

Before applying the recipe, establish the following proposed prerequisites. Failure of a consequential prerequisite is an exit condition, not an invitation to disguise the failure. [C-05; hypothesis]

| Prerequisite | How to establish it | Exit when absent |
|---|---|---|
| A bounded influence promise | State what the player can affect, what remains uncertain and what is fixed. | Narrow or remove the choice until its meaning is honest. |
| Compatible shared event | Explain why every included history can reach the event without undoing its valued distinction. | Keep paths separate or choose another shared event. |
| A relevant retained difference | Identify an opportunity, relationship, resource, commitment, interpretation or closure that actually differs. | Use an explicitly expressive-only choice, or omit it. |
| Feasible later demonstration | Author how the consequence can appear, including absence, interruption and other expected edge cases. | Shorten the consequence horizon or abandon the claim of persistence. |
| Accepted production scope | Identify the authoring, continuity, localization and presentation work before promising broad memory. | Compare a smaller pattern instance or fixed sequence. |
| Conceptual systems feasibility | Confirm separately that the required player-facing states and reactions can be supported. | Retain the document as a proposal; do not imply implementation exists. |

The pattern does not require a particular engine, database, state-machine architecture or autonomous NPC model. It does require a way for the eventual experience to honor the declared difference. No such implementation was built or tested in W01.

## Mechanism and evidence

| Proposed link | What can be supported now | Evidence limit |
|---|---|---|
| Understandable offered influence → a relevant player intention | Agency theory motivates alignment between intentions and supported action. | A design description does not prove the player understood or valued it. [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04] |
| Action → retained difference | Conditional branches can be authored so histories differ beyond a shared node. | This establishes a content relationship, not perceived meaning. [C-01; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05] [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04] |
| Retained difference → relevant follow-through | A later opportunity or response can be written to depend on that history. | Its relevance and visibility to the player are hypotheses. [C-03; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03] |
| Follow-through → recognized influence or trust | Short-form agency studies provide mixed, related evidence. | No inspected study directly validates this recipe, replay trust or equivalence to permanent branching. [C-03; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03] |
| Shared event → lower total cost | Some material may be reused. | Conditional variation and review may exceed the saved work; no measured saving is claimed. [C-04; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05] |

This causal chain is deliberately incomplete as evidence. The technique is testable because the uncertain links are named rather than hidden inside “meaningful choice.”

## Recipe

1. **Write the exact local promise.** Example: “Your delivery determines which equipment the relief team can use at the meeting.” Do not inflate it to “You decide the fate of the whole district” unless that is supportable. Distinguish influence from guaranteed success. [C-05; hypothesis] [C-08; GDR-SRC-20261010-W01-01]
2. **Define the two histories in ordinary language.** Record the chosen action, affected people, changed circumstances and what remains identical. Avoid implementation notation at this stage. [C-05; hypothesis]
3. **Identify the intended shared event.** Explain why it happens under both histories. A scheduled meeting or common destination can be a good candidate; an unconditionally reversed rescue is not a valid merge simply because it is cheap to write. [C-05; hypothesis] [C-08; GDR-SRC-20261010-W01-01]
4. **List the retained obligations.** For each history, state what must remain different at or after the event: available equipment, an owed favor, trust, a witness’s knowledge or an interpretive contrast. Tie each obligation back to the promise. Do not invent an unrelated cosmetic difference as compensation. [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04] [C-05; hypothesis]
5. **Write the shared core and history-sensitive portions.** The core is what is genuinely invariant. The variations supply the actions, opportunities or acknowledgments required by the particular promise. An expressive promise can be met expressively; a resource promise needs the resource distinction or a justified consequence of it. [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04] [C-03; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]
6. **Author a later use or resolution.** Show when the difference matters or how its intended horizon ends. Do not defer it indefinitely. For relationships, determine whether a later change cancels an obligation, complicates it or leaves it unresolved; avoid silently resetting it. [C-05; hypothesis]
7. **Check edge histories.** Consider an absent recipient, refusal to attend, revisit, failure to complete the initial action, and returning after an interruption. Limit the audit to histories the design actually supports. A branch labeled possible must not depend on a character who cannot be present without explanation. [C-05; hypothesis]
8. **Prepare access and localization context.** Record what is known, what is only believed, what must stay uncertain, the relevant relationship and the causal connection to earlier events. Make any recap optional and bounded to appropriate knowledge. Delivery design remains a dependency. [C-06; GDR-SRC-20261010-W01-14; GDR-SRC-20261010-W01-15]
9. **Run a paper consistency review before a player prototype.** Trace the promised contrast through the authored material and identify unsupported exceptions. This is a proposed step; W01 did not execute even a paper playtest. A consistency review can find a contradiction but cannot establish the player-benefit links. [C-05; hypothesis] [C-07; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]
10. **Evaluate and choose an exit or continuation.** Retain the pattern only if the valued distinction is understood and the local production tradeoff is acceptable. Otherwise separate the paths, change the shared event, revise the promise, offer only expression or remove the choice. Do not preserve the topology at the expense of the promise. [C-05; hypothesis] [C-07; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03] [C-08; GDR-SRC-20261010-W01-01]

### Adjustable variables

All values below are local design choices; no universal numerical settings are supplied. [C-05; hypothesis]

| Variable | What can be adjusted | Tradeoff to evaluate |
|---|---|---|
| Influence scope | Expression, information, relationship, opportunity, event or ending. | Broader claims need broader follow-through. |
| Divergence interval | Immediate action, a scene, a session or a longer period. | A longer interval may supply meaningful distinction but more exclusive material. |
| Persistence horizon | When the consequence appears and when its obligation ends. | Long delays increase the need for recoverable context and raise non-exposure risk. |
| Visibility | Direct acknowledgment, changed action, environmental evidence or optional record. | Explicitness can aid attribution or destroy wanted ambiguity. |
| Reversibility | Stable consequence, repairable consequence or acknowledged reset. | Repair can create agency or nullify the original stakes. |
| Shared proportion | What is truly invariant versus conditional. | Apparent reuse may hide extensive variant work. |
| Relationship specificity | A general response versus a response tied to a person’s knowledge and commitments. | Specificity can improve relevance while increasing continuity and localization demands. |

## Worked examples

### Illustrative full instance: the relief assembly

**Synthetic worked example, not an observed game or performed test.** A storm has damaged a small station. The player can recover a pump plan from one room or move medical supplies from another before both rooms become inaccessible. The situation explicitly makes the time conflict visible. Whatever happens, survivors assemble at the same shelter. The assembly is not the object of the player’s control. [C-05; hypothesis]

**Promise:** The selected recovery determines which immediate response the relief team can organize. **Shared event:** People reach the shelter and assess the damage. **Different histories:** The team has either a usable plan for pump work or additional treatment supplies. These are stipulated fictional circumstances, not disaster-response guidance. [C-05; hypothesis]

| Recipe obligation | Plan recovered | Supplies recovered |
|---|---|---|
| Immediate result | A crew member preserves the plan and acknowledges that task. | A colleague receives the supplies and acknowledges that task. |
| Shared core | Arrival, attendance check and statement of the local problem. | The same arrival, attendance check and local problem. |
| Relevant variation | The assembly offers an attempt to organize pump work; treatment remains constrained. | The assembly offers a treatment effort; pump work needs another approach. |
| Later follow-through | The chosen work creates a distinct opportunity and a visible tradeoff. | The chosen work creates a different opportunity and tradeoff. |
| Limit | The plan does not guarantee a successful repair or save every location. | Supplies do not guarantee every injured person’s recovery. |
| Exit case | If pump work is impossible in every authored continuation, the promised use is false. | If all supplies are immediately discarded with no relevant consequence, revise the promise or history. |

The meeting may reuse its location and some dialogue. It cannot present identical capabilities while claiming that the choice determined those capabilities. A side character’s thankful sentence is not interchangeable with the promised operational difference. Whether the distinctions feel important is a question for a later test, not a result of this example. [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04] [C-03; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

**Recovery case:** Suppose the person receiving supplies cannot attend. Another credible evidence route might preserve knowledge of the delivery, but inventing an all-knowing witness merely to display a callback would be a weak repair. Change the route of acknowledgment or consequence within the setting’s knowledge constraints; do not violate continuity to prove the pattern works. [C-05; hypothesis] [C-06; GDR-SRC-20261010-W01-14; GDR-SRC-20261010-W01-15]

### Illustrative smaller instance: rivalry at a shared final

Two competitors always reach a ceremonial final. Earlier, the player either admits an equipment mistake or lets a rival accept blame. The final’s existence does not change, but the rival’s willingness to collaborate on a shared preparation task can differ. This fits the pattern only if relationship consequence was the offered influence. It would not satisfy a promise that the earlier action could eliminate the rival from the competition. [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04] [C-08; GDR-SRC-20261010-W01-01]

Neither example endorses a genre rule. The application depends on the promise and compatible histories, not on a market label.

## Tradeoffs and alternatives

**Full divergence** is preferable when the contested event itself must differ or when reunion erases the relationship’s meaning. Its extra authored material may be justified precisely because the difference is the experience. [C-08; GDR-SRC-20261010-W01-01]

**A fixed sequence with honest participation** can be simpler and better suited to performance, interpretation or witnessing. **An explicitly expressive choice** can acknowledge how the player inhabits a role without pretending to change resources or destiny. Do not treat these as inferior merely because they have fewer downstream branches. [C-05; hypothesis]

**Conditional story units** may suit a broader set of situations better than a single reconvergent meeting. They bring eligibility and continuity work rather than automatically eliminating it. A heavily conditional shared scene can cost more to maintain than separate short scenes. Measure revisions, review and localization along with initial word count. [C-01; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05] [C-04; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05]

## Failure cases

| Failure | Observable warning sign in a future review/test | Candidate correction |
|---|---|---|
| Promise substitution | A world-changing choice receives only a tonal callback. | Honor the original dimension, narrow the wording or remove the choice. [C-08; GDR-SRC-20261010-W01-01] |
| Hidden, irrelevant persistence | A record says the choice is remembered but no valued outcome uses it. | Provide relevant follow-through or stop claiming it matters. [C-03; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03] |
| Forced compatibility | Someone knows an event they could not know; a rescued object disappears without explanation. | Revise the shared event or retain a separate path. [C-05; hypothesis] |
| Delayed non-exposure | Players leave before any promised consequence can appear. | Shorten the horizon or frame the commitment honestly. [C-03; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03] |
| Variant overload | Most of the “shared” scene needs conditional rewriting and repeated review. | Compare separate scenes or reduce scope; reuse is not a goal in itself. [C-04; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05] |
| Inaccessible callback | Attribution depends on an unavailable or forgotten presentation. | Provide an appropriate evidence route without spoiling unknown outcomes. [C-06; GDR-SRC-20261010-W01-14; GDR-SRC-20261010-W01-15] |
| Replay distrust | Once alternatives are seen, the offered influence feels overstated. | Revise structure or promise; do not repair only the first-play impression. [C-07; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03] |

## Counterexamples and do-not-use conditions

Do not use this pattern to guarantee a predetermined outcome while advertising control over that outcome. “Try to persuade the council; success is uncertain” and “Decide whether the building is demolished” are different promises. The former can permit failure; the latter cannot be satisfied by unconditional demolition in every continuation. The actual framing matters. [C-08; GDR-SRC-20261010-W01-01]

Do not use it when a common event is implausible, the only retained difference is unrelated to the choice, the intended experience requires divergent closure, or the team cannot author and review the needed consequences. Also avoid imposing it on a deliberately fixed or opaque work that never needed a choice. [C-05; hypothesis]

This pattern does not prove the necessity of persistence for every expressive interaction, nor a necessity for every character to remember every action. A momentary expression can be enough when that is the scope the work offers. Its exit rules protect the promise; they are not a mandate for exhaustive simulation. [C-02; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-04]

## Playtest

**Status: proposed and not performed.** No players, prototypes, executed stories or measurements exist for this pattern in W01.

**Comparison:** Prepare a truthful fixed/expressive version, this reconvergent version, and a sustained-divergence version where feasible. Hold stakes, polish, exposure, action effort and access support as similar as the design allows. If the consequence scope differs, report that difference rather than attribute all effects to topology. [C-07; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

**Procedure and participants:** Recruit relevant players for the intended experience, including relevant languages and access needs. Capture expectations before the choice without teaching the answer; present the actual later opportunity; ask participants to explain causality and importance in their own terms. Where trust after replay matters, include a separate later disclosure or alternate-path exposure. Counterbalance or separate conditions to address familiarity. [C-07; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

**Measures and confounds:** Distinguish recognition, importance, felt influence, trust, enjoyment, uncertainty and desire for a different outcome. Log production work for writing, revision, continuity, localization and presentation separately. Account for prior genre familiarity, reading burden, moral preference and performance success. These are proposed measures, not a validated composite score. [C-04; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05] [C-07; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

**Falsification and decision:** Reject or revise the application if the player’s valued distinction disappears at reunion, the declared consequence cannot occur, or participants consistently interpret a different promise from the one implemented. Do not dismiss distrust after disclosure because the immediate-response rating was positive. If broader outcomes are equivalent within a later properly designed test but variant maintenance costs more, prefer the simpler alternative. A nonsignificant test alone does not establish that equivalence. Agree quantitative margins, sampling and safety/access procedures before running an authorized study; no universal threshold is supplied. [C-07; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

## Claim ledger

Claim IDs are local to this file. Class and confidence are separate. Proposed applications and tests are not approved studio decisions or performed research. A source attached to an inference identifies its premises, not a direct test of the recommendation.

<a id="claim-c-01"></a>
### C-01 — practitioner-heuristic
Branch-and-bottleneck structures and conditional story units provide practitioner precedents for sharing later content without necessarily discarding every earlier difference.
**Support / contradiction:** The underlying approach is established craft vocabulary; this W01 recipe is an adaptation, not a claim of inventing reconvergence.
**Sources / exact locators:** GDR-SRC-20261010-W01-04: Branch and Bottleneck; GDR-SRC-20261010-W01-05: opening definition; Common Branching Structures and Storylets.
**Applicability:** Authored situations with compatible shared events and contextual variations.
**Confidence:** moderate — explicit practitioner accounts, not efficacy trials.
**Unresolved:** Which kinds of remembered differences are worth the additional authoring work.

<a id="claim-c-02"></a>
### C-02 — inference
If a relevant difference actually persists and affects a later situation, sharing another part of the event does not logically erase that difference; this alone does not prove player recognition or value.
**Support / contradiction:** Logical distinction between shared event structure and differing consequences; does not assert an experimentally measured benefit.
**Sources / exact locators:** GDR-SRC-20261010-W01-01: agency/model/interface discussion, PDF pp. 1–6; GDR-SRC-20261010-W01-04: Branch and Bottleneck.
**Applicability:** A declared local promise whose consequence can be authored and shown.
**Confidence:** moderate — direct reasoning; player-facing interpretation remains uncertain.
**Unresolved:** Whether the retained difference is the one the player believed the choice concerned.

<a id="claim-c-03"></a>
### C-03 — hypothesis
A visible, relevant follow-through may preserve perceived influence after reconvergence, but immediate acknowledgment cannot be presumed equivalent to durable consequence.
**Support / contradiction:** The related short-form studies provide partial and mixed evidence, not a direct test of this pattern or lasting trust.
**Sources / exact locators:** GDR-SRC-20261010-W01-02: PDF pp. 9–10, Tables 1–2 and discussion; GDR-SRC-20261010-W01-03: printed pp. 13–14, results/limitations.
**Applicability:** Local consequence with a demonstrable follow-up and a truthful scope of influence.
**Confidence:** low — central player-benefit link remains untested for this recipe.
**Unresolved:** Replay, disclosure, delayed payoffs, different languages and promises of major world change.

<a id="claim-c-04"></a>
### C-04 — hypothesis
Reusing a shared scene may reduce duplicated material but may increase conditional authoring and review; net savings must be measured rather than assumed.
**Support / contradiction:** Content reuse is a design possibility; the total-cost proposition has no inspected comparative production dataset.
**Sources / exact locators:** GDR-SRC-20261010-W01-04: Branch and Bottleneck; GDR-SRC-20261010-W01-05: Common Branching Structures and Storylets.
**Applicability:** Teams comparing alternatives at the same quality and consequence scope.
**Confidence:** low — plausible tradeoff with unknown balance.
**Unresolved:** Variation, localization, continuity and revision costs under the local workflow.

<a id="claim-c-05"></a>
### C-05 — hypothesis
The proposed recipe should exit when a common event cannot honor the consequential distinction or when maintaining the distinction exceeds the agreed scope.
**Support / contradiction:** Original W01 conditional procedure and exit rules. No implementation or operational trial performed.
**Sources / exact locators:** Original W01 design proposal; no external validation claimed..
**Applicability:** Bounded authoring where a shared future event is optional rather than a fixed command.
**Confidence:** low — proposed workflow, not validated optimization.
**Unresolved:** Whether exiting to divergence, an expressive-only choice or a fixed event better serves the intended experience.

<a id="claim-c-06"></a>
### C-06 — inference
Recoverable known history and a contextual localization handoff can support the visibility of retained consequence, but should not reveal unknown outcomes by default.
**Support / contradiction:** The dependencies are source-informed; the specific known/unknown distinction and effect on the pattern remain proposed.
**Sources / exact locators:** GDR-SRC-20261010-W01-14: narrative review and task-record guidance; GDR-SRC-20261010-W01-15: printed pp. 16–20, context/glossary/style guidance.
**Applicability:** Interrupted play, localized variants and access-sensitive delivery.
**Confidence:** moderate for dependency relevance; low for effect magnitude.
**Unresolved:** Whether support turns intended uncertainty into spoilers or still misses a participant’s access need.

<a id="claim-c-07"></a>
### C-07 — hypothesis
Validation should test interpretation after a consequential follow-up and, where relevant, after replay or disclosure of the merge; a nonsignificant preference result is not evidence of equivalence.
**Support / contradiction:** Proposed response to research limits; no W01 tests, sample-size analysis or equivalence margins exist.
**Sources / exact locators:** GDR-SRC-20261010-W01-02: PDF pp. 9–11; GDR-SRC-20261010-W01-03: printed p. 14, limitations.
**Applicability:** Experiences whose promises extend beyond the immediate response.
**Confidence:** low — evaluation proposal requiring design and approval.
**Unresolved:** Appropriate local margins, sample, tasks, counterbalancing and production measures.

<a id="claim-c-08"></a>
### C-08 — inference
A shared event is inappropriate when the player was offered control over that event itself and the merge unconditionally nullifies that control.
**Support / contradiction:** Reasoned consistency check on the offered influence, not a universal requirement that every desired outcome be attainable.
**Sources / exact locators:** GDR-SRC-20261010-W01-01: agency and supported action relationship, PDF pp. 1–6.
**Applicability:** Choices explicitly framed as changing a particular future event.
**Confidence:** moderate — the contradiction is identifiable from the specification; reactions still vary.
**Unresolved:** Whether the actual promise was control, an attempt under uncertainty, expression or something else.

## References

All access dates are **2026-10-10**. Source identities below are run-scoped candidates, not global SRC allocations. Reuse within W01 is intentional; cross-batch URL/DOI/edition deduplication remains pending. Locators describe material actually inspected, not a claim that the entire linked work or game was examined.

<a id="source-01"></a>
### GDR-SRC-20261010-W01-01
**Noah Wardrip-Fruin; Michael Mateas; Steven Dow; Serdar Sali. _Agency Reconsidered_.** DiGRA 2009. Publication/update: 2009.
**Inspected route:** [Agency Reconsidered](https://www.cs.uky.edu/~sgware/reading/papers/wardripfruin2009agency.pdf).
**DOI:** `10.26503/dl.v2009i1.369`.
**Identity/publisher route:** [record or alternate route](https://dl.digra.org/index.php/dl/article/view/369).
**Edition/build:** Conference paper, nine-page university-hosted PDF; not a current game build. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** PDF pp. 1–6: Introduction; Agency and Drama; Agency and Software Models; Agency and Interfaces.
**Source type:** Primary theoretical paper. **Claims in this entry:** C-02, C-08.
**Limits:** Conceptual argument, not a comparative intervention study. Studies mentioned inside the paper were not independently inspected.
**Independence/provenance:** Shares Mateas and Wardrip-Fruin with source 11; that overlap is not independent corroboration.
**Rights:** © 2009 authors and DiGRA; educational/personal-use notice in paper. No republication rights assumed.

<a id="source-02"></a>
### GDR-SRC-20261010-W01-02
**Matthew William Fendt; Brent Harrison; Stephen G. Ware; Rogelio E. Cardona-Rivera; David L. Roberts. _Achieving the Illusion of Agency_.** Springer, ICIDS 2012, LNCS 7648, pp. 114–125. Publication/update: 2012.
**Inspected route:** [Achieving the Illusion of Agency](https://cs.uky.edu/~sgware/reading/papers/fendt2012achieving.pdf).
**DOI:** `10.1007/978-3-642-34851-8_11`.
**Identity/publisher route:** [record or alternate route](https://scholars.uky.edu/en/publications/achieving-the-illusion-of-agency/).
**Edition/build:** Twelve-page author PDF with internal page numbers 1–12. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** PDF pp. 4–11, §§3–6; Tables 1–2 on PDF p. 9; hypothesis-two result and discussion on PDF p. 10.
**Source type:** Primary empirical paper. **Claims in this entry:** C-03, C-07.
**Limits:** Selected-branch analysis, recruitment/condition demographic differences, optional item responses and short online text stories restrict causal/generalization claims; nonsignificance is not equivalence.
**Independence/provenance:** Shares four authors with source 03. Different study, not an independent replication.
**Rights:** Author manuscript of Springer publication; no source PDF redistributed.

<a id="source-03"></a>
### GDR-SRC-20261010-W01-03
**Rogelio E. Cardona-Rivera; Justus Robertson; Stephen G. Ware; Brent Harrison; David L. Roberts; R. Michael Young. _Foreseeing Meaningful Choices_.** AAAI, AIIDE 10(1), pp. 9–15. Publication/update: 2014-10-08.
**Inspected route:** [Foreseeing Meaningful Choices](https://cdn.aaai.org/ojs/12716/12716-52-16233-1-2-20201228.pdf).
**DOI:** `10.1609/aiide.v10i1.12716`.
**Identity/publisher route:** [record or alternate route](https://ojs.aaai.org/index.php/AIIDE/article/view/12716).
**Edition/build:** Seven-page conference paper; printed pp. 9–15. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Printed pp. 10–14: experiment, results and limitations; Tables 3–6, especially Tables 5–6 on p. 13.
**Source type:** Primary empirical paper. **Claims in this entry:** C-03, C-07.
**Limits:** Snowball sample, retrospective judgments after outcomes, exploratory analysis decisions and uneven scale results. No preregistered equivalence or long-term trust result.
**Independence/provenance:** Overlaps authors with source 02 and Young with source 08. Treat as related research, not independent replication.
**Rights:** © 2014 AAAI. No figures, tables or source PDF reproduced.

<a id="source-04"></a>
### GDR-SRC-20261010-W01-04
**Sam Kabo Ashwell. _Standard Patterns in Choice-Based Games_.** These Heterogenous Tasks, author blog. Publication/update: 2015-01-26.
**Inspected route:** [Standard Patterns in Choice-Based Games](https://heterogenoustasks.wordpress.com/2015/01/26/standard-patterns-in-choice-based-games/).
**Edition/build:** Dated web essay; no numbered revision. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Opening qualification; Branch and Bottleneck; Time Cave; Gauntlet; Open Map; Floating Modules.
**Source type:** Primary practitioner taxonomy. **Claims in this entry:** C-01, C-02, C-04.
**Limits:** Nonexhaustive craft taxonomy with overlapping forms; diagrams and games were not independently evaluated. Title does not make this a formal standard.
**Independence/provenance:** Source 05 explicitly draws on this topology vocabulary; do not count that reuse as independent evidence.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

<a id="source-05"></a>
### GDR-SRC-20261010-W01-05
**Emily Short. _Storylets: You Want Them_.** Emily Short’s Interactive Storytelling, author blog. Publication/update: 2019-11-29.
**Inspected route:** [Storylets: You Want Them](https://emshort.blog/2019/11/29/storylets-you-want-them/).
**Edition/build:** Dated web essay; no numbered revision. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Opening definition and three components; Common Branching Structures and Storylets.
**Source type:** Primary practitioner explanation. **Claims in this entry:** C-01, C-04.
**Limits:** Useful authoring description, not measured evidence that storylets reduce production cost or improve player experience.
**Independence/provenance:** Uses Ashwell/source 04 for branching vocabulary; no independent validation of that taxonomy.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

<a id="source-14"></a>
### GDR-SRC-20261010-W01-14
**Microsoft. _Xbox Accessibility Guideline 109: Objective clarity_.** Microsoft Learn. Publication/update: updated 2026-03-04.
**Inspected route:** [Xbox Accessibility Guideline 109: Objective clarity](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109).
**Edition/build:** Web guideline revision checked 2026-10-10. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Goal; Overview; Scoping questions; implementation guidance on task records and narrative review/recaps.
**Source type:** Primary vendor accessibility guidance. **Claims in this entry:** C-06.
**Limits:** Advisory design guidance, not asserted to be a certification requirement or universally applicable formal standard. No referenced game videos inspected.
**Independence/provenance:** Different evidence function from creative accounts; not empirical confirmation of the proposed recap design.
**Rights:** Microsoft Learn content; specific license terms not inspected. Paraphrase only.

<a id="source-15"></a>
### GDR-SRC-20261010-W01-15
**IGDA Game Localization SIG; Richard Honeywood (initial draft); Jon Fung (second draft); 2021 repost courtesy Wesley Bishop. _Best Practices for Game Localization_.** International Game Developers Association. Publication/update: initial draft 2011-02-01; second draft 2012-02-01; edited repost 2021-04-09.
**Inspected route:** [Best Practices for Game Localization](https://igda-website.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/04/09142137/Best-Practices-for-Game-Localization-v22.pdf).
**Identity/publisher route:** [record or alternate route](https://igda.org/resources-archive/best-practices-for-game-localization/).
**Edition/build:** Cover identifies second draft 2012; filename v22 is not used to infer a verified semantic version. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Printed pp. 16–20 / PDF pp. 19–23: Advice for Development Teams; Familiarization; Glossary and Style Guide; Voice-Over Recording.
**Source type:** Primary practitioner working-group guidance. **Claims in this entry:** C-06.
**Limits:** Dated workflow advice, not a current technical standard or measured cost experiment. Legacy encoding/platform examples and numerical prescriptions excluded.
**Independence/provenance:** Independent working-group advice; not a causal player study.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

## Related entries and history

Related topics: [Narrative structures](../topics/narrative-structures.md), `GDR-CAND-20261010-W01-TOP-01`; [Worldbuilding](../topics/worldbuilding.md), `GDR-CAND-20261010-W01-TOP-02`; [Character design](../topics/character-design.md), `GDR-CAND-20261010-W01-TOP-03`. All are 0.1.0 drafts. No genre entry is supplied or silently assumed.

Batch-local contradictions: `W01-CON-01` (feedback is not established as equivalent to consequence) and `W01-CON-05` (recoverability versus opacity), in the [review packet](../reviews/full-run-20261010-w01-review-packet.md#contradictions).

**2026-10-10 — 0.1.0 draft, initial candidate.** The recipe is author synthesis of inspected craft/theory and limited empirical evidence. Author self-review challenged it; independent review has not occurred. No tests, permanent allocation, adoption or release. Gates C, D and E are not declared passed.
