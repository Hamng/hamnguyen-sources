#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:59:16 2025

Source: Google AI on "python multiprocessing pool map examples"

"""

import multiprocessing
import time
import itertools

def square(x):
    """Calculates the square of a number."""
    time.sleep(1)  # Simulate some work
    return x * x

#def multiply(*args):
def multiply(arg1, arg2):
    """Multiplies two numbers."""
    #print(f"type(arg2)={type(arg2)}, arg1={arg1}, arg2={arg2}")
    #print(f"args of len {len(args)}={args}, type(args[0])={type(args[0])}")
    time.sleep(1)
    #if len(args) < 2:
    #    args = tuple(args[0])
    #return args[0] * args[1]
    #return args[0] * args[1]
    #return (arg1[0] * arg1[1]) if arg2 == None else (
    return arg1 * arg2

def multiply_tuple(x):
    return multiply(*x)

if __name__ == '__main__':
    # Example 1: Simple squaring of numbers
    with multiprocessing.Pool(processes=4) as pool:
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)
        print(f"Numbers: {numbers}\nSquares: {results}")
    
    # Example 2: Using starmap for multiple arguments
    with multiprocessing.Pool(processes=2) as pool:
        pairs = [(1, 5), (2, 6), (3, 7)]
        results_mult = pool.starmap(multiply, pairs)
        results_pow = pool.starmap(pow, pairs)
        print(f"\nPairs: {pairs}\nProducts (starmap): {results_mult}\nPowers (starmap): {results_pow}")

    # Example 3: Using map with a single iterable of tuples
    with multiprocessing.Pool(processes=2) as pool:
        pairs = [(3, 7), (2, 6), (1, 5)]
        #results_mult2 = pool.map(multiply, pairs)
        results_mult2 = pool.map(multiply_tuple, pairs)
        print(f"\nPairs: {pairs}\nProducts (map): {results_mult2}")
