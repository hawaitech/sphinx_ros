# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

os.environ["SPHINX_APIDOC_OPTIONS"] = "members,show-inheritance"

import sys
from pathlib import Path

sys.path.insert(0, str(Path.resolve(Path("../../src"))))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.apidoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",  # Allow referencing sections by their title
    "sphinx_ros",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


ros_msg_reference_version = "jazzy"

# General information about the project.
project = "ROS Sphinx domain"
copyright = "2025, HawAI.tech"
author = "HawAI.tech"
release = "0.0.1"
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

apidoc_module_dir = "../../src"
apidoc_output_dir = "modules"
apidoc_toc_file = False
apidoc_separate_modules = True

# -- Options for HTML output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo_only": True,
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "./_static/exports/ROSphinx.svg"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or
# 32x32 pixels large.
html_favicon = "./_static/exports/Icon_016x016.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Example configuration for intersphinx: refer to the Python standard library and Sphinx.
intersphinx_mapping = {
    "ptyhon": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

rst_epilog = ""
rst_epilog += "\n.. |ROS| replace:: :abbr:`ROS (Robot Operating System)`"
