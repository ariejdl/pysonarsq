
import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pysonarsq",
    version = "0.1.0",
    author = "Arie Lakeman",
    description = ("a port of the project PySonar2 from Java to Python"),
    license = "same as PySonar2 license",
    keywords = "python static analyzer analyser java",
    packages=['pysonarsq', 'tests'],
    long_description=read('README.md'),
)