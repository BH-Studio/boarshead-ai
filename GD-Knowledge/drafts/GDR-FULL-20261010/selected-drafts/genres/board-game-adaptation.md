---
id: GDR-CAND-20261010-G17-GEN-02
kind: genre
title: Board-game adaptation
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
- digital board-game adaptation
- tabletop adaptation
- board-game port
tags:
- adaptation-fidelity
- automation
- hidden-information
- undo
- asynchronous-play
- social-negotiation
- coverage-open
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G17-PAT-02
- GDR-CAND-20261010-G17-PAT-01
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G17-GEN-01
source_ids:
- GDR-SRC-20261010-G17-008
- GDR-SRC-20261010-G17-009
- GDR-SRC-20261010-G17-010
- GDR-SRC-20261010-G17-011
- GDR-SRC-20261010-G17-012
- GDR-SRC-20261010-G17-013
- GDR-SRC-20261010-G17-014
- GDR-SRC-20261010-G17-015
reviewed_dependency_ids:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-P02-PAT-02
reviewer: null
approved_by: null
approved_date: null
---

# Board-game adaptation

**Complete bounded author draft; coverage remains open.** The principal recommendation is to maintain **separate accounts of rules fidelity and player experience**. Correct state transitions do not, by themselves, establish understandable, accessible or socially satisfying play; preserving every manual operation does not establish those outcomes either. This is conditional synthesis, not a released adaptation standard. [C-01, C-07, C-08]

## Definition and boundaries

For this library, **board-game adaptation** means a digital or digitally mediated playable implementation that presents an identifiable tabletop game as its source. It is a cross-cutting adaptation category, not one core mechanic. Its distinctive research obligation is to say **which original rules, edition, modules and interaction practices it preserves, changes, adds or omits**. A digital original with a board-like interface does not incur the same source-edition comparison merely by looking like a board game. [C-01]

Distinguish a rules-enforced adaptation, an open physics/sandbox recreation, a companion that handles only part of a physical game, and a deliberate digital variant. None is automatically the most faithful or accessible in every relevant sense. Tabletop Simulator’s official description includes object manipulation and optional scripting: it is a countercase to treating digital tabletop play as necessarily comprehensive automated adjudication. No specific community module was inspected. [C-06; GDR-SRC-20261010-G17-014]

Player count, live or asynchronous play, remote or co-located use, competitive or cooperative objectives, and device/input choice remain facets. House rules, expansions and digital-only scenarios need explicit scope rather than an assumption that one implementation covers “the board game.” A card-game adaptation can also require the [collectible card game](collectible-card-game.md) access analysis, but a digital purchase or cosmetic collection alone does not prove unequal functional card access. [C-01, C-21]

## Decision and scope

This entry helps choose what to preserve, automate, explain, expose, postpone, or make recoverable. It covers rule-version provenance, automated resolution, hidden information, commitment/undo, social negotiation, asynchronous timing, teaching, accessibility, localization and production evidence. It does not deliver an executable rules engine, a rules-complete comparison for any named adaptation, licensed assets, or a platform certification. [C-01, C-07, C-16]

The original-rule evidence is the **English 2020 Dune: Imperium base-game rule artifact**, inspected through a mirror. Digital evidence covers **Dune: Imperium Digital 1.5**, **4.0.1–4.0.8**, and **4.1.0** release notes, plus **Spirit Island** developer documentation with unknown exact client builds. These are **not** a matched original/digital conformance dataset. In particular, 2020 base rules are not silently applied as the oracle for every Uprising-era module, and the Spirit Island original manual could not be read. [C-02–C-05, C-16]

## Custom research instructions

Begin future research with a **version tuple**: original game/printing, errata date, included expansions/scenarios, digital build, platform/input, locale, participant/AI configuration, timing mode and declared variants. Record the provenance of each component. “Latest” without a checked identity is not a reproducible observation. Describe official patch notes as developer reports until behavior is reproduced in the named build. [C-02, C-03, C-16]

Build an action-level comparison around the questions that matter to the chosen adaptation: when a choice is legal; what may be known; who chooses an effect’s order; when costs are paid; when another player can respond; and what ends the opportunity. Consult original rules and errata before interpreting a digital restriction as an error. Keep a **deliberate variant**, a **shared tabletop erratum**, a **presentation substitution**, and a **defect** in different categories. [C-04, C-07]

Seek representative contrasts rather than one successful port: automatic versus manual adjudication; hidden versus public state; negotiation-heavy versus solitary calculation; cooperative simultaneous planning versus competitive commitment; experienced tabletop players versus digital-first learners; live versus asynchronous participation; small-screen and nonvisual access versus desktop pointing. These are proposed coverage dimensions, not supported estimates of audience composition. [C-19, C-20]

Challenge misleading comparisons: speed is not identical to enjoyment; fewer input errors is not rules understanding; a detailed action log is not automatically an authorized information channel; and a tabletop expert’s complaint can concern an intended digital variant rather than a bug. Conversely, calling a restriction intentional does not prove that players understand or prefer it. [C-07–C-09, C-12, C-20]

## Player promises and varied audiences

Possible promises include playing a familiar ruleset with distant friends, reducing setup/adjudication burden, learning without a table expert, practicing alone, preserving negotiation, or fitting moves around interruptions. These can conflict. A player who values physical handling and conversation may reject pacing that another player values for efficiency. A returning tabletop expert may need a **difference explanation**, while a digital-first learner needs an adequate model of the actual available game rather than the entire tabletop history. [C-12, C-20]

These are audience hypotheses. The research does not establish that all board-game players want maximum fidelity, asynchronous play, manual bookkeeping, or fast automation. Choose and test the particular promise; do not generalize a product’s convenience claims into a genre law. [C-08, C-11, C-20]

## Characteristic loops and structures

### Rule action, resolution, interpretation, next commitment

A useful analytical loop is **inspect permitted state → propose an action → validate/pay/commit according to the rules → resolve automatic and chosen effects → interpret the change → continue or recover**. A digital adaptation introduces distinctions between a selected action, a submitted action, an acknowledged action and a resolved action. The interface must not imply certainty about a move whose authoritative acceptance is still unknown. This is an inference about the contract, not a prescribed network implementation. [C-07, C-09, C-16]

The Dune base rules provide a narrow original example: an Agent action depends on a matching access icon, an unoccupied destination and costs paid before effects. Automated validation could enforce those relations while still leaving the player unable to explain a rejection. The first sentence is an inspected rule observation; the second is a testable design concern, not a demonstrated failure in the shipped client. [C-02; GDR-SRC-20261010-G17-008; C-12]

### Separate fidelity from experiential outcomes

| Question | Evidence required | What a pass would not establish |
|---|---|---|
| Are the stated actions and outcomes faithful? | Identified original clauses, declared variants and matched digital state transitions | Social equivalence, understanding, access or enjoyment |
| Are required choices retained? | Order-of-resolution and timing cases, including simultaneous/conflicting effects | That players find those choices easily |
| Is permitted information usable without extra disclosure? | Role-specific views, logs, speech, reconnect and spectator checks | Identical emotion, skill or response time across modalities |
| Is the intended social experience supported? | Relevant participant groups and comparisons of negotiation/conversation opportunities | That manual chores are necessary or that faster play is always worse |
| Can intended players participate? | Complete-task evaluation with relevant access needs and devices | Universal accessibility or a legal compliance determination |

This is a proposed decision framework [C-07, C-09, C-13], not a formal standard or a record of executed tests.

### Automation: remove work only after identifying its function

Classify an operation by what it currently does: deterministic bookkeeping; consequential choice; information disclosure; joint acknowledgement; or an opportunity for interaction. Then select automation granularity. A calculation with no discretionary branch may be automated while preserving an inspectable explanation. An ordering choice should not disappear merely because one order is easier to implement. A negotiated commitment needs a social policy, not simply an automatic next-phase button. [C-07, C-08, C-21]

**Independent evidence, narrowly stated:** Xu and colleagues observed social interaction around bookkeeping and rule-related activity in eight sessions involving nine distinct university computer-science participants aged 21–33. The study was qualitative, not a randomized comparison of automated and manual versions; it does not establish that removing chores causes a loss of sociality in remote adaptations. Their recommendation to consider the social function of chores is an interpretation, not an additional experiment. [C-14, C-15; GDR-SRC-20261010-G17-015, pp. 5–9, 12–13]

The practical inference is to compare **automatic resolution with enough explanation and optional interaction space** against other appropriate designs, rather than preserve friction for its own sake. Too much animation can impede access or delay play; no explanation can hide consequential changes. Neither extreme is proven superior by this source set. [C-08]

### Hidden information, conflict and recovery

An authorized information model is stricter than “show the board.” Identify whose knowledge each hand, face-down token, random result, pending offer and private plan may enter. An action log that reveals a hidden item before its rule-permitted disclosure changes the game even if the board graphics are correct. A read-aloud channel should not infer and announce a concealed fact merely because it can access it internally. [C-09; DEP-P01-INFO; DEP-P02-CUES]

Undo involves **state, information and other people’s actions**. Refunding a cost does not erase a revealed outcome or another player’s strategic response. A deterministic move can also communicate intent once shown publicly. Therefore a recovery design should specify the commitment/disclosure boundary, the role of consent and what is never restored. [C-09, C-10; DEP-F02-DEC]

Handelabra documents information-limited Spirit Phase undo and simultaneous multiplayer conflict handling. This is a feasibility/example source, not validation of this packet’s generalized undo recipe. Its documented online mode is live; it is not evidence of asynchronous support. [C-05; GDR-SRC-20261010-G17-013]

### Asynchronous timing and social negotiation

An asynchronous adaptation must decide when a decision becomes active, what starts a clock, whether waiting for a clarification pauses it, who may extend it, how notifications are delivered, and what happens after expiry or reconnect. Optional negotiation can become practically unavailable if a deadline assumes immediate replies. This is a conditional risk model, not a claim that one deadline is appropriate for every group. [C-11, C-21]

At re-entry, a player may need the public changes since their last acknowledged state, their current permitted private information, pending decisions and actual deadline basis. Do not expose private alternatives that were never committed or silently treat a notification as acknowledgement. A live cooperative variant may prefer joint pause or reassignment; a competitive asynchronous variant may require pre-agreed timeout outcomes. These are alternatives to test, not features attributed to every named product. [C-09, C-11]

The historical Dune 1.5 notes include asynchronous-turn notification fixes, establishing that such cases belong in its reported production context. This does not supply numerical clock rules or demonstrate successful re-entry. The inaccessible Board Game Arena FAQ is not used to fill those gaps. [C-03; GDR-SRC-20261010-G17-009]

## Practical choices and application process

1. **Write the adaptation contract.** Name the source version and the chosen promise. Mark unsupported modules and intentional changes rather than claiming “exact adaptation” globally. Stop a fidelity comparison when its original clause cannot be inspected. [C-01, C-07, C-16]
2. **Select discriminating rules cases.** Include legal and illegal actions, optional ordering, hidden reveals, simultaneous conflicts, victory/end conditions and interruption. A simple successful turn is insufficient. [C-07, C-09, C-19]
3. **Assign each operation an interaction policy.** Preserve a player choice; automate deterministic work; expose a relevant explanation; negotiate a joint decision; or defer unresolved adjudication. The simplest acceptable version may be a readable summary rather than a cinematic recreation. [C-08, C-21]
4. **Specify the knowledge and commitment boundary.** Determine what is private before submit, what becomes visible on acknowledgement, and what can be recovered. Unknown or conflicting state should not generate an invented success message. [C-09, C-10, C-16]
5. **Design teaching and re-entry separately.** Teach the current game; offer tabletop differences to those who need them. Retain necessary access supports when varying a same-rule example. Announce an actual rule change before testing its use. [C-12; DEP-F01-PAT]
6. **Evaluate fidelity and experience with separate observations.** Record rule outcomes, interpretation, interaction opportunities, access barriers and preference. Do not merge them into an unexplained quality score. [C-07, C-13, C-19]
7. **Recheck at version changes.** Reopen affected undo, tutorial, localization, save/replay and multiplayer cases. Freeze or visibly constrain unsupported combinations instead of implying untested parity. [C-16]

## Applying shared topics

| Inspected related identity | Genre-specific adaptation of shared guidance |
|---|---|
| `GDR-CAND-20261010-F02-TOP-01` — Decision design | Restore resources only where disclosure/commitments permit; hidden-state restoration and forgotten knowledge are not equivalent. [DEP-F02-DEC] |
| `GDR-CAND-20261010-P01-TOP-02` — Interface and information | Show rule-relevant reasons, pending acceptance and public history rather than every internal state. [DEP-P01-INFO] |
| `GDR-CAND-20261010-P01-TOP-03` — Accessibility and inclusive interaction | Evaluate the adapted task end to end, including private information and timed responses. Scoped web criteria do not dictate a universal game control size. [DEP-P01-ACCESS] |
| `GDR-CAND-20261010-F07-TOP-01` — Evaluation and balancing | Test conformance separately from understanding and social outcomes; expertise and group relationships affect interpretation. [DEP-F07-EVAL] |
| `GDR-CAND-20261010-F07-TOP-02` — Ethical and sustainable design | Leaving a shared session can affect others, but completion incentives also need interruption and access review. [DEP-F07-ETHICS] |

Selected reviewed **multiplayer/social**, **session/re-entry**, **localization**, and broader **platform/display** files are unavailable as verified dependencies here. Current selected third-wave bytes are not established by old author-packet pointers. Their guidance is not silently imported.

## Pattern selection and hybrid conflicts

The main new candidate is [Information-bounded undo](../patterns/information-bounded-undo.md), `GDR-CAND-20261010-G17-PAT-02`. It narrows the existing `GDR-CAND-20261010-F07-PAT-02` commitment/exit concern to recoverability under information disclosure and shared-state dependencies. It is not authority to override tabletop rules or a competitive event’s policy. [C-10]

[Access-normalized trial pool](../patterns/access-normalized-trial-pool.md), `GDR-CAND-20261010-G17-PAT-01`, may fit an adaptation where content access prevents experimentation, but normalizing components can change scenario difficulty, expansion interactions or an intended drafting process. A small supplied scenario may be a more faithful learning aid than every expansion at once. Ownership/sharing permissions require separate product-specific verification. [C-21]

The inspected `GDR-CAND-20261010-F01-PAT-01` helps separate copying an enabled action from understanding the rule. The inspected `GDR-CAND-20261010-P02-PAT-02` constrains alternative cues to the same permitted facts and uncertainty. Do not use either as evidence that tutorial completion or duplicated cues established learning or accessibility. [C-12, C-13]

For a negotiation-heavy adaptation, automatic offer acceptance may destroy a meaningful social commitment. For a solo optimization adaptation, preserving pauses solely to imitate a social table may impose unwanted overhead. For a competitive deduction game, a detailed undo history can disclose attempted private strategies. These are conditional hybrid conflicts requiring actual rule and audience evidence, not independent genre research completed by G17. [C-08–C-11, C-21]

## Representative cases and negative cases

| Case and inspected version | What it actually contributes | What must not be inferred |
|---|---|---|
| Dune base-rule artifact, copyright 2020 | A specific original rules reference for selected action constraints and in-run deckbuilding | Exact match to Uprising, all supplements, every erratum or a currently installed digital build [C-02] |
| Dune Digital 1.5 and June 2026 notes | Developer records of warnings, undo/resource, localization and interaction corrections | Frequency of bugs, completeness of fixes or resulting satisfaction [C-03] |
| Dune Digital 4.1.0, September 30, 2026 | A completion-oriented reputation mechanism and an explicit known-issues list | Improved completion, fair treatment of every disconnect, or complete rules correctness [C-17] |
| Spirit Island difference FAQ, build unknown | Developer distinguishes intentional differences and shared errata from an accuracy aim | Verified one-to-one conformance with an inspected original edition [C-04] |
| Spirit Island multiplayer documentation, build unknown | A documented information boundary and live simultaneous-play constraints | Current reproduction, generalized undo efficacy, or async support [C-05] |
| Tabletop Simulator About, build unknown | Sandbox interaction and optional scripting as an alternative adaptation route | Any specific module’s rules, permissions, accessibility or rights [C-06] |

The Spirit Island FAQ’s integrated Aspects are a presentation change; its fixed ordering for a specified Spirit is a rules difference; its Blight correction is presented as tabletop errata too. Those categories should not be collapsed into a single fidelity score. This classification follows the developer document; exact tabletop pairing remains unavailable. [C-04; GDR-SRC-20261010-G17-012]

### Illustrative worked adaptation: a public route and hidden cargo

**Invented teaching scenario; not a commercial game or test result.** A player selects a route, pays two food, then reveals a cargo token. The public map shows route costs and occupancy. The hidden cargo is legitimately unknown until commitment. [C-07, C-09]

Before a selection is published, a preview can show the selected route, cost and known public consequences. The player may revise it under the scenario’s proposed policy. Publishing the route itself can reveal strategy, so “no random result yet” is not sufficient to promise private reversibility. At commitment, the cargo is revealed and the result becomes new knowledge; a resource refund cannot make that reveal unobserved. A pre-commit warning can state that this step reveals unknown cargo without predicting which cargo exists. [C-09, C-10]

Suppose a second player has offered a trade contingent on the route. The adaptation must distinguish an informal message from an accepted game commitment. It cannot silently cancel the second player’s accepted action while labeling the first player’s undo “local.” In an asynchronous version, the design must say whether the offer survives a timeout and show that policy before anyone relies on it. These are proposed contractual choices, not universal board-game rules. [C-10, C-11, C-21]

For learning, vary occupancy or available food while preserving the same rule and ask which routes are legal before asking which is preferred. If a later edition changes the cost rule, identify that as an update; it is not a same-rule transfer trial. No success rate or mastery threshold is assumed. [C-12; DEP-F01-PAT]

### Strong countercases

A group may deliberately permit hindsight undo in a cooperative teaching session. That can be a valid declared variant, but it does not demonstrate information-preserving recovery and should not be merged with competitive statistics. Conversely, an event may forbid all post-submit undo; improving private previews and accessible confirmations can be appropriate without changing that policy. [C-10, C-21]

A sandbox group may value manual adjudication and house rules. This challenges an “automate everything” prescription, but does not justify forcing manual bookkeeping on players for whom it blocks participation. Similarly, optional social pacing must be tested against players seeking quick solo practice. [C-06, C-08, C-13, C-20]

## Accessibility, localization, ethics and production

**Access is a complete task.** Examine selecting and inspecting pieces without mandatory precision dragging; navigating a spatial board in a nonvisual representation; distinguishing public and private facts; understanding automatic changes; requesting help or pause; and reconnecting without losing an intended decision. Provide candidate alternatives to color-only ownership and motion-only feedback. Preservation of facts does not promise equivalent emotion, pace or competitive performance. No accommodation was tested in G17. [C-09, C-13; DEP-P01-ACCESS; DEP-P02-CUES]

**Localization is rules work.** Maintain optional/mandatory language, event order, owner/target references and consequences when text expands or changes direction. Named card definitions, icons, logs and tutorials must describe the same selected version. Report a missing translation or unresolved ambiguity instead of guessing an adjudication. Developer notes on localized UI and prompts justify inspecting these cases; they do not validate a general solution. [C-03, C-16]

**Respect social participation and interruption.** Completion incentives can reflect a legitimate desire to protect others’ time, yet can impose costs on players with unstable connectivity, caregiving duties or access barriers. Treat that tension as an open design question rather than proof that every departure is misconduct. Separate voluntary surrender, involuntary disconnect, negotiated stop and recoverable absence in proposed evaluation. No legal or moral classification of users is inferred. [C-17, C-18]

**Production costs follow the preserved contract.** Optional ordering, simultaneous actions, undo, saved state, reconnect, content modules and localization interact. A versioned case matrix is a proposal for controlling scope, not a tested architectural solution. Dire Wolf’s June notes and later known issues supply reasons not to infer exhaustive correctness from a patch label. Rights to publicly read a rulebook do not constitute approval to redistribute its cards, art or substantial text; this package contains paraphrases only and grants no implementation or publication rights. [C-03, C-16]

## Research questions and proposed validation

**No player tests, client tests or prototypes were performed.** These protocols require a separately approved implementation/recruitment plan. Sample size, duration and acceptance bounds must follow the actual question and variance, not a genre-wide default. [C-19]

| Test question | Proposed comparison and participants | Measures, confounds and falsifying result |
|---|---|---|
| Does automation hide consequential choices? | Manual/inspectable resolution versus summarized automatic resolution of the same specified state; tabletop experts and digital-first learners separately | Correct legal-action explanations, retained ordering choices, unwanted workload and preference. Prior knowledge and facilitator help confound learning. Reject an automation policy if it silently removes a required choice or leaves necessary consequences uninterpretable. |
| Can recovery correct input error without changing allowed knowledge? | Private preview/cancel, permitted bounded undo and a no-post-submit-undo condition | State restoration, disclosure history, strategic-information acquisition, partner-action invalidation and explanation of the boundary. Reject after any unauthorized new-information advantage or dependent-action corruption; usability gains do not excuse it. |
| Does asynchronous re-entry preserve a usable decision? | Acknowledged public-change summary versus current-board-only return in an explicitly timed scenario | Reconstructed public state, missed decisions, deadline understanding, unwanted notification load and private-info leaks. Delay length, memory and language differ. Reject a summary that reveals forbidden information or hides an active deadline. |
| Are interaction opportunities lost or merely changed? | Relevant groups compare alternative pacing/communication policies under otherwise matched rules | Conversation/negotiation opportunities, perceived agency, burden and ability to opt out; do not equate talk count with quality | Group familiarity, co-location and facilitator role are confounds. Reject universal social-benefit claims when relevant groups prefer different policies or effects are indeterminate. |
| Are access and localization routes actually usable? | End-to-end tasks with selected access configurations, locales and devices; do not remove accommodations for a control condition | Completion, error/recovery, workload, rule interpretation and unwanted disclosure | Expert assistance can conceal barriers. Reject a claim of equivalence when the authorized fact or action is not usable on a route. |

### Coverage checkpoint

| Area | Inspected coverage | Remaining discriminating question |
|---|---|---|
| Original rules | Selected base Dune rules, mirror; Spirit original manual inaccessible | Which exact original/errata tuple corresponds to the target digital mode? |
| Digital mechanisms | Documented differences, undo, warnings, fixes and live/async contexts | What does the actual installed build do in matched states? |
| Social effects | One small qualitative original study, plus proposed interpretation tests | Does automation change valued interaction for the chosen audience and setting? |
| Clocks and re-entry | Conditional design analysis; no current per-game deadline audit | What must each role know and when can it feasibly respond? |
| Access, ethics and localization | Reviewed dependency transfer and proposed task analysis | Which barriers persist in representative participant evaluation? |

## Claim ledger

`observed-example` here identifies an inspected artifact or developer documentation, not a personally observed game session. Abbreviated `G17-00n` source keys expand to `GDR-SRC-20261010-G17-00n`. Issue labels are local to the [batch packet](../reviews/full-run-20261010-g17-review-packet.md#contradictions-and-contested-boundaries).

| Claim | Class | Support / locator | Confidence and limit |
|---|---|---|---|
| C-01: This roster entry concerns an explicit relationship to an identified tabletop source | inference | G17-008 rule artifact; G17-012 difference FAQ; G17-014 platform description | Moderate working definition, not a universal genre partition. G17-ISSUE-01. |
| C-02: Selected Dune base rules constrain Agent legality and in-play deckbuilding | observed-example | G17-008, printed pp. 6–9; p. 15 provenance | Moderate: mirrored original, exact printing and publisher byte equivalence unverified. |
| C-03: Named Dune patches report warning, undo, interface and localization corrections | observed-example | G17-009 gameplay/fixes; G17-010 specified version sections | High for reported text; no reproduction or defect-rate conclusion. G17-ISSUE-04. |
| C-04: Spirit FAQ reports intentional differences, presentation changes and shared errata | observed-example | G17-012, opening, Blight Cards, Spirits | High for developer statement; no original-manual comparison. G17-ISSUE-04. |
| C-05: Spirit documentation describes information-limited undo and live simultaneous play | observed-example | G17-013, undo paragraph and General Multiplayer Information | High for text, client build unknown. G17-ISSUE-06. |
| C-06: Sandbox manipulation and optional scripting are an alternative route | observed-example | G17-014, opening/Create Games/Key Features | High for product description; no specific module audit. |
| C-07: Fidelity and experiential outcomes require different evidence | inference | G17-008/012; DEP-F07-EVAL; separate comparison matrix | Moderate, reasoned distinction; no universally sufficient checklist. |
| C-08: Automate by function and compare effects rather than assuming all chores are good/bad | hypothesis | C-07; G17-015 Discussion; proposed comparison | Low efficacy confidence; social transfer untested. G17-ISSUE-05. |
| C-09: Recovery, history and alternative presentation must respect the declared information/commitment model | inference | DEP-F02-DEC; DEP-P01-INFO; DEP-P02-CUES; G17-013 | Moderate: conditional contract, not a verified implementation. |
| C-10: Information-bounded undo may improve recovery without forbidden new-information advantage | hypothesis | G17-013; G17-010; PAT-02 causal chain | Low effect confidence; exact states and partner dependencies need testing. G17-ISSUE-06. |
| C-11: Explicit asynchronous clock/re-entry policy may preserve usable decisions | hypothesis | G17-009 async context; C-09; proposed protocol | Low: no inspected current deadline specification or user study. |
| C-12: Teach current rules and distinguish same-rule transfer from rule changes | hypothesis | DEP-F01-PAT corrected recipe; G17-008 selected clauses | Low for local learning effect; dependency correction preserved, not empirically validated. |
| C-13: Complete alternative-access routes require end-to-end evaluation | hypothesis | DEP-P01-ACCESS; DEP-P02-CUES; proposed tasks | Low for outcomes; no representative access testing. |
| C-14: Qualitative sessions included social activity around bookkeeping/rules | empirical-evidence | G17-015, pp. 5–9 | Moderate, narrow observational support; small single-network sample, not causal automation comparison. |
| C-15: The researchers argue for considering chores’ social function | practitioner-heuristic | G17-015, pp. 12–13 Discussion | Moderate as attributed research interpretation; not measured efficacy. |
| C-16: Versioned rules/content/locale/recovery cases are needed to assess a declared adaptation contract | inference | G17-008–012; DEP-P01-INFO; explicit tuple | Moderate, scope-control reasoning; no coverage guarantee or architecture approval. |
| C-17: Dune 4.1.0 reports completion-oriented reputation and unresolved issues | observed-example | G17-011, The Rep System; Known Issues | High for announcement; no completion or fairness result. G17-ISSUE-07. |
| C-18: Completion incentives and interruption/access needs may conflict | hypothesis | C-17; DEP-F07-ETHICS; proposed distinct departure categories | Low for prevalence/effect; no attribution of user intent from departure. |
| C-19: Proposed comparisons could discriminate specified failures under suitable controls | hypothesis | Test protocols; DEP-F07-EVAL | Low until performed; no sample-size, effect or reliability claim. |
| C-20: Different groups may value fidelity, sociality, speed or convenience differently | hypothesis | Source range and stated alternative goals; G17-015 only narrow context | Low for population distribution; no uniform genre expectation. |
| C-21: Hybrid access, negotiation and competitive policies require separate declarations | inference | C-01, C-07–C-11; related CCG draft | Moderate analytical scope; no full hybrid-genre evidence. |

## Review and history

Version **0.1.0**, `candidate_revision: initial-capture-1`; no predecessor or supersession. Author self-review challenged the idea that removing chores is always beneficial and the assumption that restoring visible resources is a safe undo. **Independent G17 review has not occurred.** Neither named adaptation is certified for rules fidelity, accessibility, social equivalence or current-build correctness.

Next decision: the parent reviewer should verify the distinction between original-rule evidence, developer reports and the new hypothesis, then decide whether PAT-02 is sufficiently narrow and nonduplicative to retain. Exact hashes and unresolved dependencies are recorded in the [lower-case review packet](../reviews/full-run-20261010-g17-review-packet.md). No repository, Project-source, engine, publication or release action follows from this draft.

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

### DEP-F07-ETHICS
**GDR-CAND-20261010-F07-TOP-02 — Ethical and sustainable design**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/topics/ethical-and-sustainable-design.md`; relevant locator: Agency, incentives and full cost; refusal/re-entry discussion.
**Transferred scope:** Disclosure is not proof of freedom from pressure; include time and exit costs. **Byte identity:** 49,049 bytes; SHA-256 `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-F07-EXIT
**GDR-CAND-20261010-F07-PAT-02 — Legible commitment and safe exit**, revision `initial-capture-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/legible-commitment-and-safe-exit.md`; relevant locator: Mechanism; context and recipe.
**Transferred scope:** Broad commitment/exit guidance; preserve consequences for other participants rather than promising consequence-free reversibility. **Byte identity:** 22,899 bytes; SHA-256 `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

### DEP-P02-CUES
**GDR-CAND-20261010-P02-PAT-02 — Fact-preserving cue alternatives**, revision `review-correction-1`. Owner is the dependency’s original domain, not G17. Inspected archive member `selected-drafts/patterns/fact-preserving-cue-alternatives.md`; relevant locator: Mechanism; recipe and factual-equivalence limits.
**Transferred scope:** Preserve facts, uncertainty, entitlement and timing, not a promise of identical emotion or performance. **Byte identity:** 27,103 bytes; SHA-256 `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0`. This is derivative research context; any G17 effect claim remains an inference or hypothesis unless separately supported.

## References

Access checked **2026-10-10, America/Los_Angeles** (retrieval session continued on 2026-10-11 UTC). Exact client builds are unknown unless a cited release note names one; release-note inspection is not client observation. `GDR-SRC-20261010-G17-*` are temporary source identities. Cross-batch URL/DOI/edition deduplication is pending Library Coordination. Lineage-only mentions of other batch source IDs resolve in the [review packet source ledger](../reviews/full-run-20261010-g17-review-packet.md#references); they are not additional supporting sources for this artifact.

### GDR-SRC-20261010-G17-008
**Paul Dennen (game design); Dire Wolf Digital (publisher). Dune: Imperium Rulebook and appended supplements.** Dire Wolf Digital; inspected copy hosted by 1jour-1jeu; publication/update: 2020 copyright; exact printing/revision of mirror unknown. [Source](https://cdn.1j1ju.com/medias/17/a9/6d-dune-imperium-rulebook.pdf).
- **Edition/build; locator:** English base-game 2020 rule artifact; 20-page PDF including supplements; not Uprising. Printed pp. 6–9: Deck Building, Agents, Intrigue Cards, Round Structure, Agent Turn; p. 15 credits.
- **Access/type/provenance:** `relevant-excerpt`; Original publisher rulebook, inspected through a third-party mirror. Original-rulebook text and screenshots of printed pp. 6 and 9 inspected at the mirror. Publisher discovery route: https://www.direwolfdigital.com/dune-imperium/resources/rules/ ; linked PDF: https://d19y2ttatozxjp.cloudfront.net/pdfs/DUNE_IMPERIUM_Rules_2020_10_26.pdf . No source PDF is redistributed.
- **Limits/independence:** Publisher site links to the dated CloudFront PDF, but that file timed out and the former direct asset URL returned 404. Mirror-to-publisher byte equivalence and exact printing are unverified. Not a paired rules-conformance test of Digital 4.x. Same original work despite multiple retrieval routes. Related Dire Wolf production family as G17-009–011, not independent corroboration.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-02, C-07, C-12, C-16.

### GDR-SRC-20261010-G17-009
**Dire Wolf Digital. Dune: Imperium Digital 1.5 Release Notes.** Dire Wolf Digital; publication/update: 2024-04-25. [Source](https://news.direwolfdigital.com/dune-imperium-digital-1-5-release-notes/).
- **Edition/build; locator:** Digital version 1.5; historical patch, not latest. Gameplay warnings and event-rule information; bug fixes for asynchronous prompts, reconnect/resignation, localization and interface.
- **Access/type/provenance:** `relevant-excerpt`; Developer release notes / observed documentation artifact. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Reports features/fixes, not independently reproduced failures or measured player benefits; no asynchronous deadline values are inferred. Same production family as G17-008,010,011; different versions, not independent replications.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-03, C-11, C-16.

### GDR-SRC-20261010-G17-010
**Dire Wolf Digital. Dune: Imperium Digital – June 2026 Patch Notes.** Dire Wolf Digital; publication/update: 2026-06-23 displayed; document covers several patches. [Source](https://news.direwolfdigital.com/dune-imperium-digital-june-2026-patch-notes/).
- **Edition/build; locator:** Versions 4.0.1–4.0.8; Uprising-era update; not current-build certification. 4.0.8 and 4.0.7 undo fixes; 4.0.5 resource restoration, tablet UI and gamepad fixes.
- **Access/type/provenance:** `relevant-excerpt`; Developer regression/fix record. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Reported corrections do not quantify defect frequency, prove all cases fixed, or establish current client behavior. Base-game 2020 rules are not the rules oracle for every included expansion. Same Dire Wolf production lineage as G17-008,009,011; repeated fixes are not independent effect studies.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-03, C-10, C-16.

### GDR-SRC-20261010-G17-011
**Dire Wolf Digital. Dune: Imperium Digital 4.1.0 Patch Notes – The Rep System Arrives!.** Dire Wolf Digital; publication/update: 2026-09-30. [Source](https://news.direwolfdigital.com/dune-imperium-digital-4-1-0-patch-notes-the-rep-system-arrives/).
- **Edition/build; locator:** Version 4.1.0 announcement; no installation or latest-build guarantee. The Rep System; UI/UX undo changes; Known Issues.
- **Access/type/provenance:** `relevant-excerpt`; Developer update and known-issues record. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Completion incentives are described, not shown to improve completion or to treat involuntary disconnects appropriately. The known-issues list prevents an all-correct claim. No precise reputation values are transferred. Same Dire Wolf production family as G17-008–010; source recency does not convert intent into outcome evidence.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-17; hypothesis context C-18.

### GDR-SRC-20261010-G17-012
**Handelabra Games. How is the digital version different from the physical version?.** Handelabra Games Help Center; publication/update: unknown absolute date; page displayed Last Updated: 202d when inspected. [Source](https://handelabra.helpshift.com/hc/en/3-spirit-island/faq/383-how-is-the-digital-version-different-from-the-physical-version/).
- **Edition/build; locator:** Spirit Island digital FAQ; client build and full tabletop/expansion version matrix unknown. Opening accuracy statement; Blight Cards; Spirits; Island Boards; Scenarios.
- **Access/type/provenance:** `full`; Firsthand developer difference/errata documentation. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Developer-reported intent and differences only. No matching original Spirit Island manual bytes were accessible here. Relative update age is not converted into an invented date. Same production organization as G17-013; not an independent audit of fidelity.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-04, C-07, C-16.

### GDR-SRC-20261010-G17-013
**Handelabra Games. Spirit Island Multiplayer.** Handelabra Games; publication/update: unknown; URL retains beta wording but body reports launch. [Source](https://www.handelabra.com/spirit-island-beta).
- **Edition/build; locator:** Steam, iOS and Android named by the source; exact client build unknown. Launch introduction; Spirit Phase undo paragraph; General Multiplayer Information.
- **Access/type/provenance:** `relevant-excerpt`; Official multiplayer and recovery documentation. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** Documents information-limited undo, live play and conflict handling. No current-client reproduction or benefit measurement; this is not an asynchronous-play source. Same production organization as G17-012; separate from Dire Wolf, but not independent validation of this packet’s undo recipe.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-05; mechanism context C-09/C-10.

### GDR-SRC-20261010-G17-014
**Berserk Games. About | Tabletop Simulator.** Berserk Games; publication/update: unknown; footer is not a publication date. [Source](https://www.tabletopsimulator.com/about).
- **Edition/build; locator:** Product description; build unknown. Opening description; Create Games; Key Features.
- **Access/type/provenance:** `relevant-excerpt`; Official sandbox product documentation. Public primary-source text inspected through web retrieval; no game client was run.
- **Limits/independence:** A platform with optional scripts is not one fully rules-enforced adaptation. Marketing claims about universal usability or permission tools are not accepted as access or moderation outcomes. Independent product organization; no inspected specific community module, rights grant, or controlled player evaluation.
- **Rights:** Copyright retained by the source owner; paraphrase and citation only. No source images, cards, or substantial source text are redistributed.
- **Claims supported here:** C-01, C-06.

### GDR-SRC-20261010-G17-015
**Yan Xu; Evan Barba; Iulian Radu; Maribeth Gandy; Blair MacIntyre. Chores Are Fun: Understanding Social Play in Board Games for Digital Tabletop Game Design.** DiGRA 2011: Think Design Play; publication/update: 2011; proceedings metadata lists 2011-01-01. [Source](https://doi.org/10.26503/dl.v2011i1.591).
- **Edition/build; locator:** 16-page proceedings paper. pp. 5–6 Methods; pp. 7–9 Findings, Chores; pp. 12–13 Discussion.
- **Access/type/provenance:** `relevant-excerpt`; Original qualitative observational research. DOI landing page and primary PDF https://dl.digra.org/index.php/dl/article/download/591/591 inspected as text. First-page screenshot succeeded; Methods/Findings screenshot attempts failed. No table/figure-derived result is used.
- **Limits/independence:** Nine distinct participants aged 21–33, eight sessions, university computer-science social network. Not a randomized automation comparison; no inference to all audiences or remote clients. Independent academic work. Its interpretation and design implications are not additional independent studies.
- **Rights:** 2011 authors/DiGRA notice permits personal and educational classroom use; commercial reuse requires permission. No PDF, screenshot, or substantial text is redistributed.
- **Claims supported here:** C-14 empirical observation; C-15 attributed interpretation; C-08 only a new hypothesis.
