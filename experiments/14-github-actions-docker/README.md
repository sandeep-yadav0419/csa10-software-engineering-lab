# Experiment 14 Continuous Deployment with GitHub Actions

## Aim

Automate Docker building and deployment with GitHub Actions.

## Procedure and result

The corrected application returns `CI/CD Pipeline Updated Successfully!`. Workflows are in the repository-level `.github/workflows/`.

1. Upload the repository and inspect the validation workflow.
2. Follow [CI setup](../../docs/ci-setup.md) to configure Docker Hub and its secrets.
3. Run Publish lab images to Docker Hub or push a change to this experiment.
4. Verify the csa10-actions-app image with the current commit SHA tag.
5. Run `docker run --rm -p 127.0.0.1:5014:5000 YOUR_DOCKER_USER/csa10-actions-app:TAG`.
6. Record the response, workflow URL and image tag.

Observed: source, tests and workflows are prepared. Registry publication requires configuration. Publishing an image alone does not start a deployed application.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
