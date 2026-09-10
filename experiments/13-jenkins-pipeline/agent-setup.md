# Jenkins agent requirements

Use Jenkins with a dedicated agent labeled `docker`. The agent needs Git, a
Docker CLI with access to a working Docker daemon, and curl. Docker daemon
access is privileged; use a dedicated lab agent, not a shared production host.
Installing a plain Jenkins controller container does not give it a Docker daemon.

Create a Pipeline job, choose Pipeline script from SCM, select Git, set this
repository URL and branch `main`, and set Script Path to
`experiments/13-jenkins-pipeline/Jenkinsfile`. Use a Jenkins GitHub credential if
the repository is private. Click Build Now. Checkout, Build, Test and Deploy
must all pass. The app runs on the agent's loopback port 5013. For a remote
agent use an SSH tunnel to view it. Save the actual console output and stage view.
