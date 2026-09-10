# CSA10 Software Engineering Lab

Prepared for Sandeep, following all 25 experiments in the supplied Software Engineering Lab Experiment List.

Includes experiment records, requirements and an Excel workbook, 12 prototype screens with Figma generation code, tested Flask apps, Dockerfiles, Kubernetes manifests, Jenkins/GitHub Actions pipelines, and reproducible Git exercises with a real merge conflict.

**Execution status:** all 25 folders contain their implementation assets and instructions. The private GitHub upload is verified, hosted validation passed, and the feature-login PR was merged. Live Jira/Figma, registry/cluster/server operations, fork PRs and stakeholder reviews require the access described in [STATUS.md](STATUS.md). Prepared files are not claimed as completed external deployments.

## Run on macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/validate_assets.py
python scripts/git_lab.py
```

Use Python 3.12 or newer. Docker Desktop/Kubernetes are additional requirements for container experiments. No paid API is used.

To run the To Do app: `python experiments/16-flask-todo/app.py`, then open `http://127.0.0.1:5000`. If port 5000 is busy, use `flask --app experiments/16-flask-todo/app.py run --port 5016`.

Open either prototype's `preview.html` directly, or serve this root with `python -m http.server 8090 --bind 127.0.0.1` and browse to its experiment folder. Designs use fixed sample selections and never process real payments.

## Experiment index

| No | Experiment |
| --- | --- |
| 01 | [Create a Kanban Board](experiments/01-kanban-board/README.md) |
| 02 | [Bus Ticket Booking Prototype](experiments/02-bus-booking-prototype/README.md) |
| 03 | [E Commerce Mobile App Prototype](experiments/03-ecommerce-prototype/README.md) |
| 04 | [Scrum Project in Jira](experiments/04-scrum-project/README.md) |
| 05 | [Library Management System MoSCoW](experiments/05-library-moscow/README.md) |
| 06 | [Link Jira with Confluence](experiments/06-jira-confluence/README.md) |
| 07 | [Task Management System MoSCoW and Kano](experiments/07-task-prioritization/README.md) |
| 08 | [Online Learning Platform MoSCoW and Kano](experiments/08-learning-prioritization/README.md) |
| 09 | [Fork and Pull Request Workflow](experiments/09-fork-pull-request/README.md) |
| 10 | [Git Branching and Merge Conflict](experiments/10-merge-conflict/README.md) |
| 11 | [Static Website with Docker](experiments/11-static-docker/README.md) |
| 12 | [Flask API with Docker and Kubernetes](experiments/12-flask-kubernetes/README.md) |
| 13 | [CI CD using Jenkins](experiments/13-jenkins-pipeline/README.md) |
| 14 | [Continuous Deployment with GitHub Actions](experiments/14-github-actions-docker/README.md) |
| 15 | [GitHub Version Control](experiments/15-version-control/README.md) |
| 16 | [Containerize Flask To Do App](experiments/16-flask-todo/README.md) |
| 17 | [Push and Pull Docker Image](experiments/17-docker-push-pull/README.md) |
| 18 | [Multi Container App with Kubernetes](experiments/18-multi-container-kubernetes/README.md) |
| 19 | [CI CD with GitHub Actions](experiments/19-flask-cicd/README.md) |
| 20 | [Create GitHub Repository](experiments/20-create-repository/README.md) |
| 21 | [Clone and Modify Repository](experiments/21-clone-modify/README.md) |
| 22 | [Commit and Push Changes](experiments/22-commit-push/README.md) |
| 23 | [Pull Latest Changes](experiments/23-pull-changes/README.md) |
| 24 | [Create feature login Branch](experiments/24-feature-login/README.md) |
| 25 | [Fork and Implement Feature](experiments/25-fork-feature/README.md) |

## Records and evidence

- [Combined lab record](docs/LAB_RECORD.md)
- [Requirements workbook](experiments/05-library-moscow/requirements-prioritization.xlsx)
- [Execution status](STATUS.md)
- [Verification evidence](evidence/verification.md)
- [GitHub publication evidence](evidence/github-publication.md)
- [CI and deployment setup](docs/ci-setup.md)
- [Sources and handout corrections](docs/references.md)

Individual experiment READMEs are the canonical instructions. The original uploaded document, real credentials, private survey responses and personal records are not included.
