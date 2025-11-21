@echo off
REM === Windows Make Replacement ===

if "%1"=="doc" goto build_doc
if "%1"=="uml" goto build_uml

echo Usage:
echo   make doc    - Build Sphinx HTML docs
echo   make uml    - Generate UML diagrams
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
