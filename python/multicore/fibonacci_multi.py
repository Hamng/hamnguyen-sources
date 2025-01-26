#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:59:16 2025

Source: Google AI on "python multiprocessing recursive"

"""

import multiprocessing
#from tqdm import tqdm

def fibonacci(n):
    if n <= 1:
        return n
    else:
        with multiprocessing.Pool() as pool:
            results = pool.map(fibonacci, [n-1, n-2])
        return sum(results)

if __name__ == "__main__":
    n = 3
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")
