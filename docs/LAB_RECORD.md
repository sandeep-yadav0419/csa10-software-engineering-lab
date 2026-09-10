# Software Engineering Lab Record

Prepared for Sandeep. These 25 records follow the uploaded lab list. Actual local results are distinguished from external execution still required. Registration number, faculty signatures, stakeholder responses and peer reviews were not supplied and have not been invented.

Use individual experiment READMEs for their working directories and relative links. This combined record is a reading copy.

## Experiment 1 Create a Kanban Board

**Aim:** Create and simulate a Kanban workflow in Jira or Trello.

Use `board.json` and `jira-import.csv`. There are three tasks and the required To Do, In Progress and Done columns.

1. Create a Library Management Kanban board in Jira or Trello.
2. Import the three tasks into Jira, or add their titles as Trello cards.
3. Move each task from To Do through In Progress to Done.
4. Capture the board during progress and after completion.
5. Run `python3 scripts/simulate_kanban.py` from the repository root for the included local simulation.

Expected: all three tasks reach Done with their intermediate transitions visible.
Observed: the local simulation ran. A live board and screenshots are pending access.

## Experiment 2 Bus Ticket Booking Prototype

**Aim:** Design a simple Bus Ticket Booking System prototype in Figma.

Four screens are supplied: Home, Search Bus, Seat Selection and Payment Summary.

1. Open `preview.html` and follow Search a bus → Choose seats → Continue to payment → Finish demo booking.
2. Check the back buttons. The route, fare and A3 seat are fixed sample choices for this navigation prototype.
3. Follow `figma-plugin/README.md` to run the development plugin in Figma. It creates editable native frames and prototype reactions.
4. Select Home, start Present mode, and check forward and back navigation.
5. Save the real Figma URL, screenshots of all frames and the prototype links.

Expected: a clickable four screen Figma flow. Payment is a mock action.
Observed: designs and link checks are ready. Execution in a connected Figma account is pending.

## Experiment 3 E Commerce Mobile App Prototype

**Aim:** Design two mobile UI variants for stakeholder feedback.

Eight screens are supplied: Home, Product, Cart and Checkout for variants A and B. A uses a product grid; B uses a list.

1. Open `preview.html`. From A Home follow View grid notebook → Add to cart → Continue to checkout → Finish demo order.
2. Repeat from B Home and compare the same sample product and price.
3. Follow the Figma development plugin instructions to generate all eight frames.
4. Present each variant from its own Home frame.
5. Ask a reviewer to complete the shopping task and enter their actual observations in `stakeholder-feedback.md`.
6. Choose a variant based on recorded feedback and explain the decision.

Observed: designs, links and the feedback form are prepared. A real Figma file, stakeholder feedback and the final design decision are pending.

## Experiment 4 Scrum Project in Jira

**Aim:** Create and manage a one week Scrum sprint in Jira.

Use the five ranked stories in `backlog.csv`, the import file and `sprint-plan.md`. The authored backlog totals 16 estimated story points.

1. Create a Scrum project named Library Management System.
2. Import the five stories and enter their acceptance criteria and estimates.
3. Rank login, search, issue, return and history in that order.
4. Create a one week sprint using actual dates. Check team capacity before starting it.
5. Move stories through To Do, In Progress and Done only when their criteria are met.
6. Close the sprint; move unfinished work back to the backlog.
7. Capture backlog, active board and completed sprint evidence.

Observed: backlog and sprint plan are complete. Jira sprint execution is pending; estimates are planning examples, not hours or observed team velocity.

## Experiment 5 Library Management System MoSCoW

**Aim:** Categorize library requirements using the MoSCoW method.

Open `requirements-prioritization.xlsx`, Library tab. `requirements.csv` contains the same authored data.

1. Review all 12 requirements, their impact and feasibility.
2. Inspect each MoSCoW category and its justification.
3. Filter the table to compare release scope. Won't Have means outside this release.
4. Change one category using its dropdown and observe the summary counts update.
5. Restore the proposal or retain your justified revision.

Result: 6 Must Have, 3 Should Have, 2 Could Have and 1 Won't Have requirements are documented. Counts and editable-category recalculation were verified. The requirements are authored lab examples, not externally elicited data.

## Experiment 6 Link Jira with Confluence

**Aim:** Integrate Jira with Confluence for project tracking.

Use `confluence-page.md` and `issues.jql` with experiment 04.

1. Create a Library Management System Confluence space and a page.
2. Insert the supplied page content and replace LIB with the actual Jira project key.
3. Insert a Jira Issues macro using `/jira` and the integration available in your workspace.
4. Use `project = LIB ORDER BY status ASC, priority DESC`. Display Key, Summary, Status, Assignee and Priority.
5. Change a Jira issue status, refresh the Confluence page and verify the reflected change.
6. Capture the live issue table and the matching Jira issue.

Observed: content and query are prepared. The live link and required screenshot are pending. Do not infer instant updates without observing them.

## Experiment 7 Task Management System MoSCoW and Kano

**Aim:** Prioritize task requirements using MoSCoW and Kano.

Use `prioritization.csv`, `jira-import.csv`, and the Task system tab in [the shared workbook](../05-library-moscow/requirements-prioritization.xlsx).

1. Create a Task Management Jira project and import the seven features.
2. Preserve MoSCoW and Kano labels and their justifications in descriptions or custom fields.
3. Rank the backlog in the supplied order.
4. Compare a Must-be need, a One-dimensional improvement and an Attractive addition.
5. Save ranked-backlog and category-filter evidence.

Result: all seven proposed classifications are documented. Jira import is pending. Kano categories are hypotheses; validating them requires real functional and dysfunctional stakeholder responses.

## Experiment 8 Online Learning Platform MoSCoW and Kano

**Aim:** Prioritize six online learning platform features.

Use `prioritization.csv`, `jira-import.csv`, and the Learning tab in [the shared workbook](../05-library-moscow/requirements-prioritization.xlsx).

1. Create an Online Learning Jira project and import all six features.
2. Apply the proposed MoSCoW and Kano categories.
3. Rank sign in, enrollment and lessons first; consider quizzes before recommendations.
4. Keep VR outside the current release and record its scope justification.
5. Capture the six-item backlog and priority results.

Result: exactly six features have categories, ranks and reasons. Jira execution and stakeholder validation are pending. An Attractive feature can be Won't Have because it exceeds the release budget or scope.

## Experiment 9 Fork and Pull Request Workflow

**Aim:** Demonstrate collaboration using a fork and pull request.

The local remote workflow is executable through `python3 scripts/git_lab.py` from the repository root.

For the literal GitHub exercise, choose a repository whose maintainer expects your contribution:

1. Fork it into your account and clone the fork.
2. Run `git switch -c feature-branch` and make a useful code or README change.
3. Stage, commit and push using separate commands.
4. Create a PR with the original repository as base and your fork branch as head.
5. Obtain a real review, address feedback and push the updated branch.
6. Merge only when required checks and review permit it.

Observed: the local fork topology and contribution sequence ran. No external GitHub fork, unsolicited upstream PR or peer review is claimed.

## Experiment 10 Git Branching and Merge Conflict

**Aim:** Create and resolve a real Git merge conflict.

Run `python3 scripts/git_lab.py` from the repository root. It uses disposable local repositories.

1. The script creates a feature branch and modifies the README mode line.
2. It changes that same line differently on main.
3. A merge is attempted; a nonzero result and conflict markers are verified.
4. The markers are replaced with a resolution preserving both intentions.
5. The resolution is staged and committed. The index is checked for unresolved files.
6. The resolved main branch is pushed to the local origin and its graph recorded.

Result: a real conflict occurred and was resolved, committed and pushed locally. See [the transcript](../../evidence/git-workflow.log). A GitHub PR is a separate remote step.

## Experiment 11 Static Website with Docker

**Aim:** Containerize and serve a static website with Nginx.

From this experiment folder:

```bash
docker build -t se-lab/static-site:local .
docker run -d --name csa10-static -p 127.0.0.1:8080:80 se-lab/static-site:local
curl --fail http://localhost:8080
docker ps --filter name=csa10-static
```

Open the page and capture it with the running container. If port 8080 is busy, map `127.0.0.1:8011:80` and use port 8011. Stop this container using `docker stop csa10-static`; remove that stopped container before reusing the name.

Result: GitHub Actions built the Nginx image, ran it, and received a successful HTTP response. A manual browser screenshot is still needed only if required for the submitted record.

## Experiment 12 Flask API with Docker and Kubernetes

**Aim:** Deploy a Flask API with Docker and Kubernetes.

The API exposes `/`, `/about` and `/health`. The Deployment uses two replicas and the Service uses NodePort 30007.

1. Start Docker Desktop Kubernetes and check `kubectl config current-context`.
2. Run `bash deploy-local.sh` in this folder to build, apply and wait for the rollout.
3. With kind/minikube, load the image into the cluster before applying; see script comments.
4. On Docker Desktop, open `http://localhost:30007` and `/about`.
5. Portable alternative: `kubectl port-forward service/flask-api-service 5012:5000`, then browse port 5012.
6. Capture both endpoints, two Ready pods and the service output.

Observed: endpoint and manifest checks passed, and GitHub Actions built and served the Docker image successfully. An actual Kubernetes rollout, two-Ready-pod evidence, and NodePort/port-forward capture remain pending. Local image names must be published or replaced for a remote cluster.

## Experiment 13 CI CD using Jenkins

**Aim:** Automate building, testing and deployment with Jenkins.

Read `agent-setup.md` and configure a Pipeline from SCM job to use this experiment's Jenkinsfile.

1. Use a dedicated agent labeled docker with Git, Docker daemon access and curl.
2. Set the repository URL, main branch and the correct Jenkinsfile path.
3. Run Build Now and inspect Checkout, Build, Test and Deploy stages.
4. The Test stage runs Flask assertions in the built image.
5. Deploy replaces only the named lab container and verifies its HTTP health response.
6. Browse agent loopback port 5013, using an SSH tunnel if needed.
7. Save the real stage view, console output and app screenshot.

Observed: source tests passed, and GitHub Actions built and served this Docker image successfully. A Jenkins server and Docker agent are still required for the literal Jenkins pipeline run. A plain Jenkins controller container does not supply a Docker daemon.

## Experiment 14 Continuous Deployment with GitHub Actions

**Aim:** Automate Docker building and deployment with GitHub Actions.

The corrected application returns `CI/CD Pipeline Updated Successfully!`. Workflows are in the repository-level `.github/workflows/`.

1. Upload the repository and inspect the validation workflow.
2. Follow [CI setup](../../docs/ci-setup.md) to configure Docker Hub and its secrets.
3. Run Publish lab images to Docker Hub or push a change to this experiment.
4. Verify the csa10-actions-app image with the current commit SHA tag.
5. Run `docker run --rm -p 127.0.0.1:5014:5000 YOUR_DOCKER_USER/csa10-actions-app:TAG`.
6. Record the response, workflow URL and image tag.

Observed: hosted tests passed; GitHub Actions built the image, started it, and verified its HTTP response. Docker Hub publication was intentionally skipped because its credentials and enable variable were not supplied. Publishing an image alone does not start a deployed application.

## Experiment 15 GitHub Version Control

**Aim:** Implement a version control workflow with module branches.

Run `python3 scripts/git_lab.py` for the isolated local exercise. It creates module1 and module2 branches with catalogue-search and overdue-loan code, then records their merge commits.

For GitHub:

1. Clone the new repository, branch from main and implement one module.
2. Stage, commit and push module1.
3. Repeat from updated main for module2.
4. Create one PR per module, obtain a review and address the feedback.
5. Merge according to repository rules and pull the final main branch.
6. Update the README with the project and actual team members.

Prepared for Sandeep; no additional teammates were supplied. Observed: local branch/merge operations ran. GitHub module PRs and peer review remain separate requirements.

## Experiment 16 Containerize Flask To Do App

**Aim:** Containerize a Flask To Do application.

The app adds, completes, reopens and deletes tasks. SQLite and a named Docker volume preserve records.

```bash
docker compose up --build -d
docker compose ps
```

1. Open `http://localhost:5016`. Add, complete and reopen a task.
2. Run `docker compose restart`; confirm the task remains.
3. Delete the task. Check that blank and overlong tasks are rejected.
4. To publish, build with `docker build -t YOUR_DOCKER_USER/flask-todo-app:v1 .`, run `docker login`, then push that tag.
5. Save app, container and persistence evidence. `docker compose down` retains data; `down -v` deletes the volume.

Observed: application tests passed, including persistence and HTML escaping; GitHub Actions also built and served the image successfully. A Compose restart with the named volume and registry publication remain pending. This is a single-user loopback lab app, not a public authentication service.

## Experiment 17 Push and Pull Docker Image

**Aim:** Demonstrate Docker image push and pull.

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

Observed: GitHub Actions built the image, ran it, and verified its HTTP response. A real Docker Hub push and clean pull by an authenticated account are still pending.

## Experiment 18 Multi Container App with Kubernetes

**Aim:** Deploy and scale a multi-service Kubernetes application.

Nginx, Flask and MySQL run in separate Deployments. Nginx proxies API requests to Flask, which records visits in persistent MySQL storage.

1. Start Kubernetes and confirm a default StorageClass for the PVC.
2. Run `bash create-secret.sh` once for a fresh lab; preserve the generated secret with its data volume.
3. Build and load the two images as described in `deploy-local.sh`, then execute that script.
4. Open Docker Desktop NodePort 30008 or use `kubectl port-forward service/frontend-service 5018:80`.
5. Click Check services; expect database connected and an increasing visits count.
6. Run `kubectl scale deployment/frontend --replicas=3` and wait for the rollout.
7. Capture the response, persistent data and three Ready frontend pods.

Observed: code/wiring checks passed; database contract tests use a mock, and GitHub Actions built and served the backend image. Live Nginx-to-Flask-to-MySQL cluster operation, persistence and scaling checks remain pending. Only the frontend is exposed by NodePort.

## Experiment 19 CI CD with GitHub Actions

**Aim:** Automate testing, publishing and deployment of a Flask app.

Use the application and Dockerfile with the root workflows and [CI setup](../../docs/ci-setup.md).

1. Push a main-branch update and inspect validation.
2. Configure Docker Hub secrets and DOCKERHUB_ENABLED=true.
3. Publishing tests the code before building and pushing csa10-flask-cicd for amd64 and arm64.
4. Verify its commit SHA tag. Configure an existing dedicated Linux/EC2 host with Docker and a runner labeled se-lab.
5. Set DEPLOY_ENABLED=true and run deployment with that tag.
6. Inspect the named container and health check; tunnel host loopback port 5019 to your Mac.
7. Save actual workflow, image and deployment evidence.

Observed: the GitHub-hosted validation workflow passed, including Docker build, container start and HTTP response. The Docker Hub publication job skipped because credentials were not configured; no EC2 instance or running deployment is claimed. Use an existing lab host where available.

## Experiment 20 Create GitHub Repository

**Aim:** Create and update a GitHub repository.

1. Create csa10-software-engineering-lab in your account and choose visibility.
2. Initialize a README if using the connector upload route.
3. Clone its HTTPS URL and edit the project description.
4. Stage, commit and push the README.
5. Verify the repository page and latest commit.

Result: the private [csa10-software-engineering-lab repository](https://github.com/sandeep-yadav0419/csa10-software-engineering-lab) was created, all 132 prepared files were uploaded, and their remote Git blob hashes were verified. See [the publication evidence](../../evidence/github-publication.md).

The included `scripts/publish_github.sh` remains an optional repeatable CLI route. It stops rather than replacing an existing origin or repository.

## Experiment 21 Clone and Modify Repository

**Aim:** Clone a repository and modify a file.

1. Copy the repository clone URL from GitHub.
2. Run `git clone URL` and enter the created folder.
3. Change a descriptive sentence in README.
4. Run `git diff -- README.md` to inspect the change.
5. Run `git status --short` to confirm the modified file.

Observed: a real clone and modification were verified in the isolated local exercise. See [the Git transcript](../../evidence/git-workflow.log). Repeat with the created GitHub URL if the instructor needs GitHub-hosted evidence. A merge conflict is not required for this experiment.

## Experiment 22 Commit and Push Changes

**Aim:** Stage, commit and push changes.

From the cloned repository:

```bash
git add README.md
git commit -m "Update the project description"
git push origin main
git status
```

Verify the remote branch's latest commit and changed README. If main is protected, use a branch and PR instead of bypassing its rules. A clean working tree alone does not prove a GitHub push.

Observed: staging, committing and pushing ran against a local bare origin in the reproducible exercise. The complete package was also committed to GitHub `main`, followed by the merged feature-login commit. See [the publication evidence](../../evidence/github-publication.md).

## Experiment 23 Pull Latest Changes

**Aim:** Receive remote changes in a local repository.

1. Start with two clones of one repository.
2. Update README in the second clone, commit and push to origin/main.
3. In the first clone run `git pull --ff-only origin main`.
4. Inspect README and `git log -1` to confirm the received change.
5. If a fast-forward is impossible, inspect the divergence before choosing merge or rebase.

Observed: the two-checkout sequence ran and its changed content was asserted. Both checkouts were operated by the local exercise, so no human collaborator is implied. See the Git transcript for the actual commands and output.

## Experiment 24 Create feature login Branch

**Aim:** Implement a login function on a feature-login branch.

`login.py` checks supplied password hashes. It does not publish a hardcoded admin password.

1. Run `git switch -c feature-login`.
2. Run `python3 experiments/24-feature-login/login.py` after installing the root requirements.
3. Set a temporary demonstration password and test valid/invalid login.
4. Make a real improvement, stage the file, commit and push feature-login.
5. Open a PR to main, obtain review and merge according to repository rules.

The full package already contains the implementation; repeating the exercise requires an incremental change before committing.

Result: valid, invalid, empty, malformed and unknown-user checks passed. The real GitHub `feature-login` branch changed the implementation and tests; [PR #1](https://github.com/sandeep-yadav0419/csa10-software-engineering-lab/pull/1) passed all nine CI jobs and was squash-merged into `main`. Automated inspection was performed; no human peer review is claimed.

## Experiment 25 Fork and Implement Feature

**Aim:** Add a feature using a fork workflow without breaking existing behavior.

`feature.py` implements completion_percent(done, total), with validation and defined behavior for an empty task list.

1. Fork an appropriate original repository whose maintainer expects a contribution.
2. Clone it and add the original as upstream.
3. Create feature-new and integrate the function where relevant.
4. Run existing tests plus the new boundary/invalid-input tests.
5. Commit and push feature-new, then open a PR to the original repository.
6. Describe the change and verification; respond to actual reviewer feedback.

Observed: feature tests passed and a separate local fork remote was used for branching, pushing, fetching and merging. No GitHub fork PR against an arbitrary third-party repository or reviewer approval is claimed.
