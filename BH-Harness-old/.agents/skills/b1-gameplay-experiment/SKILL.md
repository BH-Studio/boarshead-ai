---
name: b1-gameplay-experiment
description: "Implement or review an authorized Breach One A/B gameplay experiment with controlled variants, resettable state and falsifiable measures. Does not select production camera, drone, revive or bot policy."
---

# b1-gameplay-experiment

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Entry

Require an approved experiment milestone or explicit bounded human exception. Read the exact
experiment plan and the package's locked control conditions. Visible preference or "try this"
context alone is not a finalized experimental contract. Read the baseline index for unresolved
camera, drone, downed/revive and bot direction; do not convert those notes into defaults.

## Design-to-measurement trace

Record experience target → expected repeated behavior → mechanic/configuration change →
observable measure. Define the comparison, importance, falsification criterion and proposed or
approved success threshold. Metrics and expert inference do not prove fun. Keep automated
correctness, architectural measures and player reactions separate.

## Implementation

Use the same sandbox/content and controlled baseline except for deliberately varied factors.
Record build/config IDs, variant labels, input device, camera settings, enemy/weapon settings,
progression state, randomization/seed policy when needed, order/practice effects and resets.
Confounded factors must be disclosed. No global deterministic-simulation framework is implied.

Provide explicit variant selection, repeatable entry/reset, safe disable/remove path, and
instrumentation authorized by the package. Prevent prototype flags, sample values and debug
telemetry from silently entering production or persistent saves. Do not choose a winner automatically.

## Relevant adversarial cases, not preselected mechanics

For camera/input work: movement versus attack independence; view-switch continuity; camera versus
muzzle obstruction; near-wall/cover behavior; off-screen threats; UI focus/device switching;
motion/accessibility settings. For drone work: view exit/control restoration and loss/destruction.
For downed/revive: concurrent damage/expiry/revive ordering, cancellation and retry. For bot
variants: unavailable rescuer, AI control ownership and enabled/disabled transitions. Run only
cases supported by the approved feature scope; do not invent missing rules while testing them.

## Output

Return exact variant/config identity, reset steps, observed metrics and protocol, confounds,
failed hypotheses and NOT RUN player checks. Include a human-readable comparison with confidence
and limits. Archive or retain the experiment only under the agreed disposition; successful
prototype execution is not approval to ship its mechanic.
