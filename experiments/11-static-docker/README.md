# Experiment 11 Static Website with Docker

## Aim

Containerize and serve a static website with Nginx.

## Procedure and result

From this experiment folder:

```bash
docker build -t se-lab/static-site:local .
docker run -d --name csa10-static -p 127.0.0.1:8080:80 se-lab/static-site:local
curl --fail http://localhost:8080
docker ps --filter name=csa10-static
```

Open the page and capture it with the running container. If port 8080 is busy, map `127.0.0.1:8011:80` and use port 8011. Stop this container using `docker stop csa10-static`; remove that stopped container before reusing the name.

Expected: the page responds through Nginx. Observed: HTML and Dockerfile are prepared. Docker execution is pending because Docker is absent here.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
