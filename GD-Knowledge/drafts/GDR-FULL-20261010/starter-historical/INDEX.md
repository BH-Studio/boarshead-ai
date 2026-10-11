# Library index and identity rules

Release: 0.1.0 candidate. Research entries released: zero.

## Available now

- [Audio tension and ambience pilot specification](pilots/audio-tension-and-ambience.md), `GDK-PILOT-0001`, proposed specification only.
- [Topic template](templates/topic.md), [pattern template](templates/pattern.md), [genre template](templates/genre.md).
- [Proposed coverage map](TAXONOMY.md).

No empty backlog candidate should appear as if it were a finished reference. The folder README files explain future placement; they are not topic knowledge.

## Stable identity

Coordination allocates permanent IDs: `GDK-TOP-0001`, `GDK-PAT-0001`, `GDK-GEN-0001`; source IDs use `SRC-0001`. Numbers carry no semantic meaning. Never reuse a retired ID. Filenames are lowercase descriptive slugs, while IDs survive file renames. Templates use `UNASSIGNED` and cannot be mistaken for published entries.

Before allocating an ID, check the latest canonical index and pending allocations. Concurrent writers request an allocation through coordination. Keep one canonical home per concept. When merging, preserve old IDs as redirects in this index; when splitting, record successors and applicability.

## Entry rows to add after research

Each row records: stable ID; linked title; kind; domain owner; aliases; short description; problem/use-case tags; linked topic/genre/pattern IDs; lifecycle status; version; last evidence check; confidence summary; important applicability limits; replacement ID if any.

Lifecycle: `draft` → `in-review` → `released`; use `superseded` or `withdrawn` when needed. `proposed-specification` and `template` are separate non-research states. Released means reviewed for use as reference, not universally true or adopted in a game.

Front matter and this index must agree. Coordination checks duplicate IDs, missing files, broken relationships, unresolved placeholders and status mismatches before release. Keep a concise alphabetical alias list as coverage grows so searches for everyday terms can find the canonical concept.

## Lookup procedure

Start with the design question and constraints. Find a topic through title, aliases or problem tags. Open its applicable genre note and only the patterns relevant to the decision. Inspect limits, contradictions and sources, not just the recommendation. The [retrieval contract](RETRIEVAL_AND_DISTRIBUTION.md) defines the response and handoff requirements.
