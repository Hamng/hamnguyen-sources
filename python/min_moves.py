# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:50:01 2020

@author: Ham

"""

def move1(i1, i2):
    res = 0
    while i1+i2 != 0:
        i1, r1 = divmod(i1, 10)
        i2, r2 = divmod(i2, 10)
        res += abs(r1 - r2)
    return res

def minimumMoves(arr1, arr2):
    print('arr1[]:', arr1)
    print('arr2[]:', arr2)
    return sum([move1(i1, i2) for i1,i2 in zip(arr1, arr2)])

if __name__ == "__main__":
    print(minimumMoves([123, 543], [321, 279]))