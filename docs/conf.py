"""Sphinx configuration."""

import os
import sys
from datetime import datetime

# Add the project root directory to the path so that autodoc can find the modules
sys.path.insert(0, os.path.abspath(".."))

# Project information
project = "Pixi Project"
author = "eLearning Hub"
copyright = f"{datetime.now().year}, {author}"
release = "0.1.0"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_click",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The theme to use for HTML and HTML Help pages.
html_theme = "furo"
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "color-brand-primary": "#336790",
        "color-brand-content": "#336790",
    },
    "dark_css_variables": {
        "color-brand-primary": "#6DA4D2",
        "color-brand-content": "#6DA4D2",
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# MyST configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3
