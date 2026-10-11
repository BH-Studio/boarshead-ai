---
id: GDR-CAND-20261010-G16-GEN-01
kind: genre
title: Roguelike
version: 0.1.0
status: draft
candidate_revision: independent-review-correction-1
attempt_id: GDR-FULL-20261010:G16:initial-author-attempt-1
predecessor_sha256: 4daf9109b3fa250888427aa2d370e646b55b5e9d6dc90440bc1bb79d4eb8ebca
supersedes: []
owner_project: BH-GDR-Genres
proposed_shared_owner: null
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: open
aliases:
- traditional roguelike
- rogue-like
- run-based systemic exploration
tags:
- run-boundary
- procedural-variation
- systemic-knowledge
- contested-genre
- turn-structure
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
- GDR-CAND-20261010-G16-PAT-01
related_genres:
- GDR-CAND-20261010-G16-GEN-02
- GDR-CAND-20261010-G16-GEN-03
source_ids:
- GDR-SRC-20261010-G16-001
- GDR-SRC-20261010-G16-002
- GDR-SRC-20261010-G16-003
- GDR-SRC-20261010-G16-004
- GDR-SRC-20261010-G16-006
- GDR-SRC-20261010-G16-012
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
source_deduplication: pending-library-coordination
---

# Roguelike

**Complete bounded author draft; coverage remains open.** This entry addresses what a designer means by *roguelike*, which decisions that choice actually changes, and how to assess procedural situations, loss and learning without treating a historical checklist as a universal law. No game was run or playtest performed. Documentary examples are limited to the editions and passages in the references.

## Definition and boundaries

For this file, **roguelike is a contested family label whose useful design profile must be stated**. The traditional profile under examination combines run-bounded advancement, exploration of variable spaces, consequential resource decisions and learning of interacting rules; turn-based, grid-oriented, non-modal play is important to one influential interpretation, not a certificate of quality or an exclusion rule for every contemporary use. This is a research working definition, not a studio-approved replacement taxonomy. [C-01, C-02]

The original Berlin Interpretation is a primary community proposal, not a formal standard. It presents weighted similarities and explicitly rejects a necessary-and-sufficient membership test. Replies in the same discussion question whether lineage/influence and systemic principles are better guides than surface conventions. Its archive/mirror dating is also inconsistent: Google Groups displays September 27, 2008, reply quotations use September 26, and RogueBasin attributes September 16. The disagreement is retained as provenance uncertainty, not silently repaired. [C-02]

| Boundary question | Working treatment for this entry | Design consequence |
|---|---|---|
| Roguelike versus [roguelite](roguelite.md) | The files ask different design questions; they do not divide every shipped game cleanly. This file foregrounds systemic exploration and run-bounded planning; the companion foregrounds retained opportunity/power and multi-run structure. | Specify exactly what ends and what carries forward; do not let either label substitute for that rule. |
| Dungeon crawler versus roguelike | A dungeon is a setting/structure; the working roguelike profile concerns repeat attempts and rule-driven decisions. | A persistent authored dungeon can pose different learning and loss questions. The neighboring genre’s current draft is a missing dependency, not copied here. |
| ASCII versus tiles or other presentation | Representation is not an adequate substitute for the underlying decision structure. | Preserve available facts and discoverability across the chosen representation; do not equate a nostalgic interface with required difficulty. |
| Turn-based versus continuous action | Specify when input is accepted, what advances time, and which actions have different durations. | A clock-stopped choice, a long simulated action and a real-time dodge demand different information and access support. |
| Permanent death versus no persistence of any kind | Loss of a character does not imply absence of world traces, records, modes or player knowledge. | Maintain a typed boundary instead of promising that absolutely everything resets. |

These are conditional analytical distinctions, not universal membership tests. NetHack’s bones and explore-mode documentation is a concrete reason not to collapse the last row into a slogan; DCSS’s time rules are a reason not to collapse turn-based decisions into equal-duration steps. [C-01, C-03, C-04, C-07]

## Custom research instructions

Investigate **what a run teaches and what it asks the player to risk**, rather than compiling a list of familiar games. Record the claimed tradition, then inspect a versioned manual, source documentation or reproducible recording for action timing, knowledge visibility, resource renewal, loss boundaries and generation constraints. Keep creator aspirations separate from observed outcomes. A future source pass should include traditional console lineages, non-dungeon/noncombat designs and documented rejected or abandoned designs, not only enduring PC examples. [C-01, C-05, C-08]

For procedural space, distinguish the generator’s output count from **different problems the player must solve**. Examine reachability, resource dependencies, sightline/escape affordances, early forced risks, repeated dominant approaches and combinations of authored modules. Ask what cannot be generated and why. A shared generator specification belongs to Foundations’ Procedural and authored content topic; this file only records the consequences for this genre’s decision promise. The selected reviewed bytes of that topic are unavailable here. [C-05, C-10]

For knowledge, record which relations stay fixed between attempts and which are re-randomized. A player recognizing an icon is not necessarily predicting a rule; a player who knows a rule can still choose a riskier action. Use contrasting and boundary cases, including an affordable action that can reasonably be declined. If the rule itself changes, report a **rule-change test**, not ordinary transfer under the same rule. Do not remove captions, remaps, magnification, notes or other ordinary accommodations to manufacture a “pure” mastery measure. [C-08, C-11]

Challenge the following comparisons explicitly: “permadeath versus checkpoints” without specifying lost inventory and repeated traversal; “random versus authored” when the random condition includes authored vaults; “expert versus novice” when unlocks or spoiler knowledge differ; and “turn-based therefore accessible” without testing the whole interface. Do not derive fairness from a successful seed or demand that every seed guarantee a win. Instead, choose and test the actual fairness promise, such as avoiding an unavoidable opening defeat or ensuring a learnable warning. [C-05, C-09–C-11]

## Player promises and varied audiences

Potential promises include **adaptable planning**, **discovery of systemic relationships**, **a self-contained accomplishment**, and **a consequential attempt whose failures are interpretable**. These are candidate experience goals suggested by the inspected design traditions, not measured expectations of every roguelike player. Some people may prioritize blind discovery; others enjoy reliable information, challenge comparison, assisted exploration, unusual builds or social discussion of runs. A designer must choose which of those goals the actual product supports and recruit beyond self-selected expert communities when evaluating it. [C-01, C-08, C-13]

A hard reset can support a chosen sense of finality, yet can also require redoing already understood work. Retaining knowledge may make repetition worthwhile, but only when later situations let that knowledge change an action. Neither outcome follows from the genre label. The inspected empirical comparison concerns short platformer sessions, not this population or long-term genre preference; its limitations prevent converting it into either an argument for harsher loss or a universal case for easier recovery. [C-08, C-09]

## Characteristic loops and structures

A useful diagnostic structure is **observe a situation → infer or recall a rule → commit a resource/action → inspect the consequence → update the plan**. Over an attempt, the question becomes how local costs constrain routes, tools and later contingencies. Across attempts, distinguish a changed player model from stored power or a changed world. These horizons are analysis lenses, not a requirement to construct exactly three loops. [C-07, C-08]

### Stable rules in variable situations

DCSS’s philosophy discusses meaningful tactical/strategic differences, authored vaults and limiting repetitive optimal labor. That supports examining structured variation rather than relying on combinatorial output size. The proposed bridge is that stable relations give the player something to learn, while changed resource/spatial arrangements can make that knowledge applicable in a new way. The final link—more valued decisions for a particular audience—remains untested. More generation can instead reproduce the same dominant plan or create opaque exceptions. [C-05, C-08]

A practical audit therefore compares **decision signatures**: what must be noticed, which actions are feasible, what resource becomes scarce, and what consequence makes alternatives differ. Do not claim two maps are meaningfully distinct just because their geometry differs. Conversely, a reused room can pose a different question when arrival resources or available tools change. Both are design inferences requiring player-facing verification. [C-08, C-10]

### Consequence, interruption and persistence

Loss should be described as a transition among named states: character/build; carried resources; generated space; cross-run traces; records and opportunities; narrative state; access configuration. Player memory is not a save field that the game can reliably erase. A suspend/resume action also need not have the same semantics as defeat, deliberate abandonment or finishing an attempt. Preserving a suspend state does not logically require granting rollback after an intentional loss. These distinctions enable separate design choices; they do not prescribe a technical save architecture. [C-03, C-07]

## Practical application process

1. **Declare the experience and rule profile.** Identify the desired planning, discovery or execution decisions and describe the current loss/persistence contract in ordinary language. Record the audience and uncertainty intentionally preserved. Do not start by maximizing strictness. [C-01, C-07]
2. **Trace a representative attempt and its failure paths.** For each expensive setback, separate misunderstanding, unavailable information, execution, deliberate risk, resource exhaustion and technical interruption. A death count is not a diagnosis. [C-07, C-13]
3. **Choose the smallest useful variation.** Compare a fixed authored set, authored modules with constraints, and broader procedural composition. Evaluate the changed decisions and authoring/verification cost, not merely the number of seeds. [C-05, C-10]
4. **Choose boundary behavior independently.** Decide what defeat, completion, abandonment and interruption do to each state category. Preserve the chosen boundary in help, settings and return screens. Use the pattern below only where mixed state makes this useful. [C-07, C-11]
5. **Propose discriminating tests, then revise or omit.** Test understanding and changed-state application separately from willingness to take risks. If variation adds invalid situations but no valued new decisions, simplify it. If a reset adds only repeated labor for the declared audience, compare a shorter attempt or changed recovery boundary before adding compensation currencies. No such test has been run here. [C-08–C-10, C-13]

## Applying shared topics

The links below lead to the **exact inspected dependency receipt**, not an invented local copy of a shared topic. All transferred candidates remain draft, independently reviewed by the parent process only, and coverage-open.

| Reviewed shared candidate | Roguelike-specific adaptation; limit |
|---|---|
| [Decision design — GDR-CAND-20261010-F02-TOP-01](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer) | Distinguish intended uncertainty about a room or rule from inability to perceive an available cue. A probability display must not pretend unknown generator outcomes are measured distributions. |
| [Challenge and difficulty — GDR-CAND-20261010-F02-TOP-02](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer) | Separate tactical demand, execution demand, repeated traversal and loss of stored progress. Assistance need not alter all four. |
| [Interface — GDR-CAND-20261010-P01-TOP-02](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer) | Make discovered facts, recent consequences and current mode recoverable after an interruption without automatically revealing unexplored information. |
| [Accessibility — GDR-CAND-20261010-P01-TOP-03](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer) | A turn-based loop still needs usable configuration, navigation, reading and input. Preserve the parent’s numerical-scope correction; no universal pixel/time/contrast settings are imported. |
| [Evaluation — GDR-CAND-20261010-F07-TOP-01](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer) | Attribute success to the tested build, seed, resources, assistance and prior knowledge; do not read mastery from survival alone. |

These adaptations are G16 inferences/hypotheses, not additional validation of the shared evidence. Progression, procedural content, session structure, full localization and relevant neighboring-genre reviewed bytes remain missing. [C-07, C-08, C-11, C-13]

## Pattern selection and hybrid adaptations

[Explicit run-state boundary — GDR-CAND-20261010-G16-PAT-01](../patterns/explicit-run-state-boundary.md) is useful when different state classes cross an attempt boundary differently. It is unnecessary ceremony when a tiny self-contained game already has an unambiguous single reset and no mixed records. It does not require account upgrades. [C-07, C-14]

The inspected **Supported attempt and transfer check — GDR-CAND-20261010-F01-PAT-01** contributes the corrected contrasting/boundary test method. **Bounded disclosed difficulty adaptation — GDR-CAND-20261010-F02-PAT-02** is only conditional: diagnose the target demand, retain a fixed/manual path and do not infer inability from experimentation or repeated deaths. Both are recorded in the dependency receipt and are not reissued here. [C-08, C-11, C-13]

For an action-platformer hybrid, planning may compete with reaction demands; pausing to inspect an object can alter the intended pacing but withholding inspection can block informed choices. For a persistent exploration hybrid, regenerated geography can undermine a promise of learning a coherent place; consider stable regions with variable local problems rather than forcing complete regeneration. For a deckbuilder hybrid, losing a carefully developed deck can support a fresh attempt but remove the long-term composition goal: disclose whether cards, card unlocks, or neither persist. These are conditional conflicts, not reasons to reject hybrids. [C-12]

## Representative and negative cases

| Inspected case | What it contributes | What it does not establish |
|---|---|---|
| NetHack 3.6.7 guidebook | Bones and explore-mode exceptions challenge absolute claims about no persistence and no alternative loss mode. | Current port behavior, enjoyment, population preference or accessibility sufficiency. |
| DCSS 0.32.1 manual | Separates tactical/strategic priorities, varied action time, authored vaults and anti-grinding rationale. | Every generated start is fair, every combination is viable, or the rationale caused success. |
| Historical Spelunky creator page | An action-platformer/systemic-interaction contrast with randomized restart spaces. | Exact current controls, absence of metaprogression or a definitive genre assignment. |
| Cuerdo’s external reset-location study | Contrary evidence against a simple “less setback improves every experience measure” story. | A prescription for long roguelike attempts or the value of permanent upgrades. |

Selection favors accessible, documented designs. Failed commercial projects, long-term quitters, console traditions and non-English communities are underrepresented. Examples were read in documents; they were not reproduced in game. [C-03–C-06, C-09, C-13]

### Illustrative worked example: a supply-bound route

A fictional turn-based expedition has a route that consumes two food units. In an isolated rule-comprehension probe, a traveller with three food can pay; one with one cannot; exactly two is permitted under the explicitly declared `available >= cost` rule. These are **proposed local test values**, not tuning advice. Ask for legality before asking whether to travel: someone who can pay may sensibly conserve food for a later known route. [C-08, C-10]

Now vary the situation, not the food rule: one route exposes a visible fire hazard that a carried water flask can neutralize; another spends more travel resources but preserves the flask. The generator proposal must check that it has not hidden the only required resource behind the obstacle it unlocks. A negative case contains the same nominal branching geometry but only one legal action after arrival resources are considered; calling that “two choices” would obscure the problem. [C-08, C-10]

After defeat, the illustrative design resets food and tools but retains discovered rule notes and chosen access settings. The note may state that water suppresses this hazard without preserving the previous map’s route as if it were still valid. Evaluate whether people apply the relation in a new arrangement; copying the old route is not the intended evidence. A design whose intended pleasure is undisclosed experimentation may choose a less explicit note and test the tradeoff rather than treating the note as mandatory. [C-07, C-08, C-11, C-14]

## Accessibility, ethics, localization and production

Map symbols, multiple simultaneous status effects, long command lists and historical messages can create separate perceptual, reading, memory and input demands. Candidate adaptations include configurable presentation, inspectable discovered-state summaries, interruption-safe progress and alternate input routes. An alternative must preserve the task’s facts without accidentally revealing hidden contents. None is certified effective by this draft. Keep ordinary access configuration outside a punitive reset, while separately deciding which gameplay assists alter an explicitly chosen challenge category. [C-11]

Localize rule terminology and compact logs as relationships, not only labels: an ambiguous “until next turn” may be insufficient when actions consume unequal time. Test screen-reader ordering or enlarged layouts for spatial facts rather than assuming that a list preserves adjacency. These are proposed review targets; no translated build or assistive technology was tested. [C-04, C-11]

On production, procedural content shifts work toward constraints, interaction coverage, failure reproduction and versioned seeds; it does not remove authored-content cost. A seed alone is not a complete reproduction record if generator version, content pool or initial state changed. Test documents should record those inputs. Permadeath is not permission to destroy unrelated saves/settings or to hide an inability to interrupt. Avoid using repeated losses as an unquestioned retention target; ask whether returning is wanted, informed and practically possible. [C-10, C-13]

## Research questions and proposed validation

**All tests below are proposed, not performed.** Recruit for relevant prior genre/rule knowledge, input and access needs, language and available session time; include people who stop or struggle. Choose a sample and practical-effect criterion before a separately authorized study, based on its question and uncertainty—not a universal participant minimum. [C-13]

| Test | Comparison and procedure | Measures, confounds and rejection condition |
|---|---|---|
| Stable-rule transfer | Compare authored repeat situations with constrained new arrangements using the same resource rule; include feasible, infeasible and exact-boundary probes. Ask prediction before preference. | Rule prediction, explanation, task facts perceived, action rationale. Prior spoiler knowledge and moderator hints confound results. Reject a learning claim if success is explained by memorized layouts or absent when those cues change. |
| Variation versus recombination | Compare content sets matched for available mechanics but differing in arrangement rules. Observe first and repeat attempts, retaining failed/uninteresting seeds. | Distinct reasons for choosing, dominated paths, avoidable versus unavoidable failures, repetition reports, authoring/debug effort. Reject the generation advantage if its extra defects/costs outweigh the locally valued decision differences. |
| Boundary understanding and re-entry | Compare a simple mode statement with a targeted state summary using matched defeat, abandon and suspend scenarios. Preserve access settings in both proposed versions. | Correct predictions for both lost and retained state, accidental exits, re-entry burden and unwanted spoilers. Reject expanded disclosure if it adds burden without addressing a documented misunderstanding. |

The strongest recommendation here—make the rule and loss boundary explicit enough to support informed adaptation—can conflict with desired mystery. Test player-account consequences separately from unknown fictional outcomes. A reasonable opposing result would favor a compact boundary statement plus optional detail, not either total opacity or an exhaustive tutorial. [C-08, C-13, C-14]

## Coverage and unresolved decisions

Researched: contested historical criteria; discrete/continuous distinctions; authored/procedural coexistence; selective loss and knowledge; conditional hybrid/access implications. Unresolved: actual build observations, generator distributions, longitudinal learning, varied cultural/console lineages, cooperative cases, and effects on populations with specific access needs. Selected later-wave shared dependencies are unavailable; source coverage is not heading completion.

Next discriminating decision: **Does the proposed project promise learning a stable systemic model, navigating a fixed world, overcoming execution demands, or accumulating retained capability—and which combination is actually intended?** Select an answer before choosing how much of the world or character to reset. This question does not authorize implementation or a playtest. [C-01, C-12, C-13]

## Claim ledger

Claims are local to this artifact. `observed-example` below means an inspected document/rule artifact unless a different route is explicitly given; it does not mean a game was played. Design recipes and proposed tests are not approved studio decisions.

| Claim | Precise claim / classification | Support and exact locator | Confidence and limiting question |
|---|---|---|---|
| C-01 | Use a declared roguelike tradition and a mechanical profile rather than a binary membership certificate. **`inference`** | `GDR-SRC-20261010-G16-001`, `GDR-SRC-20261010-G16-003`, `GDR-SRC-20261010-G16-004`; Berlin opening qualification; NetHack §6.4/§11; DCSS §N | **moderate: resolves the inspected conflicts without claiming consensus**. A lineage or market interpretation can remain useful for a different question; no population validation of this working boundary. |
| C-02 | The Berlin proposal weights characteristics but disclaims a necessary-and-sufficient test; contemporary replies dispute emphasis. **`practitioner-heuristic`** | `GDR-SRC-20261010-G16-001`, `GDR-SRC-20261010-G16-002`; Original opening and high/low factors; Darren Grey/David replies; mirror attribution | **high for what the inspected proposal says, not for its authority**. No formal issuing standard. Archive/mirror dates differ; preserve the dispute rather than deciding by repetition. |
| C-03 | NetHack 3.6.7 documents bones persistence and a non-scoring explore mode, so literal zero persistence is an inadequate summary. **`observed-example`** | `GDR-SRC-20261010-G16-003`; §6.4 Bones levels; §11 Explore mode | **high for this manual, narrow**. Not a tested build, current edition or proof that these exceptions improve experience. |
| C-04 | Turn-based state changes need not all consume identical simulated time; timing form should be specified separately from genre. **`observed-example`** | `GDR-SRC-20261010-G16-004`; §C “Attributes and stats”, “Time” | **high for the tagged manual**. Continuous/hybrid adaptations below are proposals; no motor or cognition outcomes established. |
| C-05 | DCSS discusses authored vaults, strategic variety and anti-grinding alongside procedural variation. **`practitioner-heuristic`** | `GDR-SRC-20261010-G16-004`; §N Balance, Anti-grinding, Replayability | **high as developer rationale, low as causal evidence**. Generation itself does not establish strategic novelty, fairness or lower production cost. |
| C-06 | A platformer creator can describe random restart worlds and systemic objects without reproducing all traditional roguelike criteria. **`observed-example`** | `GDR-SRC-20261010-G16-006`; Historical What’s Spelunky? description | **moderate: documentary hybrid contrast**. Complete persistence inventory and actual control timing unknown; not classifying the game by an unseen build. |
| C-07 | Represent loss separately for run state, world traces, persistent opportunities, recorded knowledge, player memory and access configuration. **`inference`** | `GDR-SRC-20261010-G16-003`, `GDR-CAND-20261010-F02-TOP-02`, `GDR-CAND-20261010-P01-TOP-02`; NetHack §§6.4,11; reviewed D03 persistence process; D05 settings scope | **moderate: distinctions follow from different documented state behaviors**. No claim that one reset policy works for all goals; the proposed complete pattern remains a hypothesis. |
| C-08 | Stable actionable rules plus varied situations may support transferable planning; remixed appearances alone may instead reward memorization or guesswork. **`hypothesis`** | `GDR-SRC-20261010-G16-004`, `GDR-CAND-20261010-F01-PAT-01`, `GDR-CAND-20261010-F02-TOP-01`; DCSS §N Clarity/Replayability; reviewed D01 corrected probes; D02 information contract | **low: no direct test of this combination**. Falsify with same-rule changed-state predictions and separate preference; explicitly identify any changed-rule condition. |
| C-09 | The inspected reset-location comparison did not support a simple monotonic ranking across all measured experiences. **`empirical-evidence`** | `GDR-SRC-20261010-G16-012`; Chapter 3 §§3.3,3.5–3.8.2, especially printed pp.36–37; Chapter 4 | **moderate for the narrow reported comparison; low transfer to roguelikes**. 72 adults in a short remote platformer study; no significant mastery/immersion/challenge differences is not equivalence. Long runs and metaprogression untested. |
| C-10 | The route/supplies example and conditional generator audit are illustrations, not observations or completed tests. **`hypothesis`** | Author’s explicit reasoning / proposed design, not an external result; Worked example and proposed tests in this artifact | **low: deliberately untested design**. Seed count, probabilities and viability thresholds require a separately approved study; no local generator executed. |
| C-11 | Access routes should preserve task-relevant facts and chosen uncertainty without forcing access settings to reset or expire. **`hypothesis`** | `GDR-CAND-20261010-P01-TOP-03`, `GDR-CAND-20261010-P01-TOP-02`, `GDR-CAND-20261010-F01-PAT-01`; Reviewed D04 task-wide access/scoped standards; D05 settings; D01 accommodations | **low for the proposed genre adaptation; moderate diagnostic rationale**. No native-game numeric thresholds imported from web criteria; actual target users and devices remain untested. |
| C-12 | A roguelike hybrid must expose conflicts among action timing, learned spatial structure, deck cycles and run loss rather than infer compatibility from tags. **`inference`** | `GDR-SRC-20261010-G16-004`, `GDR-SRC-20261010-G16-006`, `GDR-CAND-20261010-F02-TOP-01`; DCSS §C “Time”/§N; Spelunky description; D02 uncertainty and horizon | **moderate conceptual confidence**. Concrete conflict severity depends on a specified hybrid; no approved taxonomy change. |
| C-13 | Character/build/seed attribution, voluntary stopping and accessible re-entry need distinct evaluation outcomes. **`hypothesis`** | `GDR-CAND-20261010-F07-TOP-01`, `GDR-CAND-20261010-F07-PAT-02`; Reviewed D09 evidence-generating processes and methods; D08 interruption/refusal | **low for the proposed study, not performed**. Completion or repeat attempts alone cannot distinguish learning, compulsion, assistance, luck or preference. |
| C-14 | The strongest objection to explicit boundary guidance is that it can reveal wanted uncertainty or overburden experienced play. **`inference`** | `GDR-SRC-20261010-G16-001`, `GDR-SRC-20261010-G16-004`, `GDR-CAND-20261010-F02-TOP-01`; Berlin exploration factor; DCSS Clarity; D02 available versus intentionally unknown facts | **moderate: credible opposing mechanism, not measured effect**. Keep player-account consequences legible without automatically revealing unexplored fictional outcomes; test the tradeoff. |

## References

Access date for every record below: **2026-10-10** (task-local evidence date). A live page or historical rulebook does not certify the current game build. Source identities are temporary except the explicitly reused run-scoped F02 identity; all global allocation/deduplication remains pending.

### GDR-SRC-20261010-G16-001
**Jeff Lait, posting a community proposal; named replies treated separately. [Berlin Interpretation — original discussion thread](https://groups.google.com/g/rec.games.roguelike.development/c/Orq2_7HhMjI).** rec.games.roguelike.development; Google Groups archive. Publication/update: 2008; opening post displayed September 27; quoted reply headers use September 26. Edition/build: Archived 2008 thread; no immutable revision supplied.
**Inspected locator and access:** Opening statement, “High value factors” and “Low value factors”; Darren Grey reply on lineage/influence; David (dpeg) reply on incidental representations. `access: relevant-excerpt`. Type: Primary community/practitioner proposal and contemporary disagreement.
**Limits / provenance:** Not a normative standard, survey of all players, or causal study. Archive timestamps conflict with mirror attribution. The RogueBasin page is a derivative route to the same proposal, not independent confirmation. **Rights:** Individual post rights not independently established; paraphrase only; no contact details reproduced

### GDR-SRC-20261010-G16-002
**RogueBasin contributors. [Berlin Interpretation](https://roguebasin.com/index.php?title=Berlin_Interpretation).** RogueBasin. Publication/update: Underlying proposal 2008; page attribution says September 16, 2008; revision date unknown. Edition/build: Retrieved page reports oldid 54794.
**Inspected locator and access:** Lead paragraph; introductory qualification; high/low-value headings; revision footer. `access: relevant-excerpt`. Type: Derivative community transcription.
**Limits / provenance:** Used for provenance conflict and locating the original, not additional evidence of consensus. Derivative of GDR-SRC-20261010-G16-001; date discrepancy remains unresolved. **Rights:** Site/post rights not independently established; no substantial text copied

### GDR-SRC-20261010-G16-003
**Eric S. Raymond; edited and expanded by Mike Stephenson and others / NetHack Development Team. [A Guide to the Mazes of Menace (Guidebook for NetHack)](https://www.nethack.org/v367/Guidebook.html).** NetHack. Publication/update: February 3, 2023. Edition/build: NetHack 3.6.7 guidebook; page explicitly identifies this as an older version.
**Inspected locator and access:** §3 display/dungeon introduction; §6.4 Bones levels; §11 Explore mode. `access: relevant-excerpt`. Type: Primary official versioned manual.
**Limits / provenance:** Documentary behavior only. No executable, platform port or game session tested. Not current-version certification. Independent production example; game influence/lineage does not establish independent outcome evidence. **Rights:** Manual rights retained by contributors; paraphrase; no manual illustrations redistributed

### GDR-SRC-20261010-G16-004
**Dungeon Crawl Stone Soup contributors. [Dungeon Crawl Stone Soup manual](https://github.com/crawl/crawl/blob/0.32.1/crawl-ref/docs/crawl_manual.rst).** Dungeon Crawl Stone Soup official repository. Publication/update: Release/publication date of this tagged text not verified. Edition/build: Repository tag 0.32.1; crawl-ref/docs/crawl_manual.rst.
**Inspected locator and access:** §C “Attributes and stats”, “Time”; §N “Philosophy”: Balance, Anti-grinding, Interface, Clarity, Replayability. `access: relevant-excerpt`. Type: Primary versioned manual and developer rationale.
**Limits / provenance:** Documentation and stated design priorities, not measured player outcomes or a run of the game. Related to the roguelike tradition; not an empirical replication of the Berlin proposal. **Rights:** Repository licensing described in manual; exact component license not separately audited; no code redistributed

### GDR-SRC-20261010-G16-006
**Spelunky creator website / Mossmouth; inspected page has no explicit author byline. [What’s Spelunky?](https://spelunkyworld.com/whatis.html).** Spelunky official website. Publication/update: Unknown; historical text describes the forthcoming XBLA version. Edition/build: Historical PC/XBLA-era description; not Spelunky 2 or a tested build.
**Inspected locator and access:** Introductory platformer description; restart/random-level paragraph; destructible environments and object interaction paragraphs. `access: relevant-excerpt`. Type: Primary creator description.
**Limits / provenance:** No actual control timing, persistence inventory or procedural generator was tested. Promotional freshness language is not efficacy evidence. Separate production context; does not settle genre membership. **Rights:** Copyright retained by creator; paraphrase

### GDR-SRC-20261010-G16-012
**Marjorie Ann Mongado Cuerdo. [Fail and Retry: How Challenge Design in Platformer Games Relates to Player Experience and Traits](https://escholarship.org/content/qt58z477g6/qt58z477g6_noSplash_474ac9f98f9174fa3d0700b506d6819e.pdf).** University of California, Santa Cruz; eScholarship. Publication/update: June 2022. Edition/build: Master’s thesis, Computational Media; Chapter 3 study, not entire thesis reanalysis.
**Inspected locator and access:** §§3.3,3.5–3.8.2 (printed pp.28–37; PDF pp.36–45); Chapter 4 (printed pp.48–49); Fig.3.3 and results screenshots at printed pp.36–37. `access: relevant-excerpt`. Type: Primary empirical study report within thesis.
**Limits / provenance:** Remote 72-adult platformer study, four reset conditions; no roguelike/deckbuilder population. No raw data reanalysis. Internal heart/points descriptions disagree between §§3.3 and 3.7; not silently reconciled. Chapter 3 identifies the related 2021 CoG paper with Cuerdo, Mahajan and Melcer; same underlying study, not counted twice. **Rights:** Author copyright; paraphrase and scoped findings only; no participant data copied

## Review and history

Version **0.1.0**, revision **initial-author-draft-1**. First G16 submission found in this scoped work; no predecessor artifact is asserted. Assembly edits before first delivery do not create a new conceptual ID. Exact final hashes are in the [review packet](../reviews/full-run-20261010-g16-review-packet.md#candidate-byte-receipt); the packet’s hash is in its separate integrity receipt.

Author self-review is recorded in the packet and is **not independent review**. Independent evidence/content review is pending; local document checks do not constitute host retrieval tests. No research acceptance, permanent identity, publication, implementation or release is claimed. No player study, prototype or game session was performed by G16. Recommendations are reusable proposals, not adoption decisions for any particular game.

The inspected reviewed dependency snapshot remains **draft 0.1.0 / coverage-open**. Relevant exact revisions, hashes and limitations are recorded under [reviewed dependency transfer](../reviews/full-run-20261010-g16-review-packet.md#reviewed-dependency-transfer). Unavailable selected later-wave dependencies remain gaps, not implicit support. Additional pattern ideas are [queued proposals](../reviews/full-run-20261010-g16-review-packet.md#queued-child-proposals), with no child batch keys allocated or sent.

## Independent review correction, 2026-10-11 UTC

Corrected only the DCSS 0.32.1 Time source locators from §D to §C, Attributes and stats. The underlying timing claim is unchanged. The initial author history and packet remain historical records of predecessor bytes. Independent review scope, selected hashes and outstanding limits are in the companion G16 review receipt. Version 0.1.0, draft status, run-scoped identity, null approvals and all unperformed player/host validations remain unchanged. This is not release acceptance.
