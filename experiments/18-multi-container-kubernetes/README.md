# Experiment 18 Multi Container App with Kubernetes

## Aim

Deploy and scale a multi-service Kubernetes application.

## Procedure and result

Nginx, Flask and MySQL run in separate Deployments. Nginx proxies API requests to Flask, which records visits in persistent MySQL storage.

1. Start Kubernetes and confirm a default StorageClass for the PVC.
2. Run `bash create-secret.sh` once for a fresh lab; preserve the generated secret with its data volume.
3. Build and load the two images as described in `deploy-local.sh`, then execute that script.
4. Open Docker Desktop NodePort 30008 or use `kubectl port-forward service/frontend-service 5018:80`.
5. Click Check services; expect database connected and an increasing visits count.
6. Run `kubectl scale deployment/frontend --replicas=3` and wait for the rollout.
7. Capture the response, persistent data and three Ready frontend pods.

Observed: code/wiring checks passed; database contract tests use a mock. Live MySQL, cluster, persistence and scaling checks are pending. Only the frontend is exposed by NodePort.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
