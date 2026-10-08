# Initial validation before manifest synchronization

The initial 19-case focused run started after regenerating the shared snapshot schema but before updating PACKAGE_FILES.json. It observed 18 passing cases and one installer error. The actual tool-returned failure excerpt was:

```
test_managed_install_and_rollback_with_metadata_but_no_git ... ERROR
bh_runtime.BHError: Distribution changed: .bh/schema.json
Ran 19 tests in 2.499s
FAILED (errors=1)
```

This excerpt is not a saved complete raw transcript. The manifest was then synchronized with the changed installed files. The subsequent reconciled 257-case run includes the same 19 cases, all passing, with complete raw logs in this folder. No validation threshold or conflict check was waived.
