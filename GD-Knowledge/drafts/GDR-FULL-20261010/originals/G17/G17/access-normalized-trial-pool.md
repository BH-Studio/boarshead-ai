---
id: GDR-CAND-20261010-G17-PAT-01
kind: pattern
title: Access-normalized trial pool
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
- temporary functional-content trial
- collection-independent experiment
- loaned trial pool
tags:
- functional-access
- experimentation
- ownership-boundary
- configuration
- hypothesis
related_topics:
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G17-GEN-01
- GDR-CAND-20261010-G17-GEN-02
source_ids:
- GDR-SRC-20261010-G17-002
- GDR-SRC-20261010-G17-003
- GDR-SRC-20261010-G17-006
reviewed_dependency_ids:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-F07-PAT-02
reviewer: null
approved_by: null
approved_date: null
---

# Access-normalized trial pool

**Draft pattern candidate, not a validated treatment.** Version 0.1.0; temporary identity `GDR-CAND-20261010-G17-PAT-01`. The proposed benefit is that a bounded trial can make an otherwise unavailable configuration testable. Better decisions, learning, satisfaction, fairness and retention do **not** follow automatically. Shared-pattern ownership and deduplication await Library Coordination.

## Purpose

Help a player or researcher explore a configuration when functional content access is the suspected obstruction. Within a declared trial context, provide the same authorized functional pool to the relevant participants without changing their underlying ownership. This separates a question about **what a configuration can do** from a question about **what a particular account has acquired**. It does not normalize skill, preferences, randomness, device access, matchmaking or every production constraint. [C-01, C-03]

The pattern can be considered for cards, characters, equipment or other configurable functional content. Its inspected production witnesses are card-game documents; use in other systems is an explicit transfer hypothesis. This is not a generic recommendation to make all content free or to replace a game’s progression economy. [C-01, C-07]

## Context and prerequisites

Use only when a specific wanted experiment is blocked by access and the trial can be separated intelligibly from ordinary play. The designer needs an identified rules/content snapshot, a finite eligible pool, clear entitlement duration, a way to distinguish borrowed from owned content, appropriate opponents/tasks, and an exit without a forced purchase. Required access accommodations should be retained; they are not experimental variables to remove. [C-03, C-04, C-08]

Define the **unit being normalized**. Equal access to item names is insufficient when usable copy counts, upgrades, variants, required companions, or prerequisite modules differ. Conversely, granting more copies than the trial rules allow changes the question. “All access” must mean all of the declared pool, not an unbounded promise about the entire product. [C-03]

Do not start this pattern merely because a collection is small. A player who wants one supplied configuration, a progression-constrained challenge, or a fresh in-run acquisition experience may have a different problem. Diagnose the wanted action first. [C-01, C-07]

## Mechanism and evidence

Arena describes temporary access to eligible cards without a collection grant. The historical Hearthstone Core announcement separately illustrates how access and underlying ownership can differ. These documents establish examples of the distinction, not controlled effects of this pattern. [C-02; GDR-SRC-20261010-G17-002; GDR-SRC-20261010-G17-006]

| Proposed causal link | What is supported | What remains uncertain |
|---|---|---|
| Define a common functional pool → remove within-trial ownership differences for that pool | Conditional reasoning: if authorized counts/versions actually match, those access differences are absent by construction [C-03] | Undetected upgrade, prerequisite, device or interface differences can break the condition. |
| Remove that obstruction → make certain configurations feasible | Follows only for configurations blocked by the normalized access dimension [C-03] | Feasibility does not show that a player can find, understand or wants the configuration. |
| Make configurations feasible → enable useful exploration | Official examples and publisher acknowledgement of brewer constraints motivate the question [C-02, C-05] | Useful exploration is a hypothesis requiring observation, not proof supplied by feature existence. |
| Exploration → better informed later choice | Proposed benefit [C-06] | Overload, unrepresentative opponents and confusing loan expiry may produce worse decisions. |
| Better informed choice → improved wellbeing, retention or spending outcomes | No established link in this batch | Do not claim it; no purchases or longitudinal evaluation occurred. |

The 2022 Arena economy account acknowledges that an iteration-focused structure can hinder frequent experimentation. This is a practitioner rationale for investigating the obstruction, not evidence that a universal normalized mode is the best remedy. [C-05; GDR-SRC-20261010-G17-003]

## Recipe

1. **Name the blocked decision.** Record the intended configuration/task, the access missing, and why observing ordinary play cannot answer the question. If comprehension rather than access is the issue, prefer a supplied configuration or explanation and stop this recipe. [C-01, C-07]
2. **Fix the trial snapshot.** Identify rules, content revisions, legal combinations, usable counts, prerequisites, opponent/task conditions and whether run-level acquisition remains intact. Do not mix two versions of the same item under one normalized label. [C-03, C-04]
3. **Choose the smallest adequate pool.** Include the functional alternatives needed for the decision, not every available asset by default. Define whether normalization applies to one participant’s sandbox or all participants in a comparison. A trial is not a balanced competitive event merely because its pool is shared. [C-03, C-07]
4. **Declare the boundary before use.** Explain where the access works, when it ends, what remains owned, what can be saved as a plan and what will not transfer. Keep the ordinary collection visually and semantically distinct. Do not imply that trial success grants the tested content. [C-02, C-04]
5. **Provide an accessible entry and exit.** Offer relevant filtering and coherent supplied examples without requiring the player to copy them. Let the player stop, inspect original ownership or return to ordinary play without purchasing. An optional acquisition proposal is a separate decision, never an automatic completion step. [C-04, C-08]
6. **Observe the intended experiment.** Ask whether the desired configuration became feasible, what the player thinks is owned, and whether the trial answered their question. Separate rule understanding from preferences; do not count departure or refusal as a failure to learn. [C-06, C-09; DEP-F01-PAT]
7. **Handle expiry without erasing intent.** A saved trial configuration can remain a clearly marked plan with its missing requirements shown. Restore the authorized ordinary access state, not an invented entitlement. Stop rather than silently convert a trial into a transaction or remove genuinely owned content. [C-04, C-08]
8. **Keep, narrow or remove the mode.** Retain it only if it serves the chosen question at acceptable local cost. Prefer supplied configurations, selective loans or an ordinary sandbox when a normalized pool adds no necessary information. Evidence of misunderstanding or pressure reopens the design even if usage rises. [C-06, C-07, C-09]

### Adjustable variables and exit conditions

| Variable | Selection question | Exit or revision signal |
|---|---|---|
| Pool breadth | Which alternatives are needed to answer the actual question? | The wanted experiment is still blocked, or irrelevant options dominate effort. |
| Functional equivalence | Are versions, counts and required dependencies genuinely comparable? | Hidden entitlement differences make the comparison invalid. |
| Duration and availability | Can the player complete the wanted activity without coercive urgency? | Expiry is misunderstood or access conditions prevent the task. No universal timer is specified. |
| Opponent/task match | Does this trial represent the intended decision context? | An unrepresentative task makes the conclusion inapplicable to ordinary play. |
| Save/exit semantics | What persists as ownership, configuration, history or nothing? | The player reasonably expects a grant that the trial will not provide. |
| Support | What helps a player inspect options without choosing for them? | Correct actions merely copy prompts or access supports have been removed. |

## Worked examples

### Illustrative card-configuration trial

**Invented example; not a shipped feature or performed study.** A player wants to test whether a defensive configuration can recover from a particular pressure sequence. The ordinary account lacks part of the intended configuration. The trial supplies the selected event’s functional pool at its allowed copy counts, while leaving the account collection unchanged. A supplied configuration is available for a player who does not want to construct one. [C-03, C-06]

The entry screen identifies the trial rules and states that its borrowed items are usable here only. A configuration saved during the trial is labeled as a plan, with borrowed requirements distinguishable from owned ones. The exit offers ordinary play, revisiting the plan or stopping; none performs an acquisition. The observer asks the player to explain both the tested interaction and what access will remain afterward. A successful interaction with an incorrect ownership belief is not a successful trial outcome. [C-04, C-08, C-09]

An ordinary-access comparison preserves the original constraint. A supplied-configuration comparison removes construction effort as well as access burden. These conditions cannot be pooled as though they isolated the same mechanism. If the player can already answer the question with a supplied configuration, the full normalized pool may be unnecessary. [C-06, C-07]

### Illustrative transfer outside cards

A loadout-based game could authorize a specified set of equipment in a training scenario without permanently unlocking it. The same recipe would distinguish authorized counts/upgrades and expiry. That is **an untested transfer proposal**. It should be rejected where equipment discovery or earning the loadout is precisely the intended activity, or where training behavior does not represent the actual task. [C-07]

## Alternatives, tradeoffs and failure cases

A **supplied configuration** requires less search but cannot test free construction. **Selective loans** preserve more collection constraints but can bias the alternatives. A **fixed functional pool for the entire game** removes the trial/ownership transition but changes the progression promise. **Ordinary collection-constrained practice** best represents that constraint but cannot reveal the performance of unavailable options. These are different decisions, not a hierarchy of fairness. [C-01, C-07]

Watch for an entitlement mismatch, inaccessible filters, missing companion content, novice overload, misleading matchmaking, false grant expectations, timer pressure, auto-spend behavior, or a population split that makes opponents unrepresentative. Increasing participation does not by itself distinguish genuine value from reward-seeking or uncertainty about expiry. Correct the contract or remove the mode rather than claiming that users should have read it more carefully. [C-04, C-06, C-08, C-09]

## Counterexamples and do-not-use conditions

Do not use this pattern to infer ordinary-match balance from a different accessible pool, to conceal an eventual purchase requirement, to offer assets without appropriate authorization, or to claim equal ability from equal inventory. Do not pregrant run-level acquisitions when their discovery is the intended game. An expert collector can legitimately prefer restricted experimentation, and a novice can legitimately prefer one coherent starter configuration. Those preferences falsify a universal prescription, not necessarily the bounded technique. [C-01, C-07, C-08]

## Proposed playtest — not performed

**Question:** does normalizing the selected access dimension let relevant players answer a previously blocked configuration question without confusing ownership or creating unacceptable burden? Compare ordinary access, supplied configurations and the proposed normalized pool under a declared content/rule snapshot. Use matched tasks; counterbalance order when carryover permits. Learning in one condition can contaminate another, so do not describe repeated exposure as independent participants. [C-09]

Include different collection histories, construction experience, intended play goals and relevant access configurations. Preserve accommodations. Observe feasibility, useful experiments attempted, rule explanation, ownership/expiry understanding, effort, perceived pressure and reasons for preferring or declining each option. Do not substitute spending intent or session length for decision quality. No actual transaction is part of the proposed study. [C-06, C-08, C-09]

**Falsifiers:** the configuration remains functionally unavailable; participants systematically misidentify what they retain; normalized access supplies no needed information beyond a simpler condition; or the mode introduces a knowledge, access or pressure problem that defeats its declared purpose. Define acceptable local burden and uncertainty before collection. No numerical pass rate, participant count or efficacy estimate is claimed. [C-09]

## Claim ledger

| Claim | Class | Evidence / locator | Confidence and boundary |
|---|---|---|---|
| C-01: Separate trial access from ownership to investigate a specified obstruction, not universal fairness | inference | G17-002 All-Access; G17-006 ownership FAQ; explicit purpose | Moderate, narrow design rationale; not a policy every game should adopt. |
| C-02: Official examples distinguish usable temporary/curated content from underlying ownership | observed-example | G17-002 All-Access Events; G17-006 historical Core/FAQ | High for documents; no current-client reproduction or outcome validation. |
| C-03: Equal authorized functional counts/versions remove that specific access difference by construction | inference | Explicit pool/entitlement model; G17-002 mechanism | High conditional reasoning; other inequalities remain. |
| C-04: A declared scope/expiry/save contract is needed to evaluate the proposed trial honestly | inference | C-01–C-03; DEP-P01-INFO; DEP-F07-EXIT | Moderate; readable disclosure alone does not prove comprehension. |
| C-05: Iteration-focused acquisition can conflict with frequent experimentation in the publisher’s account | practitioner-heuristic | G17-003, Economy 101 brewer paragraph | Moderate firsthand account, not population or effect evidence. |
| C-06: Feasible exploration may inform a later choice | hypothesis | C-03/C-05 bridge; proposed comparison | Low benefit confidence; no tests, no retention/spending conclusion. |
| C-07: Broader pools and transfers outside cards can be unnecessary or alter the intended challenge | inference | Mechanism limits; explicit counterexamples | Moderate logical applicability limit; population response unknown. |
| C-08: Evaluate access, refusal and pressure rather than treating disclosure/usage as sufficient | inference | DEP-P01-ACCESS; DEP-F07-ETHICS; DEP-F07-EXIT | Moderate as conditional review criteria, not approved policy or legal advice. |
| C-09: Proposed comparisons could falsify the pattern’s benefit | hypothesis | Playtest section; DEP-F07-EVAL; DEP-F01-PAT | Low until performed; no outcome or power claim. |

`G17-002`, `G17-003` and `G17-006` are short locator forms of the full source IDs below. Local issue **G17-ISSUE-02** preserves access-versus-experience disagreement in the review packet.

## Related entries and history

Related genre applications: [Collectible card game](../genres/collectible-card-game.md), `GDR-CAND-20261010-G17-GEN-01`, and [Board-game adaptation](../genres/board-game-adaptation.md), `GDR-CAND-20261010-G17-GEN-02`. Broad economy/progression ownership is proposed for **BH-GDR-Foundations-and-Systems**; no ownership transfer or permanent ID allocation occurred.

First captured candidate revision: `initial-capture-1`; predecessor/supersession null. Author self-review challenged the normalization-to-better-decisions link and added the supplied-configuration countercase. Independent review and participant validation remain pending. The [review packet](../reviews/full-run-20261010-g17-review-packet.md) records hashes, overlapping-concept checks and the two-pattern cap.

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

### DEP-F07-EVAL
**GDR-CAND-20261010-F07-TOP-01 — Evaluation and balancing**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/evaluation-and-balancing.md`; relevant locator: Decision and mechanisms; causal interpretation; balancing scope.
**Transferred scope:** Ownership and exposure can confound usage; aggregate match outcomes do not establish balance. **Byte identity:** 43,446 bytes; SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-F07-ETHICS
**GDR-CAND-20261010-F07-TOP-02 — Ethical and sustainable design**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/ethical-and-sustainable-design.md`; relevant locator: Agency, incentives and full cost; refusal/re-entry discussion.
**Transferred scope:** Disclosure is not proof of freedom from pressure; include time and exit costs. **Byte identity:** 49,049 bytes; SHA-256 `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-F07-EXIT
**GDR-CAND-20261010-F07-PAT-02 — Legible commitment and safe exit**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/legible-commitment-and-safe-exit.md`; relevant locator: Mechanism; context and recipe.
**Transferred scope:** Broad commitment/exit guidance; preserve consequences for other participants rather than promising consequence-free reversibility. **Byte identity:** 22,899 bytes; SHA-256 `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

## References

Access checked **2026-10-10, America/Los_Angeles** (retrieval session continued on 2026-10-11 UTC). Exact client builds are unknown unless a cited release note names one; release-note inspection is not client observation. `GDR-SRC-20261010-G17-*` are temporary source identities. Cross-batch URL/DOI/edition deduplication is pending Library Coordination. Lineage-only mentions of other batch source IDs resolve in the [review packet source ledger](../reviews/full-run-20261010-g17-review-packet.md#references); they are not additional supporting sources for this artifact.

### GDR-SRC-20261010-G17-002
**Wizards of the Coast. MTG Arena Formats.** Wizards of the Coast; publication/update: 2019-10-19 displayed; subsequent revision date unknown. [Source](https://magic.wizards.com/en/news/mtg-arena/mtg-arena-formats).
- **Edition/build; locator:** Mutable HTML; Arena build unknown. Banned and Suspended Cards; MTG Arena Formats and Events; All-Access Events.
- **Access/type/provenance:** `relevant-excerpt`; Official feature/format documentation. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Used only for distinctions and documented temporary access. Its mixed-age format roster is not treated as a verified current schedule or complete current legality list. Same publisher family as G17-001 and G17-003–005; All-Access is one documentation witness, not an efficacy experiment.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01–C-03.

### GDR-SRC-20261010-G17-003
**Wizards of the Coast. On the MTG Arena Economy in 2022.** Wizards of the Coast; publication/update: 2022-03-18 displayed; URL includes 2022-03-17. [Source](https://magic.wizards.com/en/news/mtg-arena/mtg-arena-economy-2022-03-17).
- **Edition/build; locator:** Historical 2022 economic rationale; client build unknown. MTG Arena Economy 101: overarching goals; paragraphs on deck iteration and deck brewers.
- **Access/type/provenance:** `relevant-excerpt`; Firsthand publisher rationale / practitioner account. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Intent and acknowledged tradeoffs, not independently measured wellbeing, access, affordability, or retention. No linked video was inspected; no price is transferred as current. Same publisher as G17-001,002,004,005. Publisher statements about its own audience are not independent population evidence.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-05; rationale for C-06 only.

### GDR-SRC-20261010-G17-006
**Blizzard Entertainment. Introducing the Core Set and Classic Format.** Blizzard Entertainment; publication/update: 2021-02-09; later corrections displayed without a separate revision date. [Source](https://hearthstone.blizzard.com/en-us/news/23620129/introducing-the-core-set-and-classic-format).
- **Edition/build; locator:** Historical 2021 announcement, not current Hearthstone behavior. Introducing the Core Set; FAQ: cost; existing class levels; original-set ownership and yearly replacement.
- **Access/type/provenance:** `relevant-excerpt`; Official historical feature announcement. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Used for a historical access model and its ownership boundary; no current set size, unlock threshold, balance result, or client behavior is asserted. Independent production organization from Wizards; still publisher-authored intent/feature reporting rather than independent player evidence.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-02 historical boundary.
