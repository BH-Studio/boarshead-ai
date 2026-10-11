---
id: GDR-CAND-20261010-G13-GEN-02
kind: genre
title: Life simulation
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
- life sim
- everyday-life simulation
- household simulation
tags:
- identity
- relationships
- wishes
- time
- autonomy
- repetition
- coverage-open
related_topics:
- GDR-CAND-20261010-F01-TOP-01
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-W01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G13-PAT-01
- GDR-CAND-20261010-G13-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G13-GEN-01
- GDR-CAND-20261010-G13-GEN-03
source_ids:
- GDR-SRC-20261010-G13-006
- GDR-SRC-20261010-G13-007
- GDR-SRC-20261010-G13-008
- GDR-SRC-20261010-G13-015
- GDR-SRC-20261010-G13-016
reviewer: null
approved_by: null
approved_date: null
byte_hash_record: ../reviews/full-run-20261010-g13-integrity-receipt.md
---

# Life simulation

**Draft 0.1.0 · GDR-CAND-20261010-G13-GEN-02 · coverage-open.** This entry examines the design of everyday lives, relationships and change over time. It does not claim that such play improves mental health, social skills or education. Its inspected public evidence is concentrated in Sims creator material and an Animal Crossing developer interview; proposed guidance must not be mistaken for population research.

## Definition and boundaries

Here **life simulation** means a persistent arrangement of characters, activities and circumstances in which inhabiting, caring for, directing or interpreting everyday life is a central source of play. “Life” need not mean a photorealistic human household. A neighborhood, a stylized creature or a player-authored persona may qualify when continuing activities and relationships—not only a sequence of isolated choices—organize the experience. These are provisional boundaries, not a formal standard. Virtual-pet and mobile offline-care implementations were not inspected in this batch. [C-01]

The distinction from colony simulation is one of emphasis: an inhabitant's desired way of living can remain meaningful when it conflicts with collective throughput or survival optimization. A management loop does not become life simulation merely because workers have names. A dating-focused game may foreground one relationship structure without simulating broader daily life; a farming game may be primarily an economy, a life simulation or both. A visual novel can represent daily life through authored branches rather than persistent simulation. These differences call for conditional guidance, not exclusion by marketing label. [C-01]

Sandbox concerns the player's authority to define projects; it overlaps with life simulation but does not guarantee autonomous inhabitants. “Cozy,” multiplayer, platform, realism and tone must not substitute for an account of actual pressures and supported activities. There is no claim that all life-simulation players prefer low stakes, romance, domesticity, traditional families or accumulating wealth. [C-01, C-07]

## Custom research instructions

1. **Separate four sources of intention:** the player's current goal; a represented character's wish; a household or community constraint; and a reward that the designer uses to steer activity. Inspect what happens when these disagree. A displayed wish must not silently become a mandatory optimal objective. [C-02]
2. **Inspect the entire relationship model.** Identify initiation, refusal, reciprocity, memory, obligation, repair and disengagement where relevant. A single relationship score may be sufficient for one promise but misleading for another. Record whether a “no” is a meaningful outcome or merely a temporary obstacle to repeated optimization. [C-06, C-08]
3. **Audit identity from state to presentation.** Distinguish names, pronouns, appearance, attraction, relationship preferences and any changeability rules. Inspect animation, dialogue, generated reports and save migration—not only character creation. Do not treat one included option as proof that all identities or languages are supported. [C-05, C-10]
4. **Identify every clock.** Distinguish accelerated simulation time, real-world calendar time, session-based turns and offline progress. Record what changes during absence, whose schedule determines access, and whether the player can predict the consequences of stopping. [C-04, C-09]
5. **Investigate repetition without assuming it is a defect.** Compare ritual, expressive variation, upkeep and compulsory repetition. Ask which interaction the player wants to repeat and which is merely a prerequisite for something else. Do not substitute session length or streak completion for endorsed participation. [C-07, C-09]
6. **Seek contrary audiences and implementations.** Include story directors who protect every major event, spectators who invite surprise, players who avoid romance or family progression, and users whose available play times conflict with a calendar. The present sources do not establish their relative prevalence. [C-07, C-11]

Important primary routes for further work include actual versioned settings, authored character-state documentation, developer explanations of clocks, original user studies and locale-specific production records. A failed attempt to retrieve the July 2022 Wants and Fears patch note is recorded as a lead, not quietly replaced with forum memory. “Wish” below is this entry's analytic term; no exact Sims Wants/Fears algorithm is asserted. [C-02]

## Player promises and varied audiences

Candidate promises include inhabiting a personally meaningful role, directing a household narrative, noticing an independently changing neighborhood, maintaining a satisfying ritual and expressing relationships or identity. These can conflict. A director may want to protect a particular character's future, while a spectator may value an unplanned move. A builder may prefer ordinary life to remain stable while revising a home. The presence of customization controls alone does not tell us which experience occurred. [C-07]

A creator account offers a concrete starting point: the Sims Neighborhood Stories article describes different configurations for household groups and individual households, with settings stored per save. It illustrates how a game can distinguish protected stories from autonomous background change. No independent evidence here establishes that this configuration improved agency or reduced unwanted outcomes. [C-03; GDR-SRC-20261010-G13-006]

## Characteristic loops and structures

A proposed daily loop is **notice an intention or circumstance → allocate time and attention → act or decline → encounter another agent or system response → interpret the change → choose what matters next**. A longer loop may concern skill, livelihood, a relationship, a place, care, continuity or a change in self-understanding. A daily action can serve several horizons without every horizon needing a score. [C-02, C-07]

The same meal interaction could be an upkeep demand, a social occasion, an authored ritual or background automation. Its cost and repetition should follow that role. Automating an unwanted prerequisite may help one player pursue a chosen project while removing a valued ritual for another. This is a testable design alternative, not evidence that automation is inherently respectful or that repetition is inherently manipulative. [C-07, C-09]

### Mechanisms and practical choices

| Decision | Proposed mechanism and application | Alternative or counterpressure |
|---|---|---|
| Character wishes versus player projects | Mark a wish as a character signal; let the player interpret, pursue, postpone or reject it when that matches the promise | A tightly authored persona may properly constrain choices. Do not promise complete self-authorship and then require a contradictory aspiration. |
| Directorial versus background autonomy | Scope consequential autonomous changes by affected group or individual, then show the effective policy | Complete control can flatten surprise; many fine-grained settings can become labor. A small understandable preset may be sufficient. |
| Relationship score versus distinct conditions | Use separate states only where they change understandable responses, such as availability versus affection | Additional variables can become inscrutable or imply false psychological precision. A simple openly fictional abstraction may be preferable. |
| Simulation clock versus calendar clock | Match time structure to the intended rituals and available play opportunities | Real-time continuity can create a valued shared rhythm while excluding some schedules. Session-relative time removes that conflict but changes the promise. |
| Repeating care versus optional automation | Preserve the part that expresses a chosen relationship; automate or compress redundant setup only after examining its role | A mandatory automation path can erase embodiment or discovery; routine can be the experience, not a problem to optimize away. |
| Identity flexibility versus continuity | Declare which fields the player authors, which may change, and what associated text or rules update | Editable presentation without corresponding systemic support can break the stated promise. A limited explicit scope is more honest than “fully inclusive.” |

These mechanisms are proposed in C-02 and C-06–C-10. They have not been validated as a complete recipe. The strongest recommendation is **to make player goals, character wishes and autonomous-change permissions distinguishable before adding more life-management variables**. The evidence supports the existence of separable choices, not their causal superiority. [C-02, C-03, C-07]

## Applying the guidance

Start with a concrete player intention, such as keeping a household stable while another neighborhood evolves. State which changes the player authors, which a character may initiate, and which are external conditions. Identify a conflicting case—such as a profitable action that the player does not wish to choose—and ensure the research does not score that preference as incompetence. [C-02, C-07]

Next, draw one daily and one long-horizon sequence. Mark time costs, missed opportunities, refusal, re-entry after absence and any irreversible change. Check whether narrative presentation turns an optional activity into an implied moral obligation. A clear cost label may not neutralize social pressure communicated by a disappointed character. The solution may be a different consequence or tone rather than another confirmation screen. [C-04, C-08, C-09]

Choose a simple alternative as a comparator: fewer wishes, one explicit autonomy preset, ordinary on-demand history, or a clock offset. Then plan tests that distinguish correct prediction, chosen action and interpretation. Add detail only when it enables a supported intention or a valued ambiguity at acceptable cost. This is proposed application guidance; no game change is authorized here. [C-11]

## Representative cases and counterexamples

**Animal Crossing: New Leaf — preserving a clock while changing access.** In Nintendo's interview, Kyogoku describes coming home after a shop had closed; the discussion connects adjustable business hours with preserving real-world day/night differences. That is a firsthand rationale for adapting a calendar rather than removing it. It does not establish how common the access problem was or prove that the solution accommodated every schedule. [C-04; GDR-SRC-20261010-G13-008]

**Optionality with a social cost.** The same interview describes declining a ceremony and the character's dejected response. This is a useful counterexample to treating a visible refusal button as evidence of emotionally neutral refusal. The actual player effect, including whether someone enjoys that characterization, remains unknown. No claim about vulnerable populations follows from the interview. [C-08; GDR-SRC-20261010-G13-008]

**The Sims 4 — representation is not one field.** The July 2022 design account distinguishes attraction-related parameters and acknowledges binary architectural limitations at that time. The May 2022 official team announcement separately documents an English-first pronoun feature and remaining grammatical/gendered-language limits. These are historical implementation boundaries, not a verdict on current support or evidence of audience outcomes. [C-05; GDR-SRC-20261010-G13-007; GDR-SRC-20261010-G13-016]

**Illustrative worked example: the evening studio.** This is an invented design exercise. One housemate would like a party, another needs a quiet period, the household could earn more money through an evening commission, and the player wants to finish a portrait. All four intentions are plausible, but none is automatically the game's single correct objective. [C-02]

A proposed presentation distinguishes the party wish, the quiet condition, the commission's opportunity cost and the player's pinned portrait project. The player can accurately predict that accepting the commission postpones the portrait and still decline it. Later, a non-played household considers moving away. A save-level policy permits ordinary visits while a household-specific rule protects relocation. The interface reports that effective rule; it does not claim that the simulated household “consented” on behalf of a real person. [C-02, C-03, C-12]

Compare a simpler version that offers no wish generator and only clear household conditions. The more elaborate version is justified only when it supports the intended characterization or choice. A drama-focused version could instead allow the move without prior approval and offer a truthful event history. These are competing promises, not a correct mode and an inferior accessibility mode. [C-07, C-11]

## Applying shared topics

See the [reviewed dependency manifest](../reviews/full-run-20261010-g13-review-packet.md#reviewed-dependency-manifest) for inspected sections, revisions and hashes. These are transfers from reviewed drafts, not direct reinspection of their underlying external evidence.

| Shared entry | Life-simulation change in emphasis |
|---|---|
| `GDR-CAND-20261010-F01-TOP-01`, Player experience and motivation | A player may understand a career or relationship incentive yet decline it for a self-authored life; optimization cannot stand in for chosen meaning. |
| `GDR-CAND-20261010-W01-TOP-03`, Character design | Keep inferred motive, liking and relationship interpretation distinct. A believable refusal is not a universal demand for more friction. |
| `GDR-CAND-20261010-P01-TOP-02`, Interface and information | Expose which autonomy configuration actually applies rather than merely where settings are stored. |
| `GDR-CAND-20261010-P01-TOP-03`, Accessibility and inclusive interaction, corrected | Test the complete character-creation, daily-play and re-entry path. A difficulty preset is not a substitute for readable relationship text or operable time controls. No generic native-game numerical values are imported. |
| `GDR-CAND-20261010-F01-TOP-03` and corrected `GDR-CAND-20261010-F01-PAT-01` | Use contrastive cases with different correct predictions; keep those predictions separate from a preferred fictional life. |
| `GDR-CAND-20261010-F07-TOP-01`, Evaluation and balancing | Distinguish useful diagnosis from estimating prevalence or demonstrating long-term effects. |
| `GDR-CAND-20261010-F07-PAT-02`, Legible commitment and safe exit | A technically available decline and understandable consequences are separate concerns. Do not infer wellbeing or voluntary preference from acceptance alone. |

Detailed clock/session, relationship-system interface, economy, localization and G12 parent guidance is not transferred from unseen later batches. [C-08–C-11]

## Pattern selection and hybrid conflicts

[Scoped autonomous changes](../patterns/scoped-autonomous-changes.md), `GDR-CAND-20261010-G13-PAT-01`, is especially relevant to background life change and rotational households. The proposed unit is an event class over a clear scope, not every autonomous social action. Protected identity/representation and optional events should not be conflated: an event-permission system is not a justification for erasing identities from a world. [C-12]

[Reversible experiment branch](../patterns/reversible-experiment-branch.md), `GDR-CAND-20261010-G13-PAT-02`, may support trying a household layout or scenario in a separate state. Restoring a save cannot erase what a player learned about a relationship. Avoid offering it as universal repair for a story whose meaning depends on consequences. [C-13]

A colony/life hybrid can make communal need urgent while preserving character-specific preferences; do not silently mark everyone who resists productive work as defective. A sandbox/life hybrid can permit home editing while keeping interpersonal consequences meaningful. A multiplayer life simulation adds real participants' permissions and shared-history questions that fictional autonomy settings do not settle. Those are unresolved design obligations, not assessed platform compliance. [C-01, C-08, C-12]

## Accessibility, ethics, localization and production implications

Time controls, schedules, relationship histories and context-sensitive language require testing together. A readable relationship meter does not make its categories understandable. A paused simulation may still contain an inaccessible menu or an off-screen real-time deadline. Distinguish disabled input, elapsed simulation time and continued external activity in any proposed re-entry test. [C-09, C-10]

Localization should inspect the semantic roles of names, pronouns, kinship, partnership and collective references. Replacing a pronoun token does not establish that every surrounding sentence supports that form or that a binary data model has become nonbinary. The exact language work should be directed by relevant localization expertise and reviewed against the declared support scope; no universal grammar solution is supplied. [C-05, C-10]

Do not infer sensitive facts about a player from avatar choices or require disclosure of personal identity to assess whether a fictional option works. Proposed participants can use invented scenarios. Evaluate actual supported alternatives to stereotyped life paths rather than presuming marriage, children, wealth or social popularity to be necessary progress. This is an author-proposed ethical lens, not a proven player-wellbeing intervention. [C-08, C-10]

Persistent identity and relationship systems carry compatibility and content-combination obligations across authored text, autonomous events and old saves. Extra settings also create explanation and regression costs. Simplifying the model or explicitly narrowing the feature may be preferable to promising more permutations than the team can maintain; costs have not been estimated. [C-10]

## Research questions and validation

**Proposed / NOT PERFORMED.** All studies require separate authorization, consent and an appropriate participant/sample plan. No clinical or educational endpoint is inferred from gameplay behavior. [C-11]

| Question | Comparison, procedure and measures | Confounds / decision rule |
|---|---|---|
| Are wishes interpreted as character information or compulsory chores? | Compare a minimal conditions display, optional wishes and explicitly mandatory objectives using the same actions. Ask for allowed-action predictions before asking for the player's chosen project; record perceived obligation separately. | Reward values, wording, character appeal and moderator framing can confound the comparison. Reject the optional-wish design if it persistently implies an unintended obligation or adds no useful distinction. |
| Can players predict autonomous change? | Compare a coarse autonomy preset with scoped configurations in matched fictional households. Include a group default, an overriding household rule and a queued event. Measure effective-policy prediction and ability to change it. | Random non-occurrence is not proof that a prohibition worked. Use known scenarios; reject a design that produces confident misprediction or unwanted protected changes. |
| Does the clock fit the intended activity? | Compare session-relative time, calendar time and a schedule adaptation across declared availability contexts. Observe missed access, chosen rituals, interruptions and re-entry understanding. | Laboratory absence is not naturalistic absence. Do not generalize a short session to months of routine; choose the clock that supports the promise, not merely the highest return rate. |
| Does identity support survive ordinary play? | Test fictional identity combinations across creation, refusal, household changes and generated text in supported locales and access routes. Record mismatches and successful alternatives. | Do not turn personal identity into a demographic score. Any promised form that fails is a scope/quality issue even when averages look favorable. |

### Coverage checkpoint

Researched: intention conflicts, daily/long horizons, relationships/refusal, background autonomy, identity fields, clock tradeoffs, repetition and localization boundaries. Unresolved: the actual Wants/Fears algorithm, farming and virtual-pet subfamilies, current non-English implementations, long-term audience effects, real multiplayer norms, offline-care consequences and production costs. Next discriminator: can someone correctly predict the world rule while choosing a life the reward system does not optimize? The answer must not be conflated with task failure. [C-02, C-11]

## Claim ledger

Confidence applies to the stated claim, not to the genre as a whole. Documentation observations are observations of published artifacts, not direct game observations. Recommendations not approved by Doug are `inference` or `hypothesis`, not `studio-decision`.

| Claim | Precise statement and classification | Support / locator | Confidence and reason | Limits / next discriminator |
|---|---|---|---|---|
| C-01 | **`inference`** — Life simulation is provisionally defined by persistent everyday lives and their interpretation; neighboring labels overlap conditionally. | G13 brief §Domain questions; sources 006–008; original boundary analysis. | Moderate: useful emphasis, not exhaustive membership criteria. | No approved taxonomy amendment; virtual-pet/farming/mobile variants not inspected. |
| C-02 | **`inference`** — Player goals, character wishes, household constraints and designer incentives should be analytically separated. | Reviewed F01-TOP-01 §Decision and scope; W01-TOP-03 §Core explanation; illustrative evening-studio example. | Moderate: distinctions are logically useful; benefit of displaying all four is untested. | Wish is an analytic term; source 015 is lead-only and supports no Sims implementation claim. |
| C-03 | **`observed-example`** — The inspected Neighborhood Stories page documents group and household configurations with per-save settings. | GDR-SRC-20261010-G13-006, “Configuring Neighborhood Stories”. | High for the published artifact. | No runtime verification or causal agency/comfort effect; page revision history unknown. |
| C-04 | **`practitioner-heuristic`** — Nintendo’s interview describes adapting shop hours while retaining real-world time distinctions. | GDR-SRC-20261010-G13-008, opening Kyogoku/Moro discussion, lines 18–40. | Moderate: firsthand rationale, not a representative study. | No estimate of exclusion prevalence or proof of accommodation for every schedule. |
| C-05 | **`observed-example`** — Historical Sims creator documents disclose distinct identity-related features and architecture/language limits. | GDR-SRC-20261010-G13-007, “How It Works”/gender-options FAQ; GDR-SRC-20261010-G13-016, 2022-05-24 feature section. | High for documented historical scope, not current support. | Two documents from one production family; no inclusive-outcome validation. |
| C-06 | **`inference`** — Relationship variables should be added only when they support meaningful distinct responses, not as purported human truths. | Reviewed W01-TOP-03 §Core explanation; C-02/C-05; original alternatives matrix. | Moderate: explicit representation tradeoff. | A scalar model can be appropriate; richer models may be harder to interpret. |
| C-07 | **`hypothesis`** — Separating intentions and configurable authority may support varied life-play promises better than adding management variables. | C-02–C-06; source 006 demonstrates configurability, not efficacy. | Low: no matched outcome study of the recommendation. | Reject when simplification removes desired characterization or controls create unwanted work. |
| C-08 | **`inference`** — A refusal route and player-endorsed participation are different questions; social framing and identity assumptions require review. | GDR-SRC-20261010-G13-008, optional ceremony exchange, lines 149–168; reviewed F07-PAT-02 prerequisites/counterexamples. | Moderate: distinction supported by competing possible interpretations. | No claim that a disappointed fictional character universally harms or coerces players. |
| C-09 | **`hypothesis`** — Clock and repetition choices should follow the intended ritual and access context rather than a universal retention rule. | GDR-SRC-20261010-G13-008, clock rationale; original clock/repetition comparisons. | Low: no longitudinal or cross-context effect test. | More visits do not establish endorsed participation; calendar and session clocks support different promises. |
| C-10 | **`inference`** — Identity, access, localization and persistence require end-to-end support rather than a character-creation checkbox alone. | GDR-SRC-20261010-G13-007, binary architecture FAQ; GDR-SRC-20261010-G13-016, language/grammar limits; reviewed P01-TOP-03 scope/process. | Moderate: concrete historical limitations motivate the review path. | No legal certification, cost estimate, universal linguistic prescription or current-game audit. |
| C-11 | **`hypothesis`** — Proposed validation separates correct rule prediction, chosen action, interpretation and longer-term outcomes. | Reviewed corrected F01-PAT-01 worked examples/§Playtest; F07-TOP-01 §Playtest; original protocols. | Moderate for logic, unvalidated as a protocol. | All tests not performed; no invented sample, power or efficacy claim. |
| C-12 | **`hypothesis`** — Scoped event permissions may help directorial and autonomous play coexist without authorizing every ordinary action. | GDR-SRC-20261010-G13-006, configuration scope; local G13 PAT-01; source 007 limits the identity-toggle analogy. | Low: complete pattern and cross-genre transfer untested. | Permission cannot settle real participants’ consent or justify erasing identities. |
| C-13 | **`hypothesis`** — Experiment branches can be considered for layouts but cannot undo player knowledge or guarantee narrative recovery. | Local G13 PAT-02; original life-simulation adaptation. | Low for application benefit; knowledge irreversibility is a logical limitation. | Avoid when maintaining an unbroken consequential history is the intended promise. |

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

### GDR-SRC-20261010-G13-008

**Nintendo; Iwata Asks interview with Animal Crossing: New Leaf developers. Iwata Asks: Animal Crossing: New Leaf — 2. Being the Mayor.** Publication/update: unknown on inspected page. Publisher: the organization named above (Steam hosts source 005). [Source](https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Animal-Crossing-New-Leaf/Animal-Crossing-New-Leaf/2-Being-the-Mayor/2-Being-the-Mayor-738645.html).

**Edition/build:** Animal Crossing: New Leaf / Nintendo 3DS-era interview; exact build unknown. **Access:** `relevant-excerpt`. **Inspection route:** Public primary HTML text inspected through web retrieval. **Type:** Firsthand developer interview.

**Exact locator:** Opening Kyogoku/Moro exchanges on shop hours and real-world time, lines 18–40; mayor duties, lines 72–95; optional ceremony and dejected response, lines 149–168. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Creator experience and design rationale, not representative player evidence. Do not generalize the interview’s demographic anecdotes or emotional predictions. **Independence/provenance:** Independent production family. US interview mirror timed out; UK official mirror supplied inspected text under this same source identity.

### GDR-SRC-20261010-G13-015

**The Sims Team / Electronic Arts (attribution from indexed lead). Update 07/26/2022.** Publication/update: 2022-07-26 (indexed title/date). Publisher: the organization named above (Steam hosts source 005). [Source](https://www.ea.com/ea-originals/news/update-07-26-2022).

**Edition/build:** Indexed historical patch note; body not retrieved. **Access:** `lead-only`. **Inspection route:** Indexed result located; article opening failed and alternate route returned 404. **Type:** Official patch-note lead.

**Exact locator:** No inspected body locator. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Search text mentioned Wants and Fears, but opening failed. The alternate games/the-sims route returned 404. Do not cite this lead as proof of feature behavior. **Independence/provenance:** Same publisher/franchise as 006/007/016.

### GDR-SRC-20261010-G13-016

**EA_Cade, identified as The Sims Team / Electronic Arts. Customizable Pronouns are Now Available in English.** Publication/update: 2022-05-24 (embedded update date). Publisher: the organization named above (Steam hosts source 005). [Source](https://forums.ea.com/discussions/the-sims-4-gameplay-en/customizable-pronouns-are-now-available-in-english/8633216).

**Edition/build:** PC 1.88.213.1030; Mac 1.88.213.1230; console 1.59, as specified in historical announcement. **Access:** `relevant-excerpt`. **Inspection route:** Public primary HTML text inspected through web retrieval. **Type:** Official team patch announcement on EA Forums.

**Exact locator:** Official team rank/byline and update versions, lines 16–27; “Customizable Pronouns Now Available in Create A Sim”, lines 40–49. **Claims supported:** only the local claim-ledger rows that name this ID; `lead-only` records support no substantive claim.

**Limits:** Historical English-first scope and acknowledged grammatical/gendered-language gaps only. Team assertion of testing is not independent validation. No claim about current locale coverage. **Independence/provenance:** Official team repost/announcement in same Sims production family; not a separate player study.


## Review and history

2026-10-10, `initial-capture-1`: initial complete author draft for G13. Version remains `0.1.0`; predecessor/supersession are null, not a claim that a canonical registry was searched exhaustively. Author self-review is in the [G13 packet](../reviews/full-run-20261010-g13-review-packet.md#author-self-review). Independent review has not occurred for this candidate. No participant tests, executable game observations, implementation, release or adoption occurred.

Exact bytes are recorded outside this file in the [integrity receipt](../reviews/full-run-20261010-g13-integrity-receipt.md). Existing upstream IDs, revisions and source meanings remain unchanged. This draft adds no permanent IDs and does not supersede a reviewed dependency.
