# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:49:33 2019

@author: Ham

Below is a 1-liner to reverse lines read from stdin.
VERY IMPORTANT on Windows: **MUST** use double-quotations to quote the Python codes

You can feed stdin from many files as: cat f1 f2 f3 | line_reversal
Or, you can have another 1-liner to generate input lines:

python -c "[print(i,i,i) for i in range(1,20)]" | line_reversal

"""

python -c "import sys; [print(l,end='') for l in sys.stdin.readlines()[::-1]]"