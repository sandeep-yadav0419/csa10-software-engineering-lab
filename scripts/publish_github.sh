#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
command -v gh >/dev/null || { echo 'Install GitHub CLI, then run gh auth login.'; exit 1; }
gh auth status
name="${1:-csa10-software-engineering-lab}"
owner=$(gh api user --jq .login)
if gh repo view "$owner/$name" >/dev/null 2>&1; then
  echo "Repository $owner/$name already exists. Stopping without changes."
  exit 1
fi
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if [ "$(git rev-parse --show-toplevel)" != "$PWD" ]; then
    echo 'This folder is inside another repository. Extract it outside that repository first.'
    exit 1
  fi
else
  git init -b main
fi
if git remote get-url origin >/dev/null 2>&1; then
  echo 'An origin already exists. Stopping without replacing it.'
  exit 1
fi
git add .
if ! git diff --cached --quiet; then
  git commit -m 'Implement the 25 CSA10 software engineering lab experiments'
fi
gh repo create "$owner/$name" --private --source=. --remote=origin --push --description 'CSA10 lab experiments: Agile, Figma, Git, Docker, Kubernetes and CI/CD'
gh repo view "$owner/$name" --json url --jq .url
