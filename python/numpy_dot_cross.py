# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:35:32 2019

@author: Ham

HackerRanch Challenge: Dot and Cross

dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11


cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2

Task

You are given two arrays A and B.
Both have dimensions of NxN.
Your task is to compute their matrix product.

Input Format

The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.

Output Format

Print the matrix multiplication of A and B.

Sample Input

2
1 2
3 4
1 2
3 4

Sample Output

[[ 7 10]
 [15 22]]

"""

import numpy

n = int(input().strip())
a = [list(map(int, input().strip().split())) for _ in range(n)]
b = [list(map(int, input().strip().split())) for _ in range(n)]
#print(numpy.array(a))
#print(numpy.array(b))
print(numpy.dot(a, b))
