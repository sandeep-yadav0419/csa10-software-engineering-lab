# CI and deployment setup

The validation workflow runs Python tests and isolated Docker builds on pushes
and pull requests. A passing Python test is not proof of a Kubernetes deployment.

## Docker Hub publishing for experiments 14 and 19

1. Create Docker Hub repositories `csa10-actions-app` and `csa10-flask-cicd`.
2. In GitHub Settings → Secrets and variables → Actions, create secrets
   `DOCKER_USERNAME` and `DOCKER_PASSWORD`. Use a Docker Hub access token as the
   password; never put it in source files or chat.
3. Create the repository variable `DOCKERHUB_ENABLED` with value `true`.
4. Run `Publish lab images to Docker Hub` manually. Later main-branch changes
   in experiments 14 or 19 also trigger it. Inspect both matrix results.
5. Confirm the commit SHA tag exists in Docker Hub. Use the immutable SHA for
   a repeatable deployment; `latest` changes over time.

An unconfigured publish job is intentionally skipped, not described as a
successful publish. Images are built for amd64 and arm64 for Mac compatibility.

## Actual deployment

Image publication does not start an application. On a dedicated Linux lab host
or an existing EC2 instance, install Docker and register a GitHub self-hosted
runner with labels `linux` and `se-lab`. For a public repository, do not expose
that runner to untrusted pull requests. This deployment job is manual and does
not check out or execute PR source. Configure a `lab` environment, set
`DEPLOY_ENABLED=true`, then run `Deploy published Flask lab on a dedicated host`.
The job pulls the selected published image, replaces only `csa10-flask-lab` and
checks `/health`. It has no rollback if the replacement fails; inspect the logs
and rerun a previously working SHA.

The app binds to the host loopback port 5019. From a Mac use
`ssh -L 5019:127.0.0.1:5019 ubuntu@YOUR_HOST`, then open
`http://localhost:5019`. Use an existing lab instance if available. No AWS
instance was created, no payment was incurred, and no host is claimed deployed.
Record the workflow URL, image SHA, host test and real screenshots after execution.
