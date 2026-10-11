---
id: GDR-CAND-20261010-G01-PAT-01
kind: pattern
title: Configurable threat consequences
version: 0.1.0
status: draft
owner_project: BH-GDR-Genres
run: GDR-FULL-20261010
batch: G01
identity_scope: run-scoped temporary candidate; not a permanent GDK allocation
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus supplied reviewed audio
  drafts
aliases:
- nonlethal threat mode
- reduced-consequence exploration
tags:
- consequences
- difficulty-options
- recovery
- agency
- accessibility
- conditional-recipe
related_topics: []
related_patterns: []
related_genres:
- GDR-CAND-20261010-G01-GEN-01
- GDR-CAND-20261010-G01-GEN-02
source_ids:
- GDR-SRC-20261010-G01-03
- GDR-SRC-20261010-G01-04
- GDR-SRC-20261010-G01-07
- GDR-SRC-20261010-G01-10
reviewer: null
approved_by: null
approved_date: null
proposed_owner_project: BH-GDR-Foundations-and-Systems; ownership review pending
---

# Configurable threat consequences

**Version 0.1.0 draft; hypothesis-led pattern, not validated or released.** Current drafting owner: BH-GDR-Genres. Proposed general owner: BH-GDR-Foundations-and-Systems, pending coordination. This is not a second audio pattern and does not depend on Contextual audio anomaly. [C-09–C-11]

## Purpose

Support a player-selected activity when a particular threat consequence—such as forced restart, lost supplies or repeated defeat—unnecessarily blocks it. Preserve only the threat presentation and interactions that still serve that activity. The goal is **a coherent, honestly described alternative**, not identical fear at lower difficulty. [C-04–C-06]

The central decision is whether to adjust a specific demand, change the consequence of failure, or offer a different activity altogether. A combat assist may address an aiming barrier more appropriately than removing combat. An exploration mode may deliberately change the activity and should be described as such. [C-03, C-08]

## Context and prerequisites

Use this candidate only when the designer can identify the unwanted barrier, the activity the player wants to retain and the consequences that can coherently change. A threat must have definable interactions and progression dependencies; “make it safe” is not a sufficient specification. The team must also be able to explain the resulting mode, preserve its selected state, and review foreseeable transitions. [C-04, C-07–C-09]

Before proceeding, distinguish these **proposed design dimensions**:

| Dimension | What is specified | Why the distinction matters |
| --- | --- | --- |
| Presentation and contact | Visibility, pursuit, proximity, interruption, collision, sounds and thematic content. | Nonlethal does not mean absent, passive, comfortable or nonconfrontational. |
| Harm and penalty | Health loss, inventory loss, defeat, forced rollback, time loss or other consequences. | Removing one loss can leave a different barrier intact. |
| Progression and recovery | How tasks advance, how blocked routes clear, what persists and how interrupted activity resumes. | A threat that cannot defeat the player can still prevent completion. |
| Access and chosen activity | Required information, control demands, reading opportunity and the activity retained or changed. | A reduced-consequence mode is not proof of comprehensive accessibility. |

These dimensions are an authoring aid, not a formal taxonomy or mandatory four-setting interface. Support a small number of coherent combinations rather than exposing every conceivable switch. [C-03, C-04, C-07–C-09]

**Exit before authoring:** do not use this pattern merely because a horror title is expected to offer a “safe” setting. First diagnose whether the problem is consequence burden, inaccessible information, precision demands, sensory discomfort or unwanted subject matter. A mode that changes only death cannot promise to solve the others. [C-05, C-08]

## Mechanism and evidence

| Proposed link | Actual support | Limit or disconfirming case |
| --- | --- | --- |
| A declared penalty is disabled → that particular loss no longer occurs. | Logical consequence of a correctly implemented rule; creator accounts describe nonlethal or reduced-risk alternatives. | No implementation was inspected here. Defeat may persist through another system or route. [C-01, C-02, C-07] |
| Less unwanted penalty → less avoidance/retry burden. | Plausible inference from the barrier model and official access goals; no inspected causal comparison. | Pursuit, theme or an input demand may be the actual barrier. [C-03, C-05] |
| Less barrier while meaningful interactions remain → access to the chosen activity. | Creator descriptions provide design precedents, not demonstrated usability. | Removing combat can remove the chosen activity, while a nonlethal creature can still block it. [C-01, C-03–C-05] |
| Retained threatening fiction → retained valued unease. | Practitioner intention only in this corpus. | Failure fear may diminish; the player may feel bored, reassured, curious or still distressed. Equal emotion is unestablished. [C-06] |

**Evidence boundary:** SOMA’s launch explanation and later Q&A disagree about attacks. Their common nonlethality claim supports a narrower precedent. Crow Country supplies a separate production’s reduced-risk alternative. Neither production is a controlled study, and the same SOMA account appearing in multiple entries is not additional evidence. [C-01, C-02]

## Recipe

All steps are **proposed and not executed**. No numerical setting, preset count, staffing estimate or affective outcome has universal authority here. [C-09]

### 1. Identify the barrier and retained activity

Write a concrete pair, such as “repeated loss of collected evidence interrupts investigation” and “the player wants to compare evidence while still encountering the threatening place.” Do not substitute “the player cannot handle horror.” Record whether the intended alternative is the same activity with adjusted demands or a genuinely different activity. [C-03–C-05]

**Adjust:** the target activity, unwanted consequence, relevant prior knowledge and acceptable remaining contact. **Exit:** when the barrier is access to a critical cue, first fix that information channel; when the themes themselves are unwanted, provide a truthful content description and exit rather than promising that a difficulty change will resolve them. [C-05, C-08]

### 2. Choose the least extensive viable intervention

Compare a targeted input/challenge assist, less resource loss, shorter rollback, a recoverable interruption, removal of lethal consequences, reduced pursuit, or a separate exploration activity. An unchanged mode remains a valid option for people who prefer its consequences. Do not make the alternate mode a hidden substitute for the one the player chose. [C-03, C-08]

**Adjust:** consequence severity, recovery distance, retained interactions and when settings can change. **Exit:** if a smaller assist addresses the stated barrier without changing a valued decision, prefer testing it before designing a new mode. This is a production-aware inference, not a proved efficiency ranking. [C-08, C-09]

### 3. Specify the changed rule and the invariants

For each retained threat, state what it can perceive and do, what happens on contact, which resources can change, whether it can obstruct routes, and how an interrupted task resumes. Define what remains unchanged: evidence availability, objective, required task facts, theme or other chosen invariants. Avoid an unqualified label such as “no danger” when pursuit, distressing content or a nonlethal interruption remains. [C-02, C-04, C-07]

**Adjust:** aggression, contact outcome, retreat behavior, interruption duration, resource recovery and mode-description wording. **Exit:** if the proposed description cannot accurately summarize the remaining consequences, revise the policy or choose a clearer separate activity. [C-04, C-08]

### 4. Audit progression before adding presentation polish

On a state diagram or paper table, trace entering a threatened area, completing or abandoning its task, exhausting supplies, being interrupted, changing mode where supported, saving, reloading and returning. Identify any transition that previously depended on defeat or resource loss. Define a coherent replacement, such as a retreat path or resumable task, rather than leaving the player permanently blocked. [C-07, C-09]

**Adjust:** persistence, checkpoint behavior, completion conditions and supported mode-transition points. **Exit:** when a required transition has no coherent replacement, do not ship that combination as though it were supported. Narrow the alternative’s scope or revise the task after separate implementation approval. No such work is authorized by this file. [C-07–C-09, C-11]

### 5. Explain choice and preserve access

Use neutral, specific descriptions of consequences and retained activity. Where a setting changes the activity, call it a mode rather than claiming equivalent challenge. Present the information early enough for the player to choose knowingly. Specify whether changes apply immediately, at a checkpoint or on a new start; do not imply that every option can be changed everywhere. [C-03, C-08]

Provide appropriate required-event information across the supported modalities. State explicitly that content intensity and consequence intensity are different. A player choosing reduced consequences need not want quieter sound, less complex puzzles or a less mature story; those are separate design questions. [C-03–C-05, C-09]

**Exit:** if the user cannot discover what changed, or a preferred access setting hides a required fact, revise before claiming that the alternative addresses the barrier. [C-03, C-09]

### 6. Review combined states and repeat exposure

Consider first play, informed replay, selected assists, alternate routes, depleted inventory and interruption. Avoid adding an untested combination for every independent parameter. Record unsupported combinations honestly. Repeated encounters may become familiar and useful; do not secretly restore a disabled consequence to recover surprise. [C-04, C-07–C-09]

**Adjust:** supported presets, permitted combinations, persistence and disclosure. **Exit:** when state combinations exceed the team’s capacity to verify them, reduce the supported set or use a simpler targeted change. No cost multiplier or mandatory preset count is implied. [C-07–C-09]

### 7. Compare the option against the actual alternative

After separate authorization, evaluate the chosen activity, barrier and experience separately. Do not demand equal fear as a condition of supporting an alternative whose purpose is to reduce failure-related fear. Conversely, do not call removal of a valued planning activity an accessibility success merely because completion becomes easier. [C-03, C-05, C-06, C-09]

**Exit:** remove or narrow the candidate when it does not address the stated barrier, introduces progression failures, conceals consequences, or leaves no valued activity. Prefer a targeted assist or explicitly different mode when that better fits the evidence. [C-08, C-09]

## Worked examples

### Illustrative example — hazardous-site survey

**Synthetic cross-genre example; not a game observation, prototype or player test.** A survey game asks the player to inspect structures in an unstable site. In its expedition mode, a roaming threat can interrupt a scan and force a return to the last shelter, losing unfiled measurements. The player must choose between another measurement and a costly retreat. Some prospective players instead want to inspect the site’s layout and compare its records without repeated loss. [C-09]

The proposed exploration alternative retains the route and visible threat but removes loss of filed and unfiled measurements. Contact interrupts the current scan, after which the threat withdraws and the scan can be resumed. A clearly marked retreat remains available. This is not “the threat cannot attack”; the descriptor states that contact and interruption remain but measurements are not lost. The player can also choose the original expedition mode. [C-02–C-04, C-09]

The paper audit finds a gate that previously opened only after a failed expedition. In the alternate activity, the designer must provide another coherent unlock condition or omit that alternate route from scope with an honest limitation. Simply removing defeat would otherwise leave the progression relationship undefined. This is an illustrative discovered design dependency, **not a defect found in an implemented game**. [C-07, C-09]

The simpler comparison keeps expedition decisions but banks measurements at shorter intervals. That may address repeat-loss burden while preserving more of the original tradeoff. The exploration alternative is warranted only if it serves the player’s desired activity better—not because it has a more permissive label. [C-03, C-08, C-09]

### Genre-specific use without duplicating the genre entries

In [survival horror](../genres/survival-horror.md), reducing loss may change the risk-management loop. Describe whether survival decisions remain or the alternative becomes exploration. In [psychological horror](../genres/psychological-horror.md), reduced bodily consequences may allow investigation while interpretive or thematic unease remains possible; this is not proof that the experience is suitable for everyone. No audio-context sequence is required in either adaptation. [C-04–C-06, C-10]

### Strong counterexample — a chosen one-attempt expedition

A player expressly chooses a short expedition whose central activity is deciding what to risk when return is uncertain. Removing all loss can remove that activity. A targeted input assist, more readable information or an optional separate exploration mode may be preferable to silently flattening the original consequences. The counterexample defeats a universal “always remove penalties” reading, not the legitimacy of an honestly offered alternate mode. [C-03, C-08, C-09]

## Tradeoffs and alternatives

| Alternative | Useful when | Limitation to evaluate |
| --- | --- | --- |
| Targeted input or challenge assist | The barrier is execution, not the risk decision. | May leave unwanted rollback or narrative interruption unchanged. |
| Shorter rollback or reduced resource loss | Players want the same interaction with less repeated work. | Can change the value of safe routes and resource commitments. |
| Nonlethal but interactive threats | Investigation remains valuable with confrontation retained. | Contact, pursuit, blocking and sensory intensity can remain barriers. |
| Passive or absent threats | The chosen activity does not require confrontation. | This may be a different mode, not equivalent difficulty. |
| Unchanged consequence policy | The audience knowingly values the existing stakes. | Does not answer access barriers; targeted support may still be needed. |
| Omit the threatening content or exit | The material itself is unwanted. | A consequence setting is not a substitute for truthful choice. |

These are proposed comparisons, not empirical rankings. Extra modes create description, localization, persistence and verification work. A small studio may reasonably support fewer coherent options rather than a large, poorly tested matrix; no staffing or cost threshold is established. [C-03–C-09]

## Failure cases and do-not-use conditions

| Future observable warning sign | What it would challenge | Proposed response |
| --- | --- | --- |
| A supposedly nonlethal mode still loses a resource on a secondary failure path. | The declared consequence policy is inaccurate. | Correct the rule or description and recheck dependencies. |
| A threat can indefinitely block an essential interaction. | Nonlethality was mistaken for usable progression. | Provide a coherent retreat/reset/alternate route or reject that mode. |
| The player still avoids the scene because of subject matter or motion effects. | The diagnosed barrier was incomplete or wrong. | Respect exit; evaluate presentation/content separately. |
| Completion increases but the chosen decision disappears. | An alternative activity was misrepresented as equivalent difficulty. | Rename and explain the mode, or prefer a targeted assist. |
| Switching mode silently restores a penalty or loses progress. | Choice/persistence semantics are unreliable. | Restrict transition points transparently and re-audit. |
| Alternate captions or descriptions reveal story facts prematurely. | Information changed unintentionally with mode. | Review wording and knowledge states, not only threat behavior. |
| Remaining contact is called “safe” although it is unwanted. | The label overpromises comfort or suitability. | Describe concrete consequences and remaining content without a safety guarantee. |

**Do not use** to conceal consequences, remove support after a player chooses it, replace required access information, promise emotional equivalence, or claim a medically safe experience. Do not offer a mode the team cannot verify for its declared scope. These are proposed design constraints and falsification signs, not events measured in this batch. [C-02–C-09]

## Playtest

**PROPOSED — NOT PERFORMED.** No mode, prototype, participant recruitment, preference survey or measurement exists as a result of this batch. The protocol below requires a separately approved study owner, content/consent review and implementation authorization. [C-09, C-11]

**Question:** does the selected consequence change address a stated barrier while preserving a valued, honestly described activity? Evaluate emotional differences; do not presuppose that they must disappear.

For the illustrative survey, compare A (exploration alternative with contact but no measurement loss) against B (shorter banking intervals with original expedition consequences). Keep route, objective, required-event information and threat presentation comparable where feasible; log remaining interaction and meaning differences. This compares strategies, not a pure fear manipulation. An optional original-mode reference is appropriate only for participants who voluntarily choose that content and risk profile. [C-03–C-06, C-09]

**Proposed formative allocation:** 12 consenting adults who identify repeat-loss as an unwanted barrier but value the site-survey activity; six A/B orders and six B/A orders using parallel sites. Include relevant access users at their chosen settings. The count covers orders and a bounded workload, not statistical power or a representative audience. People who decline a condition are not required to experience it; report incomplete comparisons and adapt the protocol rather than concealing selection limits. [C-09]

Before data collection, define the essential task facts, retained interactions, permitted interruptions and each mode’s promised consequences. Ask participants to explain the mode before and after play, identify any unexpected loss, describe their activity and rate barrier burden, agency, valued unease, curiosity, comfort and willingness to continue separately. Proposed 0–6 ratings are exploratory local settings, not validated norms. Record action explanations and progression failures; completion alone is insufficient. [C-05, C-06, C-09]

**Proposed local decision rule:** advance only for further review when at least nine of twelve participants can accurately describe A’s retained contact and removed loss, the median paired barrier-burden rating favors A by at least one point, and there is no critical progression or information-access failure. These are unapproved formative thresholds, not a statistical claim. Report individual differences and order effects. A participant valuing B is evidence about fit, not a failed participant.

**Reject or narrow** when the change fails to address the stated barrier, gains arise only from undisclosed differences, A removes the activity the participant wanted, or the mode cannot satisfy its declared consequence policy. Lower fear does not automatically reject a reduced-consequence mode; unwanted remaining intensity also cannot be relabeled as success. A small null result is inconclusive. Distress or withdrawal ends the session immediately without penalty. [C-03, C-05, C-06, C-08, C-09]

A later build-specific test of the SOMA documentation discrepancy would answer a different question and would not validate this general pattern. All host retrieval and participant tests remain **NOT RUN**. [C-02, C-09]

## Claim ledger

Claim IDs are local to this entry. Confidence refers to the exact stated scope, not prestige or popularity. `Hypothesis` does not become established by appearing in multiple files.

### C-01

**Claim:** Developer descriptions of SOMA and Crow Country document alternatives that reduce dangerous consequences while retaining some threatening setting or interaction. **Class:** `practitioner-heuristic`. **Confidence:** moderate for the descriptions; low for any general emotional benefit.

**Source/locator:** GDR-SRC-20261010-G01-03, GDR-SRC-20261010-G01-04, GDR-SRC-20261010-G01-07; 03 Safe Mode explanation; 04 Safe Mode answer; 07 final exploration-mode answer. **Evidence-to-application bridge:** These are precedents for separating consequences from presentation, not proof that an arbitrary game can do so successfully. **Limits/opposition:** 03/04 are one production and conflict on attack behavior; 07 is a distinct production. No builds or mode comparison were observed. **Unresolved:** Which activities and consequences actually differ in a specified build.

### C-02

**Claim:** SOMA’s nonlethal mode must not be represented as verified absence of attacks. **Class:** `inference`. **Confidence:** high for the documentary limit, unknown for build behavior.

**Source/locator:** GDR-SRC-20261010-G01-03, GDR-SRC-20261010-G01-04; 03 What is Safe Mode? versus 04 Why did SOMA get a Safe Mode?. **Evidence-to-application bridge:** Use the shared nonlethality claim while preserving the incompatible attack descriptions. **Limits/opposition:** Cannot reconcile provocation, version, creature type or imprecise wording without additional evidence. **Unresolved:** Resolve G01-CON-02 through dated build documentation or authorized observation.

### C-03

**Claim:** Official guidance recommends separating challenge options, while distinguishing different activities or game modes from equivalent difficulty options. **Class:** `practitioner-heuristic`. **Confidence:** high for attribution; local accessibility untested.

**Source/locator:** GDR-SRC-20261010-G01-10; Overview; Implementation guidelines, especially lines 109–155. **Evidence-to-application bridge:** A mode should describe what changes, rather than promise the same activity when a required interaction is removed. **Limits/opposition:** Vendor guidance is not a formal standard or certification; no emotional-equivalence finding. **Unresolved:** Which targeted adjustments preserve the desired activity for actual users.

### C-04

**Claim:** Define presentation, harmful consequence and progression/recovery separately before selecting a coherent configurable mode. **Class:** `inference`. **Confidence:** moderate for the design decomposition; its added value is unmeasured.

**Source/locator:** GDR-SRC-20261010-G01-03, GDR-SRC-20261010-G01-04, GDR-SRC-20261010-G01-07, GDR-SRC-20261010-G01-10; Creator mode descriptions and XAG 108 differentiated options. **Evidence-to-application bridge:** A player-facing threat can remain perceptible even when a specified loss condition changes; explicitly modeling the relationships makes the design decision reviewable. **Limits/opposition:** The dimensions interact. A nonlethal stalker can still block a door, interrupt a task or cause distress. Not every combination should be supported. **Unresolved:** Whether the decomposition identifies the barrier more usefully than an existing difficulty control.

### C-05

**Claim:** Removing a specified penalty may reduce avoidance or retry burden and permit a valued activity, but this outcome must be tested. **Class:** `hypothesis`. **Confidence:** low for local behavior; documentary precedents are not a causal comparison.

**Source/locator:** GDR-SRC-20261010-G01-03, GDR-SRC-20261010-G01-04, GDR-SRC-20261010-G01-07, GDR-SRC-20261010-G01-10; 03 gameplay difference; 04 behavior changes; 07 exploration alternative; 10 access goals. **Evidence-to-application bridge:** If that penalty is the actual barrier, changing it can plausibly let the player continue the selected activity. **Limits/opposition:** The barrier may instead be pursuit, sensory presentation, themes, reading, motor demands or unwanted content; removing death alone may not help. **Unresolved:** What barrier participants identify and whether the altered mode changes it.

### C-06

**Claim:** Retaining threatening presentation after reducing consequences may retain valued unease, but equal fear, accessibility or satisfaction is not established. **Class:** `hypothesis`. **Confidence:** low: no directly inspected controlled mode comparison.

**Source/locator:** GDR-SRC-20261010-G01-03, GDR-SRC-20261010-G01-04, GDR-SRC-20261010-G01-07; 03 Is the game still scary?; 07 exploration answer. **Evidence-to-application bridge:** Creators report an intention to retain atmosphere, which justifies an optional test rather than an effectiveness claim. **Limits/opposition:** Failure-related fear may change by design. A participant can value curiosity instead of fear, or reject the remaining content. **Unresolved:** Whether the chosen activity and experience are supported at preferred settings.

### C-07

**Claim:** A progression and state audit is needed when modifying consequences, including defeat-dependent transitions and resource recovery. **Class:** `inference`. **Confidence:** moderate for logical dependencies, unknown effort and defect frequency.

**Source/locator:** GDR-SRC-20261010-G01-04, GDR-SRC-20261010-G01-10; 04 Safe Mode behavior adjustments; 10 save/pause and differentiated challenge guidance. **Evidence-to-application bridge:** Removing a consequence does not automatically remove other dependencies that expected it to occur. **Limits/opposition:** No engine behavior or implementation defect was inspected. These are conceptual audit categories, not measured failure rates. **Unresolved:** Which transitions and persistence combinations exist in a later authorized design.

### C-08

**Claim:** Use the smallest transparent adjustment that addresses the actual barrier; omit the pattern when the premise cannot support a coherent alternate activity. **Class:** `inference`. **Confidence:** moderate as an evidence-limited decision rule, not an optimality theorem.

**Source/locator:** GDR-SRC-20261010-G01-03, GDR-SRC-20261010-G01-04, GDR-SRC-20261010-G01-07, GDR-SRC-20261010-G01-10; Creator accounts and XAG 108 distinction between modes and challenge. **Evidence-to-application bridge:** Unnecessary combinations increase authoring and explanation burden while potentially removing the intended decision. **Limits/opposition:** Some alternate modes are worthwhile specifically because they change the activity; label them honestly rather than forbidding them. **Unresolved:** Whether a targeted assist, shorter rollback or separate exploration mode is the better alternative.

### C-09

**Claim:** The recipe, illustrative scenarios, adjustable variables and proposed tests are original testable design specifications. **Class:** `hypothesis`. **Confidence:** low for eventual usefulness and sensitivity.

**Source/locator:** Current brief, inspected local inputs, or explicitly original synthesis as specified below; Original G01 synthesis in Recipe, Worked examples and Playtest. **Evidence-to-application bridge:** Specify a comparison and observable reasons to reject the option. **Limits/opposition:** No implementation, settings change, participants, playtest, survey or technical validation occurred. **Unresolved:** Later study-owner review, resources, measures, consent and feasibility.

### C-10

**Claim:** A general configurable-consequences pattern is distinct from an audio-context anomaly, but its cross-domain ownership remains pending. **Class:** `inference`. **Confidence:** moderate for conceptual distinction; no canonical ownership receipt.

**Source/locator:** GDR-SRC-20261010-G01-03, GDR-SRC-20261010-G01-04, GDR-SRC-20261010-G01-07, GDR-SRC-20261010-G01-10; Current pattern Purpose/Recipe; supplied contextual-audio pattern Purpose/Recipe; TAXONOMY.md domain boundaries. **Evidence-to-application bridge:** This recipe changes consequence policies and player-selected activities rather than recognizable sound relationships. **Limits/opposition:** Shared Challenge and difficulty and Session structure and retention topics are not available as researched dependencies. **Unresolved:** Library Coordination and Foundations and Systems should decide the canonical home and duplication risk.

### C-11

**Claim:** Doug authorized this temporary draft pattern within G01, not implementation, release or permanent ID allocation. **Class:** `studio-decision`. **Confidence:** high: explicit current user request.

**Source/locator:** Current brief, inspected local inputs, or explicitly original synthesis as specified below; Current G01 request, Optional justified patterns and action exclusions, 2026-10-10. **Evidence-to-application bridge:** Keep temporary identity and null approval metadata. **Limits/opposition:** No authorization to modify a repository, game mode or participant protocol. **Unresolved:** Independent review, ownership and later human decisions.

## References

Source identities below are run-scoped candidates, not global allocations. All listed public text was inspected on **2026-10-10**, with `access: relevant-excerpt`. Section titles are the durable locators; browser line ranges are supplemental. Linked media, game builds and raw datasets were not inspected unless explicitly stated. Source reuse is not additional corroboration.

### GDR-SRC-20261010-G01-03

**Thomas Grip. [What is SOMA’s Safe Mode?](https://frictionalgames.com/2017-11-what-is-somas-safe-mode/).** Frictional Games. **Publication/update:** 2017-11-30; page also displays 2023-10-10, change substance unknown. **Edition/build:** Safe Mode launch description; Xbox One/PC context, exact build unknown.

**Type/access:** Firsthand developer explanation; relevant-excerpt, 2026-10-10. **Locator:** What is Safe Mode?; Is the game still scary?; What is the major difference in gameplay?; Why release it now?; lines 8–21. **Supports:** C-01, C-02, C-04, C-05, C-06, C-08, C-10.

**Limits/relationships:** No measured mode comparison. Attack wording conflicts with 04; nonlethality is the common documented claim. Same production as 04, not independent evidence. **Rights:** Reuse license not verified; paraphrase only. No artwork, video, audio or full source text redistributed.

### GDR-SRC-20261010-G01-04

**Ian Thomas, interviewee; Frictional Games, compiler/editor. [Q&A with Frictional writer Ian Thomas](https://frictionalgames.com/2018-02-qa-with-frictional-writer-ian-thomas/).** Frictional Games. **Publication/update:** 2018-02-22; page also displays 2023-10-10, change substance unknown. **Edition/build:** Compiled Q&A, not the original stream; SOMA build unspecified.

**Type/access:** Firsthand practitioner interview, edited transcript; relevant-excerpt, 2026-10-10. **Locator:** Why did SOMA get a Safe Mode? lines 31–37; Why didn’t SOMA reuse enemies? lines 55–57; story-development and narrative-construction answers, lines 58–71. **Supports:** C-01, C-02, C-04, C-05, C-06, C-07, C-08, C-10.

**Limits/relationships:** Same production as 03. No transcript-to-stream audit or game observation; contradiction about provoked attacks remains unresolved. **Rights:** Reuse license not verified; paraphrase only. No artwork, video, audio or full source text redistributed.

### GDR-SRC-20261010-G01-07

**Heidi Kemps; SFB Games interviewees Adam Vian and Tom (as named in the article). [Crow Country: retro original PlayStation-era gameplay stylings meet modern horror](https://blog.playstation.com/2024/05/02/crow-country-retro-original-playstation-era-gameplay-stylings-meet-modern-horror/).** PlayStation.Blog / Sony Interactive Entertainment. **Publication/update:** 2024-05-02. **Edition/build:** Pre-release PS4/PS5 account; game build unknown.

**Type/access:** Firsthand developer interview; relevant-excerpt, 2026-10-10. **Locator:** Everything old is new again, lines 66–70; Modern conveniences, lines 74–78; Surprises all around, lines 83–88. **Supports:** C-01, C-04, C-05, C-06, C-08, C-10.

**Limits/relationships:** Practitioner preferences and mode description, not a controlled comparison. Independent SFB production; not independent of its own promotional claims. Images/media not inspected. **Rights:** Reuse license not verified; paraphrase only. No artwork, video, audio or full source text redistributed.

### GDR-SRC-20261010-G01-10

**Microsoft. [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108).** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live web revision checked 2026-10-10.

**Type/access:** Official vendor accessibility guidance, not treated here as a formal standard; relevant-excerpt, 2026-10-10. **Locator:** Overview lines 35–42; Implementation guidelines lines 95–155, especially 109–127 and 140–155. **Supports:** C-03, C-04, C-05, C-07, C-08, C-10.

**Limits/relationships:** Recommendations, not certification or evidence of equal emotional experience. Same issuer as 11/12. /gaming/ URL redirects to /xbox/. Public text retrieved despite an authorization banner; no sign-in or gated API inspected. **Rights:** Reuse license not verified; paraphrase only. No artwork, video, audio or full source text redistributed.

## Related entries and history

Related genre candidates: [Survival horror](../genres/survival-horror.md), GDR-CAND-20261010-G01-GEN-01; [Psychological horror](../genres/psychological-horror.md), GDR-CAND-20261010-G01-GEN-02. The [G01 review packet](../reviews/full-run-20261010-g01-review-packet.md) records G01-CON-02 and the proposed ownership handoff. Shared Challenge and difficulty, Session structure and retention, and accessibility topics are missing as researched dependencies; no stable IDs or contents are invented for them.

**2026-10-10 — 0.1.0 draft:** initial candidate. Author self-review by the drafting assistant, not independent review. Strongest challenge: describing separate consequence dimensions may imply an easy or emotionally neutral change. Revision retained: nonlethality is not absence of contact, and changed modes need not preserve the original activity or fear. The pattern explicitly prefers a targeted adjustment when it is the better fit. [C-02–C-08]

Gate C independent review, Gate D host retrieval, and Gate E acceptance/release remain outstanding. Next decision: review the pattern’s scope and ownership, then determine whether an authorized local comparison is warranted. No implementation, release or production-ID allocation follows from this draft. [C-09–C-11]
