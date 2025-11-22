.PHONY: doc uml

doc:
	sphinx-build -b html doc/api/source doc/api/source/html
	@echo "Documentation built in: doc/api/source/html"

uml:
	python scripts/uml.py

test:
	python -m unittest discover -s test

coverage:
	python -m coverage report -m
	coverage html
	@echo "Coverage HTML in htmlcov/index.html"

lint:
	flake8 dice
	flake8 test
	pylint dice
	pylint test