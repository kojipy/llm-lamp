
PYTHON := .venv/bin/python

.PHONY: install*
install/poetry:
	curl -sSL https://install.python-poetry.org | python3 - --version 1.7.1

.PHONY: setup
setup:
	poetry install

.PHONY: build
build:
	docker build -t apiserver .

.PHONY: run*
run/docker:
	docker run --rm -p 127.0.0.1:8080:8080 apiserver

.PHONY: run
run:
	poetry run uvicorn src.main:app --reload