---
id: GDR-CAND-20261010-G19-PAT-01
permanent_id: null
kind: pattern
title: Calibration–challenge separation
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_identity: G19-authoring-01
predecessor_sha256: null
supersedes: null
owner_project: BH-GDR-Genres
run: GDR-FULL-20261010
batch: G19
updated: '2026-10-11'
evidence_checked: '2026-10-11'
evidence_timezone: UTC; local date 2026-10-10 America/Los_Angeles
coverage_status: open
aliases:
- timing-bias diagnosis
- calibration versus difficulty
tags:
- timing
- diagnosis
- reversible-settings
- access
related_topics:
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns: []
related_genres:
- GDR-CAND-20261010-G19-GEN-01
source_ids:
- GDR-SRC-20261010-G19-001
- GDR-SRC-20261010-G19-002
- GDR-SRC-20261010-G19-006
reviewer: null
approved_by: null
approved_date: null
byte_hash_record: ../reviews/full-run-20261010-g19-review-packet.md#candidate-byte-manifest
---

# Calibration–challenge separation

**Draft research candidate, not released knowledge.** Scope: G19 only. Definitions and application recipes are reversible research proposals, not approved studio decisions. No game implementation, participant test, independent review or publication occurred in this batch.

## Purpose

**Calibration–challenge separation** is a diagnostic and authoring pattern for timing-sensitive interactions. Its intended purpose is to prevent a persistent timing mismatch, a faulty chart, inaccessible information and a chosen challenge level from being treated as the same problem. The desired outcome is a more interpretable decision about what to change—not a promise of higher scores, equal skill or lower measured hardware latency. [K-01, K-04]

The pattern is reusable beyond [rhythm](../genres/rhythm.md), wherever a reference event and an accepted action relationship matter. It is not an engine recipe, a latency certification procedure or an accessibility compliance standard. It deliberately does not allocate a universal tolerance, calibration sample count or acceptable error spread. [K-01, K-07]

## Context and prerequisites

Use it when a task has a defined timing reference, the implementation can distinguish at least some adjustment scopes, and a participant or tester reports a mismatch worth diagnosing. Before adoption, identify the executable/chart versions, chosen input and output routes, what the score or task judges, and which setting affects which relationship. A reversible configuration and a way to reach it without first passing the problematic task are prerequisites for the proposed player-facing flow. [K-01, K-03, K-06]

A **reference passage** is a controlled comparison stimulus, not automatically ground truth for a device’s physical latency. The person must be able to perceive the relevant cue and understand the requested action; otherwise tapping estimates mix access or comprehension with timing. Do not require mastery of a complex chart to configure a basic reference relationship. Do not remove needed access support to obtain a supposedly “pure” measurement. [K-04, K-07]

Stop the calibration interpretation when the reference is ambiguous, the setting’s sign/scope is unknown, the timing changes during the observation, or the proposed process cannot preserve the player’s preferred access route. Record a diagnostic gap or choose an explicit non-scoring/assistance route; do not manufacture a precise value. [K-01, K-07]

## Mechanism and evidence

The documented osu! global/local distinction is a feasibility example of scoped adjustments. It does not establish that all engines use the same sign, clock or target. [K-03; GDR-SRC-20261010-G19-001; GDR-SRC-20261010-G19-002]

For a deliberately simplified analysis, let `e_i` be an observed action-to-reference time difference. A pure fixed adjustment gives `e_i′ = e_i − k`. Then `e_i′ − e_j′ = e_i − e_j`: the pairwise differences and centered spread are unchanged. Thus a fixed shift can move a persistent bias without curing variable timing. This is algebra, **not a measurement of any named game**. It does not apply unchanged when a setting also changes scheduling, buffering or acceptance rules. [K-02]

An illustrative decomposition of observed error might include device/presentation relationships, chart-specific timing, cue interpretation, anticipatory player behavior and variable execution. The decomposition is not identifiable from a single trace; its terms are not assumed independent or directly observable. A stable early tap could be learned anticipation, a reference problem, or both. Reporting it as proven hardware delay would overstate the evidence. [K-07]

| Proposed causal link | Support | Limit and consequence |
|---|---|---|
| Separate adjustment scopes → interventions need not change every passage together | Documented scope distinction, plus explicit authoring control. [K-03] | Requires actual target semantics; do not import an offset sign from another product. |
| Pure fixed shift → moved center without removed variability | Exact result in the stated algebraic model. [K-02] | A real control may affect more than one timing relationship; inspect before interpreting. |
| Separate task probes → a better choice between content correction, access support and challenge change | Reviewed demand/input distinctions motivate an inference. [K-04, K-07] | Probe validity and causal identification are not established by a successful run. |
| Reversible, clearly named choices → improved understanding or perceived control | Hypothesis only. [K-06] | Setup may add burden, prime expectation or obscure a simpler solution. Must be tested. |

Gan et al.’s cue comparison reinforces the need to specify the stimulus rather than assume that every visual timing cue behaves alike. It does not validate this pattern’s calibration workflow. [K-05; GDR-SRC-20261010-G19-006]

## Recipe

1. **Declare the judged relationship.** State whether the action is judged against music, a visible event, an authored timestamp, a sustained interval or another reference. Name the exact chart/build and current settings. Exit with “reference unresolved” when these disagree rather than fitting a value to an undefined target. [K-01, K-07]
2. **Check access and rule prediction first.** Provide the relevant cue through the chosen route and ask what event or action is expected before demanding precision. Separate a person who cannot perceive/interpret the event from one who predicts correctly but cannot execute it. Keep the check brief and retain accommodations. [K-04]
3. **Compare scopes without changing challenge.** Use more than one known passage to ask whether a mismatch is broad or confined to particular content. Inspect existing chart/reference metadata before changing a global setting. A passage-specific problem is a reason to investigate content, not proof of a chart defect. [K-01, K-03]
4. **Inspect location and variability separately.** For a later authorized measurement, retain signed differences and their variation instead of only score. Treat a changing relationship as a diagnostic warning. Stop the fixed-correction path when variability or reference uncertainty dominates the question. No universal cutoff is prescribed. [K-02, K-07]
5. **Offer a reversible, explicitly scoped adjustment.** Explain what changes and what remains fixed, including whether scoring conditions change. Keep reset/undo available. Do not silently combine a timing correction, acceptance-window change and note-density reduction and then credit “calibration.” [K-01, K-06]
6. **Validate the interpretation on a different appropriate passage.** Hold the intended rule and demand comparable while changing the specific event sequence. Check whether improvement generalizes beyond the familiar reference. When the effect is local, return to content or learned anticipation as alternatives. [K-04, K-07]
7. **Offer challenge or expression choices separately.** A player can choose a less demanding action pattern, forgiving score mode or free performance even after a reference is aligned. Name these as design choices, not calibration failures or personal deficits. Preserve the chosen precision mode when that is the desired experience. [K-01, K-04]
8. **Record the result and recheck trigger.** Record configuration, affected scope, unresolved causes, local acceptance rule and whether the participant valued the change. Recheck when relevant hardware, chart, rendering or input behavior changes. If the process remains uninformative, stop and reduce the claim; do not store a misleading “certified” value. [K-06, K-07]

## Adjustable variables and decision points

| Variable | What may be adjusted | What must remain explicit |
|---|---|---|
| Reference stimulus | Passage, modality, tempo/pattern, preview | Whether it is independently verified or only a comparison stimulus. |
| Scope | Common output/input relationship versus local content relationship | Exact setting behavior; engine-specific signs are not transferred. |
| Diagnostic observations | Prediction, signed timing, variation, task result, comfort | Different constructs and denominators; no single score diagnoses cause. |
| Challenge | Accepted action, density, simultaneous demands, failure consequence | A challenge change is not represented as physical calibration. |
| Recovery | Reset, undo, save per configuration, later re-entry | No compelled scored success or unsupported claim of permanence. |
| Success criterion | Locally defined stability of interpretation and valued outcome | Set before comparison with appropriate participants; no universal threshold. |

All variable recommendations are conditional proposals under [K-01, K-04, K-06, K-07], not tested settings.

## Worked examples

**Illustrative example A: broad stable mismatch.** A prototype uses a known reference phrase and a separate scored song. A player predicts the required action correctly and produces similarly shifted differences in both. The designer verifies the setting’s target, proposes a reversible common adjustment without changing the chart, and compares a new passage. Even if the score rises, the record says only that this configuration/participant benefited under those conditions; it does not claim the estimated value is pure hardware delay. If variation remains large, a fixed shift is not represented as curing it. [K-01, K-02, K-07]

**Illustrative example B: one-content problem.** A reference and most passages align, while a single chart section appears displaced. The designer checks that section’s intended musical reference and timing annotation rather than altering the whole catalog. An expressive off-grid accent may be intentional, so the remedy might be clearer preview or explanation rather than retiming the action. The pattern ends without a correction when the original design is understood and preferred. [K-01, K-03, K-04]

**Illustrative example C: correct understanding, unsuitable action demand.** A person correctly predicts a complex phrase but cannot execute the required simultaneous actions. A remap, lower simultaneous demand or separately labeled forgiving mode is investigated. Changing global offset alone is not a justified answer. Conversely, someone playing an unscored free instrument may need no timing calibration at all. [K-01, K-04]

These are invented applications. No prototype, instrumented trace, participant or comparison was executed in G19.

## Alternatives and tradeoffs

A simple well-explained default with optional manual adjustment may be less burdensome than a diagnostic wizard. A verified content correction may be preferable to asking every player to compensate for one chart. A broader accepted-action range may be appropriate where expression matters more than score precision, provided it is described honestly. A fully freeform mode can remove the judged timing reference altogether. These choices answer different goals rather than form a quality ranking. [K-01, K-04, K-06]

The proposed separation requires content provenance, clear settings, retention of comparable references and device-sensitive evaluation. It can overcomplicate an occasional timing task, produce false confidence from noisy traces, or make players feel tested before they can play. Competitive score policy is a separate responsibility: neither assistance stigma nor unexamined score pooling is justified by this pattern. [K-06, K-07]

## Failure cases, counterexamples and do-not-use conditions

| Failure or counterexample | Observable warning | Response / exit |
|---|---|---|
| Drift, variable scheduling or inconsistent execution is called a constant offset | Correct-looking adjustment changes from passage to passage or moment to moment | Stop fixed-correction interpretation; investigate the source of variability. [K-02, K-07] |
| Calibration task is itself inaccessible | Person cannot perceive the event or predict the requested action | Restore a usable route or choose a different reference; do not infer low rhythm ability. [K-04] |
| A chart’s intentional rhythm is “corrected” toward a simplistic grid | Adjustment conflicts with the stated phrase interpretation | Review musical intent and presentation; do not enforce a grid as truth. [K-01] |
| Wizard improvement is actually easier scoring | Acceptance rules changed with the offset | Separate conditions and relabel the intervention. [K-01, K-06] |
| Setup burden exceeds the value for casual/freeform use | Player prefers the original workflow or wants no scored timing | Offer the simpler route; do not mandate this pattern. [K-06] |
| A laboratory/device claim is inferred from software scores | Report contains a precise hardware number without independent reference | Withdraw the hardware attribution; preserve the narrower observation. [K-07] |

## Falsifying proposed playtest

**Not performed.** After separate implementation/test authorization, compare the separated flow with the existing simple adjustment flow and an explicitly labeled assistance alternative. Use matched passages and document the exact settings; include relevant experience and access profiles, counterbalance learning where feasible, and analyze repeated observations within each participant/configuration rather than treating every tap as a new person. [K-01, K-04]

Measure rule prediction, signed timing location, spread, error on an unfamiliar matched passage, configuration comprehension, comfort, time/burden and preferred choice separately. Confounds include expected “better” settings, practice, anticipation, musical familiarity, reference error, varying device behavior and simultaneous changes to scoring. A high score is not sufficient to select this pattern. [K-04, K-06, K-07]

Reject or narrow the pattern when it cannot reliably distinguish the local alternatives, produces no valued benefit over a simpler flow, confuses setting semantics, or improves one preferred route by making another inaccessible. Reject a constant-correction explanation if spread reduction only appears after changing other mechanics. Define practical comparison criteria with the intended audience before testing; no participant count, timing window or effect guarantee is specified. [K-01, K-02, K-06]

## Related entries, ownership and open questions

Primary adaptation: [Rhythm](../genres/rhythm.md). Party-rhythm applicability is conditional on shared-device and turn-taking needs, not a new genre. Shared concepts remain owned by Presentation and Interaction (controls, feedback, modality/access) and Foundations and Systems (difficulty, evaluation). A proposed pattern handoff to those owners awaits Coordination; this G19 candidate does not replace their entries.

Open questions: measurement validity, hardware versus user attribution, actual wizard burden, expressive/off-grid references, different sensory access populations and ranked-mode policy. `G19-X01` and `G19-X02` remain open. Additional chart-provenance work is queued in the packet, not extracted as another G19 pattern.

## Claim ledger

Claim labels attach to the stated proposition, not every possible application of a cited title. An inference is not promoted to an empirical finding by borrowing a citation. Proposed tests are **not performed**.

| Claim | Proposition | Class | Sources | Locator / support and bridge | Confidence and scope | Open question / contrary case |
| --- | --- | --- | --- | --- | --- | --- |
| K-01 | Separate calibration, chart correction and challenge selection when diagnosing timing failures. | hypothesis | GDR-SRC-20261010-G19-001; GDR-SRC-20261010-G19-002 | Documented global/local distinction motivates the recipe; no comparative recipe test. | moderate for diagnostic plausibility; low for player benefit | Misdiagnosis remains possible when reference or player timing is unstable. |
| K-02 | A constant correction changes timing-error location but not pairwise differences or centered spread. | inference | G19 reasoning / inspected dependencies | Algebra in Mechanism and evidence: e_i′ = e_i − k. | high for the stated constant-shift model, not for a real pipeline with other changes | If the implementation changes scheduling, acceptance or variance too, this is not a pure constant shift. |
| K-03 | The inspected osu! pages describe universal/local offset scope and a user-facing adjustment workflow. | observed-example | GDR-SRC-20261010-G19-001; GDR-SRC-20261010-G19-002 | Universal offset / Adjusting; Offset Wizard use. | high for documentation; executable unverified | Verify adjustment semantics in the target version before applying signs or scope. |
| K-04 | Separating prediction, execution and outcome can avoid treating all misses as one difficulty problem. | inference | G19 reasoning / inspected dependencies | Inspected F02-TOP-02 61–99; P02-TOP-01 77–94; F07-TOP-01 65–93. | moderate: reviewed conceptual distinctions, not a tested G19 intervention | Can the proposed probes actually separate the local bottlenecks? |
| K-05 | Timing performance can depend on how a cue represents temporal structure; a modality label alone is insufficient. | empirical-evidence | GDR-SRC-20261010-G19-006 | Experiments 1–2 and Discussion; narrow tapping context. | moderate for that experiment; indirect to this recipe | No tactile or game-enjoyment equivalence is established. |
| K-06 | A reversible calibration flow plus a separate assistance choice may make recovery more interpretable. | hypothesis | GDR-SRC-20261010-G19-002 | Existing adjustment workflow supplies feasibility example; control/benefit link untested. | low: causal user benefit unvalidated | Does additional setup confuse or burden the intended player? |
| K-07 | Do not infer hardware latency or player ability from a single software timing trace. | inference | G19 reasoning / inspected dependencies | Non-identifiable illustrative error decomposition; inspected input/evaluation distinctions. | high for ambiguity of mixed causes; not a measured device claim | Which additional observation would discriminate the plausible causes? |

## References

All access dates are **2026-10-11 UTC (2026-10-10 America/Los_Angeles)**. The observer is this G19 authoring session. Document observations are observations of the cited artifact, not runtime gameplay. Public works are paraphrased; copyright remains with authors/publishers, and redistribution licenses were not audited. No screenshots, source text copies, music, rulebooks or participant data are redistributed. Source IDs are temporary; cross-batch/global deduplication by URL/DOI/edition remains pending.

### GDR-SRC-20261010-G19-001

osu! wiki contributors. **Universal offset**. osu! wiki. Publication/update: unknown. [Inspected source or recorded lead](https://osu.ppy.sh/wiki/en/Offset/Universal_offset). Edition/build: live documentation; applicable executable build unverified. Access: `full`. Type: primary project documentation. Locator: Universal offset, paragraphs 1–5; Adjusting universal offset; parsed lines 15–34. Supports: K-01, K-03. Limits: Document behavior only; offset sign and effect are implementation-specific. No executable or device timing measured. Independence: Same wiki/source family as 002; not independent corroboration.

### GDR-SRC-20261010-G19-002

osu! wiki contributors. **Offset Wizard**. osu! wiki. Publication/update: unknown. [Inspected source or recorded lead](https://osu.ppy.sh/wiki/en/Client/Options/Offset_Wizard). Edition/build: live documentation; executable build unknown. Access: `full`. Type: primary project documentation. Locator: Offset Wizard description and use, parsed lines 15–24. Supports: K-01, K-03, K-06. Limits: Documented adjustment workflow; does not establish that player taps isolate hardware delay. Independence: Same project documentation family as 001.

### GDR-SRC-20261010-G19-006

Lingyu Gan; Yingyu Huang; Liang Zhou; Cheng Qian; Xiang Wu. **Synchronization to a bouncing ball with a realistic motion trajectory**. Scientific Reports 5, article 11974. Publication/update: 2015-07-07. [Inspected source or recorded lead](https://www.nature.com/articles/srep11974). Edition/build: DOI 10.1038/srep11974; original article. Access: `relevant-excerpt`. Type: original empirical research. Locator: Results: experiments 1 and 2, lines 91–110; Discussion, lines 151–162; Methods—Participants and Stimuli and procedure, lines 165–182. Supports: K-05. Limits: Main experiments recruited 15 each; experiment 2 analyzed 14; overlapping participation. Healthy-hearing adults; simple finger tapping, not game enjoyment or disability access. Figures, supplement and raw data not independently inspected. Independence: Original study; its cited earlier papers were not separately inspected. No claim of equivalence from nonsignificance.

## Inspected shared-dependency records

These are **selected, parent-reviewed but unreleased draft bytes**, not newly validated public evidence. The original public sources behind them were not all reopened. Only the following scoped guidance transfers. Full receipt and missing links: [reviewed dependencies](../reviews/full-run-20261010-g19-review-packet.md#reviewed-dependencies). Dependency files are deliberately not reissued in this G19 delivery.

- **GDR-CAND-20261010-F02-TOP-02**, *Challenge and difficulty*, version 0.1.0, revision `independent-review-correction-1`. Archive member `selected-drafts/topics/challenge-and-difficulty.md`, lines 61–99. SHA-256 `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1`. Transfer: Separate sensory, rule, planning, motor and social demands from failure punishment and recovery.
- **GDR-CAND-20261010-P02-TOP-01**, *Controls and input*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/controls-and-input.md`, lines 77–94. SHA-256 `b9235153ba8b742c6df47e9e23844d9ab5da82e4212ebd22f04e314f6ccce21b`. Transfer: Distinguish input acquisition, recognition, eligibility and feedback; remapping is not removal of timing demand.
- **GDR-CAND-20261010-P02-TOP-02**, *Feedback and game feel*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/feedback-and-game-feel.md`, lines 69–89. SHA-256 `6cf571a87946b9b40470cce966862219906f495b50c0b1db04e1ad7677ca4415`. Transfer: Input receipt differs from outcome; sensory intensity is not a universal substitute for informative feedback.
- **GDR-CAND-20261010-P01-TOP-03**, *Accessibility and inclusive interaction*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/accessibility-and-inclusive-interaction.md`, lines 56–103 and 243–265. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. Transfer: Task-chain access; preserve reviewed WCAG web/CSS scope and informative/vendor distinctions. No numerical defaults transferred.
- **GDR-CAND-20261010-F07-TOP-01**, *Evaluation and balancing*, version 0.1.0, revision `initial-capture-1`. Archive member `selected-drafts/topics/evaluation-and-balancing.md`, lines 65–93. SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`. Transfer: Define outcome/denominator and causal comparison; paper checks do not validate physical timing.

## Review and history

Version 0.1.0; candidate revision `initial-draft-1`; initial bounded G19 capture, no predecessor or superseded submitted artifact. Exact bytes are identified in the review packet; wording changes retain this conceptual ID and require a new revision/receipt. Author self-review is recorded in the packet and is not independent review. Gate C is pending; only local static packaging checks are performed, not Gate D host tests; Gate E/release and game adoption are not authorized. Coverage remains open. The next decision is whether the independent reviewer accepts this bounded evidence treatment or requests specific corrections before Coordination considers further work.
