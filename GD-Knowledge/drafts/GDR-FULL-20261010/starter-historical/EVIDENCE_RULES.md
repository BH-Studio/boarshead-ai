# Evidence and attribution rules

## Claim classes

Every material claim must use one of these labels in its claim ledger. Mixed paragraphs should be split when their support differs.

- `formal-standard`: an identified normative document, issuing body, edition, clause and applicability. Distinguish MUST requirements from recommendations. A studio preference or widely repeated tip is not a formal standard.
- `empirical-evidence`: a study or observed dataset. Record methods, participants or units, setting, effect and uncertainty where available, and limits on generalization.
- `practitioner-heuristic`: advice or experience from a practitioner. Record role, actual production context and whether the account supplies supporting measurements.
- `observed-example`: directly verified behavior in a game, build, recording or artifact. Identify platform/version, scene and timestamp or reproduction steps. Observation does not establish developer intent or causal effectiveness.
- `inference`: a reasoned interpretation derived from identified evidence. Make the bridge and alternatives explicit.
- `studio-decision`: an approved local choice with decision owner, date and scope. A decision is not scientific evidence.
- `hypothesis`: a testable proposal with insufficient direct support. Do not promote it by repetition.

Claim class and confidence are different. A formal standard may be irrelevant to the platform; a well-documented observation may be high confidence but narrow. Use `high`, `moderate` or `low` confidence with a written reason, not a fabricated numerical score.

## Source selection

Prefer sources close to the claim: normative publishers for requirements, original papers for study results, creators for reported intent, current engine/platform documentation for technical behavior, and reproducible observation for what a game does. Evaluate expertise, methods, independence, incentives, specificity, date and applicability. Prestige and popularity alone are insufficient.

Triangulate consequential generalizations with independent evidence when possible. Two articles quoting one talk are one underlying account. There is no magic source count that proves a claim. If one source is the best available evidence, say so and narrow the conclusion. Search explicitly for failures, replications and contrary examples.

Do not invent titles, authors, quotations, DOIs, page numbers, dates, game features, sales figures or study findings. A source you cannot retrieve can remain a lead with `access: lead-only`; it cannot support details you did not read. An AI answer is not a substitute for the cited original.

## Source record

Give each source a permanent `SRC-0001`-style ID allocated through coordination. In each research entry's References section include: ID; author or organization; title; publication/update date or `unknown`; publisher; verified URL or DOI; edition/build; access date; exact chapter/page/section/timestamp used; access status (`full`, `relevant-excerpt`, `abstract-only`, `lead-only`); source type; rights/license note; claims supported; limitations and independence relationships.

Use a nearby claim marker such as `[C-01; SRC-0001]` and an ordinary clickable reference in the References section. Claim IDs are scoped to the entry. Source IDs are global. Reuse source IDs across entries. Coordination records any renamed or consolidated source IDs in the register.

For game observations include observer, observation date, platform/build and evidence route. Synthetic examples must be labeled `illustrative`, never presented as shipped-game observations or test results.

## Copyright and privacy

Paraphrase faithfully and attribute. Quote only the small amount necessary, with exact wording and a locator; avoid reproducing substantial parts of books, talks, courses, screenshots or paywalled material. Do not add the supplied screenshot to a public package without permission and a rights check. The starter records only a paraphrased research lead; attribution is unresolved.

Do not publish private studio material, personal information or proprietary project evidence merely because it informed research. Obtain approval and sanitize where needed. Source URLs containing private tokens or credentials must never be saved.

## Contradictions and freshness

Record conflicting claims in [the register](REGISTERS.md). Compare definitions, populations, player goals, hardware, genre and measurement methods before treating a disagreement as a direct contradiction. Preserve genuine unresolved conflict and state what evidence would resolve it.

Technical and platform claims carry a checked date and version. Review them when the dependency changes or before implementation. Research findings do not expire on an arbitrary schedule, but new evidence can supersede them. Keep superseded records and redirects so historical citations remain interpretable.
