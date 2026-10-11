---
id: GDR-CAND-20261010-F06-TOP-01
kind: topic
title: Multiplayer and social systems
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
- cooperative interdependence
- mixed-ability matchmaking
- social permissions
- griefing resistance
- communication and moderation
tags:
- cooperation
- competition
- asymmetry
- matchmaking
- communication
- moderation
- trust
- shared-state
- participation
related_topics:
- GDR-CAND-20261010-F06-TOP-02
- GDR-CAND-20261010-F01-TOP-01
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-F06-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-F06-001
- GDR-SRC-20261010-F06-002
- GDR-SRC-20261010-F06-003
- GDR-SRC-20261010-F06-004
- GDR-SRC-20261010-F06-005
- GDR-SRC-20261010-F06-006
- GDR-SRC-20261010-F06-007
- GDR-SRC-20261010-F06-011
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: First F06 submission; conditional research synthesis, no release or
  tested outcome benefit.
hash_record: ../reviews/full-run-20261010-f06-integrity-receipt.md
---

# Multiplayer and social systems

**Research candidate, not released guidance.** Version 0.1.0; candidate revision `initial-draft-1`. This entry supports conditional design decisions, not a universal multiplayer formula. Independent review and participant validation have not occurred for F06. The [batch packet](../reviews/full-run-20261010-f06-review-packet.md) records authorization, input hashes, source coverage, contradictions and gates.

## Decision and scope

Choose **what people must share, what they may decide separately, how they find compatible participation, and how they can protect themselves or leave**. Cooperation and competition are arrangements of rules and interests, not guarantees of friendship, fair treatment or a worthwhile session. The useful unit is a specific relationship: who acts, who benefits, who bears a cost, who knows the relevant facts, and who can refuse. These are proposed analytical definitions rather than formal standards. [C-01]

This topic covers simultaneous and asynchronous participation, recurring groups and strangers, complementary roles, mixed-ability matching, communication, trust, moderation and resistance to harmful use of shared powers. It does not specify transport protocols, server authority architecture, identity verification, anti-cheat implementations, legal obligations or staffing approval. A sound design requirement still needs separate engineering, operations and policy review before implementation. Session commitments and return after absence are developed in [Session structure and retention](session-structure-and-retention.md). [C-01, C-12, C-16]

### Separate the outcome before choosing the mechanism

| Dimension | Working question | Misleading substitute |
|---|---|---|
| Match quality | Does this pairing support the intended contest, cooperation and role experience? | A close final score alone. |
| Technical synchronization | Did participants receive a usable, sufficiently coherent account of actions and outcomes? | Treating every lost encounter as a skill mismatch. |
| Fairness perception | Can players understand and endorse relevant rules, stakes and comparison conditions? | Assuming an internally balanced model will feel fair. |
| Participation | Can intended players join, act meaningfully, communicate as needed and recover? | Counting a login or filled slot as inclusion. |
| Social experience | Is interdependence valued, understandable and tolerable for these people? | Treating voice activity or party size as relatedness. |
| Protection and wellbeing | Can harm be reduced and addressed without assigning all responsibility to its targets? | Using time played, report volume or sanctions as a safety score. |

The table is a diagnostic inference, not a validated measurement instrument. Its value is separating explanations that imply different interventions. For example, increasing a player's statistical skill estimate cannot repair an unusable report menu. [C-01, C-05, C-15]

## Core explanation and mechanisms

### Cooperation creates both contribution and leverage

A shared goal can make another person useful, but usefulness and necessity are different. Optional help permits independence; hard interdependence can create meaningful coordination while also giving one participant the ability to halt another's progress. Separate **contribution**, **visibility of contribution**, **dependency on a particular person**, and **the consequences of that person being unavailable**. [C-10, C-12]

Harris, Hancock and Scott's prototype study involved 34 participants in 17 acquainted pairs. Its qualitative accounts describe both valued necessity and coordination friction; character roles also differed in input and task demands. The proposed self-sufficient “SuperKirks” alternative was discussed in interviews, not tested as an actual comparison. The findings therefore motivate questions about interdependence, not a conclusion that making every teammate indispensable increases enjoyment. [C-02; GDR-SRC-20261010-F06-001]

The evidence-to-application bridge is conditional: when the intended experience includes reliance on another person, prototype a **legible dependency** and compare it with optional assistance. Make the contributor's decision meaningful rather than merely requiring a second body at a switch. Include misunderstanding, absence and refusal in the scenario. When these cases produce hostage-like waiting rather than a valued challenge, shorten the dependency, permit a handoff, or use parallel contribution. Those outcomes remain local hypotheses. [C-10, C-12]

### Competition and asymmetry require a participation contract

Competition can involve conflicting short-term interests within otherwise cooperative groups. Asymmetry may concern available actions, information, authority, time demands or consequences. Equivalent interfaces, equal resources, equal contribution and a fair contest are different design goals. A player may choose a role because of its distinctive responsibility rather than equal output on one scoreboard. Conversely, a “supportive” role can become unwanted maintenance work. [C-01, C-10]

Before balancing numbers, state what each role is entitled to know and do, what its partner must provide, and what happens after a mistake or departure. A role should not be assigned from an inferred disability, age, gender or presumed competence. Offer understandable role previews and a voluntary route to practice or change roles where the shared rules permit. A role with lower motor demand is not automatically easier overall: tracking, planning or social coordination may still be substantial. These are design inferences transferred from reviewed F02 demand separation, not a new validated role-assignment method. [C-10, C-11, C-12]

A strong counterexample is a consensual contest in which private information or the possibility of betrayal is central. Revealing every role state or requiring unanimous permission for every adversarial move would remove the intended decision. Preserve the agreed uncertainty while restricting out-of-contract powers such as deleting another player's account-owned work. The boundary must be stated by the actual game's rules; this entry does not decide which fictional betrayal a community must welcome. [C-10, C-16]

### Matchmaking is a constrained choice, not a single fairness number

Blizzard's historical Season 10 account describes Wide Groups as a way for differently ranked friends to enter Competitive together, with a separate matching arrangement and longer expected queues. It also separates solos from Wide Groups. This documents a concrete participation–queue–matching tradeoff; it does not show that the arrangement caused greater fairness or reduced alternate-account use. [C-03; GDR-SRC-20261010-F06-003]

The same developer's October 15, 2024 patch account reports scaling back loss-streak avoidance after not seeing measurable impact and expressing concern about queue time. No experiment protocol or uncertainty is supplied. This is useful contrary practitioner evidence against treating an intuitively attractive matching intervention as established, but not proof that all streak-sensitive matching is ineffective. [C-04; GDR-SRC-20261010-F06-004]

For a proposed mode, distinguish constraints that protect the activity from preferences that can be traded. Examples of candidate constraints are an agreed ruleset, usable connection conditions and an available role composition; candidate preferences include narrower skill differences or preserving a party. Their priority is a project decision still to be made, not a universal order. Disclose material tradeoffs before entry and allow cancellation while waiting. When a scarce population cannot support every queue, compare a simpler mode structure with multiplying categories until none fills reliably. [C-13]

Matching mixed-ability friends by only an average can conceal how demands are distributed across individual roles. That is an analytical possibility, not a measured F06 effect. Test whether participants can contribute and understand the pairing, not merely whether the team average is equal. Do not use an accommodation setting as a covert proxy for rank or a reason to separate people automatically. Technical failures, unfamiliar rules and deliberate experimentation must remain competing explanations for observed performance. [C-01, C-13, C-15]

### Communication includes the route to decline it

XAG 120 addresses the complete communication experience, including access to configuration and social controls. Its practitioner guidance supports checking more than the existence of voice or text chat. It does not establish that any one channel is accessible to everyone or that implementing the listed features produces safety. [C-05; GDR-SRC-20261010-F06-006]

For each coordination fact, ask who is entitled to know it, whether it is a suggestion or a commitment, when it expires, and which usable route can carry it. Candidate routes include predefined messages, action-linked indicators, text, voice and shared state. More channels need not mean every channel is always active. Preserve mute, block and reporting access without requiring the player to enter the channel they are trying to avoid. Sensory presentation and input details belong to the reviewed P01/P02 dependencies, not to an F06 universal interface recipe. [C-11]

Kasumovic and Kuznekoff's reanalysis of Halo 3 voice-manipulation recordings reports more negative statements in the female-voiced condition; its analyzed speaking-teammate sample and exclusions are narrow. It does not demonstrate that silence is a sufficient protection or that low-ranked players should be presumed abusive. The design question it raises is whether required voice exposes a participation cost that the game need not impose—not whether targets should be responsible for preventing abuse. [C-07; GDR-SRC-20261010-F06-011]

### Griefing resistance starts with what one participant can change

A report can occur after damage; an action rule can sometimes prevent a specific damaging transition before it happens. This is a logical difference, not proof that preventive restrictions improve the whole social experience. Identify powers over shared assets, player movement, communication, visibility, membership, rewards and the continuation of an activity. Some attacks use otherwise legitimate actions repeatedly or in coordination, so a simple “forbidden action” list is insufficient. [C-10, C-14]

Minecraft Education's permissions documentation distinguishes Operator and World Builder powers and warns that granting operator status can allow the host to lose authority. This is a directly inspected documentary example of role boundaries and a counterexample to equating “trusted role” with safely limited power. It is not an evaluation of abuse prevention in public communities. [C-08; GDR-SRC-20261010-F06-005]

The proposed [Scoped shared-state permissions](../patterns/scoped-shared-state-permissions.md) pattern makes authority, scope, duration, revocation and recovery explicit. Use it only where the distinction between intended conflict and out-of-contract harm can be specified. Permission enforcement, race conditions, recovery correctness and audit privacy need engineering review; interface confirmation alone does not enforce a rule. [C-10, C-16]

### Moderation evidence is not a report counter

Kwak, Blackburn and Han studied historical reported League of Legends matches and Tribunal decisions, not a representative sample of all play. Their results include a contrary finding: an expected greater tendency to pardon losing-team cases was not supported. Reporting and judgments were context-sensitive, and requests for reports were observational rather than randomized. These records do not justify treating every report as valid, every loss-related complaint as false, or low reporting as safety. [C-06; GDR-SRC-20261010-F06-002]

Separate immediate protection, reporting, evidence assessment, proportionate action, communication of reasons and correction of mistakes. Riot's inspected FAQ describes sanctions, notification and an appeal-ticket route; it does not establish that detection or appeals are accurate, timely or fair. A policy statement is an implementation intention and operating description, not a measured outcome. [C-09; GDR-SRC-20261010-F06-007]

For targets, consider the cost of finding protection and the possibility of retaliation. For bystanders, consider whether reporting requires public confrontation or disclosure. For reported players, consider understandable reasons and a usable correction route without exposing a target's private information. For moderators, include language coverage, context, workload and escalation capacity in the production decision. These are proposed evaluation dimensions; this batch supplies no validated multilingual moderation model or staffing ratio. [C-14, C-16]

## Design choices and alternatives

| Choice | Appropriate question and potential benefit | Cost, boundary and simpler alternative |
|---|---|---|
| Parallel contributions rather than mandatory coordination | Is being together more important than relying on a specific action? | Less interdependence; compare shared presence with independently completable work. |
| Complementary roles with bounded dependencies | Does a distinct decision make each role worth choosing? | Bottlenecks, unequal recognition and handoff demands; compare optional assistance or role rotation. |
| Skill-banded versus party-preserving entry | Is the promise a comparable contest, playing with friends, or both under disclosed conditions? | Waits, uneven individual encounters, fragmented populations; compare a separate unranked contract or fewer categories. |
| Structured communication versus open conversation | Can core coordination be expressed without mandatory unrestricted chat? | Limited nuance, localization cost and possible message spam; retain optional richer channels only with usable controls. |
| Scoped authority versus all-or-nothing trust | Can routine contribution be separated from destructive or administrative power? | Permission complexity and legitimate-action denials; small private groups may prefer simpler explicit ownership. |
| Preventive restrictions plus response routes | Which harms can be blocked by rules, and which require contextual review? | Restrictions may displace abuse; moderators and appeals remain necessary for unresolved cases. |
| Recurring groups versus transient assembly | Is continuity a benefit people can choose? | Obligations, exclusion and accumulated authority; asynchronous or drop-in alternatives may better fit time constraints. |

These are candidate options, not approved defaults. Choose the smallest arrangement that preserves the desired decisions; omitting a public channel or persistent shared economy is a legitimate alternative when the studio cannot responsibly support it. [C-10–C-16]

## Application process

1. **Name the social promise and limits.** Record whether the desired experience is coordinated reliance, friendly presence, a comparable contest, negotiation or something else. Define intended players, group familiarity, access needs, continuity and the cost of a failed session. Do not start with “maximize engagement.” [C-01]
2. **Map rights and dependencies.** For each consequential action, record actor, affected people/state, required knowledge, authorized conflict and refusal/recovery route. Distinguish temporary action delegation from permanent ownership. Stop if the team cannot distinguish the promised contest from out-of-contract harm. [C-10, C-12]
3. **Choose entry and communication contracts.** Explain relevant matching tradeoffs, role expectations, continuation rules and channel choices before a commitment. A person who declines voice still needs an honest account of which activities remain usable. Fix access barriers rather than disguising them as lack of skill. [C-05, C-11, C-13]
4. **Specify adverse transitions.** Include reconnect, abandonment, mistaken permission grants, owner absence, collusion, targeted message spam and rule changes. Write outcomes for both the departing person and everyone remaining. Coordinate the exit contract with F07 and the session topic. [C-10, C-12, C-14]
5. **Choose the cheapest discriminating prototype.** A paper permission matrix can expose an authority error; it cannot establish whether a timed cooperative role is enjoyable. A matchmaking explanation can test understanding; it cannot establish queue availability. State what the representation omits. [C-15]
6. **Prepare protection and evaluation before exposure.** Obtain separate approval before any participant work. Define withdrawal, simulated adverse cases, data minimization, moderator capacity and the unit of analysis. Do not recruit targets to experience actual abuse as a test stimulus. [C-14–C-16]
7. **Compare against simpler alternatives and retain uncertainty.** Evaluate participation, intended contribution, comprehension, incidents and burdens separately. Keep, revise, remove or defer the mechanism. A higher return rate does not override an unresolved protection failure. [C-01, C-15]

## Patterns and genre adaptations

F06 extracts **one multiplayer pattern**, [Scoped shared-state permissions](../patterns/scoped-shared-state-permissions.md), `GDR-CAND-20261010-F06-PAT-01`. Its complete social benefit is untested. F07's existing `GDR-CAND-20261010-F07-PAT-02`, **Legible commitment and safe exit**, already owns the general commitment/refusal/handoff boundary; it is not recreated here. P02's `GDR-CAND-20261010-P02-PAT-02`, **Fact-preserving cue alternatives**, supplies a communication constraint, not proof of equivalent social outcomes.

No genre file is assigned or created. A future genre adaptation must say how characteristic information, conflict and time commitments change the contract. A label alone cannot settle whether betrayal, unrestricted voice, a persistent world or a strict departure penalty is appropriate. Related genre bytes were not needed for this genre-neutral entry and are not claimed inspected. [C-10–C-13]

## Examples and counterexamples

### Illustrative: a public collaborative workshop

Participants assemble a shared exhibit. Each person can edit their own component and propose a merge into the shared version; publishing the exhibition is separate from editing. A contributor can revoke future editing permission for their component, but cannot promise to make already viewed information unknown. A moderator's ability to hide abusive text is separate from authority to transfer ownership. This is a synthetic design, not an observed game's feature set. [C-10, C-14]

A proposed usability comparison is deliberately hostile to the pattern: compare this arrangement with a simple private room where everyone has equal power. The permission-rich design may prevent an obvious destructive move while causing so many denied actions and approval requests that ordinary collaboration becomes worse. The appropriate response could be fewer powers, narrower public scope or the simpler private-room alternative—not more confirmation dialogs. [C-10, C-15]

### Illustrative: differently experienced friends entering a contest

One person knows the roles; the other understands the rules but lacks execution practice. The group is shown that party-preserving entry may trade a closer individual matchup for playing together. Both can rehearse their chosen role without a public rank change. The novice is not automatically assigned a maintenance role, and the experienced player cannot secretly change the partner's difficulty. This is a candidate contract; no queue algorithm or participant benefit has been established. [C-10, C-13]

The counterexample is a mode promising tightly comparable individual competition. Admitting any party composition might undermine that promise; a separate mode or declining the configuration can be defensible when honestly disclosed. “Always keep friends together” and “always match equal rank” are both overbroad. [C-13]

### Documentary counterexamples, not success stories

The inspected Overwatch accounts provide both an intentional tradeoff and an intervention later scaled back. Minecraft Education's broad operator power supplies an authority hazard. The empirical interdependence study includes friction rather than a pure benefit, and the Tribunal study includes a failed hypothesis. None is offered as proof that a commercially successful game validates a design rule. [C-02–C-04, C-06, C-08]

## Failure modes and constraints

**Access and communication:** A usable chat entry field does not ensure usable notifications, mute controls, reporting or invitations. A required callout may arrive too late in a slower channel; resolving that can require changing the time demand, not merely adding text. Maintain the same entitlement to relevant facts without leaking private roles or turning a hint into an answer. P01's corrected numerical scope is preserved: this entry supplies no universal font size, contrast, target size or timing window. [C-05, C-11]

**Authority and exploitation:** Delayed revocation, shared credentials, ownership transfer, host capture, alt-account re-entry and coordinated actions can bypass a superficial permission model. Logging everything is not a neutral answer; it can expose private communication or create unmanageable review volume. Record which attacks are outside the model and who can accept that residual risk before implementation. [C-10, C-14, C-16]

**Social cost displacement:** A tool that makes it easy for one person to leave may silently assign unwanted work to another. A reputation system may entrench incumbent preferences rather than identify harm. A public vote can become a coalition weapon. These are plausible failure cases to investigate, not prevalence claims or findings from an F06 experiment. [C-12, C-14]

**Production and localization:** Every role, status and appeal path needs comprehensible language and maintained state semantics. Literal translation does not settle what an insult, joke or consensual rivalry means in context. Do not infer intent from locale. Distinct languages, input routes and mixed-language groups require their own evaluation; the inspected studies do not supply globally valid classifiers. Persistent moderation promises also create ongoing operating work, which a design document does not authorize or fund. [C-11, C-14, C-16]

## Playtest and validation

**All studies below are proposed and not performed.** No participant recruitment, harassment exposure, live matchmaking experiment or moderation action occurred. Numeric thresholds, sample sizes and stopping budgets must be chosen for the local decision before a later authorized study. [C-15]

| Question / comparison | Context and procedure | Measures, confounds and falsification |
|---|---|---|
| Does the dependency make contribution valued rather than merely compulsory? Compare optional help with bounded interdependence. | Include acquainted and newly assembled groups separately; preserve role previews and accommodations. Use benign scripted unavailability, not personal blame. | Observe meaningful actions, stalled periods, willingness to repeat the role and felt ability to refuse. Reject necessity as the default if it mainly creates waiting or coercion without the intended contribution. Role/interface differences and familiarity remain confounds. |
| Does the entry contract support mixed-ability participation? Compare truthful matching explanations and mode alternatives. | First test understanding without changing live matching. A later queue study would require actual population/connection data and separate authority. | Ask what is promised, what is not, and why a pairing may differ. Comprehension does not establish match quality; a filled queue does not establish fair experience. |
| Do scoped powers reduce reachable harm without blocking work? Compare the PAT-01 matrix with the simplest viable ownership model. | Use synthetic assets, scripted actions and consenting participants. Include concurrent changes, revocation and an unavailable owner. | Count authorized-task denials, unintended state changes, restoration correctness, explanation errors and operator burden. Reject or simplify if the mechanism merely moves harm into an unprotected action. |
| Are protection and correction paths usable? Compare complete routes, not just report buttons. | Walk through benign simulations as target, bystander, reported person and reviewer. Cover controller, keyboard, alternative input and relevant languages. | Record route completion, unnecessary disclosure, misunderstanding and time away from play. More reports or sanctions cannot serve as a success criterion alone. |

For statistical work, players within a party, recurring group or match are dependent. Repeated reports from the same incident are not independent victims or trials. Plan clustering, spillover, attrition and uncertainty with F07 rather than converting every event into a sample. A small discovery session can identify a failure without estimating its population rate. [C-15]

## Claim ledger

Confidence concerns the stated claim, not the prestige of its source. **High** for a narrow documentary fact does not mean high confidence in social benefit.

| Claim | Precise claim / class | Evidence and locator; support or challenge | Applicability, confidence and unresolved question |
|---|---|---|---|
| C-01 | Separate match quality, synchronization, perceived fairness, participation and social/protection outcomes. `inference` | Reviewed F01 player-experience §§Social play; F07 evaluation measurement distinctions; analytical distinction in this entry. | Moderate: separates different questions logically, not a validated instrument. Which outcomes matter locally remains undecided. |
| C-02 | The studied acquainted pairs described both valued interdependence and coordination friction. `empirical-evidence` | F06-001, printed pp. 355–359; hypothetical mechanics were not a tested condition. | Moderate for qualitative accounts in this prototype; low for other populations or causal benefits. Would strangers or different interfaces respond similarly? |
| C-03 | The historical Wide Group policy trades participation with differently ranked friends against matching/queue constraints. `practitioner-heuristic` | F06-003, Playing Competitive with Friends. | High for documented intent, low for effect. Does the local population sustain the proposed queues? |
| C-04 | The developer reported scaling back loss-streak avoidance without measurable observed benefit and with queue-time concern. `practitioner-heuristic` | F06-004, General Updates → Matchmaking Updates. | High that the account says this; low on magnitude/causality because protocol and uncertainty are missing. Contrary to presumed automatic benefit, not proof of universal failure. |
| C-05 | Communication access includes configuration and protection/social routes, not just sending messages. `practitioner-heuristic` | F06-006, Implementation guidelines. | Moderate for scoped design guidance; no participant outcome or conformance claim. Which routes remain inaccessible? |
| C-06 | Historical Tribunal results are selected reporting/judgment evidence, and the losing-team-pardon hypothesis was not supported. `empirical-evidence` | F06-002, Data Collection/Table 1, reporting analysis, H4.2 and Figure 8. | Moderate: explicit sample and negative evidence; cannot estimate all-player prevalence or validate sanctions. What incidents never reach reporting? |
| C-07 | The Halo 3 reanalysis reports different negative-comment patterns by voiced condition. `empirical-evidence` | F06-011, Methods and Results negative-statement analysis. | Moderate for the analyzed recordings, low for broad demographic explanations; sample/unit and outlier limits retained. No causal claim that disabling voice produces inclusion. |
| C-08 | Minecraft Education documents distinct privileges and an operator-grant risk to host authority. `practitioner-heuristic` | F06-005, Operator and World Builder. | High for article wording, not for present-build enforcement or prevention effectiveness. Can a simpler model suffice locally? |
| C-09 | Riot describes reasons/sanctions and an appeal-ticket route, not verified accuracy or safety. `practitioner-heuristic` | F06-007, Why was I banned?; Can my suspension/ban be removed? | High for the documented policy, low for actual operating outcomes. How are errors and appeals handled in practice? |
| C-10 | Map participation dependencies and scope consequential powers before adding social incentives. `inference` | C-02/C-08; reviewed F02 decision/reversibility distinctions; PAT-01 separates logical permission limits from its untested benefit. | Moderate as analysis; low for net trust/usability benefit. Restriction can block legitimate cooperation or intended conflict. |
| C-11 | Preserve entitled coordination facts across usable routes while allowing communication choices. `inference` | C-05/C-07; reviewed P01 information contract and P02 fact-preserving alternatives. | Moderate as a conditional requirement; emotional/performance equality is unproven. Can timing and privacy be preserved? |
| C-12 | A meaningful contribution should not silently impose an indefinite attendance obligation or transfer unwanted work. `inference` | Reviewed F01 social-cost discussion; F07-PAT-02 recipe; linked F06 session analysis. | Moderate as a design distinction, not an approved studio policy. What consequences are willingly endorsed? |
| C-13 | Disclosed, purpose-specific matching contracts may support participation better than optimizing one score. `hypothesis` | C-03/C-04 motivate a comparison, not efficacy; alternatives and queue scarcity explicit. | Low: no F06 matching experiment or population model. Can benefits survive waiting and role imbalance? |
| C-14 | Combine appropriately bounded action powers with usable protection, contextual review and correction routes. `hypothesis` | C-06/C-08/C-09 identify limits of isolated tools; no evaluated combined intervention. | Low for net harm reduction; plausible displacement, brigading and surveillance costs remain. Which harms are actually reduced? |
| C-15 | Use discriminating comparisons and account for group/event dependence rather than equating events with people. `inference` | Reviewed F07-TOP-01 and F07-PAT-01; selected-data limits in C-06/C-07. | Moderate as evaluation logic; no study executed and no power guarantee. Which design can identify the intended effect? |
| C-16 | Restrict the feature scope when authority, localization, support or recovery cannot be maintained responsibly. `inference` | C-08/C-09 limitations; reviewed F07 ethical production obligations; stated adverse-case reasoning. | Moderate for conditional risk logic; not a funding, staffing or legal decision. What residual risks can an authorized owner accept? |

Source abbreviations `F06-001` through `F06-011` in this table expand to the exact `GDR-SRC-20261010-F06-...` identities below; unlisted numbers are not claims of inspected support for this entry.

## References

Public sources were inspected on **2026-10-11 UTC**. Each record below identifies the exact scope used, not whole-literature coverage. A working URL is not a license to reproduce its media. Local claim IDs are scoped to this artifact.

### GDR-SRC-20261010-F06-001

**John Harris, Mark Hancock and Stacey D. Scott.** [Leveraging Asymmetries in Multiplayer Games: Investigating Design Elements of Interdependent Play](https://markhancock.ca/pmwiki/uploads/Publications/p350-harris.pdf). **Publication/update:** 2016; CHI PLAY conference 16–19 October. **Publisher:** ACM, CHI PLAY 2016, pp. 350–361.

**DOI:** 10.1145/2967934.2968113. **Version/edition:** Published paper, coauthor-hosted PDF; BMRS research prototype, not a current commercial build. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Original empirical prototype study, primarily qualitative evidence used here.

**Inspected locators:** Printed pp. 355–356: Method, Participants, Procedure; pp. 357–359: role/leadership accounts, Familiarity with Player Partner Limits Interdependence, Interdependence and Necessity, Hypothetical Mechanics; pp. 359–360: Discussion. **Supports:** C-02, C-10.

**Limits:** 34 participants in 17 acquainted pairs, ages 18–29, local university recruitment. Character, interface and challenge differences complicate attribution. The self-sufficient “SuperKirks” alternative was hypothetical interview material, not a playable comparison. PDF body text inspected; attempted page rendering and a separate download failed. No figure-derived claim.

**Independence/deduplication:** One research team and prototype. Participant quotations and its discussion are not separate independent confirmations. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-002

**Haewoon Kwak, Jeremy Blackburn and Seungyeop Han.** [Exploring Cyberbullying and Other Toxic Behavior in Team Competition Online Games](https://syslab.cs.washington.edu/papers/lol-chi15.pdf). **Publication/update:** 2015; CHI conference 18–23 April. **Publisher:** ACM, CHI 2015.

**DOI:** 10.1145/2702123.2702529. **Version/edition:** Published paper; historical League of Legends Tribunal records collected April 2013. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Original observational analysis of reported matches and Tribunal decisions.

**Inspected locators:** PDF pp. 2–3: Data Collection and Table 1; pp. 4–5: reporting/bystander analyses; p. 8: H4.2 and Figure 8; pp. 8–9: Discussion and limitations. **Supports:** C-06, C-14, C-15.

**Limits:** Table 1: 1,460,344 accused players, 6,016,046 matches and 10,898,958 reports, not independent unique exposure trials. All included matches had a report; neither all-player prevalence nor intervention effectiveness is identified. NA/EUW/KR are server samples, not ethnic categories. Report-request analyses are observational; no odds-to-probability causal claim imported. Table 1 and p. 8 figure/discussion rendered and inspected.

**Independence/deduplication:** Independent of the other F06 studies. Tribunal decisions, report counts and the authors’ explanations share one selected historical dataset. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-003

**Blizzard Entertainment.** [Defense Matrix Update: Season 10 and Beyond](https://news.blizzard.com/en-us/article/24061006/defense-matrix-update-season-10-and-beyond). **Publication/update:** unknown exact publication day; historical Season 10 announcement. **Publisher:** Blizzard News.

**DOI:** not recorded. **Version/edition:** Historical Overwatch 2 Season 10 announcement; not a verified current game configuration. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** First-party practitioner policy/design account.

**Inspected locators:** Playing Competitive with Friends, paragraphs on Wide Groups, longer queues, role distribution and solo-player separation; Update on Stopping Leavers, paragraph treating disconnects as departures. **Supports:** C-03, C-13.

**Limits:** Documents an intended grouping/penalty contract, not measured fairness, reduced alternate accounts, player safety or wellbeing. Accessible Blizzard News body does not expose a reliable exact publication date. Original Overwatch-domain route returned 403. No game session inspected.

**Independence/deduplication:** Same publisher/product as F06-004. The two pages are not independent empirical corroboration. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-004

**Blizzard Entertainment / official Overwatch forum account.** [Overwatch 2 Retail Patch Notes – October 15, 2024](https://us.forums.blizzard.com/en/overwatch/t/overwatch-2-retail-patch-notes-%E2%80%93-october-15-2024/932243). **Publication/update:** 2024-10-15 patch date; forum displays 2024-10-14 19:00 without an established timezone. **Publisher:** Official Overwatch Forums, Announcements, post 1.

**DOI:** not recorded. **Version/edition:** Season 13 retail patch account; historical, no live-build validation. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** First-party practitioner report, including a reported null/insufficient-impact outcome.

**Inspected locators:** General Updates → Interactive Scoreboard; Matchmaking Updates, first two bullets and developer comments on loss-streak avoidance. **Supports:** C-04, C-13.

**Limits:** The developer reports no measurable effect of loss-streak avoidance and concern about longer queues, but supplies no sample, estimand, uncertainty interval or experiment protocol. This is not proof of zero effect. Exact encoded-dash official forum route resolved; regional live patch pages failed.

**Independence/deduplication:** Same underlying release/account as official patch-page and third-party mirrors; retain one identity for this patch account. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-005

**Minecraft Education / Microsoft, support author Justin.** [Profile Types and Permissions](https://edusupport.minecraft.net/hc/en-us/articles/360047117072-Profile-Types-and-Permissions). **Publication/update:** updated 2026-07-22 23:26; timezone not specified. **Publisher:** Minecraft Education Support.

**DOI:** not recorded. **Version/edition:** Live support article; no numbered game build supplied. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** First-party practitioner implementation documentation.

**Inspected locators:** Student and Faculty Profiles; Operator; World Builder. **Supports:** C-08, C-10, C-16.

**Limits:** Educational account/host context, not a general public-server safety experiment. Operator powers include granting/removing operator status; the article warns that the host can lose permissions and may need to disconnect/reconnect. World Builder is separately controlled. No actual classroom, account or game tested.

**Independence/deduplication:** Same corporate family as XAG guidance, but separate product documentation; neither is independent outcome evidence. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-006

**Microsoft.** [Xbox Accessibility Guideline 120: Communication experiences](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/120). **Publication/update:** last updated 2026-03-04. **Publisher:** Microsoft Learn.

**DOI:** not recorded. **Version/edition:** Live unnumbered guideline page within XAG framework v3.2; no immutable commit supplied. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Vendor accessibility practitioner guidance.

**Inspected locators:** Goal; Overview; Implementation guidelines: accessing/configuring communication, social controls, invitations, mute/block/report and notification preferences. **Supports:** C-05, C-11.

**Limits:** Feature presence is not measured access or protection. No embedded game/video demonstration was reproduced. This guideline is not a formal standard or legal compliance requirement.

**Independence/deduplication:** Shares the XAG framework and issuer with inherited F01-14 and F02-009, not independent empirical corroboration. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-007

**Riot Games, support author RiotTyphon.** [League of Legends Suspension & Ban FAQ](https://support.riotgames.com/en-us/league-of-legends/penalties/league-of-legends-suspension-ban-faq). **Publication/update:** 2026-06-02 17:21; timezone not specified. **Publisher:** Riot Games Support.

**DOI:** not recorded. **Version/edition:** Live policy FAQ; no game build supplied. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** First-party practitioner policy documentation.

**Inspected locators:** Bans, Suspensions, and Restrictions; Why was I banned?; Can my suspension/ban be removed?. **Supports:** C-09, C-14, C-16.

**Limits:** Explains notification, sanctions and an appeal-ticket route; does not establish detection accuracy, response time, appeal success, target safety or moderator conditions. Policy wording about correct penalties is not verification that any particular penalty is correct.

**Independence/deduplication:** Independent publisher from Blizzard; different policy system, not a comparative intervention study. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-011

**Michael M. Kasumovic and Jeffrey H. Kuznekoff.** [Insights into Sexism: Male Status and Performance Moderates Female-Directed Hostile and Amicable Behaviour](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0131613). **Publication/update:** 2015-07-15. **Publisher:** PLOS ONE 10(7), e0131613.

**DOI:** 10.1371/journal.pone.0131613. **Version/edition:** Published article; reanalysis of Halo 3 Xbox 360 voice-manipulation recordings from earlier work. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Original empirical reanalysis of field recordings.

**Inspected locators:** Materials and Methods → Data Collection, Coding, Game and Player Data; Results, opening sample paragraphs and negative-statements analysis. **Supports:** C-07, C-11, C-15.

**Limits:** Results describe 163 games, 102 with speaking and 147 teammates in the analysis; Coding mentions 126 selected video files, an unresolved reporting-unit difference. Silent control excluded; two unusually negative speakers excluded from the negative-statement analysis. Observed-skill associations are not a license to profile players. Authors’ evolutionary explanation is not uniquely demonstrated; silent players’ demographics are unknown.

**Independence/deduplication:** Reuses Kuznekoff and Rose’s earlier recordings: not an independent replication of that original study. Other F06 datasets are distinct. **Rights:** CC BY; attribution retained, paraphrase only; no recordings or personal data redistributed.

## Reviewed dependency transfer

Relevant actual selected bytes were read from `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip`, Library `libfile_082dcf2646dc8191af243051d202f4a8`, backing `file_00000000b0d881f7a51345657bda5287`, version 1. Locally computed archive SHA-256: `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. This establishes retrieved bytes, not canonical authority. The packet records all inspected excerpts and manifest comparisons.

Transferred boundaries: F01 social contribution is not party size; F02 distinguishes intended uncertainty from missing accessible information and social demands from hidden individual adjustment; F07 distinguishes behavior, experience and wellbeing and already owns general safe exit; P01's numerical scopes remain limited to their actual standards/guidelines; P02 separates message receipt from accepted outcomes and fact preservation from identical experience. No external empirical result is imported solely from a dependency citation.

| Selected archive path / exact identity | Version / candidate revision | SHA-256 |
|---|---|---|
| `selected-drafts/topics/player-experience-and-motivation.md` — `GDR-CAND-20261010-F01-TOP-01` | `0.1.0` / `not recorded in selected file`; draft | `f3ffc7d53b6dc88756a915f177d7f6a31aaafd24802913077e9f42e913fd8e06` |
| `selected-drafts/topics/decision-design.md` — `GDR-CAND-20261010-F02-TOP-01` | `0.1.0` / `initial-capture-1`; draft | `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c` |
| `selected-drafts/topics/challenge-and-difficulty.md` — `GDR-CAND-20261010-F02-TOP-02` | `0.1.0` / `independent-review-correction-1`; draft | `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1` |
| `selected-drafts/topics/evaluation-and-balancing.md` — `GDR-CAND-20261010-F07-TOP-01` | `0.1.0` / `initial-capture-1`; draft | `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8` |
| `selected-drafts/patterns/legible-commitment-and-safe-exit.md` — `GDR-CAND-20261010-F07-PAT-02` | `0.1.0` / `initial-capture-1`; draft | `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a` |
| `selected-drafts/topics/interface-and-information.md` — `GDR-CAND-20261010-P01-TOP-02` | `0.1.0` / `review-correction-1`; draft | `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d` |
| `selected-drafts/topics/multimodal-communication.md` — `GDR-CAND-20261010-P02-TOP-03` | `0.1.0` / `review-correction-1`; draft | `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c` |
| `selected-drafts/patterns/fact-preserving-cue-alternatives.md` — `GDR-CAND-20261010-P02-PAT-02` | `0.1.0` / `review-correction-1`; draft | `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0` |

Cross-batch paths above are provenance locators, not active relative links to files included in this F06 delivery. Dependencies remain reviewed **drafts**, unreleased and coverage-open. The F03 packet was partially readable as unreviewed context, but its full reference/body bytes and exact raw hash were not available here; no F03 conclusion is adopted. F04/F05 active drafts were not used. Latest canonical index, pending allocation ledger and child registrations remain unavailable.

## Open questions and change history

**Coverage:** Cooperation, competition, asymmetry, matchmaking experience, communication, trust, moderation and griefing resistance received bounded treatment. Stronger evidence is still needed for strangers and recurring groups, disability-inclusive social participation, mixed-language moderation, appeals, low-population matching, platform differences, persistent-world governance, children and moderator working conditions. No empirical queue simulation, safety audit, live policy comparison or participant study was performed.

Unresolved packet-local cases are `F06-CON-01` (interdependence versus compulsory bottlenecks), `F06-CON-02` (party inclusion versus matching/queue costs) and `F06-CON-03` (protection versus restriction, reporting bias and error correction). Further role-handoff, mixed-ability matching and moderation work is queued without child-key allocation in the packet. Their existence does not increase this packet's two-pattern cap.

**History:** 2026-10-11 UTC — first F06 author submission, `0.1.0 draft`, `initial-draft-1`; predecessor and supersession null. No conceptual ID changed, upstream file overwritten, permanent source allocated or prior batch repeated. Author self-review is in the packet; independent review remains pending. Next decision: a separate reviewer challenges C-10/C-13/C-14 and decides whether PAT-01 is sufficiently distinct and bounded to retain as a draft.
