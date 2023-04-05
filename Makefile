setup: install build publish package-install

install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

cov-report:
	poetry run pytest --cov=gendiff --cov-report=xml

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