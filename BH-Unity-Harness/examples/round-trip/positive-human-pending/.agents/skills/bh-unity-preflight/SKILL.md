---
name: bh-unity-preflight
description: Inspect a Unity project before intake or on resume. Do not implement, repair, or accept results.
---

# bh-unity-preflight

Read AGENTS, the three .bh configuration files, and current checkpoint when present. Run `python Tools/BH/bh.py --root . preflight`; for an active task also run `resume` (this writes state/checkpoint). Discover actual Unity version, packages/lockfile, pipeline, targets, instruction files, active skills, diagnostics bridge and Editor ownership. Preserve the existing VS Code/SonarQube configuration. Discover available tool names instead of assuming a namespace.

Inputs: project root and installed candidate. Outputs: observed capabilities, instruction conflicts, dirty-worktree baseline, blocked configuration, and exact next action. Preflight does not install tools or edit project settings. Inspect global/ancestor instructions and ignored instruction files manually; the bounded repository scan cannot see all host policy. Missing required tooling blocks its check. Synthetic fixtures never establish real integration compatibility.

Example: an open Editor and batch-only configuration require choosing a supported existing-Editor route or explicitly closing the Editor yourself; never launch a second Editor to make the check pass.
