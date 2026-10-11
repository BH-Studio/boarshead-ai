---
id: GDR-CAND-20261010-W02-PAT-02
kind: pattern
title: Multi-route objective contract
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_id: W02
attempt_id: W02-authoring-attempt-1
owner_project: BH-GDR-Worlds-and-Characters
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate + supplied W02 dispatch, 2026-10-10
aliases:
- outcome-based quest contract
- alternate-resolution recognition
- objective acceptance contract
tags:
- quests
- objectives
- alternatives
- constraints
- resolution
- tracking
related_topics:
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-W02-TOP-02
- GDR-CAND-20261010-W02-TOP-03
related_patterns:
- GDR-CAND-20261010-W02-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-W02-009
- GDR-SRC-20261010-W02-011
- GDR-SRC-20261010-W02-012
- GDR-SRC-20261010-W02-013
- GDR-SRC-20261010-W02-017
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-W02
predecessor_hash: null
supersedes: null
change_summary: Initial W02 submission; no earlier batch artifacts reproduced or replaced.
byte_hash_record: ../reviews/full-run-20261010-w02-review-packet.md#artifact-byte-manifest
---

# Multi-route objective contract

**Draft research candidate — not released guidance.** Candidate identity is run-scoped, not a permanent GDK allocation. No W02 independent review, gameplay prototype or player test has occurred.

## Purpose

Help designers recognize supported ways of resolving a goal without silently reducing the goal to one implementation-specific action or erasing meaningful differences among methods. The proposed benefit is an understandable relationship between **what was asked**, **what was done**, **what counts**, and **what remains consequential**. It does not guarantee more agency, more fun, equal rewards or limitless systemic freedom. [C-01]

## Context and prerequisites

Use when an objective reasonably admits multiple supported methods, or when the current wording accidentally suggests that it does. The team needs a player-understandable outcome, an explicit decision about required/prohibited means, a definition of who accepts the result, and the capacity to recognize method-specific effects. [C-01]

Distinguish four questions conceptually: did the world outcome occur; did it satisfy the agreed conditions; did a particular person accept it; and what rewards or consequences follow? These need not be separate systems or interfaces. They may collapse to one simple statement in a small game, but a conflict between them should not disappear merely because the journal has one checkbox. [C-01, C-04]

**Prerequisite failure:** when a particular method is itself the task, write that requirement honestly and do not broaden it. When alternatives cannot be completed, recognized or maintained within the production scope, narrow the promise or defer the route. “Any solution works” is not an acceptable substitute for determining what actually works. [C-01, C-03]

## Mechanism and evidence

| Proposed link | Support and classification | Evidence boundary |
|---|---|---|
| Stated outcome and means restrictions help players predict acceptance. | Original hypothesis motivated by quest-production examples. [C-01, C-03] | No inspected trial compares this complete contract to alternative objective wording. |
| Feasible routes meet relevant prerequisites and can end coherently. | Structural/generation research supports attention to conditions; application remains an inference. [C-02] | Feasibility is not quality or proof that all player-invented solutions work. |
| Different means remain distinguishable through costs and aftermath. | Proposed interpretation of authored alternatives and reward-recognition concerns. [C-04] | Distinction need not imply equal desirability, reward or ethical treatment. |
| Tracking communicates accepted, partial, rejected or failed outcomes. | Information-access examples motivate reviewing how players recover known state. [C-05] | A current-state summary’s benefit was not tested by those feature descriptions. |
| Recognition improves comprehension/trust without reducing exploration. | Explicit hypothesis for local validation. [C-06] | More explicit wording can spoil the intended discovery or flatten method-essential play. |

This pattern is not a standardized quest schema. The corpus, practitioner account and historical patch record have different evidential roles; combining them does not turn the recipe into an empirically proven technique. [C-01, C-02, C-04]

## Recipe

1. **Write the requested result and why it matters.** Identify who wants it, whether the player has accepted it and what is known about the stakes. A discovered problem can remain a lead until the player commits. [C-01]
2. **Specify means constraints and acceptance.** State required actions, prohibited actions, relevant deadlines or permissions only when they are part of the actual design. Separate temporary relief from durable completion where that distinction matters. Avoid adding hidden constraints simply to preserve one authored route. [C-01]
3. **List supported routes in terms of player decisions.** For each route identify prerequisite knowledge/access/resources, actual action, meaningful cost, failure/withdrawal possibilities, and how its result will be recognized. Do not count different target names as distinct decisions without examining the activity. [C-02, C-03]
4. **Challenge each route with changed order and state.** Ask what happens when the player already has the needed item, discovers the solution before the offer, loses access to an actor, partially resolves the problem or changes their mind. Decide whether the state is valid completion, partial relief, recoverable failure, explicit refusal or an unsupported case requiring redesign. [C-02]
5. **Preserve method consequences.** A common outcome can share closure while retaining debt, damaged relationships, harmed resources or fulfilled promises. Coordinate progression separately; identical numerical rewards do not establish equivalence and different rewards do not automatically invalidate a route. [C-04]
6. **Write acceptance and recovery messages.** Communicate what changed, why the result counts or does not count, and what remains possible. Do not replay a stale objective or classify partial relief as complete restoration. Keep unknown solutions unknown unless the player chooses an appropriate assist. [C-05]
7. **Walk through and evaluate the smallest useful set.** Compare at least the actually claimed alternatives and the strongest excluded method. An author may propose paper walkthroughs before game work; W02 did not execute one. Retain only routes whose promise, recognition and aftermath can be supported. [C-03, C-06]

### Adjustable variables

Adjust breadth of outcome wording, strictness and visibility of means restrictions, route-discovery support, reversibility of commitments, degree of partial resolution, explanation of rejection and the amount of persistent aftermath. Choose reward differences with Foundations and presentation with Presentation. No standard number of methods, graph depth, reward ratio or hint interval is supplied. [C-04, C-05, C-06]

### Exit conditions

Use a single-method objective when the method is the learning, expressive or procedural goal. Use a fixed authored scene when the protagonist’s commitment is not a player choice. Stop adding alternatives when the player cannot distinguish them or production cannot honor the claimed consequence. If the currently approved world rules or quest acceptance authority are unavailable, document the unresolved decision instead of authorizing a result yourself. [C-01, C-06]

## Worked examples

### Illustrative: restore the community’s water

This invented scenario is not shipped-game observation or approved game canon. The initial design asks for reliable water while preserving a downstream irrigation channel. The author must decide whether preservation is a strict condition or a preference whose breach has consequences.

**Contract version A:** “Restore reliable water without disabling the downstream channel.” Repair and a sufficiently sustainable supply agreement are possible routes; unilateral diversion that disables irrigation does not satisfy the agreed conditions. It may still create temporary water and a new situation, so its failure to satisfy the contract should be explained rather than ignored. [C-01, C-04; illustrative]

**Contract version B:** “Get water flowing again.” A diversion may count, but downstream harm remains attributable and can affect the requester’s response. The design must not infer from the shared completion outcome that every method receives identical approval. Changing from A to B is a substantive quest decision, not merely clearer copy. [C-01, C-04; illustrative]

| Case | Recognition under an explicitly chosen contract | Failure signal to audit |
|---|---|---|
| Player already has compatible repair parts | Permit the supported repair without forcing a needless acquisition step, unless authorization is genuinely required. | Quest demands a specific pickup event despite the promised result already being possible. |
| Player arranges one day of deliveries | Record temporary relief unless the accepted reliability criterion is satisfied. | Journal declares permanent completion because any delivery occurred. |
| Player diverts water and harms irrigation | Reject A’s means condition or accept B’s result with the designed aftermath; do not silently switch contracts. | Both contracts produce the same celebratory response and no relevant consequence. |
| Player asks about the supplier but does not accept a debt | Inquiry reveals terms; a later acceptance creates the obligation. | Dialogue inquiry silently activates repayment. |
| Player leaves and returns after circumstances change | Restore the current accepted goal and known constraints, not an obsolete offer. | Re-entry hides that a route closed or repeats an irreversible promise. |

A small team may choose only repair plus one negotiated alternative, or change the goal to temporary relief. That is a legitimate narrowing of scope when reflected in the offer, tracker and resolution. It is not a failure to implement an imagined universal three-route rule. [C-03, C-06; illustrative]

### Illustrative counter-case inside the same setting

An apprenticeship assessment requires the player to isolate the pump safely and replace the failed part. A delivery agreement does not demonstrate the required procedure. Keep the method-specific objective and explain its purpose; the water outcome does not override the assessment. This is the decisive boundary test for the pattern. [C-01; illustrative]

## Tradeoffs and alternatives

A broad outcome can invite experimentation but also increases the gap between imaginable and supported methods. A narrow instruction is easier to communicate and may be exactly right when learning a process or performing a character commitment. A purely systemic opportunity may not need a formal quest at all. The pattern is useful when it clarifies an existing promise, not when it manufactures a contract for every activity. [C-01, C-02]

Shared closure can reduce duplicated authoring, but retaining meaningful aftermath still costs writing, presentation, localization and validation effort. The inspected production sources do not supply a transferable budget threshold. Compare the smallest credible authored alternative rather than assuming generated or branched content is cheaper. [C-03, C-04]

## Failure cases

| Observable warning | Why it matters | Proposed response |
|---|---|---|
| Players repeatedly attempt plausible unsupported methods. | Outcome wording or world affordances imply more freedom than exists. | Implement the actually authorized route, expose the relevant constraint, or narrow the promise. [C-01] |
| A method works but cannot resolve the journal. | Completion appears tied to one route rather than the accepted criterion. | Reconcile recognition, or explain why the criterion was not met. [C-02, C-05] |
| Every alternative becomes the same activity with a different noun. | Output count disguises limited decisions. | Compare action/cost/knowledge differences; remove cosmetic claims of variety. [C-02] |
| One method silently abandons a promise or harm. | Shared outcome erases method meaning. | Retain relevant aftermath or change what the quest claims to accept. [C-04] |
| A translated objective changes a condition. | Different audiences receive different contracts. | Review complete states, not isolated strings, including rejection and partial success. [C-07] |
| Hints reveal the intended solution before discovery. | Clarity has displaced the challenge. | Offer access to known information and separately selectable solution assistance. [C-05, C-06] |

## Counterexamples and do not use conditions

Do not broaden a method-essential objective, erase moral or resource consequences in the name of “player freedom,” or imply that every technically possible action must be recognized. A legitimately impossible or prohibited route may be part of the intended decision. The issue is whether the relevant boundary is understandable and consistent, not whether the player can always prevail. [C-01, C-04]

Do not replace a deliberately open-ended role with artificial completion checkboxes when its ongoing nature is the point. Conversely, do not leave a finite objective permanently unresolved merely to preserve more content. Define what closure means in the local experience and test the simpler alternative. [C-01, C-06]

## Playtest

**Proposed, not performed.** Compare an explicit outcome-with-constraints design to an honest method-specific objective and the existing candidate wording. Keep supported routes and writing/presentation quality comparable where the research question permits. Separate a wording test from adding new content; otherwise improved completion cannot be attributed to the contract. [C-06]

Ask players to predict what counts before acting, then observe considered and attempted routes without coaching them toward the designer’s list. Include already-satisfied, out-of-order, partial-resolution and re-entry cases. Recruit relevant access and language profiles and varying familiarity with the game’s task conventions. Record discoverability, false expectations, explanation of acceptance/rejection, retained consequences and production repair effort separately. [C-05, C-06, C-07]

**Reject or narrow** the pattern when it increases unsupported expectations, makes method-essential goals meaningless, reduces intended discovery, hides harmful consequences, or adds authoring complexity without resolving the targeted misunderstanding. A higher completion rate alone is not enough. Agree locally on practical margins, failure severity and sampling precision before testing; no numerical universal passes the pattern. Confirm transfer on unfamiliar objectives whose deeper constraint differs from the taught example. [C-06]

## Claim ledger

Claim identifiers are local to this artifact. Confidence describes the stated narrow claim, not proof that the proposed technique improves a game. `inference` and `hypothesis` recommendations are author proposals, not approved studio decisions.

### C-01

**Claim:** An explicit outcome-with-means-constraints contract may align expected and actual resolution, while a method-essential objective should remain method-specific.

**Class:** `hypothesis`. **Support/contradiction:** Reasoned recipe, not a tested universal technique.

**Sources and precise locators:** GDR-SRC-20261010-W02-011, GDR-SRC-20261010-W02-013 — Quest production and historical recognition accounts motivate the problem; complete contract is original.

**Applicability:** Only supported, authorized methods and consequences; no unlimited freedom. **Confidence:** low for comparative benefits. **Unresolved:** Does the contract clarify the actual decision without enlarging an unsupported promise?

### C-02

**Claim:** Feasibility, prerequisites and actual decision variation should be checked separately from output volume or quality.

**Class:** `inference`. **Support/contradiction:** Structural evidence informs checks but cannot prove player value.

**Sources and precise locators:** GDR-SRC-20261010-W02-012 — State-sensitive generation and Conclusion/Further Work; p. 2 corpus context.

**Applicability:** Historical MMORPG-derived corpus is not a universal quest grammar. **Confidence:** moderate for the distinction, low for gameplay outcomes. **Unresolved:** Which apparent alternatives change meaningful action, knowledge or cost?

### C-03

**Claim:** A small complete path before expansion is one conditional production alternative, not a required quest topology or fixed route count.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Single practitioner production account.

**Sources and precise locators:** GDR-SRC-20261010-W02-011 — First Playable Draft and Further Iterations.

**Applicability:** Depends on authoring constraints and interaction complexity. **Confidence:** moderate for faithful reporting; efficiency not quantified. **Unresolved:** Does starting small expose or conceal the decisive dependency?

### C-04

**Claim:** Accepted outcomes should not silently erase method-specific obligations, costs, judgments or incentive differences.

**Class:** `inference`. **Support/contradiction:** Conditional synthesis, not a reward-parity standard.

**Sources and precise locators:** GDR-SRC-20261010-W02-011, GDR-SRC-20261010-W02-013 — Alternative outcomes and historical reward-recognition discussion; contract treatment proposed here.

**Applicability:** Requires local narrative and Foundations progression decisions. **Confidence:** moderate for identifying conflicts; low for measured experience benefit. **Unresolved:** Which differences are intended and which accidentally invalidate an alternative?

### C-05

**Claim:** Tracking and re-entry should expose known acceptance conditions and current state through supported access routes without automatically solving unknown challenges.

**Class:** `hypothesis`. **Support/contradiction:** Feature documentation does not test this complete policy.

**Sources and precise locators:** GDR-SRC-20261010-W02-017 — Navigation and Traversal; Text-to-Speech; contract/recap application is original.

**Applicability:** PS4 example is a source of possibilities, not prescribed settings. **Confidence:** low for comparative benefit. **Unresolved:** Does support restore context without spoilers or stale commitments?

### C-06

**Claim:** Expectation, recognition, retained consequence and unfamiliar-case tests can falsify the proposed benefit; none was executed.

**Class:** `hypothesis`. **Support/contradiction:** No gameplay implementation, participant data or passed criterion.

**Sources and precise locators:** Original author proposal; no direct empirical source — Original comparison and stop criteria in this pattern.

**Applicability:** Local priorities, precision and acceptable harms must be specified. **Confidence:** low pending evaluation. **Unresolved:** Does a simpler method-specific or unformalized activity perform better?

### C-07

**Claim:** Review full localized quest states and responses because a changed condition can change the player’s actual contract.

**Class:** `inference`. **Support/contradiction:** Transfer from professional practice, not measured outcome equivalence.

**Sources and precise locators:** GDR-SRC-20261010-W02-009 — LQA context and source-change discussion.

**Applicability:** Review required for relevant locales and supported presentation. **Confidence:** moderate for the semantic dependency, low for proposed workflow benefit. **Unresolved:** Which wording changes acceptance, partial completion or refusal?


## References

Access date for every record below: **2026-10-10**. “Inspected” means the stated text/pages, not an entire linked corpus, game build, video or cited book. Source identities are temporary; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-W02-009

**Jennifer O’Donnell, with the named professional contributors acknowledged in the article.** [How to Get the Most from LQA – What It Is and Best Practices](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/). IGDA. Publication/update: 2023-05-31.

**Edition/build:** Dated professional guidance article. **Access:** `relevant-excerpt`. **Source type:** Practitioner guidance.

**Precise locators used:** What is LQA?; What happens during LQA?; discussion of context, characterization, terminology, UI and source changes during testing.

**Claims supported or constrained in this entry:** C-07. **Limits:** Professional recommendations, not a controlled comparison of localization workflows. **Independence:** Shares the IGDA localization practice network with source 010; not an independent player study.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-011

**Nick Witsel.** [An Iterative Approach to Quest Design](https://www.gamedeveloper.com/design/an-iterative-approach-to-quest-design). Game Developer. Publication/update: 2017-03-20.

**Edition/build:** First-person article about then-in-development Lordbound, a Skyrim mod; not a current-build observation. **Access:** `relevant-excerpt`. **Source type:** Firsthand practitioner account.

**Precise locators used:** First Steps; Quest Design and First Playable Draft; Further Iterations; Conclusion. Prose inspected, screenshots not used as gameplay evidence.

**Claims supported or constrained in this entry:** C-01, C-03, C-04. **Limits:** No usable sample or controlled measurement for the reported player feedback. **Independence:** Independent production context from sources 012 and 013; not an independent player-effect test.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-012

**Jonathon Doran; Ian Parberry.** [A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs](https://ianparberry.com/pubs/pcg2011.pdf). ACM, PCGames 2011 workshop. Publication/update: 2011-06-28 conference date.

**Edition/build:** Eight-page proceedings paper; not the separate earlier technical report. **Access:** `relevant-excerpt`. **Source type:** Original structural corpus research and prototype report.

**Precise locators used:** p. 2, Structural Analysis and Table 1 (screenshot inspected); pp. 5–6, generation/constraints; pp. 7–8, Conclusion and Further Work.

**Claims supported or constrained in this entry:** C-02. **Limits:** Database quest descriptions, not a player-outcome or current-build study. **Independence:** Different from the author’s other quest project summaries; conflicting summary counts were not merged into this edition.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-013

**Larian Studios; official forum post by Jess.** [Community Update #11: Inspiration, Freedom & Pacifism](https://forums.larian.com/ubbthreads.php?Number=740727&ubb=showflat). Larian Studios forums. Publication/update: 2020-12-02 (forum displays 02/12/20).

**Edition/build:** Baldur’s Gate 3 Early Access Patch 3; original announcement post 740727 only. **Access:** `relevant-excerpt`. **Source type:** First-party patch/development account.

**Precise locators used:** Opening patch discussion of experience for avoided combat and dialogue/environmental solutions; following discussion of dialogue checks. Replies excluded.

**Claims supported or constrained in this entry:** C-01, C-04. **Limits:** A historical stated change, not a measured improvement or a current-release guarantee. **Independence:** Separate studio from sources 011, 016 and 017; still self-reported production evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-017

**Matthew Dunnerstick / Naughty Dog.** [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed). Naughty Dog. Publication/update: 2020-06-09; inspected page also contains launch-patch annotations.

**Edition/build:** PS4 launch-era feature description with 1.01/1.02 annotations; not a PS5 Remastered audit. **Access:** `relevant-excerpt`. **Source type:** Official feature documentation.

**Precise locators used:** Navigation and Traversal; Text-to-Speech and Audio Cues; Translation Prompts; Subtitles. Feature-description text inspected, embedded videos not inspected.

**Claims supported or constrained in this entry:** C-05. **Limits:** Documented options are not evidence that the same configuration works for every player. **Independence:** Separate studio from the other creator accounts; no independent comparative user data supplied.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.


## Related entries and history

Primary topic: [Quests and objectives](../topics/quests-and-objectives.md), `GDR-CAND-20261010-W02-TOP-02`. Related: [Dialogue and voice](../topics/dialogue-and-voice.md), `GDR-CAND-20261010-W02-TOP-01`, and [Lore delivery and continuity](../topics/lore-delivery-and-continuity.md), `GDR-CAND-20261010-W02-TOP-03`. Complement: [Intent and response contract](intent-and-response-contract.md), `GDR-CAND-20261010-W02-PAT-01`.

Missing dependencies include reviewed W01 bytes, Foundations progression/economy/systemic-content guidance, Presentation interface/localization guidance and actual game-approved quest outcomes. No unseen IDs or runtime assignments are fabricated. Conflicts `methods-versus-outcomes`, `validity-versus-quality` and `guidance-versus-discovery` remain open in the [packet](../reviews/full-run-20261010-w02-review-packet.md#contradictions-and-contested-claims).

2026-10-10 — version 0.1.0, `initial-draft-1`; initial W02 pattern. Predecessor and supersession null; exact hash in the packet. Author self-review only, independent review and approvals absent. No permanent GDK allocation, release or application is authorized by this artifact.
