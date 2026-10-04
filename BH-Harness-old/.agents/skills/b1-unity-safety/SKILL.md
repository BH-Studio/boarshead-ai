---
name: b1-unity-safety
description: "Review or modify Unity assets, serialization, lifecycle, assemblies and scene/editor setup within approved Breach One scope. Not a package-import or engine-upgrade authorization."
---

# b1-unity-safety

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Inputs

Read `docs/AI/UNITY_AND_MIDDLEWARE_POLICY.md`, the package, actual Unity/package versions,
affected asmdefs, assets and existing authoring conventions. For pure document edits, this skill
usually does not apply. For serialization or middleware changes, also load the corresponding skill.

## Procedure

1. Map runtime/editor/test assembly boundaries and all affected scene/prefab/definition references.
   Check platform conditionals and build inclusion. Keep editor-only dependencies out of runtime.
2. Preserve existing `.meta` files and GUID relationships. Inventory source and metadata changes
   together. New assets need an authorized import/generation path; never fabricate successful
   import or discard missing references to make compilation appear clean.
3. Treat serialized field/type/namespace/assembly moves as compatibility work. Use actual
   migration facilities supported by the installed versions, and test representative old assets.
4. Separate immutable/shared definitions from instance/session state. Check play/stop, reload,
   retry, scene unload, disable/re-enable, pooling reuse and event-unsubscription behavior where
   touched. Restore test mutations and account for domain-reload settings.
5. Complete authoring setup: owning prefab, inspector bindings, layer/collision configuration,
   input and animation references, scene entry/reset, invalid-data feedback and reproducible
   build/setup steps. Do not leave required wiring as an undocumented instruction to the human.
6. Avoid unrelated scene/settings reserialization, broad formatting, new packages, duplicate
   animation/motor owners or speculative editor tools. Record authorized non-code changes.
7. Run the approved static, import, PlayMode, content and built-player checks. Editor-only
   execution cannot certify player builds or perceived usability.

## Output

Return affected assets/metadata/assemblies, serialization impact, setup/rebuild instructions,
actual checks, remaining manual validation and unexpected diff. If Unity access is unavailable,
return exact setup/validation steps and NOT RUN status; do not claim reference integrity was
verified in the Editor. See the authoring/setup template for complex scenes or builders.
