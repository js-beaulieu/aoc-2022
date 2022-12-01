.PHONY: install
install:
	poetry install
	poetry run pre-commit install

.PHONY: test
test:
	poetry run pytest

.PHONY: test-cov
test-cov:
	poetry run pytest --cov=aoc

.PHONY: cq
cq:
	poetry run pre-commit run --all
