---
id: GDR-CAND-20261010-G04-GEN-01
kind: genre
title: Shooter
version: 0.1.0
candidate_revision: initial-capture-1
status: draft
run_id: GDR-FULL-20261010
batch_key: G04
attempt_id: G04-authoring-01
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- shooting-centered game
- FPS family
- third-person shooter family
tags:
- aiming
- execution
- spatial-attention
- weapon-roles
- assistance
- genre-boundaries
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G04-PAT-01
- GDR-CAND-20261010-G04-PAT-02
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G04-GEN-02
- GDR-CAND-20261010-G04-GEN-03
source_ids:
- GDR-SRC-20261010-G04-003
- GDR-SRC-20261010-G04-002
- GDR-SRC-20261010-G04-004
- GDR-SRC-20261010-G04-005
- GDR-SRC-20261010-G04-014
- GDR-SRC-20261010-P02-001
- GDR-SRC-20261010-P02-005
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G04 capture; no prior G04 candidate superseded.
byte_hash_record: ../reviews/full-run-20261010-g04-integrity-receipt.md
coverage_state: bounded-research-completed-coverage-open
independent_review: not-performed-for-G04
---

# Shooter

**Version 0.1.0 · initial-capture-1 · draft · coverage open.** This file is genre-specific research guidance, not a released standard, a complete history of shooters or a game implementation specification. Public documents were inspected; no game, recording, prototype or participant test was run.

## Definition and boundaries

For this entry, a **shooter** is a game or substantial mode in which directing shots or shot-like ranged actions is a recurring, consequential part of player-controlled execution. “Shot-like” includes deliberately aimed projectiles or rays whose placement, timing or target selection changes the task. This is a proposed analytic definition, not a genre authority’s formal rule. A photograph mechanic, automatic turret economy or occasional weapon in an adventure does not establish membership by itself: ask what the player repeatedly decides and executes. [C-01]

First-person and third-person cameras, top-down presentation, single-player, cooperative and competitive play are facets. Arena control, arcade pattern avoidance, campaign encounter management and objective-oriented shooting may share the family while requiring different priorities. [Tactical shooter](tactical-shooter.md) changes the commitment and information analysis; [extraction game](extraction-game.md) changes what leaves the session and who bears loss. Neither replaces this parent’s aiming and feedback analysis. Violent theme is not a logical prerequisite: an illustrative target-painting or rescue-delivery game could fit. Nintendo’s ink-combat example challenges military and kill-score assumptions, but is **not evidence that Splatoon is literally nonviolent**. [C-01, C-02]

**Membership boundary test:** remove directed shots while preserving movement and objectives. If the distinctive recurring challenge survives essentially unchanged, another genre may own the central guidance. This is a reversible research diagnostic, not a numerical quota of play time. Auto-aim and access assistance do not automatically remove membership when consequential targeting, timing or positioning remains. [C-01, C-09]

## Custom research instructions

For each investigated shooter mode, record the rules version, camera, device and access configuration, target behavior, friendly/neutral entities, objective and failure/recovery model. Identify whether the task is target acquisition, sustained tracking, prediction, target discrimination, timing, spatial route choice or a combination; do not substitute a single accuracy percentage for all of these demands. [C-03, C-04, C-06]

Research a representative **range**, not a prestige ranking: campaign resource combat, arena pickups, cooperative objective defense, arcade/projectile avoidance and a third-person or non-military scoring context. Include negative cases in which precise aim is not the main bottleneck. This batch inspects official examples of several of these structures, but does not supply a current arcade build observation or comparative first/third-person dataset. Seek such evidence before generalizing across that gap. [C-01, C-02, C-10]

For claims about hit behavior, obtain authoritative rules or a reproducible trace tied to a build; distinguish a developer’s diagnosis from a player’s perception. For causal claims about assistance, inspect methods and outcomes in an original study, then test the actual weapon, scene, device and population. Do not use shooting-range performance, creator popularity, player reviews or a successful game’s existence as proof of combat fairness or satisfaction. [C-04, C-05, C-11]

Challenge these misleading comparisons explicitly: hitscan versus projectile is not immediate versus network-delayed confirmation; fast elimination is not tactical depth; visual realism is not target legibility; more feedback is not more accurate feedback; an accessibility option is not automatically a difficulty or matchmaking policy. [C-03–C-06, C-09]

## Player promises and varied audiences

Treat the following as **candidate promises to elicit**, not facts about every shooter player: expressing precision; reading and escaping a projectile field; making weapons complement movement; supporting teammates; controlling useful territory; or feeling competent while experiencing a campaign. A player may value one and dislike another. Spectacle, military simulation, competitive ranking and sustained tension are optional rather than implied promises. [C-01, C-07, C-09]

Ask separately what a person wants to choose, what they want to execute manually, and what physical or perceptual demands obstruct that experience. Someone who wants route planning but cannot sustain a hold should not have to trade away route choice merely to access the action. Conversely, assistance that automatically picks a target can remove a discrimination task another person values. The recommendation is to identify and test the trade, not to guarantee an assist can preserve every promise simultaneously. [C-06, C-09]

## Characteristic loops and structures

Use this **analytic loop**, not a universal mandatory sequence: acquire relevant state → select a position/target/tool → aim or time execution → inspect the result → reposition, replenish or switch. At encounter scale, track which actions remain feasible after misses and damage. At session scale, identify whether recovery is a respawn, checkpoint, new round or return to a persistent inventory. Long-term unlocks belong to progression/economy dependencies, not an assumption that every shooter needs a grind. [C-01, C-03, C-07]

Three documented contrasts ground the range. Nintendo describes turf coverage scoring and a separate cooperative Salmon Run structure. id Software’s launch guide ties different combat actions to replenishment resources. Bethesda’s historical Quake Champions overview describes map pickups and weapons with different temporal demands. These are **documented design examples**, not evidence that one structure is superior or that aggression is universally rewarding. [C-02]

## Characteristic decisions and evidence-to-application bridges

| Decision | Conditional mechanism and practical choice | Alternative, failure signal and evidence limit |
|---|---|---|
| Hitscan, traveling projectile or mixed arsenal | Separate the simulated collision rule from authoritative confirmation. Travel can make prediction and interception relevant; immediate resolution can emphasize current alignment. Specify what the reticle and tracer actually promise. | A decorative fast tracer must not teach false travel timing. Mixed rules cost explanation and testing. These are rule-level inferences, not a recommended projectile speed. [C-03] |
| Target acquisition versus discrimination | Test whether misses come from finding, identifying, tracking, predicting or physically activating. Change the blocking demand without quietly changing who may be targeted. | Target lock may remove manual selection or select friendlies/irrelevant targets. A less powerful configurable aid or different target presentation may fit better. [C-04, C-06, C-09] |
| Spatial attention | Identify information needed outside the aim point: incoming threat, ally state, objective, route and resources. Preserve essential alternatives without a simultaneous cue quota. | Extra indicators can crowd targets or disclose hidden opponents. Camera changes are an unresolved dependency, not a free fix. [C-06, C-10] |
| Weapon roles | Describe role by target/space/time/resource interaction: sustained pressure, precise interruption, area placement, utility or safe delivery. Compare the actions each enables under the encounter’s constraints. | A nominally distinct weapon can be redundant, or a utility tool can become mandatory busywork. Do not infer useful diversity from a long list of equipment. [C-07] |
| Resource replenishment | Specify where recovery resources come from and which actions spend or expose them. A forward-recovery loop and a conservation loop teach different commitments. | Scarcity can make cautious play coherent; forced aggression can defeat a restorative or stealth promise. F03/F04 review is needed before an economy prescription. [C-02, C-07] |
| Feedback intensity | Preserve facts about request, launch and confirmed result. Tune ornament separately from factual certainty. | Stronger effects cannot fix wrong authority or ambiguous semantics. Offline instantaneous events may need only one outcome cue. [C-03, C-05] |

### Application process

1. **Diagnose the intended task.** Write an encounter-level statement such as “choose a safe firing lane while predicting a moving target,” then identify what must remain a choice under assistance. Record reachable settings and the supported device/display context. [C-06, C-09]
2. **Make a compact role-and-state map.** For each weapon/tool, record target eligibility, collision rule, resource cost, action commitment, confirmation and recovery. Record what the player can legitimately know at each point, including misses whose cause is uncertain. [C-03, C-07]
3. **Choose the smallest intervention.** Prefer correcting misleading state or an inaccessible activation before adding adaptive enemy behavior. Consider omitting ornament, offering configurable targeting, revising a sightline or changing a resource source; these solve different problems. [C-05, C-06, C-09]
4. **Compare the actual encounter, not just a gallery.** Include target selection, movement, clutter and relevant resource pressure. Separate assistance performance from awareness of assistance and from preference. [C-04, C-11]
5. **Keep, narrow or reject.** Retain an intervention only for configurations where it preserves the intended decision and acceptable access. If it removes target discrimination, leaks hidden state or solves accuracy while worsening participation, revise the promise or choose another intervention. [C-09, C-11]

## Pattern selection and adaptations

[Provisional-versus-confirmed impact feedback](../patterns/provisional-versus-confirmed-impact-feedback.md), `GDR-CAND-20261010-G04-PAT-01`, applies when the apparent result can precede known success. It is unnecessary when the outcome is already known and one clear cue suffices. A projectile launcher and a hitscan weapon can both need this distinction; a projectile’s visible travel does not by itself communicate authoritative success. [C-03, C-05]

For modality alternatives, use the inspected P02 information-preservation pattern through the dependency receipt, rather than create a second generic redundant-cue pattern. For a shooter/extraction hybrid, [viable baseline re-entry loadout](../patterns/viable-baseline-re-entry-loadout.md) addresses a different scale: access to a subsequent voluntary attempt. It does not guarantee that the current battle is recoverable. [C-06, C-DEP]

A hybrid conflict must stay visible: precise competitive threat location, a cinematic occluding camera, and reduced visual load can pull in different directions. Decide which information is legitimately available, then test alternate presentations of that same information; do not declare that a camera or genre label wins. [C-10]

## Representative cases, worked example and counterexamples

| Inspected case | Why it belongs in this comparison | What it does not prove |
|---|---|---|
| Splatoon 3, official guide | Alternative scoring and cooperative structure within shooting-centered play. | No causal evidence about audience preference, accessibility or absence of violence. [C-02] |
| DOOM Eternal, 2020 guide | Encounter resources interact with combat actions. | Not a rule that every encounter should force close aggression. [C-02] |
| Quake Champions, 2018 Early Access overview | Arena pickups and differing weapon timing demands. | Not current balance, an ideal role count or evidence that newcomers benefit from those demands. [C-02] |
| Aim-assistance study, CHI 2014 | A controlled warning against transferring a simplified-task benefit unchanged. | Not modern input parity, universal aim-lock superiority or long-term competitive legitimacy. [C-04] |

**Illustrative worked encounter — field repair delivery.** A third-person player must shoot repair capsules into moving drone sockets while staying out of intermittent machinery lanes. One launcher resolves at the aimed socket; another sends a visible capsule that can be intercepted. A resource-free pointer previews eligible sockets without selecting one. The intended decisions are socket choice, firing lane and timing, not endurance of a held button. [C-08]

Apply the process by first checking whether errors come from socket identification or sustained input. A toggle can change the latter while leaving selection manual. For the traveling capsule, show launch separately from confirmed attachment; stop any “repaired” cue when the server rejects attachment. Offer an alternative confirmation that conveys the same socket/result, not the hidden cause of every miss. If both launchers become functionally identical under target lock, either preserve a different consequential role or remove the redundant tool. None of these invented changes has been built or evaluated. [C-03, C-06, C-08, C-09]

**Strong counterexample:** a deliberately abstract local arcade mode may make ammunition infinite, restart immediate and every action’s result unambiguous. Persistent resource management, a re-entry kit and extra pending-state UI would add burden without serving its promise. A bullet-pattern game may place more weight on traversal than fine aiming; assistance research about target acquisition cannot settle its difficulty. [C-01, C-07, C-09]

## Accessibility, ethics, localization and production

Audit speed, simultaneous actions, repeated presses and long holds separately. Remapping alone is not a remedy for every activation demand. Test essential threat and result information with chosen cue routes and effects settings; decorative reduction must not silently remove the only meaningful signal. Do not turn uncertain spatial audio into an exact named-enemy caption. The XAG sources are platform guidance, **not formal standards establishing shooter compliance**. [C-06]

For localization, validate role names, “hit” versus “blocked,” direction/reference frame and remapped prompts in context; a short English label is not proof of timely interpretation in another language. For production, every targeting variant multiplies combinations with movement, occlusion, neutral entities, network correction and presentation settings. Narrow the supported matrix explicitly rather than claim all input devices or cameras are interchangeable. No numerical font, pixel, field-of-view, time-to-kill or input-buffer setting is recommended here. [C-09, C-10]

Competitive changes require considering the people on both sides of an assist, including disclosure and rule consistency. Narrative or campaign settings may permit individual customization without that same opponent constraint. Treat voluntary difficulty and representation choices separately from coercive session incentives. Violence, policing and military depiction warrant contextual review where present; a shooter label supplies no cultural or ethical exemption. [C-09–C-11]

## Research questions and validation — proposed, not performed

**S-A: Does assistance preserve the intended task in context?** Compare baseline and a selected configurable aid in the same rule set, first in a simple target task and then in the intended encounter. Include relevant skill histories and people using the supported input/access routes. Measure target discrimination, misses, objective completion, perceived control and mistaken target choice separately. Counterbalance order and record learning, device, target motion and resource pressure. Reject or narrow the aid when accuracy improves but the defining decision disappears, harm shifts to another population, or the benefit exists only in the simplified task. No sample size or power guarantee is invented. [C-04, C-09, C-11]

**S-B: Is a weapon role genuinely useful?** Compare the encounter with the candidate tool, a simpler tool and omission. Keep objectives and available task information fixed; log viable options at decision points, not just usage share. Interview why a tool was declined. Reject a “distinct role” claim when it is never locally advantageous under understood rules, or when use is coerced by an arbitrary lock rather than its intended affordance. This is a proposed discriminator, not proof that all tools need equal use. [C-07, C-11]

**S-C: Did the player understand a changed constraint?** Present contrasting illustrative scenarios where a shot is valid, invalid and at a boundary. Change the correct answer, not only cosmetic values; retain access supports. Ask prediction before preference. Declining a valid action is not evidence of failed learning. This preserves the reviewed F01 correction without asserting durable learning was measured. [C-11, C-DEP]

## Coverage and next discriminating questions

Researched: family boundaries; varied objective/resource examples; prediction versus confirmation; contextual assistance; input and information access; conditional weapon/resource decisions. Open: contemporary arcade and third-person comparative evidence; long-term assist effects; projectile/hitscan implementation details; robust role/economy models; camera comfort; anti-cheat and competitive access policy. F03/F04 and P03/W03 bytes are not imported. The next decisive evidence is an identified scenario/build plus contextual comparison, not another genre-wide tip list. [C-01–C-11]

## Review and history

Initial capture only; predecessor and supersession are null. Author self-review is recorded in the packet. Independent G04 review has not occurred; Gate C remains open, Gate D has only the local checks explicitly recorded, and Gate E release has not occurred. Temporary IDs, dates and hashes are distribution identities, not approvals. [C-DEP]
## Inspected shared guidance and dependency status

These are parent-selected **0.1.0 draft** dependencies, not released references. Relevant bytes were inspected in the cumulative archive; no earlier batch is resubmitted. This transfers scoped reasoning, not the empirical findings of unopened underlying papers. Full identity/hash receipt and the exact missing-source list are in the [review packet](../reviews/full-run-20261010-g04-review-packet.md#reviewed-dependencies).

| Selected candidate | Revision and precise local locator | Conditional transfer |
|---|---|---|
| `GDR-CAND-20261010-F02-TOP-01` | `initial-capture-1`; archive `selected-drafts/topics/decision-design.md`, lines 53–75; 95–128 | Decision quality versus outcome, legitimate uncertainty, reversibility and opportunity cost. |
| `GDR-CAND-20261010-F02-TOP-02` | `independent-review-correction-1`; archive `selected-drafts/topics/challenge-and-difficulty.md`, lines 55–77; 125–137 | Demand decomposition, recovery as a viable state, affected parties and invariants. |
| `GDR-CAND-20261010-P02-TOP-01` | `review-correction-1`; archive `selected-drafts/topics/controls-and-input.md`, lines 60–105; 109–120 | Action/binding/activation distinctions, physical demand and device parity limits. |
| `GDR-CAND-20261010-P02-TOP-02` | `review-correction-1`; archive `selected-drafts/topics/feedback-and-game-feel.md`, lines 77–89 | Attempt, acceptance, pending and outcome are different facts; no fixed cue quota. |
| `GDR-CAND-20261010-P02-TOP-03` | `review-correction-1`; archive `selected-drafts/topics/multimodal-communication.md`, lines 84–96; 119–130 | Alternative cues preserve known facts, uncertainty and decision timing. |
| `GDR-CAND-20261010-P02-PAT-02` | `review-correction-1`; archive `selected-drafts/patterns/fact-preserving-cue-alternatives.md`, lines 50–107 | Information contracts, configured alternatives, and rejection when timely meaning is lost. |
| `GDR-CAND-20261010-F01-PAT-01` | `independent-review-correction-1`; archive `selected-drafts/patterns/supported-attempt-and-transfer-check.md`, lines 98–120 | Changed-answer transfer cases; separate understanding from preference; retain access support. |
| `GDR-CAND-20261010-P01-TOP-03` | `review-correction-1`; archive `selected-drafts/topics/accessibility-and-inclusive-interaction.md`, lines 60–102; corrections/P01/CORRECTION_RECEIPT.md | CSS-pixel pointer scope, rendered text-body height, scaling and platform context must not be collapsed. |
| `GDR-CAND-20261010-F07-TOP-01` | `initial-capture-1`; archive `selected-drafts/topics/evaluation-and-balancing.md`, lines 67–93; 123–133 | Denominators, qualitative explanation and interacting-player units. |
| `GDR-CAND-20261010-F07-TOP-02` | `initial-capture-1`; archive `selected-drafts/topics/ethical-and-sustainable-design.md`, lines 62–90; 106–128; 156–172 | Voluntary challenge differs from coercion; refusal, stop, return and harm guardrails. |

F03 progression/economy and F04 combat/traversal outputs are **unreviewed running/queued dependencies without inspected bytes here**. No exact candidate ID or path is invented. Current canonical index/pending allocations and the live recovery ledger are missing. Shared ownership links remain proposals. The supplied audio pilot is hypothesis context only, never a requirement for this genre or recipe. [C-DEP]

## Claim ledger

Claim classes describe support, not certainty. `observed-example` refers only to the identified document when no game observation is stated. Confidence applies to the narrowly worded claim.

| Claim | Precise claim | Class | Sources and locators | Confidence and reason | Limits / unresolved question |
|---|---|---|---|---|---|
| C-01 | The working family is defined by consequential directed shooting, not a camera, military theme, PvP mode or violence requirement. | inference | Dispatch §Domain questions; GDR-SRC-20261010-G04-004/GDR-SRC-20261010-G04-014, named sections | Moderate: useful analytic boundary supported by contrasting examples, not a settled scholarly taxonomy. | Membership changes when shooting becomes incidental or automated; audience classification remains contested. |
| C-02 | Different documented scoring and resource structures expose different shooting decisions. | observed-example | GDR-SRC-20261010-G04-004: Turf War/Salmon Run; GDR-SRC-20261010-G04-005: The Unholy Trinity; GDR-SRC-20261010-G04-014: Weapons/Arenas | High for the cited descriptions, not gameplay efficacy. | Historical guides, promotional selection bias; no current build comparison. |
| C-03 | Hitscan/travel simulation and client/server confirmation are separate design dimensions. | inference | GDR-SRC-20261010-G04-002: From Click to Headshot; GDR-SRC-20261010-G04-014: Weapons | Moderate: follows the described timing distinction; applicability depends on implementation. | No universal latency or travel-time threshold; exact authority behavior requires implementation review. |
| C-04 | Aim-assistance results in a simplified task do not establish equivalent benefits in richer combat. | empirical-evidence | GDR-SRC-20261010-G04-003: PDF pp. 5–6 and 8–9 | Moderate: related controlled studies provide a context contrast; small, male-heavy samples and custom implementations limit transfer. | No claim about every modern controller assist, long-term fairness or a universal best technique. |
| C-05 | Investigate confirmed-state correctness separately from how impact is communicated. | practitioner-heuristic | GDR-SRC-20261010-G04-002: Correctness vs Clarity; Case Study 2 | Moderate: firsthand development diagnosis, not an independent efficacy test. | Misleading feedback is one explanation; incorrect simulation remains possible. |
| C-06 | Audit physical activation demand and essential information routes before calling the problem insufficient skill. | inference | GDR-SRC-20261010-P02-001: Background/guidelines; GDR-SRC-20261010-P02-005: Goal/Overview; inspected F02-C/P02-I | Moderate: bridges explicit access guidance to this diagnostic workflow. | Neither vendor guidance nor reduced demand proves equal competitive outcomes. |
| C-07 | Resource and weapon-role changes should be evaluated as changes to viable actions, not damage rankings alone. | hypothesis | GDR-SRC-20261010-G04-005: The Unholy Trinity; GDR-SRC-20261010-G04-014: Weapons/Arenas; inspected F02-D | Low for the proposed workflow benefit; the economic action links are inspectable, satisfaction is not. | F03/F04 missing; no solved optimal weapon portfolio or economy. |
| C-08 | The worked encounter and role matrix are illustrative candidates, not shipped features or test results. | hypothesis | G04 authored examples; C-03/C-06/C-07 reasoning | Low until adapted and tested. | Local prototype decisions require separate authorization. |
| C-09 | Assistance should preserve the intended decision while changing the obstructing demand, subject to affected-player review. | hypothesis | GDR-SRC-20261010-G04-003: Discussion/Limitations; GDR-SRC-20261010-P02-001; inspected F02-C | Low for any specific configuration; evidence motivates contextual evaluation rather than a guarantee. | In competitive play an assistance change can alter others’ game; no unilateral parity claim. |
| C-10 | Camera, representation, language and production constraints can invalidate otherwise plausible adaptations. | inference | Inspected P01-A/P02-I/P02-M; C-03/C-06 | Moderate as a dependency analysis, not a quantified effect. | No camera comfort standard, translation benchmark or universal numerical setting established. |
| C-11 | Proposed tests separate comprehension, action execution, outcomes and voluntary preference; no test has been performed. | hypothesis | Inspected F01-T/F07-E/F07-S; test designs below | Low: discriminating study proposals, not results. | Participant recruitment, sample justification, instrumentation and approval remain future work. |
| C-DEP | Shared guidance was inspected at selected draft revisions; the named unresolved dependencies are not transferred. | observed-example | Local archive inspection receipt in G04 review packet | High for byte identity/inspection scope; parent selection authority comes from the supplied dispatch. | Hash matching proves inventory consistency, not source truth, canonical allocation or release. |
## References

All access dates are 2026-10-10. In relationship notes, `G04-NNN` abbreviates `GDR-SRC-20261010-G04-NNN`; it is not another source identity. Observation route: assistant inspection of the identified public document, not game play, a match recording or participant observation. All excerpts are paraphrased; copyright remains with the rights holders. No source text, media or paper is redistributed. Dates refer to the named document unless explicitly identified as a game release.

### GDR-SRC-20261010-G04-003

Rodrigo Vicencio-Moreira, Regan L. Mandryk, Carl Gutwin, Scott Bateman. **[The Effectiveness (or Lack Thereof) of Aim-Assist Techniques in First-Person Shooter Games](https://rodrigov.ca/wp-content/uploads/2016/03/aim-assist-cameraReadychi2014-v8-final.pdf)**. Date: 2014; CHI conference 2014-04-26 to 2014-05-01. Publisher: ACM CHI 2014; author-hosted camera-ready copy. Edition/build: CHI 2014, proceedings pp. 937–946; DOI 10.1145/2556288.2557308; 10-page camera-ready PDF. Access: `relevant-excerpt`. Type: original empirical research.

**Precise locator:** PDF pp. 5–6, study methods; pp. 8–9, results/discussion/limitations. PDF p. 8 figure and p. 9 visually inspected; Table 1 visual fetch failed.. **Claims supported here:** C-04, C-09. **Limits:** Three short custom-game studies: n=12,16,15; predominantly male, selected skill groups. No pooled independent n or long-term equity conclusion. Qualitative conclusions only; no numerical effect-size extraction. **Independence:** One paper with related studies, not three independent research groups. Author host is a copy, not a replication. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-002

Kevin Lee, game systems software engineer, Riot Games. **[The State of Hit Registration](https://playvalorant.com/en-us/news/dev/the-state-of-hit-registration/)**. Date: 2020-08-06. Publisher: Riot Games. Edition/build: 2020 account, including beta 0.50 context; proposed improvements are not verified current features. Access: `relevant-excerpt`. Type: firsthand development explanation.

**Precise locator:** “Correctness vs Clarity”; “From Click to Headshot”; “Case Study 2: Crouching into Shot VFX”; “Planned Clarity Improvements”. **Claims supported here:** C-03, C-05. **Limits:** Text inspected; embedded recordings not watched. Does not measure benefit of the G04 recipe. **Independence:** Same Riot provenance group as G04-001/015; P02 feedback transfers are not additional experiments. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-004

Nintendo. **[Welcome to Splatsville](https://play.nintendo.com/news-tips/tips-tricks/splatoon-3-tips-and-tricks/)**. Date: unknown. Publisher: Play Nintendo. Edition/build: Splatoon 3, Nintendo Switch described; no build supplied. Access: `relevant-excerpt`. Type: first-party game guide.

**Precise locator:** “Story Mode”; “Salmon Run”; “Turf War”; content-rating footer. **Claims supported here:** C-01, C-02. **Limits:** Official description, not observed play or audience study; cartoon violence remains explicit. **Independence:** One Nintendo account; inaccessible weapons pages are not extra support. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-005

id Software. **[DOOM Eternal – Demon Slaying 101](https://slayersclub.bethesda.net/en-US/news/doom-eternal-demon-slaying-101)**. Date: 2020-03-17. Publisher: Bethesda Slayers Club. Edition/build: Launch-period campaign guide; exact executable not inspected. Access: `relevant-excerpt`. Type: first-party game guide.

**Precise locator:** “The Unholy Trinity”; “Positively Dashing”; “Mods Make the Slayer”. **Claims supported here:** C-02, C-07. **Limits:** Explains mechanics and gives advice; supplies no causal measurement of engagement or optimal aggression. **Independence:** Same publisher ecosystem as G04-014, different game context; not independent efficacy evidence. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-G04-014

Parker Wilhelm, Content Manager. **[Hit the Ground Fragging with Quake Champions in Early Access!](https://bethesda.net/tr-TR/news/hit-the-ground-fragging-with-quake-champions-in-early-access)**. Date: 2018-06-07. Publisher: Bethesda. Edition/build: Early Access overview; Turkish locale wrapper contains English article, date “07 Haziran 2018”. Access: `relevant-excerpt`. Type: first-party product/weapon overview.

**Precise locator:** “Modes”; “Weapons,” especially Super Nailgun, Rocket Launcher, Railgun; “Arenas”. **Claims supported here:** C-01–C-03, C-07. **Limits:** Historical mode and weapon account only. Ignore unsupported origin/“invented the genre” marketing and old prices. **Independence:** Same publisher ecosystem as G04-005, distinct game context; no causal results. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-P02-001

Microsoft. **[Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107)**. Date: updated 2026-03-04. Publisher: Microsoft Learn. Edition/build: Unnumbered web guidance revision; reopened for G04. Access: `relevant-excerpt`. Type: platform accessibility guidance.

**Precise locator:** “Background and foundational information”; remapping and activation-demand guidelines, including speed, complexity, duration. **Claims supported here:** C-06, C-09. **Limits:** No universal timing value, competitive parity guarantee or formal-standard classification. **Independence:** Identity reused from inspected P02 source record; no new G04 allocation for the same source. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.

### GDR-SRC-20261010-P02-005

Microsoft. **[Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103)**. Date: updated 2026-03-04. Publisher: Microsoft Learn. Edition/build: Unnumbered web guidance revision; reopened for G04. Access: `relevant-excerpt`. Type: platform accessibility guidance.

**Precise locator:** “Goal”; “Overview”; “Scoping questions”; multisensory communication options. **Claims supported here:** C-06, C-10. **Limits:** No inference that simultaneous cue multiplication improves all performance; preserves meaning rather than promising equal experience. **Independence:** Identity reused from inspected P02 source record; same Microsoft guidance family as P02-001 and G04-013. **Rights:** copyrighted public document; minimal paraphrase and link only; no republication license inferred.
