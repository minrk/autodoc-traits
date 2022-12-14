import os
import sys

project = "autodoc_traits tests"
extensions = [
    "autodoc_traits",
    # sphinx.ext.napoleon is added to avoid warnings if testing with :inherited-members:`
    # where the traitlets base classes members has numpy or google-format docstrings
    "sphinx.ext.napoleon",
]

# ensure sample_module.py is on path
tests_dir = os.path.join(os.path.dirname(__file__), "..")
tests_dir = os.path.abspath(tests_dir)
sys.path.insert(0, tests_dir)

# Don't parse .rst documents expected to raise an error unless we want to test
# that specifically.
exclude_patterns = ["**/*_raises_error.rst"]
