setup: install build publish

install:
	poetry install

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests/test_gendiff.py

test:
	poetry run pytest

cov-report:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck lint

selfcheck:
	poetry check

publish-cov: check
	poetry run pytest --cov=gendiff --cov-report xml

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build
