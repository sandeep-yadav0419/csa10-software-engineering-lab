# Experiment 23 Pull Latest Changes

## Aim

Receive remote changes in a local repository.

## Procedure and result

1. Start with two clones of one repository.
2. Update README in the second clone, commit and push to origin/main.
3. In the first clone run `git pull --ff-only origin main`.
4. Inspect README and `git log -1` to confirm the received change.
5. If a fast-forward is impossible, inspect the divergence before choosing merge or rebase.

Observed: the two-checkout sequence ran and its changed content was asserted. Both checkouts were operated by the local exercise, so no human collaborator is implied. See the Git transcript for the actual commands and output.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
