# Optional Unity batch build producer — candidate, NOT_RUN in Unity

The common runtime parses real BuildReport observations but cannot manufacture a project-specific build method. This separately reviewed C# producer supplies a narrow Windows64 route. It is NOT automatically installed and has not been compiled here. In an explicitly approved local pilot, add BHBuild.cs to an Editor-only folder/assembly; let Unity create its .meta and preserve that identity. Keep this helper out of runtime assemblies. The game must already use StandaloneWindows64, have enabled scenes, have build hooks reviewed, and have no competing Editor. No packages, symbols, build profiles or targets are changed by the helper.

After verifying the exact Unity patch and compiler, pin the Editor executable and this source file in the binding. Use adapter `build`, target `StandaloneWindows64`, result `build.json`, and expectations `errors equals 0` and `total_bytes at_least 1`, mapped to the approved build AC. Arguments are an array, not a shell string:

```json
["-batchmode", "-projectPath", "{project}", "-executeMethod", "BoarsHead.Harness.BHBuild.Run", "-logFile", "{log}", "-bhResult", "{result}", "-bhProject", "{project_id}", "-bhTask", "{task_id}", "-bhRun", "{run_id}", "-bhTarget", "StandaloneWindows64"]
```

The helper explicitly exits after writing the result; do not assume a failure before the method ran produced a usable report. A missing result remains ERROR/NOT_RUN. Compilation is not proven by the existence of this C# file. Run actual EditMode/PlayMode tests separately using the project's supported test-framework version. Built-player behavior and performance still require their own gates. Build callbacks execute project code and may mutate inputs; the wrapper detects hashed input changes and refuses clean audit claims.

For release checks, `Tools/BH/check_release_profile.py` reads an approved JSON policy with `version: 1.0.0`, `review_ref`, and a nonempty `forbidden_filename_patterns` array, then scans actual output filenames. Bind it as `facts` and require `forbidden_matches equals 0`; pin both script and policy. Example arguments: `--build-dir <actual prior build output> --policy <pinned policy> --result {result} --project {project_id} --task {task_id} --run {run_id}`. Declared paths and relevant build dependencies must be reviewed. This only detects declared filename patterns; inspect assembly inclusion, scripting defines, bundled content, remote capabilities and runtime behavior separately. Unknown integration identity means a missing release gate, not automatic approval.

Primary documentation inspected 2026-10-04: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html ; https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/reference-command-line.html . These documented API families do not prove compatibility with an uninspected installed Unity patch.
