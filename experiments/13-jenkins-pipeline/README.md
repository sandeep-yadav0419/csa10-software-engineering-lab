# Experiment 13 CI CD using Jenkins

## Aim

Automate building, testing and deployment with Jenkins.

## Procedure and result

Read `agent-setup.md` and configure a Pipeline from SCM job to use this experiment's Jenkinsfile.

1. Use a dedicated agent labeled docker with Git, Docker daemon access and curl.
2. Set the repository URL, main branch and the correct Jenkinsfile path.
3. Run Build Now and inspect Checkout, Build, Test and Deploy stages.
4. The Test stage runs Flask assertions in the built image.
5. Deploy replaces only the named lab container and verifies its HTTP health response.
6. Browse agent loopback port 5013, using an SSH tunnel if needed.
7. Save the real stage view, console output and app screenshot.

Observed: source tests passed, and GitHub Actions built and served this Docker image successfully. A Jenkins server and Docker agent are still required for the literal Jenkins pipeline run. A plain Jenkins controller container does not supply a Docker daemon.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
