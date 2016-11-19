#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = False
napoleon_use_rtype = False


# General
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'

# Information
project = 'ChessChallenge'
copyright = 'MIT License'
author = 'Roberto Antonio Becerra García'

version = '0.2'
release = '0.2.0'

# Docs
language = 'en'
exclude_patterns = []

add_function_parentheses = True
add_module_names = True
show_authors = False

# HTML Output
pygments_style = 'sphinx'
html_theme = 'haiku'
todo_include_todos = False

html_static_path = ['_static']
html_search_language = 'en'

htmlhelp_basename = 'ChessChallengedoc'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
