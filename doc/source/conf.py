import io
import os
import sys
sys.path.insert(0, os.path.abspath('./_ext'))

version = None
with io.open('../../sphinx_codefence.py', encoding='utf-8') as infile:
  for line in infile:
    line = line.strip()
    if line.startswith('VERSION ='):
      version = line.split('=', 1)[1].strip().strip('"')
assert version is not None

project = 'sphinx-codefence'
copyright = '2019, Josh Bialkowski'
author = 'Josh Bialkowski'
extensions = [
  "sphinx_codefence"
]

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
master_doc = "index"
