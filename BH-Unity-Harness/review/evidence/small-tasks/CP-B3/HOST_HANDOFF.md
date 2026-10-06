# CP-B3 local Unity host handoff

Status: BLOCKED_HOST_ACCESS. This cloud session can read/write the repository but has no Unity/Coplay tool connection, no Unity/C# executable found on PATH, and no supplied disposable project roots, target selectors or endpoint. This says nothing about software installed on the user's Windows PC. No live pilot or C# test ran.

To unblock, open the boarshead-ai repository in Codex on the machine with Unity. Supply two disposable project locations that may be used for the pilot, or explicitly authorize creation of two new disposable projects at chosen locations. Existing games must not be used as implicit test targets. A path pasted into the cloud chat alone does not grant this session filesystem or localhost access.

Paste this prompt into that local Codex session:

```text
Continue CP-B3 ONLY for BH-Studio/boarshead-ai on main.
Read BH-Unity-Harness/review/BUILD_CHECKPOINT.md first and the exact files it directs you to, including review/evidence/small-tasks/CP-B3/RESULT.json and HOST_HANDOFF.md. Recheck the remote head and local working tree; preserve unrelated changes and follow applicable AGENTS.md. Do not force Git writes.

First establish actual host access and inspect the available Unity Editor and existing Coplay installation without installing, upgrading or launching anything automatically. Ask me for the two disposable project locations if they have not been supplied. If project creation, package setup or Editor launch is necessary, present the exact missing setup and obtain that specific authorization before doing it. Do not use a live game, assume a Unity version or fetch a moving vendor branch.

Record the actual Editor executable/version, selected project roots, native instance selectors/session IDs, approved local endpoint or native route, loaded package/server source origins and resolved dependencies. Keep credentials out of evidence. Treat the pinned source versions in the integration spec as reviewed references, not proof of installed compatibility. No paid services or purchase.

On an available approved disposable setup, compile the exact BHAssetQuery.cs, observe actual registration/loaded schemas, and execute the bounded CP-B3 pilot defined by the checkpoint and Editor/CONTRACT.md. Capture raw requests/responses, source hashes, all actual outcomes and limitations, including two-target routing, changed session/domain, invalid-folder rejection and query limits. CP-B1 cannot invoke the handler; do not silently widen its allowlist or remove diagnostic-only guards. If there is no usable reviewed route, record that blocker rather than inventing one. Do not treat unknown readiness, disk/index coherence, native-session binding or loaded schema as verified.

Keep optional capabilities and BH acceptance mapping disabled. Do not start CP-C/D/E, alter core/design contracts or repeat prior broad research. Save new evidence without overwriting the existing cloud access-check evidence under BH-Unity-Harness/review/evidence/small-tasks/CP-B3/. Update/read back the checkpoint and actual diff, commit non-force, verify the published result and stop. Distinguish compilation, live tests actually run, unresolved facts and human adoption.
```

The current handler baseline is commit b0c0df5b533733ae8df6d94846c0ce985243565d, blob cf2ad2713732e7ac06c4e0775bce538ff47f3cc1, SHA-256 9536b7ce263169f5e7bbb8a39c8e72cb6d26672c5ab759fc4669fba6cbe5648a. Reconcile the current file identity when resuming. This handoff is not a live setup approval or a claim that local Codex already has a Unity connection.
