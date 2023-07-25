setup: install build publish

install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

cov-report:
	poetry run pytest --cov=gendiff --cov-report xml

check:
	poetry check
	poetry run pytest --cov=gendiff --cov-report xml
	poetry run flake8 gendiff

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build