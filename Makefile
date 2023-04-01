setup: install build publish package-install

lint:
	poetry run flake8 gendiff

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install