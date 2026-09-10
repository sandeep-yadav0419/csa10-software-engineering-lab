# Experiment 24 Create feature login Branch

## Aim

Implement a login function on a feature-login branch.

## Procedure and result

`login.py` checks supplied password hashes. It does not publish a hardcoded admin password.

1. Run `git switch -c feature-login`.
2. Run `python3 experiments/24-feature-login/login.py` after installing the root requirements.
3. Set a temporary demonstration password and test valid/invalid login.
4. Make a real improvement, stage the file, commit and push feature-login.
5. Open a PR to main, obtain review and merge according to repository rules.

The full package already contains the implementation; repeating the exercise requires an incremental change before committing.

Result: valid, invalid, empty, malformed and unknown-user checks passed. The real GitHub `feature-login` branch changed the implementation and tests; [PR #1](https://github.com/sandeep-yadav0419/csa10-software-engineering-lab/pull/1) passed all nine CI jobs and was squash-merged into `main`. Automated inspection was performed; no human peer review is claimed.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
