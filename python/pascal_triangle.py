# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 07:01:01 2019

@author: Ham

Generate the N-th row of a Pascal triangle

"""

import array

def pascal_triangle_row(n):
    "doc"
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    if n == 2:
        return [1, 2, 1]
    if n == 3:
        return [1, 3, 3, 1]
    prev = pascal_triangle_row(n - 1)
    return [1, n] + [prev[i - 1] + prev[i] for i in range(2, n - 1)] + [n, 1]

def pascal_inplace(a, n):
    "doc"
    a[0] = 1
    if n == 0:
        return a
    a[n] = 1
    if n == 1:
        return a
    a[1] = n
    if n == 2:
        return a
    pascal_inplace(a, n - 1)        # would set a[n-1] to 1
    #print(list(a)[:n], n - 1)
    a[n - 1] = n                    # so need to set it to n now
    #print(list(a), n - 1)
    previous = a[0]
    for i in range(1, n - 1):
        current = a[i]
        a[i] += previous
        previous = current
    return a

if __name__ == '__main__':
    n = int(input().strip())
    #print(pascal_triangle_row(n))

    a = array.array('i', [-2] * (n + 1))
    #print(list(pascal_inplace(a, n)))
    for i in range(n + 1):
        print("  " * (n - i), list(pascal_inplace(a, i))[:i+1])
