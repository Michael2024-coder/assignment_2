.PHONY: doc uml

doc:
	sphinx-build -b html doc/api/source doc/api/source/html
	@echo "Documentation built in: doc/api/source/html"

uml:
	python scripts/uml.py
