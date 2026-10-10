---
id: GDK-PILOT-0001
kind: pilot-specification
title: "Audio tension and ambience"
version: 0.1.0
status: proposed-specification
owner_project: BH-GDR-Presentation-and-Interaction
updated: "2026-10-10"
evidence_checked: null
source_ids: []
---
# Audio tension and ambience pilot

## Decision requested

Approve this bounded research pilot and its output standard before full-library research begins. This is a specification, not a researched topic or validated design pattern. The source graphic has been visually inspected, but its author, provenance and supporting evidence are unresolved. Its image is not redistributed in this package.

## Starting hypothesis

A designer might establish a believable ambient setting, introduce recognizable contextual cues, and then disrupt those expectations with an anomalous cue. Under some conditions this may help create unease or anticipation. This is a candidate practitioner-style heuristic, not a universal three-step requirement, formal standard or established empirical finding.

The pilot must investigate when learned expectations matter, whether this proposed sequence is necessary or merely one option, and whether an effect is tension, surprise, confusion, startle or some combination. Do not use those outcomes interchangeably.

## Scope and questions

- Define ambience, cue, expectation, uncertainty, tension, fear, surprise and startle for this research.
- Examine familiarity, contrast, repetition, timing, spatial interpretation, silence and perceived agency.
- Distinguish diegetic sound, music and interface warnings; investigate their interaction without treating them as equivalent.
- Compare the layered hypothesis with isolated anomalies, silence/absence, sustained uncertainty and overt warning. These are comparison candidates, not asserted effective techniques.
- Investigate habituation and repeated play: can a technique stop working or become a reliable gameplay signal?
- Identify accessibility implications, including hearing differences, captions, alternative modalities, dynamic range and sensory overload.
- Consider player control, safe spaces, predictability, cognitive load and noisy/mobile listening contexts.
- Identify production and implementation implications at a conceptual level. Do not prescribe a middleware, engine integration or unsourced audio setting.

Exclude a complete music theory survey, full psychoacoustics review, audio implementation tutorial and new game design. Expand scope only after review.

## Proposed deliverables

1. One genre-neutral topic: audio tension and ambience, using the topic template.
2. One named pattern candidate: contextual ambience, familiar cue and anomalous cue. Final name and wording should follow the findings rather than copying the graphic's certainty.
3. A second pattern only if evidence supports a meaningfully distinct reusable alternative; otherwise report the negative finding.
4. Two focused genre files, provisionally survival horror and adventure, using their own custom research instructions. Narrow each to the pilot's researched audio implications and explicitly mark broader genre coverage incomplete; do not pretend two full genre monographs were completed.
5. Claim/source ledger, contradiction assessment, proposed index entries and review packet. All Markdown.

These entries receive permanent topic/pattern/genre IDs from coordination at the research-brief gate. Do not reserve duplicate IDs independently.

## Evidence strategy

Seek original relevant perception/expectation research, firsthand game-audio talks or postmortems, accessible developer explanations and directly inspectable game sequences. Use secondary accounts as leads. Look for contrary cases rather than only horror examples that appear to confirm the graphic.

Aim for varied source types and more than one independent production context when available. If the literature is weak, report that finding and narrow the recommendation instead of filling a quota. Identify game build, platform and exact sequence for every observed example. Do not infer that a cue caused reported player responses without supporting evidence.

## Proposed playtest design

Start with a small, consent-based prototype study suitable to the team's actual resources; participant count and analysis should be justified after the question and variability are known. Do not claim statistical power from an arbitrary default.

Compare ambient context plus familiar and anomalous cues with carefully chosen ablations and an alternative technique. Keep the scene, task, threat behavior and relevant audio properties comparable; document any differences that cannot be controlled. Counterbalance order where practical and track repeat exposure. Consider a loudness-controlled comparison to avoid mistaking “louder” for the intended mechanism.

Ask separately about anticipation, unease, surprise, confusion, comfort and perceived threat. Combine self-report with task behavior where appropriate; do not treat physiological arousal as a direct measure of fear. Check whether captions and alternative cues preserve gameplay information and what they change experientially.

Predefine which findings would justify further testing, adaptation or rejection. A result that context adds no benefit, or that omission still creates tension, would challenge the source graphic's necessity claim. A confusing or inaccessible cue can fail the design goal even if it increases arousal. No playtest is performed by this starter.

## Acceptance and stop conditions

The pilot succeeds if it produces useful, evidence-calibrated guidance with complete references, genuine alternatives, counterexamples, failure conditions, accessible testing proposals and reliable retrieval. It can succeed by disproving or sharply narrowing the initial idea.

Stop for Doug's review after the complete pilot packet and retrieval QA. Do not begin the whole taxonomy, change a live game, or treat pilot acceptance as blanket approval for subsequent research batches.
