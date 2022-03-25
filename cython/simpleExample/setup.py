"""
A simple setup file for compiling cython code.

Call with "python setup.py build_ext --inplace"

"""

from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize("simple_example.pyx"),
    compiler_directives={"language_level": "3"},
    zip_safe=False,
)
