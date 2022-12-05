#!/usr/bin/env just --justfile

set dotenv-load := true
set positional-arguments := true

install:
    poetry install
    poetry run pre-commit install

test +args:
    poetry run pytest "$@"
test-cov: (test "--cov=aoc")
test-cov-report: (test "--cov=aoc --cov-report=xml")

cq:
    poetry run pre-commit run --all
