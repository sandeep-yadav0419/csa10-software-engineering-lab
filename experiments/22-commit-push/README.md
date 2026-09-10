# Experiment 22 Commit and Push Changes

## Aim

Stage, commit and push changes.

## Procedure and result

From the cloned repository:

```bash
git add README.md
git commit -m "Update the project description"
git push origin main
git status
```

Verify the remote branch's latest commit and changed README. If main is protected, use a branch and PR instead of bypassing its rules. A clean working tree alone does not prove a GitHub push.

Observed: staging, committing and pushing ran against a local bare origin in the reproducible exercise. Live GitHub publication is recorded separately.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
