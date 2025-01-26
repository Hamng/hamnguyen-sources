# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:07:08 2020

@author: Ham

A sample one-liner to do a listop on the 1st line of stdin

"""

echo 3 4 5 | python -c "import sys; print(sum(map(int, input().split())))"
