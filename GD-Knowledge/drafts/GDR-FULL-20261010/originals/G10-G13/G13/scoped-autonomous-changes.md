---
id: GDR-CAND-20261010-G13-PAT-01
kind: pattern
title: Scoped autonomous changes
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_identity: G13-authoring-20261010-A1
predecessor_sha256: null
supersedes: null
change_summary: Initial G13 capture in this session; no predecessor G13 artifact was
  supplied or located in the bounded retrieval.
identity_scope: temporary-run-scoped-candidate
run_id: GDR-FULL-20261010
batch_id: G13
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_state: coverage-open
independent_review_state: not-yet-reviewed
aliases:
- autonomy boundaries
- background event permissions
- protected simulation changes
tags:
- autonomy
- permission-scope
- authorship
- persistence
- hypothesis
- coverage-open
related_topics:
- GDR-CAND-20261010-F01-TOP-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G13-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G13-GEN-01
- GDR-CAND-20261010-G13-GEN-02
- GDR-CAND-20261010-G13-GEN-03
source_ids:
- GDR-SRC-20261010-G13-006
- GDR-SRC-20261010-G13-007
reviewer: null
approved_by: null
approved_date: null
byte_hash_record: ../reviews/full-run-20261010-g13-integrity-receipt.md
proposed_domain_owner: BH-GDR-Foundations-and-Systems; coordination decision pending
---

# Scoped autonomous changes

**Draft 0.1.0 · GDR-CAND-20261010-G13-PAT-01 · hypothesis, coverage-open.** Let a player set understandable boundaries for selected persistent world changes without personally approving every ordinary simulated action. This is a proposed reusable design pattern, not an implementation specification or a claim that more settings improve play.

## Purpose

The intended problem is a mismatch between a world that continues to act and a player's expectation of authority over particular persistent changes. The proposed outcome is **predictable authority**, not guaranteed happiness, a fully obedient world or elimination of surprise. Separate permission for an event class from the event's feasibility, likelihood and desirability. [C-01, C-03]

## Context and prerequisites

Consider this pattern when consequential background changes can occur while a player is focused elsewhere, when their scope is distinguishable, and when those changes can be checked against a persistent policy before commitment. Examples might include relocating a household, replacing a settlement institution or altering a shared construction. These examples are illustrative; suitability is untested. [C-03]

The design needs a truthful mapping between a player's setting and the events actually governed. It also needs a declared authority owner and a policy for queued events, inherited settings, new agents, save/load, import and reset. “Allowed” cannot mean “will occur,” and “disabled now” cannot silently promise reversal of past changes. When the game cannot reliably enforce a proposed boundary, do not expose a reassuring but inaccurate control. [C-03, C-04]

**Not the same as:** a difficulty preset, direct control of an agent's every action, an undo system, legal consent or actual consent between people. A player's permission to simulate an event does not make every participant in the fiction willing. In shared play, one user's setting cannot automatically authorize changing another person's work. [C-04, C-07]

## Mechanism and evidence

The Sims Team's Neighborhood Stories article documents configurable background change at multiple scopes and a route to inspect recent events. This is a concrete design precedent, not evidence that these controls improve comprehension or reduce unwanted experiences. [C-02; GDR-SRC-20261010-G13-006]

| Proposed link | Evidence support | Limit / alternative explanation |
|---|---|---|
| Some simulated changes can be governed by a scoped policy | Source 006 describes such a policy in one product | Actual implementation and defaults were not reproduced here |
| A policy can distinguish protected from permitted changes | Logical if the implemented rule and precedence are faithful | A label can be clear while queued events bypass it |
| A player can predict the policy's effect | Hypothesis requiring contrasting-case tests | More controls may increase errors and configuration burden |
| Predictability can support the player's intended degree of authorship | Hypothesis, informed by reviewed motivation and commitment distinctions | Players seeking surprise may dislike the constraint; the chosen default may matter more |

The strongest recommendation is therefore conditional: **offer the smallest reliable scope distinction that answers an observed authorship conflict; add finer overrides only when simpler controls fail the actual decision.** No study in this batch establishes an optimal number of scopes or a causal benefit. [C-03, C-05]

## Recipe

1. **Name the protected change.** Describe the persistent consequence in player terms, its affected parties, its normal initiator and when it becomes committed. Distinguish ordinary activity from a change that meaningfully alters future possibilities. Do not begin by offering a toggle for every internal variable. [C-03]
2. **Specify authority and feasibility separately.** Write the permission predicate and the ordinary event conditions in separate conceptual records. For example, permission for a household to move does not guarantee an available destination or a desire to move. Decide which fictional wishes can still conflict with the player's policy. [C-04]
3. **Choose the minimum scope hierarchy.** Start with a coherent default and one justified exception scope. Add event categories, groups or individuals only for a demonstrated distinction. Document whether a more specific rule overrides, inherits or combines with broader rules. This is a proposed design sequence, not the exact algorithm of the source game. [C-05]
4. **Resolve lifecycle boundaries before presenting controls.** Define policy changes for pending events, events already committed, entities created later, copied saves and imported content. Show exceptions that cannot be governed. A policy change may affect future events without undoing history; say so. [C-04, C-06]
5. **Expose effective policy and a representative consequence.** Give a readable statement of what currently applies to the selected subject, including inherited exceptions. Offer a concrete contrasting case rather than only an ambiguous toggle label. Preserve access accommodations. [C-05, C-08]
6. **Provide proportionate retrospective evidence.** Where useful, allow a player to inspect a relevant committed change and the policy scope that applied. Do not invent a character's motive to explain a policy result. Avoid alerting on every ordinary action; an on-demand history can be the simpler alternative. [C-06]
7. **Validate refusal as well as permission.** Use protected, permitted-but-infeasible, and permitted-and-feasible cases. Ask what may happen before asking what the player would prefer. Test an exception, reset and pending-event transition. Retain one source identity per inspected precedent. [C-08]
8. **Exit, simplify or narrow the promise.** If enforcement is unreliable, remove the claim of protection until repaired. If participants cannot predict precedence despite adequate access, reduce scopes or use explicit scenario presets. If the system requires continual approvals that undermine the intended experience, prefer a clear default or a separate authoring mode. [C-05, C-08]

### Adjustable variables

The proposed variables are event category granularity, default policy, inheritance depth, override visibility, confirmation point, handling of queued events, retrospective history detail and single/shared authority. Change one relevant variable at a time when diagnosing confusion; changing both the model and its explanation obscures the cause. No numerical threshold or universal default is specified. [C-05, C-08]

## Worked examples

**Illustrative: an inhabited workshop settlement.** The player wants residents to choose ordinary jobs but wants to preserve the founding household's home. The prototype permits routine scheduling by default. A separate relocation policy governs future household moves, and the founding household has an explicit exception. A new household inherits the group policy, not the founder's exception. This is an invented prototype, not a description of any shipped title. [C-03–C-06]

A request to relocate the founder arrives before a policy change. The proposed rule checks permission at commitment; the pending request remains visible but cannot commit after relocation becomes protected. The interface identifies the effective exception and does not describe the founder as content or unhappy merely because a rule blocked the change. If ordinary relocation also requires an empty dwelling, permission alone does not create one. A worked contrasting case permits another household to relocate but leaves it unable to do so until a destination exists. [C-04, C-06]

A simpler alternative is to make all homes fixed during a scenario. If this meets the intended authorship promise, per-household controls add no justified value. A contrary scenario intentionally asks the player to adapt to migration they cannot prevent; there, advance explanation of the scenario's authority boundary may be preferable to the pattern. [C-05, C-09]

**Illustrative adaptation to a living sandbox.** A collaborative garden might let autonomous maintenance replace dead plants only within explicitly assigned plots. The proposed boundary is plot ownership and maintenance permission, not each player's identity or social status. If the authority model cannot exclude another person's work, this pattern must not promise safe unattended editing. No shared-game permission system was tested in G13. [C-07]

## Tradeoffs and alternatives

Fine-grained policy permits exceptions but creates configuration, persistence, localization and debugging obligations. A single preset, fixed scenario rules, explicit opt-in project automation or a pause-before-commit review can be better. A reversible experiment branch answers a different question—what a player can try without committing to the original state—and is not a substitute for a policy that must operate continuously. [C-05, C-06, C-09]

A larger menu can produce the appearance of control while the effective policy remains opaque. Conversely, withholding controls may be a deliberate part of the experience, provided that the constraint is represented honestly rather than as a broken promise. Neither alternative establishes player wellbeing or ethical acceptability merely through interface design. [C-07, C-09]

## Failure cases

| Failure | Observable warning sign in a proposed evaluation | Candidate correction |
|---|---|---|
| Override precedence is misunderstood | Participants predict the group rule for an overridden subject | Flatten the hierarchy or show the effective rule beside the subject |
| Permission is mistaken for a command | Players expect an allowed event despite missing prerequisites | Separate “may happen” from feasibility and selection |
| The policy is stale or bypassed | A newly protected change still commits from a queue | Recheck at the declared boundary or disclose a narrower commitment rule |
| Protection becomes total micromanagement | Ordinary play requires repeated event approvals | Reduce event granularity or choose a stable preset |
| History manufactures motive | A policy denial is narrated as a character's preference | Record the actual known cause and retain uncertainty |
| Shared authority is false | A user's policy changes another person's protected state | Stop deployment of that scope; redesign authority before evaluating benefits |

These are proposed failure diagnostics, not measured incidents. [C-04–C-08]

## Counterexamples and do not use conditions

Do not require this pattern in a static composition toy, a tightly authored scenario with no relevant autonomous changes, or a design whose central challenge depends on explicitly uncontrollable developments. Avoid treating every surprise as a defect. A simpler rule that players understand can be superior to a comprehensive policy editor. [C-09]

**Identity boundary:** controls over simulated events must not be equated with controls to erase categories of people. The inspected historical Sims orientation article distinguishes identity parameters from turning the feature off. This supports examining the difference, not copying that article's acknowledged binary architecture or claiming its design is universally inclusive. [C-07; GDR-SRC-20261010-G13-007]

## Playtest

**Proposed, NOT PERFORMED.** Compare a fixed understandable policy, a coarse configurable policy and a scoped exception version only where each is a credible solution to the same intended problem. Keep event possibilities, ordinary feasibility, source text quality and access aids comparable. Recruit participants with relevant control preferences, not assumed genre demographics; justify the sample and local decision bounds before testing. [C-08]

Ask participants to predict protected, allowed-but-infeasible and allowed-feasible outcomes, then choose the policy they prefer. Present an inherited case and an explicit exception under the same rule. Do not change the rule unnoticed and call failure “poor transfer.” Separately test an announced rule change and whether participants recognize the new contract. Evaluate prediction accuracy, unwanted committed changes, configuration effort, reversals and reported authorship fit. These are distinct measures, not a single satisfaction score. [C-08]

Reject the protection claim on any reproducible violation of its declared boundary. Reject added granularity when it does not improve the relevant distinction over the simpler condition or creates locally unacceptable burden. A predictable result that players dislike is evidence about preference or the rule, not necessarily a comprehension failure. No participant outcomes, effect sizes or safety guarantees exist yet. [C-08]

## Related entries, ownership and unresolved questions

Genre adaptations: [colony simulation](../genres/colony-simulation.md), [life simulation](../genres/life-simulation.md) and [sandbox](../genres/sandbox.md). Complement: [reversible experiment branch](reversible-experiment-branch.md). The inspected `GDR-CAND-20261010-F07-PAT-02` addresses commitment and safe exit; this candidate's proposed distinction is ongoing event authority with inheritance and lifecycle rules. Possible overlap still requires Library Coordination and Foundations ownership review; it is not a newly approved concept home. [C-10]

Reviewed dependencies and hashes are in the [packet manifest](../reviews/full-run-20261010-g13-review-packet.md#reviewed-dependency-manifest). Open issues include the cost of authority granularity, shared-world governance, truthful event histories, cross-locale comprehension and the boundary between authorship and character autonomy. See local issues G13-CON-02, G13-CON-03 and G13-CON-06 in the packet. The proposal remains coverage-open.

## Claim ledger

Confidence applies to the stated claim, not to the genre as a whole. Documentation observations are observations of published artifacts, not direct game observations. Recommendations not approved by Doug are `inference` or `hypothesis`, not `studio-decision`.

| Claim | Precise statement and classification | Support / locator | Confidence and reason | Limits / next discriminator |
|---|---|---|---|---|
| C-01 | **`inference`** — Predictable authority over selected autonomous changes is distinct from total control, event feasibility and guaranteed player benefit. | G13 domain decision questions; reviewed F01-TOP-01 and F07-PAT-02; original distinction. | Moderate: conceptual separation is useful, not a validated intervention. | The relevant authorship conflict must be demonstrated in the target context. |
| C-02 | **`observed-example`** — The Neighborhood Stories article documents policy granularity and access to background-event history. | GDR-SRC-20261010-G13-006, “Configuring Neighborhood Stories” and “What Are Neighbor Sims Up To?”. | High for the inspected article. | No runtime reproduction, current-default audit or outcome measurement. |
| C-03 | **`hypothesis`** — A small reliable scope distinction may support an intended authorship boundary while ordinary activity continues. | C-01/C-02; original mechanism and workshop example. | Low: the proposed pattern has not been evaluated. | Surprise and uncontrollable developments may be intended; settings can increase burden. |
| C-04 | **`inference`** — Permission, feasibility, event selection and commitment timing require distinct meanings for a truthful control. | C-02 as precedent; original logical boundary analysis. | Moderate: follows from the proposed contract, not source-game algorithm verification. | Lifecycle implementation remains unspecified and untested; past changes are not automatically undone. |
| C-05 | **`hypothesis`** — Start with the smallest useful policy hierarchy and validate effective-rule prediction before adding granularity. | Reviewed P01-TOP-02 information distinctions; C-02; original recipe and alternative. | Low: benefit of this sequence and hierarchy size is unmeasured. | A fixed scenario or coarse preset can outperform detailed controls. |
| C-06 | **`inference`** — Persistent policies need declared save/queue/reset behavior and truthful historical explanations. | C-02; original lifecycle analysis and worked example. | Moderate for requirements implied by the protection promise. | No empirical estimate of cost; history must not fabricate motives or causation. |
| C-07 | **`inference`** — Event authority is not legal consent, real interpersonal consent, identity erasure or unilateral shared-world ownership. | GDR-SRC-20261010-G13-007, “Can I turn this feature off?”/architectural limitations; reviewed F07-PAT-02 context; original ethics boundary. | Moderate for the distinctions, not universal inclusion or legal guidance. | No current representation audit, legal standard or multiplayer validation. |
| C-08 | **`hypothesis`** — Evaluation must separate rule prediction, preferred action, enforcement fidelity and authorship fit. | Corrected F01-PAT-01 worked examples/§Playtest; F07-TOP-01 §Playtest; original proposed protocol. | Moderate for discrimination logic; actual protocol unvalidated. | No tests performed; sample and local benefit/burden criteria require prior justification. |
| C-09 | **`inference`** — Do not add scope controls where a simpler rule meets the promise or uncontrollability is central. | Original negative cases; C-03/C-05 causal alternatives. | Moderate for conditional exclusion, not tested preference prevalence. | Do not treat all surprise or unwanted fiction as a defect. |
| C-10 | **`hypothesis`** — The candidate may be distinct from commitment/safe-exit guidance through ongoing authority and lifecycle semantics. | Inspected F07-PAT-02 §Context/§Counterexamples; original novelty proposal. | Low: latest canonical/pending pattern registry is unavailable. | Library Coordination must check overlap and assign the eventual owner; no permanent ID. |

## References

Access date for every record: **2026-10-10 America/Los_Angeles / 2026-10-11 UTC**. Rights: copyrighted source text remains with its owner; only brief paraphrases and bibliographic metadata are included. No screenshots, videos or source-page copies are redistributed. Source IDs are temporary G13 identities; canonical URL/edition deduplication remains pending.

### GDR-SRC-20261010-G13-006

**Nate / The Sims Team, Electronic Arts. Neighborhood Stories System.** Publication/update: 2022-03-15 (displayed); subsequent edits unknown. Publisher: the organization named above (Steam hosts source 005). [Source](https://www.ea.com/games/the-sims/the-sims-4/news/neighborhood-stories-system).

**Edition/build:** Dated Sims 4 feature article as retrieved in 2026; no launch-build or current-build reproduction. **Access:** `relevant-excerpt`. **Inspection route:** Public primary HTML text inspected through web retrieval. **Type:** Creator design account and feature documentation.

**Exact locator:** “Configuring Neighborhood Stories”: group defaults, household-specific settings, global setting and per-save persistence; “What Are Neighbor Sims Up To?”; retrieved text lines 40–73. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Supports documented policy granularity and history access, not reduced distress, better storytelling or accurate current defaults. Displayed publication date is not proof that every retrieved sentence is unchanged since 2022. **Independence/provenance:** Same franchise/organization as sources 007, 015 and 016; multiple pages are not independent population evidence.

### GDR-SRC-20261010-G13-007

**SimGuruJessica, design lead, Electronic Arts / Maxis. Sexual Orientation in The Sims 4.** Publication/update: 2022-07-15. Publisher: the organization named above (Steam hosts source 005). [Source](https://www.ea.com/games/the-sims/the-sims-4/news/sexual-orientation-in-the-sims-4).

**Edition/build:** Historical feature version described as 1.0; no game build observed. **Access:** `relevant-excerpt`. **Inspection route:** Public primary HTML text inspected through web retrieval. **Type:** Firsthand design and implementation-limitation account.

**Exact locator:** “How It Works”; “Why are there only two gender options?”; “Can I turn this feature off?”; retrieved text lines 23–87. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Describes separate attraction parameters and acknowledges binary architectural limitations at that time. Does not validate inclusive outcomes or establish the state of the latest build. **Independence/provenance:** Same Sims production family as 006/016; reported consultation with GLAAD and It Gets Better is creator-reported, not independently inspected consultation evidence.


## Review and history

2026-10-10, `initial-capture-1`: initial complete author draft for G13. Version remains `0.1.0`; predecessor/supersession are null, not a claim that a canonical registry was searched exhaustively. Author self-review is in the [G13 packet](../reviews/full-run-20261010-g13-review-packet.md#author-self-review). Independent review has not occurred for this candidate. No participant tests, executable game observations, implementation, release or adoption occurred.

Exact bytes are recorded outside this file in the [integrity receipt](../reviews/full-run-20261010-g13-integrity-receipt.md). Existing upstream IDs, revisions and source meanings remain unchanged. This draft adds no permanent IDs and does not supersede a reviewed dependency.
