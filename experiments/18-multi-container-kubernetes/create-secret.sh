#!/usr/bin/env bash
set -euo pipefail
# Use random lab passwords without displaying them or saving them in Git.
task_secret_dir=$(mktemp -d)
chmod 700 "$task_secret_dir"
trap 'rm -rf "$task_secret_dir"' EXIT
python3 - "$task_secret_dir" <<'PY'
import os, secrets, sys
from pathlib import Path
for name in ['root-password','app-password']:
    path=Path(sys.argv[1])/name
    path.write_text(secrets.token_urlsafe(32))
    os.chmod(path,0o600)
PY
# Run once for a fresh lab. Existing secrets are not overwritten because the
# database volume may already contain credentials. This command fails if it exists.
kubectl create secret generic lab-db --from-file=root-password="$task_secret_dir/root-password" --from-file=app-password="$task_secret_dir/app-password"
