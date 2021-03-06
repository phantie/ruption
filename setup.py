"""Build with
   > py setup.py sdist"""

from setuptools import setup, find_packages
from os.path import join, dirname
from ruption import __version__

setup(
    author = 'phantie',
    name = 'ruption',
    version = '.'.join(str(_) for _ in __version__),
    packages = find_packages(),
    long_description = open(join(dirname(__file__), 'README.md')).read(),
)