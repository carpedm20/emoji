# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

import emoji as emoji_pkg
project = 'emoji'
copyright = emoji_pkg.__source__
author = emoji_pkg.__author__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = emoji_pkg.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

html_baseurl = 'https://carpedm20.github.io/emoji/docs/'

html_theme_options = {
    'page_width': '1200px',
    'github_user': 'carpedm20',
    'github_repo': 'emoji',
    'github_banner': False,
    'show_related': False,
    'canonical_url': 'https://carpedm20.github.io/emoji/docs/',
    'extra_nav_links': {
        'GitHub repository': 'https://github.com/carpedm20/emoji',
        'emoji on PyPI': 'https://pypi.org/project/emoji/',
        'All supported emoji': 'https://carpedm20.github.io/emoji/',
        'All emoji on unicode.org': 'http://www.unicode.org/emoji/charts/full-emoji-list.html',
        'Unicode Standard': 'http://www.unicode.org/reports/tr51/',
    }
}