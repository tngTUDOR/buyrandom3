"""Sphinx configuration."""
import importlib.metadata

project = "buyrandom3"
author = "Tomás NAVARRETE GUTIÉRREZ"
copyright = "2022, Tomás NAVARRETE GUTIÉRREZ"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"

needs_sphinx = '5.0'

version = importlib.metadata.version("buyrandom3")
