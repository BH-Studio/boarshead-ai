---
id: GDR-CAND-20261010-G07-PAT-01
kind: pattern
title: "Consequence-preserving roster recovery"
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_identity: G07-local-attempt-01
predecessor_sha256: null
supersedes: null
change_summary: "Initial bounded G07 draft; inspected selected reviewed dependencies; no predecessor or other batch replaced."
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_key: G07
updated: "2026-10-10"
evidence_checked: "2026-10-10"
coverage_state: open
aliases: ["capability-route recovery", "persistent roster fallback"]
tags: ["persistent-roster", "capability-prerequisites", "consequence", "conditional-recovery", "hypothesis"]
related_topics: ["GDR-CAND-20261010-F02-TOP-01", "GDR-CAND-20261010-F02-TOP-02", "GDR-CAND-20261010-W02-TOP-02", "GDR-CAND-20261010-P02-TOP-01", "GDR-CAND-20261010-P02-TOP-02", "GDR-CAND-20261010-P02-TOP-03", "GDR-CAND-20261010-F07-TOP-01", "GDR-CAND-20261010-F07-TOP-02", "GDR-CAND-20261010-P01-TOP-03"]
related_patterns: ["GDR-CAND-20261010-F01-PAT-01", "GDR-CAND-20261010-F02-PAT-01", "GDR-CAND-20261010-W02-PAT-02", "GDR-CAND-20261010-F07-PAT-02"]
related_genres: ["GDR-CAND-20261010-G07-GEN-01", "GDR-CAND-20261010-G07-GEN-02"]
source_ids: ["GDR-SRC-20261010-G07-001", "GDR-SRC-20261010-G07-002", "GDR-SRC-20261010-G07-005", "GDR-SRC-20261010-G07-006"]
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
byte_hash_record: "../reviews/full-run-20261010-g07-integrity-receipt.md"
proposed_domain_owner: BH-GDR-Foundations-and-Systems
ownership_decision: pending-library-coordination
---

# Consequence-preserving roster recovery

**Conditional pattern candidate; not released or validated.** This is one reusable technique for a persistent party, crew or other roster. It is not a requirement for every tactical RPG or tactics game. Its proposed owner is Foundations and Systems, with genre adaptations maintained here; Coordination has not approved that ownership or a permanent ID. The [review packet](../reviews/full-run-20261010-g07-review-packet.md) retains the overlap, evidence gaps and review questions.

## Purpose

When a design promises meaningful continuation after a roster setback, preserve a **reachable route to sufficient capabilities** without automatically restoring the lost person, relationship, equipment, victory or ending. The intended problem is an unintended prerequisite dead-end: the interface or story invites continuation, but the remaining roster cannot obtain a capability required to continue under the promised conditions. Ordinary difficulty, an intentionally closed branch and an explicitly terminal run are different cases. [C-01, C-02]

The proposed player-facing benefit is that a loss can remain consequential while the continuing task remains viable and understandable. That benefit is a **hypothesis**, not established evidence. Some players or designs instead value uncompromising terminal consequences; this pattern may be actively wrong for that promise. [C-04, C-07]

## Context and prerequisites

Use only after the design identifies what “continue” means: reach another chapter, finish the campaign by some route, remain competitive within a mode, or merely explore a changed state. These are not interchangeable guarantees. Specify which endings, optional opportunities and original identities may be lost. A marketing sentence about meaningful choices is not a complete continuation contract. [C-01]

Required design inputs are a defined adverse state, an explicit set of next required capabilities, and a bounded audit horizon whose limitations are stated. Capability can be an action, item access, language, faction permission, transport, available time or another condition—not only combat strength. Record the accessible means of acquiring it and all costs. A rescue mission that requires the missing rescuer, a recruitment fee obtainable only behind the locked route, or a replacement introduced after the deadline is not a recovery route. [C-02, C-05]

The pattern also needs a way to communicate consequences without falsely promising reversibility, production capacity to author and maintain the route, and an approved policy for saves, competitive play and shared campaigns when applicable. The research packet does not authorize any of those implementation decisions. If the intended mode ends after the loss, no recovery mechanism is required merely to satisfy this pattern. [C-05, C-07, C-08]

## Mechanism and evidence

| Proposed causal link | Evidence available | What remains unproved |
|---|---|---|
| A setback changes later capabilities or character availability. | Documented design alternatives in Nintendo, Square Enix, Worldwalker and Supergiant materials; the exact state transition is a rule-specific inference. | No observed campaign-state dataset or frequency of accidental traps. [C-02, C-03] |
| A route supplying the required capability can make a specified continuation feasible. | Logical implication only if its prerequisites, order and costs actually hold in the specified state. | No exhaustive reachability proof for a real game or all future content; manual examples are not executed models. [C-02, C-05] |
| Retaining other consequences can distinguish recovery from full restoration. | A distinction between state variables; documents supply limited examples of different loss/continuation policies. | Whether players perceive the retained consequence as coherent or meaningful. [C-03, C-04] |
| Communicating the route can help players understand what remains possible. | Reviewed F02/W02/F07 guidance motivates the information and commitment questions. | Comparative comprehension and access benefit of this exact recipe. [C-04, C-06] |
| Viable, understood continuation improves the intended experience relative to alternatives. | No original player-effect evidence inspected for the complete mechanism. | Magnitude, preference variation, long-term engagement and whether recovery weakens stakes. This link remains low-confidence. [C-04, C-07] |

The sources demonstrate **alternatives exist**, not that this synthesis has been implemented as a package or tested. Fire Emblem Engage's documented mode choice, Tactics Ogre: Reborn's documented recovery/training structures, Wildermyth's described loss/legacy choices and Pyre's campaign-continuation description are different designs, not four replications of the pattern. [C-03]

## Recipe

1. **Name the promise and the excluded guarantees.** Write what progression remains possible after the selected setback, under what mode and horizon. State which losses and endings remain final. Where the promise is terminal loss, stop rather than smuggling in recovery. This is a proposed local design choice to be approved by the relevant game team, not an approved studio-wide policy. [C-01, C-07]
2. **Separate capability, identity and world state.** For each affected actor record available actions, equipment, resources, relationships, permissions, narrative participation and timing. Mark which requirements are truly mandatory for the stated continuation and which merely support a preferred strategy. Do not treat an authored “needs this person” condition as interchangeable with “needs any healer.” [C-02]
3. **Select adverse states and the audit boundary.** Include at least the locally relevant losses, injuries, departures, resource exhaustion and mutually exclusive choices; justify which combinations are inspected. Use actual scenario specifications and saved states when authorized in a future implementation. Describe unchecked states plainly. Do not call a sample audit proof that every campaign state is safe. [C-05]
4. **Trace a complete route, not just a replacement reward.** List the next required capability, how the remaining party reaches its provider, costs and deadlines, and the state after acquisition. A valid route must not depend circularly on the missing capability or a branch already closed by the loss. Examine access demands as prerequisites too: an alternative that removes the supported input path is not an equivalent remedy. [C-02, C-05, C-08]
5. **Choose what changes and what remains lost.** Possible remedies include a substitute role, a different objective route, a temporary concession, an altered encounter or a differently authored continuation. Preserve chosen identity/world consequences rather than claiming a replacement has restored a relationship. Avoid automatically reopening every optional outcome. Prefer the smallest maintainable change consistent with the promise, but test whether it becomes an exploitable dominant tactic. [C-04, C-07]
6. **Expose the consequential choice.** Before an irreversible commitment, communicate the known category of loss and relevant mode policy. Afterward, show a discoverable next step without implying that it erases the setback. Distinguish a recoverable inability, an intentionally closed branch and an actual ending. Use the existing legible-commitment and objective-contract guidance rather than adding a redundant disclosure system. [C-06]
7. **Audit transitions and foreseeable abuse.** Revisit route viability after representative resource, roster, mission-order and save/reload changes. Check narrative contradictions, unavailable speakers, duplicate rewards, deliberate sacrifice-for-replacement loops and mode incompatibilities. Record unsolved cases and affected promises. This step describes future validation work; none was executed on a game here. [C-05, C-08]
8. **Compare with simpler alternatives and decide.** Use the proposed tests below to compare continuity, comprehension and retained stakes. Keep, narrow, revise or reject the technique; no result is presumed. When a viable route is too expensive to author or contradicts the intended ending, change the promise, offer a prior-save/restart option under a disclosed policy, or omit the technique rather than advertise continuation that cannot be supported. [C-07, C-09]

### Adjustable variables and exit conditions

| Variable | Decision to make | Exit or redesign condition |
|---|---|---|
| Continuation scope | Next scenario, alternative campaign route, or another explicitly named horizon. | No stable definition exists, or only an intended terminal ending follows. |
| Recovery target | Restore an action, access permission, timing opportunity or other capability. | The requirement is inseparable from a deliberately lost identity/ending. |
| Cost and delay | What resources, opportunity, changed goals or waiting are required? | Payment depends on the missing capability, violates the deadline, or creates an inaccessible loop. |
| Consequence retention | Which relationships, outcomes, possessions and role identities remain changed? | The remedy falsely restores all stakes or creates contradictory narrative state. |
| Discoverability and choice | When can the player know and choose the route? | It requires privileged external knowledge or misleading reassurance. |
| Replacement quality | What capabilities are sufficient without eclipsing existing roster investment? | Deliberate loss becomes the plainly superior acquisition strategy under the game's intended incentives. |
| Mode and multiplayer policy | Which configurations permit the route and who consents? | It violates competitive rules or another participant's agreed campaign state. |
| Audit horizon and maintenance | Which states and future additions were actually checked? | Required coverage exceeds maintainable scope; uninspected content is presented as guaranteed safe. |

These variables have no universal numerical values. The decision criteria depend on the approved game's actual task and stakes. [C-01, C-05, C-07, C-08]

## Worked examples

### A lost interpreter and two different continuation promises — illustrative

Suppose an invented persistent crew loses its only interpreter before entering a mountain city. The game has promised that the journey can continue after crew loss, **not** that every diplomatic ending remains available. The next required gate checks whether the party has a recognized travel permit. The interpreter could have negotiated that permit through a trusted contact; that personal route is now closed. A surviving quartermaster can instead reach a public office before its stated closure, exchange supplies already available outside the gate and obtain a limited transit permit. [C-10]

The recovery target is **legal transit**, not resurrection, language proficiency, the contact's trust or the original ending. The route is feasible only if the office is reachable without the interpreter, the supplies are available before entry, the deadline is still open and the permit is accepted by the next gate. The design must specify those facts; the pattern cannot create them by assertion. The aftermath can retain the loss, reduced supplies and missed diplomatic opportunity while permitting an altered next chapter. [C-02, C-04, C-10]

A manual state trace for this illustrative specification is: interpreter absent → original contact route unavailable → quartermaster reaches public office → available supplies exchanged → limited permit acquired → gate admits transit → diplomatic ending still closed. This is a stated sequence of preconditions, **not a programmatically executed model or player test**. If the office requires an interpreter or supplies obtainable only inside the city, the sequence fails and the recipe rejects it. [C-05, C-10]

The critical forecast is modest: “the personal negotiation is no longer available; another transit route exists.” It should not say “nothing important was lost.” Players might still find the replacement contrived or the retained cost trivial. Those reactions remain hypotheses requiring observation. [C-04, C-06]

### A tactical role lost before the next encounter — illustrative

A different invented game promises that losing a ranged specialist does not automatically prevent finishing the next chapter. Rather than award a stronger copy of the same character, a future scenario may permit a shielded approach to the device that otherwise needed a ranged interaction. The alternate route retains the absence of the specialist and may give up a time-sensitive optional objective. Before calling this recovery, check the actual remaining roster's movement/action budget, route access, interruption rules and objective acceptance. This is where the reviewed multi-route objective contract helps. [C-02, C-05, C-10]

A counterexample is an explicit challenge mode whose rule is “complete the expedition with this original crew or end the run.” Supplying a mandatory replacement would alter the chosen task. The appropriate action may be to provide a legible ending and restart/re-entry policy, not apply this pattern. No difficulty or accessibility label by itself decides that tradeoff. [C-07, C-08]

## Tradeoffs and alternatives

**Retained-consequence recovery** may preserve campaign continuity, but costs new routes, dialogue/state handling and balance checks; it may reduce scarcity or feel contrived. **Temporary injury** preserves a character but may shift the cost to waiting or substitutes. **Broad recruitment** makes capability replacement natural but can weaken a tightly authored cast or encourage intentional sacrifice. **Prior-save replay** can preserve a stringent campaign model while imposing repetition and not undoing learned information. **Full restoration** can prioritize experimentation but makes a different promise about loss. **An explicit terminal ending** is a valid alternative when selected and intelligible. These are conditional design comparisons, not measured rankings. [C-04, C-07, C-08]

An alternate route should not be treated as automatically equivalent. It can change resource costs, combat requirements, narrative obligations, access demands and which player goals remain possible. A fairness claim requires a declared criterion; identical rewards or completion rates alone do not establish equivalent experiences. A simpler design with fewer persistent dependencies can be preferable to a sophisticated recovery system whose prerequisites are too expensive to verify. [C-02, C-07]

## Failure cases and observable warning signs

| Failure | Warning to investigate, not an observed result | Possible correction or rejection |
|---|---|---|
| Circular remedy | Every available route requests the skill, person or currency made unavailable by the setback. | Change a prerequisite or acknowledge the ending; do not label the route viable. |
| False identity replacement | Dialogue treats a substitute as if the original relationship or promise survived. | Separate role capability from identity state and author the changed consequence. |
| Attrition ratchet | Recovery cost depletes the resources required for the next recovery and eventually strands the party. | Audit the sequence over the promised horizon; change scope/cost or use another policy. |
| Dominant sacrifice loop | Deliberate loss reliably yields a preferable replacement under intended play goals. | Inspect incentives and retained consequences; avoid unmeasured blanket punishment as a fix. |
| Invisible recovery | Players repeatedly conclude continuation is impossible despite an intended route. | Test discoverability and terminology; do not attribute this automatically to low skill. |
| Inaccessible substitute | The alternate path imposes a new sensory, timing or input prerequisite outside supported access. | Preserve relevant access paths or label the options as nonequivalent. |
| Erased stakes | Participants in a future test describe the selected loss as cosmetic or the remedy as obligatory. | Retain a different consequence, narrow the mode or omit the pattern. |
| Unmaintainable guarantee | New missions or patches invalidate routes that the release still promises. | Version the audit and promise; reopen review before asserting continued coverage. |

No frequency, causal attribution or player outcome is asserted by these warnings. They define what a later audit/test should look for. [C-05, C-07–C-09]

## Counterexamples and do-not-use conditions

Do not apply the recipe as a compulsory rescue in a deliberately terminal run, as a way to override another player's agreed persistent campaign, or as a covert replacement for an accepted consequence. Do not promise preservation of all endings when the point of the decision is to close some of them. Do not use an expensive new recovery subsystem where eliminating an accidental prerequisite or documenting an existing valid route addresses the actual problem. [C-07]

The strongest counterargument is that consequences feel consequential partly because some losses cannot be repaired. That argument does not prove every loss should be terminal, but it defeats a universal recovery rule. Another counterargument is that restoring function can itself erase the particular scarcity being tested even when narrative dialogue remembers the loss. The proposed pattern therefore depends on a prior continuation promise and an explicit account of which scarcity should remain. [C-04, C-07]

A lack of full empirical corroboration is also a limit, not support for whichever policy is more comfortable. The access-limited permadeath research lead is recorded in the genre entry and packet; it supplies no tested result for this recipe. The pattern must be judged as an untested synthesis until direct evidence is available. [C-04]

## Playtest and validation — proposed, not performed

First perform a **future specification/reachability audit** on authorized scenario data. Enumerate the explicitly chosen adverse states and trace each candidate remedy through all prerequisites within the defined horizon. Record checked and unchecked states, options, versions and any failure. A route that fails even its own stated preconditions is rejected before player-effect claims are tested. This audit would establish bounded structural feasibility, not enjoyment, accessibility or universal safety. None of it has been run here. [C-05, C-09]

Then compare a locally justified recovery policy with an appropriate alternative such as prior-save replay, temporary injury or an explicitly terminal mode. Match encounter rules and party capability as far as the tested mechanism allows; record unavoidable differences in continuity, time investment and information. Recruit for the intended goals and relevant access needs rather than assuming one tactics population. Do not require genuine personal loss or distress to make a test “authentic”; disclose the simulated scenario and allow withdrawal. [C-08, C-09]

Measures should distinguish whether the party **can** continue, whether the participant can identify a viable route, whether they understand what remains lost, and how they evaluate agency, coherence, attachment and stakes. Observe voluntary route choice and burden; do not treat completion alone as endorsement. Narrative attachment, prior knowledge, build strength, familiarity with loss mechanics and order effects are confounds to record. Sample sizes, thresholds and analysis plans need a justified local protocol, not an invented guarantee. [C-04, C-09]

Reject the remedy if its promised route is structurally unavailable, inaccessible within the supported conditions, or misleading about preserved consequences. Narrow or reject the benefit claim if comprehension does not improve for the identified problem, if participants selecting the intended stakes consistently find it negates them, or if it produces a dominant loss-for-reward strategy. A positive result in one authored scenario cannot establish long-campaign or multiplayer validity. When checking learning, retain the underlying rule while changing the surface; a different recovery rule is an adaptation/discrimination probe, not evidence of unchanged-rule transfer. [C-05, C-07, C-09]

## Claim ledger

| Claim | Precise claim and class | Support / locator | Confidence and limit |
|---|---|---|---|
| C-01 | The pattern is conditional on an explicit continuation promise, not every loss. `inference` | Defined scope; F07 commitment and W02 objective distinctions. | Moderate as a design boundary; no approved game policy or genre standard. |
| C-02 | Capability, identity and world-state prerequisites are distinct; a remedy must reach the required capability. `inference` | Explicit examples and dependency reasoning. | High within specified rules; no exhaustive real-game proof. |
| C-03 | The cited developers document differing loss/continuation alternatives. `observed-example` | 001 footnote18; 002 incapacitation/training; 005 death/legacy; 006 campaign continuation. | High for the documents; not implemented observation of this complete recipe or effect evidence. |
| C-04 | Retaining other consequences while restoring a capability route may support intelligible continuity. `hypothesis` | Proposed synthesis from C-02/C-03 and tests below. | Low: no original comparative player evidence for the mechanism. |
| C-05 | A route is feasible only if its complete prerequisites hold; an audit's guarantee is limited to its checked scope. `inference` | State-transition reasoning; F07 measurement limits. | High logical condition, but no gameplay/state audit performed here. |
| C-06 | Consequence and route communication should distinguish recovery from restoration. `inference` | F02 opportunity-cost, W02 objective-contract, F07 commitment selected sections. | Moderate conditional design reasoning; comprehension effects untested. |
| C-07 | Terminal-loss, identity-specific and scarcity goals can defeat the recovery recommendation. `inference` | Counterexamples and alternatives; source001 documents selectable loss policies. | Moderate for conditional conflict, not measured preference distribution. |
| C-08 | Access, localization, multiplayer policy and authoring state costs constrain the technique. `inference` | Reviewed P01/P02/F07; prerequisite/state reasoning. | Moderate risk analysis; no access certification, economic estimate or competitive approval. |
| C-09 | The proposed audits/comparisons can disconfirm structural and experience claims separately. `hypothesis` | Protocol above, reviewed F01/F07 limitations. | Low until tasks/measures are validated; no tests or participants. |
| C-10 | The interpreter and ranged-role examples illustrate possible routes and failure conditions. `inference` | Explicit invented rules above. | High for their stated logical conditions only; not observations or tested models. |

## Related entries and history

Applications: [Tactical RPG](../genres/tactical-rpg.md), `GDR-CAND-20261010-G07-GEN-01`, for party/campaign coupling; [Tactics](../genres/tactics.md), `GDR-CAND-20261010-G07-GEN-02`, only when local outcomes persist into a roster. Existing patterns retained: `GDR-CAND-20261010-F02-PAT-01` (opportunity costs), `GDR-CAND-20261010-W02-PAT-02` (objective routes), and `GDR-CAND-20261010-F07-PAT-02` (commitment and exits). Their exact inspected versions are in the packet, not silently copied into this delivery.

The distinct proposed contribution is **cross-scenario capability reachability after persistent roster change**. It is narrower than general difficulty adaptation and more longitudinal than one objective contract. This distinction is an author proposal; a separate reviewer/Coordination may decide it belongs as an adaptation of existing guidance rather than a new pattern. No canonical owner or permanent ID is asserted. Local conflicts: G07-CON-01, G07-CON-02 and G07-CON-03.

Version **0.1.0**, revision `initial-draft-1`, no predecessor or supersession. Draft recommendation, coverage open; independent review not performed, reviewer/approval fields null. The next decision is whether independent review retains this distinct pattern and its narrow conditional claim. No release, adoption or implementation follows from the file's creation.

## References

All listed sources were accessed on **2026-10-10 (America/Los_Angeles; session also falls on 2026-10-11 UTC)**. The G07 author inspected the cited text through web retrieval. Unless explicitly stated otherwise, `observed-example` means observation of the named document, **not play of a game build**; no scene/timestamp or reproduction is invented. Public-page bodies were not archived in this deliverable. Copyright remains with the respective owners; short paraphrases and source metadata only, no redistributed screenshots, game assets, article bodies or manual pages. Repeated IDs identify the same source across G07 files. Cross-batch URL/DOI/edition deduplication is pending Library Coordination.

### GDR-SRC-20261010-G07-001

**Nintendo; developer interview, with the used remarks attributed to Higuchi, Tei and Nakanishi. [Ask the Developer Vol. 8, Fire Emblem Engage — Part 3](https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-8-fire-emblem-engage-part-3/).** Nintendo. Publication/update: 2023-01-17. Edition/build: Fire Emblem Engage; Nintendo Switch, launch-era developer interview; no executable build inspected. Access: `relevant-excerpt`. Type: first-party developer interview.

**Exact locator:** Bond/skill/class inheritance discussion, browser extraction lines 108–124; closing discussion: Tei on attachment, Higuchi on Classic/Casual and footnote (18), lines 134–148. **Supports:** C-03. **Limits:** Statements about attachment and attracting players are creator beliefs/intent, not measured effects. The mode distinction is documented, not reproduced. No inference that all character deaths or defeat states obey one exception-free rule. **Independence:** Nintendo / Intelligent Systems; independent production from the other game studios, but related to Nintendo-hosted publisher descriptions as a distribution channel.

### GDR-SRC-20261010-G07-002

**Square Enix. [Tactics Ogre: Reborn — battle-design remake explanation (Japanese original)](https://www.jp.square-enix.com/tor/battledesign/).** Square Enix. Publication/update: unknown; Reborn-specific documentation. Edition/build: Tactics Ogre: Reborn, not the original or Wheel of Fortune; numbered build unspecified; page marks images as in development. Access: `relevant-excerpt`. Type: first-party system documentation.

**Exact locator:** Unit-level management; scouting; trajectory prediction; incapacitation and revival; training; Union Level; C.H.A.R.I.O.T.; W.O.R.L.D./level sync, browser extraction lines 32–37, 88–93, 133–150, 161–168, 198–214. **Supports:** C-03. **Limits:** English paraphrase of Japanese text by the G07 author, not an official English localization or independent bilingual review. Promotional benefit claims are not efficacy evidence. No runtime, balance or corner-case verification. **Independence:** Square Enix; related production/publishing family to Triangle Strategy, not independent evidence of a general rule.

### GDR-SRC-20261010-G07-005

**Worldwalker Games LLC. [Wildermyth — About This Game](https://store.steampowered.com/app/763890/Wildermyth/).** Worldwalker Games LLC / WhisperGames via Steam. Publication/update: page update unknown; release 2021-06-15. Edition/build: Base-game Steam description; Omenroad and console differences not researched; numbered build unspecified. Access: `relevant-excerpt`. Type: first-party developer product description.

**Exact locator:** Choices That Matter; A New Approach to Death; Deep and Creative Tactical Combat; A Custom Pantheon of Legends, browser extraction lines 183–199. **Supports:** C-03. **Limits:** Descriptions establish available design ideas only. No precise maiming probability, mortality exception, retirement algorithm or relationship effect size inferred. Community-wiki details were not promoted to primary support. **Independence:** Worldwalker production; Steam is a distribution host, not a second witness.

### GDR-SRC-20261010-G07-006

**Supergiant Games. [Pyre](https://supergiant-games.itch.io/pyre).** Supergiant Games via itch.io. Publication/update: release 2017-07-25; visible update 2026-09-16 07:26 UTC. Edition/build: PC/macOS/Linux product description; base campaign and separately advertised True Nightwing mode; numbered build unspecified. Access: `relevant-excerpt`. Type: first-party developer product description.

**Exact locator:** Opening description; Action-Packed Three-on-Three Battle System; A Branching Story with No Game-Over; True Nightwing note, browser extraction lines 10–35 and metadata 38–43. **Supports:** C-03. **Limits:** Used as a contested RPG/tactics boundary case, not a settled tactical-RPG classification. The page describes enlightenment/masteries, so it does not establish a progression-free game. No claim all modes share identical rules. **Independence:** Supergiant production; not corroborated by reposting its same text elsewhere.
