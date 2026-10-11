---
id: GDR-CAND-20261010-G15-PAT-01
kind: pattern
title: Discovery-scoped resource survey
version: 0.1.0
status: draft
run_id: GDR-FULL-20261010
batch_id: G15
id_scope: run-scoped-temporary
candidate_revision: initial-draft-1
attempt_identity: G15-authoring-01
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G15 author draft; no prior G15 candidate bytes identified
  in inspected inputs.
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
evidence_checked_utc: '2026-10-11'
coverage_status: coverage-open
aliases:
- known-resource lookup
- discovery-gated survey
- resource reacquisition aid
tags:
- reacquisition
- knowledge-scope
- resource-state
- optional-information
- discovery
- coverage-open
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-G02-PAT-02
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G15-GEN-01
- GDR-CAND-20261010-G15-GEN-02
source_ids:
- GDR-SRC-20261010-G15-001
- GDR-SRC-20261010-G15-004
- GDR-SRC-20261010-G15-005
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
---

# Discovery-scoped resource survey

> **Untested reusable pattern candidate.** Purpose: support reacquisition of an already meaningful resource without automatically exposing everything the world contains. The documented precedent supports the existence of a mechanism, not its causal benefit. The generalized recipe, worked cases and tests are proposals; no code or player test was executed.

## Purpose and boundary

Use when players repeatedly need a resource they have already encountered or identified, and the suspected barrier is **recovering actionable information**, not producing the resource itself. The intended benefit is to preserve a chosen discovery activity while reducing unwanted repeat-search or memory burden. Both benefit claims remain hypotheses. [C-03, C-04]

This is not a universal compass, an automatic recipe-unlock system, a guarantee of current stock, or a requirement to hide information from players. It is narrower than a general known-space reminder: it specifies the eligibility and disclosure of **query results over changing resource state**. It is also narrower than a complete anti-grind system, because it leaves acquisition, access, conversion and social permission separate. [C-05, C-10]

**Documented precedent.** Grounded's 0.12.0 notes describe a material-analysis and station-coverage-gated survey. The 0.14.0 notes alter the switch location. These are two versions of one production's system, not independent effectiveness evidence. Activated coverage is not the same thing as personally visiting every result coordinate. The stronger policy below is a proposed adaptation, not a claim about that game's exact implementation. [C-01; GDR-SRC-20261010-G15-004, §Resource Survey Stations; GDR-SRC-20261010-G15-005, §World/Resources]

## Context and prerequisites

The team must be able to state the target task, which resource identities and regions may be disclosed, how knowledge is acquired, and whether the query describes current or historical state. A usable information route must exist for the claimed audience; an inaccessible map is not rescued by a correct filter. Decide whether discovery belongs to an individual, a party, a shared world or another explicitly defined unit. [C-02, C-06, C-07]

The resource must actually be available through a supported continuation, or the result must clearly describe why it is not. A valid location can still require an unavailable tool, an unreached station or somebody else's reserved stock. The pattern is not suitable as the only remedy for a production-chain dead end. [C-05]

A production must have enough content/state control to maintain its disclosure promises after depletion, regrowth, moving creatures, changed recipes, setting changes and save migration. These are conceptual prerequisites, not instructions to implement a particular database or engine system. Stop this recipe when that control is unavailable; compare a simpler notebook or creator-authored hint instead. [C-06, C-08]

## Mechanism and evidence by causal link

| Proposed link | Support | Important limit |
|---|---|---|
| A query selects a resource category under eligibility conditions | A versioned official precedent describes this form of lookup. [C-01] | No G15 runtime observation or code inspection; historical documentation only. |
| Applying a declared knowledge/scope policy limits authorized output | Logical consequence of the proposed policy if correctly represented and enforced. [C-02] | No proof that implementation, indirect inference or shared-state leakage is complete. |
| An understandable result supplies a lead for repeated acquisition | Task-analysis inference and inspected cue/known-space guidance. [C-03, C-05, C-07] | Reachability, quantity, freshness and permission can still invalidate the lead. |
| A usable lead reduces unwanted repeated search or memory burden | Hypothesis. [C-03] | People may enjoy searching; a query can itself add menu work or remove choice. |
| Less repeat burden leaves more time/attention for the chosen activity | Hypothesis. [C-03, C-09] | Faster completion is not automatically better agency, wellbeing or engagement. |
| Scoped information preserves valued discovery | Hypothesis. [C-04] | Result density, empty results or known resource locations can still disclose a hidden region, event or creature. |

Confidence is **moderate for the logical distinctions, low for the complete recipe's causal benefit**. No formal standard, verified effect size or universal disclosure threshold supports this pattern.

## Actionable recipe

All steps are proposed. Numerical precision, range, refresh period, number of results and test margins require local justification; none is a prescribed default. [C-02–C-09]

### 1. Identify the repeated decision and the actual barrier

Write an example of the task before adding an interface: “choose which known grove to revisit for a material needed by my selected project.” Determine whether the player instead lacks material identity, access, quantity, conversion capacity, carrying space or permission. Record the desired uncertainty—such as an unseen location or unknown recipe—that should remain unresolved. [C-03, C-05]

**Exit:** when the intended activity is searching for that resource itself, or when the actual blocker is supply or progression, use another intervention or offer this as an explicitly different activity. Do not call it a universal quality-of-life improvement. [C-08]

### 2. Specify the knowledge and disclosure policy

Define how an identity becomes eligible: seeing a specimen, analyzing it, receiving a consensual shared discovery, or another locally chosen event. Separately define allowed geographic scope: visited space, activated coverage, a public region or a chosen broader disclosure mode. Then define whether a known identity may reveal an unknown location. These choices must not be hidden in the word “discovered.” [C-02, C-04, C-06]

A **proposed conceptual eligibility relation** is: the viewer is authorized to know the resource identity, the result lies in the declared query scope, and the result representation is permitted at its chosen precision. This is a reasoning model, not executed code or a formal guarantee. An anonymous density map or a count can disclose information even without a resource name. Audit those outputs too. [C-02, C-04]

**Exit:** when the policy cannot distinguish legitimate assistance from a protected revelation, narrow the scope, choose a deliberate spoiler mode with clear consent, or do not use the pattern. Essential access information is not optional merely because it would require a different sensory representation. [C-04, C-07, C-08]

### 3. Separate remembered observation from current state

Choose whether the result means “observed here,” “currently detected within supported coverage,” “may occur in this habitat,” or another explicit relation. Define expiration, movement, depletion and renewal. Distinguish an empty result caused by absence from a query that cannot answer because the identity or region is ineligible. Avoid wording that falsely promises a known area is exhausted or safe. [C-05, C-06]

If accurate live information cannot be maintained, use a truthful historical observation rather than a stale claim of certainty. More frequent updates may cost production effort or reveal moving hazards; they are not automatically better. [C-06, C-08]

### 4. Offer the minimum useful result through usable routes

Compare a remembered note, habitat description, region list, rough area, precise waypoint or player-authored marker. Match detail to the decision and the declared disclosure policy. An alternate representation should preserve identity, location reference, uncertainty and relevant timing—not invent an unseen cause or omit a needed direction. Do not force every modality at once. [C-03, C-07]

Make the query discoverable and optional when it is an optional aid. Support revisiting or dismissing results without losing an unfinished project. Keep resource names and result-state wording coherent across localization and narration. Exact visual or motor targets require separate scoped guidance, not numbers invented here. [C-06, C-07]

### 5. Check the lead against the acquisition chain

For each representative result, ask whether a route exists, whether a required tool/station is available, whether the material can be harvested under the supported settings, and whether the result is public or reserved. Avoid implying “you can obtain this now” when only “a known occurrence is reported here” is justified. [C-05]

A project may deliberately leave these conditions for the player to reason about. The interface then needs truthful uncertainty rather than an automatic solution. A query that silently solves the entire chain can remove the planning activity the pattern was intended to support. [C-04, C-05, C-08]

### 6. Review shared knowledge and state transitions

Inspect individual versus shared discoveries, newly joining players, host changes, revoked permissions, moved resources, concurrent collection, mode changes and old saves. Decide whether shared discovery is opt-in, common knowledge or private. An absent player should not be assumed to have consented to every reveal because another player activated a scanner. [C-06]

These policies can differ by game and mode. A shared public-world economy may intentionally expose common resources; a mystery expedition may protect individual knowledge. The recipe does not prescribe one default. If a policy cannot be supported consistently, limit the feature's scope rather than claiming seamless equivalence. [C-06, C-08]

### 7. Compare, then keep, narrow or remove

After separate test authorization, compare the smallest viable survey against a notebook/habitat hint and the intended unaided activity. Preserve resource availability, travel and threat demands as far as the question permits. Ask what players learned, which choices remained meaningful, whether they wanted the aid and what it revealed—not only how fast they gathered. [C-03, C-04, C-09]

**Exit:** reject or narrow the recipe when it leaks protected facts, gives misleading state, does not reduce the diagnosed burden, removes desired exploration, fails a claimed access route or imposes maintenance cost disproportionate to its demonstrated benefit. An unchanged activity remains a valid outcome. [C-08]

## Adjustable variables

| Variable | What the team must decide | Failure to watch for |
|---|---|---|
| Knowledge owner | Individual, party, world, or explicit sharing policy | A teammate's progression silently reveals a personal discovery |
| Eligibility event | Seen, sampled, analyzed, purchased information, or other declared event | Merely mentioning an unknown ingredient enables locating it |
| Geographic scope | Personally known area, activated coverage, public region, or disclosed alternate mode | “Known” is interpreted differently by author and player |
| Result precision | Habitat, region, approximate location, exact marker | Fine detail solves an intended search or reveals nearby protected content |
| Freshness | Historical, live, confidence-qualified, or manually refreshed | Empty/depleted or moved nodes presented as current certainty |
| Acquisition qualifiers | Which requirements or uncertainty are shown | A true location is interpreted as immediate, permitted availability |
| Representation | Text/list/map/narration/other usable options | Required fact disappears or changes certainty across modalities |
| Optionality | Player selection, scope preferences and dismissal | Aid becomes compulsory optimization or unwanted revelation |

## Worked examples

### Illustrative example: coastal fiber reacquisition

**Invented example, not Grounded behavior or a test result.** A player has identified ordinary fiber and recorded two coastal beds. A third cave contains an unknown material. A survey station covers both the coast and cave entrance, but the chosen policy permits only identified materials in personally visited areas. Activating the station therefore does not authorize every location in its coverage. This is deliberately narrower than coverage alone. [C-02, C-04, C-09]

The player queries ordinary fiber for a selected filter project. The result list gives the two recorded coastal areas, distinguishes a current observation from yesterday's note, and lets the player mark one. It does not display the unknown cave material's name, count or silhouette. If a bed has been collected since the last observation, the result remains historical until refreshed, not “guaranteed available.” The design must decide whether revealing ordinary fiber in a newly detected but unvisited cave would disclose too much; that is a policy decision, not a technical inevitability. [C-02, C-04, C-06, C-09]

The player can still choose between a longer safe route and a shorter hazardous one. A motor-access representation changes how the result is selected, not which hidden locations are authorized. A later shared-world case tests whether another player's discovery updates everyone's list and whether that transition was understood. These are proposed checks, not passed tests. [C-05–C-07, C-09]

### Illustrative reusable adaptation outside survival crafting

An investigation game could let a player recall **previously catalogued public records** by authorized district without exposing undiscovered suspects. Historical versus current availability still matters, and a known record's location might disclose an intended connection. Use this pattern only if reacquisition is the target; if assembling the connection is the mystery itself, a notebook may be the better alternative. No specific detective game is asserted to use this adaptation. [C-04, C-08–C-10]

## Alternatives, tradeoffs and counterexamples

A **player notebook** has lower live-state maintenance and preserves personal annotation, but may leave an unwanted recall burden. **Habitat hints** preserve approximate search while reducing scope, but can be too vague for the intended user. **More abundant supply** changes acquisition rather than knowledge and may remove scarcity. **Project purchase/automation** changes the underlying activity rather than merely supporting reacquisition. **No aid** can be coherent when searching is the valued activity and its information is usable. These are comparisons to evaluate, not ranked universal solutions. [C-03–C-08]

A competitive shared-world game can make revealing a resource location also reveal another player's position or plan. A known specimen can occur beside an unknown landmark, making a “known resource only” filter insufficient. A depleted finite world can produce accurate but useless results. A geological exploration game can lose its main decision if an authorized survey immediately identifies every profitable deposit. These are logical/synthetic counterexamples, not observed defects in the named precedent. [C-04–C-06, C-08]

**Do not use** as a patch for an impossible production chain, as a compulsory substitute for usable environmental clues, as a promise of exact stock when stale data is all that exists, or as a reason to collect private player information. No telemetry is required by the conceptual pattern. [C-05–C-08]

## Proposed playtests and rejection criteria

**NOT PERFORMED.** No sample, effect size or pass threshold is claimed. Define participant characteristics, consent, stoppage, analysis and locally meaningful decision margins before running a study. Include first-time and returning players, differing spatial/recipe knowledge, relevant access users and groups with differing discovery preferences. [C-09]

| Test | Method and controls | Measures / result that would change the recommendation |
|---|---|---|
| T-P-1: reacquisition without automatic revelation | Compare notebook, optional scoped query and an explicitly broader query after matched initial discovery. Keep resource amount and travel comparable; account for order and memory. | Record time components, chosen routes, unwanted revelations and desired discovery. Narrow/reject if only the broad reveal helps, the scoped aid adds burden, or players lose the activity they selected. |
| T-P-2: stale and negative results | Present matched live, historical, depleted and out-of-scope cases using the declared wording and access routes. Ask for predictions before revealing actual state. | Check whether users distinguish “not found,” “not eligible” and “not current.” Reject a representation that systematically communicates stronger certainty than the policy supplies. |
| T-P-3: shared knowledge and changed rules | Simulate or later prototype a teammate's discovery, host change and save-version change without live account operations here. | Ask who can now know what and why. Reject or redesign sharing when it produces unwanted disclosure, contradictory lists or an unsupported progression state. |

A successful local usability test would still not prove genre-wide benefit, long-term satisfaction or reliability across every game state. Static artifact checking below is not one of these player tests.

## Claim ledger

| Claim | Precise claim / proposal | Class | Support and precise locator | Confidence and limit |
|---|---|---|---|---|
| C-01 | Grounded provides a documented analysis-and-coverage-gated resource survey precedent. | observed-example | GDR-SRC-20261010-G15-004, Resource Survey Stations; GDR-SRC-20261010-G15-005, World/Resources update. | High for two historical documents of one system; not independent replication. |
| C-02 | A correctly specified filter can limit what a lookup is allowed to disclose. | inference | C-01; explicit proposed eligibility relation in this recipe. | Moderate logical confidence; code correctness and side-channel completeness not tested. |
| C-03 | A discoverable optional lookup may reduce repeated memory/search burden. | hypothesis | C-01; reviewed F02 information distinction and P02 cue recipe. | Low: no comparative player-effect evidence inspected. |
| C-04 | Retaining unknown identities/regions while choosing granularity may preserve valued discovery. | hypothesis | C-02/C-03; synthetic disclosure examples. | Low: players may infer hidden content from allowed results; scope must be tested. |
| C-05 | Lookup does not itself solve physical reachability, resource exhaustion, conversion bottlenecks or social ownership. | inference | GDR-SRC-20261010-G15-001, acquisition/conversion distinction; GDR-SRC-20261010-G15-005, changing resource availability; reviewed G02 state/knowledge distinction. | Moderate structural rationale; implementation still unverified. |
| C-06 | Signal freshness, negative-result meaning and individual/team knowledge policies explicitly. | hypothesis | C-02/C-05; reviewed P02 facts/uncertainty; hypothetical multiplayer/world-state cases. | Low effect confidence; no proven default policy. |
| C-07 | Use player-selectable result representations that preserve authorized facts without forcing every modality. | inference | Reviewed P01 access and P02 cue alternatives; recipe applicability. | Moderate rationale; alternatives require direct user evaluation. |
| C-08 | Reject or narrow the pattern when it removes the intended search activity, leaks protected facts or costs more to maintain than a simpler reminder. | hypothesis | C-03–C-07; counterexamples and proposed tests. | Low benefit confidence; exit criteria are proposed local choices, not universal thresholds. |
| C-09 | The worked examples and evaluation plan are illustrative and unperformed, with no claimed engine correctness or player benefit. | hypothesis | Synthetic examples and proposed T-P-1/T-P-2/T-P-3 below. | Low causal confidence; no participants, prototype or runtime test. |
| C-10 | This proposed pattern is narrower than known-space recovery, generic recipe lookup or automatic unknown-resource revelation. | inference | Reviewed G02/P02 scopes; C-01–C-08. | Moderate scope distinction; cross-library duplication and ownership review remain pending. |


## References

### GDR-SRC-20261010-G15-001

**Mojang Studios staff.** [How to craft](https://www.minecraft.net/en-us/article/how-craft). Minecraft / Mojang Studios. **Publication/update:** 2023-06-05. **Edition/build:** Web guide; game build unspecified.

**Access:** `relevant-excerpt`; 2026-10-10 America/Los_Angeles / 2026-10-11 UTC. **Type:** Primary official instructional artifact. **Inspected locator:** Starting to Craft; Crafting Recipes; Crafting Supplies; Crafting in Minecraft (retrieved text lines 513–571). **Claim uses (G15-scoped):** GEN-01:C-01,C-02,C-06; PAT-01:C-05. **Limits:** Guide is introductory, not an exhaustive recipe specification. No Java/Bedrock build was run; avoid converting simplified wording into universal crafting rules. **Independence:** Same organization as source 002; not independent effect evidence. **Rights:** Copyright retained by the source owner; only brief attributed paraphrases and bibliographic links are distributed. No screenshots, game assets or full text copied.

### GDR-SRC-20261010-G15-004

**Obsidian Entertainment.** [The Time Has Come to go Into the Wood](https://www.obsidian.net/news/grounded/the-time-has-come-to-go-into-the-wood). Obsidian official Grounded news. **Publication/update:** 2022-02-01. **Edition/build:** Grounded update 0.12.0.

**Access:** `relevant-excerpt`; 2026-10-10 America/Los_Angeles / 2026-10-11 UTC. **Type:** Primary release notes / creator description. **Inspected locator:** Resource Survey Stations (retrieved lines 119–126); Custom Game Options (127–144). **Claim uses (G15-scoped):** GEN-01:C-03,C-09; PAT-01:C-01 (later links are hypotheses, not source findings). **Limits:** No game was run. Described survey coverage is activated-station coverage, not proof that each marked position was personally visited. It does not establish reduced grind, spoiler avoidance or accessibility. **Independence:** Same document initially failed on grounded.obsidian.net; successful official-domain route retains this one identity. Same production as source 005. **Rights:** Copyright retained by the source owner; only brief attributed paraphrases and bibliographic links are distributed. No screenshots, game assets or full text copied.

### GDR-SRC-20261010-G15-005

**Obsidian Entertainment.** [Grounded Heads into the Home Stretch](https://grounded.obsidian.net/news/grounded/grounded-heads-into-the-home-stretch). Grounded official news. **Publication/update:** 2022-08-25. **Edition/build:** Grounded update 0.14.0, Game Preview.

**Access:** `relevant-excerpt`; 2026-10-10 America/Los_Angeles / 2026-10-11 UTC. **Type:** Primary release notes / creator description. **Inspected locator:** Shared Worlds (retrieved lines 71–81); Armor and Weapon Upgrade Changes (118–142); World/Resources (230–232). **Claim uses (G15-scoped):** GEN-01:C-03,C-04,C-05,C-10; PAT-01:C-01,C-05. **Limits:** Historical beta notes, including save-loss warning; no current service guarantee. One active host is distinct from an always-running server. Rad Nugget exception is retained when discussing finite-to-craftable resources. **Independence:** Same production as source 004; later revision changes survey-switch placement. Not independent corroboration of player benefit. **Rights:** Copyright retained by the source owner; only brief attributed paraphrases and bibliographic links are distributed. No screenshots, game assets or full text copied.


## Related entries, ownership and review history

Applied in [Survival crafting](../genres/survival-crafting.md), `GDR-CAND-20261010-G15-GEN-01`. Conditional hybrid relevance only in [Soulslike](../genres/soulslike.md), `GDR-CAND-20261010-G15-GEN-02`.

Inspected complementary drafts: `GDR-CAND-20261010-F02-TOP-01` for legitimate information, `GDR-CAND-20261010-P01-TOP-03` for access, `GDR-CAND-20261010-P02-PAT-02` for cue meaning, and `GDR-CAND-20261010-G02-PAT-02` for separate reachability and actionable knowledge. Exact receipts are in [the review packet](../reviews/full-run-20261010-g15-review-packet.md#reviewed-dependency-receipt). No dependency source identity is repurposed as a G15 source.

**Ownership proposal, not allocation:** Foundations and Systems for resource/state semantics; Worlds and Characters for permitted geographic discovery; Presentation and Interaction for queries and alternative representations. BH-GDR-Genres authors this temporary candidate. Library Coordination must check duplication and decide its eventual home before any permanent ID or release. In particular, compare with the existing known-space recovery and cue patterns rather than assuming novelty. [C-10]

Initial draft `0.1.0`, revision `initial-draft-1`, predecessor null. Contradictions: `G15-CON-01`, `G15-CON-06`, `G15-CON-07`. Exact hash is recorded outside this file. Author self-review is not independent review; all approval fields remain null. Gate C is pending, overall Gate D is not passed, and Gate E/release is blocked.

**Next decision:** independently judge whether a dynamic resource-query policy warrants a separate pattern or should become a narrower adaptation of an existing entry, then review the strongest counterexample: correctly scoped information can still remove valued discovery.
