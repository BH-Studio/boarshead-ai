# Repository compatibility review

Read-only inspection on 10 October 2026. No existing harness, director or GPT configuration was changed while preparing this package. This is architectural alignment, not a verified software integration.

## Inspected references

- [Repository README](https://github.com/BH-Studio/boarshead-ai/blob/main/README.md), Git blob `342e3a07559fecd2fca2d39c97810f56fa5ffb68`: human judgment, defined responsibilities, reviewed outputs and repository artifacts.
- [Game Systems Director entry point](https://github.com/BH-Studio/boarshead-ai/blob/main/BH-Game-Design-Director/00_READ_ME_FIRST.md), blob `b01aaef4ed58c9a8bd29fb5ca350db5411301303`: targeted evidence, contextual specialist lenses, red-team review and explicit design/milestone gates.
- [Narrative and systems integration](https://github.com/BH-Studio/boarshead-ai/blob/main/BH-Narrative-and-Worldbuilding-Director/05_MIGRATION_AND_SYSTEMS_INTEGRATION.md), blob `4b4aa1ff9dd4b10d661ce5f34bacb1492a2c5aaf`: approved canon remains separate from provisional ideas; narrative interfaces describe player-facing needs rather than prescribing runtime architecture.
- [Unity harness quickstart](https://github.com/BH-Studio/boarshead-ai/blob/main/BH-Unity-Harness/QUICKSTART.md), blob `3f3a85af8caa266b9e27fc9357ac64e3f9b80667`: game-agnostic candidate, separate host/game pilots and no implicit permission to install or replace a live workflow.
- [Harness delivery and continuation](https://github.com/BH-Studio/boarshead-ai/blob/main/BH-Unity-Harness/DELIVERY_AND_CONTINUATION.md), blob `e303576fd581e3d1b4ab93c21af439573c62a8b5`: selective distribution and current manifests rather than copying an entire repository.

The URLs above follow main and may change; the recorded blob hashes identify the inspected content. This review did not inspect every source file, execute harness commands, test host behavior or certify contract compatibility.

## Alignment decisions proposed

1. Put general research in GD-Knowledge, separate from a specific game's approved state.
2. Provide evidence and options to existing directors without bypassing their human gates.
3. Preserve research, creative judgment and implementation as distinct activities.
4. Use narrow, versioned reference selections and explicit provenance.
5. Treat specialist roles as perspectives unless actual independent execution is demonstrated.
6. Use ordinary Projects and portable Markdown rather than making new personal GPT creation a dependency.

## Integration boundary

A future harness change should first inspect its current exact interface and review state. This package supplies only an advisory retrieval contract. It neither implements an adapter nor changes contract versions, installers, runtime files, source manifests or approvals.

## Incidental repository finding

The inspected root README links use spaced directory names while the current directory listing uses hyphenated names. The links in this package use the verified current names. Root README repair is outside this starter and has not been performed.
