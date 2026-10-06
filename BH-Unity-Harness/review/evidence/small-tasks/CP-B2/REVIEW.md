# CP-B2 source review and publication scope

Baseline: main 72d5e4e1d1a184b4bdafc0181f12164155499b31; root tree d0d34ad55d982348bdc541eec41ddb3ab6dc39a7. Checkpoint read first. Current root and complete harness tree had no applicable AGENTS.md for the changed optional/review paths; project-template instructions do not apply to this task. Vendor tree b3ec16283d5ce88e7576fbe2eacf2d2eb9bdf1dc remains unchanged.

Fourteen retrieved source blobs were checked against their Git identities. Sources include the checkpoint, current specification/matrix, CP-B1 result/source record, unchanged discovery implementation, README, provider protocol/runner, installed manifest and four vendor files. Vendor reading was limited to existing state/search behavior and the custom attribute/HandleCommand registration seam; runtime compilation functionality was not adopted. Source identities are in SOURCES.json.

Manual inspection conclusions:

- Handler source has one synchronous, explicit-folder FindAssets call. Folder failure raises unavailable, never supplies a null search scope. Candidate count precedes type/path/object access. No pagination, previews or implicit refresh is requested.
- Up to 25 records are sorted by ordinal GUID; paths and types must be known and in scope. Name uses a bounded main-object load; loading can have project callback effects, requiring a disposable host pilot.
- Observed identity is generated from local Unity/process/domain facts, not copied from expected_identity. Domain changes reject an old expected identity. It is not a native Coplay session, credential or approval. Test/reload/disk/schema facts remain unknown; the handler cannot produce BH provider readiness.
- Folder checks and query share an Editor-thread invocation with before/after checks. This is not a filesystem lock: external path/index races and symlink API behavior require host validation. Reparse checks do not establish disk/index coherence.
- Native envelope bytes and scalar lengths are capped. GUID enumeration precedes count checks and cannot be hard-interrupted. Request raw bytes/depth/duplicate keys and final wrapped response size remain transport responsibilities. Timeout cannot be interpreted as native cancellation.
- Automatic FastMCP registration is disabled, but the attribute may remain discoverable to native routing once someone manually installs this source. Installation/routing is not performed or claimed here.

Actual validation: `python coplay-cpb2/validate_cpb2.txt coplay-cpb2`, exit 0, raw stdout/stderr in RAW.log, 13 lexical source-policy checks. These inspect source shape and policy guard presence; they do not execute C#, prove branch behavior, validate Unity APIs or replace the host negatives. No compiler or Unity executable was found on PATH. C#/Unity/Windows/Coplay tests NOT_RUN; zero executable tests claimed. CP-B1 Python code was not edited and its suite was not repeated. Earlier full candidate coverage is historical and must be reconciled at final assurance.

Publication set: two new optional Editor source/contract files; optional README, integration specification, action matrix and checkpoint updates; these five CP-B2 evidence files. No core, installed manifest, design producer, vendor source, package dependency or game file changes. Exact uploaded artifacts and actual commit diff must be read back before completion. CP-B3 alone is next; no host pilot or CP-C work occurred in this task.
