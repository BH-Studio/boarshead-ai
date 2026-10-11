---
id: GDR-CAND-20261010-G06-PAT-01
kind: pattern
title: Dependency-complete loadout switch
version: 0.1.0
status: draft
candidate_revision: initial-research-1
attempt_id: G06-attempt-1
run_id: GDR-FULL-20261010
batch_id: G06
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- saved-build dependency check
- invalid loadout recovery
- configuration bundle validation
tags:
- configuration
- prerequisites
- loadout
- reversibility
- accessibility
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G06-GEN-01
- GDR-CAND-20261010-G06-GEN-02
- GDR-CAND-20261010-G06-GEN-03
source_ids:
- GDR-SRC-20261010-G06-007
- GDR-SRC-20261010-G06-008
- GDR-SRC-20261010-G06-011
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
coverage_status: open
predecessor_sha256: null
supersedes: null
change_summary: Initial G06 submission; inspected dependency selections preserved;
  no prior batch reissued.
hash_record: ../reviews/full-run-20261010-g06-integrity.md
---

# Dependency-complete loadout switch

> **Draft research candidate, not released guidance.** Research authorization does not approve this definition, any causal claim, a game implementation or publication.

## Purpose

**Dependency-complete loadout switch** is a proposed technique for changing a saved configuration whose parts enable one another. It aims to prevent a player from selecting a familiar preset and unknowingly losing a required item, action, trigger or party contribution. Its immediate design output is a comprehensible switch contract and an explicit invalid-state disposition—not a promise of improved enjoyment or an engine implementation. [C-01]

Use the pattern beyond a particular RPG only when the same problem exists: a collection of capabilities is restored together and some parts may no longer be valid. A strategy unit group or configurable tool set could have this structure, but those are illustrative transfers requiring their own evidence and ownership review. Independent cosmetic toggles usually do not justify the recipe. [C-08]

## Context and prerequisites

The game already permits some configuration changes, and a design owner can state when and at what cost. The affected parts, their enabling conditions, and what persists after changing must be inspectable. The team must know whether the operation changes only equipment, also skills/trigger bindings, or something else; an unknown scope cannot support a truthful preview. [C-05; C-06]

The relevant information must be available through the intended control and access routes. In shared play, distinguish the player's own assets from borrowed equipment and roles requiring another person's agreement. The game need not reveal hidden opponents or puzzle answers merely to describe the selected configuration's known state. This pattern does not authorize changing the game's commitment policy, narrative history, purchased entitlements or another participant's decisions. [C-05; C-07]

**Do not begin this recipe as a universal upgrade.** First compare it with a direct independent change, clear manual editing, a single stable build, or no switching at all. The pattern is justified only by a real dependency/communication problem and a supported player promise. Global duplication and domain ownership remain pending Library Coordination; Foundations and Presentation own the shared mechanism/interface concerns. [C-08]

## Mechanism and evidence

| Proposed causal link | Inspected support or reasoning | What is not established |
|---|---|---|
| Configurations contain dependencies that can invalidate a saved plan | Grim Dawn's documented prerequisite/binding rules provide a concrete example. [C-03] | Not every game's configuration has those rules; no G06 client execution occurred. |
| A saved-plan preview can distinguish available from missing parts | Diablo IV's Armory account documents bundled capture and missing-item indication. [C-02] | The account does not validate the full proposed recipe or define every fallback. |
| Warnings need to survive dependency changes and the chosen access route | The 2.1.3 patch report identifies missing loadout and screen-reader dependency warnings. [C-04] | No incidence rate, reproduced defect or proof of complete repair; the two documents are not independent trials. |
| A dependency-complete explanation lets a player predict affected capabilities | Inference from known prerequisite relations plus inspected P02 fact/action distinctions. [C-05; C-07] | Perception, understanding and usable timing require actual user evaluation. |
| Explicit valid-state/fallback policy avoids an unintended configuration commitment | Logical requirement for honoring the declared switch promise. [C-06] | No universal all-or-nothing operation, confirmation dialog or software transaction is mandated. |
| Better prediction and recovery improve the chosen experience | The intended benefit of the assembled pattern. [C-01; C-09] | **Low-confidence hypothesis**, not demonstrated agency, accessibility, mastery or enjoyment. |

The recipe may increase reading and interaction cost without helping an experienced user, or protect a preset the player no longer wants. Keep that opposing explanation in the comparison. Treat documented implementation and negative reports as reasons to test, not proof that more preview is always better. [C-08; C-09]

## Recipe

1. **Define the permitted change.** Record the selectable bundle, the point at which changes take effect, the current cost, who may authorize it, and which state remains outside the operation. Distinguish capability selection from restoring spent resources, restarting cooldowns, duplicating items or rewriting history. Exit if the actual scope cannot be stated truthfully. [C-05]

2. **Trace the affected dependency set.** Identify prerequisites among items, skills, resource capacity, trigger bindings and any shared ownership/role condition. Include effects of removing an old enabling part, not only requirements for adding the new part. Use a bounded dependency record suitable to the game's size; do not infer that every system needs a graph engine. [C-03; C-05]

3. **Evaluate the saved plan against the current state.** Mark what is present, missing, ineligible, externally owned or changed by the ruleset. Distinguish a saved preference from an active usable configuration. Recheck where relevant state can change while the player is inspecting it; the exact concurrency mechanism belongs to implementation review. [C-02; C-05]

4. **Explain the decision-critical difference.** Show which intended action or contribution is affected and why. A missing item name alone may not tell the player that their recovery action will be disabled. Offer enough detail to inspect the dependency without forcing a full build encyclopedia into every ordinary switch. Preserve the same known facts through supported access routes and localized terminology. [C-07]

5. **Choose an explicit invalid-plan disposition.** Possible policies include no change while explaining the repair; returning to manual editing; or an explicitly previewed partial configuration that the player elects to use. A partial loadout is not automatically wrong, but silently applying one after promising the complete preset is misleading. Keep a prior configuration only when it is still valid; otherwise expose the repair state rather than calling it restored. [C-06]

6. **Make the commitment legible and proportionate.** Ask for confirmation only where the cost or irreversible consequence warrants it. A frequent reversible switch may need less ceremony. Keep cancellation usable; do not let a confirmation mechanism hide a real policy problem. Preserve permitted preparations and genuine expedition/party constraints rather than promising unrestricted switching. [C-05; C-08]

7. **Communicate the actual post-change state.** Identify relevant changed actions and bindings, including a replacement or disabled command. Do not play a learned success cue for a rejected switch. Keep ordinary state feedback and accommodations; this is not an occasion to fade required access support. [C-06; C-07]

8. **Offer bounded repair or testing, where appropriate.** A player may inspect the new configuration, correct the missing part or use an authorized trial. Do not claim that a target dummy validates all encounter contexts. If switching is not allowed here, show the true restriction and the legitimate next opportunity rather than inventing access. [C-05; C-08]

9. **Review changed dependencies.** Reopen the relevant design and retrieval record after rule changes that invalidate saved plans. Preserve the identity of the saved preference separately from claims that it still works. A migration explanation and an honest manual-repair route may be better than silently selecting a different role. No migration or runtime code is produced by this recipe. [C-05; C-06]

### Adjustable variables

Adjust bundle scope, preview detail, switch location/timing, respec cost, confirmation friction, partial-application policy, treatment of borrowed parts, supported narration/detail routes and availability of a trial. These are local choices to justify; there is no universal loadout count, refund price, grace period, latency target or warning length. A source's count or limit is evidence about that source, not a G06 parameter. [C-05; C-08]

### Exit conditions

Exit the pattern and choose a simpler change, manual repair or no switch when dependencies cannot be determined; a required fact cannot be communicated through an intended access route; authority over a shared part is unresolved; the promised preservation/fallback cannot be honored; the operation's actual cost is unknown; or the switch conflicts with the game's deliberately selected commitment. Do not hide such a failure behind a successful-save message. [C-06–C-08]

## Worked examples

### Illustrative example: saved support configuration with a missing enabler

A fictional character has a **Support** plan: a focus item enables *Mend*, and a passive requires *Mend* as its valid trigger. A **Scout** plan uses a movement skill and does not need that focus. The focus was later lent to a teammate. These rules and names are invented; they are not claimed Diablo or Grim Dawn behavior. [C-05; C-06]

Under the recipe, selecting Support evaluates current ownership and the dependent action chain. A proposed summary states that the focus is unavailable, so *Mend* and its attached passive cannot operate. The player can cancel, retrieve the item through the game's legitimate sharing process, or enter an explicit manual repair. The operation must not quietly borrow the teammate's asset or label the incomplete state Support-ready. [C-05–C-07]

Suppose the chosen policy permits partial configurations. The preview can offer a version without *Mend* only when its limitations are explicit and the player elects it. That is not the same commitment as restoring the original complete plan. Suppose instead the previous configuration has also become invalid because the current world forbids its movement action: “keep the old build” is no longer a truthful universal fallback. Expose the actual repair choice. [C-06]

A proposed narration route announces the affected action and reason, with detail available on request. It does not merely recite an icon's color or assert that a teammate has agreed. After a valid switch, action feedback reflects the actual configured commands. This is a player-visible contract, not a runtime API or interface layout. [C-07]

### Illustrative adaptation: expedition preparation

A crawler lets the party select equipment at camp but not after crossing a declared one-way boundary. A saved plan depends on a supply held in camp storage. The preparation preview may help the party notice the missing supply; it does not authorize materializing it inside the dungeon or restoring a spent expedition resource. Where the boundary is the intended commitment, show the next legitimate opportunity instead of applying a generic free-reset policy. [C-05; C-08]

### Negative example: independent cosmetic selections

A palette and emblem have no enabling dependencies and can be changed harmlessly at any time under the imagined rules. A bundled prerequisite preview provides no useful decision distinction. Prefer direct change with ordinary feedback. This counterexample is deliberately simple: the existence of a reusable pattern does not justify adding the problem it is meant to solve. [C-08]

## Tradeoffs and alternatives

Dependency tracing and preview can add authoring, maintenance, localization and inspection burden. A compact summary can omit an important transitive effect; exhaustive detail can hide the reason the player needs. A useful candidate therefore pairs a decision-critical explanation with optional detail, but its superiority must be tested rather than assumed. [C-07; C-09]

Alternatives include manual editing with clear eligibility feedback, removing unnecessary dependencies, independent selections, a fixed role with adjustable access controls, or a consciously selected lasting commitment. Removing a dependency can be better than explaining it repeatedly when the dependency creates no desired decision. A saved plan that is invalid often may also indicate unstable rules or an inappropriate save promise rather than a need for more warnings. [C-08]

Switch timing changes the activity. Instant restoration can become compulsory encounter-by-encounter preparation; restricted restoration can preserve planning or impose unwanted repetition. This pattern does not choose between those policies. It requires that the chosen scope and consequences be knowable and that invalid-state behavior match the promise. [C-05; C-08]

## Failure cases

| Failure / observable warning sign in a future test | Candidate cause | Revision or exit |
|---|---|---|
| Player recognizes the missing item but expects the dependent action to work | Preview omits the capability relation | Explain the affected action; compare against simpler dependency design |
| A saved label appears active after only some components apply | Saved/active/usable states are conflated | Expose explicit partial policy or reject the change with repair |
| Narration omits the dependency-breaking warning | Required fact is tied to one presentation route | Correct the route and retest with relevant users; do not call icon presence sufficient |
| Cancellation restores a configuration no longer valid | Fallback assumes stale state | Report the real repair state; abandon unconditional restoration claims |
| Frequent switching resets spent resources unintentionally | Bundle scope includes unintended world/resource state | Redefine the contract and refer implementation testing to its owner |
| Party contribution disappears without shared awareness | Authority and coordination consequences were omitted | Require the appropriate local consent/notification policy or defer the operation |
| Users spend more effort dismissing previews than making useful decisions | Dependency burden or presentation is disproportionate | Simplify, offer appropriate detail control, or omit the pattern |

These are proposed diagnostic cases. Source 008 documents specific warning defects in its own product; the other rows are reasoned possibilities, not observed incidents in named games. [C-04–C-09]

## Counterexamples and do not use conditions

Do not require bundled validation for every stance change, independent cosmetic choice or fixed-character scenario. Do not present a loadout switch as a way to revoke completed moral decisions or another person's consent. Do not promise that the pattern makes any build viable, removes legitimate encounter counterplay, or guarantees the user's preferred outcome. [C-08]

A deliberate commitment game may be better without presets. An expert may prefer direct manual editing. A simplified configuration model may remove the invalid-state problem more cleanly. In each case the intended benefit of this recipe can vanish even though its individual steps are logically coherent. Preserve these alternatives at independent review. [C-08; C-09]

## Playtest

**Proposed, not performed.** Compare the proposed dependency-complete preview with an equally usable direct/manual summary on the same represented rules. Include valid plans, a missing enabler, an invalid dependent trigger, an explicitly allowed partial plan, a cancellation case and a stale previous configuration. Select cases that change the correct prediction, not a series where “reject” is always right. This adapts the inspected F01 transfer-check correction. [C-09]

Recruit only after separate approval. Include relevant configuration familiarity, input/access routes and languages; do not expose a participant to an inaccessible baseline just to create paired data. Record task/version, permitted policy, prior knowledge, help, inspection time and changes during the task. Counterbalance case order where feasible and separate learning carryover from interface effects. [C-07; C-09]

Ask the player to predict which actions will remain usable and what will be spent or preserved before committing. Then observe the choice, unintended state changes, repair behavior, perceived control and burden. Preference for a partial build is not automatically a wrong answer. A paper test can assess a represented dependency but cannot establish real-time operation, narration timing or teammate coordination. [C-05; C-09]

**Decision rules to establish before testing:** a material missing warning on a supported route or a fallback contradicting its declared policy requires correction before the affected claim can advance; an apparent benefit explained only by extra information or exposure does not validate the bundle mechanism. Predefine what counts as a worthwhile prediction/repair improvement and an unacceptable added burden for the local question. Reject or simplify the pattern if the simpler comparator performs as well for the intended decision or if preview creates persistent false expectations. No sample-size guarantee, numerical success threshold or effect result is supplied. [C-09]

## Related entries and ownership

Applicable G06 adaptations: [Role-playing](../genres/role-playing.md), [Action RPG](../genres/action-rpg.md), [Dungeon crawler](../genres/dungeon-crawler.md). The parent genre decides the chosen scope of role change; the ARPG entry isolates action/build interaction; the crawler entry addresses preparation and expedition constraints. No genre automatically overrides the others. [C-08]

Inspected related shared drafts: F02 Decision design (`GDR-CAND-20261010-F02-TOP-01`), P02 Controls/Feedback/Multimodal (`GDR-CAND-20261010-P02-TOP-01`, `GDR-CAND-20261010-P02-TOP-02`, `GDR-CAND-20261010-P02-TOP-03`), F07 Evaluation/Ethics (`GDR-CAND-20261010-F07-TOP-01`, `GDR-CAND-20261010-F07-TOP-02`), and the corrected F01 transfer pattern (`GDR-CAND-20261010-F01-PAT-01`). Their exact identities are expanded in the [packet](../reviews/full-run-20261010-g06-review-packet.md#reviewed-dependency-bytes). The new mechanism is dependency-aware bundle restoration, not a renamed general safe-exit, balance diagnosis or remapping template. Nevertheless, central duplicate/ownership clearance is pending. F03 economies/progression and F04/F05 system implications remain unresolved body dependencies. [C-05; C-08]

## Claim ledger

Every classification applies to the exact scoped statement below. Application proposals remain hypotheses or inferences even where their documented ingredients are well supported. No formal standard or new empirical-effect finding is asserted in this entry.

### C-01

**Statement:** Dependency-complete switching may reduce unintended loss of usable capabilities when restoring interdependent saved configurations.

**Class:** `hypothesis`. **Support/locator:** `GDR-SRC-20261010-G06-007`, `GDR-SRC-20261010-G06-008`, `GDR-SRC-20261010-G06-011`; Mechanism table separates documented ingredients from the untested assembled benefit.

**Confidence:** Low: no inspected experiment validates this recipe. **Limit / next discriminating question:** Does a simpler direct summary or reduced dependency model achieve the same goal with less burden?

### C-02

**Statement:** The Armory announcement documents bundled saved configurations and a missing-item indicator.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-007`; The Armory, retrieved lines 463–467.

**Confidence:** High for the official description; no hands-on behavior verification. **Limit / next discriminating question:** The document does not specify every fallback or prove users interpret the indicator.

### C-03

**Statement:** The Devotion guide documents dependencies among affinity, allocations and compatible trigger bindings.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-011`; Affinity, Celestial Powers and Resetting Devotion Points.

**Confidence:** High for the narrow documented rules. **Limit / next discriminating question:** Not a claim that all configurations require the same dependency model.

### C-04

**Statement:** The 2.1.3 patch report describes absent Armory and screen-reader dependency warnings as defects addressed by that update.

**Class:** `observed-example`. **Support/locator:** `GDR-SRC-20261010-G06-008`; Build #62672, 2025-03-04, specified Bug Fixes/Accessibility sections.

**Confidence:** High for the reported fix; no incidence or complete repair established. **Limit / next discriminating question:** Do not infer that the proposed G06 recipe was used or validated.

### C-05

**Statement:** A switch contract should distinguish the saved preference, current eligibility, affected capabilities, authority, timing and preserved state.

**Class:** `inference`. **Support/locator:** `GDR-SRC-20261010-G06-007`, `GDR-SRC-20261010-G06-011`; Logical consequence of the documented dependency/saved-plan distinction; inspected F02/P02 shared guidance supplies qualified commitment/action semantics.

**Confidence:** Moderate as a useful design decomposition; no experiential effect established. **Limit / next discriminating question:** Which dependencies are actually necessary, and can the supported operation be stated more simply?

### C-06

**Statement:** Invalid-plan behavior must match the declared promise; explicit partial application can be valid, and an invalid prior state is not a safe universal fallback.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Conditional state reasoning; worked examples are illustrative. This is a player-visible policy, not a mandatory transaction architecture.

**Confidence:** High for the logical promise/state distinction; low for the best fallback policy. **Limit / next discriminating question:** Does the player understand the actual usable configuration and legitimate repair choices?

### C-07

**Statement:** Decision-critical dependency information should remain usable through the intended access/language route without falsely resolving hidden world information.

**Class:** `hypothesis`. **Support/locator:** `GDR-SRC-20261010-G06-008`; Narrow reported warning failure plus inspected P02 multimodal/feedback and P01 scope distinctions.

**Confidence:** Low for cross-population efficacy; no access test performed. **Limit / next discriminating question:** Can relevant users predict affected actions and state without excessive explanation or missing warnings?

### C-08

**Statement:** The pattern should be omitted or narrowed when dependencies are absent, the change is not permitted, or a simpler/stable-role design better serves the chosen commitment.

**Class:** `inference`. **Support/locator:** No direct public causal evidence; Explicit counterexamples and scope reasoning; F07 safe-exit is a related but broader inspected draft, not a validated substitute.

**Confidence:** Moderate for applicability framing; local preference remains unresolved. **Limit / next discriminating question:** Does the pattern solve a demonstrated dependency problem or manufacture extra work?

### C-09

**Statement:** Changed-case prediction, repair and burden comparisons can challenge the pattern, but the proposed tests have not been performed.

**Class:** `hypothesis`. **Support/locator:** No direct public causal evidence; Adaptation of inspected corrected F01 transfer pattern and F07 evaluation/diagnosis; proposed measures and comparisons are not accepted results.

**Confidence:** Low for test sufficiency before independent methods review. **Limit / next discriminating question:** A material policy/access mismatch or no worthwhile advantage over the simpler comparator requires revision, narrowing or rejection.

## References



Source identities are temporary G06 identities. Access was checked on 2026-10-10; unnumbered web pages are not authenticated retail builds. An observed example below means an inspected source artifact, not a played game. Canonical URL/edition deduplication remains pending.



### GDR-SRC-20261010-G06-007

**Blizzard Entertainment.** *Master the Occult in Season of Witchcraft*. Publication/update: unknown publication day; Season of Witchcraft / 2.1 launch context, January 2025.

[Inspected source route](https://news.blizzard.com/en-us/article/24167111/master-the-occult-in-season-of-witchcraft). Edition/build: Historical 2.1 feature announcement; no current-client behavior verified. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary feature announcement.

**Locator:** Eternal Updates: The Armory, and More → The Armory (retrieved lines 460–467). **Claims:** C-01, C-02, C-05.

**Limits:** Bundle capture, missing-item indication and the stated no-Gold Paragon-loadout switch are documented. Does not promise all respec operations everywhere are free, or supply usability outcomes. **Independence:** Same studio/game as 006, 008 and 009; feature account and bug notes answer different questions. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-008

**Blizzard Entertainment.** *Diablo IV Patch Notes (2.1)*. Publication/update: 2025-03-04 for the inspected 2.1.3 section.

[Inspected source route](https://news.blizzard.com/en-us/article/24171214/diablo-iv-patch-notes-2-1). Edition/build: 2.1.3 Build #62672, All Platforms; surrounding compilation contains other versions. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary developer defect/fix report.

**Locator:** Vessel of Hatred → Bug Fixes: absent warning for an Armory loadout with more than two Runewords; Base Game → Bug Fixes → Accessibility: screen-reader warning when refunding a connecting Paragon node (retrieved lines 45–63, 154–159). **Claims:** C-01, C-04, C-07.

**Limits:** Reported defects/fixes were not reproduced; no incidence rate, user sample or proof of complete repair is supplied. **Independence:** Same underlying product as 007/009. Negative implementation evidence, not an independent efficacy test. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



### GDR-SRC-20261010-G06-011

**Crate Entertainment.** *Guide — Character — Devotion*. Publication/update: unknown.

[Inspected source route](https://www.grimdawn.com/guide/character/devotion/). Edition/build: Mutable official Grim Dawn guide; exact game build not supplied. Access date: 2026-10-10. Access: `relevant-excerpt`. Type: Primary game-system documentation.

**Locator:** Unlocking Constellations; Affinity; Celestial Powers; Resetting Devotion Points (retrieved lines 154–205). **Claims:** C-01, C-03, C-05.

**Limits:** Prerequisites, valid trigger bindings and refund dependencies are documented. Numerical caps and current expansion parity are not imported. **Independence:** Same documentation family as 010; not two independent player datasets. **Rights:** Copyrighted source; attributed paraphrase only; no images, full rules or source payload redistributed.



## Unresolved contradictions and tradeoffs

Packet-local records `G06-CON-02`, `G06-CON-03` remain open in the [contradiction register](../reviews/full-run-20261010-g06-review-packet.md#contradictions-and-competing-explanations). They are not globally allocated CON IDs. A tradeoff is not called an empirical contradiction when the goals, date or system differ.

## Review and history

Version 0.1.0, candidate revision `initial-research-1`, attempt `G06-attempt-1`, first submission. No predecessor or supersession is asserted. Author self-review is recorded in the [G06 review packet](../reviews/full-run-20261010-g06-review-packet.md); it is not independent review. Byte identity is in the detached [integrity receipt](../reviews/full-run-20261010-g06-integrity.md). Coverage remains open. Gate C independent review, Gate D host retrieval and Gate E acceptance/release remain uncompleted. No prototype, participant recruitment or playtest was performed.
