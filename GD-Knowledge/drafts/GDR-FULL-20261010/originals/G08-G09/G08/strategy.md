---
id: GDR-CAND-20261010-G08-GEN-01
kind: genre
title: Strategy
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_id: G08-authoring-01
run_id: GDR-FULL-20261010
batch_id: G08
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles
coverage_state: open
aliases:
- strategic planning
- strategy family
tags:
- planning
- commitment
- resource-allocation
- cooperation
- noncombat
- hybrid-boundaries
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-W02-TOP-02
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G08-PAT-01
- GDR-CAND-20261010-G08-PAT-02
related_genres:
- GDR-CAND-20261010-G08-GEN-02
- GDR-CAND-20261010-G08-GEN-03
source_ids:
- GDR-SRC-20261010-G08-008
- GDR-SRC-20261010-G08-009
- GDR-SRC-20261010-G08-012
- GDR-SRC-20261010-G08-013
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G08
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G08 candidate; no predecessor or release claimed.
hash_record: ../reviews/full-run-20261010-g08-integrity-receipt.md
---

> **Draft research, not released guidance.** Version 0.1.0; candidate revision `initial-draft-1`. Independent G08 review, gameplay testing and human acceptance have not occurred. Recommendations labeled `hypothesis` are proposed for evaluation, not established effects. All examples labeled *illustrative* are invented and untested. Dates use America/Los_Angeles; the run ID is unchanged.

# Strategy

## Definition and boundaries

**Working usage:** Strategy is a broad, contested family in which choosing and revising commitments among interdependent goals, resources, positions or capabilities is a substantial part of play. The player reasons about an opponent, other participants, a changing system, or some combination, across consequences that extend beyond the current input. This is G08’s analytical definition, not a formal taxonomy or a finding that every marketed strategy game has the same structure. A resource can be an activation opportunity, positional access or information; neither currency nor an economic growth system is mandatory. [C-01]

A label is useful here when it changes the design question. A short encounter can contain strategic commitments; a large map can contain mostly prescribed execution. “Tactics” commonly draws attention to local coordination, but map scale, campaign length and military subject matter do not establish a reliable dividing line by themselves. Keep G07’s separate tactics and tactical-RPG work unresolved until its selected bytes are available. Do not absorb it into this parent entry. [C-01; C-08]

[Real-time strategy](real-time-strategy.md) specializes decisions made while relevant simulation continues. [Turn-based strategy](turn-based-strategy.md) specializes permission, commitment and resolution organized by turns or phases. A real-time battle inside a turn-based campaign requires both analyses, including the cost of transferring plans between layers. The parent file owns the cross-horizon and goal-conflict questions; the child files own their particular timing demands. Single-player, cooperative, competitive, asynchronous, platform and tone remain facets, not replacement genre definitions. [C-01; C-08]

The inspected publisher descriptions provide deliberate range rather than a representative sample: Greater Than Games presents a cooperative defense premise for *Spirit Island*, Free Lives frames *Terra Nil* around ecosystem restoration, and Slitherine presents *Frozen Synapse* through simultaneous tactical commitments. These examples challenge compulsory military conquest, compulsory human opposition and a single time structure; their catalog labels do not settle membership or prove player outcomes. [C-02; sources 008, 009, 013]

## Custom research instructions

For subsequent Strategy work, reconstruct the **decision contract** before collecting a list of familiar genre features: what can be committed, what it prevents, whose actions can intervene, what is knowable at commitment, and which future states matter. Use a rules manual, a dated designer account or a reproducible build to establish each mechanism. Use actual player data only for the outcomes and population that were measured. Do not treat a famous game, a large choice tree or the designer’s preferred style as evidence of depth. [C-01; C-03; C-11]

Sample opposing cases deliberately: abstract positional play without production; a noncombat system with competing goals; cooperative coordination with unequal expertise; competitive adversarial play; a small decision space with consequences; and an expansive system with routine upkeep. Compare committed policies rather than raw counts of clicks or options. A counterexample should challenge a particular causal bridge, not merely look unlike a military RTS. [C-02; C-03]

Record the intended audience and activity separately. A person may seek optimization, rivalry, collective planning, improvisation, discovery or a comprehensible account of consequences. These are **candidate player promises to investigate**, not demonstrated market segments or universal expectations. Ask which commitments they want to own and which routine work they want delegated. Preserve disagreements between players rather than averaging them into a single “strategy audience.” No representative audience study was inspected for this parent classification. [C-04]

Investigate whether a claimed choice is feasible, distinguishable, consequential and actually wanted. Challenge the assumptions that more branches mean more agency, symmetric factions mean fair access, realism improves legibility, longer sessions produce richer commitments, or optimal play is the only legitimate goal. Include localization and access modes when determining what information is available; do not quietly give one route certainty unavailable to another. [C-03; C-06; C-10]

## Player promises and varied audiences

A useful proposed promise is **“my priorities can change what remains possible, and I can understand enough of that relationship to form and revise a plan.”** It does not promise omniscience, equal outcomes or a guaranteed recovery from every error. The promise fails differently when a commitment was misunderstood, when an opponent outmaneuvered an understood plan, and when the interface prevented executing it. Those failures require different responses. [C-03; C-04]

For competitive play, some players may value execution under pressure alongside planning; for cooperative play, the desired contribution may be advising, controlling a distinct role or negotiating a joint objective. For a restorative system, a valued result may be a chosen ecosystem or a stable arrangement, not domination or endless growth. These are conditional use cases supported as possible design premises, not causal evidence about satisfaction. Do not equate lower urgency with lesser strategic value or greater urgency with greater skill. [C-02; C-04; C-08]

## Characteristic loops and structures

This entry separates three analytical horizons without prescribing a mandatory three-layer loop. At the **decision horizon**, a player compares an action or policy with alternatives that it excludes. At the **plan horizon**, prior commitments shape several later opportunities and responses. At the **session or campaign horizon**, persistence may change capabilities, relationships or goals. A compact abstract match can combine all relevant consequences within one session; a game need not add persistent upgrades merely to qualify. [C-01; C-03]

Model the connection explicitly: state and beliefs → chosen commitment → intervening system/participant actions → observed consequence → retained or revised plan. The arrows express an analytical description, not a universal psychological sequence. Beliefs may be incomplete; a good plan can fail because a rival acted differently; an accidental action can produce a favorable outcome. Evaluate the quality of the available decision separately from the eventual result. [C-03; DEP-F02-D]

A **goal conflict** exists only when relevant objectives cannot all be fulfilled under the stated constraints. Calling every resource scarce or every action meaningful supplies no evidence of such conflict. Distinguish a hard feasibility constraint from a soft preference, a shared pool from individual allowances, and present cost from future upkeep. When an economy or map is central, its resource accounting and topology belong to their shared owners; this draft does not replace unavailable F03/W03 bodies with an asserted approved model. [C-03; C-07]

### Practical design choices and alternatives

| Decision | Conditional application | Alternative and failure signal |
|---|---|---|
| Keep multiple commitments in competition | Use when postponing one project creates the intended tradeoff and the relevant costs can be understood. | Independent budgets preserve parallel participation; pooling is inappropriate when one mandatory expense consumes meaningful choice. |
| Reveal consequences or preserve uncertainty | Reveal current permissions and known costs; distinguish forecasts, discovered facts and unknown participant choices. | A deliberately opaque negotiation can retain uncertainty, but it cannot silently rely on a fact one access route never receives. |
| Make a commitment reversible | Permit correction of an unexecuted instruction or allow an explicitly priced change of policy when this matches the intended stakes. | Irreversible scouting knowledge and revealed rival plans cannot be restored merely by refunding resources. |
| Delegate repeated execution | Use when the player chooses a policy and wants repetition to follow it within explicit limits. | Manual handling may be the intended skill or expression; delegation fails when it decides the disputed strategic priority. |
| Extend the planning horizon | Add a future consequence only when it affects a decision players can reasonably revisit or anticipate. | Short, independent scenarios may serve the audience better than a persistent obligation or an unmanageable late-game state. |
| Allow refusal, negotiated completion or noncombat outcomes | Use when those outcomes genuinely satisfy the intended objective and supported constraints. | Method-essential challenges should state their method; do not advertise freedom that the actual resolution rules reject. |

These are original conditional applications of inspected shared distinctions, not a tested ranking of game structures. [C-03; C-05; C-06; C-07]

## Applying shared topics

The [reviewed dependency transfer](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer) records exact selected paths, candidate revisions and byte hashes. The dependencies are not copied into this packet; their IDs are routing identities, not broken local links or claims of release.

| Inspected shared entry | Strategy-specific adaptation |
|---|---|
| Decision design — `GDR-CAND-20261010-F02-TOP-01` | Compare a feasible foregone plan, not merely the immediate price. Separate information about the rules from information the opponent is entitled to conceal. |
| Challenge and difficulty — `GDR-CAND-20261010-F02-TOP-02` | Profile modeling, memory, attention, motor access and social coordination separately; a loss is not diagnostic of poor planning. |
| Quests and objectives — `GDR-CAND-20261010-W02-TOP-02` | Express shared or conflicting outcomes and supported means. Audit survival, economic, positional and negotiated resolution without assuming they are interchangeable. |
| Controls and input; Multimodal communication — `GDR-CAND-20261010-P02-TOP-01` and `...P02-TOP-03` | Preserve the information needed to compare commitments across maps, lists and nonvisual routes. Configuration access and automated decision-making are different interventions. |
| Evaluation and balancing; Ethical and sustainable design — `GDR-CAND-20261010-F07-TOP-01` and `...F07-TOP-02` | Measure reasons, opportunities and burdens alongside outcomes. Include the cost of refusal, interruption, role imbalance and production maintenance. |

`GDR-CAND-20261010-F03-TOP-02` (Economies and resources) and `GDR-CAND-20261010-W03-TOP-02` (Level and spatial design) are known from retrieved **under-review packet text**, not inspected topic bodies. No substantive guidance is transferred from them. Current combat, simulation, multiplayer/session and G07 guidance remains an unresolved dependency; the briefing does not authorize assuming their review status. [C-07]

## Pattern selection and adaptations

[Shared activation budget](../patterns/shared-activation-budget.md), `GDR-CAND-20261010-G08-PAT-01`, is worth considering when allocating activity among actors is itself a desired decision. It changes the feasible allocation set; it does not merely display costs. Avoid it when all actors must carry out compulsory maintenance or when one player could routinely consume every teammate’s opportunity. [C-05]

[Bounded standing orders](../patterns/bounded-standing-orders.md), `GDR-CAND-20261010-G08-PAT-02`, separates choosing a policy from repeatedly issuing its routine commands. Use it only when the scope, stopping conditions and retained player control are legible. It is not a promise of accessibility or a license for an assistant to select goals. [C-05; C-06]

Relevant existing patterns retain their identities: F02 `visible-opportunity-cost-comparison` (`GDR-CAND-20261010-F02-PAT-01`) can explain the actual competing commitments; W02 `multi-route-objective-contract` (`GDR-CAND-20261010-W02-PAT-02`) can make supported outcomes and methods explicit; F07 `triangulated-balance-diagnosis` (`GDR-CAND-20261010-F07-PAT-01`) can structure a future discriminating evaluation. Their benefit claims remain bounded reviewed-candidate claims, not independent G08 evidence. [C-07; C-11]

## Representative cases and negative cases

**Abstract, clocked play.** The inspected 2023 FIDE rules reproduction distinguishes alternating moves from the chessclock. This is a useful counterexample to requiring resource production and to equating a turn structure with unlimited thinking time. The normative scope is over-the-board chess; this is not a recommendation to copy tournament rules into digital strategy. [C-09; source 012]

**Noncombat and cooperative premises.** The creator and publisher descriptions above establish that restoration and cooperative defense are inspectable design premises. They do not show that all players experience those games as calm, that a cooperative group shares authority equitably, or that a restoration theme produces environmental learning. Those benefits remain separate research questions. [C-02; C-04]

**Illustrative worked example — an archipelago supply council.** Three settlements share transport capacity before a storm season. The stated goals are to keep essential deliveries feasible and let players choose which optional community project to advance. Players can inspect known routes and present storage, but a weather forecast is explicitly uncertain. A new depot improves a later route while consuming capacity needed now; repairing an existing crossing preserves access but does not advance the optional project. These relationships, not a combat skin or the map’s size, make the proposed case relevant to Strategy. [C-03; C-05]

First write two feasible plans and identify the commitment that prevents completing both. Then decide whether the intended challenge is forecasting weather, negotiating priorities or scheduling transport. Revealing the exact future storm would remove the first challenge; hiding current route permissions would add a different and potentially unintended one. In a cooperative version, each participant could control a settlement’s preference while jointly approving shared allocations; that allocation of authority is an untested local design option, not inherently fair. [C-03; C-06; C-10]

**Counterexample.** If the scenario has one mandatory transport sequence, always enough capacity, no meaningful intervention and no valued choice of priorities, a long checklist does not become a strategic dilemma merely because it uses a map. Conversely, a small abstract position can contain consequential commitments without any production chain. These logical contrasts challenge the proposed definition and recommendation; they are not observations of a shipped game. [C-01; C-03]

## Accessibility and production implications

Preserve alternatives to map-only reasoning: a structured description of known connections, actor state and legal destinations may offer another route, but its equivalence must be tested for the actual task. A visually marked “best route” can both remain inaccessible and reveal an answer not given elsewhere. Separate access to facts from a recommendation about what to do with them. P01’s reviewed numerical corrections are retained: no CSS-pixel target, text-size example or platform-specific timing value becomes a universal native-game setting here. [C-06; DEP-P01-A]

Localization must preserve distinctions such as available versus reserved, expected versus guaranteed, and current control versus claimed ownership. Text expansion, voice sequencing, number conventions and changed grammatical order can affect how commitments are understood. These are review obligations motivated by the information contract, not measured G08 language effects. Include access to history and current intent after interruption without making session length or retention a proxy for value. [C-06; C-10]

A larger state space increases the **set of cases to reason about**, not necessarily cost by a known numerical factor. Enumerate cancellation, conflicting commitments, changed ownership, save/re-entry and alternate outcomes before promising support. Ethical review should examine what the model rewards, whose needs count as costs, and whether historical or cultural shorthand is mistaken for a neutral simulation. This packet claims neither realism certification nor a conclusion about the politics or intent of a named game. [C-10]

## Research questions and validation

**Proposed, not performed.** For the illustrative council, compare the same underlying scenario with separate allocations and with a shared activation pool. Keep known facts, access routes and objective acceptance rules comparable. Recruit participants spanning relevant strategy familiarity, input/access needs and cooperative experience; do not select only competitive experts and generalize to everyone. Determine sample size and practical decision margins from the specific question and resources, not a genre default. [C-11]

Observe whether players can identify a genuine foregone alternative, whether their declared priority predicts a chosen plan, which actions cannot be executed, and whether unwanted upkeep displaces the intended decision. Ask about burden, perceived control and disagreement separately from success. Confounds include tutoring, arithmetic familiarity, partner dominance and scenario learning. Use unfamiliar **same-rule** cases to examine transfer; change the underlying rule only in a separately reported adaptation/discrimination check. Correctly declining an affordable action may express preference rather than misunderstanding. [C-11; DEP-F01-T; DEP-W02-M]

Reject or narrow the pooled-budget recommendation when participants have no valued allocation choice, repeatedly lose their intended contribution, or gain no meaningful control while burden increases. Reject an access presentation that omits a necessary distinction even when aggregate success rises. These are proposed decision criteria; practical margins must be agreed before a study, and no test has run. [C-05; C-06; C-11]

### Coverage checkpoint

Researched in this bounded draft: operational boundaries; goal and commitment conflicts; temporal distinctions; abstract/noncombat/cooperative countercases; conditional shared-topic application; the two pattern routes; access, ethics and production considerations. Unresolved: representative audience promises, long-horizon multiplayer diplomacy, comparative fairness, real-world cultural interpretation, persistence/re-entry outcomes and the missing economy/spatial/social bodies. The next discriminating question is whether a proposed commitment exposes a valued tradeoff **without replacing access difficulty or routine upkeep with a claim of strategic depth**. All coverage remains open.

## Claim ledger

Local C-identities belong only to this file. Confidence concerns the precisely scoped claim, not the whole genre. A source’s description of a mechanic does not establish its benefit. `DEP` references mean inspected reviewed-candidate passages, not newly inspected underlying studies; see the [dependency receipt](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer).

### C-01

**Claim:** The Strategy label is used here for consequential planning and revision across interdependent commitments, not a checklist of military or economic features.

**Class:** `inference`. **Support and precise locator:** G08 working definition; range contrasts in sources 008 Description, 009 opening/Game Specs, 012 Articles 1/6, 013 product description. **Confidence:** moderate as a useful analytical proposal; not a consensus taxonomy. **Applicability, contrary case and unresolved issue:** Contested boundaries with tactics, puzzle, management and simulation remain open; genre label alone predicts no player outcome.

### C-02

**Claim:** Inspected creator/publisher descriptions supply noncombat restoration, cooperative defense and simultaneous tactical examples.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-008, Description; GDR-SRC-20261010-G08-009, opening/Game Specs; GDR-SRC-20261010-G08-013, product description. **Confidence:** high for the documented premises; narrow documentary observation. **Applicability, contrary case and unresolved issue:** No game was played; selection is purposive and does not establish audience prevalence, enjoyment or causal effectiveness.

### C-03

**Claim:** Strategic opportunity should be analyzed through feasible foregone commitments, known/unknown state and downstream consequences, separately from the eventual outcome.

**Class:** `inference`. **Support and precise locator:** DEP-F02-D: Decision design lines 53–103; DEP-W02-Q: Quests and objectives lines 53–108. **Confidence:** moderate; logical distinctions plus reviewed-candidate methodological support. **Applicability, contrary case and unresolved issue:** The best presentation and desired uncertainty remain local hypotheses. A player may knowingly choose a less instrumentally efficient outcome.

### C-04

**Claim:** Agency, optimization, rivalry, collective planning and restorative stewardship are candidate promises to investigate, not universal audience expectations.

**Class:** `hypothesis`. **Support and precise locator:** G08 audience hypotheses; premises in 008 Description and 013 product description motivate sampling, not benefit claims. **Confidence:** low for audience-wide expectations; no representative audience evidence inspected. **Applicability, contrary case and unresolved issue:** Cooperation can still involve disagreement or pressure, and restorative themes do not prove a calm experience.

### C-05

**Claim:** A shared activity budget or bounded delegation may support intentional prioritization only when it preserves valued choices and avoids compulsory maintenance or domination.

**Class:** `hypothesis`. **Support and precise locator:** G08 PAT-01/PAT-02 causal-link ledgers; DEP-F02-D and DEP-F07-V methodological constraints. **Confidence:** low for comparative benefit; no G08 intervention performed. **Applicability, contrary case and unresolved issue:** Independent allowances, direct control, fewer actors or shorter scenarios can be better alternatives; see G08-CON-01/02.

### C-06

**Claim:** Access to known facts, rule permissions and uncertainty should be preserved across alternative presentations without silently supplying protected answers.

**Class:** `inference`. **Support and precise locator:** DEP-P02-M: Multimodal communication lines 58–108; DEP-P02-C: Controls lines 83–145; DEP-P01-A: lines 89–110 and correction receipt. **Confidence:** moderate for the information distinction; task efficacy untested. **Applicability, contrary case and unresolved issue:** No numeric accessibility default or claim of full equivalence. Changed modality may change experience while preserving facts.

### C-07

**Claim:** Shared topics retain their domain ownership; under-review packet metadata does not supply missing topic guidance.

**Class:** `studio-decision`. **Support and precise locator:** Current G08 dispatch, assigned scopes/dependency receipt; inspected archive selection receipt; F03/W03 retrieved packet text. **Confidence:** high for the user-authorized research boundary, not a scientific claim. **Applicability, contrary case and unresolved issue:** Only research scope is authorized. Latest canonical/pending allocation records remain absent; no implementation decision is approved.

### C-08

**Claim:** Hybrid strategy designs need explicit reconciliation of clocks, commitments and goals rather than a winning parent/subgenre label.

**Class:** `inference`. **Support and precise locator:** Working definition plus 009 opening/Game Specs; compare this packet’s RTS/TBS contracts. **Confidence:** moderate as an analytical separation. **Applicability, contrary case and unresolved issue:** No rule that every hybrid must expose both layers at once, or that adding a strategic map creates strategic agency.

### C-09

**Claim:** The inspected 2023 over-the-board chess rules distinguish alternating moves from clock handling.

**Class:** `formal-standard`. **Support and precise locator:** GDR-SRC-20261010-G08-012, Introduction, Articles 1.2–1.3 and 6.1–6.2.1. **Confidence:** moderate-high for the narrow reproduced wording; original FIDE bytes not obtained. **Applicability, contrary case and unresolved issue:** Historical OTB scope only; no claim about latest tournament requirements or universal digital-game design.

### C-10

**Claim:** Review must cover representation, contribution/exit, localization of uncertainty and maintainability of supported commitment states.

**Class:** `inference`. **Support and precise locator:** DEP-F07-E: Ethical and sustainable design lines 57–77, 92–104; DEP-P02-M; G08 original production/state analysis. **Confidence:** moderate as risk-oriented analysis; effects and costs unmeasured. **Applicability, contrary case and unresolved issue:** No numerical QA multiplier, cultural universality, or inferred intent of a named developer. Cross-cultural and social evaluations remain gaps.

### C-11

**Claim:** Proposed evaluation must distinguish permitted action from preference, same-rule transfer from changed-rule adaptation, and observed behavior from experience.

**Class:** `inference`. **Support and precise locator:** DEP-F01-T: corrected pattern lines 98–116; DEP-W02-M: corrected line 148; DEP-F07-V: evaluation lines 57–98. **Confidence:** high for correctly carrying these distinctions; low for any untested intervention effect. **Applicability, contrary case and unresolved issue:** No participant test, sampling guarantee or independent G08 validation. Practical margins and participant coverage await a separately approved study.

## References

Source IDs are temporary run-scoped identities, reused throughout G08. Access means the named passages were inspected, not that a game was run. Cross-batch URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G08-008

Free Lives. **[Terra Nil press kit](https://freelives.net/terra-nil-press-kit/)**. Free Lives. Publication/update: unknown. Edition/build: Creator press kit describing the game; patch/platform behavior unverified. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Description and game-positioning text on ecosystem restoration and removing built infrastructure. **Type:** Creator-provided design description. **Limits/independence:** A declared design premise, not evidence of relaxation, sustainability learning or audience-wide genre expectations. **Rights:** No press assets redistributed; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-009

Slitherine; developer identified as Mode 7 Games. **[Frozen Synapse](https://www6.slitherine.com/game/frozen-synapse)**. Slitherine. Publication/update: unknown; catalog identifies original release 2011-05-25. Edition/build: Historical PC catalog; installer listing v1.00 is metadata, not an inspected executable. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Opening description; Game Specs: Tactical / Turn-Based WEGO; Info paragraph on plan/test/execute. **Type:** Publisher-provided game description. **Limits/independence:** Documented temporal structure, not proof that tactics always wins, intuitive access, current services or actual play results. **Rights:** Slitherine/Mode 7 rights retained; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-012

FIDE, issuing body; English reproduction hosted by IPCA. **[Laws of Chess 2023](https://ipcachess.org/laws-of-chess-2023/)**. International Physically Disabled Chess Association (IPCA). Publication/update: Effective 2023-01-01; approval displayed as 07/08/2022. Edition/build: 2023 over-the-board Laws; historical edition, not certified latest. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Introduction 0.1; Articles 1.1–1.3, 6.1–6.2.1; Appendix D.1, D.2.1 and D.2.6. **Type:** Normative sport rules reproduced by a FIDE-affiliated association. **Limits/independence:** FIDE handbook/PDF routes failed; wording inspected through IPCA, byte equivalence unverified. Applicability is specified over-the-board chess, not a game-design or digital-accessibility standard. **Rights:** Rights retained; short paraphrase, no full rules reproduced. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-013

Greater Than Games. **[Spirit Island — product page](https://shop.greaterthangames.com/products/spirit-island)**. Greater Than Games. Publication/update: unknown. Edition/build: Publisher product description; tabletop printing not established. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Product description: cooperative defense premise; official rulebook/FAQ links. **Type:** Publisher-provided description and primary-source discovery route. **Limits/independence:** Supports the advertised cooperative premise only. Core rulebook links were exposed but PDF content was not retrieved; no core phase rules inferred from this page. **Rights:** Rights retained; no product assets or rulebook reproduced. Claims using this source are identified in this entry’s ledger.

## Review and history

2026-10-10 — first genre draft in G08, `initial-draft-1`, attempt `G08-authoring-01`. Candidate ID persists through corrections. Predecessor and supersession are null; exact delivered hashes are recorded outside this file to avoid self-reference. No canonical receipt, Library upload or independent G08 approval is claimed.

Evidence and heading coverage remain open. The [review packet](../reviews/full-run-20261010-g08-review-packet.md) records contradictions, missing bodies, complete inventory, proposed index rows and queued child work. Additional research must retain existing identities; child keys require Library Coordination registration before submission. The next decision is independent content review of these conditional recommendations and boundaries, not implementation or release.
