---
id: GDR-CAND-20261010-F06-PAT-01
kind: pattern
title: Scoped shared-state permissions
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_id: F06
attempt_id: F06-authoring-01
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC inspection/assembly date; run and authorization date remain 2026-10-10
aliases:
- bounded collaboration powers
- shared asset permissions
- revocable task authority
tags:
- shared-state
- cooperation
- trust
- griefing-resistance
- ownership
- recovery
related_topics:
- GDR-CAND-20261010-F06-TOP-01
- GDR-CAND-20261010-F06-TOP-02
related_patterns:
- GDR-CAND-20261010-F07-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-F06-005
- GDR-SRC-20261010-F06-006
- GDR-SRC-20261010-F06-001
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: First F06 submission; conditional research synthesis, no release or
  tested outcome benefit.
hash_record: ../reviews/full-run-20261010-f06-integrity-receipt.md
---

# Scoped shared-state permissions

**Conditional pattern candidate, not released or implementation-ready.** The complete technique has not been evaluated in an F06 game or participant study. It is a proposed way to specify who may affect shared state without making routine participation equivalent to unrestricted administrative power.

## Purpose

Permit the contribution a person is invited to make while making consequential powers, their scope and their withdrawal understandable. Intended outcomes are less reachable out-of-contract damage and workable collaboration. Those are different goals: preventing an action may be straightforward under an enforced rule, while improving trust or reducing overall griefing is an untested outcome hypothesis. [C-02–C-04]

This pattern is not a moderation service, an identity-proofing scheme or a promise to prevent every abuse. A participant can misuse communication, timing or coordinated legitimate actions even when asset permissions are correct. The pattern therefore complements rather than replaces usable protection and review routes. [C-04, C-06]

## Context and prerequisites

Use where participants affect shared assets, shared progress, membership, group objectives or another person's action opportunities, and where the intended conflict can be distinguished from out-of-contract interference. A small, private group that knowingly wants unrestricted collaborative editing may not need this structure. Nor should it silently remove theft, deception or adversarial control that participants deliberately chose as part of a contest. [C-02, C-08]

Before applying the recipe, establish an accountable design owner, a description of asset/role ownership, the ordinary actions people must complete, an accessible way to understand and change grants, and a feasible recovery boundary. The implementation must eventually enforce the intended rules at the authoritative state transition, not merely hide a button. F06 supplies no architecture or enforcement validation. **Exit before implementation** if authority or recovery cannot be specified accurately. [C-02, C-05, C-06]

The source example is deliberately narrow: Minecraft Education documents role privileges in an educational host context. Its warning about the host losing operator authority is not a test of this recipe; it is a reason to question broad delegation. The interdependence study helps motivate preserving meaningful contribution, not indiscriminate restriction. [C-01, C-08]

## Mechanism and evidence

| Proposed causal link | Support | Boundary / what is not established |
|---|---|---|
| Naming affected state and intended powers exposes authority ambiguity. | Analytical inference; the inspected Minecraft article supplies a concrete broad-power hazard. [C-01, C-02] | A written matrix is not enforced behavior and may omit combined actions. |
| Enforced restrictions remove specific disallowed state transitions from an actor's available actions. | Conditional logical consequence of a correctly enforced rule. [C-03] | No enforcement was implemented or tested; alternate accounts, collusion, timing and unlisted powers may bypass the intended boundary. |
| Task-sized grants can retain useful collaboration without unrestricted administration. | Proposed inference from different action needs; no matched experiment of this recipe. [C-02, C-04] | Too many grants can block legitimate work, create approval bottlenecks or diminish chosen interdependence. |
| Clear revocation and recovery reduce confusion about continuing authority. | Design inference; XAG supports usable configuration/protection routes. [C-05, C-06] | Revocation cannot make copied information unknown or necessarily undo a committed consequence. |
| The arrangement improves trust or reduces net harm. | **Hypothesis only.** [C-04] | No direct F06 efficacy result; restrictions can displace harm into another route or give the owner coercive power. |

This is not a claim that “more permissions” means “more safety.” The relevant comparison is the simplest alternative that serves the same activity. [C-04, C-08]

## Recipe

### 1. Name the contribution and the protected interests

Write one ordinary task in player-facing terms. Identify the people affected, what they can lose, and which conflicts are intentionally permitted. Separate asset ownership, editing, publishing, spending, membership and moderation. Do not bundle these because one role name sounds trusted. [C-02]

**Decision:** if the task only needs a personal workspace followed by an optional share, compare that simpler design first. **Exit:** if the rule promises unrestricted shared control and participants genuinely chose it, do not secretly insert protection that contradicts the activity; revise the contract openly or omit the pattern. [C-08]

### 2. Build an action–state–authority matrix

For each consequential action, record actor, target, scope, preconditions, affected parties, confirmation/commit point, who can revoke, and what recovery means. Include reading or revealing information, not just editing it. Mark powers that no routine contributor should inherit automatically, such as transferring ownership or removing the recovery owner. These are proposed design distinctions, not a prescribed role hierarchy. [C-02, C-06]

### 3. Grant only the required scope through a usable route

Offer a clear explanation of what the grant permits and does not permit. A proposed grant might cover one asset, one contribution phase or one group role rather than the whole world. Make the current authority reviewable and the control usable through the intended input/sensory routes. A grant must not require joining unwanted voice chat or understanding an undocumented administrative command. [C-02, C-05]

Choose scope and duration to fit real work. Repeatedly demanding permission for harmless routine actions can defeat the purpose; compare a stable role with narrower exceptional powers instead. No universal expiry time, maximum number of permissions or confirmation count is recommended. [C-04, C-08]

### 4. Keep preview, request, authorization and result distinct

A preview can show a proposed shared change without executing it. A request can remain pending; approval does not necessarily mean the requested action has completed. At the actual commitment, the design requires a check against the current target, role and relevant state—not only the state when the dialog opened. How the runtime satisfies that requirement is outside this research pattern. [C-03, C-06]

**Exit:** if the interface cannot distinguish pending from completed or the system cannot honor the authority boundary, do not label the action protected. Use a simpler restricted activity or defer it pending engineering review. [C-06]

### 5. Define revocation without inventing rollback

Say whether revocation stops new actions, cancels pending ones, changes existing ownership or leaves already committed work intact. Those outcomes differ. Decide what happens when the granting person is absent, disconnected or no longer entitled to grant. A returning participant must receive current authority, not a stale permission from an old session. [C-06]

Information already disclosed cannot be undisclosed. A restoration of shared state can also affect other people's later work; do not call it harmless undo. Where a consequence is irreversible, disclose that boundary before granting or acting. Use the existing F07 safe-exit pattern for general refusal and departure behavior, rather than duplicating it here. [C-06]

### 6. Specify proportionate evidence and recovery

Record enough attributable state-change information to diagnose the authorized action and restore what the contract promises. Avoid indiscriminate collection of private messages or revealing a reporter's identity. Distinguish an action record from proof of malicious intent. Define who may inspect the record and who may correct an error; no actual logging system is designed or deployed here. [C-06]

### 7. Challenge the boundary through combined and stale-state cases

Before participant exposure, propose checks for concurrent edits, grant/revoke during a pending action, temporary-role expiry, host departure, impersonation through confusing names, copying private information, coordinated spending and protected work created by someone who later leaves. The goal is not to publish an exploit procedure; it is to identify missing authority promises using synthetic state. [C-03, C-06, C-07]

### 8. Compare and exit deliberately

Compare the matrix with personal-only state, a private trusted room or a simpler owner/contributor model. Retain this pattern only if it preserves the intended work with an acceptable burden and an upheld authority boundary. Revise, simplify or remove it when legitimate denials, explanation failures or displaced harm outweigh the proposed benefit. Participant evaluation requires separate approval. [C-04, C-07, C-08]

### Adjustable variables

| Variable | Local choice | Exit or revision signal |
|---|---|---|
| Grant scope | Asset, action family, phase or role. | Routine work repeatedly crosses an unexplained boundary. |
| Duration and renewal | Explicit end, phase end or retained grant. | Stale grants survive changed membership or renewal creates repetitive pressure. |
| Commit model | Immediate allowed action, preview, request or reviewed merge. | Pending and completed states cannot be understood reliably. |
| Recovery authority | Who can repair which state under what conditions. | The recovery actor can be removed by the same routine grant it should oversee. |
| Record visibility | Minimum diagnostic state, access and retention plan. | Diagnosis requires unjustified private disclosure or produces an unmanageable queue. |
| Access routes | Review, grant, revoke and help through usable channels. | A person can enter collaboration but cannot control its consequential powers. |

The variables are a hypothesis-led design surface, not approved production settings. [C-02–C-07]

## Worked examples

### Illustrative: jointly assembling a public exhibit

A room contains personal components and one published shared exhibit. Mira may edit her component; Noel may suggest changes to it; neither can publish a new public version solely by editing. A room owner can accept a merge but cannot transfer ownership of Mira's component through that action. All names and rules are synthetic, with no relationship to a real account or playtest. [C-02, C-06]

| Action | Proposed authority | Important case |
|---|---|---|
| Edit personal component | Its contributor. | Editing does not silently alter the published shared version. |
| Suggest a change | An invited contributor within the specified component. | A suggestion is not an accepted edit and cannot execute embedded instructions. |
| Merge into shared exhibit | The designated publication role under current grants. | The review compares the current component/version, not an obsolete preview. |
| Delete shared exhibit | A separately granted destructive power, not ordinary contribution. | Recovery must account for later contributions, not restore an old state over them silently. |
| Remove a participant | A separate membership power. | Removing membership stops the defined future actions; it does not fabricate ownership transfer. |

Suppose Noel opens a merge preview, then the owner revokes the publication grant before Noel confirms. The proposed rule denies the later commit and explains that authority changed. A second case gives Noel a valid current grant but changes the component; the interface must not present approval of the older preview as consent to the new content. These are expected design outcomes, **not executed tests**. [C-03, C-06, C-07]

A simpler personal-display design might satisfy the same audience without any merge process. The team should choose it if the publication workflow creates more coordination work than the shared exhibit is worth. [C-04, C-08]

### Documentary boundary example

Minecraft Education's article describes an Operator role broad enough to alter other operator grants and warns about a host losing its own permissions. The pattern does not claim that its proposed ownership arrangement exists in Minecraft or that the product is unsafe. The example demonstrates why the exact grant matters more than a reassuring role name. [C-01]

## Tradeoffs and alternatives

The intended trade is narrower routine power for additional rule and interface complexity. Legitimate experts may find scope frustrating; a novice owner may be overwhelmed; an unavailable approver may become a bottleneck. A private group may prefer equal powers, while a public collaborative space may require limited contribution. Neither choice is universally appropriate. [C-04, C-08]

Alternatives include personal state with optional sharing, read-only spectators, moderated publication rather than live editing, separate experimental space, or omitting the persistent shared asset. These are candidate design choices, not claims of proven safety. General permission architecture, authentication and fraud defense require their own implementation review. [C-02, C-08]

## Failure cases

**Permission theater:** Controls look restricted but a different action path can change the same protected state. Warning sign: the matrix covers buttons rather than effects. Correction: define the state transition and have engineering validate all entry routes. [C-03, C-06]

**Owner capture or coerced granting:** A participant obtains authority broader than a task needs, or pressures someone to grant it. Warning sign: collaboration depends on yielding unrelated powers. Correction: compare a narrower task, an independent owner recovery boundary or removing the feature. The recipe does not establish a social remedy for coercion. [C-01, C-04]

**Protection becomes exclusion:** Experienced contributors control grants in a way that prevents other people from participating. Warning sign: authorized tasks remain blocked despite understandable requests. Correction: simplify the participation contract and examine who benefits from the restriction. [C-04, C-08]

**Recovery damages valid later work:** Restoring a deleted object also erases later contributions or exposes private history. Warning sign: “undo” has no stated scope. Correction: explicitly define restoration effects and offer a truthful unresolved state when safe recovery is unavailable. [C-06]

## Counterexamples and do not use conditions

Do not apply this pattern to remove a deliberately chosen adversarial action while continuing to advertise it as possible. Do not require a permission request for every reversible personal decision. Do not present it as protection when the studio cannot maintain authoritative checks, usable revocation or the promised recovery. Where shared authority cannot be governed responsibly, reducing the feature scope is preferable to claiming an unverified safeguard. [C-03, C-06, C-08]

The strongest opposing case is a trusted, small group that wants fluid co-creation. There, explicit micro-permissions may damage the experience more than rare mistakes do. That case can falsify the recommendation locally without contradicting the logical value of an enforced boundary elsewhere. [C-04, C-08]

## Playtest

**Proposed and not performed.** Begin with author-reviewed synthetic state-transition cases, then obtain separate approval for any participant study. Do not provoke real harassment, destroy personal work or recruit people to endure abuse. [C-07]

Compare the proposed matrix with the simplest viable alternative for the same task. Include groups with different familiarity, participants using relevant access routes, a temporarily unavailable owner and a returner with stale expectations. Keep assets and intended tasks equivalent; counterbalance order where feasible and account for learning and group dependence. [C-07]

Measure successful intended contributions, unexplained denials, mistaken grant interpretation, unintended changes, time spent administering, recoverability, perceived autonomy and qualitative reasons for preferring either arrangement. Restriction count or number of blocked actions alone is not success. The authority claim fails if a disallowed transition succeeds through an equivalent path; the broader recommendation fails if it adds unacceptable friction, merely displaces harm or cannot preserve the intended social contribution. Define locally acceptable burdens before collecting data and report uncertainty rather than inventing universal thresholds. [C-03, C-04, C-07]

## Claim ledger

| Claim | Class and precise scope | Support / challenge | Confidence and open issue |
|---|---|---|---|
| C-01 | `practitioner-heuristic`: the inspected Minecraft Education article documents role distinctions and a broad operator-grant hazard. | F06-005, Operator and World Builder. | High for article content, not a measured risk rate or verified current build. |
| C-02 | `inference`: mapping task, state and authority can expose powers unrelated to intended contribution. | C-01; distinct role/interdependence demands in F06-001; synthetic matrix reasoning. | Moderate as analysis, low for net social benefit. Completeness depends on the actual game. |
| C-03 | `inference`: if all relevant transitions enforce a scoped rule, the specified disallowed action is unavailable through those transitions. | Conditional rule logic, not an executed security test; C-01 identifies why scope matters. | High only as the conditional statement, not enforcement assurance. Other paths and collusion remain unresolved. |
| C-04 | `hypothesis`: task-sized grants may reduce net out-of-contract harm while retaining valued collaboration. | C-01/C-02 motivate the recipe; F06-001 also warns that necessary coordination can be valued. | Low: no comparative test of this pattern, and burden/displacement can reverse benefit. |
| C-05 | `practitioner-heuristic`: configuration and protection controls need usable access routes. | F06-006, Implementation guidelines. | Moderate for guidance, not demonstrated usability of this proposed matrix. |
| C-06 | `inference`: authority freshness, commitment, revocation, information disclosure and recovery need distinct semantics. | Reviewed F02 decision and P02 action-state distinctions; C-01; explicit state reasoning. | Moderate as a requirement decomposition. No runtime, privacy or recovery assurance. |
| C-07 | `hypothesis`: a comparison against simpler ownership models can discriminate intended contribution from administrative burden. | Reviewed F07-PAT-01 comparison/unit logic; proposed test only. | Low for expected results; protocol and human participation require separate approval. |
| C-08 | `inference`: omit or simplify the pattern when it contradicts chosen conflict or needlessly blocks trusted collaboration. | F06-001's context limits, C-02/C-04 tradeoffs; synthetic counterexamples. | Moderate as conditional design logic, not a preference claim for all groups. |

## References

Public sources were inspected on **2026-10-11 UTC**. Each record below identifies the exact scope used, not whole-literature coverage. A working URL is not a license to reproduce its media. Local claim IDs are scoped to this artifact.

### GDR-SRC-20261010-F06-005

**Minecraft Education / Microsoft, support author Justin.** [Profile Types and Permissions](https://edusupport.minecraft.net/hc/en-us/articles/360047117072-Profile-Types-and-Permissions). **Publication/update:** updated 2026-07-22 23:26; timezone not specified. **Publisher:** Minecraft Education Support.

**DOI:** not recorded. **Version/edition:** Live support article; no numbered game build supplied. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** First-party practitioner implementation documentation.

**Inspected locators:** Student and Faculty Profiles; Operator; World Builder. **Supports:** C-01, C-02, C-03, C-04, C-06.

**Limits:** Educational account/host context, not a general public-server safety experiment. Operator powers include granting/removing operator status; the article warns that the host can lose permissions and may need to disconnect/reconnect. World Builder is separately controlled. No actual classroom, account or game tested.

**Independence/deduplication:** Same corporate family as XAG guidance, but separate product documentation; neither is independent outcome evidence. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-006

**Microsoft.** [Xbox Accessibility Guideline 120: Communication experiences](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/120). **Publication/update:** last updated 2026-03-04. **Publisher:** Microsoft Learn.

**DOI:** not recorded. **Version/edition:** Live unnumbered guideline page within XAG framework v3.2; no immutable commit supplied. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Vendor accessibility practitioner guidance.

**Inspected locators:** Goal; Overview; Implementation guidelines: accessing/configuring communication, social controls, invitations, mute/block/report and notification preferences. **Supports:** C-05.

**Limits:** Feature presence is not measured access or protection. No embedded game/video demonstration was reproduced. This guideline is not a formal standard or legal compliance requirement.

**Independence/deduplication:** Shares the XAG framework and issuer with inherited F01-14 and F02-009, not independent empirical corroboration. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-001

**John Harris, Mark Hancock and Stacey D. Scott.** [Leveraging Asymmetries in Multiplayer Games: Investigating Design Elements of Interdependent Play](https://markhancock.ca/pmwiki/uploads/Publications/p350-harris.pdf). **Publication/update:** 2016; CHI PLAY conference 16–19 October. **Publisher:** ACM, CHI PLAY 2016, pp. 350–361.

**DOI:** 10.1145/2967934.2968113. **Version/edition:** Published paper, coauthor-hosted PDF; BMRS research prototype, not a current commercial build. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Original empirical prototype study, primarily qualitative evidence used here.

**Inspected locators:** Printed pp. 355–356: Method, Participants, Procedure; pp. 357–359: role/leadership accounts, Familiarity with Player Partner Limits Interdependence, Interdependence and Necessity, Hypothetical Mechanics; pp. 359–360: Discussion. **Supports:** C-02, C-04, C-08.

**Limits:** 34 participants in 17 acquainted pairs, ages 18–29, local university recruitment. Character, interface and challenge differences complicate attribution. The self-sufficient “SuperKirks” alternative was hypothetical interview material, not a playable comparison. PDF body text inspected; attempted page rendering and a separate download failed. No figure-derived claim.

**Independence/deduplication:** One research team and prototype. Participant quotations and its discussion are not separate independent confirmations. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

## Related entries and history

Parent topic: [Multiplayer and social systems](../topics/multiplayer-and-social-systems.md), `GDR-CAND-20261010-F06-TOP-01`. Return-state interaction: [Session structure and retention](../topics/session-structure-and-retention.md), `GDR-CAND-20261010-F06-TOP-02`. This recipe owns **powers over shared state**, not general safe exit, action remapping or all moderation policy.

Actually inspected reviewed dependencies retain their identities: `GDR-CAND-20261010-F02-TOP-01` Decision design, selected file lines 66–103 (uncertainty/reversibility); `GDR-CAND-20261010-P02-TOP-02` Feedback and game feel, lines 71–89 (receipt/pending/outcome); `GDR-CAND-20261010-F07-PAT-01` Triangulated balance diagnosis, lines 71–95 (comparison, units, exits); and `GDR-CAND-20261010-F07-PAT-02` Legible commitment and safe exit, lines 60–117. Their exact hashes and archive selection are in the [packet](../reviews/full-run-20261010-f06-review-packet.md). Those files remain reviewed drafts, not included/released dependencies.

Packet-local contradictions: `F06-CON-01`, `F06-CON-03`, `F06-CON-06`. No permanent pattern or source ID has been allocated. Additional moderation and role-handoff work is queued separately, not silently represented by this pattern.

**History:** 2026-10-11 UTC, initial-draft-1, version 0.1.0 draft; predecessor/supersession null. Exact hash in the [integrity receipt](../reviews/full-run-20261010-f06-integrity-receipt.md). Independent review, participant testing, implementation and release remain pending or unauthorized. The next decision is whether to retain this narrow conditional pattern or simplify/merge it after independent ownership and evidence review.
