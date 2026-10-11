---
id: GDR-CAND-20261010-G17-GEN-01
kind: genre
title: Collectible card game
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G17 author draft; no prior captured G17 revision replaced.
id_scope: run-scoped-temporary
run_id: GDR-FULL-20261010
batch_id: G17
attempt_id: G17-visible-session-20261010-A1
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles; retrieval and file creation on 2026-10-11 UTC
coverage_state: coverage-open
independent_review: not-performed-for-G17
aliases:
- CCG
- collectible card games
- trading card game (boundary-qualified)
tags:
- collection-access
- deck-construction
- formats
- probability
- re-entry
- monetization-experience
- coverage-open
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G17-PAT-01
- GDR-CAND-20261010-G17-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G17-GEN-02
source_ids:
- GDR-SRC-20261010-G17-001
- GDR-SRC-20261010-G17-002
- GDR-SRC-20261010-G17-003
- GDR-SRC-20261010-G17-004
- GDR-SRC-20261010-G17-005
- GDR-SRC-20261010-G17-006
- GDR-SRC-20261010-G17-007
- GDR-SRC-20261010-G17-008
reviewed_dependency_ids:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-P02-PAT-02
reviewer: null
approved_by: null
approved_date: null
---

# Collectible card game

**Complete bounded author draft; coverage remains open.** This file is not a released definition, a legal classification, a balance finding, or an approved game design. Its principal recommendation is to **diagnose collection access separately from decisions made inside a match**. The access-normalized trial proposed below is an optional research instrument, not a requirement that every collectible game remove collection progression. [C-01, C-07, C-13, C-14]

## Decision and scope

Use this entry when choosing how a persistent card pool, deck preparation, match rules, and content acquisition fit together. The questions are: what can this player actually field; what can they learn without acquiring more; what changes when a format or card changes; and which inequalities are intended, disclosed, or outside the intended experience? A card collection’s size, an individual deck’s effectiveness, and a player’s skill are different quantities. [C-01, C-07, C-13]

This batch covers construction, access, match information and tempo, draw probability, formats, rotation/re-entry, acquisition alternatives, and the adaptation obligations created by digital versions. It does not determine an optimal economy, catalogue every CCG, audit current card legality, establish a monetization compliance category, or certify accessibility. Trading markets, tournament operations, collusion, child-specific design evidence, shutdown entitlements, and longitudinal player outcomes remain gaps. [C-01, C-15, C-16]

## Definition and contested boundaries

**Working definition — inference, not a formal taxonomy:** a collectible card game organizes a meaningful part of play around a persistent, extensible pool of individually differentiated cards that players can assemble or select into playable configurations. The consequential feature for this file is the relationship between **persistent access and feasible strategies**. Randomized purchase, player-to-player trading, rarity tiers, competitive play, and real-money acquisition are not assumed necessary. “Collectible” and “trading” are market labels whose overlap must be checked for the specific game. [C-01]

Keep these boundaries separate:

| Neighbor or facet | Distinction used here | Consequence for research |
|---|---|---|
| Deck construction | Preparing a playable configuration before the relevant match | Inspect ownership, copy limits, legality, sideboards and versioned card identity. |
| In-run deckbuilding | Acquiring/removing cards as part of the play trajectory | Inspect acquisition opportunities and cycling within that run, not automatically persistent ownership. |
| Limited play inside a CCG | A constrained event pool and a deck prepared from it | The event’s access rules may differ from account ownership; determine what, if anything, persists. |
| Fixed-distribution expandable card game | Known contents rather than blind selection | An important acquisition countercase, not proof that all players own the same functional options. |
| Board-game adaptation | A digital implementation owes an account of its relationship to an identified tabletop rule set | Rule fidelity, access changes and interface changes need separate records. |
| Platform, synchronous/asynchronous play, cooperative/PvP, live service | Orthogonal facets | Do not create new genre claims merely from storefront tags. |

Arena’s documentation distinguishes constructed, preconstructed and limited contexts and describes temporary All-Access without adding the borrowed cards to a collection. That is evidence of separable access and construction rules, not proof of better learning. [C-02; GDR-SRC-20261010-G17-002]

The 2020 **Dune: Imperium** rule artifact describes deck changes during play, beginning from the same starting cards. It is a counterexample to identifying every game with card acquisition as a persistent-collection CCG. The inspected copy is a publisher-authored rulebook on a mirror; its precise printing is not verified. [C-17; GDR-SRC-20261010-G17-008]

Fantasy Flight’s fixed-distribution LCG description is a useful neighboring model, not a replacement definition for CCGs. A fixed package removes one uncertainty about acquisition contents; it does not remove cost, availability, or strategic asymmetry. [C-03; GDR-SRC-20261010-G17-007]

## Custom research instructions

For future work on this genre, record the **account/collection state, event pool, card-data revision, format, match structure, platform and installed build** before comparing outcomes. “Same game” is insufficient when two queues permit different versions of a card. Check original rules, official format policy, the actual build, and dated economy explanations separately. Do not treat storefront tags, creator goals or an evergreen format list as a complete current specification. [C-02, C-08, C-10, C-16]

Sample contrasts that can change the recommendation: constructed versus limited; supplied decks versus personal collections; a single favored deck versus frequent experimentation; competitive versus cooperative card play; newcomer versus returning expert; fixed versus randomized acquisition; tabletop versus digital-specific card effects. These are research strata, not established demographic proportions. Seek players who reject the proposed trial mode as well as players it might help. [C-12, C-14, C-19]

Challenge four misleading comparisons. A larger collection is not a measured skill level. Equal starting hands do not establish equal long-run strategic opportunity. A popular deck is not necessarily overpowered if exposure, cost or recommendation systems differ. An acquisition probability is not a match-win probability. Preserve these distinctions when coordinating with Foundations and Systems rather than duplicating its economy or evaluation topics. [C-06, C-07, C-13]

## Player promises and varied audiences

Candidate promises include expressing a preferred strategy, learning interactions, accumulating personally valued cards, reacting to changing opponents, and participating with friends despite different collection histories. They are **hypotheses about audience goals**, not universal expectations or measured genre needs. A collector may value persistence that an experimenter experiences as a barrier; a tournament player may prioritize a stable adjudication environment over frequent novelty. [C-12]

The 2022 Arena economy account prioritizes deck iteration and explicitly acknowledges difficulties for frequent deck brewers. It supplies a firsthand statement of a design tradeoff, not independent evidence that its chosen structure was optimal or that all newcomers want the same progression. [C-05; GDR-SRC-20261010-G17-003]

## Characteristic loops and structures

### Persistent access, preparation, match, reconsideration

A useful diagnostic model is **obtain access → construct or select → enter an eligible context → make match decisions → interpret the result → retain, revise or abandon the configuration**. A player can decline acquisition or stop after a satisfactory deck; completion of a collection is not the assumed endpoint. Separately record whether results grant new access, only cosmetic recognition, or neither. This model is an analytical frame, not evidence that every stage increases engagement. [C-01, C-07, C-15]

For an illustrative format, let `E(p,e,c)` be the count of card `c` that player `p` is entitled to use in event `e`, after the event’s own merge rules for owned and loaned access. Let `M(e,c)` be its permitted copy count. A candidate deck count `D(c)` must satisfy `D(c) ≤ min(E(p,e,c), M(e,c))`, card legality, and the event’s total-size and combination constraints. Do not simply add owned and loaned copies when a loan supplies a maximum playset rather than additional copies. Craftable-but-unacquired content is not already owned; a deck preview should not silently spend resources to make itself feasible. [C-07]

This model explains a diagnostic failure: a player might understand a counterstrategy yet be unable to field it. Conversely, granting its cards does not ensure that the player recognizes it, prefers it, or uses it effectively. Label failures separately as **unavailable, illegal, undiscovered, misunderstood, deliberately declined, or ineffective in this matchup**. [C-07, C-09, C-13]

### Information and tempo belong to the match rules

“Tempo” here means the value of initiative and action timing relative to the current objective and response opportunities, not simply playing the cheapest card. The Magic rules’ priority system illustrates why turn ownership, permission to act, and resolution order cannot be collapsed into one “your turn” signal. That is a Magic-specific rules example, not a recommendation to add a stack to every card game. [C-08; GDR-SRC-20261010-G17-001]

When a game has responses, distinguish **selection, payment, commitment, response opportunity and resolution**. Explain the player’s own legal opportunities without exposing a hidden opponent option through a differently timed prompt or a specially worded unavailable-action message. A game intentionally without responses may communicate a simpler turn boundary; adding reaction windows can change its pacing and strategic identity rather than merely improve its interface. [C-09, C-21]

### Probability: define the event before showing a number

**Illustrative mathematical example, not a shipped deck or test result:** with a uniformly shuffled 40-card deck, four qualifying answers and five draws without replacement, no mulligan and no other draw/filter effect, the probability of seeing at least one answer is `1 − C(36,5)/C(40,5)`, approximately **42.7%**. This is a calculated property of those assumptions, not an expected win rate or a recommended deck size. Known draws, replacement, conditional shuffles and multi-card combinations require a different calculation. [C-06]

Acquisition is another stochastic process. Arena’s reward page describes both chosen-card wildcard redemption and rates affected by prior pack outcomes. It therefore cannot be reduced, without further inspection, to repeated independent chances of obtaining a desired finished deck. No pack-opening frequency, acquisition cost or affordability estimate is established here. [C-20; GDR-SRC-20261010-G17-004]

### Formats, versions and return after absence

Separate rotation, a ban, a numerical rebalance, a revised rules interpretation, an expiring loan, and a closed queue. They may all make an old saved deck unusable for the requested activity, but their remedies and ownership implications differ. A record should distinguish “still in your collection,” “currently permitted here,” and “this is the effect this version now has.” [C-07, C-11, C-16]

The September 2026 Arena announcement includes a future October 13 release and a planned February 2, 2027 Alchemy removal. As of this evidence check, those are **announced future events**, not completed changes. The older formats page and a future retirement announcement are not automatically contradictory. A live implementation must recheck the actual event and card data. [C-10; GDR-SRC-20261010-G17-005]

## Design choices and evidence-to-application bridges

| Choice | Conditional reason to consider it | Cost, failure or simpler alternative |
|---|---|---|
| Persistent personal collection in ordinary play | Collection development is part of the chosen promise | Access can constrain experiments. Do not interpret the resulting deck distribution as an unconstrained preference sample. |
| Supplied preconstructed decks | The question concerns match rules rather than construction | Conceals construction knowledge; offer variation later only when that becomes the question. |
| Access-normalized trial pool | The question is whether missing functional content blocks testing a configuration | May not represent ordinary collection-constrained play; can overload a novice or fragment opponents. Use a small, disclosed pool when full access adds no value. |
| Fixed known-content acquisition | The player wants a specific expansion or option rather than uncertain contents | Remaining financial/time/access barriers and dependencies still matter. |
| Rotating legal pool | A design seeks a changing bounded environment | Returning-deck disruption, maintenance and relearning; alternatives include stable pools, separate formats or optional seasonal events. None is universally preferable. |

These recommendations are conditional synthesis [C-07, C-11, C-14, C-15], not causal results inferred from the named products.

**Bridge for the strongest recommendation.** Official temporary-access examples establish that access and ownership can be separated. The deck-feasibility model explains which unavailable configurations become testable. It does **not** establish that extra options improve understanding, satisfaction or ordinary-match balance. Therefore start with a bounded trial only when access is the suspected obstruction; compare it with supplied decks and existing access before adopting it. Reject or narrow it when it fails that diagnostic purpose. [C-02, C-07, C-14]

## Application process

1. **Fix the decision and snapshot.** Choose whether the problem is learning a rule, trying a configuration, joining friends, competitive matchup quality or returning to an old deck. Record actual rule and entitlement versions. Do not make every problem an economy redesign. [C-01, C-16]
2. **Trace one intended configuration.** Can the player find it, determine legality, obtain authorization to use it, understand its costs and enter the intended event? Preserve a no-spend route and distinguish a missing card from a forbidden one. [C-07, C-09, C-15]
3. **Choose a local comparison.** A supplied deck isolates some match demands; an access-normalized pool permits construction; ordinary collections retain the progression constraint. These conditions answer different questions. [C-13, C-14]
4. **Prototype the information boundaries.** Show relevant costs, response timing, card version and event restrictions through usable channels. A private hand stays private in speech, logs and recovery screens. [C-09, C-18]
5. **Evaluate decision quality and preference separately.** Ask what is legal, what can happen, and then what the player prefers. Do not score a soundly explained unconventional deck as misunderstanding. [C-13, C-19; DEP-F01-PAT]
6. **Plan re-entry explicitly.** For an invalid old deck, explain each cause, offer inspection and eligible alternatives, preserve the saved intent, and require a separate informed action for any proposed spend. Teach changed rules as changes, not as a failed transfer check. [C-11; DEP-F01-PAT]
7. **Decide, do not auto-scale.** Keep, narrow or reject the comparison based on the local question and observed harms. The tests below are proposals; no implementation or participant work has occurred. [C-19]

## Applying shared topics

| Inspected related identity | What the genre changes; precise transfer limit |
|---|---|
| `GDR-CAND-20261010-F02-TOP-01` — Decision design | Collection feasibility and hidden-card knowledge constrain apparently reversible choices; revealing a draw cannot be undone by refunding a resource. [DEP-F02-DEC] |
| `GDR-CAND-20261010-P01-TOP-02` — Interface and information | A card needs contextual legality, revision and timing, not only readable body text. Avoid entitlement leaks between players. [DEP-P01-INFO] |
| `GDR-CAND-20261010-P01-TOP-03` — Accessibility and inclusive interaction | Deck construction, private information and response windows need end-to-end access. No CSS-size number is transferred as a native-game rule. [DEP-P01-ACCESS] |
| `GDR-CAND-20261010-F07-TOP-01` — Evaluation and balancing | Account access, matchup, experience and queue selection are distinct conditioning variables. [DEP-F07-EVAL] |
| `GDR-CAND-20261010-F07-TOP-02` — Ethical and sustainable design | Evaluate acquisition, time demands and the ability to decline; disclosure alone is insufficient evidence of an acceptable experience. [DEP-F07-ETHICS] |

Shared **economies and resources**, **progression and rewards**, **multiplayer and social systems**, and **session structure and retention** need their selected reviewed bytes before transfer. The **deckbuilder** neighbor from G16 is not available as a verified reviewed dependency in this snapshot. These are missing links, not new G17 topic artifacts or invented canonical IDs.

## Pattern selection and hybrid adaptations

Use [Access-normalized trial pool](../patterns/access-normalized-trial-pool.md), `GDR-CAND-20261010-G17-PAT-01`, to investigate an access obstruction without promising permanent ownership or equal skill. It is the main candidate for this genre. [C-14]

Use [Information-bounded undo](../patterns/information-bounded-undo.md), `GDR-CAND-20261010-G17-PAT-02`, only in contexts whose stated rules allow recovery. Private deck-editor changes are different from publicly revealing a play, drawing hidden content or observing a response. A digital tabletop hybrid may require separate teaching and competitive policies. [C-09, C-21]

The inspected `GDR-CAND-20261010-F01-PAT-01` supplies the corrected learning distinction: vary a situation while preserving the rule to test transfer; announce and teach a changed card rule as re-entry. The inspected `GDR-CAND-20261010-P02-PAT-02` supplies fact-preserving alternatives, not permission to name hidden cards. Neither dependency’s player benefit was established by this batch. [DEP-F01-PAT; DEP-P02-CUES]

In a CCG/roguelite hybrid, decide separately whether account unlocks affect the offered run pool, whether the run assembles its deck, and whether a trial changes those distributions. Normalizing the full collection can accidentally remove the run’s intended acquisition choices. In a board-game adaptation, a cosmetic collection may coexist with a fixed functional pool; calling it collectible does not prove functional inequality. These are diagnostic hybrid cases, not newly researched genre definitions. [C-21]

## Representative cases, counterexamples and illustrative application

**Historical access versus ownership.** Hearthstone’s 2021 Core announcement describes free, progression-unlocked access with periodic replacement and distinguishes it from ownership in the original set. This is a counterexample to equating “free to use here” with a permanent grant of every corresponding card. Current Hearthstone unlock rules were not verified. [C-04; GDR-SRC-20261010-G17-006]

**Illustrative returning-player case — not a real game observation.** A saved defensive deck fails entry. One card is prohibited by the selected format, two requested copies are absent, and one authorized loan has ended. The recovery screen groups these causes without deleting the saved deck. A preview proposes a legal configuration but does not purchase replacements. The player can inspect the unchanged historical plan, select another eligible event, use a supplied deck where offered, or leave. Test whether people distinguish those choices from restoration of their original ownership; do not claim that every substitute preserves the preferred playstyle. [C-07, C-11, C-15]

**Illustrative tempo case.** A player can spend a limited action now or preserve it for a possible response. A tutor indicates feasibility and timing but does not instruct the player to “always save it.” In the same-rule transfer case, the visible objective changes so immediate use can be preferable. In a later rules revision, the response permission itself changes: that is a separate update-teaching case. The assessment asks first what is possible, then why the player prefers a choice. [C-08, C-09, C-19; DEP-F01-PAT]

**Strong counterexample to unrestricted trial access.** A newcomer seeking one comprehensible starter deck may face more construction work with the complete card pool, while an experienced collector may deliberately value constrained experimentation. Supplying a few coherent alternatives could answer the local question with less burden. No observed population effect is claimed for either response. [C-12, C-14]

## Accessibility, ethics, localization and production

Card art, faction color, miniature icons and animation should not be the only proposed access route to a legally available fact. Examine magnification/reflow, persistent readable card details, keyboard/controller navigation, alternative selection rather than mandatory dragging, and private speech or nonvisual access. These are **candidate accommodations to test**, not certified features. Avoid disclosing opponents’ hidden information through narration, hover descriptions, hand previews or turn-return notifications. [C-09, C-18; DEP-P01-ACCESS; DEP-P02-CUES]

Localization must retain operative distinctions such as optional versus required, target versus affected object, play versus acquire, and current versus future effect. Keep localized names searchable without making an ambiguous translated name the sole functional identity. A small screen can show legal choices progressively, but hiding the reason for illegality can leave a player guessing. Test complete construction-to-match tasks in intended languages and input modes, not just a sample card screenshot. [C-16, C-18]

Economy review should distinguish a price from total expected resources, required prerequisite content, time to a usable configuration, temporary access and future eligibility. A clear disclosure does not establish wellbeing, freedom from pressure or legal compliance. Proposed comparisons use no real purchases. No gambling, consumer-law or jurisdiction-specific classification is inferred. [C-15]

Production obligations include versioned card definitions, format legality, saved-deck interpretation, localization parity, content interaction coverage and access-state correctness. More interaction combinations create more cases to inspect, but this draft supplies neither a numerical test-coverage guarantee nor an engine architecture. Changing a card reopens dependent tutorial and replay expectations. A balance patch is not evidence that all downstream cases were validated. [C-16]

## Research questions and proposed validation

**All tests below are proposed and not performed.** Determine participant counts, duration, practical decision bounds and analysis before recruiting; no arbitrary universal threshold is supplied. [C-19]

| Question and comparison | Participants/context and observations | Confounds and rejection condition |
|---|---|---|
| Does access prevent the intended experiment? Compare ordinary access, supplied alternatives and an access-normalized pool under the same rules | Include players with different collection histories and construction experience. Observe feasible configurations attempted, cost/ownership understanding, time burden and stated preference | Card knowledge, novelty, queue strength and organizer assistance confound results. Reject a universal-access recommendation if it adds no relevant experiment or worsens comprehension/pressure. |
| Can a player return without confusing legality with ownership? Compare grouped-cause recovery with a simple invalid-deck message | Returning players and simulated version changes; ask them to explain each cause and decline all acquisition | Familiarity with card names and changes confounds results. Reject the proposed screen if it causes mistaken permanent-ownership beliefs or unintended spend expectations. |
| Can the player use the match rule without copying a tutor? Compare same-rule varied situations and separately announced changed-rule situations | Include knowledgeable and novice players with their chosen accommodations; ask feasibility, prediction, then preference | Prompt recognition and answer exposure can mimic learning. Reject a mastery claim when correct action selection cannot be distinguished from copying. |
| Is a low-performing configuration weak or access-constrained? Evaluate matched rule versions, exposure, opponents and available alternatives | Define the matchup/skill/access question before collecting data; record uncertainty and repeated-player structure | Aggregate wins, small samples and self-selection are insufficient. Reject a balance conclusion when the plausible alternatives cannot be discriminated. |

### Coverage checkpoint and next discriminating questions

| Area | Researched here | Still open / next question |
|---|---|---|
| Definition and neighbors | Construction, collection, fixed distribution and in-run distinction | Which additional player/community definitions materially change guidance? |
| Access and recovery | Official temporary/historical core models; feasibility synthesis | Does the proposed trial improve the intended decision for collection-constrained users? |
| Probability and tempo | One explicit draw model; selected Magic rule clauses | How do the actual shuffle, mulligan, response and acquisition algorithms change the model? |
| Formats and freshness | Dated announcement versus older living page | Which actual event/build/card snapshot is the implementation targeting? |
| Social, ethical and production effects | Conditional analysis and proposed tests | Selected shared topic bytes; longitudinal and representative-access evidence remain absent. |

## Claim ledger

Confidence describes the stated scope, not universal usefulness. `observed-example` below means **a directly inspected rule/document artifact**, not gameplay personally observed. Local issue labels refer to the [review packet](../reviews/full-run-20261010-g17-review-packet.md#contradictions-and-contested-boundaries).

| Claim | Class | Support and precise locator | Confidence, limit and unresolved issue |
|---|---|---|---|
| C-01: Separate persistent access, configuration and match decisions; use the stated working scope | inference | G17-001 rules 100.2; G17-002 format categories; G17-007 opening; G17-008 p. 6 | Moderate: useful partition, not agreed universal taxonomy. G17-ISSUE-01. |
| C-02: Arena documentation separates event construction/access and temporary All-Access | observed-example | G17-002, Formats and Events; All-Access Events | High for the text; unknown current client/event availability. |
| C-03: Fixed-distribution LCG is a meaningful acquisition countercase | observed-example | G17-007, opening and expansion paragraphs | High for publisher terminology; not equal affordability. G17-ISSUE-01. |
| C-04: Historical Core access did not imply original-set ownership | observed-example | G17-006, Core introduction and ownership FAQ | High for 2021 announcement; no present-day assertion. |
| C-05: The 2022 economy account favors iteration and acknowledges brewer constraints | practitioner-heuristic | G17-003, Economy 101, deck-iteration and brewer paragraphs | Moderate: firsthand rationale, not independent measurement. |
| C-06: The illustrative no-replacement draw probability is approximately 42.7% under its explicit assumptions | inference | Combinatorial derivation in Probability section; locally recomputed with integer combinations | High conditional mathematical result; no gameplay/acquisition outcome. |
| C-07: Format legality and usable entitlement constrain feasible decks independently of understanding | inference | Explicit E/M/D model; G17-001 rules 100; G17-002 All-Access; DEP-F02-DEC | High within model; effect of constraints on experience unknown. G17-ISSUE-02. |
| C-08: A turn label cannot substitute for Magic’s priority/response rules | observed-example | G17-001, 117.1–117.7 | High for identified rules; no all-CCG stack prescription. |
| C-09: Present permitted timing and recovery without exposing hidden facts | inference | DEP-P01-INFO; DEP-F02-DEC; DEP-P02-CUES; G17-001, 401 | Moderate design reasoning; side-channel/usability tests absent. |
| C-10: The September 2026 announcement contains future dated format changes | observed-example | G17-005, Timeline | High for announced schedule; not a completed-change assertion. G17-ISSUE-03. |
| C-11: Cause-specific recovery may reduce ownership/legality confusion without spending | hypothesis | C-07; DEP-F01-PAT; DEP-F07-ETHICS | Low for benefit; returning-player tests required. |
| C-12: Players may value different collection and construction promises | hypothesis | G17-003 as a source of audience distinctions, not prevalence; explicit alternative goals | Low for population expectations; representative investigation absent. |
| C-13: Access, exposure and matchup confound aggregate deck-use/balance conclusions | inference | DEP-F07-EVAL; DEP-F02-DEC; C-07 | Moderate diagnostic reasoning; no G17 balance dataset. |
| C-14: An optional normalized trial may support otherwise blocked experimentation | hypothesis | G17-002 All-Access; G17-006 historical Core; PAT-01 causal chain | Low efficacy confidence; official examples establish mechanisms only. G17-ISSUE-02. |
| C-15: Evaluate acquisition/exit costs separately from disclosure and avoid automatic spending in the proposed recovery | inference | DEP-F07-ETHICS; DEP-F07-EXIT; G17-003 rationale | Moderate conditional design judgment; not approved studio policy or legal advice. |
| C-16: Card/format changes warrant versioned interpretation and dependent content checks | inference | G17-001 edition; G17-005 Timeline; DEP-P01-INFO | Moderate; full rules/content/build matrix uninspected. |
| C-17: Dune’s inspected base rules exemplify in-play deckbuilding | observed-example | G17-008, printed p. 6 Deck Building | Moderate: original rule artifact on unverified mirror; not a current digital observation. |
| C-18: End-to-end alternative access routes require evaluation, not presumed parity | hypothesis | DEP-P01-ACCESS; DEP-P02-CUES; proposed complete-task comparisons | Low for local outcomes; no tested access population. |
| C-19: Proposed tests can discriminate some named explanations if controls and decision criteria are set | hypothesis | Test designs in this file; DEP-F01-PAT; DEP-F07-EVAL | Low until run; no sample-size/power guarantee. |
| C-20: Reward documentation distinguishes chosen redemption from a changing pack mechanism | observed-example | G17-004, wildcard redemption and reset paragraphs | High for documentation; no realized-rate verification. |
| C-21: Hybrid run, collection and adaptation constraints need distinct policies | inference | C-01, C-07, C-09; neighboring board-adaptation draft | Moderate analytical caution; no researched hybrid population. |

In this ledger, `G17-00n` abbreviates the full source identity `GDR-SRC-20261010-G17-00n`; it does not allocate a second identity.

## Review and history

Version **0.1.0**, `candidate_revision: initial-capture-1`; no predecessor or superseded G17 artifact. Author self-review challenged unrestricted trial access, collection-as-skill assumptions and the meaning of transfer. **Independent G17 evidence review, actual-host retrieval and human acceptance are pending.** The source coverage is intentionally narrower than the entire genre. Full artifact hashes and the source-access ledger are in the [exact batch review packet](../reviews/full-run-20261010-g17-review-packet.md).

Next decision: the parent reviewer should verify the access/ownership distinctions and determine whether PAT-01 is sufficiently distinct and supported to retain as a draft pattern. This does not authorize game adoption, publication, source replacement, permanent IDs or release.

## Reviewed dependency provenance

The selected files below were read from the actual waves 1–2 ZIP: **1,994,913 bytes**, SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Supplied Library pointer: `libfile_082dcf2646dc8191af243051d202f4a8`; backing file: `file_00000000b0d881f7a51345657bda5287`; Library version not returned. The archive’s selection receipt reports parent independent review; this author did not perform that review. Each dependency remains **0.1.0 draft**, with null approval fields. Its underlying references were **not** independently reopened merely by reading the dependency.

Local `DEP-*` labels below are locator aliases, not new source allocations. The dependency files are not republished in this G17 package. Their exact IDs remain related-entry pointers; the [batch packet](../reviews/full-run-20261010-g17-review-packet.md#reviewed-dependencies) holds the consolidated transfer and missing-link ledger.

### DEP-F01-PAT
**GDR-CAND-20261010-F01-PAT-01 — Supported attempt and transfer check**, revision `independent-review-correction-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/supported-attempt-and-transfer-check.md`; relevant locator: Purpose; Recipe; Illustrative example, especially the corrected affordability/reservation probes.
**Transferred scope:** Same-rule transfer must distinguish copying from using the relation; changed rules require re-entry teaching; retain access support. **Byte identity:** 32,244 bytes; SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-P01-INFO
**GDR-CAND-20261010-P01-TOP-02 — Interface and information**, revision `review-correction-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/interface-and-information.md`; relevant locator: Information contract and causal-chain discussion.
**Transferred scope:** Player entitlement, certainty, timing and recovery; present access is not proof of usable access. **Byte identity:** 50,777 bytes; SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-P01-ACCESS
**GDR-CAND-20261010-P01-TOP-03 — Accessibility and inclusive interaction**, revision `review-correction-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/accessibility-and-inclusive-interaction.md`; relevant locator: Standards and guidance: edition, clause and applicability; scoped numerical example.
**Transferred scope:** Do not turn web CSS target criteria or vendor guidance into universal native-game thresholds. **Byte identity:** 56,707 bytes; SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-F02-DEC
**GDR-CAND-20261010-F02-TOP-01 — Decision design**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/decision-design.md`; relevant locator: Information contract; Commitment is multidimensional; application/validation discussion.
**Transferred scope:** Restored resources are different from erased knowledge; feasibility and player preference are separate. **Byte identity:** 33,529 bytes; SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-F07-EVAL
**GDR-CAND-20261010-F07-TOP-01 — Evaluation and balancing**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/evaluation-and-balancing.md`; relevant locator: Decision and mechanisms; causal interpretation; balancing scope.
**Transferred scope:** Ownership and exposure can confound usage; aggregate match outcomes do not establish balance. **Byte identity:** 43,446 bytes; SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-F07-ETHICS
**GDR-CAND-20261010-F07-TOP-02 — Ethical and sustainable design**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/ethical-and-sustainable-design.md`; relevant locator: Agency, incentives and full cost; refusal/re-entry discussion.
**Transferred scope:** Disclosure is not proof of freedom from pressure; include time and exit costs. **Byte identity:** 49,049 bytes; SHA-256 `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-F07-EXIT
**GDR-CAND-20261010-F07-PAT-02 — Legible commitment and safe exit**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/legible-commitment-and-safe-exit.md`; relevant locator: Mechanism; context and recipe.
**Transferred scope:** Broad commitment/exit guidance; preserve consequences for other participants rather than promising consequence-free reversibility. **Byte identity:** 22,899 bytes; SHA-256 `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-P02-CUES
**GDR-CAND-20261010-P02-PAT-02 — Fact-preserving cue alternatives**, revision `review-correction-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/fact-preserving-cue-alternatives.md`; relevant locator: Mechanism; recipe and factual-equivalence limits.
**Transferred scope:** Preserve facts, uncertainty, entitlement and timing, not a promise of identical emotion or performance. **Byte identity:** 27,103 bytes; SHA-256 `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

## References

Access checked **2026-10-10, America/Los_Angeles** (retrieval session continued on 2026-10-11 UTC). Exact client builds are unknown unless a cited release note names one; release-note inspection is not client observation. `GDR-SRC-20261010-G17-*` are temporary source identities. Cross-batch URL/DOI/edition deduplication is pending Library Coordination. Lineage-only mentions of other batch source IDs resolve in the [review packet source ledger](../reviews/full-run-20261010-g17-review-packet.md#references); they are not additional supporting sources for this artifact.

### GDR-SRC-20261010-G17-001
**Wizards of the Coast. Magic: The Gathering Comprehensive Rules.** Wizards of the Coast; publication/update: 2026-09-25 (effective date). [Source](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt).
- **Edition/build; locator:** English rules effective September 25, 2026; not an Arena client build. 100.2a–d, 100.4, 100.6; 117.1–117.7; 401.1–401.5.
- **Access/type/provenance:** `relevant-excerpt`; Original game rules / observed rule artifact. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Format-specific exceptions remain. No full-card database, tournament-policy audit, or client conformance test was performed. These are game rules, not a universal formal game-design standard. Same publisher family as G17-002 through G17-005; not independent outcome evidence.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-07–C-09, C-16.

### GDR-SRC-20261010-G17-002
**Wizards of the Coast. MTG Arena Formats.** Wizards of the Coast; publication/update: 2019-10-19 displayed; subsequent revision date unknown. [Source](https://magic.wizards.com/en/news/mtg-arena/mtg-arena-formats).
- **Edition/build; locator:** Mutable HTML; Arena build unknown. Banned and Suspended Cards; MTG Arena Formats and Events; All-Access Events.
- **Access/type/provenance:** `relevant-excerpt`; Official feature/format documentation. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Used only for distinctions and documented temporary access. Its mixed-age format roster is not treated as a verified current schedule or complete current legality list. Same publisher family as G17-001 and G17-003–005; All-Access is one documentation witness, not an efficacy experiment.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-02, C-07, C-14.

### GDR-SRC-20261010-G17-003
**Wizards of the Coast. On the MTG Arena Economy in 2022.** Wizards of the Coast; publication/update: 2022-03-18 displayed; URL includes 2022-03-17. [Source](https://magic.wizards.com/en/news/mtg-arena/mtg-arena-economy-2022-03-17).
- **Edition/build; locator:** Historical 2022 economic rationale; client build unknown. MTG Arena Economy 101: overarching goals; paragraphs on deck iteration and deck brewers.
- **Access/type/provenance:** `relevant-excerpt`; Firsthand publisher rationale / practitioner account. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Intent and acknowledged tradeoffs, not independently measured wellbeing, access, affordability, or retention. No linked video was inspected; no price is transferred as current. Same publisher as G17-001,002,004,005. Publisher statements about its own audience are not independent population evidence.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-05; rationale context for C-12/C-15, not effects.

### GDR-SRC-20261010-G17-004
**Wizards of the Coast. Reward Distribution | Magic: The Gathering Arena.** Wizards of the Coast; publication/update: unknown; mutable page checked 2026-10-10. [Source](https://magic.wizards.com/en/mtgarena/drop-rates).
- **Edition/build; locator:** Live reward documentation; actual client build unknown. Paragraph beginning Wildcards redeem, and following wildcard-rate/reset explanation.
- **Access/type/provenance:** `relevant-excerpt`; Official reward-mechanism documentation. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Only the choice-redemption and state-dependent-rate distinction was inspected for use. No full acquisition model, numerical rate audit, pack purchase, or account test was performed. Same publisher family as G17-001–005; not independent verification of realized reward frequencies.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-20.

### GDR-SRC-20261010-G17-005
**Dave Finseth. MTG Arena State of the Formats 2026.** Wizards of the Coast; publication/update: 2026-09-11. [Source](https://www.magic.wizards.com/en/news/mtg-arena/state-of-the-formats-2026).
- **Edition/build; locator:** Dated announcement; not a verified installed build. How Will This Work?; Rebalanced Cards; Timeline, especially October 13, 2026 and February 2, 2027.
- **Access/type/provenance:** `relevant-excerpt`; Firsthand developer announcement. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Announcements and scheduled future changes are not evidence that those changes already occurred. No format play-rate chart or causal popularity claim is used. Same publisher family as G17-001–004. More recent dated scope information, not a second independent experiment.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-10, C-16.

### GDR-SRC-20261010-G17-006
**Blizzard Entertainment. Introducing the Core Set and Classic Format.** Blizzard Entertainment; publication/update: 2021-02-09; later corrections displayed without a separate revision date. [Source](https://hearthstone.blizzard.com/en-us/news/23620129/introducing-the-core-set-and-classic-format).
- **Edition/build; locator:** Historical 2021 announcement, not current Hearthstone behavior. Introducing the Core Set; FAQ: cost; existing class levels; original-set ownership and yearly replacement.
- **Access/type/provenance:** `relevant-excerpt`; Official historical feature announcement. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Used for a historical access model and its ownership boundary; no current set size, unlock threshold, balance result, or client behavior is asserted. Independent production organization from Wizards; still publisher-authored intent/feature reporting rather than independent player evidence.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-04, C-14 mechanism context.

### GDR-SRC-20261010-G17-007
**Fantasy Flight Games. Living Card Games.** Fantasy Flight Games; publication/update: unknown; checked 2026-10-10. [Source](https://www.fantasyflightgames.com/more/living-card-games/).
- **Edition/build; locator:** Publisher description of LCG distribution; no specific game edition claimed. Opening distribution definition; Core Set and expansion paragraphs.
- **Access/type/provenance:** `relevant-excerpt`; Official publisher definition / market terminology. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Living Card Game is publisher terminology/trademark, not a universal taxonomy. Fixed contents do not establish equal affordability, availability, or competitive strength. Independent publisher source; its marketing claims are not adopted as measured benefits.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-03.

### GDR-SRC-20261010-G17-008
**Paul Dennen (game design); Dire Wolf Digital (publisher). Dune: Imperium Rulebook and appended supplements.** Dire Wolf Digital; inspected copy hosted by 1jour-1jeu; publication/update: 2020 copyright; exact printing/revision of mirror unknown. [Source](https://cdn.1j1ju.com/medias/17/a9/6d-dune-imperium-rulebook.pdf).
- **Edition/build; locator:** English base-game 2020 rule artifact; 20-page PDF including supplements; not Uprising. Printed pp. 6–9: Deck Building, Agents, Intrigue Cards, Round Structure, Agent Turn; p. 15 credits.
- **Access/type/provenance:** `relevant-excerpt`; Original publisher rulebook, inspected through a third-party mirror. Original-rulebook text and screenshots of printed pp. 6 and 9 inspected at the mirror. Publisher discovery route: https://www.direwolfdigital.com/dune-imperium/resources/rules/ ; linked PDF: https://d19y2ttatozxjp.cloudfront.net/pdfs/DUNE_IMPERIUM_Rules_2020_10_26.pdf . No source PDF is redistributed.
- **Limits/independence:** Publisher site links to the dated CloudFront PDF, but that file timed out and the former direct asset URL returned 404. Mirror-to-publisher byte equivalence and exact printing are unverified. Not a paired rules-conformance test of Digital 4.x. Same original work despite multiple retrieval routes. Related Dire Wolf production family as G17-009–011, not independent corroboration.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-17.
