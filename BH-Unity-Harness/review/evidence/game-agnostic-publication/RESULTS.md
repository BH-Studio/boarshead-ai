# Final offline suite — observed outcomes

Functional commit: 72bf50263b39f9ccd236fb54ecae341c97f80125.
148 tests; zero failures/errors/skips; six partitions; 33.271 seconds combined.

The following is the exact concatenation of the six final raw logs, with partition separators only. Original JSON/log bytes and earlier red/green runs are in RAW_EVIDENCE.tar.gz. No live-host tests are claimed.

## Partition 0

```text
test_active_policy_and_knowledge_have_no_source_game_names (test_game_agnostic.GameAgnosticTests.test_active_policy_and_knowledge_have_no_source_game_names) ... ok
test_malformed_skill_registry_fails_explicitly (test_game_agnostic.GameAgnosticTests.test_malformed_skill_registry_fails_explicitly) ... ok
test_shipped_profiles_block_execution_until_reconciled (test_game_agnostic.GameAgnosticTests.test_shipped_profiles_block_execution_until_reconciled) ... ok
test_destination_requires_marker (test_installer.InstallerTests.test_destination_requires_marker) ... ok
test_preview_no_writes (test_installer.InstallerTests.test_preview_no_writes) ... ok
test_rollback_refuses_managed_edit (test_installer.InstallerTests.test_rollback_refuses_managed_edit) ... ok
test_failed_is_fail_not_error (test_package.BuildParserTests.test_failed_is_fail_not_error) ... ok
test_wrong_target (test_package.BuildParserTests.test_wrong_target) ... ok
test_canonical_copies (test_package.PackageTests.test_canonical_copies) ... ok
test_release_empty_blocks (test_package.PackageTests.test_release_empty_blocks) ... ok
test_open_game_decisions_not_promoted (test_review_amendments.ReviewAmendmentTests.test_open_game_decisions_not_promoted) ... ok
test_compile_error (test_runtime.ProcessTests.test_compile_error) ... ok
test_nonzero_exit (test_runtime.ProcessTests.test_nonzero_exit) ... ok
test_wrong_test_name (test_runtime.ProcessTests.test_wrong_test_name) ... ok
test_begin_without_plan (test_runtime.RuntimeTests.test_begin_without_plan) ... ok
test_dropped_acceptance (test_runtime.RuntimeTests.test_dropped_acceptance) ... ok
test_duplicate_skills_block (test_runtime.RuntimeTests.test_duplicate_skills_block) ... ok
test_lock_serializes_writers (test_runtime.RuntimeTests.test_lock_serializes_writers) ... ok
test_missing_human_acceptance (test_runtime.RuntimeTests.test_missing_human_acceptance) ... ok
test_new_commit_invalidates (test_runtime.RuntimeTests.test_new_commit_invalidates) ... ok
test_out_of_scope_mutation_blocks (test_runtime.RuntimeTests.test_out_of_scope_mutation_blocks) ... ok
test_real_cli_preflight (test_runtime.RuntimeTests.test_real_cli_preflight) ... ok
test_root_count_mismatch (test_runtime.RuntimeTests.test_root_count_mismatch) ... ok
test_synthetic_boundary (test_runtime.RuntimeTests.test_synthetic_boundary) ... ok
test_wrong_design_method (test_runtime.RuntimeTests.test_wrong_design_method) ... ok

----------------------------------------------------------------------
Ran 25 tests in 5.641s

OK
```

## Partition 1

```text
test_arbitrary_unreviewed_skill_blocks_without_a_game_prefix (test_game_agnostic.GameAgnosticTests.test_arbitrary_unreviewed_skill_blocks_without_a_game_prefix) ... ok
test_missing_nonpreserved_knowledge_cannot_pass_package_check (test_game_agnostic.GameAgnosticTests.test_missing_nonpreserved_knowledge_cannot_pass_package_check) ... ok
test_test_receipts_include_markdown_inputs_not_generated_evidence (test_game_agnostic.GameAgnosticTests.test_test_receipts_include_markdown_inputs_not_generated_evidence) ... ok
test_explicit_manual_merge (test_installer.InstallerTests.test_explicit_manual_merge) ... ok
test_repeat_unchanged (test_installer.InstallerTests.test_repeat_unchanged) ... ok
test_seed_local_edits_preserved (test_installer.InstallerTests.test_seed_local_edits_preserved) ... ok
test_missing_result_is_malformed (test_package.BuildParserTests.test_missing_result_is_malformed) ... ok
test_assembler_accepts_crlf_checkout_of_preserved_blob (test_package.PackageTests.test_assembler_accepts_crlf_checkout_of_preserved_blob) ... ok
test_distribution_nonempty (test_package.PackageTests.test_distribution_nonempty) ... ok
test_release_empty_policy_blocks (test_package.PackageTests.test_release_empty_policy_blocks) ... ok
test_overlay_matches_real_schema (test_review_amendments.ReviewAmendmentTests.test_overlay_matches_real_schema) ... ok
test_diagnostics_clean (test_runtime.ProcessTests.test_diagnostics_clean) ... ok
test_reviewed_narrow_dependencies (test_runtime.ProcessTests.test_reviewed_narrow_dependencies) ... ok
test_xml_entities (test_runtime.ProcessTests.test_xml_entities) ... ok
test_blocking_question (test_runtime.RuntimeTests.test_blocking_question) ... ok
test_dropped_check (test_runtime.RuntimeTests.test_dropped_check) ... ok
test_failed_then_pass_preserves_history (test_runtime.RuntimeTests.test_failed_then_pass_preserves_history) ... ok
test_manifest_mismatch (test_runtime.RuntimeTests.test_manifest_mismatch) ... ok
test_missing_raw_artifact (test_runtime.RuntimeTests.test_missing_raw_artifact) ... ok
test_no_self_certification (test_runtime.RuntimeTests.test_no_self_certification) ... ok
test_override_instruction_conflict (test_runtime.RuntimeTests.test_override_instruction_conflict) ... ok
test_recovery_budget (test_runtime.RuntimeTests.test_recovery_budget) ... ok
test_roundtrip_human_pending (test_runtime.RuntimeTests.test_roundtrip_human_pending) ... ok
test_unbound_required_check_blocks_plan (test_runtime.RuntimeTests.test_unbound_required_check_blocks_plan) ... ok
test_wrong_harness_version (test_runtime.RuntimeTests.test_wrong_harness_version) ... ok

----------------------------------------------------------------------
Ran 25 tests in 6.865s

OK
```

## Partition 2

```text
test_assembler_accepts_only_declared_review_reference_path (test_game_agnostic.GameAgnosticTests.test_assembler_accepts_only_declared_review_reference_path) ... ok
test_profiles_are_distinct_synthetic_contracts (test_game_agnostic.GameAgnosticTests.test_profiles_are_distinct_synthetic_contracts) ... ok
test_unregistered_skill_cannot_hide_behind_studio_prefix (test_game_agnostic.GameAgnosticTests.test_unregistered_skill_cannot_hide_behind_studio_prefix) ... ok
test_fresh_install_actual_manifest (test_installer.InstallerTests.test_fresh_install_actual_manifest) ... ok
test_rollback_active_record_blocks (test_installer.InstallerTests.test_rollback_active_record_blocks) ... ok
test_stale_preview (test_installer.InstallerTests.test_stale_preview) ... ok
test_no_outputs (test_package.BuildParserTests.test_no_outputs) ... ok
test_assembler_real_git_blob (test_package.PackageTests.test_assembler_real_git_blob) ... ok
test_missing_preserved_blocks_full_validation (test_package.PackageTests.test_missing_preserved_blocks_full_validation) ... ok
test_release_no_match_narrow_only (test_package.PackageTests.test_release_no_match_narrow_only) ... ok
test_prior_k12_preserved_exactly (test_review_amendments.ReviewAmendmentTests.test_prior_k12_preserved_exactly) ... ok
test_diagnostics_new (test_runtime.ProcessTests.test_diagnostics_new) ... ok
test_skipped_required (test_runtime.ProcessTests.test_skipped_required) ... ok
test_zero_tests (test_runtime.ProcessTests.test_zero_tests) ... ok
test_case_collision (test_runtime.RuntimeTests.test_case_collision) ... ok
test_dropped_invariant (test_runtime.RuntimeTests.test_dropped_invariant) ... ok
test_human_automation_rejected (test_runtime.RuntimeTests.test_human_automation_rejected) ... ok
test_manual_not_automated (test_runtime.RuntimeTests.test_manual_not_automated) ... ok
test_missing_receipt (test_runtime.RuntimeTests.test_missing_receipt) ... ok
test_nonfinite_json (test_runtime.RuntimeTests.test_nonfinite_json) ... ok
test_path_traversal (test_runtime.RuntimeTests.test_path_traversal) ... ok
test_repeated_init_unchanged (test_runtime.RuntimeTests.test_repeated_init_unchanged) ... ok
test_stale_dirty_evidence (test_runtime.RuntimeTests.test_stale_dirty_evidence) ... ok
test_unknown_configuration_field (test_runtime.RuntimeTests.test_unknown_configuration_field) ... ok
test_wrong_project_receipt (test_runtime.RuntimeTests.test_wrong_project_receipt) ... ok

----------------------------------------------------------------------
Ran 25 tests in 5.587s

OK
```

## Partition 3

```text
test_explicitly_reviewed_extra_skill_is_preserved (test_game_agnostic.GameAgnosticTests.test_explicitly_reviewed_extra_skill_is_preserved) ... ok
test_real_seed_does_not_select_game_configuration (test_game_agnostic.GameAgnosticTests.test_real_seed_does_not_select_game_configuration) ... ok
test_active_task_blocks (test_installer.InstallerTests.test_active_task_blocks) ... ok
test_lock_blocks (test_installer.InstallerTests.test_lock_blocks) ... ok
test_rollback_managed_only (test_installer.InstallerTests.test_rollback_managed_only) ... ok
test_traversal_transaction (test_installer.InstallerTests.test_traversal_transaction) ... ok
test_output_digest_mismatch (test_package.BuildParserTests.test_output_digest_mismatch) ... ok
test_assembler_rejects_real_preserved_content_conflict (test_package.PackageTests.test_assembler_rejects_real_preserved_content_conflict) ... ok
test_no_design_in_game (test_package.PackageTests.test_no_design_in_game) ... ok
test_seed_project_schema_valid (test_package.PackageTests.test_seed_project_schema_valid) ... ok
test_significant_generic_invariants_retained (test_review_amendments.ReviewAmendmentTests.test_significant_generic_invariants_retained) ... ok
test_facts_disagree (test_runtime.ProcessTests.test_facts_disagree) ... ok
test_timeout (test_runtime.ProcessTests.test_timeout) ... ok
test_approval_subject (test_runtime.RuntimeTests.test_approval_subject) ... ok
test_concurrent_state_revision (test_runtime.RuntimeTests.test_concurrent_state_revision) ... ok
test_duplicate_check_id (test_runtime.RuntimeTests.test_duplicate_check_id) ... ok
test_illegal_transition (test_runtime.RuntimeTests.test_illegal_transition) ... ok
test_missing_artifact (test_runtime.RuntimeTests.test_missing_artifact) ... ok
test_missing_reference (test_runtime.RuntimeTests.test_missing_reference) ... ok
test_nunit_requires_names (test_runtime.RuntimeTests.test_nunit_requires_names) ... ok
test_preflight_no_writes (test_runtime.RuntimeTests.test_preflight_no_writes) ... ok
test_required_above_profile (test_runtime.RuntimeTests.test_required_above_profile) ... ok
test_stale_human_acceptance (test_runtime.RuntimeTests.test_stale_human_acceptance) ... ok
test_unknown_schema_keyword (test_runtime.RuntimeTests.test_unknown_schema_keyword) ... ok
test_wrong_version (test_runtime.RuntimeTests.test_wrong_version) ... ok

----------------------------------------------------------------------
Ran 25 tests in 3.801s

OK
```

## Partition 4

```text
test_foreign_profile_invariants_are_rejected (test_game_agnostic.GameAgnosticTests.test_foreign_profile_invariants_are_rejected) ... ok
test_reference_only_lesson_is_not_a_knowledge_selection (test_game_agnostic.GameAgnosticTests.test_reference_only_lesson_is_not_a_knowledge_selection) ... ok
test_bad_approval_no_install (test_installer.InstallerTests.test_bad_approval_no_install) ... ok
test_managed_edits_conflict (test_installer.InstallerTests.test_managed_edits_conflict) ... ok
test_rollback_preserves_edited_seed (test_installer.InstallerTests.test_rollback_preserves_edited_seed) ... ok
test_wrong_destination (test_installer.InstallerTests.test_wrong_destination) ... ok
test_stale_output_directory (test_package.BuildParserTests.test_stale_output_directory) ... ok
test_assembler_rejects_unsafe_reference (test_package.PackageTests.test_assembler_rejects_unsafe_reference) ... ok
test_package_additions_no_false_full_pass (test_package.PackageTests.test_package_additions_no_false_full_pass) ... ok
test_applicable_detail_checklists_present (test_review_amendments.ReviewAmendmentTests.test_applicable_detail_checklists_present) ... ok
test_audit_detects_mutation (test_runtime.ProcessTests.test_audit_detects_mutation) ... ok
test_facts_match (test_runtime.ProcessTests.test_facts_match) ... ok
test_two_materially_different_profiles (test_runtime.ProcessTests.test_two_materially_different_profiles) ... ok
test_archive_and_no_task_reuse (test_runtime.RuntimeTests.test_archive_and_no_task_reuse) ... ok
test_dirty_after_plan_before_approval (test_runtime.RuntimeTests.test_dirty_after_plan_before_approval) ... ok
test_duplicate_json_keys (test_runtime.RuntimeTests.test_duplicate_json_keys) ... ok
test_interrupted_run_resume (test_runtime.RuntimeTests.test_interrupted_run_resume) ... ok
test_missing_configuration (test_runtime.RuntimeTests.test_missing_configuration) ... ok
test_named_suite_failure_not_leaf_pass (test_runtime.RuntimeTests.test_named_suite_failure_not_leaf_pass) ... ok
test_nunit_requires_positive_count (test_runtime.RuntimeTests.test_nunit_requires_positive_count) ... ok
test_protected_mutation_blocks (test_runtime.RuntimeTests.test_protected_mutation_blocks) ... ok
test_required_na_rejected (test_runtime.RuntimeTests.test_required_na_rejected) ... ok
test_structural_approval_not_authentication (test_runtime.RuntimeTests.test_structural_approval_not_authentication) ... ok
test_unlock_cannot_terminate_live_owner (test_runtime.RuntimeTests.test_unlock_cannot_terminate_live_owner) ... ok

----------------------------------------------------------------------
Ran 24 tests in 6.379s

OK
```

## Partition 5

```text
test_generic_lesson_preserves_fifteen_responsibilities (test_game_agnostic.GameAgnosticTests.test_generic_lesson_preserves_fifteen_responsibilities) ... ok
test_scanner_rejects_name_variants (test_game_agnostic.GameAgnosticTests.test_scanner_rejects_name_variants) ... ok
test_conflicting_agents_preserved (test_installer.InstallerTests.test_conflicting_agents_preserved) ... ok
test_preserve_not_blanket_override (test_installer.InstallerTests.test_preserve_not_blanket_override) ... ok
test_rollback_preview_read_only (test_installer.InstallerTests.test_rollback_preview_read_only) ... ok
test_cancelled_not_pass (test_package.BuildParserTests.test_cancelled_not_pass) ... ok
test_success_actual_hashed_output (test_package.BuildParserTests.test_success_actual_hashed_output) ... ok
test_budget_metrics (test_package.PackageTests.test_budget_metrics) ... ok
test_release_actual_match (test_package.PackageTests.test_release_actual_match) ... ok
test_knowledge_digest_tracks_k12_without_extra_uploads (test_review_amendments.ReviewAmendmentTests.test_knowledge_digest_tracks_k12_without_extra_uploads) ... ok
test_build_failure (test_runtime.ProcessTests.test_build_failure) ... ok
test_missing_artifact (test_runtime.ProcessTests.test_missing_artifact) ... ok
test_wrong_run_identity (test_runtime.ProcessTests.test_wrong_run_identity) ... ok
test_begin_without_approval (test_runtime.RuntimeTests.test_begin_without_approval) ... ok
test_draft_is_not_execution (test_runtime.RuntimeTests.test_draft_is_not_execution) ... ok
test_duplicate_receipt_check (test_runtime.RuntimeTests.test_duplicate_receipt_check) ... ok
test_lfs_pointer_blocks (test_runtime.RuntimeTests.test_lfs_pointer_blocks) ... ok
test_missing_design_approval (test_runtime.RuntimeTests.test_missing_design_approval) ... ok
test_nested_instruction_conflict (test_runtime.RuntimeTests.test_nested_instruction_conflict) ... ok
test_open_overlay_decision (test_runtime.RuntimeTests.test_open_overlay_decision) ... ok
test_raw_output_reparsed_not_green_wrapper (test_runtime.RuntimeTests.test_raw_output_reparsed_not_green_wrapper) ... ok
test_resume_discovery (test_runtime.RuntimeTests.test_resume_discovery) ... ok
test_symlink_escape (test_runtime.RuntimeTests.test_symlink_escape) ... ok
test_unreconciled_overlay (test_runtime.RuntimeTests.test_unreconciled_overlay) ... ok

----------------------------------------------------------------------
Ran 24 tests in 4.996s

OK
```
