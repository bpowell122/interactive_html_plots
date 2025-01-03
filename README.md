# Interactive HTML plots

-----
This repo provides examples on generating interactive plots (e.g. using Plotly), and subsequently interacting with these plots in a static HTML context (such as deploying to GitHub Pages).

## Installation

1. Git clone this repository
2. ``pip install .``

## Generating HTML pages

### Manually

Render the plots as HTML files 

1. ``python src/interactive_html_plots/main.py``

Render the ReST files in the ``docs`` directory as HTML files

2. ``sphinx-build docs/_source docs/_build``

3. View the landing page ``docs/_build/html/index.html`` in a web browser

### Automatically
This repo includes a GitHub Action to automatically perform the above steps, and serves them to https://bpowell122.github.io/interactive-html-plots, any time a new commit is pushed to the main branch.

## License

`interactive-html-plots` is distributed under the terms of the [GPLv3](https://spdx.org/licenses/GPLv3.html) license.
