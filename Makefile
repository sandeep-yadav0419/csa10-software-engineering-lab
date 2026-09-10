.PHONY: setup test git-lab check serve
PYTHON ?= python3
setup:
	$(PYTHON) -m venv .venv
	.venv/bin/python -m pip install -r requirements-dev.txt
test:
	.venv/bin/python -m unittest discover -s tests -v
git-lab:
	$(PYTHON) scripts/git_lab.py
check:
	.venv/bin/python scripts/validate_assets.py
serve:
	$(PYTHON) -m http.server 8090 --bind 127.0.0.1
