---
id: GDR-CAND-20261010-G16-PAT-02
kind: pattern
title: Cycle-aware deck acquisition
version: 0.1.0
status: draft
candidate_revision: initial-author-draft-1
attempt_id: GDR-FULL-20261010:G16:initial-author-attempt-1
predecessor_sha256: null
supersedes: []
owner_project: BH-GDR-Genres
proposed_shared_owner: BH-GDR-Foundations-and-Systems
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: open
aliases:
- cycle-aware rewards
- acquire retain or replace
- deck-composition choice
tags:
- deck-cycle
- acquisition
- replacement
- refusal
- information-rights
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F02-PAT-01
- GDR-CAND-20261010-G16-PAT-01
related_genres:
- GDR-CAND-20261010-G16-GEN-01
- GDR-CAND-20261010-G16-GEN-02
- GDR-CAND-20261010-G16-GEN-03
source_ids:
- GDR-SRC-20261010-G16-008
- GDR-SRC-20261010-G16-009
- GDR-SRC-20261010-G16-015
- GDR-SRC-20261010-G16-011
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
source_deduplication: pending-library-coordination
---

# Cycle-aware deck acquisition

**Draft pattern; complete benefit unvalidated.** Use this technique to make an acquisition, retention or replacement decision correspond to how the actual deck will supply later actions. It does not prescribe smaller decks, optional rewards everywhere, numerical probability displays or universal removal access. No balance model, prototype or participant session was executed.

## Purpose

Address a specific composition problem: a reward is presented as an unconditional improvement even though its arrival timing, dilution, resource demands or scoring role can conflict with the player’s current plan. The intended outcome is a **state-sensitive composition choice**, not a higher skip rate or equal popularity of every card. [C-01–C-03]

The existing reviewed **Visible opportunity-cost comparison — GDR-CAND-20261010-F02-PAT-01** owns the truthful comparison-display technique. This candidate adds **mechanical control over a circulating action supply**: how an acquisition enters future cycles, what alternatives are available, and when those alternatives should not be offered. Proposed shared ownership is Foundations and Systems; Library Coordination may determine that the incremental pattern should merge or remain only a genre adaptation. [C-09]

## Context and prerequisites

Apply when changing composition during play influences a future hand or cycle and a diagnosed problem concerns taking, retaining or changing cards. The designer must know the actual zones, entry timing, recycle rule, action/resource constraints, goal horizon and legal information visibility. A deck that is merely selected before a match is outside this pattern unless it also has a relevant in-play composition decision. [C-02, C-09]

The game must be able to offer a **genuine** alternative such as no acquisition, a costed replacement, a selected removal or a different reward, without silently destroying its intended challenge. The alternatives must be reachable and understandable; a nominal skip button is not meaningful if it secretly prevents all further progress. The pattern is not appropriate when the intended activity is coping with compulsory additions and that goal is otherwise working. [C-03, C-08]

## Mechanism and evidence

| Proposed link | Support | Limit |
|---|---|---|
| Composition changes future availability through a specific entry/recycle rule. | Documented acquisition and cycling rules; conditional formal reasoning. [C-01, C-02] | Actual behavior differs by game/edition and exception. |
| The player has a meaningful way to preserve or change that supply. | Optional acquisition/removal exists in an inspected rules context. [C-01] | Existence does not prove improved agency, satisfaction or strategic depth. |
| Timing/context information helps the player recognize the consequence. | Reviewed information/opportunity-cost guidance plus game-rule distinctions. [C-02, C-03] | May reveal prohibited information, add cognitive burden or teach a designer-preferred answer. |
| A recognized consequence enables a choice aligned with the player’s objective. | Hypothesized transfer into the proposed game. [C-03, C-07] | The objective may favor a larger deck, compulsory adaptation or collection over efficiency. |
| Context-sensitive diagnostics distinguish useful specialization from weak or inaccessible cards. | Practitioner metrics cautions and reviewed evaluation guidance. [C-06] | No universal usage threshold or causal attribution from a pick-rate dashboard. |

A narrow probability result can support a statement about arrival under its assumptions; it cannot validate the complete chain. Nor can a popular game’s inclusion of removal prove that adding removal will improve another design. [C-01, C-03, C-04]

## Recipe

1. **Define the suspected composition failure.** Record whether players misunderstand arrival timing, accept unwanted additions, lack an intended correction route, or encounter a nonfunctional option. Separate that from knowingly preferring a risky or large collection. If the only concern is that players do not choose the designer’s favorite card, do not deploy the pattern. [C-03, C-06]
2. **Write the zone/cycle contract.** Identify supply, ownership, draw pile, hand, in-play, discard and removed states. Specify where a gain enters, whether unplayed cards are retained, when a recycle occurs and what can modify the default. Treat non-shuffling and exception cases explicitly. [C-02, C-05]
3. **State the player’s relevant horizons and constraints.** Identify the next immediate task, the next usable circulation opportunity and any terminal ownership/scoring value. Include resource/action budgets, prerequisites and supporting cards. A card’s arrival and ability to be used are different facts. [C-02, C-04]
4. **Design the smallest genuine alternative.** Compare acquiring with retaining the present composition; add replacement/removal only when it serves the intended goal. Specify costs, eligibility and destination of changed cards. Preserve compulsory acquisitions where they are the chosen challenge rather than quietly making them optional. [C-01, C-03, C-08]
5. **Communicate entitled consequences, not an answer key.** Make entry timing and known changes inspectable through accessible descriptions or lawful summaries. Do not reveal a hidden draw order, future opponent state or forbidden discard contents. Use a probability only when its denominator/order assumptions are actually known and valid. [C-02, C-04, C-05]
6. **Audit edge states.** Check acquisition immediately before/after a recycle, minimum viable resource supply, empty draw pile, cards temporarily outside the cycle, one-use/exhaust effects, deck-size scoring, forced edits and reachable combinations that invalidate the generic explanation. A default rule must not override an explicit exception. [C-01, C-02, C-05]
7. **Compare choices in their offered context.** For a future approved study, record what was available, eligible and known, plus current resources, remaining horizon, existing composition and relevant experience. Observe declines and failed decks, not only wins or selected cards. [C-06, C-07]
8. **Test understanding separately from preference.** Ask when a card can appear and what becomes feasible before asking what to take. Include a state where an addition serves a known goal and a contrasting state where it does not, plus a timing boundary. A reasonable preference for a large collection is not an error. [C-04, C-07, C-08]
9. **Retain, simplify or remove the intervention.** Keep it only if the diagnosed problem improves while the intended adaptation/collection challenge and information rights remain acceptable. If a richer choice simply turns every offer into a burdensome optimization task, compare a simpler reward or fewer decision points. [C-03, C-06–C-08]

### Adjustable variables

Adjust gain destination, first eligible draw, recycle policy, hand retention, offer-pool rules, alternative cost, removal/replacement eligibility, scoring relationship, revealed lawful information, presentation detail and frequency of composition decisions. Tune numerical parameters locally; neither this pattern nor the cited examples supply an optimum deck size, card count, skip rate or viable-archetype count. [C-02–C-05]

### Exit conditions

Stop without deployment when the zone/timing rule is unknown, the alternative is fake or inaccessible, a summary reveals prohibited information, the deck does not have a relevant future circulation horizon, or allowing refusal/removal defeats the intended challenge. Also stop when the proposed fix relies on a false uniform-random model. A truthful description of the existing acquisition may be sufficient; extra choice is not the default goal. [C-02–C-05, C-08]

## Worked examples

### Illustrative example A: a cycle-sensitive resource offer

A fictional route-planning deck contains ten eligible cards when freshly shuffled, exactly one of which solves a known bridge task. A five-card draw, with no search or extra draws, contains that target with probability `5/10`. Adding two non-target cards before that shuffle changes that narrowly defined arrival probability to `5/12`; removing two non-target cards changes it to `5/8`. This is a symmetry calculation under explicit assumptions, not game telemetry or a recommended deck size. [C-04]

The added cards might nevertheless be the right choice: they could be alternate bridge solutions, provide the resource needed to use the permit, or score at the route’s end. The removal could make the permit unplayable by eliminating loading capacity. A valid explanation distinguishes **chance to draw**, **ability to use**, and **value for the declared goal**. It does not label skip as optimal. [C-02, C-04, C-08]

Suppose the offered card enters discard and the immediate bridge must be crossed before recycling. The offer does not immediately solve that task unless an explicit effect brings it into use. At a later state after recycling, its relevance changes. Ask participants to predict the timing in both states; do not secretly move the acquisition to the hand in one condition and describe the result as transfer of the same rule. A declared rule-change condition can separately test whether people understand a new gain destination. [C-02, C-07]

### Illustrative example B: ordered recycling

A fictional cooperative deck uses an ordered discard-to-draw return. Its current discard order is known under this example’s declared rules. The same acquisition affects the sequence rather than merely a uniform draw probability. The proposed interface explains where the new card joins the sequence and what is legitimately known. It does not compute a random probability simply because other deckbuilders shuffle. [C-02, C-04, C-05]

A negative case grants a discard-order preview in a competitive rule set that prohibits inspecting the discard pile. The preview changes information rights; that is not a harmless convenience. Either preserve the original rule or explicitly design and review a different mode. This example is illustrative; the documentary visibility contrast is in the referenced Dominion and Aeon’s End passages. [C-05, C-07]

### Documentary counterexample: larger can have a purpose

Dominion’s inspected rules include both a removal card and a scoring card whose value depends on deck size. That is enough to reject a universal “thin whenever possible” recipe, without claiming a particular strategy wins a given supply. The correct question is what the present addition/removal does under the current goal and conditions. [C-01, C-08]

## Tradeoffs and alternatives

Optional acquisition can preserve an established plan while reducing the pressure to improvise. Costed replacement can support correction but create additional optimization work and rule exceptions. Automatic upgrades can simplify offers yet remove the intended composition decision. Mandatory additions can preserve a desired disruption challenge but need clear timing and a viable path through it. None is ranked as universally superior. [C-02, C-03, C-08]

A smaller curated offer pool, better availability of a required existing tool, an earlier explanation of cycling or a change to arrival timing may solve the diagnosed problem without adding removal. Conversely, a novel card pool may intentionally ask players to learn unfamiliar relationships; trimming it solely to equalize pick rates can defeat that purpose. Use the existing opportunity-cost pattern only where a truthful feasible comparison helps, not as a compulsory overlay for every card. [C-03, C-06, C-09]

Production implications include text/keyword consistency, checks of boundary timing, extra branches in reward flow and additional localization/access work. These are anticipated obligations, not measured cost estimates. A paper state test can diagnose a timing explanation, but cannot certify real-time input, animated feedback or a long-run metagame. [C-02, C-07]

## Failure cases

| Failure | Warning sign in a proposed evaluation | Candidate response |
|---|---|---|
| A “free” addition is advertised as strictly beneficial. | Participants correctly name a cost to their current cycle that the interface omits. | State the real composition effect; consider a retain alternative when appropriate. |
| A probability uses the whole owned collection as its denominator. | Prediction disagrees with actual eligible draw/retained/exhausted states. | Model the actual zone and conditional order; remove the number when the model is unknown. |
| Removal deletes a necessary enabling resource. | A superficially efficient deck cannot perform a required action. | Check functional prerequisites; do not prescribe a blanket low-card target. |
| Equal pick rates become the balance objective. | A niche card is strengthened until it dominates multiple contexts. | Inspect offer/state/goal-specific use and rationale instead of global parity. |
| Optional edits erase the intended disruption challenge. | People avoid every awkward composition and the declared adaptation goal disappears. | Restore an explicit compulsory category or choose another intervention. |
| Added comparison detail overwhelms the action. | Correct reasoning improves only with excessive assistance or participants no longer want routine offers. | Simplify decisions, reduce frequency or use optional details. |

All warning signs are proposed diagnostics, not observed G16 test results. [C-02–C-08]

## Counterexamples and do-not-use conditions

Do not apply this pattern to an out-of-match collection screen as though it were the same within-cycle problem, to a one-pass deck with no relevant future reuse, or to a game where compulsory acquisitions are an explicitly valued challenge. Do not add cheap removal to a score-for-collection system simply because efficient small decks are familiar. [C-08, C-09]

Do not “help” by exposing unknown order or another player’s private cards, and do not imply that a numerically transparent offer is thereby accessible or fun. The source-specific visibility rules and the inspected no-shuffling default are reasons to make the information/recycle contract explicit rather than assuming a universal interface. [C-03–C-05]

## Proposed playtest and falsification

**Status: proposed / not performed.** Begin with a documented question: for example, whether people knowingly accept a delayed card, misunderstand its first possible arrival, or lack an intended way to retain a functioning deck. Compare the current truthful flow with the targeted alternative using the same offers, resources, goal and rule visibility. A separate condition may test a mechanical rule change, but it must be named as such. [C-03, C-07]

Recruit for relevant familiarity, language, access routes and intended solo/cooperative/competitive use. Preserve ordinary accommodations and lawful information in all conditions. Counterbalance or otherwise account for learning from repeated card sets; record moderator hints. Include an immediate task, a later-cycle task and a terminal ownership goal so a blanket “skip” or “buy” answer cannot masquerade as comprehension. [C-07, C-08]

Measure arrival/legality predictions, functional actions remaining, explanation of the chosen goal, wanted versus unwanted additions, mental effort, accidental actions and perceived disruption. For logged behavior, use actual eligible offers as the denominator and retain failed/abandoned constructions. Prior expertise, content familiarity, novelty, power differences, assistance and cooperation style are possible confounds. Do not treat preference for acquisition as failure merely because a probability decreased. [C-04, C-06, C-07]

**Reject the proposed pattern for this context** if the diagnosed misunderstanding is absent, the alternatives add burden without a locally meaningful composition benefit, or they remove an intended adaptation/collection activity. **Reject the specific implementation** if it leaks prohibited information, uses a false probability model or leaves a required task inaccessible. Set the sample justification and decision thresholds before real testing; no actual counts or favorable outcomes are asserted. [C-03–C-08]

## Related entries and ownership

The principal genre home is [Deckbuilder](../genres/deckbuilder.md). Use its adaptations for a [Roguelike](../genres/roguelike.md) or [Roguelite](../genres/roguelite.md) hybrid only when the specific cycle exists. [Explicit run-state boundary](explicit-run-state-boundary.md) concerns between-attempt state, not a substitute for the card-zone contract.

The inspected shared opportunity-cost and transfer-test candidates keep their identities and are not reissued. Their exact bytes are in the [dependency receipt](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer). Coordination must decide whether this mechanical contribution merits a separate canonical pattern. Conflict references: `G16-CON-03` thinning versus other goals, `G16-CON-04` randomness/visibility, and `G16-CON-06` optional control versus compulsory adaptation. These are packet-local keys only.

## Claim ledger

Claims are local to this artifact. `observed-example` below means an inspected document/rule artifact unless a different route is explicitly given; it does not mean a game was played. Design recipes and proposed tests are not approved studio decisions.

| Claim | Precise claim / classification | Support and exact locator | Confidence and limiting question |
|---|---|---|---|
| C-01 | Official rules show optional acquisition, delayed circulation, removal and goals that can favor a larger deck. **`observed-example`** | `GDR-SRC-20261010-G16-008`; Dominion pp.4–6 and p.12 Chapel/Gardens | **high for the inspected rules, narrow**. Neither optional buying nor removal is a universal deckbuilder requirement; no gameplay outcome observed. |
| C-02 | An acquisition’s impact depends on its entry zone, recycle policy, usable resources, horizon and objective. **`inference`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`, `GDR-CAND-20261010-F02-TOP-01`; Dominion buy/cleanup; Aeon’s End pp.13/15; reviewed D02 horizon | **moderate mechanism confidence**. Uniform random draw is not an assumption that can be transferred to every deck. |
| C-03 | Giving a genuine retain/acquire/replace choice may support intended composition control when forced additions are the diagnosed problem. **`hypothesis`** | `GDR-SRC-20261010-G16-008`, `GDR-CAND-20261010-F02-PAT-01`; Dominion optional buy/removal; reviewed D06 alternatives | **low: the complete pattern has no measured game-level benefit**. More refusal can undermine adaptation, pacing or collection goals; choosing decline is not inherently correct. |
| C-04 | A uniform one-target model changes arrival probability with pool size, but does not determine strategic value. **`inference`** | Author’s explicit reasoning / proposed design, not an external result; Fresh uniform permutation, one target, h draws without replacement: P(arrival)=h/n | **high under explicit assumptions**. Not applicable to arbitrary order, extra draws, unknown state or the chance of winning; worked values are illustrative. |
| C-05 | A non-shuffling default and source-specific visibility rules prevent a universal probability/inspection interface. **`observed-example`** | `GDR-SRC-20261010-G16-009`, `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-015`; Aeon’s End p.15 and default/exception context; Dominion p.9; The Descent description | **moderate for extracted Aeon rules, high for Dominion**. Aeon PDF graphical verification failed; normal recycling is not a claim that exceptions never shuffle. |
| C-06 | Availability-conditioned diagnostics and qualitative context are preferable to treating equal pick rates as a definition of balance. **`practitioner-heuristic`** | `GDR-SRC-20261010-G16-011`, `GDR-CAND-20261010-F07-TOP-01`; GDC pp.7,11,13,16; reviewed D09 competing explanations/denominators | **moderate recommendation support, unvalidated complete workflow**. Creator slides and dashboard are not independent causal validation or raw-data access. |
| C-07 | Worked examples and rejection tests are proposed, with comprehension separated from preference and controlled access routes. **`hypothesis`** | `GDR-CAND-20261010-F01-PAT-01`, `GDR-CAND-20261010-P01-TOP-03`; Reviewed D01 corrected contrasting probes; D04 task-wide access | **low for the new test; no execution**. One correct answer cannot establish transfer or long-term improvement; state versus rule changes distinguished. |
| C-08 | Refusal or removal should not be offered indiscriminately when forced adaptation or growing collections are intended. **`inference`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`, `GDR-CAND-20261010-F02-PAT-01`; Documented contrasting objectives and proposed counterexample; D06 player-goal constraint | **moderate conceptual confidence**. A designer must specify whose goal is being preserved; no universal thinning policy. |
| C-09 | Deck-composition control, comparison-display support and account unlock policy are distinct scopes that need coordinated ownership. **`inference`** | `GDR-CAND-20261010-F02-PAT-01`, `GDR-CAND-20261010-F02-TOP-01`; D06 recipe scope; D02 horizons; G16 genre boundary analysis | **moderate: explicit scope distinction**. Coordination can merge this candidate if its incremental contribution is insufficient; no duplicate canonical concept claimed. |

## References

Access date for every record below: **2026-10-10** (task-local evidence date). A live page or historical rulebook does not certify the current game build. Source identities are temporary except the explicitly reused run-scoped F02 identity; all global allocation/deduplication remains pending.

### GDR-SRC-20261010-G16-008
**Donald X. Vaccarino / Rio Grande Games. [Dominion, Second Edition — rulebook](https://www.riograndegames.com/wp-content/uploads/2016/09/Dominion2nd.pdf).** Rio Grande Games. Publication/update: Copyright 2021; inspected layout footer July 19, 2021. Edition/build: Second Edition, inspected 2021-printing/layout PDF; URL directory is not publication date.
**Inspected locator and access:** Printed pp.3–6 setup, turn, buying and cleanup; p.9 Additional Rules; p.12 Chapel and Gardens. `access: relevant-excerpt`. Type: Primary official tabletop rulebook.
**Limits / provenance:** PDF text plus screenshots of pp.4,5,9,12 inspected. No tabletop session performed; not every expansion/edition. Independent tabletop design context; later digital implementations not assumed equivalent. **Rights:** Copyright Rio Grande Games; brief paraphrases of rules; no card art or PDF redistributed

### GDR-SRC-20261010-G16-009
**Kevin Riley; development Nick Little, Travis R. Chance and Jenny Iglesias. [Aeon’s End — rulebook](https://board-game-rules.com/wp-content/uploads/2025/01/aeons-end_Official-Rules.pdf).** Lone Oak Games / original game publication; retrieved from third-party rules mirror. Publication/update: Copyright 2016; exact printing not identified. Edition/build: 20-page PDF, credits first, printed rule pages 1–19; mirror upload path 2025 is not source edition.
**Inspected locator and access:** Printed p.1 Object; p.4 card-rule precedence; p.5 Crooked Mask mat text; pp.7,11 turn-order deck; p.13 acquisition; p.15 Draw Phase / No Deck Shuffling. `access: relevant-excerpt`. Type: Primary publisher rulebook content on a third-party mirror.
**Limits / provenance:** Parsed text accessible; page screenshots failed (cache/internal errors). No byte identity against an original-publisher copy; graphical layout/card-text verification remains incomplete. Ordinary no-shuffle rule has explicit exceptions in extracted text. Same underlying work as inaccessible 1jour-1jeu mirror. Publisher product pages corroborate family-level description, not this PDF’s exact printing. **Rights:** Copyright 2016 Lone Oak Games; no art or full rules reproduced

### GDR-SRC-20261010-G16-015
**Indie Boards and Cards; designers Nick Little and Kevin Riley. [Aeon’s End: The Descent — product page](https://indieboardsandcards.com/our-games/aeons-end-the-descent/).** Indie Boards and Cards. Publication/update: Update unknown; release label January 2024. Edition/build: The Descent standalone product; not the 2016 base rulebook.
**Inspected locator and access:** Product-description paragraph identifying shuffle-free deck-building and replayable narrative. `access: relevant-excerpt`. Type: Primary publisher description.
**Limits / provenance:** A different installment. Used only to corroborate that the family includes a shuffle-free default, not to fill base-rule gaps. Dependent creator/product-family context with -009 and -014. **Rights:** Copyright publisher; paraphrase

### GDR-SRC-20261010-G16-011
**Anthony Giovannetti, co-founder, Mega Crit. [Slay the Spire: Metrics Driven Design and Balance](https://media.gdcvault.com/gdc2019/presentations/Giovannetti_Anthony_SlayTheSpire.pdf).** Game Developers Conference / GDC Vault. Publication/update: GDC 2019, March 18–22 conference; exact presentation day not verified. Edition/build: 22-page presentation slide deck; game builds vary/unspecified.
**Inspected locator and access:** PDF pp.7,10–11,13–16,21; screenshots inspected for pp.7,11,13,16. `access: relevant-excerpt`. Type: Primary practitioner presentation; documentary metric dashboard.
**Limits / provenance:** Slides are not a full talk transcript. Raw logs, analysis code, controlled comparisons and audience representativeness unavailable. Same Mega Crit context as GDR-SRC-20261010-G16-007. Dashboard data are not a second independent study. **Rights:** Presentation rights retained; paraphrase; no slides/card images redistributed

## Review and history

Version **0.1.0**, revision **initial-author-draft-1**. First G16 submission found in this scoped work; no predecessor artifact is asserted. Assembly edits before first delivery do not create a new conceptual ID. Exact final hashes are in the [review packet](../reviews/full-run-20261010-g16-review-packet.md#candidate-byte-receipt); the packet’s hash is in its separate integrity receipt.

Author self-review is recorded in the packet and is **not independent review**. Independent evidence/content review is pending; local document checks do not constitute host retrieval tests. No research acceptance, permanent identity, publication, implementation or release is claimed. No player study, prototype or game session was performed by G16. Recommendations are reusable proposals, not adoption decisions for any particular game.

The inspected reviewed dependency snapshot remains **draft 0.1.0 / coverage-open**. Relevant exact revisions, hashes and limitations are recorded under [reviewed dependency transfer](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer). Unavailable selected later-wave dependencies remain gaps, not implicit support. Additional pattern ideas are [queued proposals](../reviews/full-run-20261010-g16-review-packet.md#queued-child-proposals), with no child batch keys allocated or sent.
