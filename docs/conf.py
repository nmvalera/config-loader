"""
    docs.conf.py
    ~~~~~~~~~~~~

    Cfg-Loader documentation build configuration file

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
from datetime import datetime

import cfg_loader

sys.path.insert(0, os.path.abspath('..'))

BUILD_DATE = datetime.utcnow()

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sqlalchemy': ('https://docs.sqlalchemy.org/en/latest/', None),
    'marshmallow': ('https://marshmallow.readthedocs.io/en/latest/', None)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source file names.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
PROJECT_NAME = 'Cfg-Loader'
AUTHOR = 'ConsenSys France'

project = PROJECT_NAME
author = AUTHOR
copyright = '{0}, ConsenSys France'.format(BUILD_DATE.year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

version = release = cfg_loader.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'venv',
    '*.egg-info',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ],
}
