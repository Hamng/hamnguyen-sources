# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 08:59:36 2020

@author: Ham

A sample one-liner to do a listop on a list of command-line args

"""

python -c "import sys; print(sum(map(int, sys.argv[1:])))" 3 4 5