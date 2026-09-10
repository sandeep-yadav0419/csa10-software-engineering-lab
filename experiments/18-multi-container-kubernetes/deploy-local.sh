#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
docker build -t se-lab/backend:local backend
docker build -t se-lab/frontend:local frontend
# For kind or minikube, load both images into the cluster before continuing.
# kind load docker-image se-lab/backend:local se-lab/frontend:local
# minikube image load se-lab/backend:local
# minikube image load se-lab/frontend:local
kubectl get secret lab-db >/dev/null
kubectl apply -f services.yaml -f mysql-deployment.yaml -f backend-deployment.yaml -f frontend-deployment.yaml
kubectl rollout status deployment/mysql --timeout=240s
kubectl rollout status deployment/backend --timeout=180s
kubectl rollout status deployment/frontend --timeout=180s
kubectl get deployments,pods,services,pvc
