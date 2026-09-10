#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${DOCKER_USER:?Set DOCKER_USER to your Docker Hub username}"
image="$DOCKER_USER/csa10-html-site:v1"
docker build -t "$image" .
docker login
docker push "$image"
docker pull "$image"
docker run --rm -d --name csa10-pulled-site -p 127.0.0.1:8017:80 "$image"
docker ps --filter name=csa10-pulled-site
docker images "$DOCKER_USER/csa10-html-site"
curl --retry 10 --retry-delay 1 --retry-connrefused --fail http://localhost:8017
