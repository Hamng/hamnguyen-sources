# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:46:19 2019

@author: Ham
The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4
outer

The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
Task

You are given two arrays:  and . 
Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array . 
The second line contains the space separated elements of array .

Output Format

First, print the inner product. 
Second, print the outer product.

Sample Input

0 1
2 3
Sample Output

3
[[0 0]
 [2 3]]

"""

import numpy

if __name__ == '__main__':
    a = [0, 1]
    b = [2, 3]
    #a = [int(x) for x in input().split()]
    #b = [int(x) for x in input().split()]
    print(numpy.inner(a, b))
    oter = numpy.outer(a, b)
    print(oter)
    #print("[" + str(oter[0]))
    #for e in oter[1:-2]:
    #    print(" " + str(e))
    #print(" " + str(oter[-1]) + "]")
