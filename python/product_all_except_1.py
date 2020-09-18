# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:27:33 2020

@author: Ham

Facebook Interview Question #1: Product of all except 1

Given an array of N numbers, return an output array, for each index i, the element in output array is product of all numbers except the one at index i

example: [1,5,6,2]
output:[5*6*2, 1*6*2, 1*5*2, 1*5*6] -> [60, 12, 10, 30]

    
    left:[1,1,5, 30]
    right:[60,12,2,1]
            
    output array:[60, 12, 10, 30]

"""

import itertools
import functools

def product_i(arr, pos):
    #prod = 1
    #lft = arr[:pos]
    #for v in lft:
    #    prod *= v
    #rgt = arr[pos+1:]
    #for v in rgt:
    #    prod *= v
    #print('prod:', prod, 'left:', lft, 'right:', rgt)
    #return prod
    return functools.reduce(lambda x, y: x*y,
                            itertools.chain(arr[:pos], arr[pos+1:]),
                            1)

def product_array(arr):
    # Order of complexity: O(N*(N-1)) = O(N^2)
    return [product_i(arr, pos) for pos in range(len(arr))]
    #print(res)
    #return res


def product_all_but_1(arr):
    # Order of complexity: O(3*N) = O(N)
    # from left, cumulative product of all elements except the last one
    # i.e. [1, a0, a0*a1, a0*a1*a2, ...,
    #       a0*...a[-5], a0*...a[-4], a0*...a[-3], a0*...a[-2]]
    lft = [1]
    [lft.append(lft[-1] * v) for v in arr[:len(arr)-1]]
    #print('left:', lft)

    # Similarly, from right, cumulative product of all elems except 1st
    #  [a1*...a[-1], a2*...a[-1], a3*...a[-1], a4*...a[-1], ...,
    #   a[-3]*a[-2]*a[-1], a[-2]*a[-1], a[-1], 1]
    rgt = [1]
    [rgt.insert(0, rgt[0] * v) for v in arr[-1:0:-1]]
    #print('Right:', rgt)
    return [l*r for l, r in zip(lft, rgt)]


def mult_all_div_1(arr):
    # Order of complexity: O(2*N) = O(N)
    # Limitations: not yet handle 0 element(s)
    # Even if all elems are ints, results won't be ints
    # First, calculate the product of all elements
    prod = functools.reduce(lambda x, y: x*y, arr, 1)
    return [prod//v for v in arr]


if __name__ == "__main__":
    print(product_array([1, 5, 6, 2, 9]))
    print(product_all_but_1([1, 5, 6, 2, 9]))
    print(mult_all_div_1([1, 5, 6, 2, 9]))
