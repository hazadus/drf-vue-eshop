lint:
	python -m flake8 .
	python -m isort --check-only --profile black .
	python -m black . --check
test:
	python -m manage test
coverage:
	interrogate -vv .
format:
	python -m isort --profile black .
	python -m black .
run:
	make format
	make lint
	make test
	make coverage
	python -m manage runserver
