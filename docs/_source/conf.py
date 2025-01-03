import os
import sys

sys.path.insert(0, os.path.abspath('../../../'))  # Project root relative to this file

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'interactive_html_plots'
copyright = '2024, Barrett M Powell'
author = 'Barrett M Powell'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# significant gratitude to https://github.com/sphinx-doc/sphinx/issues/7912
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    'navigation_with_keys': False,
    'logo': {
        'text': f'Interactive HTML Plots v{release}',  # set the logo display text at top left of navigation bar
    },
}
html_sidebars = {
  "**": []  # remove the "Section Navigation" left-side sidebar in all pages
}
