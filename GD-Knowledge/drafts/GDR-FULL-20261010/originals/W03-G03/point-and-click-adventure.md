---
id: GDR-CAND-20261010-G03-GEN-03
kind: genre
title: Point-and-click adventure
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
predecessor_sha256: null
supersedes: null
change_summary: Initial G03 capture; no earlier G03 artifact superseded.
run_id: GDR-FULL-20261010
batch_id: G03
attempt_id: G03-attempt-01
identity_scope: run-scoped-temporary-candidate
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_timezone: America/Los_Angeles
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate + supplied G03 brief + inspected
  first-wave selected-draft excerpts
aliases:
- point-and-click
- point & click adventure
- graphic adventure — overlapping usage
tags:
- hotspots
- inventory-combination
- dialogue-state
- input-affordances
- recovery
related_topics:
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-W01-TOP-01
related_patterns:
- GDR-CAND-20261010-G03-PAT-01
- GDR-CAND-20261010-G03-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G03-GEN-01
- GDR-CAND-20261010-G03-GEN-02
source_ids:
- GDR-SRC-20261010-G03-001
- GDR-SRC-20261010-G03-002
- GDR-SRC-20261010-G03-007
- GDR-SRC-20261010-G03-008
- GDR-SRC-20261010-G03-009
- GDR-SRC-20261010-G03-012
- GDR-SRC-20261010-G03-014
- GDR-SRC-20261010-G03-015
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G03
hash_record: ../reviews/full-run-20261010-g03-review-packet.md#candidate-inventory
---

# Point-and-click adventure

**Draft, bounded research guidance.** This entry addresses object/verb selection, hotspots, inventory and conversation state. It is not the definition of the entire adventure family and does not make a mouse mandatory. Current game behavior was not directly observed; documented examples below identify their actual evidence route.

## Definition and boundaries

The working label identifies adventures where selecting represented objects, places or conversational possibilities and applying contextually meaningful actions is a major means of investigation and progress. A visible cursor is neither sufficient nor necessary: a strategy game can use pointing without this puzzle structure, while a controller or touch adaptation can preserve the relevant selection decisions. This is an analytical definition for this entry, not an approved market taxonomy. [C-01]

The official *Return to Monkey Island* overview explicitly presents a point-and-click label alongside context-sensitive interactions, dialogue trees and inventory. That is useful membership evidence for the site’s own framing, but its usability language is not a test result. Whether a particular controller adaptation preserves these decisions must be inspected rather than inferred from platform availability. [C-02; GDR-SRC-20261010-G03-008]

Compared with [adventure](adventure.md), this file adds the problem of **expressing an intended action through a selection interface**. Compared with [action adventure](action-adventure.md), it does not assume that continuous execution is the main obstacle. A timed interaction or danger sequence can still exist; examine whether timing, selection, interpretation or state is actually being tested. [C-01; C-03]

## Custom research instructions

For every important interaction, distinguish **detecting a possible target; selecting the intended target; choosing or expressing a verb; satisfying its state conditions; interpreting the response**. “The player did not solve it” is not an adequate diagnosis when any earlier step may have failed. A target can be obvious but difficult to select, or easy to select while its intended use remains unexplained. [C-03]

Inventory research must separately examine acquiring an item, recognizing its relevant property, combining or applying it, consuming it, and recovering from an inappropriate use. Conversation research must separately examine available topics, previously discussed topics, newly reactivated information and puzzle-changing commitments. Do not assume a greyed label means the same thing as “irrelevant” or that every dialogue tree is a dialogue puzzle. [C-03; C-05; C-08]

Seek creator reports of rejected interfaces, original studies of inference or inventory tasks, and reproducible scenes with exact input device, platform, build and state. Compare coherent difficult reasoning with an association only the author knows. Seek failures and fixes, not only nostalgia-oriented retrospectives. A patch report is evidence that the studio reported a defect, not proof that G03 reproduced it or verified the repair. [C-04–C-07; C-14]

Challenge pixel hunting, indiscriminate item combination, punitive dead ends, mouse exclusivity, literal dialogue wording and mandatory obscurity as genre necessities. The sample’s concentration in a Gilbert/Lucasfilm-associated tradition must not become a universal account of audiences or authors. [C-01; C-03; C-04; C-14]

## Player promises and varied audiences

Candidate promises include being able to express a plausible intention, learn from a response, investigate at an appropriate pace and make progress through understanding rather than accidental activation. Some players may choose sparse guidance or demanding search; others may need visible targets, alternate input or explicit recaps. A historic interaction style does not establish a shared modern preference or make its barriers essential. [C-03; C-09]

The key separation is **search as intended reasoning** versus **interface discovery as an unintended obstacle**. Highlighting every target may remove a meaningful search task in one scene. In another, it may merely make already-visible objects selectable without revealing what they mean. Determine which information the player is entitled to have and what the intended uncertainty concerns. No universal “hotspot help always spoils puzzles” or “hotspot help is always neutral” follows. [C-03; C-09]

## Characteristic loops and state structures

A diagnostic interaction loop is: inspect → select an object/topic → propose an action → receive a state-sensitive response → revise an interpretation or plan. It is useful because it separates intention from input execution and story state. It is not a required order: players can experiment before inspecting, and a dialogue may itself reveal the relevant action. [C-03]

Inventory and conversation can create different hidden prerequisites. Combining two items may require a prior observation, or a character may discuss a topic only after another speaker has disclosed a fact. A state table should say whether these are world constraints, knowledge checks, or authoring shortcuts. An unexplained flag requirement should not be disguised as failure to think logically. [C-08]

Gilbert’s dialogue essay distinguishes his preferences for showing complete lines from topic-based choices and discusses authoring tradeoffs. Treat this as a practitioner position, not proof that either representation is best. A complete line can clarify tone; a topic label can preserve flexibility but may hide the exact commitment. The appropriate contract depends on whether the choice merely opens discussion or makes a consequential statement. [C-05; C-08; GDR-SRC-20261010-G03-009]

## Conditional interface and puzzle decisions

| Decision | Conditional application and mechanism | Countercondition / simpler alternative |
| --- | --- | --- |
| Hotspot visibility | Make selectable objects discoverable through the supported input when finding invisible targets is not the intended challenge. Keep the inference about their use separate. [C-03; C-09] | When locating evidence is itself the task, an optional reveal changes that task. Name the change; consider a bounded search-area cue rather than exposing all answers. |
| Verb or context menu | Show available actions before an irreversible commitment when the player could reasonably misunderstand the default. A label or preview can separate selecting from acting. [C-03; C-08] | A single reversible, well-communicated action may need no menu. Extra confirmations can burden routine investigation. |
| Inventory combination | State the object properties that make a combination plausible; reject unsupported actions without silently consuming a necessary item. [C-08] | Irreversible crafting or loss may be intentional. It needs a communicated consequence and a supported progression policy, not automatic protection. |
| Failed-attempt feedback | Respond to the type of obstruction—target, verb, state or incompatible intention—where the player’s action provides enough evidence to do so. [C-08] | A canned response may be sufficient for genuinely irrelevant actions. Specific feedback can over-disclose a solution or require unaffordable writing coverage. |
| Conversation/topic state | Distinguish “already heard,” “temporarily unavailable,” “new information added” and “this commits a choice” when the distinction matters. [C-08; C-10] | Do not color-code uncertain relevance as objective truth or reveal an unseen branch solely through UI state. |
| Optional help | Let the player name a blockage without having to target the unknown solution object first; validate help against the actual saved state. [C-07; C-09] | An explicit overview, task reminder, direct answer on request or redesigned puzzle may be better than a complex unreliable hint engine. |

These are proposed applications. Most predicted effects remain hypotheses; a coherent design rationale is not a performed usability test.

## Mouse, touch and controller implementations

The inspected Revolution update posts document concrete interface work in Steam/Steam Deck contexts, including touch interaction and controller-navigation fixes. They support the need to inspect device-specific behavior, not a claim that all ports or input devices are equivalent. Exact binary versions and currently shipped behavior were not verified. [C-06; GDR-SRC-20261010-G03-012]

| Input context | Design alternatives to compare — not asserted universal product behavior | What to inspect and preserve |
| --- | --- | --- |
| Mouse/pointing device | Hover labels, click-to-select followed by action, contextual menus, or a clearly communicated primary action. | Can the player discover nonprimary verbs without guessing a button convention? Does pointer precision become the unintended gate? |
| Touch | Selection then explicit action, visible controls instead of hover-only information, or discoverable gestures with an alternative. | Finger occlusion, mistaken commitment, gestures that conflict with scrolling, and access to the same clue facts. Do not assume a hidden long press is self-explanatory. |
| Controller | Focus traversal between targets, an analog cursor, spatial target selection, or a deliberate hybrid. | Target order, focus visibility, cancellation, reachability and whether cycling exposes objects that pointing users would have to find. |

This table specifies proposed design comparisons, not measured superiority. Holding the same semantic actions does not guarantee equal effort, clue disclosure or satisfaction. Conversely, preserving mouse-like cursor motion at all costs may add effort without preserving an intended puzzle. [C-09; C-10]

## Applying shared topics

| Inspected shared candidate | Specific adaptation here | Retained correction or limit |
| --- | --- | --- |
| `GDR-CAND-20261010-P01-TOP-02`, Interface and information | Give objects, inventory and topics a task-information contract: what is available, uncertain, stale or consequential? | Diegetic or familiar-looking controls are not automatically usable. |
| `GDR-CAND-20261010-P01-TOP-03`, Accessibility and inclusive interaction | Check access to targets, verbs, dialogue, text and recovery separately from the intended inference. | No WCAG CSS-pixel criterion or XAG text/default guidance is converted to a universal game threshold; no arbitrary numerical settings are supplied. |
| `GDR-CAND-20261010-F01-TOP-03`, Learning and onboarding | Explain an unknown interface convention without solving an unrelated puzzle. Re-entry support should distinguish encountered facts from new conclusions. | Failed selection is not evidence of failed reasoning. |
| `GDR-CAND-20261010-F01-PAT-01`, Supported attempt and transfer check | When claiming the player learned an interaction rule, use new cases requiring different answers, with prediction distinct from preferred action. | Do not count repetition as transfer or withdraw input/access accommodations. |
| `GDR-CAND-20261010-W01-TOP-01`, Narrative structures | Mark whether a dialogue selection changes information, relationship, world state or only expression. | Do not equate expressive acknowledgement with consequential branching. |

These are inspected draft-to-draft adaptations, classified as inference rather than released rules. [C-10]

**Missing reviewed links:** W02 Dialogue and voice / Quests and objectives; F03 Progression and rewards; W03 Level and spatial design / World structure and exploration; P02 Controls and input / Feedback and game feel; P03 Platform and display context / Camera and framing. Existing submitted batches are not resubmitted here. No unseen candidate content is represented as inspected. [C-14]

## Pattern selection and application process

Use [Recoverable dependency gate](../patterns/recoverable-dependency-gate.md), `GDR-CAND-20261010-G03-PAT-01`, to examine inventory consumption, conversation commitments, one-way room transitions and saves made during puzzle animations. For each, state whether recovery is expected or the consequence is intentional. The graph alone cannot tell whether an item use is inferable. [C-08]

Use [Player-requested state-aware hints](../patterns/player-requested-state-aware-hints.md), `GDR-CAND-20261010-G03-PAT-02`, where a live puzzle has a trustworthy state representation and the player can request help without naming its hidden solution. For this subgenre, a hint should distinguish “I cannot select it,” “I do not know which action is available,” and “I do not understand the relationship.” [C-07; C-09]

Apply the candidates by observing a future authorized attempt’s **intention and actual input separately**, identifying the first failed stage, selecting a scoped intervention, and comparing both successful expression and preserved reasoning. A correct response reached by exhaustive combinations is not evidence that the intended inference worked. Remove or redesign an intervention that turns every failed attempt into an unwanted answer. [C-03; C-08; C-13]

## Worked example — illustrative inventory and conversation puzzle

**The botanical archive.** An archivist offers a sealed seed ledger after a ventilation mechanism is restored. A brittle cord, a flexible plant tie and a counterweight are available. The diagram explains that the weight must move freely; the player can inspect each material’s relevant properties. A topic about an earlier repair becomes newly informative after the player sees a damaged pulley. All scene details are invented. [C-11]

The proposed intended solution is to replace the binding cord with the flexible tie. A player instead offers a rigid rod, reasoning that it could hold the vent open. The response should identify the actual constraint—if one is established—rather than merely mocking the attempt. If the rod would plausibly work and no conflicting requirement exists, the team must consider accepting it, changing the evidence, or revising the puzzle. Author preference alone is not a physical explanation. [C-08; C-11]

On a proposed mouse interface, selecting the cord can expose inspect and replace actions. A touch prototype might separate selecting from committing replacement; a controller prototype might cycle through targetable components. Those are untested alternatives. The controller focus list could reveal the hidden pulley earlier than other interfaces, so the team must decide whether pulley discovery is a puzzle or merely an access step. Equating all three interfaces because they share a verb is insufficient. [C-09; C-11]

A failed use does not consume the plant tie unless the design explicitly supports the consequences of that loss. A save during the repair must not retain “tie consumed” while losing “vent repaired.” The conversation topic should distinguish a previously heard account from the new detail triggered by the damaged pulley without automatically asserting that the topic contains the solution. [C-08; C-11]

**Counterexample:** in a comedy about unsafe experiments, an irreversible failed combination might be the intended consequence. The recovery pattern should then preserve the declared mode—perhaps a replayable experiment or a consequential ending—rather than silently making every attempt harmless. Equally, an explicit “reveal all targets” option can be valuable without claiming it preserves a search challenge. [C-08; C-09; C-11]

## Representative cases, failures and evidence boundaries

| Primary evidence | Bounded lesson | Prohibited leap |
| --- | --- | --- |
| Official *Return to Monkey Island* overview, undated live page | One product explicitly uses the label and advertises its interaction vocabulary. [C-02] | The vocabulary proves intuitive controls or commercial effectiveness. |
| Gilbert, *Dialog Puzzles*, 2015 pre-release account | Full-line versus topic-based dialogue is a deliberate authoring choice. [C-05] | One author’s preference settles every conversation UI. |
| Gilbert, *Dialogs, Hints and more...*, build 1388.918 account | A targeted-help design can require knowledge the stuck player lacks; older save data can make contextual hints inaccurate. [C-07] | The revised hint system is empirically validated or current on every platform. |
| Revolution, 2024 Update #1 | Studio-reported Syria cave/ring-pull save-state defect exemplifies a progression recovery problem. [C-06] | G03 reproduced the issue or verified all repairs. |
| Revolution, 2024 Update #2 | Reported touch/controller/UI fixes expose concrete selection and visibility concerns. [C-06] | A patch note establishes equal usability across devices. |

The original genre-adjacent empirical study inspected in G03 concerns visual search, not inventory combination. A directly relevant 2024 master’s-thesis record by Kienast was available only as an abstract; the full thesis was not retrieved. Its title and abstract cannot supply participant results or a puzzle-design rule. The inaccessible official Steam store lead likewise supplies no feature evidence here. [C-14; GDR-SRC-20261010-G03-014; GDR-SRC-20261010-G03-015]

## Accessibility, localization, ethics and production

Offer supported ways to discover and operate essential targets without requiring fine pointing, hover, an undocumented gesture, or a single sensory channel when those are barriers to the intended audience. This is a proposed access review, not a statement that all such techniques must be absent. Assess information entitlement before deciding whether a target reveal is an accommodation, an answer hint, or both. Avoid assumptions about disability or genre expertise. [C-09; C-10]

Text choices require semantic review, not only layout review. A translated inventory label may no longer suggest the relevant material property; a dialogue paraphrase may imply a stronger commitment than the spoken line; a culture-specific joke may be the only alleged reason for an item combination. Localize the evidence relationship, preserve speaker intent where required, and test plausible alternative readings. Full voice, subtitles and text-only routes may require different timing and recovery designs. These are hypothesized risks, not measured rates. [C-12]

Authoring a bespoke response for every object/verb pair can be expensive and still fail to distinguish useful intentions. Prioritize plausible hypotheses and consequential mistakes, group genuinely equivalent failures, and preserve uncertainty about what the player meant. This is a proposed production strategy, not a sourced cost-saving percentage. It can fail when grouped feedback conceals a different state requirement. [C-08; C-12]

Do not frame assistance as evidence of intellectual inferiority or sell relief from intentionally opaque blockers. Preserve the option to stop, defer help or request more explicit help. Any later telemetry or recorded interviews need appropriately scoped consent and privacy handling; no participants or private player records were collected in this task. [C-12; C-14]

## Research questions and validation

**All tests are proposed; none was run.** Device interaction, build behavior and player interpretation need separate evidence. [C-13]

| Question | Proposed comparison and observation | Falsifying or narrowing result |
| --- | --- | --- |
| Is the obstacle target detection, selection, verb access or inference? | Ask a participant to state an intended action, then attempt it using a supported input. Record intended target, selected target, available verb, resulting state and interpretation of feedback. | An “easy puzzle” remains inaccessible because the intended action cannot be expressed. Redesign access rather than add solution hints. |
| Does a hotspot reveal preserve the intended task? | Compare bounded visibility alternatives using the same puzzle facts; distinguish locating an object from understanding its use. | The aid discloses the very evidence whose discovery was the chosen challenge. Relabel the mode or offer a narrower option; do not claim neutrality. |
| Does failed-action feedback support reasoning rather than exhaustive search? | Compare a concise state-relevant response with a generic rejection for plausible incorrect attempts. Record the next hypothesis and reason, not just eventual success. | Specific feedback merely reveals the solution or encourages faster combination enumeration without understanding. Narrow or remove it. |
| Does conversation state remain intelligible after revisits? | Include a topic that gains new information, an unavailable topic and a consequential choice. Test re-entry and localized text variants. | Visual state implies irrelevance, completion or commitment incorrectly. Revise the representation and state definitions. |
| Are recovery states coherent? | Specify future save/reload cases before, during and after consumption, animation completion and conversation commitment. | A supported state loses both the prerequisite and its outcome. Technical correction is required; it does not by itself prove puzzle fairness. |
| Is learning more than repeating an example? | Use the corrected F01 rule-discrimination probes with new objects and different correct actions or predictions, preserving accommodations. | Familiar answers succeed while discriminating cases fail. Do not report transfer. |

Participants and test contexts should reflect relevant device familiarity, motor/visual access, reading and language needs, and prior puzzle traditions. Do not impose an inaccessible baseline for comparison. Determine local success and spoiler-tolerance criteria before observing results; no universal hotspot dimension, help delay, puzzle length or sample-size guarantee is justified here. [C-10; C-13]

### Coverage and remaining discriminating questions

| Subtopic | G03 coverage | Gap / next question |
| --- | --- | --- |
| Hotspot and verb affordances | Analytical separation, input-specific comparisons and documented UI failures | Direct mouse/touch/controller observations on identified builds remain absent. |
| Inventory and dependency recovery | Conditional audit and studio-reported save failure | Full empirical inventory-puzzle thesis unavailable; current-build behavior unverified. |
| Conversation/topic state | Creator preference account and explicit state alternatives | W02 draft bytes and multi-language behavior not inspected. |
| Failed attempts and optional hints | Concrete creator rejection of a help design; conditional feedback analysis | No controlled test of intention-sensitive feedback or the full hint recipe. |
| Nostalgia and punitive expectations | Historic heuristic treated as contestable rather than necessary | No representative audience-preference evidence. |
| Accessibility and localization | P01 correction-preserving guidance and proposed tests | No complete device/access-population parity study. |

## Claim ledger

| ID | Precise claim / role | Class | Source and locator | Confidence and unresolved limit |
| --- | --- | --- | --- | --- |
| C-01 | This working definition concerns selection-mediated investigation, not mouse hardware alone or all adventures. | inference | 008 product vocabulary; 012 input-specific update reports; supplied genre brief. | Moderate analytical utility, low as universal membership rule. |
| C-02 | The official Return to Monkey Island overview names point-and-click and lists interaction systems. | observed-example | 008, Return to Point & Click Swashbuckling; inspected webpage artifact. | High for the description, not for gameplay or usability. |
| C-03 | Detection, selection, verb access, state and inference are distinct potential causes of a failed attempt. | inference | 007 targeted-help problem; 012 UI/input defects; inspected P01 information contract. | Moderate explanatory plausibility; no validated diagnostic instrument. |
| C-04 | Gilbert’s historic critique does not establish pixel hunting, punitive failure or any alternative as a universal genre requirement. | practitioner-heuristic | 001, qualified preface and Arbitrary puzzles / Reward Intent / I forgot to pick it up. | High for the qualified author position; no audience consensus inferred. |
| C-05 | Gilbert describes full-line/topic-label dialogue choices and their authoring tradeoffs as a creator preference. | practitioner-heuristic | 009, author body before sample script. | High attribution, not comparative usability proof. |
| C-06 | Revolution reports a save-dependent cave obstruction and device/UI issues in two dated update posts. | observed-example | 012, Update #1 (Can’t) Open Sesame; Update #2 UI/STEAM DECK. | High for inspected documentation; defects/fixes were not reproduced. |
| C-07 | Gilbert reports rejecting a help interaction that required identifying the relevant object, and warns about old-save hint state. | practitioner-heuristic | 007, HintTron/telephone and old-save discussion. | High attribution, no controlled effect or reliability percentage adopted. |
| C-08 | State-specific feedback and recoverable dependencies may support coherent investigation when they distinguish meaningful conditions. | hypothesis | Bridge from 001/002/009/012; authored application table and counterexamples. | Low for causal benefit; may over-disclose, cost too much or defeat intended consequences. |
| C-09 | Device-specific access and requested hint scope should be evaluated without assuming equal disclosure or experience. | hypothesis | 007/012; inspected P01 access distinctions. | Low for specific interventions; platform parity remains untested. |
| C-10 | Shared-candidate adaptations retain information/access distinctions and corrected discriminating transfer probes without universal UI numbers. | inference | Actual inspected P01, F01 and W01 excerpts, with correction receipts. | Moderate as bounded draft transfer; not fresh validation of their original references. |
| C-11 | The botanical-archive example illustrates plausible failed actions, alternate input and save-state dependencies. | hypothesis | Synthetic worked example only. | Low; no real game or player outcome claimed. |
| C-12 | Semantic localization, bounded response authoring and nonpunitive help are proposed production/ethical constraints. | hypothesis | Conditional synthesis from 009 and inspected P01/W01 guidance. | Low project-specific confidence; no cost model or approved studio policy implied. |
| C-13 | The proposed tests can distinguish several failure causes but have no observed outcomes. | hypothesis | Test specifications in this entry. | Low until authorized execution and suitable evaluation. |
| C-14 | Full inventory-puzzle thesis evidence, direct build observations and named dependency bytes remain uninspected. | inference | 014 abstract-only record; 015 failed access; G03 work/access record. | High for this session’s limitations, not a claim that no relevant evidence exists. |

Source suffixes expand to `GDR-SRC-20261010-G03-<nnn>`. Local unresolved conflicts: `G03-CON-03` (help/discovery), `G03-CON-04` (input access versus disclosure), and `G03-CON-06` (recovery versus intentional consequences). No new global contradiction IDs are allocated.

## References

Access date for every record below: **2026-10-10, America/Los_Angeles**. Web-text line numbers identify this inspected retrieval; headings and named paragraphs are the portable locators. A source identity is temporary, reused within G03; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G03-001

**Ron Gilbert. [Why Adventure Games Suck / Why Adventure Games Suck And What We Can Do About It](https://grumpygamer.com/why_adventure_games_suck/).** Grumpy Gamer (author site). Date: 1989 original essay; 2004-05-12 republication and retrospective preface.

**Edition/context:** 1989 essay in its 2004 web wrapper; accessed page has a 2026 site footer. **Access:** `full`. **Type:** Firsthand designer essay; practitioner heuristics.

**Inspected locator:** Preface, especially the paragraph beginning “As I read this”; sections “Live and learn,” “I forgot to pick it up,” “Arbitrary puzzles,” “Reward Intent,” and “Give the player options.” Inspected web-text lines 21–26, 53–63, 74–90.

**Support in this artifact:** C-04; bounded historical rationale underlying C-08.

**Limits:** Historical viewpoint, not an audience survey or causal experiment. The retrospective preface explicitly qualifies the older advice. No numerical rule or blanket rejection of failure/linearity is adopted. **Independence:** Same author/design tradition as sources 002, 007 and 009; not four independent replications.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-002

**Ron Gilbert. [Puzzle Dependency Charts](https://grumpygamer.com/puzzle_dependency_charts/).** Grumpy Gamer (author site). Date: 2014-08-10.

**Edition/context:** Dated web essay; text inspected, diagrams and linked large chart not visually inspected. **Access:** `relevant-excerpt`. **Type:** Firsthand design-process account.

**Inspected locator:** Opening account of Maniac Mansion/Monkey Island; definition of dependency chart; worked-text distinction between unlocking/oiling/opening; linearity/choice and act bottlenecks. Web-text lines 19–23, 28–53, 60–63.

**Support in this artifact:** C-08 prerequisite-audit rationale only; no chart imagery or prescribed branch count used.

**Limits:** Retrospective attribution, no comparative production measurements. Diagram details not independently observed. Its suggested branch counts are not library targets. **Independence:** Same author as 001, 007 and 009. The essay itself distinguishes surviving notebook material from an unavailable original Monkey Island chart.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-007

**Ron Gilbert. [Dialogs, Hints and more...](https://blog.thimbleweedpark.com/hints_and_dialogs.html).** Official Thimbleweed Park development blog. Date: 2017-06-20.

**Edition/context:** Build 1388.918 update account; Steam availability reported, other platforms pending in that post. **Access:** `relevant-excerpt`. **Type:** Firsthand implementation/failure account.

**Inspected locator:** Author body, especially rejected HintTron object-targeting/cooldown design, telephone hints and old-save state warning. Web-text lines 7–44.

**Support in this artifact:** C-07 and rationale for C-03/C-09.

**Limits:** No controlled evaluation; old-save reliability percentage is an unvalidated author estimate and is not reused. Comments and embedded configuration instructions are not evidence or instructions to execute. **Independence:** Same author as 001/002/009. Hint content credited to Jenn and, with permission, Meghann O’Neill’s earlier online hints; that underlying hint work was not independently inspected.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-008

**Official Return to Monkey Island website; individual text author unknown. [About Return to Monkey Island / Game overview](https://returntomonkeyisland.com/game-overview).** Official game website; production credits name Terrible Toybox-associated creators and Lucasfilm collaboration. Date: unknown.

**Edition/context:** Undated live overview accessed on the stated check date; no build identifier. **Access:** `relevant-excerpt`. **Type:** Publisher/developer product-description artifact.

**Inspected locator:** “Return to Point & Click Swashbuckling!” and “Created by a Legendary Crew!” Web-text lines 38–40 and 52–54.

**Support in this artifact:** C-02 and qualified vocabulary informing C-01.

**Limits:** Evidence for the site’s label and advertised interaction vocabulary only. “Easy-to-use” marketing is not a usability finding; no platform parity or gameplay observation asserted. **Independence:** Production lineage overlaps with Gilbert sources; separate product, not independent outcome evidence.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-009

**Ron Gilbert. [Dialog Puzzles](https://blog.thimbleweedpark.com/dialog_puzzles.html).** Official Thimbleweed Park development blog. Date: 2015-06-30.

**Edition/context:** Pre-release design essay; includes an author-created script example, not a verified shipped scene. **Access:** `relevant-excerpt`. **Type:** Firsthand dialogue-design account.

**Inspected locator:** Author body on dialogue-tree terminology, full lines versus topic labels and writing/programming tradeoffs; web-text lines 7–38. Sample script lines 45–99 inspected only as an authored example.

**Support in this artifact:** C-05 and proposed dialogue/localization tradeoffs; no numeric cost claim.

**Limits:** Preferences for verbatim choices are not universal usability rules. No numeric dialogue-cost multiplier adopted. Reader comments are not a representative sample. **Independence:** Same creator and project as 007; same wider tradition as 001/002.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-012

**Revolution Software (studio-signed update posts). [Broken Sword – Shadow of the Templars: Reforged: Update #1 and Update #2](https://steamcommunity.com/app/2544110/allnews/).** Official Steam community news for app 2544110. Date: Update #1: 2024-10-02; Update #2: 2024-10-11.

**Edition/context:** Two dated update excerpts within a mutable news collection; Steam/Steam Deck context; exact binary versions unknown. **Access:** `relevant-excerpt`. **Type:** Firsthand patch/failure documentation.

**Inspected locator:** Update #1 “(Can’t) Open Sesame” and “STEAM DECK,” web-text lines 580–604, 695–704; Update #2 “UI” and “STEAM DECK,” lines 489–491, 535–560.

**Support in this artifact:** C-06; input/state failure examples inform hypotheses without reproducing gameplay.

**Limits:** Reported bugs and fixes are not reproduced by G03; no claim all saves/devices are fixed. Collection is not a permanent per-post URL; datelines and exact section headings distinguish the excerpts. **Independence:** One studio/product across both posts; same product as inaccessible lead 015, not independent corroboration.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-014

**Philipp Emanuel Kienast. [Measuring and Reflecting on the Cognitive Load of Inventory Puzzles in Point-And-Click Adventure Games](https://pure.fh-ooe.at/en/studentTheses/measuring-and-reflecting-on-the-cognitive-load-of-inventory-puzzl/).** University of Applied Sciences Upper Austria, master’s-thesis repository record. Date: 2024 (award year; exact publication date unknown).

**Edition/context:** Repository abstract and bibliographic record only. **Access:** `abstract-only`. **Type:** Thesis lead; not inspected empirical support.

**Inspected locator:** Abstract and bibliographic fields, web-text lines 12–31, 40–47. Linked catalogue route https://permalink.obvsg.at/fho/AC17342127 failed to retrieve.

**Support in this artifact:** C-14 access gap only. No thesis result accepted.

**Limits:** Full thesis, participants, methods, results and appendices unavailable in this session. No findings or design-guide recommendations imported. **Independence:** Potentially relevant independent academic lead; independence of underlying examples not assessed.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-015

**Revolution Software storefront description; exact author not inspected. [Broken Sword – Shadow of the Templars: Reforged — Steam store page](https://store.steampowered.com/app/2544110/Broken_Sword__Shadow_of_the_Templars_Reforged/).** Steam. Date: unknown.

**Edition/context:** Product app 2544110; store body not retrieved. **Access:** `lead-only`. **Type:** Inaccessible product-page lead.

**Inspected locator:** Search result located app 2544110; direct English and alternate-slug open attempts returned internal/cache errors.

**Support in this artifact:** C-14 access gap only. No storefront feature used.

**Limits:** Search snippets are not support. No claimed feature, genre label, accessibility claim, current price or platform guarantee is taken from this lead. **Independence:** Same studio/product as 012; source identity retained for access-gap tracking only.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

## Inspected shared-candidate provenance

Source container: **GD-Knowledge-first-wave-reviewed-drafts-2026-10-10.zip**, Library `libfile_6852a9bc35108191bdcf23bd487e3b42`; actual bytes retrieved in G03 and SHA-256 matched to parent receipt: `e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef`. Root is `GD-Knowledge-first-wave-reviewed-drafts-2026-10-10/`. The following are inspected **excerpts of selected drafts**, not re-verification of their entire public bibliographies. All remain version **0.1.0**, status **draft**, null approval metadata. They are not resent with G03.

**GDR-CAND-20261010-P01-TOP-02** — `selected-drafts/topics/interface-and-information.md`; revision `review-correction-1`; SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`. Locator: “Working definitions” and “Task-information contract,” inspected lines 63–81.

**GDR-CAND-20261010-P01-TOP-03** — `selected-drafts/topics/accessibility-and-inclusive-interaction.md`; revision `review-correction-1`; SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. Locator: Definition/access chain and proposed evaluation, inspected lines 54–87 and 193–221; corrections/P01/CORRECTION_RECEIPT.md lines 3–21.

**GDR-CAND-20261010-F01-TOP-03** — `selected-drafts/topics/learning-and-onboarding.md`; revision `original`; SHA-256 `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598`. Locator: “Guidance should track the learning demand”; “Discovery and explanation”; “Practice”; “Feedback”; “Re-entry,” inspected lines 65–103.

**GDR-CAND-20261010-F01-PAT-01** — `selected-drafts/patterns/supported-attempt-and-transfer-check.md`; revision `independent-review-correction-1`; SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Locator: Purpose, prerequisites, mechanism, recipe and corrected transfer probes, inspected lines 49–118; correction.diff.md lines 18–43.

**GDR-CAND-20261010-W01-TOP-01** — `selected-drafts/topics/narrative-structures.md`; revision `initial`; SHA-256 `9bac355072317ed9db0c299d926d293cd70052426ceb8db9cae98beaee1d15c7`. Locator: Decision, vocabulary, promise/action/persistence/interpretation and discovered order, inspected lines 57–100.

The parent-selected correction receipts govern which draft was inspected; they do not make its hypotheses accepted evidence. External dependency file paths are recorded as text because the files are not in this delivery. The [G03 packet](../reviews/full-run-20261010-g03-review-packet.md#dependency-register) holds unresolved links and proposed integration ownership.

## Review and history

Initial G03 capture; version `0.1.0`, status `draft`, revision `initial-capture-1`; predecessor and supersession null. Author self-review retains the strongest contrary case: revealing targets can remove a genuine search task, while excessive intention-specific feedback can solve an inference the player wanted to own. A broad “make everything obvious” rule was not adopted.

The [review packet](../reviews/full-run-20261010-g03-review-packet.md) contains the exact hash, claim/source mapping, proposed index row and independent-review request. Next decision: Gate C review of the distinction between interface barriers and intended search, with later capture of P02/P03/W02 dependencies and authorized device-specific evidence. No release or implementation follows from this file’s completion.
