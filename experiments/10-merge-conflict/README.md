# Experiment 10 Git Branching and Merge Conflict

## Aim

Create and resolve a real Git merge conflict.

## Procedure and result

Run `python3 scripts/git_lab.py` from the repository root. It uses disposable local repositories.

1. The script creates a feature branch and modifies the README mode line.
2. It changes that same line differently on main.
3. A merge is attempted; a nonzero result and conflict markers are verified.
4. The markers are replaced with a resolution preserving both intentions.
5. The resolution is staged and committed. The index is checked for unresolved files.
6. The resolved main branch is pushed to the local origin and its graph recorded.

Result: a real conflict occurred and was resolved, committed and pushed locally. See [the transcript](../../evidence/git-workflow.log). A GitHub PR is a separate remote step.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
