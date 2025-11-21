# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Assignment_2'
copyright = '2025, Maraizu Dominic-Judes, Uchenna Peter and Michael Agunbiade'
author = 'Maraizu Dominic-Judes, Uchenna Peter and Michael Agunbiade'
release = 'v9.0.0'

# -- Path setup --------------------------------------------------------------
import os
import sys

# Add the project root directory (three levels up) so autodoc can find "package"
sys.path.insert(0, os.path.abspath("../../.."))

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",      # enables .. automodule::
    "sphinx.ext.napoleon",     # Google & NumPy docstring support
    "sphinx.ext.viewcode"      # adds links to highlighted source code
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
