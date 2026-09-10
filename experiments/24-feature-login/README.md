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

Observed: valid, invalid and unknown-user tests passed, and a local feature-login branch was created, pushed and merged. A GitHub PR and peer review require separate evidence.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
