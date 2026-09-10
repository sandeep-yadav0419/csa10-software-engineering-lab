#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
docker build -t se-lab/flask-api:local .
# Docker Desktop Kubernetes shares its local image store. For kind, first use:
# kind load docker-image se-lab/flask-api:local
# For minikube: minikube image load se-lab/flask-api:local
kubectl apply -f deployment.yaml -f service.yaml
kubectl rollout status deployment/flask-api --timeout=180s
kubectl get pods -l app=flask-api
kubectl get service flask-api-service
