---
id: GDR-CAND-20261010-G12-PAT-01
kind: pattern
title: Pending-work reconciliation
version: 0.1.0
status: draft
candidate_revision: initial-author-draft-1
attempt_identity: G12-authoring-01
run_id: GDR-FULL-20261010
batch_id: G12
id_scope: run-scoped-temporary
owner_project: BH-GDR-Genres
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; dispatch and Los Angeles work date 2026-10-10 retained in run identity
coverage_status: open
aliases:
- committed versus delivered
- work-in-flight reconciliation
tags:
- feedback-delay
- commitment
- state-legibility
- diagnosis
related_topics:
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G12-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G12-GEN-01
- GDR-CAND-20261010-G12-GEN-02
- GDR-CAND-20261010-G12-GEN-03
source_ids:
- GDR-SRC-20261010-G12-003
- GDR-SRC-20261010-G12-006
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial G12 bounded research draft; previous batch identities and queues are not reset.
hash_record: ../reviews/full-run-20261010-g12-integrity-receipt.md
proposed_domain_owner: BH-GDR-Foundations-and-Systems; ownership/overlap review pending
---

# Pending-work reconciliation

**Unvalidated pattern candidate.** Use a focused distinction between what is usable now, what is already committed and what remains blocked before a player makes another delayed commitment. Its intended outcome is better-informed control, not fewer actions at any cost. There is no demonstrated G12 player benefit. [C-01, C-03]

## Purpose

Help a player answer: **“Does an existing commitment address this obligation within the relevant horizon, or does something else need to change?”** The target is not an empty number alone. A fulfilled requirement, an order placed and a resource physically available are different model states. A sensible preference can still favor extra capacity or redundancy after the player understands those states. [C-01, C-02]

## Context and prerequisites

Apply when interventions have meaningful delay, the player is entitled to inspect relevant commitments, and those commitments can be represented truthfully. Prerequisites are a defined obligation and horizon, authoritative identifiers or reliable aggregation, distinguishable transition states, a freshness rule, and a feasible response when work is blocked. The producer of a forecast must know whether it is deterministic, estimated or conditional. These are proposed conditions for this technique, not claims that every system needs a ledger. [C-02, C-04]

Do not begin with a universal state taxonomy. For a material-delivery decision, define the units and whether owned-but-reserved stock counts as available. For a service decision, installed capacity may not be reachable capacity. For a human task, consent, authority and scheduling can matter independently of nominal hours. The player should not have to solve unrelated accounting merely to receive one useful explanation. [C-02, C-06]

## Mechanism and evidence

| Proposed causal link | Support | Limit and falsifier |
|---|---|---|
| An action can be committed before its outcome is delivered. | The dynamic-investment source models a supply line; the Factorio account distinguishes new from current deliveries. [C-01; GDR-SRC-20261010-G12-003, GDR-SRC-20261010-G12-006] | These examples do not validate an interface. A purely immediate system has no useful pending distinction. |
| A truthful, horizon-specific representation can distinguish already-addressed from still-unmet obligations. | Inference from explicit state definitions and DEP-UI’s information contract. [C-02] | Unknown completion or overlapping counts can defeat the distinction; label uncertainty instead of inventing certainty. |
| That distinction may reduce unintended duplicate commitment or improve diagnosis. | **Hypothesis**, not a measured effect in these sources. [C-03] | The investment task offered information yet still produced difficulty. Visibility can be insufficient, confusing or irrelevant to the actual goal. |
| A response or stop control may restore meaningful authority. | Conditional inference from DEP-DECISION and documented stop semantics. [C-04] | Information without an actionable alternative may merely create frustration; stopping new work does not necessarily undo current work. |

The strongest recommendation is therefore **test a small, decision-local representation**, not “show every queue.” There is no warranted claim that exact forecasts, denser dashboards or more attention are inherently better. [C-03, C-06]

## Recipe

1. **Name one decision and its obligation.** Specify the resource/task, affected actor or place, deadline or horizon, and what the player can actually change. Separate a feasibility question from a preference or value judgment. Exit when no upcoming choice uses the distinction. [C-02]
2. **Define exclusive states for the selected unit.** For example, available, reserved, queued, in progress, in transit, blocked and completed can be useful, but only with definitions that avoid counting the same item twice. Preserve cross-references when a task and its required material use different units. Do not add quantities with incompatible units. [C-02]
3. **Reconcile commitments against the horizon.** Identify which pending work can address the obligation and under which assumptions. Distinguish an order from assured arrival; an installed building from usable service; a blocked promise from delivered output. Use a categorical or uncertain answer when an exact forecast is unsupported. [C-02, C-04]
4. **Present the smallest useful causal explanation.** At the decision point, show the current constraint, relevant existing commitment, expected or unknown transition and data freshness. Offer drill-down rather than require every history panel to remain open. Keep entitled information accessible through suitable modalities. [C-03, C-05]
5. **Explain the available intervention and its limits.** Alternatives may include waiting, reprioritizing, repairing, replacing, making a new commitment or accepting a shortfall. State whether “stop” prevents new work, cancels queued work or also affects current execution, and what remains paid or irreversible. Exit to an honest inspection-only view when the model cannot support the implied control. [C-04]
6. **Check difficult state transitions before any player-benefit claim.** Later implementation review should inspect stale information, cancellation, reallocation, partial delivery, changed rules and lost connectivity. These are proposed checks; no project code is run here. [C-04, C-05]
7. **Compare against a simpler alternative.** Use changed-answer cases with accommodations retained. Revise or remove the view if it does not improve the chosen decision, adds excessive burden, leaks intended uncertainty or suppresses desired redundant planning. [C-03, C-06, C-07]

### Adjustable variables and exit conditions

Tune aggregation by job, resource, district or time horizon; visibility on demand versus persistent display; categorical versus numerical forecasts; displayed history depth; exception severity; and degree of control. No universal refresh rate, queue size, display density or forecast precision is proposed. Larger values are not inherently improvements. [C-05]

Stop extracting the pattern into a product design when its state cannot be made truthful, when apparent pending work is actually unknowable to the player, or when the desired activity is discovering the concealed relation. A summary warning or post-scenario explanation may be preferable. Required access supports are never removed merely to keep a causal rule mysterious. [C-05, C-06]

## Worked examples

### Illustrative spare-parts obligation

**Synthetic and deterministic for this example; not a playtest result.** Six parts are required before tomorrow’s deadline. Two unreserved parts are available. Four previously ordered parts will arrive before the deadline under the stated scenario assumptions. The commitment view answers that the six-part obligation is covered without a new order; it does not claim the player should reject extra reserves. [C-02, C-07]

In the changed case, the same four parts arrive after the deadline. The correct deadline-feasibility answer is now **no**, despite identical current stock and order quantity. The useful explanation is the timing mismatch, not “order less.” A third optional case makes the shipment’s timing unknown; the honest answer is conditional rather than automatically yes or no. This adaptation preserves the reviewed F01 distinction between changed surface values and a genuinely discriminating answer. [C-07; DEP-TRANSFER]

The interface offers waiting, an alternative supply route, rescheduling the obligation or accepting a shortfall where the invented rules allow. When a rule is disabled, the screen describes what happens to the four existing parts. The historical Factorio delivery example motivates checking this boundary, not copying its semantics into every game. [C-04]

### Illustrative district service

A fictional clinic has completed construction, but its connection is unavailable. “One clinic built” and “service reaching this district” should not be counted as the same fulfilled obligation. A local view can show connection repair already committed; a global completed-building count may hide that dependency. This example follows its stipulated rules and does not claim any named game works this way. [C-02, C-06]

## Tradeoffs and alternatives

A reconciliation view consumes attention, screen space, localization work and reliable state history. It can encourage players to overtrust an estimate or reduce a richer decision to arithmetic. A short explanation at commitment time, a single blocked-work indicator, optional history or slower pace can be a cheaper alternative. Full disclosure can spoil discovery; a carefully scoped log can leave the underlying hypothesis for the player to infer. [C-05, C-06]

The technique complements [bounded delegation contract](bounded-delegation-contract.md): delegated work needs interpretable commitments when players retain supervisory responsibility. It differs from F03’s cataloged conversion-loop-budget candidate, whose selected contents were not available; this pattern addresses pending state and timing, not exchange-loop exploitation. Ownership and overlap with Foundations remain pending. [C-08]

## Failure cases and do-not-use conditions

**Double counting:** reserved parts appear in “available” and “pending completion.” Warning sign: the interface promises capacity the model cannot supply. Correct the unit and state definitions before evaluating player understanding. **False certainty:** a traffic-dependent arrival is displayed as guaranteed. Warning sign: players cannot reconcile missed predictions with visible assumptions. Use an uncertainty category or explain the changing condition. [C-02, C-04]

**Burden without authority:** the player studies a queue but cannot alter any relevant outcome. A summary or a different decision may be more appropriate. **Wrong target:** a player intentionally holds redundancy, while the evaluation labels extra orders a failure. Compare behavior to the chosen objective, not a presumed efficiency optimum. **Lost play:** inspecting all relations eliminates the intended discovery or scheduling challenge. Offer optional inspection or omit the pattern. [C-03, C-06]

Do not use this as a disguised promise of optimal ordering, as proof of real-world management competence, or as a substitute for clarifying the model’s actual behavior. [C-03, C-07]

## Proposed playtest — not performed

Compare a minimal current-state view, a concise commitment explanation and a fuller queue view while holding the underlying scenarios and controls constant. Include feasible-before-deadline, late, blocked and unknown cases. Counterbalance order where appropriate; retain the same access accommodations; recruit across relevant planning/numeracy experience and access needs. Choose study size from the later design and variability, not an arbitrary genre rule. [C-07]

Ask for **prediction, reason and chosen action separately**. Measures can include correct feasibility discrimination, unintended duplicate commitment, missed obligations, confidence calibration, time spent inspecting, perceived burden and whether valued choices remain. Confounds include prior model knowledge, display density, arithmetic difficulty, scenario order and learning from previous cases. A preference for a redundant order is not scored as a comprehension failure when its rationale is compatible with the chosen goal. [C-07]

Reject or narrow the benefit claim when the new view fails to improve the preregistered decision measure, creates unjustified confidence, increases important access errors, or costs more valued play than it enables. If it helps only a subgroup or situation, retain that condition rather than average it into a universal result. Model accounting checks are separate from this unperformed player test. [C-03, C-07]

## Related entries, coverage and history

Applies conditionally to [simulation](../genres/simulation.md), [management](../genres/management.md) and [city builder](../genres/city-builder.md). Related contradictions: **G12-CON-01** and **G12-CON-03**. Evidence supports the existence of delayed commitments and meaningful stop boundaries; the interface-to-player-benefit links remain hypotheses. Exact display design, runtime state reliability and cultural/access differences are open. [C-01–C-08]

Version `0.1.0`, `draft`, revision `initial-author-draft-1`. No predecessor, supersession, player study or independent review. Proposed shared owner: BH-GDR-Foundations-and-Systems, subject to Coordination’s overlap check. Additional model-scope and maintenance techniques are queued, not silently folded into this recipe.

## Claim ledger

Claim IDs are local to this artifact. Bare three-digit source numbers in a ledger expand to `GDR-SRC-20261010-G12-`; DEP labels resolve in Reviewed dependency provenance. Family abbreviations such as G12-PAT-01 expand to `GDR-CAND-20261010-` plus that family suffix. Confidence concerns the stated claim, not a general endorsement. Recommendations and synthetic examples are not studio-approved decisions. No unperformed test is evidence.

| Claim | Precise claim | Class | Source and locator / reasoning | Confidence and applicability | Unresolved question |
|---|---|---|---|---|---|
| C-01 | A committed action and a delivered outcome can be different states with consequential delay. | inference | 003 supply-line formulation, printed p.26; 006 Logistic chest enable/disable. | High for this distinction in the cited models, not every game. | Does the target decision actually involve delayed commitments? |
| C-02 | A defined unit, horizon and nonduplicated state partition can support truthful obligation reconciliation. | inference | DEP-UI task information contract; explicit spare-parts/district assumptions; no general player effect inferred. | Moderate logical support; actual state reliability must be verified. | Are forecast assumptions and units valid and visible? |
| C-03 | A focused commitment view may improve decisions, but visibility alone is not established as sufficient. | hypothesis | 003 METHOD/Discussion provides a contrary constraint; this recipe is not an intervention tested there. | Low causal confidence; strongest claim requires a direct comparison. | Does it improve a valued decision rather than merely expose more data? |
| C-04 | Stop and recovery controls should distinguish new, queued and executing commitments and their irreversibility. | inference | 006 Logistic chest enable/disable; DEP-DECISION reversibility passages. | Moderate conditional reasoning; historical semantics need not be copied. | Which consequences can the target system actually reverse? |
| C-05 | Aggregation, disclosure, freshness and alternative access should be chosen for a local decision rather than fixed universal thresholds. | hypothesis | DEP-UI; DEP-ACCESS; adjustable variables in this recipe. | Low implementation-specific confidence; no user testing performed. | What is the minimum truthful and accessible explanation? |
| C-06 | Omit or narrow the pattern when inspection burden, absent authority or lost discovery outweighs its purpose. | hypothesis | DEP-DECISION entitled information; counterexamples in this artifact. | Moderate design rationale, low outcome evidence. | Which desired activity would the additional view remove? |
| C-07 | A proposed test must distinguish changed-answer prediction from preference and preserve access supports. | hypothesis | DEP-TRANSFER corrected example lines96–127; DEP-EVALUATION; spare-parts illustration. | Moderate construct rationale; protocol unperformed. | What result rejects the benefit, including overload and confidence errors? |
| C-08 | This candidate addresses delayed commitments, while shared ownership and possible overlap require later coordination. | inference | G12 scope and packet; F03 original inventory only, not selected pattern bytes. | High for intended candidate scope, not a completed duplicate-content audit. | Does Foundations identify an existing same-purpose pattern? |

## References

Observer: the G12 authoring assistant, through document inspection, not game execution. Access/check date: **2026-10-11 UTC**. Source IDs are temporary run-scoped identities, reused within G12. Cross-batch canonical URL/DOI/edition deduplication remains pending. `relevant-excerpt` does not mean the full work, runtime or linked material was inspected.

### GDR-SRC-20261010-G12-003

**John D. Sterman. _Misperceptions of Feedback in Dynamic Decision Making_.** Publication/update: 1989. Publisher: International System Dynamics Conference proceedings; condensed reprint of an Academic Press journal article. [Inspected source route](https://proceedings.systemdynamics.org/1989/proceed/plenary-pdf/sterm021.pdf).

**Claims supported or used as an inference/hypothesis premise:** C-01; contrary constraint on C-03. **Edition/build:** Eleven-page proceedings scan, printed pp. 21–31; first-page footnote identifies condensed reprint from Organizational Behavior and Human Decision Processes 43 (June 1989), original pp. 301–335; DOI 10.1016/0749-5978(89)90041-1 identifies original, not a separately inspected text. **Access:** `relevant-excerpt`. **Type:** Original empirical research, accessed through author conference reprint. **Exact locator:** PDF pp. 1–4, 6–8 (printed pp. 21–24, 26–28): title/footnote; METHOD; representative trajectories/Fig. 3; supply-line formulation; Discussion and Fig. 5. These pages were visually inspected using web screenshots.

**Rights:** Academic Press copyright noted; paraphrase only, no scans or figures redistributed. **Limits and independence:** N=49 selected fluent-English students/professionals in a capital-investment task, not a game-audience sample. Full state/history available, no time limit. Reported oscillatory performance does not identify the effect of a new dashboard. Fig. 5 is model simulation, not a second human experiment. Full journal, raw data and uninspected tables not used; no effect size, confidence interval or replication claim transferred. Distinct from Sterman’s 1989 Management Science beer-distribution paper. Author overlap with 004 does not create replication.

### GDR-SRC-20261010-G12-006

**Klonan. _Friday Facts #428 – Reactor & Logistics circuit control_.** Publication/update: 2024-09-13. Publisher: Wube Software / Factorio development blog. [Inspected source route](https://www.factorio.com/blog/post/fff-428).

**Claims supported or used as an inference/hypothesis premise:** C-01/C-04. **Edition/build:** Pre-2.0 development description; executable build unknown. **Access:** `relevant-excerpt`. **Type:** Firsthand development account. **Exact locator:** “Reactor circuit connection”; “Roboport circuit improvements”; “Logistic chest enable/disable”.

**Rights:** Copyrighted blog; paraphrase only. **Limits and independence:** Reports direct reactor signals, tracking limits and disabling new requester orders while existing deliveries finish. Does not validate agency or accessibility effects. LAN-party feedback is an author account, not an inspected controlled dataset; same production line as 005.

## Reviewed dependency provenance

These are inspected **parent-selected reviewed drafts**, not released references and not new G12 sources. Their underlying cited papers were not automatically re-inspected. Only the named passages are transferred as qualified research guidance. Exact bytes came from the materialized waves 1–2 archive; they are not copied into this output. Full archive and gap receipts are in the [batch dependency record](../reviews/full-run-20261010-g12-review-packet.md#reviewed-dependencies).

**DEP-TRANSFER: `GDR-CAND-20261010-F01-PAT-01`**, version `0.1.0`, `draft`, candidate revision `independent-review-correction-1`. Archive path `selected-drafts/patterns/supported-attempt-and-transfer-check.md`. Inspected: Recipe; corrected Worked examples, lines 96–127: vary the correct feasibility answer, retain accommodations, separate preference from rule prediction. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`.

**DEP-UI: `GDR-CAND-20261010-P01-TOP-02`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/interface-and-information.md`. Inspected: Task information contract and availability-to-recovery diagnostic, lines 55–85. SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`.

**DEP-ACCESS: `GDR-CAND-20261010-P01-TOP-03`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/accessibility-and-inclusive-interaction.md`. Inspected: Applicability/scope and access chain, lines 56–103; P01 CORRECTION_RECEIPT.md. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`.

**DEP-DECISION: `GDR-CAND-20261010-F02-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/decision-design.md`. Inspected: Entitled information, uncertainty, opportunity cost and reversibility, lines 63–104. SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`.

**DEP-EVALUATION: `GDR-CAND-20261010-F07-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/evaluation-and-balancing.md`. Inspected: Evidence-to-question distinctions, lines 65–94: correctness checks do not measure enjoyment. SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`.

**Transfer boundary:** preserve source/candidate identities as recorded. No universal UI pixel, contrast, timing, difficulty or sample-size rule is imported. F01’s corrected feasibility/transfer discrimination is retained; access supports are not faded as tutorial prompts. Later reviewed simulation/economy/spatial-topic bytes remain missing unless explicitly identified in the packet.

