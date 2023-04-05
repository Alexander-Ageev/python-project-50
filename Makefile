setup: install build publish package-install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-cov:
	poetry run pytest

test-report:
	poetry run pytest --cov=gendiff --cov-report=xml

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install