# Experiment 19 CI CD with GitHub Actions

## Aim

Automate testing, publishing and deployment of a Flask app.

## Procedure and result

Use the application and Dockerfile with the root workflows and [CI setup](../../docs/ci-setup.md).

1. Push a main-branch update and inspect validation.
2. Configure Docker Hub secrets and DOCKERHUB_ENABLED=true.
3. Publishing tests the code before building and pushing csa10-flask-cicd for amd64 and arm64.
4. Verify its commit SHA tag. Configure an existing dedicated Linux/EC2 host with Docker and a runner labeled se-lab.
5. Set DEPLOY_ENABLED=true and run deployment with that tag.
6. Inspect the named container and health check; tunnel host loopback port 5019 to your Mac.
7. Save actual workflow, image and deployment evidence.

Observed: the GitHub-hosted validation workflow passed, including Docker build, container start and HTTP response. The Docker Hub publication job skipped because credentials were not configured; no EC2 instance or running deployment is claimed. Use an existing lab host where available.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
