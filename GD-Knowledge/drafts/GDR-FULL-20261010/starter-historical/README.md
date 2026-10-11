# GD Knowledge starter architecture

Version 0.1.0 candidate • 10 October 2026 • Boar's Head Studio

This package proposes a reusable game-design research library and five BH-GDR research workspaces. The immediate decision is whether to approve the taxonomy and audio pilot specification. It is a research system starter, not a completed reference library. No topic, pattern or genre has passed research review in this release.

## Start here

1. Review the [taxonomy](TAXONOMY.md) and [audio pilot](pilots/audio-tension-and-ambience.md).
2. Approve or revise their scope before full research begins.
3. Configure the five Projects using the exact instructions in [Project setup](projects/README.md).
4. Run the pilot, review evidence and retrieval, and approve its quality before commissioning topic batches.

## Library structure

- [Shared research instructions](RESEARCH_INSTRUCTIONS.md): research method and output contract.
- [Evidence rules](EVIDENCE_RULES.md): source quality, claim classification and attribution.
- [Library index](INDEX.md): authoritative IDs, entry states and lookup rules.
- [Retrieval and distribution](RETRIEVAL_AND_DISTRIBUTION.md): small domain packs and harness handoff.
- [Review gates](REVIEW_GATES.md): what must be checked before an entry is released.
- [Decision and contradiction register](REGISTERS.md): unresolved decisions and conflicting evidence.
- [Topic template](templates/topic.md), [pattern template](templates/pattern.md), [genre template](templates/genre.md).
- [Topics](topics/README.md): genre-neutral explanations and design questions.
- [Patterns](patterns/README.md): named, reusable techniques with conditions and tests.
- [Genres](genres/README.md): one file per genre with custom research guidance and application notes.
- [Compatibility review](COMPATIBILITY.md): existing repository conventions inspected read-only.
- [Release manifest](MANIFEST.md): scope, file inventory and verification.

The canonical destination is `BH-Studio/boarshead-ai/GD-Knowledge`. GitHub becomes the source of truth after reviewed publication. Project attachments are versioned working snapshots, not automatically synchronized replicas. This starter does not install or alter the Unity harness or existing GPT instructions.

## Boundaries

The library serves different games, audiences, platforms and teams. No single game's canon, budget or design assumptions become defaults. Specific examples must identify their context and limits. Genre notes adapt shared knowledge rather than silently rewriting it. Human approval of a research entry does not approve its adoption in a game.

All package content is Markdown. YAML front matter lives inside Markdown files; it does not require separate YAML files. The ZIP is a transport envelope only. Third-party references retain their own rights; a repository license does not relicense quoted source material.
