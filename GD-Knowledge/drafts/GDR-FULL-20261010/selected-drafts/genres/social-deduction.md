---
id: GDR-CAND-20261010-G19-GEN-03
permanent_id: null
kind: genre
title: Social deduction
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
- hidden-role deduction
- social inference game
tags:
- partial-information
- deception
- accusation
- elimination
- communication-consent
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G19-PAT-02
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G19-GEN-02
source_ids:
- GDR-SRC-20261010-G19-010
- GDR-SRC-20261010-G19-011
- GDR-SRC-20261010-G19-012
- GDR-SRC-20261010-G19-013
- GDR-SRC-20261010-G19-014
- GDR-SRC-20261010-G19-015
- GDR-SRC-20261010-G19-016
- GDR-SRC-20261010-G19-020
reviewer: null
approved_by: null
approved_date: null
byte_hash_record: ../reviews/full-run-20261010-g19-review-packet.md#candidate-byte-manifest
---

# Social deduction

**Draft research candidate, not released knowledge.** Scope: G19 only. Definitions and application recipes are reversible research proposals, not approved studio decisions. No game implementation, participant test, independent review or publication occurred in this batch.

## Definition and contested boundaries

A **social-deduction game**, for this draft, makes inference about other agents’ identities, loyalties, objectives or trustworthiness of game claims consequential under incomplete information. Participants can strategically conceal, misrepresent or selectively disclose within the agreed rules. The core question is not simply “who is lying?” but **which game-state explanations remain plausible, whose incentives shape a statement, and what action follows under uncertainty**. This working definition does not turn ordinary behavior into a reliable personality test. [S-01, S-12]

Hidden roles are common in the inspected examples but are not a sufficient definition: a cooperative puzzle can partition knowledge without giving players adversarial reasons to deceive. Likewise, bluffing over a resource can be adjacent to social deduction without making hidden identity the central repeated task. A detective story with authored clues can share hypothesis testing while lacking live opponents manipulating claims. These are contested boundaries to investigate, not reasons to merge the distinct taxonomy entries. [S-01, S-02]

Party play is a separate axis of guidance: [Party](party.md) addresses the shared occasion, participation and re-entry, while this file addresses strategic information and accusation. Neither voice, a particular group size, a designated moderator, nor serial elimination is universal. Online, local, cooperative, PvP and tone remain facets. [S-05, S-07, S-15]

## Custom research instructions

Inspect a versioned ruleset and concrete role configuration before describing truth, deception or victory. Build an evidence route for **what the system knows, what each participant observes, what statements may be false, who is allowed to communicate, and what becomes public at each phase**. Specify whether the source is a rulebook, official explanation, creator account, recorded session or directly played build. This batch has primary rule/document inspections but no runtime observations. [S-03–S-09]

Compare different sources of uncertainty: deliberately hidden state, uncertain observations, unreliable role information, omissions, strategic lies, misunderstood rules and inaccessible communication. Do not automatically call all false statements deception; a participant may be mistaken, and a rules system may intentionally issue an unreliable signal. Do not turn a moderator’s private state into a public accessibility aid without auditing the information contract. [S-09, S-10, S-13]

Seek contrary structures: no elimination, limited post-elimination influence, role-dependent communication, structured text and cooperative asymmetric information. Inspect mixed-experience groups and relevant communication-access participants without defining a “good liar” by extroversion, eye contact, accent, pauses or diagnosis. Group consent to in-game deception is not blanket consent to interpersonal harassment or recording. [S-02, S-05–S-08, S-12–S-14]

Prioritize full role/rules artifacts, configuration-specific creator notes, observed sessions and original studies with identifiable methods. Empirical access findings here do not validate a lie detector, perfect group size or universally fair discussion timer. Future demographic or cultural comparisons must be supported directly rather than guessed from national stereotypes. [S-10, S-12, S-15]

## Player promises and varied audiences

Candidate promises include forming and revising a plausible explanation, using limited influence before uncertainty resolves, performing an in-game role, and experiencing a reveal that makes earlier signals interpretable. Some audiences may enjoy social improvisation; others may prefer more explicit evidence and constrained statements. These are hypotheses about possible desired experiences, not a single population profile. [S-01, S-09]

A player may enjoy deduction while disliking accusation directed at them, or enjoy bluffing while finding private-message logistics inaccessible. A person who chooses text may need richer qualifiers, not fewer opportunities to participate. Evaluate preferred experience, task access and strategic agency separately; lack of speech is not lack of interest, and a mistaken accusation is not proof of dishonesty or cognitive deficit. [S-10, S-12]

## Characteristic loops and structures

A reusable analytic loop is **receive partial information → choose what to reveal or conceal → compare claims and actions → commit influence → observe a resolution or further signal → revise the explanation**. This synthesis can describe cyclical day/night play, action-and-meeting play or a single bounded reveal structure. It is not a claim that every game uses all those phases or the same win condition. [S-01, S-03, S-04, S-07]

Commitment may involve a nomination, vote, resource spend, public claim or trust decision. Different structures separate accusation from elimination, elimination from team outcome, and loss of ability from loss of voice. Those distinctions matter more than simply labeling a player alive or dead. Session reset can make role knowledge obsolete while leaving social reactions intact; the latter is a risk to investigate, not an asserted effect for every group. [S-09, S-11, S-14]

## Information boundaries and mechanisms

### Separate emitted evidence from the truth it appears to describe

The inspected Clocktower explanation permits some role information to be false under declared game conditions. Among Us’s overview describes observation and discussion under opposing objectives. Neither document licenses treating every player statement or interface signal as omniscient truth. [S-03, S-04; GDR-SRC-20261010-G19-011; GDR-SRC-20261010-G19-012]

The proposed application is to represent five layers distinctly: **scenario truth**, **signal actually delivered**, **participant’s statement about it**, **declared reliability conditions**, and **permitted recipients**. In design notes, “the witness was shown a warning” can be certain while “the warning identifies the traitor” remains uncertain. An accessible transcript should preserve the emitted message and its legitimate source context, not replace it with hidden ground truth. Conversely, it should not erase information available in the original route merely to preserve difficulty. [S-09, S-10]

| Proposed audit object | Question to answer before implementation | Failure to look for |
|---|---|---|
| Private assignment or signal | Which participant is entitled to know it, and can the signal itself be unreliable? | A public help message confirms a hidden role or silently corrects an intentionally unreliable clue. |
| Claimed observation | Is this a player assertion, a logged action, or an authoritative state disclosure? | A summary upgrades hearsay to verified fact. |
| Meeting/accusation record | What timing, source attribution and uncertainty remain visible? | A delayed caption is treated as a new confession, or an automatic summary drops a qualifier. |
| Spectator/dead-player view | What new knowledge becomes available, and may any of it reach active players? | An observer learns hidden truth and leaks it through a channel designed for ordinary play. |
| End-of-round reveal | Which secrets end, which persist, and can participants decline the debrief? | Replay/stream overlays disclose future-round information or pressure a person to defend their real character. |

This is an **illustrative design audit**, not a complete specification for any cited title. Each row must be checked against the actual rules and participants. [S-09, S-13, S-14]

### Treat communication capacity as a game resource and an access question

The historical Quick Chat update documents a structured text route. That is a counterexample to a genre-wide voice requirement, not evidence that a phrase library supports every explanation equally. [S-05; GDR-SRC-20261010-G19-013]

A proposed channel comparison should ask whether the player can assert a source, timing, negation, qualification and uncertainty when those distinctions matter. Adding phrases may reduce omission but increase navigation and reading burden; free text may increase expressive range but also moderation and composition demands. Voice can support fast interaction while requiring access and facilitation that cannot be assumed. Alternative channels should be evaluated for the *particular inference task*, not ranked by a universal hierarchy. [S-10]

The qualitative communication study supplies contextual barriers, not proof that a specific channel fixes them. Preserve that distinction when adopting speaker indicators, persistent claims or interpreter-aware pacing. A public transcript can aid review while increasing persistence of accusations; private logging may require new privacy and moderation decisions. No such intervention was tested here. [S-10, S-14; GDR-SRC-20261010-G19-020]

### Choose elimination and participation independently

Clocktower’s base rules retain conversation and a limited remaining vote after death. One Night’s publisher advertises a no-elimination structure. These are different rule options, not comparative evidence of social benefit. [S-03, S-07; GDR-SRC-20261010-G19-011; GDR-SRC-20261010-G19-015]

A later, specific Among Us source changes the comparison: the **September 29, 2026 v19.0.0 Influencer announcement** describes a ghost role that can send a living crewmate a constrained picture message. It is therefore incorrect to impose a universal rule that post-death play must never transmit information to living players. The correct constraint is the **declared role/version information permission**, not blanket silence. [S-06; GDR-SRC-20261010-G19-016]

The application proposal is to compare a no-elimination design, an explicitly bounded post-elimination role, and a genuine rest/observer option. More duties can preserve influence for one participant while prolonging unwanted involvement for another. New ghost powers can also change deduction, ending conditions and balance; they are not merely “engagement” features layered outside the rules. [S-11]

### Bound accusation by in-game evidence and consent

Innersloth’s conduct policy distinguishes game deception from harassment and advises disengaging from harassment. It also discourages leaving solely over an unwanted role. Those propositions have different scopes; the latter is not a ban on safety withdrawal. This is the publisher’s policy artifact, not a formal standard or verified enforcement result. [S-08; GDR-SRC-20261010-G19-014]

For a reusable design proposal, explain permitted role deception, prohibited personal targeting, help/report routes and the right to stop before play. During play, enable discussion of claims and actions without presenting access needs or mannerisms as reliable guilt signals. The aim is not to remove every uncomfortable game decision; it is to avoid making social exclusion an unexamined substitute for strategic uncertainty. A group that does not want adversarial roleplay may be better served by cooperative asymmetric inference than by a softened accusation game. [S-02, S-12, S-14]

## Applying shared topics

Inspected **P02-PAT-02**, *Fact-preserving cue alternatives*, and **P02-TOP-03** transfer directly to hidden-role information: preserve facts, timing, uncertainty **and recipients**. Readable private text must not be broadcast to all players as an accommodation shortcut. The unresolved **P01-PAT-01/P02-PAT-02** overlap remains; it is not independent corroboration. **P01-TOP-03** also applies to joining, private setup, action and recovery, with its reviewed numerical accessibility scope unchanged. [S-09, S-10]

Inspected **F01-TOP-03** and corrected **F01-PAT-01** support neutral same-rule learning checks. Teach what a vote legally does using contrasting public examples, without teaching a strategy by revealing the real hidden assignment. Do not infer understanding from always repeating “accuse” or from correctly guessing a role once. **F02-TOP-02** separates strategic challenge, communication access and the punishment of exclusion; **F07-TOP-01/TOP-02** preserve outcome separation and safe-exit questions. [S-11, S-13, S-14]

Selected reviewed multiplayer/social systems, session structure, localization and detailed information-governance dependencies are missing from the inspected subset. Their proposed owner links remain in the [packet](../reviews/full-run-20261010-g19-review-packet.md#missing-dependencies); no later-wave author draft is silently treated as reviewed. [S-15]

## Pattern selection and adaptations

Use **GDR-CAND-20261010-G19-PAT-02**, [Post-elimination participation contract](../patterns/post-elimination-participation-contract.md), where loss of an active role creates an ongoing participation decision. Adapt influence, knowledge and channel permissions to the exact role set. Do not impose it where the round ends together or the chosen experience includes an optional break. It does not claim that continued participation always creates belonging. [S-11]

Use inspected **P02-PAT-02** for alternative cues and **F01-PAT-01** for rules comprehension, preserving secret state. A [party](party.md) hybrid must reconcile entry/exit with role secrecy: a recap for a returning participant may be appropriate only for facts they are entitled to know. A rhythm/social-deduction hybrid could turn motor access differences into apparent suspicion; treat that as a design hypothesis to challenge, not a claim about any shipped game. [S-09, S-10, S-12, S-13]

## Representative and contrary cases

| Inspected source | Decision exposed | Inference to resist |
|---|---|---|
| Clocktower Rules Explanation, oldid=1310 | Reliability conditions, a neutral Storyteller, and participation after death. [S-03] | System-delivered information is always true; death always means silence; every script follows the same exceptions. |
| Among Us overview and v2023.7.11 Quick Chat update | Action observations and structured communication. [S-04, S-05] | Spoken confidence is required or reveals genuine honesty. |
| Among Us Influencer v19.0.0 announcement | Intentionally constrained ghost-to-living communication. [S-06] | All ghost information transfer is forbidden, or the exception permits unrestricted revelation. |
| One Night publisher summary | A no-elimination/no-moderator alternative. [S-07] | Sequential player removal or a human moderator is necessary for deduction. |
| Keep Talking remote instructions | Cooperative information asymmetry. [S-02] | Hidden information by itself makes a game social deduction. |

This is a boundary-oriented, English-language documentary sample. Builds, actual sessions, complete role configurations, moderation outcomes and effects on belonging were not observed. [S-15]

**Illustrative worked application—not a tested game:** A prototype has a private clue that can be unreliable under a declared rule. An accessible version repeats exactly the clue and its stated reliability condition to the recipient; it does not query the hidden truth and “correct” it. During discussion, a player can say “I received this signal” separately from “I think it proves this conclusion.” On elimination, the prototype offers either a predeclared limited-influence role or a break; any observer view that exposes secret state disables channels not authorized for that view. A different configuration might deliberately allow a restricted message instead, but that is an explicit rules variant requiring a fresh inference/balance review. A same-rule practice example uses different public signals requiring different legal predictions, never the live secret. [S-09–S-14]

## Accessibility, ethics, localization and production

Audit private setup, discussion, accusation, commitment, elimination and reveal as distinct access tasks. Communication alternatives may need persistent source labels, unambiguous referents and enough time to formulate a statement, but none has a universally correct timer. Preserve a nonpublic route for asking rules or access questions. A helper should explain the rules without confirming which roles exist or whether a particular player is truthful. [S-10, S-13, S-15]

Localization should preserve negation, uncertainty, role terminology and distinctions between “saw,” “was told,” and “infer.” A proposed linguistic audit should check whether grammar or a voice/text variant accidentally reveals hidden state; this is a potential failure mode, not an observed bug in a named title. Avoid culture-based claims about deception style. [S-09, S-10, S-12]

Consent should cover permitted fictional deception, accusation, recording/streaming, private-message handling and exit. Reports and access requests should not become new strategic evidence. Host/moderator labor, disputed rules, bad-faith accusations and recovery from mistaken disclosure require production ownership. A safer small-scope alternative may be an authored cooperative mystery or a single-round reveal rather than an under-supported adversarial community. No clinical claim, behavior diagnosis, legal compliance determination or enforcement guarantee is made. [S-12–S-14]

## Research questions and validation

All tests are **proposed, not performed**. Test groups require consent for the nature of deception; no covert collection, real-world deception study or personality profiling is authorized. Fix and report role set, familiarity, communication routes, moderator behavior and the particular reveal/exit rules. Analyze groups and repeated rounds appropriately; do not count each accusation as an independent person.

| Question / comparison | Procedure and measures | Confounds and falsifier |
|---|---|---|
| Does an alternative channel preserve strategic information? | Under matched scripted public/private signals, compare chosen communication routes. Ask participants to distinguish delivered signal, assertion, inferred truth and remaining uncertainty. | Phrase vocabulary, navigation, transcription delays and extra disclosure confound modality. Reject equivalence if a route loses a required qualifier or reveals hidden truth. [S-09, S-10] |
| Does post-elimination play preserve valued agency? | Compare a bounded role, voluntary observation/rest and a no-elimination variant where feasible. Record desired role, legal influence, information leakage, burden and preferred continuation separately. | Different win probabilities and role identities mean this is not a pure interface change. Reject a blanket inclusion recommendation if participants feel obliged to stay or deduction becomes trivial. [S-11] |
| Can rules help remain neutral? | Staff-only later walkthrough of private help requests followed by consented player evaluation. Use paired same-rule public examples with different answers. | Response timing or wording may disclose role existence. Stop and revise whenever the help route supplies hidden state not granted by the rules. [S-13] |
| Does the conduct/exit design bound social cost without removing desired strategy? | Compare clearly explained game-claim norms and private exit/report routes with the existing baseline; evaluate participant-defined comfort, agency, targeting and burden. | Prior relationships, conflict style, facilitator power and self-censorship affect responses. Reject “safe” claims when only the host reports success or people cannot disengage without retaliation. [S-12, S-14] |

## Coverage checkpoint and next discriminating question

Researched: contested scope; signal/truth/statement distinctions; accusation and commitment; elimination alternatives; structured communication; private information access; consent and recovery questions. Unresolved: executable versions, complete role/script rules, configuration balance, live remote latency, multilingual information leaks, repeated-group social consequences, moderation efficacy, representative voice/text access, and exact party/deduction boundary cases. The next question is **whether each participant can acquire, express and act on the intended uncertainty without unwanted disclosure or interpersonal coercion**. Contradictions `G19-X04` through `G19-X07` are retained as scoped distinctions and open tradeoffs, not universal resolutions.

## Claim ledger

Claim labels attach to the stated proposition, not every possible application of a cited title. An inference is not promoted to an empirical finding by borrowing a citation. Proposed tests are **not performed**.

| Claim | Proposition | Class | Sources | Locator / support and bridge | Confidence and scope | Open question / contrary case |
| --- | --- | --- | --- | --- | --- | --- |
| S-01 | Working scope centers on strategic inference about agents from incomplete information and potentially deceptive claims or actions. | inference | GDR-SRC-20261010-G19-011; GDR-SRC-20261010-G19-012; GDR-SRC-20261010-G19-015 | Compare role/information structures in primary descriptions; Definition and boundaries. | moderate: useful working scope, not a definitive genre essence | Bluffing without a central identity-inference task may sit at a contested boundary. |
| S-02 | Asymmetric cooperative information alone is not sufficient to establish adversarial social deduction. | inference | GDR-SRC-20261010-G19-010 | Defuser/Experts information split compared with opposing-team cases. | moderate: analytic distinction | A hybrid can add deception; classification follows the actual rules, not the interface. |
| S-03 | Clocktower’s base explanation permits false information under specified conditions and retains some participation after death. | observed-example | GDR-SRC-20261010-G19-011 | Day/night information explanation; death and ghost votes, lines 48–76. | high for revision 1310 rules artifact; role exceptions not exhausted | Do not infer that every narrator message is guaranteed truth or every dead role has identical permissions. |
| S-04 | Among Us’s overview ties tasks, observation, meetings and voting to opposed objectives. | observed-example | GDR-SRC-20261010-G19-012 | How to Play, crewmate and impostor sections. | high for documented overview; build/settings unknown | Overview is not a complete information-permission specification. |
| S-05 | A versioned Among Us update describes structured Quick Chat. | observed-example | GDR-SRC-20261010-G19-013 | v2023.7.11 Quick Chat section. | high for historical documented route; current implementation not tested | No universal voice requirement follows; expressive/linguistic parity remains unmeasured. |
| S-06 | The v19.0.0 Influencer announcement describes a constrained ghost-to-living picture-message ability. | observed-example | GDR-SRC-20261010-G19-016 | New Role: The Influencer / Message and settings, lines 31–58. | high for the role announcement; no runtime or effect validation | The exception is role/version-specific, not permission for unrestricted dead-player disclosure. |
| S-07 | One Night’s publisher describes a no-elimination, no-moderator structure. | observed-example | GDR-SRC-20261010-G19-015 | Opening product summary, lines 29–31. | high for product description; exact rulebook not inspected | Do not infer specific voting, role-change or tie resolution rules. |
| S-08 | Innersloth’s conduct policy separates permitted game deception from harassment and explicitly permits disengaging from harassment. | observed-example | GDR-SRC-20261010-G19-014 | Behaviour and Keep the Spirit of the Game. | high for policy wording; not a formal standard or enforcement proof | Role-dodging discouragement must not be treated as a ban on safety exits. |
| S-09 | Represent scenario truth, observed signals, player statements, reliability and disclosure permissions separately. | hypothesis | GDR-SRC-20261010-G19-011; GDR-SRC-20261010-G19-012; GDR-SRC-20261010-G19-016 | Different documented information rules motivate proposed representation; inspected P02-PAT-02 constrains audience/uncertainty. | moderate for diagnostic distinctions; low for outcome benefit | Can participants reason with the declared uncertainty without authoring an automatic lie detector? |
| S-10 | A communication alternative can preserve the intended information contract without preserving identical experience or expressive capacity. | inference | GDR-SRC-20261010-G19-013; GDR-SRC-20261010-G19-020 | Documented structured channel; qualitative access limits; inspected P02-TOP-03/PAT-02. | moderate for conditional distinction | Does changing channel systematically omit necessary qualifiers, source or timing? |
| S-11 | Compare continued participation, bounded influence and a no-elimination alternative rather than assuming one death model is inclusive. | hypothesis | GDR-SRC-20261010-G19-011; GDR-SRC-20261010-G19-015; GDR-SRC-20261010-G19-016 | Contrasting primary rule examples support alternatives, not comparative effectiveness. | low for recommendation efficacy | Could continued duties be unwanted, strategically distorting or cognitively burdensome? |
| S-12 | Accusation should be assessed as in-game inference, not used to diagnose honesty, personality or communication disability. | inference | GDR-SRC-20261010-G19-014; GDR-SRC-20261010-G19-020 | Policy boundary and contextual communication barriers do not establish real-world trait inference. | moderate for the evidence limit; local conduct design still proposed | Can the design reward reasoning without encouraging personal targeting or demeanor stereotypes? |
| S-13 | A neutral rules/access help channel can protect uncertainty only if its replies do not reveal hidden state inadvertently. | hypothesis | GDR-SRC-20261010-G19-011 | Private Storyteller questions and inspected F01/P02 principles motivate proposed protocol. | low: no intervention test | Does the help response disclose role existence, timing or legitimacy to other players? |
| S-14 | A consent, privacy and recovery plan should bound the social cost of deception and accusation. | hypothesis | GDR-SRC-20261010-G19-014 | Publisher conduct principles plus inspected F07-TOP-02; not a BHS-approved policy. | moderate for identifying risks; low for prevention effectiveness | Are refusal, withdrawal and reporting usable without forced disclosure or retaliation? |
| S-15 | Role-set configuration and group context need separate investigation; no universal group size, discussion timer or role formula is supplied. | inference | G19 reasoning / inspected dependencies | Limited inspected rules range, no comparative group-size evidence or performed tests. | high for absence of supporting evidence in G19 | What configuration-specific probabilities, agency and access constraints matter locally? |

## References

All access dates are **2026-10-11 UTC (2026-10-10 America/Los_Angeles)**. The observer is this G19 authoring session. Document observations are observations of the cited artifact, not runtime gameplay. Public works are paraphrased; copyright remains with authors/publishers, and redistribution licenses were not audited. No screenshots, source text copies, music, rulebooks or participant data are redistributed. Source IDs are temporary; cross-batch/global deduplication by URL/DOI/edition remains pending.

### GDR-SRC-20261010-G19-010

Steel Crate Games. **How to play remotely**. Keep Talking and Nobody Explodes official site. Publication/update: unknown. [Inspected source or recorded lead](https://keeptalkinggame.com/how-to-play-remotely/). Edition/build: remote-play guidance; game/manual edition unknown. Access: `relevant-excerpt`. Type: developer instructions. Locator: Defuser/Experts information separation, lines 19–21 and 31–50. Supports: S-02. Limits: Asymmetric cooperative information is documented, not deception by opposing players. Alternative communication is a G19 proposal, not a verified shipped mode. Independence: Independent creator context from Jackbox and Innersloth.

### GDR-SRC-20261010-G19-011

The Pandemonium Institute / official Blood on the Clocktower wiki. **Rules Explanation**. Blood on the Clocktower official wiki. Publication/update: last edited 2023-04-03 01:12. [Inspected source or recorded lead](https://wiki.bloodontheclocktower.com/index.php?title=Rules_Explanation&oldid=1310). Edition/build: wiki revision oldid=1310; base rules explanation, not exhaustive role/script rules. Access: `full`. Type: official rules artifact. Locator: Day/night and information explanation, lines 48–62; The Four Rules, lines 63–71; death and ghost votes, lines 72–76. Supports: S-01, S-03, S-09, S-11, S-13. Limits: Rules inspected, no played session. Specific roles/scripts may qualify base rules; rhetorical claims about outcome frequency not adopted. Independence: Primary rules source; no independent effect evaluation.

### GDR-SRC-20261010-G19-012

Innersloth. **Among Us — How to Play**. Innersloth. Publication/update: unknown; live page. [Inspected source or recorded lead](https://www.innersloth.com/games/among-us/). Edition/build: overview, no exact build; detailed role exceptions require versioned sources. Access: `relevant-excerpt`. Type: developer game instructions. Locator: How to Play / crewmate and impostor objectives and actions, lines 112–191. Supports: S-01, S-04, S-09. Limits: Overview only. Does not define all settings, roles, private channels or ghost permissions. Independence: Same creator family as 013–014 and 016.

### GDR-SRC-20261010-G19-013

Chris D., Innersloth. **New Quick Chat is Here! v2023.7.11**. Innersloth. Publication/update: 2023-07-11. [Inspected source or recorded lead](https://www.innersloth.com/new-quick-chat-is-here-v2023-7-11/). Edition/build: v2023.7.11 announcement; not a current-build audit. Access: `relevant-excerpt`. Type: versioned developer update. Locator: Quick Chat update, phrase builder/categories/favorites, lines 38–52. Supports: S-05, S-10. Limits: Structured text route documented; no validation of expressive parity, reading access, translation quality or current account restrictions. Independence: Same creator family as 012, 014 and 016.

### GDR-SRC-20261010-G19-014

Innersloth, with Schell Games referenced for Among Us 3D. **Code of Conduct**. Innersloth. Publication/update: unknown; live revision. [Inspected source or recorded lead](https://www.innersloth.com/code-of-conduct/). Edition/build: live policy for Among Us / Among Us 3D; enforcement not audited. Access: `relevant-excerpt`. Type: first-party community policy artifact. Locator: Behaviour, lines 29–44; Safety & Privacy; Keep the Spirit of the Game, lines 60–73; Dealing with Unwelcome Player Interactions. Supports: S-08, S-12, S-14. Limits: A publisher policy, not a formal standard, BHS-approved policy, or evidence of enforcement effectiveness. Safety exits must not be conflated with role-selection dodging. Independence: Same creator family as 012–013 and 016.

### GDR-SRC-20261010-G19-015

Bezier Games. **One Night Ultimate Werewolf**. Bezier Games official product page. Publication/update: unknown. [Inspected source or recorded lead](https://beziergames.com/collections/all-games/products/one-night-ultimate-werewolf?mobile-app=true). Edition/build: product description; rulebook/app edition not inspected. Access: `relevant-excerpt`. Type: publisher product/rules summary. Locator: Opening description, parsed lines 29–31: hidden roles, one night/morning, no elimination or moderator. Supports: S-01, S-07, S-11. Limits: No downloaded rulebook, exact vote/tie rules, role swaps, app playback or actual session inspected. Marketing duration/group counts not generalized. Independence: Independent publisher context from Clocktower; no comparative efficacy evidence.

### GDR-SRC-20261010-G19-016

Chris D., Innersloth. **New Ghost Crewmate Role: The Influencer! | Emergency Meeting #44**. Innersloth. Publication/update: 2026-09-29. [Inspected source or recorded lead](https://www.innersloth.com/new-ghost-crewmate-role-the-influencer-emergency-meeting-44/). Edition/build: announced update v19.0.0; no executable inspected. Access: `relevant-excerpt`. Type: versioned developer update. Locator: New Role: The Influencer; Message ability and configurable settings, lines 31–58. Supports: S-06, S-09, S-11. Limits: Specified ghost-to-living message exception; source describes potential misinterpretation, not measured rates or validated inclusion. Do not infer every ghost has it. Independence: Same creator family as 012–014; later role-specific document qualifies overview rather than being independent proof.

### GDR-SRC-20261010-G19-020

Michael Crabb; Michael Heron. **Communication Challenges in Social Board Games**. Simulation & Gaming 54(5), SAGE. Publication/update: 2023-06-12. [Inspected source or recorded lead](https://journals.sagepub.com/doi/10.1177/10468781231183908). Edition/build: DOI 10.1177/10468781231183908; original open-access article. Access: `relevant-excerpt`. Type: original qualitative empirical research. Locator: Methodology—Participants, Lab Setup, Reflective Journal, Procedure; Results and five named themes; Limitations and Future Work, lines 87–189. Supports: S-10, S-12. Limits: Four sessions, 14 participants with hearing loss/deafness, eight returned journals. Novices, researcher presence, nonresponse and unnoticed distress limit inference. Abstract/body differ on theme count; no numerical effect of facilitation established. Independence: Independent research, including One Night and other tabletop games; cited background papers not separately inspected.

## Inspected shared-dependency records

These are **selected, parent-reviewed but unreleased draft bytes**, not newly validated public evidence. The original public sources behind them were not all reopened. Only the following scoped guidance transfers. Full receipt and missing links: [reviewed dependencies](../reviews/full-run-20261010-g19-review-packet.md#reviewed-dependencies). Dependency files are deliberately not reissued in this G19 delivery.

- **GDR-CAND-20261010-F01-TOP-03**, *Learning and onboarding*, version 0.1.0, revision `original`. Archive member `selected-drafts/topics/learning-and-onboarding.md`, lines 63–104. SHA-256 `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598`. Transfer: Separate rule understanding, input access, supported attempts and genuinely new applications.
- **GDR-CAND-20261010-F01-PAT-01**, *Supported attempt and transfer check*, version 0.1.0, revision `independent-review-correction-1`. Archive member `selected-drafts/patterns/supported-attempt-and-transfer-check.md`, lines 49–120; especially Recipe 77–94 and corrected example 98–120. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Transfer: Preserve same rule while varying correct responses; separate rule prediction from chosen preference and execution; never remove accommodations with hints.
- **GDR-CAND-20261010-F02-TOP-02**, *Challenge and difficulty*, version 0.1.0, revision `independent-review-correction-1`. Archive member `selected-drafts/topics/challenge-and-difficulty.md`, lines 61–99. SHA-256 `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1`. Transfer: Separate sensory, rule, planning, motor and social demands from failure punishment and recovery.
- **GDR-CAND-20261010-P01-TOP-03**, *Accessibility and inclusive interaction*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/accessibility-and-inclusive-interaction.md`, lines 56–103 and 243–265. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. Transfer: Task-chain access; preserve reviewed WCAG web/CSS scope and informative/vendor distinctions. No numerical defaults transferred.
- **GDR-CAND-20261010-P02-TOP-03**, *Multimodal communication*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/multimodal-communication.md`, lines 58–103. SHA-256 `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c`. Transfer: Preserve event facts, uncertainty, timing and audience; do not infer equal experience or broad benefit from extra channels.
- **GDR-CAND-20261010-P02-PAT-02**, *Fact-preserving cue alternatives*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/patterns/fact-preserving-cue-alternatives.md`, lines 50–138 and 264–270. SHA-256 `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0`. Transfer: Information contract, legitimate unknowns and channel loss; unresolved overlap with P01-PAT-01 retained.
- **GDR-CAND-20261010-F07-TOP-01**, *Evaluation and balancing*, version 0.1.0, revision `initial-capture-1`. Archive member `selected-drafts/topics/evaluation-and-balancing.md`, lines 65–93. SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`. Transfer: Define outcome/denominator and causal comparison; paper checks do not validate physical timing.
- **GDR-CAND-20261010-F07-TOP-02**, *Ethical and sustainable design*, version 0.1.0, revision `initial-capture-1`. Archive member `selected-drafts/topics/ethical-and-sustainable-design.md`, lines 70–125. SHA-256 `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0`. Transfer: Refusal/exit, consent and ongoing support/moderation costs remain design constraints, not proven effects.

## Review and history

Version 0.1.0; candidate revision `initial-draft-1`; initial bounded G19 capture, no predecessor or superseded submitted artifact. Exact bytes are identified in the review packet; wording changes retain this conceptual ID and require a new revision/receipt. Author self-review is recorded in the packet and is not independent review. Gate C is pending; only local static packaging checks are performed, not Gate D host tests; Gate E/release and game adoption are not authorized. Coverage remains open. The next decision is whether the independent reviewer accepts this bounded evidence treatment or requests specific corrections before Coordination considers further work.
