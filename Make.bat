@echo off
REM === Windows Make Replacement ===

if "%1"=="doc" goto build_doc
if "%1"=="uml" goto build_uml
if "%1"=="test" goto build_test
if "%1"=="coverage" goto build_coverage
if "%1"=="lint" goto build_lint

echo Usage:
echo   make doc    - Build Sphinx HTML docs
echo   make uml    - Generate UML diagrams
echo   make test       - Run unit tests
echo   make coverage   - Run coverage + HTML report
echo   make lint       - Run flake8 linting
exit /b 0



:build_doc
echo Building Sphinx documentation...
sphinx-build -b html doc/api/source doc/api/source/html
echo Documentation built in: doc/api/source/html
exit /b 0


:build_uml
echo Generating UML diagrams...
python scripts/uml.py
exit /b 0

:build_test
echo Running tests...
python -m unittest discover -s test
exit /b 0


:build_coverage
echo Running coverage...
python -m coverage report -m
coverage html
echo Coverage report saved to htmlcov/index.html
exit /b 0


:build_lint
echo Running flake8...
flake8 dice
flake8 test
pylint dice
pylint test
exit /b 0
