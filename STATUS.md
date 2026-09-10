# Execution status

All 25 experiments have implementation assets and records. This table separates completed local work from remaining platform execution. Update it only after observing the result.

| Exp | Prepared or verified here | Remaining literal lab step |
| --- | --- | --- |
| 01 | Task dataset and executed local simulation | Jira/Trello board and screenshots |
| 02 | Four screens, link graph and Figma code syntax | Run in Figma and capture prototype |
| 03 | Eight screens, link graph and feedback form | Run in Figma and collect stakeholder feedback |
| 04 | Five ranked stories and 16 point sprint plan | Execute a real Jira sprint |
| 05 | 12 requirements and recalculating workbook | None for the categorization exercise |
| 06 | Confluence content and JQL | Create live Jira macro and screenshot |
| 07 | Seven proposed MoSCoW/Kano classifications | Import to Jira and capture backlog |
| 08 | Six proposed MoSCoW/Kano classifications | Import to Jira and capture six features |
| 09 | Local fork contribution sequence | GitHub fork PR and real review |
| 10 | Real local conflict resolved and merged | GitHub branch PR evidence |
| 11 | Nginx image built and served successfully in GitHub Actions | Capture the running page if a lab screenshot is required |
| 12 | Endpoint tests, manifest checks, and hosted Docker build/run passed | Kubernetes rollout and endpoint evidence |
| 13 | Jenkinsfile prepared; its image built and served in GitHub Actions | Execute the actual Jenkins pipeline |
| 14 | Hosted tests and Docker build/run passed in GitHub Actions | Docker Hub publication and deployment |
| 15 | Local module branches and merges | GitHub module PRs and peer review |
| 16 | Persistence tests plus hosted Docker build/run passed | Compose restart persistence evidence and registry publication |
| 17 | Image built, served and HTTP-checked in GitHub Actions | Docker Hub push/pull evidence |
| 18 | Three-tier wiring, contract tests, and backend Docker run passed | Live cluster, MySQL persistence and scaling |
| 19 | Hosted tests and Docker build/run passed; publish/deploy workflows prepared | Registry credentials and Linux/EC2 deployment host |
| 20 | Private repository created; all 132 files uploaded and hash-verified | None |
| 21 | Actual local clone and modification | Repeat against GitHub URL if required |
| 22 | Local stage/push simulation plus verified commits on GitHub main | None for commit/push evidence |
| 23 | Second-checkout update pulled and verified | Real collaborator if required |
| 24 | Real feature-login branch, PR #1, passing CI, and squash merge | Human peer review, if required |
| 25 | Feature tests and local fork integration | GitHub fork PR to an agreed original repository |

## Access and runtime state

The private GitHub repository was created and verified on 10 September 2026: [csa10-software-engineering-lab](https://github.com/sandeep-yadav0419/csa10-software-engineering-lab). The uploaded tree contains all 132 prepared files and every remote Git blob hash matched its local source. The [initial validation run](https://github.com/sandeep-yadav0419/csa10-software-engineering-lab/actions/runs/34431767106) passed its Python/asset/Git job and all eight Docker matrix jobs. [Pull request #1](https://github.com/sandeep-yadav0419/csa10-software-engineering-lab/pull/1) also passed the same validation and was squash-merged.

Jira/Confluence and Figma were not connected during preparation. Docker and kubectl are absent from the preparation machine, although Docker builds and isolated HTTP smoke tests ran on GitHub-hosted runners. No Jenkins server, Docker Hub credentials or EC2 host was supplied. The Docker Hub publish job therefore skipped intentionally.

The cloud browser could not open the local prototype URL, so live browser clicks were not verified. Prototype navigation graphs and Figma JavaScript syntax were checked. The generated designs and spreadsheet renders are reviewed separately.

The local fork and second checkout are simulations of collaboration using real Git operations. They are not evidence of an actual GitHub fork, PR or human peer review.
