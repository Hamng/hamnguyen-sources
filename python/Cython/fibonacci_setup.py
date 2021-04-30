# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:57:35 2021

@author: Ham
Copied from Cython: setup script for fibonacci.pyx
To run:
    python fibonacci_setup.py build_ext --inplace

"""

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fibonacci.pyx",
                          compiler_directives={'language_level' : "3"}),
)