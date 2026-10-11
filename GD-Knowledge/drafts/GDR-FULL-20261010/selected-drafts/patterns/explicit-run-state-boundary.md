---
id: GDR-CAND-20261010-G16-PAT-01
kind: pattern
title: Explicit run-state boundary
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
- typed run reset
- selective persistence contract
- what survives a run
tags:
- run-state
- persistence
- defeat
- interruption
- re-entry
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F02-PAT-02
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G16-GEN-01
- GDR-CAND-20261010-G16-GEN-02
- GDR-CAND-20261010-G16-GEN-03
source_ids:
- GDR-SRC-20261010-G16-003
- GDR-SRC-20261010-G16-005
- GDR-SRC-20261010-F02-012
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
source_deduplication: pending-library-coordination
---

# Explicit run-state boundary

**Draft pattern; the complete benefit is a hypothesis.** This is a reusable technique for a game whose attempt boundary resets some state but preserves other state. It is not a recommendation that games need permadeath, upgrades or any particular save policy. No player-facing implementation or study was performed.

## Purpose

Help players and designers distinguish **what is lost, retained, changed or newly available when an attempt ends**, including how ending differs from pausing or recovering after an interruption. The intended outcome is informed, usable commitment and re-entry—not increased retention, a specific difficulty level or compulsory acceptance of harsh consequences. [C-01–C-03]

The new contribution is a **typed state transition at a run boundary**, connected to a compact player-facing explanation and a falsifiable understanding check. The existing reviewed **Legible commitment and safe exit — GDR-CAND-20261010-F07-PAT-02** already owns broader disclosure/refusal ethics; this pattern must not duplicate or replace it. Proposed shared ownership is Foundations and Systems, subject to Library Coordination’s overlap review. [C-02, C-03]

## Context and prerequisites

Apply when there is a recognizable attempt or episode and a real risk of confusing unlike persistence rules: for example, a character resets while account opportunities and story state remain. Documentary contrasts in NetHack, Rogue Legacy and Hades justify investigating mixed persistence; they do not validate this recipe’s effect. [C-01]

The design team must be able to state the actual transition rules, identify ordinary access configuration, enumerate meaningful triggers, and decide what information is intentionally unknown. It needs authority to change an inaccurate rule or explanation, not merely to add a confirmation screen. It also needs a viable approach to interruption appropriate to the intended activity; this pattern cannot promise one when the underlying design has none. [C-02–C-05]

**Do not begin deployment** while reward eligibility, save behavior, shared-player consequences or current-build state are uncertain. A research specification may record alternatives and unanswered questions, but it must not present those alternatives as implemented facts. No independent implementation approval follows from this draft. [C-05, C-06]

## Mechanism and evidence

| Link in the proposed causal chain | Inspected basis | Remaining uncertainty |
|---|---|---|
| Different state categories cross boundaries differently. | Official/manual/creator descriptions provide concrete examples. [C-01] | Their documentation may not describe every platform, mode or exception. |
| A typed transition makes those differences inspectable. | Reasoning from explicit states/triggers; reviewed persistence/settings guidance. [C-02, C-05] | A complete-looking matrix can omit an important event or depend on an unverified rule. |
| A targeted explanation makes relevant consequences available before commitment. | Reviewed interface/commitment guidance. [C-03] | Availability does not establish attention, comprehension or usefulness. |
| Accurate understanding supports a choice consistent with the player’s goal. | A plausible design mechanism, not a measured result. [C-03, C-07] | Players can understand a rule and dislike it, or knowingly prefer risk; preference must not be scored as misunderstanding. |
| Correct boundary handling and access persistence support usable re-entry. | Reviewed task-wide access and recovery guidance. [C-04, C-05] | Actual recovery behavior, usability, trust and experience require separate tests. |

No source establishes the full chain or a universal disclosure format. The pattern can fail even when its state table is factually correct, especially if it reveals unwanted fiction or burdens routine play. [C-03, C-08]

## Recipe

1. **Name the attempt and every consequential trigger.** Define ordinary defeat, successful completion, deliberate abandonment, suspend/resume, a mode change and technical interruption separately. Include shared-player transitions where relevant. A pause is not automatically an end; an abandoned attempt is not automatically a successful completion. [C-02, C-05]
2. **Inventory state by meaning, not storage location.** Separate active character/build, carried resources, generated environment, cross-run traces, persistent power, persistent opportunities, narrative records, discovered knowledge, challenge/mode state and access configuration. Player memory is not a field the game can guarantee to erase. Merge categories only when they actually share a policy. [C-01, C-02, C-04]
3. **Choose the transition for each category and trigger.** Record retain, reset, transform, grant or withhold, together with eligibility and exceptions. Declare what is a proposal versus verified behavior. This step chooses a local policy; the pattern does not prefer more persistence. [C-02, C-05, C-06]
4. **Check cross-state consistency.** A retained objective must not require an object that was silently reset unless that is an intended recoverable condition. Resuming the same completed event should not grant an unintended second reward. A retained map note should not falsely describe a regenerated layout. Keep these as design/verification conditions, not a proposed engine implementation. [C-02, C-05]
5. **Separate ordinary access from gameplay stakes.** Keep chosen usable interaction settings outside punitive/earned progression. For gameplay assists or challenge categories, explain the actual scope and consequences neutrally. Do not infer a player’s needs from deaths or remove accommodations after success. [C-04]
6. **Present only decision-relevant boundary information.** Before starting or ending an attempt, make material loss/retention and interruption consequences available in an accessible summary, with optional detail. Name the current mode and scope. Do not expose undiscovered room contents or plot merely to fill the state table; the designer’s verification artifact can contain information the player should not yet receive. [C-03, C-08]
7. **Provide a coherent return state.** After a transition, show what changed and what remains to do where that resolves a real re-entry problem. Avoid a long mandatory loss inventory when a brief summary suffices. Preserve the selected input/presentation route. [C-03, C-04]
8. **Test prediction before preference.** Use scenarios with both retained and reset categories and at least one contrasting trigger. Ask what will happen, then what the person wants to do. Include a case where all, some or none of a particular reward is eligible under the stated policy. Label any changed-rule variant explicitly. [C-06, C-07]
9. **Retain, simplify, revise or exit.** Keep the technique only where it addresses a demonstrated problem without unacceptable burden, wrong information or spoiler cost. When the actual rule cannot be explained accurately, simplify the rule or hold the feature for review; do not conceal uncertainty behind a reassuring message. [C-03, C-05, C-08]

### Adjustable variables

Adjust state granularity, loss amount, eligibility trigger, carried-forward opportunity, mode scope, explanation timing/detail, return summary, interruption semantics and permissible user control. Any numeric values are local design parameters needing approval and testing. No default run duration, loss percentage, reward frequency, confirmation delay or reading-time threshold is asserted. [C-02, C-06]

### Exit conditions

Stop the recipe without recommending deployment if a material state transition is unknown; an explanation contradicts actual behavior; essential configuration is lost; a required refusal/interruption action is inaccessible; shared-player effects are unresolved; or the explanation damages a deliberately chosen uncertainty without resolving a real account-consequence misunderstanding. A simpler fixed-run statement may be the correct output. [C-03–C-05, C-08]

## Worked examples

### Illustrative example A: selective successor state

A fictional expedition uses the following **proposed** rules. They are not taken from a shipped game and were not tested. [C-06]

| State | Defeat | Complete the expedition | Suspend and resume |
|---|---|---|---|
| Active tools and carried food | Reset for the next expedition. | Reset after the expedition ends. | Preserve this attempt’s exact state. |
| Research earned by finishing a named objective | Retain already completed objective credit; no credit merely for dying. | Retain completed credit. | Do not grant the same objective again. |
| Optional tool-family unlocks | Retain. | Retain. | Retain. |
| Generated route | Regenerate for a new attempt. | Regenerate for a new attempt. | Preserve the current route. |
| Discovered general rule notes | Retain; distinguish general rules from old route observations. | Retain. | Retain. |
| Chosen remaps, text preferences and other ordinary access configuration | Retain. | Retain. | Retain. |

A compact proposed entry statement says that tools and food belong to this expedition, while completed research and unlocked tool families survive it. The suspend action separately says it continues this expedition later. The player does not need to read the internal matrix, and the interface should not promise new credit for an objective already completed. [C-02, C-03, C-05, C-06]

Test a defeat immediately before an objective is completed and one immediately after: those cases distinguish retained completed credit from credit that was never earned. Next test suspend versus abandonment. Someone who correctly predicts the losses but abandons because their available time changed has understood the rule; the test must not mark the decision wrong. If readers instead infer that every death grants research, revise the eligibility explanation or rule before considering deployment. [C-06, C-07]

### Illustrative example B: a self-contained challenge

A short abstract challenge has no persistent character growth or narrative. It records a best score and ordinary settings; attempts otherwise begin from the same defined start. The full matrix would likely add little to a clear “new attempt” statement and a separate record/settings explanation. This counterexample limits the pattern: use the smallest representation of the actual boundary, not an RPG-style meta-progression screen in every game. The “likely” benefit/cost remains a hypothesis to check locally. [C-02, C-06, C-08]

### Documentary comparator, not recipe validation

NetHack’s documented bones and explore mode show that a traditional reference can have exceptions to total reset. Rogue Legacy’s creator describes persistent successors/upgrades, and Hades’ FAQ describes another selective progression model. These support inspecting distinctions, not choosing any particular row in the illustrative table or claiming the table improves player experience. [C-01]

## Tradeoffs and alternatives

A detailed boundary model creates specification, interface, localization and verification work. More categories can make the model more accurate while making an explanation less usable. Persistent narrative and unlocks can also create cross-state combinations that a simple reset avoids. A compact single-rule design may be preferable when mixed persistence is not central to the experience. [C-02, C-03, C-06]

Alternatives include a genuinely self-contained run, a stable campaign with no attempt-wide reset, an explicit mode preset, a brief end-of-attempt summary, or a player-controlled checkpoint structure. These alternatives change different experiences; none is an evidence-backed universal substitute. General commitment/refusal concerns remain with the existing reviewed safe-exit pattern. [C-05, C-08]

Interruption protection and rollback after a known bad outcome are different policies. A research specification can distinguish them without promising a particular anti-cheat, multiplayer or recovery implementation. Any actual shared-service, account or save-system changes require separate authorization and technical review. [C-05]

## Failure cases and observable warning signs

| Failure | Observable warning sign in a future test | Candidate correction |
|---|---|---|
| A single “progress” label hides unlike states. | People correctly predict one category but consistently infer the wrong rule for another. | Separate only the confused categories; avoid expanding every explanation. |
| Explanation and current mode disagree. | Returning players describe a prior mode’s consequences. | Show current scope and revalidate mode-change communication. |
| Retained knowledge becomes false after regeneration. | Notes are interpreted as current geography rather than prior observations. | Separate stable rules from run-specific observations. |
| Loss includes access configuration. | A participant cannot comfortably configure or continue after restart. | Remove ordinary access configuration from the gameplay reset policy; retest the complete task. |
| Confirmation becomes a reading/input obstacle. | Accidental acceptance, repeated skipping or inability to use the safeguard. | Reduce ceremony, provide a usable alternative, or simplify the underlying transition. |
| Disclosure destroys wanted discovery. | Participants understand account consequences but report that fictional uncertainty was unnecessarily resolved. | Disclose the real commitment boundary without exposing the hidden fiction. |

These are proposed diagnostics, not observed frequencies or performed usability results. [C-03–C-08]

## Counterexamples and do-not-use conditions

Do not use the full pattern for a simple reset already understood by the intended audience, for a purely linear save system with no mixed attempt state, or as a justification to add persistent progression. Do not use it to normalize a harmful or unwanted rule merely because the rule can be explained. Comprehension does not establish consent to every consequence, ethical acceptability, long-term trust or enjoyment. [C-03, C-08]

A fictional narrative may intentionally conceal whether an in-world event is remembered. The designer can still be clear about loss of the player’s saved progress or ability to stop without revealing the narrative answer. Where even that distinction is genuinely ambiguous, record the conflict for review rather than claiming the pattern resolves it automatically. [C-05, C-08]

## Proposed playtest and falsification

**Status: proposed / not performed.** Compare the current truthful minimal explanation with a targeted state-boundary explanation using the same rules and stakes. Do not compare an inaccurate control condition with an accurate treatment merely to make the pattern look effective. Start with scenario/mock-up testing when the question is comprehension; use a separately authorized interactive slice for timing, recovery and input questions. [C-06, C-07]

Recruit people with differing prior run-game familiarity, relevant access routes, languages and interruption needs. Keep the same information rights and ordinary accommodations available. Counterbalance scenario order where appropriate; track teaching from earlier scenarios and moderator assistance. Include defeat, completion, suspend and a material eligibility boundary, plus both retained and lost categories. A rule-change variant is separately labeled and does not count as stable-rule transfer. [C-06, C-07]

Measure accurate consequence predictions, ability to locate the relevant information, accidental irreversible actions, re-entry task completion, explanation burden and unwanted spoilers. Ask separately whether the person prefers the rule or would stop. Familiarity, reading load, prior losses, reward desirability and the clarity of the rule itself can confound the comparison. Do not use more retries or acceptance rate as a proxy for understanding. [C-03, C-06, C-07]

**Reject or simplify the pattern** when the targeted misunderstanding is not present, the richer explanation adds burden without a locally meaningful benefit, material errors persist, or it reveals prohibited information. **Reject the implementation proposal regardless of comprehension gain** when access configuration or promised interruption behavior is not preserved. Predeclare local decision criteria and sample justification before a real study; no participants, power calculation or numeric effect threshold are supplied by this draft. [C-04–C-08]

## Related entries and ownership

Apply selectively through [Roguelike](../genres/roguelike.md), [Roguelite](../genres/roguelite.md) and a run-based [Deckbuilder](../genres/deckbuilder.md). Current-turn card zones are not this pattern’s boundary; [Cycle-aware deck acquisition](cycle-aware-deck-acquisition.md) owns that narrower composition question.

Reviewed dependencies D01, D03–D05 and D07–D09 are identified with exact hashes in the [review packet](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer). Foundations ownership and duplication disposition are **proposed, not approved**. Conflict references: `G16-CON-02` persistence semantics and `G16-CON-05` disclosure versus discovery, both packet-local, not global register allocations.

## Claim ledger

Claims are local to this artifact. `observed-example` below means an inspected document/rule artifact unless a different route is explicitly given; it does not mean a game was played. Design recipes and proposed tests are not approved studio decisions.

| Claim | Precise claim / classification | Support and exact locator | Confidence and limiting question |
|---|---|---|---|
| C-01 | Mixed persistence is documented; a single “everything resets” description can be false for an actual design. **`observed-example`** | `GDR-SRC-20261010-G16-003`, `GDR-SRC-20261010-G16-005`, `GDR-SRC-20261010-F02-012`; NetHack §§6.4,11; Cellar Door successor/upgrades descriptions; Hades progression FAQ | **high for the inspected descriptions, not their efficacy**. No executable tested; a simple design can genuinely have a near-total gameplay reset. |
| C-02 | Separating state categories and transition triggers makes a persistence policy inspectable without prescribing what must persist. **`inference`** | `GDR-CAND-20261010-F02-TOP-02`, `GDR-CAND-20261010-P01-TOP-02`, `GDR-SRC-20261010-G16-003`; Reviewed D03 persistence process; D05 settings scope; NetHack selective-persistence example | **moderate: follows from the differing states/triggers**. A written matrix can still be wrong or too complex; execution and player interpretation are separate checks. |
| C-03 | Showing an accurate targeted boundary before commitment may reduce mistaken assumptions about loss or retention. **`hypothesis`** | `GDR-CAND-20261010-F07-PAT-02`, `GDR-CAND-20261010-P01-TOP-02`; Reviewed D08 complete-commitment recipe; D05 information chain | **low: complete causal benefit untested**. More text may increase burden or unwanted spoilers; no effect size or universal display rule. |
| C-04 | Access settings and ordinary accommodations should remain outside earned/punitive run progression. **`hypothesis`** | `GDR-CAND-20261010-P01-TOP-03`, `GDR-CAND-20261010-P01-TOP-02`, `GDR-CAND-20261010-F01-PAT-01`; Reviewed D04 task chain; D05 settings; D01 retained accommodations | **low for a specific design implementation, moderate rationale**. No native-game numerical accessibility requirement is created here; actual access outcomes untested. |
| C-05 | A consistency check must distinguish defeat, success, abandonment, suspend/resume and technical recovery. **`inference`** | `GDR-CAND-20261010-F02-TOP-02`, `GDR-CAND-20261010-F02-PAT-02`, `GDR-CAND-20261010-F07-PAT-02`; Reviewed D03 persistence; D07 save/load audit; D08 bounded interruption | **moderate: different triggers can have different consequences**. Not a save-system architecture or anti-cheat solution; uncertain transition behavior blocks deployment. |
| C-06 | The worked state matrices and complete pattern are proposals, not observed game behavior or performed tests. **`hypothesis`** | Author’s explicit reasoning / proposed design, not an external result; Recipe, worked examples and test design | **low: no new test or prototype occurred**. Document checks cannot establish gameplay correctness, usability, fairness or trust. |
| C-07 | Boundary-comprehension tests need both lost and retained cases, and must separate prediction from a legitimate preference to continue or stop. **`hypothesis`** | `GDR-CAND-20261010-F01-PAT-01`, `GDR-CAND-20261010-F07-TOP-01`; Reviewed D01 lines98–116 corrected transfer probes; D09 methods | **low for this proposed transfer, moderate diagnostic logic**. Rule changes must be labeled; a blanket answer or one correct probe does not establish durable transfer. |
| C-08 | The full pattern is inappropriate when its explanation overwhelms a simple loop or reveals the intended fictional uncertainty. **`inference`** | `GDR-CAND-20261010-F02-TOP-01`, `GDR-CAND-20261010-F07-PAT-02`; Reviewed D02 known/unknown distinction; D08 safe-exit scope | **moderate: plausible countermechanism**. Preserve truthful player-account consequences without automatically revealing plot or unexplored mechanics. |

## References

Access date for every record below: **2026-10-10** (task-local evidence date). A live page or historical rulebook does not certify the current game build. Source identities are temporary except the explicitly reused run-scoped F02 identity; all global allocation/deduplication remains pending.

### GDR-SRC-20261010-G16-003
**Eric S. Raymond; edited and expanded by Mike Stephenson and others / NetHack Development Team. [A Guide to the Mazes of Menace (Guidebook for NetHack)](https://www.nethack.org/v367/Guidebook.html).** NetHack. Publication/update: February 3, 2023. Edition/build: NetHack 3.6.7 guidebook; page explicitly identifies this as an older version.
**Inspected locator and access:** §3 display/dungeon introduction; §6.4 Bones levels; §11 Explore mode. `access: relevant-excerpt`. Type: Primary official versioned manual.
**Limits / provenance:** Documentary behavior only. No executable, platform port or game session tested. Not current-version certification. Independent production example; game influence/lineage does not establish independent outcome evidence. **Rights:** Manual rights retained by contributors; paraphrase; no manual illustrations redistributed

### GDR-SRC-20261010-G16-005
**Cellar Door Games. [Our Games — Rogue Legacy and Rogue Legacy 2 sections](https://www.cellardoorgames.com/).** Cellar Door Games. Publication/update: Page update unknown; product release labels June 27, 2013 and April 28, 2022. Edition/build: Public product descriptions captured on evidence-check date; actual game builds unknown.
**Inspected locator and access:** “Rogue Legacy 2” paragraph beginning with genealogical rogue-LITE; “Rogue Legacy” successor/traits paragraph. `access: relevant-excerpt`. Type: Primary creator product description.
**Limits / provenance:** Promotional descriptions verify terminology and claimed features, not universal definitions, accessibility outcomes or progression benefits. Both titles are one studio context, not two independent empirical studies. **Rights:** Copyright Cellar Door Games; paraphrase only

### GDR-SRC-20261010-F02-012
**Supergiant Games. [Hades FAQ](https://www.supergiantgames.com/blog/hades-faq/).** Supergiant Games. Publication/update: Published December 7, 2018; last updated July 16, 2025. Edition/build: FAQ for original Hades; individual platform/build unspecified.
**Inspected locator and access:** What kind of game is Hades?; difficulty/permanent progression/God Mode; story across attempts. `access: relevant-excerpt`. Type: Primary creator FAQ.
**Limits / provenance:** Documentary features and intent, not observed efficacy. No resistance percentage or tuning inferred. Exact existing source identity reused from inspected F02 challenge-and-difficulty references. Fresh direct web inspection here; no G16 alias allocated. **Rights:** Copyright Supergiant Games; paraphrase only

## Review and history

Version **0.1.0**, revision **initial-author-draft-1**. First G16 submission found in this scoped work; no predecessor artifact is asserted. Assembly edits before first delivery do not create a new conceptual ID. Exact final hashes are in the [review packet](../reviews/full-run-20261010-g16-review-packet.md#candidate-byte-receipt); the packet’s hash is in its separate integrity receipt.

Author self-review is recorded in the packet and is **not independent review**. Independent evidence/content review is pending; local document checks do not constitute host retrieval tests. No research acceptance, permanent identity, publication, implementation or release is claimed. No player study, prototype or game session was performed by G16. Recommendations are reusable proposals, not adoption decisions for any particular game.

The inspected reviewed dependency snapshot remains **draft 0.1.0 / coverage-open**. Relevant exact revisions, hashes and limitations are recorded under [reviewed dependency transfer](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer). Unavailable selected later-wave dependencies remain gaps, not implicit support. Additional pattern ideas are [queued proposals](../reviews/full-run-20261010-g16-review-packet.md#queued-child-proposals), with no child batch keys allocated or sent.
