# Verification evidence

The committed logs record what actually ran during package preparation.

| Check | Observed result | Evidence |
| --- | --- | --- |
| Python tests | 15 tests passed, with additional parameterized subcases | [python-tests.log](python-tests.log) |
| Experiment coverage | All 25 directories have their instructions | [asset-validation.log](asset-validation.log) |
| Infrastructure configuration | YAML parsed; deployment selectors, service ports and shell syntax checked | [asset-validation.log](asset-validation.log) |
| Prototype structure | Four bus screens and eight shop screens; all navigation destinations resolve | [asset-validation.log](asset-validation.log) |
| Figma source | Both generator files pass Node JavaScript syntax checks | Source under experiments 02 and 03 |
| Visual review | All 12 SVG screens and all three workbook sheets rendered and inspected | The supplied SVG and XLSX artifacts |
| Workbook formulas | Counts are Library 6/3/2/1, Task 3/2/1/1, Learning 3/1/1/1; editing a category changes the summary | Requirements workbook |
| Git exercise | Actual local clone, commit, push, pull, branch and merge operations completed; real conflict observed and resolved | [git-workflow.log](git-workflow.log), [git-summary.json](git-summary.json) |
| Kanban simulation | Three tasks progressed through the three columns | [kanban-simulation.json](kanban-simulation.json) |
| GitHub upload | All 132 remote blob hashes matched the prepared files | [github-publication.md](github-publication.md) |
| Hosted validation | Test job and eight Docker build-and-HTTP-smoke jobs passed on both the upload and login PR | [github-publication.md](github-publication.md) |
| Feature-login PR | PR #1 passed validation and was squash-merged | [github-publication.md](github-publication.md) |

## Reproduce the executable checks

From the repository root after installing requirements-dev.txt:

```bash
python -m unittest discover -s tests -v
python scripts/validate_assets.py
python scripts/git_lab.py
python scripts/simulate_kanban.py
node --check experiments/02-bus-booking-prototype/figma-plugin/code.js
node --check experiments/03-ecommerce-prototype/figma-plugin/code.js
```

Fresh simulation logs are written to evidence/runtime and are ignored by Git;
the committed logs remain the original observed run. Local temporary paths in
those logs identify disposable test repositories, not live GitHub repositories.

## Limits of the checks

The MySQL success-path test uses a mock. The failure-path test verifies that the
API reports an unavailable database without failing its liveness probe.
Neither proves a live database connection or Kubernetes deployment.

The cloud browser could not reach the local HTML preview. Static navigation and
design rendering were checked; browser-click behavior and execution of the
Figma plugin inside Figma remain unverified.

Docker, kubectl and Jenkins were not available on the preparation machine. GitHub-hosted
runners successfully built and smoke-tested eight isolated images, but did not perform a
Kubernetes rollout, Jenkins run, registry publication or server deployment. Jira,
Confluence, Figma, registry, host and human peer-review evidence still requires actual
access and execution; see [STATUS.md](../STATUS.md).
