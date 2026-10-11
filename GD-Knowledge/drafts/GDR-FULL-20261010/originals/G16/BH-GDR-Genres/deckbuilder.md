---
id: GDR-CAND-20261010-G16-GEN-03
kind: genre
title: Deckbuilder
version: 0.1.0
status: draft
candidate_revision: initial-author-draft-1
attempt_id: GDR-FULL-20261010:G16:initial-author-attempt-1
predecessor_sha256: null
supersedes: []
owner_project: BH-GDR-Genres
proposed_shared_owner: null
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: open
aliases:
- deck-building game
- in-play deck construction
- deck-building
tags:
- deck-composition
- draw-order
- acquisition
- removal
- cycle-horizon
- competitive
- cooperative
- noncombat
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
- GDR-CAND-20261010-G16-PAT-02
related_genres:
- GDR-CAND-20261010-G16-GEN-01
- GDR-CAND-20261010-G16-GEN-02
source_ids:
- GDR-SRC-20261010-G16-008
- GDR-SRC-20261010-G16-009
- GDR-SRC-20261010-G16-014
- GDR-SRC-20261010-G16-015
- GDR-SRC-20261010-G16-010
- GDR-SRC-20261010-G16-007
- GDR-SRC-20261010-G16-011
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
source_deduplication: pending-library-coordination
---

# Deckbuilder

**Complete bounded author draft; coverage remains open.** This entry helps a designer distinguish building a deck during play from choosing a preconstructed collection, decide how changes reach future hands, and evaluate acquisition, removal and order uncertainty across single-player, competitive, cooperative and noncombat contexts. No game session, player test or game/balance code was executed.

## Definition and boundaries

The working scope is **a game in which changing deck composition during play is a material strategic activity**. Acquisition, removal, transformation or replacement can alter the player’s future supply of actions or scoring resources. Drawing from an unchanged deck is not, by itself, the activity studied here. Selecting a collection before a match is *deck construction* for this distinction; a hybrid can include both. The boundary is an explicit research convention derived from the inspected examples, not a formal genre standard. [C-01]

A preparation draft can establish a deck without making its construction an ongoing part of play. Conversely, a game can begin with a fixed personal starter and still make in-play acquisition central. Recycling is particularly relevant to many techniques below, but it is not imposed as a universal membership test: a one-pass deck or a design dominated by in-place transformation can require a different analysis. Do not apply the cycle-aware pattern where repeated circulation is absent or irrelevant. [C-01, C-08]

| Neighbor / facet | Distinction that matters here |
|---|---|
| Collectible card game | Owning or obtaining a collection outside the match does not establish in-match deckbuilding. Inspect whether composition changes during the relevant unit of play. The separate genre’s reviewed bytes are unavailable. |
| Card battler | Combat resolved with cards need not include deckbuilding; deckbuilding need not involve combat. |
| Roguelike / roguelite hybrid | The attempt boundary determines whether the current deck resets; account unlocks can change the future acquisition pool without preserving that deck. Use the companion files for that separate question. |
| Board-game adaptation | An adaptation must preserve or deliberately change visibility, order and timing rules; the digital interface cannot assume every physical information constraint is accidental. |
| Solo / cooperative / competitive | These are facets. They change incentives and information rights, not the basic reason for studying composition during play. |

These distinctions do not decide which label a market must use. They prevent copying rules or advice into a context with a different strategic problem. [C-01, C-05, C-06, C-13]

## Custom research instructions

Start with a **zone and timing model**: available supply, owned deck, draw pile, hand, in-play area, discard, temporarily unavailable cards and permanently removed cards. Do not silently use “deck” to mean all of these. Inspect when a gain enters each zone, whether hand contents persist, what forces recycling, which information is visible, and what happens when a draw crosses a pile boundary. A familiar reshuffle loop is not enough to infer another game’s rules. [C-02, C-04, C-05, C-08]

For every proposed acquisition/removal, examine three horizons: the next tactical task, the next relevant deck cycle, and the terminal scoring or victory condition. Ask when the card can first contribute, what it displaces, what resources/action permissions it needs, whether it enables other cards, and whether its value comes from being owned rather than played. These are analytical horizons, not a requirement that every game contain three distinct phases. [C-03, C-08]

Use primary rulebooks, designer accounts with actual rejected iterations, versioned card changes and inspected decision records. Include competitive and cooperative rules, a noncombat example, a non-shuffling default and at least one reason a larger deck can be useful. Challenge recommendations such as “always skip,” “always thin,” “all cards should have equal pick rates,” and “more cards produce more choice.” Do not infer card-level behavior from an official page that only advertises a genre label. [C-03–C-06, C-09, C-15]

For probability claims, state the eligible population, order model, known information, replacement policy and draw modifications. If order is known, conditional or deliberately constructed, do not present a uniform-random probability as a fact. If the rules hide information, an accessible display should communicate available facts rather than silently reveal prohibited contents. For a physical/digital comparison, inspect both actual editions; this batch did not play or verify a digital port. [C-04, C-05, C-07, C-12]

## Player promises and varied audiences

Candidate promises include **building a system from partial resources**, **adapting to available opportunities**, **discovering combinations**, **anticipating future hands**, and **making a personally meaningful or competitively effective composition**. These are design hypotheses, not a claim about all card-game players. Some people may enjoy efficient small engines, others large collections or unstable combinations, and others a cooperative plan or a word-making puzzle. [C-01, C-06, C-08, C-15]

The inspected range supports keeping that variety visible: Dominion supplies a competitive rules context; Aeon’s End describes cooperation and a different recycling model; Paperback’s publisher describes word construction; Mega Crit identifies a digital roguelike/deckbuilder hybrid. None of those examples proves a player preference or a benefit caused by deckbuilding. Physical dexterity, reading load, strategic familiarity and comfort with arithmetic also vary independently of enthusiasm for cards. [C-06, C-12]

## Characteristic loops and mechanisms

### A deck is both an action supply and an evolving commitment

A cycle-oriented diagnostic loop is **obtain a hand → allocate constrained actions/resources → change composition → discard/retain according to rules → draw/recycle → revisit earlier acquisitions**. The relationship between present purchase and later opportunity is the key design question. A card that cannot arrive before the objective ends has a different immediate value from one entering the current hand; either can still matter for ownership-based scoring. [C-02, C-03, C-08]

Dominion’s optional purchase and default gain-to-discard/cleanup rules provide a documented mechanism for delayed influence. Its removal and deck-size scoring examples undermine both “buy everything” and “smaller is always better.” The inference is not that all deckbuilders need the same options, but that composition choices should be evaluated against the actual horizon and objective. [C-02, C-03, C-08]

### Order uncertainty is not a genre requirement

The inspected Aeon’s End rulebook describes an ordinary player-deck recycling rule without shuffling, while a separate turn-order deck is randomized. A separate official The Descent page confirms the publisher’s use of a shuffle-free family description, but is a different installment, not evidence for every 2016 rule. The extracted base-rule text also contains a Crooked Mask-specific reshuffle instruction and a card-over-rulebook precedence clause. Therefore use **non-shuffling default**, not “this game can never shuffle a player deck.” [C-04]

Access qualification: the mirrored base-rule PDF’s text was inspected, but screenshot retrieval failed. Its printed page/section locators are provided; graphical layout and exact printing need follow-up verification. No claim here requires treating the mirror as an authenticated original-publisher byte stream. [C-04, C-05]

The design bridge is that removing one source of randomness can relocate the planning problem to ordering, retention or another uncertain system. It does not prove that the result is easier, deeper or more accessible. A known sequence can burden memory; a randomized sequence can burden contingency planning. Choose the uncertainty appropriate to the intended activity, then test actual comprehension and burden. [C-04, C-08, C-12]

### Illustrative calculation: dilution is conditional, not a strategy rule

Assume a **fresh, uniformly shuffled pool** with exactly one target card, no extra draws or searches, and a five-card hand drawn without replacement. Each position is equally likely to contain the target, so the probability it appears in that hand is `5 / n`, where `n` is the pool size. These are mathematical examples, not observed game data or recommended deck sizes. [C-07]

| Illustrative pool | Target-arrival probability | What can legitimately be concluded |
|---|---:|---|
| Ten eligible cards | 5/10 = 50% | Baseline under the stated model. |
| Add two non-target cards before shuffling | 5/12 ≈ 41.7% | Arrival of this one target in this one hand becomes less likely. |
| Remove two non-target cards before shuffling | 5/8 = 62.5% | Arrival becomes more likely, if the other assumptions remain true. |

This does **not** establish which deck wins. Added cards might be additional solutions, draw more cards, supply necessary resources, protect against another problem or score simply by being owned. Removing an “unwanted” resource can make the target unusable. A partially depleted draw pile, known top card, no-shuffle cycle, changing hand size or multi-copy target requires a different model. Separate arrival probability, legal play and goal value. [C-03, C-07, C-08]

## Design choices and application process

| Decision | Conditional use | Tradeoff / alternative |
|---|---|---|
| Fixed shared supply versus variable offers | A stable set can support planning; changing offers can require adaptation. | Stable sets may repeat solved lines; variable offers can deny a required tool. Consider curated subsets before a huge pool. |
| Optional acquisition versus compulsory reward | Refusal can preserve an existing engine when an offered addition conflicts with it. | Mandatory additions may be the intended challenge. Do not erase this pressure merely to make every reward pleasant. |
| Removal, replacement or transformation | Each can change repeated action supply in a different way. | Removal may shrink needed resources; transformation may preserve identity but alter knowledge demands. Choosing no edit can be valid. |
| Immediate gain versus delayed arrival | Immediate use can solve a current problem; discard arrival asks for future planning. | Delays can be illegible or strategically irrelevant near the end. State timing before comparing strength. |
| Random recycling versus ordered recycling | Supports different forms of contingency or sequence planning. | Neither guarantees strategic depth or access; provide only the information the rules permit. |

These are design hypotheses based on documented alternatives, not a ranking. [C-02–C-05, C-08, C-10, C-16]

Apply them by first identifying the suspected failure—unusable rewards, automatic purchases, dominant loops, misunderstood timing, or inaccessible decision information. Write the zone/timing model and a short reachable example before adding cards. Compare the current system with the smallest relevant alternative; do not change price, rarity, card power and information presentation together while claiming an isolated effect. Then evaluate choices in context and retain, revise or remove the intervention based on the declared player goal. [C-08–C-10, C-14, C-15]

A low pick rate alone cannot tell whether a card is weak, niche, poorly explained, rarely offered in a useful state or disliked. Giovannetti’s practitioner presentation includes card-choice instrumentation, a contextual purpose goal and caution about metrics-only conclusions. The appropriate transfer is to investigate those competing explanations, not to force every card toward equal usage or derive universal balance thresholds from a dashboard image. [C-09]

## Applying shared topics

[Reviewed dependency transfer](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer) identifies exact versions, hashes and inspected passages. No shared source is silently upgraded to released knowledge.

| Reviewed shared identity | What deckbuilding changes |
|---|---|
| GDR-CAND-20261010-F02-TOP-01 — Decision design | Define current versus future value, acquisition timing and legitimate knowledge. Do not compare nominal prices without resource/action constraints. |
| GDR-CAND-20261010-F02-PAT-01 — Visible opportunity-cost comparison | Use only truthful, feasible alternatives. The G16 pattern adds a composition/cycle decision, not a renamed price display. |
| GDR-CAND-20261010-F01-PAT-01 — Supported attempt and transfer check | Test the same recycle rule in contrasting states and at its boundary. Correctly predicting a diluted draw is different from preferring not to buy. |
| GDR-CAND-20261010-P01-TOP-02 / TOP-03 — Interface / Accessibility | Preserve zone identity, timing and information rights across input, magnification or narration. Scoped standards do not supply universal card-font or hit-target settings. |
| GDR-CAND-20261010-F07-TOP-01 — Evaluation and balancing | Track offered opportunities, actual selection context and eligible users. A winning deck sample excludes many failed or abandoned constructions. |

The current reviewed Economies and resources, Progression and rewards, Procedural and authored content, Multiplayer and social systems, Localization and presentation, collectible card game and board-game adaptation entries were not obtained. Their absence limits cross-domain synthesis rather than authorizing duplicate topic text. [C-05, C-08, C-09, C-12, C-13]

## Pattern selection and hybrid adaptations

[Cycle-aware deck acquisition — GDR-CAND-20261010-G16-PAT-02](../patterns/cycle-aware-deck-acquisition.md) applies when acquisition/removal changes a future cycle and the designer suspects a real composition-decision problem. It includes refusal as one option, not a mandatory reward rule. Omit it when the deck does not circulate, editing is entirely pre-match, or forced acquisitions are the desired adaptation challenge. [C-08, C-10, C-16]

[Explicit run-state boundary — GDR-CAND-20261010-G16-PAT-01](../patterns/explicit-run-state-boundary.md) concerns what survives an attempt, not whether a card goes to discard this turn. In a run-based hybrid, separately specify whether the current deck, card unlocks, starting loadouts, narrative and challenge settings persist. A new account unlock may affect the offer pool while leaving the current deck untouched. [C-13]

In competitive play, a richer analytical interface can change an intended memory or hidden-information task. In cooperation, shared planning can help coordinate decks but can also allow one participant to dictate others’ turns; evaluate contribution and control, not only team wins. In a word-building hybrid, a card’s value depends on the player’s lexicon and the target language as well as printed resource value. These are proposed adaptation risks, not measured claims about the representative games. [C-05, C-11, C-12]

## Representative cases and counterexamples

| Case and evidence route | Useful comparison / negative case | Limit |
|---|---|---|
| Dominion, Second Edition, 2021-layout official rules | Competitive acquisition, optional buying, delayed circulation; removal and deck-size scoring prevent a universal thinning rule. | No physical game or digital port tested; expansions not generalized. |
| Aeon’s End, ©2016 mirrored rules plus official publisher pages | Cooperation, non-shuffling default and randomized turn order separate deckbuilding from one specific randomness model. | Parsed PDF only for base rules; screenshots/printing authentication incomplete. The Descent is a separate installment. |
| Paperback Deluxe official description | Noncombat word-making shows that combat is not required by this working deckbuilder scope. | Full rules, dictionary and translations uninspected. |
| Original Slay the Spire official description and GDC slides | Digital run-based hybrid and context-sensitive balance practice. | No gameplay build, raw telemetry or whole talk transcript inspected; slides do not prove efficacy. |

This is a purposive contrast set, not representative sampling of the market. Designers’ public descriptions favor intended strengths; failed designs, less documented regions and players who quit are not adequately represented. [C-02–C-06, C-09, C-15]

### Illustrative worked example: a delivery deck

A fictional noncombat delivery game starts a route with movement, loading and one bridge-crossing permit. An offered second permit appears powerful but enters the discard pile and will not be drawn until after the next recycle. The current route contains no second bridge; a later optional route might. Buying it spends the same resource needed to reserve warehouse space. All rules and values are invented for analysis. [C-08, C-14]

The useful comparison is not “rare card versus common card.” Ask whether another permit is a current solution, future insurance, terminal scoring asset or dead weight for the declared goal. Declining may preserve movement density. Buying may be reasonable for a planned route; removing the only loading card may make an apparently efficient deck unable to complete any delivery. An interface can explain current arrival timing without revealing an intentionally hidden future map. [C-05, C-08, C-10, C-14]

For a contrasting state, make a second bridge a known requirement before the next recycle. Now a card that reaches the discard pile still does not solve an immediate need; an immediate-hand replacement might. The test distinguishes timing understanding from a blanket preference for permits. At the recycle boundary, verify whether the newly acquired card actually joins the eligible pile under the specified sequence. No participants or code were used to test this example. [C-07, C-08, C-14]

## Accessibility, ethics, localization and production

Card-heavy interfaces can demand repeated reading, zone navigation, comparison and sequencing. Candidate access routes include structured card descriptions, consistent state terminology, non-color-only zone cues, controllable animation speed and alternate ways to select or inspect a card. For tabletop play, handling and shuffling are different physical tasks from strategic planning; aids may change those demands without needing to change the rules. All adaptations require actual task testing. [C-12]

Information rights must remain explicit. Dominion’s inspected rules restrict discard inspection, whereas the extracted Aeon’s End rules permit inspecting—but not rearranging—the discard pile. Do not import one convention into the other or assume an accessible summary can expose private state. A deliberately different digital mode can change the contract, but it must be described as a rule change rather than invisible interface polish. [C-05, C-12]

For lexical deckbuilding, translating labels is insufficient if letter availability, word formation, accepted dictionaries or scripts change the underlying action economy. Treat language-specific decks and lexicon validation as a separate design/research problem; include literacy variation and avoid presenting unfamiliarity with one language as poor strategic skill. No edition-specific language balancing or dictionary-rights analysis was performed here. [C-11]

Production costs include wording consistency, interaction exceptions, reachable combination coverage, display expansion and maintaining saved/replayed states when card definitions change. A broader pool adds potential interactions, but the burden depends on the rules’ structure—not merely card count. Do not use rare purchases or future monetized card availability to conceal a missing viable route; commercial/economic and child-facing questions require separate review. These are proposed design guardrails, not findings about any named game or legal compliance advice. [C-08, C-12, C-15]

## Research questions and proposed validation

**All tests are proposed and unperformed.** Select participants for relevant card-rule familiarity, language, input/access needs and solo/cooperative/competitive goals; justify sample size and local decision thresholds before conducting an approved study. [C-14]

| Test | Comparison and procedure | Measures, confounds and rejection condition |
|---|---|---|
| Cycle understanding | Same rules, contrasting draw/discard states and an exact recycle-boundary case. Ask when a gained card can arrive before asking whether to acquire it. | Timing/zone predictions, explanation, access errors. Reject the explanation if it produces a memorized “always buy/skip” answer rather than state-sensitive understanding. |
| Composition control | Compare compulsory acquisition, optional refusal, and a separately costed replacement on matched offers. Include states where an addition helps a declared goal and where it does not. | Reasons, viable later actions, unwanted additions, perceived adaptation and burden. Reject optional refusal if it removes the intended challenge without addressing a demonstrated problem. |
| Contextual card utility | Record eligible offers, resource state, remaining horizon, other owned cards, assistance and prior experience; observe selected and declined cards. | Availability-conditioned use and qualitative rationale, not just winning decks. A low-use niche card is not automatically a balance failure; reject a proposed buff if it only increases dominant combinations. |
| Information/access fidelity | Compare presentation routes that preserve the same legal facts; test longer localized descriptions and interruption/re-entry. | Facts perceived, state/timing errors, accidental actions and task burden. Reject an adaptation that reveals prohibited information or blocks a necessary task, regardless of win rate. |

The strongest opposing case is **compulsory adaptation**: receiving awkward cards may be the designed problem, not a defective reward. The pattern is justified only if the designer wants composition control at that point and the test supports its benefit. It should not turn every disruptive event into an optional transaction. [C-10, C-16]

## Coverage and next discriminating question

Researched: in-play construction boundary; acquisition/removal; draw/order uncertainty; delayed horizons; mathematical limits; solo/competitive/cooperative/noncombat contrasts; information rights; hybrid, access and localization implications. Still open: actual digital builds, interaction datasets, competitive metagames, localized lexicons, participant effects, and later reviewed shared dependencies. Complete sections do not certify complete genre coverage.

Next decision: **Is the central pleasure acquiring options, engineering repeated access, adapting to imposed cards, scoring a collection, or constructing words—and which part of that activity would refusal, removal or added randomness actually change?** Answer that before treating a larger or thinner deck as the design target. [C-08, C-10, C-15, C-16]

## Claim ledger

Claims are local to this artifact. `observed-example` below means an inspected document/rule artifact unless a different route is explicitly given; it does not mean a game was played. Design recipes and proposed tests are not approved studio decisions.

| Claim | Precise claim / classification | Support and exact locator | Confidence and limiting question |
|---|---|---|---|
| C-01 | For this entry, deckbuilding means strategically changing deck composition during play; pre-match construction alone is a neighboring activity. **`inference`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`, `GDR-SRC-20261010-G16-010`, `GDR-SRC-20261010-G16-007`; Dominion pp.3–6; Aeon’s End pp.4,13,15; Paperback description; Mega Crit original game section | **moderate working-definition confidence**. Not an official genre standard; variants can combine preconstruction, drafting and in-play changes. |
| C-02 | Dominion’s documented buy/cleanup/recycle rules make acquisition affect later hands; buying is optional. **`observed-example`** | `GDR-SRC-20261010-G16-008`; Printed pp.4–6, especially Buy Phase and Cleanup | **high for the inspected second-edition rules**. No play session, expansion or digital port tested; timing of other games’ gains may differ. |
| C-03 | Deck thinning is not universally beneficial: Dominion documents both removal and a scoring incentive connected to deck size. **`observed-example`** | `GDR-SRC-20261010-G16-008`; Printed p.12 Chapel and Gardens; rulebook screenshots inspected | **high for this rules contrast**. Not a universal recommendation to trash or bloat; actual card value depends on the state and goal. |
| C-04 | A deckbuilder need not randomize the player deck on ordinary recycling; randomness can concern another state such as turn order. **`observed-example`** | `GDR-SRC-20261010-G16-009`, `GDR-SRC-20261010-G16-014`, `GDR-SRC-20261010-G16-015`; 2016 rules pp.7,11,15; The Descent description | **moderate: parsed primary rules plus official family-level corroboration**. PDF visual checks failed. The default has exceptions; do not claim absolutely no player-deck shuffling anywhere or merge editions. |
| C-05 | Information visibility is part of the rules, not a generic permission to expose all deck/discard contents. **`observed-example`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`; Dominion p.9 Additional Rules; Aeon’s End p.15 Notes | **high for Dominion text/screenshots; moderate for Aeon’s End extracted text**. Accessibility adaptation must preserve lawful task facts; competitive hidden-information rules are not automatically overridden. |
| C-06 | The inspected range includes competitive tabletop, cooperative deckbuilding, noncombat word-building and a single-player digital hybrid. **`observed-example`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`, `GDR-SRC-20261010-G16-014`, `GDR-SRC-20261010-G16-010`, `GDR-SRC-20261010-G16-007`; Rulebook object/setup sections and the named official product descriptions | **moderate: documentary range, not a market census**. Actual matches/builds not run; physical/digital production and diverse audiences remain insufficiently sampled. |
| C-07 | With one target in a fresh uniformly shuffled pool of n cards and an h-card draw without replacement, the target-arrival probability is h/n. **`inference`** | Author’s explicit reasoning / proposed design, not an external result; Symmetry of a uniform permutation; mathematical worked example in this artifact | **high under explicit assumptions**. Arrival is not playability, utility or victory. Not valid for unknown/nonuniform order, partial-cycle conditioning, extra draw or changing h. |
| C-08 | The effect of an acquisition depends on arrival delay, cycle horizon, resource/action constraints, synergy and terminal scoring, not only printed card strength. **`inference`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`, `GDR-CAND-20261010-F02-TOP-01`; Dominion buy/cleanup and Chapel/Gardens; Aeon’s End acquisition/draw; reviewed D02 horizon | **moderate mechanism confidence**. The best choice is state/goal-specific; no universal minimum deck size or number of viable cards. |
| C-09 | GDC’s card-choice dashboard and contextual-card goal support inspecting availability and build context, not flattening every pick rate. **`practitioner-heuristic`** | `GDR-SRC-20261010-G16-011`; GDC slides pp.7,10–11,13,16 | **high attribution, low causal generalization**. No raw logs or independent replication; the presentation itself cautions against metrics-only conclusions. |
| C-10 | Optional acquisition or conditional removal can make composition an active decision, but may harm designs based on compulsory adaptation. **`hypothesis`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`, `GDR-CAND-20261010-F02-PAT-01`; Dominion optional buy/removal; Aeon’s End acquisition; reviewed D06 comparison boundaries | **low for the complete proposed pattern**. Compare mandatory rewards and other interventions; more refusal is not inherently better or smarter. |
| C-11 | Lexical deckbuilding localization can require redesign of letter economy and rule evaluation, not just translating card names. **`hypothesis`** | `GDR-SRC-20261010-G16-010`; Paperback word/letter acquisition description; author’s mechanism analysis | **low: no localized edition or dictionary tested**. Language morphology, accepted lexicon, familiarity, scripts and rights require specialist validation; no universal letter frequencies inferred. |
| C-12 | Card text, zone navigation, sequencing and physical shuffling introduce different access demands. **`hypothesis`** | `GDR-CAND-20261010-P01-TOP-03`, `GDR-CAND-20261010-P01-TOP-02`, `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`; Reviewed D04/D05 task chain; source-specific card/zone rules | **low for any particular assist implementation; moderate diagnostic rationale**. No device, screen reader, tabletop access aid or translated build tested; no universal numeric UI thresholds. |
| C-13 | Hybrid run loss and account unlocks change different parts of the deckbuilding problem and should be assessed separately. **`inference`** | `GDR-SRC-20261010-G16-007`, `GDR-SRC-20261010-G16-011`, `GDR-CAND-20261010-F02-TOP-01`; Original Slay the Spire hybrid label; GDC modes/context; reviewed D02 horizons | **moderate: conditional analysis**. Do not infer exact unlock tables from the product page or treat account growth as within-run deckbuilding. |
| C-14 | The courier/logistics example and proposed deck comparisons are illustrative; their outcome claims remain untested. **`hypothesis`** | Author’s explicit reasoning / proposed design, not an external result; Worked example and validation section | **low: proposal only**. No actual balance simulation, player session or commercial product observation created in G16. |
| C-15 | More cards can create more combinations without creating more useful or comprehensible decisions. **`inference`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-011`, `GDR-CAND-20261010-F02-TOP-01`; Dominion timing/scoring countercases; GDC p.7 and p.13; reviewed D02 option count | **moderate: plausible structural distinction, unknown effect size**. Do not presume fewer cards always improve choice; deliberate collection and discovery are valid competing goals. |
| C-16 | The strongest countercase to a refusal/removal recommendation is a design where unwanted acquisitions are the intended adaptation challenge. **`inference`** | `GDR-SRC-20261010-G16-008`, `GDR-SRC-20261010-G16-009`, `GDR-CAND-20261010-F02-PAT-01`; Contrasting rules and proposed compulsory-acquisition case; D06 player-goal boundary | **moderate conceptual confidence**. Requires a declared goal and comparison, not evidence that compulsory rewards are generally preferable. |

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

### GDR-SRC-20261010-G16-014
**Indie Boards and Cards. [Aeon’s End — product page](https://indieboardsandcards.com/our-games/aeons-end/).** Indie Boards and Cards. Publication/update: Update unknown; release label September 2017. Edition/build: Product page, SKU IBCAED2; no played copy inspected.
**Inspected locator and access:** Game description: cooperation, variable turn order and discard planning. `access: relevant-excerpt`. Type: Primary publisher description.
**Limits / provenance:** Corroborates broad product description, not exact edition-specific rules or effects. Same product family as GDR-SRC-20261010-G16-009 and -015; not independent outcome evidence. **Rights:** Copyright publisher; paraphrase

### GDR-SRC-20261010-G16-015
**Indie Boards and Cards; designers Nick Little and Kevin Riley. [Aeon’s End: The Descent — product page](https://indieboardsandcards.com/our-games/aeons-end-the-descent/).** Indie Boards and Cards. Publication/update: Update unknown; release label January 2024. Edition/build: The Descent standalone product; not the 2016 base rulebook.
**Inspected locator and access:** Product-description paragraph identifying shuffle-free deck-building and replayable narrative. `access: relevant-excerpt`. Type: Primary publisher description.
**Limits / provenance:** A different installment. Used only to corroborate that the family includes a shuffle-free default, not to fill base-rule gaps. Dependent creator/product-family context with -009 and -014. **Rights:** Copyright publisher; paraphrase

### GDR-SRC-20261010-G16-010
**Fowers Games. [Paperback — Deluxe product page](https://www.fowers.games/products/copy-of-paperback-deluxe).** Fowers Games. Publication/update: Unknown. Edition/build: Deluxe listing; complete edition-specific rulebook not inspected.
**Inspected locator and access:** Description of starting letters/wilds, making words, acquiring letters and scoring wilds. `access: relevant-excerpt`. Type: Primary publisher product description.
**Limits / provenance:** Narrow documentary noncombat/word-building example. No dictionary, localization pack, detailed rules or player session inspected. Distinct creator context; localization conclusions are G16 hypotheses, not publisher-validated results. **Rights:** Copyright Fowers Games; paraphrase only

### GDR-SRC-20261010-G16-007
**Mega Crit. [Games — Slay the Spire section](https://www.megacrit.com/games/).** Mega Crit. Publication/update: Unknown. Edition/build: Original Slay the Spire section only; not the separate sequel section; build unknown.
**Inspected locator and access:** Original Slay the Spire heading and description. `access: relevant-excerpt`. Type: Primary creator product description.
**Limits / provenance:** Only establishes the creator’s hybrid description, not detailed rules or commercial causation. Same studio/game as GDR-SRC-20261010-G16-011, not independent triangulation. **Rights:** Copyright Mega Crit; paraphrase

### GDR-SRC-20261010-G16-011
**Anthony Giovannetti, co-founder, Mega Crit. [Slay the Spire: Metrics Driven Design and Balance](https://media.gdcvault.com/gdc2019/presentations/Giovannetti_Anthony_SlayTheSpire.pdf).** Game Developers Conference / GDC Vault. Publication/update: GDC 2019, March 18–22 conference; exact presentation day not verified. Edition/build: 22-page presentation slide deck; game builds vary/unspecified.
**Inspected locator and access:** PDF pp.7,10–11,13–16,21; screenshots inspected for pp.7,11,13,16. `access: relevant-excerpt`. Type: Primary practitioner presentation; documentary metric dashboard.
**Limits / provenance:** Slides are not a full talk transcript. Raw logs, analysis code, controlled comparisons and audience representativeness unavailable. Same Mega Crit context as GDR-SRC-20261010-G16-007. Dashboard data are not a second independent study. **Rights:** Presentation rights retained; paraphrase; no slides/card images redistributed

## Review and history

Version **0.1.0**, revision **initial-author-draft-1**. First G16 submission found in this scoped work; no predecessor artifact is asserted. Assembly edits before first delivery do not create a new conceptual ID. Exact final hashes are in the [review packet](../reviews/full-run-20261010-g16-review-packet.md#candidate-byte-receipt); the packet’s hash is in its separate integrity receipt.

Author self-review is recorded in the packet and is **not independent review**. Independent evidence/content review is pending; local document checks do not constitute host retrieval tests. No research acceptance, permanent identity, publication, implementation or release is claimed. No player study, prototype or game session was performed by G16. Recommendations are reusable proposals, not adoption decisions for any particular game.

The inspected reviewed dependency snapshot remains **draft 0.1.0 / coverage-open**. Relevant exact revisions, hashes and limitations are recorded under [reviewed dependency transfer](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer). Unavailable selected later-wave dependencies remain gaps, not implicit support. Additional pattern ideas are [queued proposals](../reviews/full-run-20261010-g16-review-packet.md#queued-child-proposals), with no child batch keys allocated or sent.
