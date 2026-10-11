# P04 OriginB technical and creator-source spot-check

Checked 2026-10-11 via public-web text retrieval. Scope: later/animation-and-performance.md technical/creator claims and later/art-direction.md corresponding technical/recent-creator references. No engine execution, browser interaction, footage inspection, repository operation, or external write. No substantive contradiction found in the inspected claims.

## Edition check

The live Epic page titles retrieved today explicitly identify **Unreal Engine 5.8 Documentation** for Root Motion, Networked Movement, Motion Matching, and Physically Based Materials. The manuscript’s edition labels are supported as displayed documentation editions; this does not establish a runtime-tested build or freeze these unversioned live URLs.

## Confirmed sources and locators

- **P04-007, Animation C-06:** https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine — Overview, Root Motion, Results; retrieved lines 6, 16, 38–43, 78–81. Distinction between movement-driven presentation and enabled animation-root displacement is supported. The latter still operates with movement/physics handling; the manuscript does not claim otherwise.
- **P04-008, Animation C-07:** https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine — Replicating Special Case Movement with Root Motion / From AnimMontages; retrieved lines 194–203. In particular, line 202 says gameplay logic must trigger montages correctly across machines, and line 203 identifies the Gameplay Ability System route. The manuscript’s scoped coordination-responsibility statement is supported.
- **P04-009, Animation C-08:** https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-matching-in-unreal-engine — introductory query/schema/database description, lines 2–9; Anim Notify Filtering, lines 310–325; Pose Search Schema Channel Weights, lines 326–337. Adjacent selections can duplicate notifies, and changing weights alone can fail to address data/movement mismatch. Supported. Filtering’s exception for Notify States is outside the manuscript’s current claim and need not be added unless it becomes implementation guidance.
- **P04-003, Art C-05:** https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine — What Does Physically Based Mean?, lines 9–12; PBR Material Attributes, lines 15–24. Explicit non-photorealistic applicability and separate base-color/roughness/metallic/specular controls support the attribution. Interaction-permission discussion is correctly presented as the manuscript’s inference.
- **P04-006, Animation C-05:** https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html — retrieved HTML lines 53–54 identify Unity 6.3 LTS (6000.3); Transition properties, lines 182–213; Transition interruption, lines 218–291. Seconds versus normalized source-state duration and interruption controls are supported. Their separation from gameplay consequence reversal is an inference, appropriately bounded in the manuscript.
- **P04-010, Animation C-09:** https://www.naughtydog.com/blog/uncharted_4_a_thiefs_end_the_5_year_anniversary_retrospective — May 10, 2021 by Dinah Bakeer, lines 4–7; UNCHARTED TERRITORY, Hayden at line 25 and Soria at lines 29–31. New facial-capture rig/system and NPC traversal coordination with scripting/AI are supported.
- **P04-011, Animation C-16 / Art C-15:** https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games — May 28, 2026, line 4; Johnston’s stylization/surface answer, lines 57–61; Laygo’s animation answer, lines 63–67. The manuscript accurately limits stylized marks/lifelike skin, exaggerated hand-keyed animation, and a shared expandable base set to creator-reported choices. No measured responsiveness or production savings is supplied by these passages.
- **P04-012, Art C-15:** https://blog.playstation.com/?p=407986 — July 24, 2025, line 45; David Jaumandreu byline, line 56; Campos, lines 63–67; Lozano, lines 68–71. Low-resolution palette/detail constraints, background/level separation, silhouette intent, and contrasting protagonists are supported. Proposed July 31 launch at lines 57 and 74 supports its pre-release context, without asserting current release status.

## Optional precision edit

In Animation line 263 (C-16 limit), Animation line 343 (P04-011 reference), and Art line 289 (P04-011 reference), **“pre-open-beta”** is more exact than **“pre-beta.”** The interview’s closing answer (line 105) specifically places its upcoming open beta on May 30. This is a low-severity metadata refinement, not a contradiction of the substantive animation/style claims. The cited article alone does not establish whether any earlier closed beta occurred.

## Review boundary

This supports the cited technical and production attributions only. It does not validate the manuscript’s design proposals empirically, check the two research papers, re-review inherited XAG/Valve/Riot claims, or establish any gate approval.
