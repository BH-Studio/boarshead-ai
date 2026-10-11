---
id: GDR-CAND-20261010-G17-PAT-02
kind: pattern
title: Information-bounded undo
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
- disclosure-bounded recovery
- knowledge-aware undo
- commitment-bounded takeback
tags:
- recovery
- hidden-information
- commitment
- shared-state
- hypothesis
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G17-GEN-02
- GDR-CAND-20261010-G17-GEN-01
source_ids:
- GDR-SRC-20261010-G17-010
- GDR-SRC-20261010-G17-011
- GDR-SRC-20261010-G17-013
reviewed_dependency_ids:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-P02-PAT-02
reviewer: null
approved_by: null
approved_date: null
---

# Information-bounded undo

**Draft pattern candidate, not a verified recovery system.** Version 0.1.0; temporary identity `GDR-CAND-20261010-G17-PAT-02`. The recipe proposes recoverable actions inside a declared information and commitment boundary. It does not promise to erase a person’s knowledge, recover every mistake or override the rules of a particular event.

## Purpose

Permit correction of an eligible action while preserving the game’s declared limits on information, commitments and other participants’ choices. The distinctive question is not merely “can the resource be refunded?” but **“what has already become known, acted on, timed out or externally committed?”** [C-01, C-04]

This narrows the inspected `GDR-CAND-20261010-F07-PAT-02`, **Legible commitment and safe exit**. That pattern owns the broader commitment/exit framing. The new candidate addresses disclosure and shared-state dependency boundaries and remains subject to central overlap/ownership review. Its inspected witnesses are digital board-game documents; application to other genres is conditional synthesis. [C-01, C-06]

## Context and prerequisites

Use only when the intended rules permit some recovery and the team can identify the relevant state transitions, information recipients, pending/accepted actions, random disclosures and dependent decisions. The player needs an accessible way to distinguish preview, submission, accepted commitment, resolution and recovery. The policy must be available before an irreversible step without disclosing the hidden result itself. [C-04, C-05]

A safe-looking deterministic action may still reveal strategic intent when shown to another player. Conversely, a private pre-commit selection can often be revised without changing anyone else’s information. These are different cases. The pattern does not assume that the software can infer all human knowledge; where information effects are uncertain, use a conservative earlier boundary. [C-04]

**Exit condition:** if the rules forbid undo, source rules are unresolved, rollback dependencies cannot be identified, or authorized/private views cannot be preserved, do not offer post-commit recovery under this pattern. Prefer private previews, accessible confirmation or a separately declared teaching variant. Do not silently label a hindsight-enabled variant as information-preserving undo. [C-06]

## Mechanism and evidence

Handelabra’s Spirit Island multiplayer documentation describes undo bounded by new-information disclosure. Dire Wolf’s June 2026 notes report resource/state restoration problems around undo, and its later 4.1.0 notes include changed undo behavior. These are documented mechanism and regression witnesses, not proof that the complete recipe below is correct or beneficial. [C-02, C-03; GDR-SRC-20261010-G17-013; GDR-SRC-20261010-G17-010; GDR-SRC-20261010-G17-011]

| Link in the proposed mechanism | Support | Limit / possible failure |
|---|---|---|
| Identify disclosure and dependency boundaries → distinguish potentially reversible from committed actions | Conditional reasoning plus an official bounded-undo example [C-02, C-04] | A public selection, failed-action signal or partner response can reveal information before an obvious reveal animation. |
| Restore eligible state coherently → remove a specified input/action error | State-contract inference [C-04] | Restoring counters alone can omit random state, ownership, triggers, history or another participant’s accepted action. |
| Block later recovery → prevent forbidden hindsight advantage through that recovery route | Conditional inference [C-04] | Keeping the same random seed is insufficient once a player learned the outcome and can choose a different action. Other information side channels remain possible. |
| Explain the boundary accessibly → reduce surprise about irreversibility | Hypothesis [C-05] | Warnings can be missed, overused or themselves disclose hidden conditions. |
| Correct eligible errors → improve participation without harming other goals | Hypothesis [C-07] | Recovery can undermine intentional commitment, social accountability or pace; no player effect was measured here. |

## Recipe

1. **Record the permitted recovery policy.** Identify rules/edition, digital build, mode and any declared variant. Define the class of correction sought and who is authorized to request or approve it. If recovery is disallowed, stop and improve pre-commit handling instead. [C-04, C-06]
2. **Trace the action before implementing an undo button.** Record selection, submission, acceptance, costs, optional order choices, reveals, automatic effects, partner actions and timing effects. Include information transmitted through animations, logs, audio, notifications and invalid-action reasons. [C-04]
3. **Place the boundary conservatively.** An unpublished local preview is a different boundary from a published action, and both differ from a random reveal. If the action communicates strategically useful intent or enables another participant’s response, do not automatically treat it as local/reversible. [C-04, C-06]
4. **Define an eligible rollback unit.** Specify everything that must remain consistent: authorized resources/content, pending choices, relevant random state, trigger order, acknowledged history, clock policy and dependent commitments. Do not erase another person’s knowledge or record to claim the action never happened. [C-03, C-04]
5. **Explain before crossing the boundary.** Use a truthful rule-category message, such as “this step commits the choice and reveals previously unknown information,” when that is the declared rule. Do not say which hidden outcome or opponent option causes the boundary. Use a consistent reason class rather than a hidden-state-dependent message. [C-05]
6. **Apply only an authorized recovery.** Recheck eligibility against accepted state, not only an old local preview. A late acknowledgement, partner action or reveal can invalidate the earlier assumption. Where consent is allowed, explain exactly whose decision is affected; silence is not a general permission to reverse it. [C-04, C-06]
7. **Present a consistent recovered state.** Tell the requester what was restored and what remained committed using only permitted facts. If acceptance is unknown after an interruption, show the uncertainty rather than fabricating success or submitting a new action to simulate undo. [C-04, C-05]
8. **Test boundaries and remove unsafe recovery.** Include exploratory misuse, retries, concurrent actions, localization and access configurations. A missing guarantee is a reason to narrow the recoverable unit, not to assume the case never occurs. [C-08]

This is a design recipe, not engine code, an approved synchronization protocol, or a claim that an implementation can rewind arbitrary external effects.

### Adjustable variables

| Variable | Possible policies | Required distinction |
|---|---|---|
| Recoverable stage | Private preview; accepted but still eligible unit; expressly consented variant | Selection is not necessarily commitment; public intent disclosure matters. |
| Depth | Last eligible unit or a chain ending at a boundary | A fixed number of steps/seconds is not a substitute for dependency analysis. |
| Consent | Local only; affected-party agreement where rules permit; no recovery | Consent does not erase revealed facts or automatically preserve competitive comparability. |
| History visibility | Role-specific explanation of the recovered action | Logs must not publish private attempts or hidden outcomes. |
| Randomness | Preserve authorized state when an eligible unit is restored | Preventing rerolls does not prevent scouting once information was revealed. |
| Clock effects | Preserve, charge or adjust according to a predeclared mode policy | Undo must not accidentally provide unlimited decision time or punish an access need through an undocumented rule. |
| Teaching variant | Explicitly permit hindsight exploration if that is the chosen activity | Keep separate from a claim of information-preserving or ranked-equivalent recovery. |

No universal grace interval, undo depth, confirmation count or response deadline is supplied. [C-04–C-06]

## Worked examples

### Illustrative private selection versus revealed cargo

**Invented scenario; not a client observation or performed test.** A player selects a route privately. The interface shows its known food cost and destination before publication. The scenario permits private revision, so changing that selection can restore the preview without affecting other participants. The player then commits; payment occurs and a previously unknown cargo result is shown. [C-04]

After that reveal, refunding the food and restoring the same cargo token would not restore the player’s earlier knowledge. The player could now select another route based on the learned cargo. Therefore this policy stops at the reveal/commit boundary rather than offering a reroll or pretending that restoring the seed solved scouting. Before commit, the warning describes the category of irreversible information change, not the outcome. [C-04, C-05]

Now add a public route announcement before the reveal. An opponent responds by withdrawing an offer. Even though no random result has appeared, the request is no longer a purely private correction. The prior boundary must be moved earlier or handled under an explicit variant/consent policy. This exposes why “no random draw yet” is an insufficient eligibility test. [C-04, C-06]

### Illustrative simultaneous cooperative planning

Two participants plan contributions to a shared objective. One privately selects an amount but has not published or enabled another choice: local revision may be permitted. After publication, a partner commits a dependent contribution. Reversing only the first contribution can invalidate the partner’s plan. A declared cooperative policy could pause and seek affected-party agreement, but the explanation must state that the group is revising known commitments; it must not call this erasure of knowledge. [C-04, C-06]

If the system cannot distinguish submitted from accepted contributions after reconnect, show the unresolved status and recover authoritative state before offering the action again. This is a required question for the design contract, not evidence of a particular networking implementation. [C-04, C-05]

## Tradeoffs and alternatives

**Private preview/cancel** is simpler and preserves more boundaries, but cannot repair every post-commit error. **No post-submit undo** can preserve a competitive policy while increasing the importance of readable confirmations and accessible input. **Explicit teaching hindsight** can support exploration while intentionally changing the knowledge model. **A consensual tabletop-style takeback** may fit a social group but can create negotiation pressure and is not automatically appropriate for anonymous ranked play. Choose the policy that serves the declared activity, not the one with the longest undo history. [C-06, C-07]

Production costs include action dependency analysis, preserving authorized views, re-entry consistency and regression testing across content/locale changes. An additional recovery feature can create new failure routes. Patch notes justify examining these cases but supply no general estimate of cost or defect likelihood. [C-03, C-04]

## Failure cases and observable warning signs

| Failure | Observable sign in a proposed evaluation | Correction or stop |
|---|---|---|
| Outcome scouting | Player learns hidden content, reverses costs and chooses a different action | Move boundary before disclosure; do not rely solely on fixed randomness. |
| Partial rollback | Resources, triggers, ownership or history disagree after recovery | Disable the affected unit until its contract is demonstrably consistent. |
| Partner invalidation | Another accepted action becomes illegal or misleading | Trace dependent commitments; narrow to private changes or a declared variant. |
| Information-leaking explanation | Different reason text identifies a hidden opponent option | Use a consistent permitted-information explanation; examine timing too. |
| Clock exploitation | Recovery repeatedly grants extra response time or silently resets a deadline | Apply the stated timing policy and test interruption/access effects separately. |
| False success after reconnect | Local interface says “undone” while acceptance is unknown | Preserve pending/unknown status; do not infer authority from a local display. |
| Unusable safeguard | A required confirmation is inaccessible or narration exposes private facts | Revise the complete access route and withhold the usability claim. |

These are falsifiable risk cases, not reported defects in a named client unless the reference explicitly documents one. [C-04, C-05, C-08]

## Counterexamples and do-not-use conditions

Do not apply the pattern to a ruleset whose chosen experience requires binding commitments, to authoritative external transactions, or to actions whose effects cannot be coherently accounted for. An intentional cooperative hindsight mode is not “unsafe” merely for allowing hindsight, but it is **outside the information-preserving claim**. Label it as a different mode and do not silently combine its outcomes with a no-hindsight comparison. [C-06]

A no-undo implementation can be preferable when a strong pre-commit preview solves the actual access problem at lower cost. Conversely, player errors should not be moralized as a reason to deny useful correction where the rules allow it. Whether recovery improves participation or dilutes the desired challenge remains a proposed evaluation question. [C-07]

## Proposed playtest and falsification — not performed

First propose a **conformance scenario set** before a participant study: legal and illegal recovery on either side of disclosure; public intent without randomness; a hidden draw with fixed randomness; a concurrent partner commitment; reconnect during acknowledgement; repeated requests; clock effects; changed content revisions; and localized/nonvisual explanations. Define expected authorized views and state outcomes before execution. The scenarios have not been run. [C-08]

Then compare an appropriate private-preview policy, the proposed bounded policy and a no-post-submit policy under the same rules. Include new and experienced players, participants affected by relevant input/access demands, and both cooperative and competitive contexts only when the intended application includes them. Preserve accommodations; separate simulated mistakes from real frustration, and separate rule understanding from preference. [C-07, C-08]

Measure successful eligible recovery, unauthorized information gains, invalidated partner choices, rule-boundary understanding, workload and perceived agency. Ask participants to explain why an action can or cannot be reversed rather than merely click the enabled button. Same-rule changed-situation probes must remain separate from a newly taught rule revision. [C-08; DEP-F01-PAT]

**Reject or narrow the information-preserving claim** after any forbidden disclosure advantage or inconsistent dependency restoration in the specified scope. That is a logical failure of the declared contract, not a statistical threshold. The participant-benefit claim additionally fails if eligible recovery brings no valued improvement, introduces unacceptable burden, or changes the desired commitment experience. Predeclare local practical bounds; no participant count, effect size or universal timing rule is supplied. [C-04, C-07, C-08]

## Claim ledger

| Claim | Class | Source / locator | Confidence and limits |
|---|---|---|---|
| C-01: This pattern narrows broad recovery to disclosure and shared-commitment boundaries | inference | DEP-F02-DEC; DEP-F07-EXIT; explicit purpose | Moderate conceptual distinction; central overlap review pending. |
| C-02: Spirit Island documentation describes an information boundary for undo | observed-example | G17-013, Spirit Phase undo paragraph | High for official text; build unknown, no client test or efficacy finding. |
| C-03: Dune patch records identify restoration/undo changes across versions | observed-example | G17-010, 4.0.8/4.0.7/4.0.5; G17-011 UI/UX | High for reported fixes; not verification that all cases now work. |
| C-04: Reversal must account for persistent knowledge and dependent commitments, not only costs | inference | DEP-F02-DEC; G17-013; explicit state/knowledge analysis | High as a conditional logical limit; completeness of a real implementation unknown. |
| C-05: Accessible, nonrevealing boundary explanations may reduce surprise | hypothesis | DEP-P01-INFO; DEP-P01-ACCESS; DEP-P02-CUES; proposed interface | Low benefit confidence; warning side channels/usability untested. |
| C-06: Rules, consent and uncertainty can justify earlier boundaries or another recovery mode | inference | DEP-F07-EXIT; C-04; explicit counterexamples | Moderate conditional policy analysis; no adopted event policy. |
| C-07: Eligible correction may improve participation without harming valued commitment | hypothesis | C-02/C-04 bridge; proposed comparisons | Low: full causal chain and transfer beyond documented cases unvalidated. |
| C-08: The proposed scenario/test set can expose named contract failures | hypothesis | Playtest design; DEP-F01-PAT; DEP-F07-EVAL | Low until executed; logical falsifiers are not a coverage or reliability guarantee. |

`G17-010`, `G17-011`, and `G17-013` expand to the full source IDs below. Local issues **G17-ISSUE-04** and **G17-ISSUE-06** retain version-fidelity and recovery-policy boundaries.

## Related entries and history

Main application: [Board-game adaptation](../genres/board-game-adaptation.md), `GDR-CAND-20261010-G17-GEN-02`; conditional application: [Collectible card game](../genres/collectible-card-game.md), `GDR-CAND-20261010-G17-GEN-01`. Broad decision/recovery ownership is proposed for **BH-GDR-Foundations-and-Systems**, with Presentation and Interaction review of messages and access. This is not an approved ownership reassignment.

First captured revision `initial-capture-1`; no predecessor or supersession. Author self-review added public intent disclosure and partner dependencies as counterexamples to a too-simple “before random reveal” boundary. No independent review, implementation, player test or release occurred. The [review packet](../reviews/full-run-20261010-g17-review-packet.md) records the nonduplication question and complete artifact hashes.

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

### DEP-F07-EXIT
**GDR-CAND-20261010-F07-PAT-02 — Legible commitment and safe exit**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/legible-commitment-and-safe-exit.md`; relevant locator: Mechanism; context and recipe.
**Transferred scope:** Broad commitment/exit guidance; preserve consequences for other participants rather than promising consequence-free reversibility. **Byte identity:** 22,899 bytes; SHA-256 `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-P02-CUES
**GDR-CAND-20261010-P02-PAT-02 — Fact-preserving cue alternatives**, revision `review-correction-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/fact-preserving-cue-alternatives.md`; relevant locator: Mechanism; recipe and factual-equivalence limits.
**Transferred scope:** Preserve facts, uncertainty, entitlement and timing, not a promise of identical emotion or performance. **Byte identity:** 27,103 bytes; SHA-256 `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

## References

Access checked **2026-10-10, America/Los_Angeles** (retrieval session continued on 2026-10-11 UTC). Exact client builds are unknown unless a cited release note names one; release-note inspection is not client observation. `GDR-SRC-20261010-G17-*` are temporary source identities. Cross-batch URL/DOI/edition deduplication is pending Library Coordination. Lineage-only mentions of other batch source IDs resolve in the [review packet source ledger](../reviews/full-run-20261010-g17-review-packet.md#references); they are not additional supporting sources for this artifact.

### GDR-SRC-20261010-G17-010
**Dire Wolf Digital. Dune: Imperium Digital – June 2026 Patch Notes.** Dire Wolf Digital; publication/update: 2026-06-23 displayed; document covers several patches. [Source](https://news.direwolfdigital.com/dune-imperium-digital-june-2026-patch-notes/).
- **Edition/build; locator:** Versions 4.0.1–4.0.8; Uprising-era update; not current-build certification. 4.0.8 and 4.0.7 undo fixes; 4.0.5 resource restoration, tablet UI and gamepad fixes.
- **Access/type/provenance:** `relevant-excerpt`; Developer regression/fix record. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Reported corrections do not quantify defect frequency, prove all cases fixed, or establish current client behavior. Base-game 2020 rules are not the rules oracle for every included expansion. Same Dire Wolf production lineage as G17-008,009,011; repeated fixes are not independent effect studies.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-03; risk context for C-04.

### GDR-SRC-20261010-G17-011
**Dire Wolf Digital. Dune: Imperium Digital 4.1.0 Patch Notes – The Rep System Arrives!.** Dire Wolf Digital; publication/update: 2026-09-30. [Source](https://news.direwolfdigital.com/dune-imperium-digital-4-1-0-patch-notes-the-rep-system-arrives/).
- **Edition/build; locator:** Version 4.1.0 announcement; no installation or latest-build guarantee. The Rep System; UI/UX undo changes; Known Issues.
- **Access/type/provenance:** `relevant-excerpt`; Developer update and known-issues record. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Completion incentives are described, not shown to improve completion or to treat involuntary disconnects appropriately. The known-issues list prevents an all-correct claim. No precise reputation values are transferred. Same Dire Wolf production family as G17-008–010; source recency does not convert intent into outcome evidence.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-03 version-change witness.

### GDR-SRC-20261010-G17-013
**Handelabra Games. Spirit Island Multiplayer.** Handelabra Games; publication/update: unknown; URL retains beta wording but body reports launch. [Source](https://www.handelabra.com/spirit-island-beta).
- **Edition/build; locator:** Steam, iOS and Android named by the source; exact client build unknown. Launch introduction; Spirit Phase undo paragraph; General Multiplayer Information.
- **Access/type/provenance:** `relevant-excerpt`; Official multiplayer and recovery documentation. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Documents information-limited undo, live play and conflict handling. No current-client reproduction or benefit measurement; this is not an asynchronous-play source. Same production organization as G17-012; separate from Dire Wolf, but not independent validation of this packet’s undo recipe.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-02; mechanism context for C-04, not efficacy.
