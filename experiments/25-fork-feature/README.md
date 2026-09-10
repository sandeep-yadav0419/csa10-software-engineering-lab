# Experiment 25 Fork and Implement Feature

## Aim

Add a feature using a fork workflow without breaking existing behavior.

## Procedure and result

`feature.py` implements completion_percent(done, total), with validation and defined behavior for an empty task list.

1. Fork an appropriate original repository whose maintainer expects a contribution.
2. Clone it and add the original as upstream.
3. Create feature-new and integrate the function where relevant.
4. Run existing tests plus the new boundary/invalid-input tests.
5. Commit and push feature-new, then open a PR to the original repository.
6. Describe the change and verification; respond to actual reviewer feedback.

Observed: feature tests passed and a separate local fork remote was used for branching, pushing, fetching and merging. No GitHub fork PR against an arbitrary third-party repository or reviewer approval is claimed.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
