import sys, os

sys.path.append(os.path.abspath('../src'))

# The suffix of source filenames.
source_suffix = '.txt'

# The master toctree document.
master_doc = 'index'
exclude_trees = ['pyenv', 'tmp', 'out', 'parts', 'clients', 'eggs']
extensions = ['crate.sphinx.csv']
