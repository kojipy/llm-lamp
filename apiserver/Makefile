
PYTHON := .venv/bin/python

.PHONY: install*
install/poetry:
	curl -sSL https://install.python-poetry.org | python3 - --version 1.7

.PHONY: setup
setup:
	poetry install


.PHONY: run
run:
	poetry run uvicorn src.main:app --reload