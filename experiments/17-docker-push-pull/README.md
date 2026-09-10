# Experiment 17 Push and Pull Docker Image

## Aim

Demonstrate Docker image push and pull.

## Procedure and result

From this folder:

```bash
export DOCKER_USER=YOUR_DOCKER_HUB_USERNAME
bash push-pull.sh
```

1. Authenticate to Docker Hub through its CLI prompt.
2. Inspect the push digest and pull output for csa10-html-site:v1.
3. Open `http://localhost:8017`.
4. Capture the Docker Hub tag, CLI output and browser page.
5. Stop the named container with `docker stop csa10-pulled-site`.

`docker ps` lists containers and `docker images` lists local images; neither lists your remote repositories. A second container cannot bind an already-used host port.

Observed: GitHub Actions built the image, ran it, and verified its HTTP response. A real Docker Hub push and clean pull by authenticated account are still pending.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
