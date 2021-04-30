# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:53:19 2021

@author: Ham
Copied from Cython to generate Fibonacci series

To use, on (IPython) console:
    1. cd dir containing this fibonacci.pyx, and its supporting fibonacci_setup.py
    2. python fibonacci_setup.py build_ext --inplace
    3. import fibonacci
    4. fibonacci.fib(20000)

"""

def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

    print()
