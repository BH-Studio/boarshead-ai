---
id: GDR-CAND-20261010-G19-GEN-01
permanent_id: null
kind: genre
title: Rhythm
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
- rhythm game
- music-timing game
tags:
- timing
- chart-authoring
- calibration
- expression
- sensory-access
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G19-PAT-01
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G19-GEN-02
source_ids:
- GDR-SRC-20261010-G19-001
- GDR-SRC-20261010-G19-002
- GDR-SRC-20261010-G19-003
- GDR-SRC-20261010-G19-004
- GDR-SRC-20261010-G19-005
- GDR-SRC-20261010-G19-006
- GDR-SRC-20261010-G19-017
- GDR-SRC-20261010-G19-018
- GDR-SRC-20261010-G19-019
reviewer: null
approved_by: null
approved_date: null
byte_hash_record: ../reviews/full-run-20261010-g19-review-packet.md#candidate-byte-manifest
---

# Rhythm

**Draft research candidate, not released knowledge.** Scope: G19 only. Definitions and application recipes are reversible research proposals, not approved studio decisions. No game implementation, participant test, independent review or publication occurred in this batch.

## Definition and boundaries

For this entry, a **rhythm game** makes temporal relationships—pulse, phrasing, patterned intervals, anticipation or intentional timing variation—material to what the player does or expresses. A musical soundtrack alone does not qualify. Timing can be a prerequisite, a reward dimension, a coordination constraint or an expressive medium; these are not interchangeable promises. A rhythm-action hybrid may remain playable off-beat while rewarding synchronization. This is an operational research definition, not a canonical genre ruling. [R-01]

A **chart** here is the mapping between a musical/time structure and expected or available actions. It is distinct from an audio file, a beat detector, a generated environment and the display that previews actions. “Accuracy” must identify the scored reference: event onset, release, sustained alignment, selected pitch, gesture or something else. A **timing offset** changes a time relationship; **timing variability** is the spread or instability of that relationship. Reducing the latter is not accomplished merely by subtracting a constant from every event. These distinctions support the diagnostic proposal, not a specific engine implementation. [R-08, R-09]

Dance, instrument-like performance, single-switch timing, lane reading and rhythm-combat are useful research strata, not interchangeable samples. This batch directly inspects creator documentation for single-button, rhythm-shooter and expressive-pitch examples; dance/VR performance, arcade cabinets and expert tournament play remain gaps. Multiplayer, VR and mobile are facets rather than automatically separate genres. Party-rhythm should additionally consult [Party](party.md); its participation requirements may conflict with uninterrupted individual precision. [R-01, R-12]

## Custom research instructions

For a future rhythm investigation, first state whether the player should **predict a pattern, execute a prescribed action, interpret music, coordinate with others, or improvise**. Record which of those actually earns progress and which is merely advertised. Preserve distinctions between perceived pulse, annotated beat, note onset, sound onset and accepted input; do not call all of them “the beat.” [R-01, R-04, R-09]

Inspect authored charts and their music, chart-editor/export documentation, scoring rules, executable version and hardware path before explaining a numerical timing window. Seek failure cases on sparse or changing rhythms as well as regular pulse. Compare novice notation comprehension, familiar-chart memory and new-chart prediction separately. An expert demonstration cannot establish first-session legibility. A generated chart should be inspected as output, not inferred from an announcement that some content is procedural. [R-08, R-09, R-13]

Sample sensory and motor access needs independently, including people who use an alternative modality rather than only hearing participants with a channel muted. Compare continuous visual anticipation with transient visual events before declaring a modality hierarchy. Full tactile papers 017–018 and Soundfall session 019 remain leads, not validation. Do not translate a creator’s “learn rhythm” promise into educational transfer or a one-button control into universal motor accessibility. [R-03, R-04, R-05, R-14]

## Player promises and varied audiences

Candidate promises include satisfying temporal precision, discovering an intelligible musical pattern, expressive performance, and a shared activity that tolerates different proficiency. These are **design hypotheses to select with the intended audience**, not a claim that every rhythm player wants them simultaneously. A stricter score may serve a chosen mastery mode while undermining an improvisational session; an unscored mode can be appropriate without being a substitute for someone’s desired ranked challenge. [R-01, R-07, R-11]

Separate at least four questions in evaluation: Can the person perceive the relevant event? Can they work out the intended response? Can they execute it with their chosen input? Do they value the resulting experience? A correct prediction followed by a missed action is different from a misunderstood rhythm. None of those alone establishes enjoyment. Avoid diagnosing a person’s musical ability, motivation or impairment from misses. [R-04, R-13]

## Characteristic loops and structures

A useful analytic loop is **encounter a phrase → anticipate its action opportunity → act or deliberately deviate → receive timing/outcome information → adjust the next attempt**. Some designs emphasize memorizing a phrase; others reading a new chart or improvising around it. A session may be a complete song, a practice segment, a performance set or a mixed action level. Catalog progression and score pursuit can sit above this loop, but neither is required by this working definition. This structure is a synthesis, not an observed universal sequence. [R-01, R-05–R-07]

The production decision is which reference stays stable when a player retries. Repeating music while silently changing chart timing can make previous learning misleading. Conversely, deliberately generated variants can make prediction, rather than exact memorization, the intended challenge. Label which contract applies. Recovery should say whether progress, combo, score eligibility, musical continuity or shared play is reset; a single “failure” flag conceals these different consequences. [R-08, R-09, R-12]

## Mechanisms and design choices

### Separate synchronization diagnosis from difficulty selection

The osu! documentation distinguishes universal and beatmap-local adjustment and offers an Offset Wizard. That establishes an inspectable example of separate adjustment scopes, not a guarantee of accurate user calibration. [R-02; GDR-SRC-20261010-G19-001; GDR-SRC-20261010-G19-002]

The application bridge is conditional: when a consistent alignment problem affects multiple reliable reference passages, investigate the common presentation/input path; when it is confined to one chart passage, investigate that content before changing every song. When error is unstable, a fixed adjustment can shift its center without removing variability. When the person predicts correctly but cannot execute the demand, consider motor/task adaptation instead. A failed tap cannot, by itself, identify which explanation is correct. Use [Calibration–challenge separation](../patterns/calibration-challenge-separation.md), retaining its stop conditions. [R-08]

Offer calibration reversal and access to settings without requiring a scored success. Keep a user-selected challenge or assistance change separately named: correction of a timing relationship and widening an accepted-action window are not the same operation. Competitive score comparability requires an explicit mode policy, not a moral judgment about assistance. No universal latency budget, millisecond tolerance or device ranking is supplied here. [R-04, R-08, R-12]

### Preserve useful prediction without assuming auditory supremacy

Gan and colleagues’ main tapping experiments used small adult samples: 15 in the first and 14 analyzed in the second, with some overlap. Bouncing visual motion did not show the same disadvantage as a flash at the longer tested intervals; the fastest tested bouncing condition performed worse than tones. The study did not demonstrate formal equivalence, tactile access, game enjoyment or performance in deaf participants. Its timing intervals are experimental settings, **not recommended game windows**. [R-03; GDR-SRC-20261010-G19-006]

The bridge is to compare the *information available before an action*, not just whether a sound, flash or vibration exists. A moving cue may expose approach-to-contact; a brief event may only announce that time has arrived. A tactile signal could identify pulse yet fail to identify lane, duration or action type. Those are hypotheses requiring appropriate participants and hardware, not conclusions supplied by this paper. Alternate modes should declare which temporal information they preserve and what experience they change. [R-04, R-10, R-14]

### Author, generate, or combine charts deliberately

An authored chart can select musically meaningful moments while requiring labor for each arrangement, difficulty and access variant. A generated chart can offer coverage or variation while making musical interpretation and output validation separate responsibilities. These are proposed production tradeoffs, not measured cost savings. A hybrid workflow can generate a candidate, record its inputs/version, and require human audit of ambiguous segments; purely authored output is the simpler alternative when content volume is small. [R-09]

Audit three layers separately: **musical interpretation** (which pulse/phrase the designer intends), **action assignment** (what the player must do), and **presentation** (what information arrives before that action). An apparent sync problem may originate in any layer. An omitted note can be intentional phrasing rather than detector failure; a mathematically even grid need not match an intended expressive performance. Do not treat the generation of a Soundfall environment as evidence that an arbitrary note-chart generator is reliable. [R-06, R-09]

### Choose scoring and expression rather than conflating them

Strict temporal scoring, graded expressive output, forgiving completion and unscored performance are alternatives with different contracts. A freeplay mode can preserve exploration without pretending its outcomes are identical to a ranked run. Conversely, removing every consequence of timing can destroy the selected precision promise. Record whether a mistake changes the sound produced, merely the score, or the ability to continue; evaluate those changes separately. [R-07, R-11]

## Applying shared topics

The inspected shared material is reached through the [dependency receipt](../reviews/full-run-20261010-g19-review-packet.md#reviewed-dependencies), not an assumed cross-Project link. **P02-TOP-01** changes the rhythm diagnosis by separating acquisition, recognition and feedback timing; **F02-TOP-02** prevents treating perception, pattern knowledge and motor density as one difficulty slider. **P01-TOP-03** requires the full access task chain, including configuration and recovery. Its corrected WCAG/CSS numerical scope is preserved: no web target-size or contrast number is repurposed here as a musical timing requirement. [R-04, R-08]

**P02-TOP-03** and **P02-PAT-02** guide alternatives that preserve designated facts and uncertainty. **F01-TOP-03** and corrected **F01-PAT-01** guide onboarding: test a new instance of the same rule where the correct response differs, rather than counting repetition of the same answer as transfer. **F07-TOP-01** guides outcome separation and device-sensitive tests. No underlying shared-source result is asserted to have been reverified by this G19 inspection. [R-10, R-13]

Reviewed music-design, procedural-content and platform-specific measurement dependencies are not supplied as selected inspected entries. Their ownership and links remain pending. The audio-tension pilot is not evidence for rhythmic accuracy, musical pleasure or tactile equivalence. [R-14]

## Pattern selection and adaptations

Use **GDR-CAND-20261010-G19-PAT-01**, [Calibration–challenge separation](../patterns/calibration-challenge-separation.md), only where a timing reference and reversible adjustment can be distinguished from player performance. Do not apply it as mandatory personalization to a freeform instrument with no judged timing reference. [R-08, R-11]

Adapt inspected **GDR-CAND-20261010-P02-PAT-02**, *Fact-preserving cue alternatives*, to the event/phrase information actually required. Its potential overlap with **P01-PAT-01** remains unresolved; these are not two independent validations. For a party-rhythm round that eliminates contributors, **G19-PAT-02**, [Post-elimination participation contract](../patterns/post-elimination-participation-contract.md), may apply, but a non-eliminating or unscored group mode may be simpler. Do not force an eliminated person to continue performing for other players. [R-10–R-12]

## Representative and contrary cases

| Inspected artifact | What it makes worth investigating | Misleading conclusion to reject |
|---|---|---|
| Rhythm Doctor creator page | Single-button seventh-beat structure; handmade content/editor; local joining/leaving. [R-05] | One input means low temporal or cognitive demand; creator teaching intent proves learning. |
| Soundfall developer article | Rhythm rewards alongside spatial action; generated environments. [R-06] | Every action game with music is rhythm; procedural content proves chart validity. |
| Trombone Champ creator description | Continuous pitch expression can coexist with precision scoring and freeplay. [R-07] | Every rhythm action must be a fixed discrete note with failure on deviation. |
| Gan et al. experiment | Visual stimulus structure matters to a narrow synchronization result. [R-03] | All visual, audio and tactile cues are equivalent, or all rhythm should be auditory-only. |

These are deliberately selected boundary cases, not a representative market survey. No executable, full playthrough, player sample from these titles, chart file or shipping build was directly inspected. [R-14]

**Illustrative worked application—not a shipped observation:** A small performance prototype asks players to act at the end of a signaled phrase. A tester can point to the correct future event but regularly misses it on one setup. Keep the chart and scoring fixed, offer a reversible reference adjustment, and separately inspect whether the error remains stable across passages. A second tester reads the endpoint incorrectly: provide a supported explanation and then a new phrase with a different endpoint under the same rule. A third predicts correctly and aligns on a simple passage but cannot perform the denser action sequence: offer a lower motor-demand variant, not a hidden global shift. All three may still prefer different levels of challenge. No results are asserted. [R-04, R-08, R-13]

## Accessibility, ethics, localization and production

Access settings should be reachable before a performance and remain understandable without hearing the tutorial. Consider independently adjustable cue channels, remapping, sustained-action demands, effect intensity and recovery. A visually anticipatory alternative might compete with reading a chart; a haptic cue might conflict with other feedback or be unavailable on the chosen input. Test the task, not the option’s mere presence. No photosensitivity safety threshold or clinical claim is made. [R-04, R-10]

For localization, proposed audit fields include spoken count-in timing, written notation/terminology, subtitle placement, and whether translated instructions reveal an answer earlier than another channel. A culturally familiar song is not evidence that its pulse is equally legible to all audiences. Request relevant participant experience rather than inferring it from nationality or age. [R-09, R-10, R-13]

For production, budget chart review across variants and the supported hardware/configuration matrix; preserve reference assets so updates can be compared. Record rights clearance for music and player-generated charts as an external approval dependency, not legal clearance supplied by this research. Shared-device calibration, streaming delay and competitive verification are untested here. Avoid collecting recordings or diagnostic labels when simple consented timing/task measures answer the question. [R-08, R-09, R-12, R-14]

## Research questions and validation

All tests below are **proposed, not performed**. Participant count, meaningful-difference criterion and analysis must be chosen for the local question, variance and available resources; no default sample guarantees reliability.

| Question and comparison | Procedure and measures | Confounds and rejection rule |
|---|---|---|
| Does a scoped adjustment address a stable alignment problem better than a difficulty change? | Authorized later prototype: compare reversible reference adjustment, unchanged control and explicitly labeled assistance on the same passages. Separately collect prediction, signed error, variability, score and preference. | Practice, anticipation, reference error, device drift and demand changes can imitate improvement. Reject a hardware-correction interpretation if the reference is unverified or benefit is confined to memorized passages. [R-08] |
| Does an alternative cue preserve anticipatory information? | Compare selected primary/alternative channels and a designed channel-loss condition, keeping chart/event information specified. Include users for whom that alternative is intended; measure recognition, execution and comfort separately. | Visual motion and flashes are not equivalent stimuli; extra information is not a pure modality change. Reject the “same contract” claim if timing, hidden information or action type is changed without disclosure. [R-03, R-10] |
| Is a chart variant valid and worth its authoring cost? | Audit annotated musical choices and action demands, then test unfamiliar passages against an authored reference under matched scoring. Preserve disputed musical interpretations. | “More notes” confounds density and rhythm; familiarity confounds understanding. Reject automatic adoption when provenance or ambiguous passages cannot be audited. [R-09] |
| Is the player learning the rule rather than repeating one response? | Predict and perform contrasting new phrases governed by the same explained rule; include cases requiring different correct endpoints while retaining access supports. | Notation and motor changes can confound transfer. Revise the teaching interpretation if prediction does not discriminate cases even when repeated performance succeeds. [R-13] |

## Coverage checkpoint and next discriminating question

Researched: scope boundaries, timing versus difficulty diagnosis, cue-information distinctions, authored/generated chart decisions, expression/scoring alternatives, and proposed validation. Unresolved: tactile empirical body access; dance/VR and motion access; generated chart artifacts; current executable versions; device/network measurement; competitive comparability; localization evaluation; durable learning or enjoyment effects. The **next discriminating question** is whether the intended task failure comes from unavailable information, a misinterpreted pattern, execution demand or an unstable reference—before selecting an intervention. Contradictions `G19-X01` and `G19-X02` remain qualified, not resolved into universal rules.

## Claim ledger

Claim labels attach to the stated proposition, not every possible application of a cited title. An inference is not promoted to an empirical finding by borrowing a citation. Proposed tests are **not performed**.

| Claim | Proposition | Class | Sources | Locator / support and bridge | Confidence and scope | Open question / contrary case |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Working scope: rhythmic temporal structure materially organizes action or expression; music accompaniment alone is insufficient. | inference | GDR-SRC-20261010-G19-003; GDR-SRC-20261010-G19-004; GDR-SRC-20261010-G19-005 | Compare documented required timing, timing rewards and free-pitch expression; Definition and boundaries. | moderate: useful operational boundary, not a universal taxonomy | Does an ambiguous hybrid make rhythmic structure consequential enough for this entry? |
| R-02 | The inspected documentation distinguishes universal and local offset scope and describes an Offset Wizard. | observed-example | GDR-SRC-20261010-G19-001; GDR-SRC-20261010-G19-002 | Universal offset paragraphs 1–5 / Adjusting; Offset Wizard use. Interpretation of diagnosis is classified separately in R-08. | high for documentation; low for unmeasured devices | Which timing components does the actual target build adjust? |
| R-03 | In the inspected tapping experiments, visual-motion results depended on interval and stimulus, challenging unconditional audio superiority. | empirical-evidence | GDR-SRC-20261010-G19-006 | Results experiments 1–2; Methods Participants; Discussion. | moderate: narrow adult tapping study, not an equivalence trial or game access study | Does the comparison survive a different cue, device and participant population? |
| R-04 | Perceptual availability, motor execution, score and enjoyment should be evaluated separately. | inference | GDR-SRC-20261010-G19-006 | A tapping-stability outcome cannot establish enjoyment; reviewed P01-TOP-03 and F02-TOP-02 separate task demands. | moderate: construct separation is reasoned; project measurement design still needed | Which bottleneck actually prevents the intended experience? |
| R-05 | Rhythm Doctor documents a single-button seventh-beat premise, authored levels, editor and local drop-in/out co-op. | observed-example | GDR-SRC-20261010-G19-003 | Creator feature list; storefront metadata. | high for described features; executable unverified | No verified efficacy of musical instruction or broad single-input accessibility. |
| R-06 | Soundfall’s developer describes on-beat benefits in a rhythm-shooter and procedural environments. | observed-example | GDR-SRC-20261010-G19-004 | Opening gameplay explanation and co-op paragraph. | high for creator account; not runtime observation | Environment generation does not establish note-chart quality or network timing fairness. |
| R-07 | Trombone Champ’s creator description combines scored precision with free pitch and freeplay. | observed-example | GDR-SRC-20261010-G19-005 | About This Game / Controls. | high for storefront behavior description; no play session | Expression and precision need not be exclusive, but audience preferences are unmeasured. |
| R-08 | Diagnose stable timing bias, variable timing, local chart misalignment and task demand before selecting a remedy. | hypothesis | GDR-SRC-20261010-G19-001; GDR-SRC-20261010-G19-002 | Observed scope distinction supports separable interventions; PAT-01 supplies reasoning and exit conditions. | moderate for diagnostic logic; low for benefit of the complete recipe | Will diagnosis misattribute anticipation or motor variability to device error? |
| R-09 | Chart provenance and separate audit passes for musical interpretation, actions and presentation could expose different failure sources. | hypothesis | GDR-SRC-20261010-G19-003; GDR-SRC-20261010-G19-004 | Authored and generated-content examples motivate proposed audit; no study validates the pipeline. | low: production proposal | Can audit cost be justified for the intended catalog and variants? |
| R-10 | An alternate cue should preserve designated event timing and legitimate uncertainty without promising equal felt musicality. | inference | G19 reasoning / inspected dependencies | Inspected P02-TOP-03 and P02-PAT-02; G19 adaptation to rhythmic anticipation. | moderate for information contract; experiential equivalence unproven | Does the cue expose an otherwise hidden upcoming event or conceal a required accent? |
| R-11 | A reversible non-scoring or less-punitive route may preserve exploration when strict scoring is not the selected promise. | hypothesis | GDR-SRC-20261010-G19-005 | Free-expression counterexample motivates testing; no comparative benefit established. | low: audience- and mode-dependent | Could removing consequential timing erase the player’s chosen mastery goal? |
| R-12 | Local shared play, precision rankings and combat urgency can impose conflicting timing/recovery constraints. | inference | GDR-SRC-20261010-G19-003; GDR-SRC-20261010-G19-004; GDR-SRC-20261010-G19-005 | Different documented interaction structures plus inspected F02/P02 demand distinctions. | moderate for potential conflict; not a claim about bugs in these titles | Which rules stay common and which modes are explicitly different? |
| R-13 | Contrastive same-rule predictions are stronger onboarding probes than repeated success on one memorized answer. | inference | G19 reasoning / inspected dependencies | F01-PAT-01 corrected Recipe and example, lines 77–120; adaptation proposed here. | moderate: reviewed method transfer, not measured rhythm learning | Could notation reading or changed motor requirements confound the probe? |
| R-14 | Tactile equivalence, generated-chart reliability and current device/build performance remain unestablished in this batch. | inference | G19 reasoning / inspected dependencies | Access gaps 017–019; no runtime inspection, no participant tests. | high for this batch’s evidence boundary | Acquire full tactile papers and version-specific primary artifacts before stronger claims. |

## References

All access dates are **2026-10-11 UTC (2026-10-10 America/Los_Angeles)**. The observer is this G19 authoring session. Document observations are observations of the cited artifact, not runtime gameplay. Public works are paraphrased; copyright remains with authors/publishers, and redistribution licenses were not audited. No screenshots, source text copies, music, rulebooks or participant data are redistributed. Source IDs are temporary; cross-batch/global deduplication by URL/DOI/edition remains pending.

### GDR-SRC-20261010-G19-001

osu! wiki contributors. **Universal offset**. osu! wiki. Publication/update: unknown. [Inspected source or recorded lead](https://osu.ppy.sh/wiki/en/Offset/Universal_offset). Edition/build: live documentation; applicable executable build unverified. Access: `full`. Type: primary project documentation. Locator: Universal offset, paragraphs 1–5; Adjusting universal offset; parsed lines 15–34. Supports: R-02, R-08. Limits: Document behavior only; offset sign and effect are implementation-specific. No executable or device timing measured. Independence: Same wiki/source family as 002; not independent corroboration.

### GDR-SRC-20261010-G19-002

osu! wiki contributors. **Offset Wizard**. osu! wiki. Publication/update: unknown. [Inspected source or recorded lead](https://osu.ppy.sh/wiki/en/Client/Options/Offset_Wizard). Edition/build: live documentation; executable build unknown. Access: `full`. Type: primary project documentation. Locator: Offset Wizard description and use, parsed lines 15–24. Supports: R-02, R-08. Limits: Documented adjustment workflow; does not establish that player taps isolate hardware delay. Independence: Same project documentation family as 001.

### GDR-SRC-20261010-G19-003

7th Beat Games; creator account fizzd. **Rhythm Doctor**. itch.io creator page. Publication/update: unknown; storefront has mixed status/version metadata. [Inspected source or recorded lead](https://fizzd.itch.io/rhythm-doctor). Edition/build: page advertises download Version 1.0.1; executable not inspected; latest build not established. Access: `relevant-excerpt`. Type: creator-authored storefront. Locator: Creator description/features, lines 5–20; download/status metadata, lines 40–77; excludes user comments. Supports: R-01, R-05, R-09, R-12. Limits: Intent and features as described, not a played build, music-learning effect or accessibility result. Status and download labels are not reconciled. Independence: Firsthand product account, not independent player evidence.

### GDR-SRC-20261010-G19-004

Ben Mumford-Zisk, Director of Communications, Drastic Games. **The rhythm-based co-op of Soundfall hits PS5 and PS4 this spring**. PlayStation Blog. Publication/update: 2022-05-05. [Inspected source or recorded lead](https://blog.playstation.com/2022/05/05/the-rhythm-based-co-op-of-soundfall-hits-ps5-and-ps4-this-spring/). Edition/build: PS5/PS4 announcement context; runtime build unknown. Access: `relevant-excerpt`. Type: firsthand developer article. Locator: Author/date header; rhythm-action and procedural environment description, lines 58–59; co-op/freeplay paragraph, line 73. Supports: R-01, R-06, R-09, R-12. Limits: Generation of environments is not validation of generated note charts, beat tracking or netcode. Emotional language is creator intent. Independence: Same development context as lead 019; not independent validation.

### GDR-SRC-20261010-G19-005

Holy Wow Studios LLC. **Trombone Champ**. Steam, developer/publisher description. Publication/update: game release 2022-09-15; description revision unknown. [Inspected source or recorded lead](https://store.steampowered.com/app/1059990/Trombone_Champ/). Edition/build: desktop storefront; runtime version unknown. Access: `relevant-excerpt`. Type: creator-authored storefront. Locator: About This Game and Controls, parsed lines 132–157; developer/publisher and release metadata. Supports: R-01, R-07, R-11, R-12. Limits: Feature description only; no gameplay, reviews, popularity metrics or claimed world-first status used as evidence. Independence: Independent product context from other rhythm examples; no causal comparison.

### GDR-SRC-20261010-G19-006

Lingyu Gan; Yingyu Huang; Liang Zhou; Cheng Qian; Xiang Wu. **Synchronization to a bouncing ball with a realistic motion trajectory**. Scientific Reports 5, article 11974. Publication/update: 2015-07-07. [Inspected source or recorded lead](https://www.nature.com/articles/srep11974). Edition/build: DOI 10.1038/srep11974; original article. Access: `relevant-excerpt`. Type: original empirical research. Locator: Results: experiments 1 and 2, lines 91–110; Discussion, lines 151–162; Methods—Participants and Stimuli and procedure, lines 165–182. Supports: R-03, R-04. Limits: Main experiments recruited 15 each; experiment 2 analyzed 14; overlapping participation. Healthy-hearing adults; simple finger tapping, not game enjoyment or disability access. Figures, supplement and raw data not independently inspected. Independence: Original study; its cited earlier papers were not separately inspected. No claim of equivalence from nonsignificance.

### GDR-SRC-20261010-G19-017

Simon Andrew Whitton; Fang Jiang. **Sensorimotor synchronization with visual, auditory, and tactile modalities**. Psychological Research 87, 2204–2217. Publication/update: 2023-02-11. [Inspected source or recorded lead](https://link.springer.com/article/10.1007/s00426-023-01801-3). Edition/build: DOI 10.1007/s00426-023-01801-3. Access: `abstract-only`. Type: original research lead. Locator: Publisher abstract/metadata only; PMC10567517 full-body route returned a challenge page. Supports: no material claim; follow-up lead only. Limits: Publisher body is subscription-preview only; PMC full-body route returned a challenge page. No methods/results body inspected and no effect claims adopted. Independence: Separate sensory-timing study lead; not corroboration in this batch.

### GDR-SRC-20261010-G19-018

author not verified. **Can you feel the rhythm? Comparing vibrotactile and auditory stimuli in the rhythm video game Jump’n’Rhythm**. Behaviour & Information Technology / Taylor & Francis. Publication/update: 2023 from search metadata; exact publication date unverified. [Inspected source or recorded lead](https://www.tandfonline.com/doi/abs/10.1080/0144929X.2023.2243525). Edition/build: DOI 10.1080/0144929X.2023.2243525; edition not inspected. Access: `lead-only`. Type: research lead. Locator: Search metadata/abstract lead; publisher open returned HTTP 403. Supports: no material claim; follow-up lead only. Limits: No sample, method, results, haptic benefit or gameplay equivalence adopted. Independence: Independent study potentially relevant; unavailable support, not evidence triangulation.

### GDR-SRC-20261010-G19-019

Nick Cooper, Drastic Games. **Independent Games Summit: Hitting the Right Notes: Tying Gameplay to Music in Soundfall**. GDC Vault. Publication/update: 2023 conference year; session date unverified. [Inspected source or recorded lead](https://www.gdcvault.com/play/1029186/Independent-Games-Summit-Hitting-the). Edition/build: GDC 2023 session listing. Access: `lead-only`. Type: firsthand talk lead. Locator: Session metadata and overview only; recording/transcript not inspected. Supports: no material claim; follow-up lead only. Limits: No implementation, chart-generation, multiplayer synchronization or efficacy claims adopted from overview. Independence: Same studio as 004; viewing it later would not make it independent causal validation.

## Inspected shared-dependency records

These are **selected, parent-reviewed but unreleased draft bytes**, not newly validated public evidence. The original public sources behind them were not all reopened. Only the following scoped guidance transfers. Full receipt and missing links: [reviewed dependencies](../reviews/full-run-20261010-g19-review-packet.md#reviewed-dependencies). Dependency files are deliberately not reissued in this G19 delivery.

- **GDR-CAND-20261010-F01-TOP-03**, *Learning and onboarding*, version 0.1.0, revision `original`. Archive member `selected-drafts/topics/learning-and-onboarding.md`, lines 63–104. SHA-256 `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598`. Transfer: Separate rule understanding, input access, supported attempts and genuinely new applications.
- **GDR-CAND-20261010-F01-PAT-01**, *Supported attempt and transfer check*, version 0.1.0, revision `independent-review-correction-1`. Archive member `selected-drafts/patterns/supported-attempt-and-transfer-check.md`, lines 49–120; especially Recipe 77–94 and corrected example 98–120. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Transfer: Preserve same rule while varying correct responses; separate rule prediction from chosen preference and execution; never remove accommodations with hints.
- **GDR-CAND-20261010-F02-TOP-02**, *Challenge and difficulty*, version 0.1.0, revision `independent-review-correction-1`. Archive member `selected-drafts/topics/challenge-and-difficulty.md`, lines 61–99. SHA-256 `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1`. Transfer: Separate sensory, rule, planning, motor and social demands from failure punishment and recovery.
- **GDR-CAND-20261010-P01-TOP-03**, *Accessibility and inclusive interaction*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/accessibility-and-inclusive-interaction.md`, lines 56–103 and 243–265. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. Transfer: Task-chain access; preserve reviewed WCAG web/CSS scope and informative/vendor distinctions. No numerical defaults transferred.
- **GDR-CAND-20261010-P02-TOP-01**, *Controls and input*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/controls-and-input.md`, lines 77–94. SHA-256 `b9235153ba8b742c6df47e9e23844d9ab5da82e4212ebd22f04e314f6ccce21b`. Transfer: Distinguish input acquisition, recognition, eligibility and feedback; remapping is not removal of timing demand.
- **GDR-CAND-20261010-P02-TOP-03**, *Multimodal communication*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/topics/multimodal-communication.md`, lines 58–103. SHA-256 `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c`. Transfer: Preserve event facts, uncertainty, timing and audience; do not infer equal experience or broad benefit from extra channels.
- **GDR-CAND-20261010-P02-PAT-02**, *Fact-preserving cue alternatives*, version 0.1.0, revision `review-correction-1`. Archive member `selected-drafts/patterns/fact-preserving-cue-alternatives.md`, lines 50–138 and 264–270. SHA-256 `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0`. Transfer: Information contract, legitimate unknowns and channel loss; unresolved overlap with P01-PAT-01 retained.
- **GDR-CAND-20261010-F07-TOP-01**, *Evaluation and balancing*, version 0.1.0, revision `initial-capture-1`. Archive member `selected-drafts/topics/evaluation-and-balancing.md`, lines 65–93. SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`. Transfer: Define outcome/denominator and causal comparison; paper checks do not validate physical timing.

## Review and history

Version 0.1.0; candidate revision `initial-draft-1`; initial bounded G19 capture, no predecessor or superseded submitted artifact. Exact bytes are identified in the review packet; wording changes retain this conceptual ID and require a new revision/receipt. Author self-review is recorded in the packet and is not independent review. Gate C is pending; only local static packaging checks are performed, not Gate D host tests; Gate E/release and game adoption are not authorized. Coverage remains open. The next decision is whether the independent reviewer accepts this bounded evidence treatment or requests specific corrections before Coordination considers further work.
