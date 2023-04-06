setup: install build publish

install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

cov-html:
	poetry run pytest --cov=gendiff --cov-report html:report

cov-report:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build