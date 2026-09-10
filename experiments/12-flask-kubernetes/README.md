# Experiment 12 Flask API with Docker and Kubernetes

## Aim

Deploy a Flask API with Docker and Kubernetes.

## Procedure and result

The API exposes `/`, `/about` and `/health`. The Deployment uses two replicas and the Service uses NodePort 30007.

1. Start Docker Desktop Kubernetes and check `kubectl config current-context`.
2. Run `bash deploy-local.sh` in this folder to build, apply and wait for the rollout.
3. With kind/minikube, load the image into the cluster before applying; see script comments.
4. On Docker Desktop, open `http://localhost:30007` and `/about`.
5. Portable alternative: `kubectl port-forward service/flask-api-service 5012:5000`, then browse port 5012.
6. Capture both endpoints, two Ready pods and the service output.

Observed: endpoint tests and manifest checks passed. Actual container and cluster execution are pending. Local image names must be published/replaced for a remote cluster.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
