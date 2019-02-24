# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 20:58:30 2019

@author: Ham

HackerRanch Challenge: itertools.product()

Task

You are given a two lists A and B.
Your task is to compute their cartesian product X.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note: A and B are sorted lists, and the cartesian product's tuples
should be output in sorted order.

Input Format

The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

Constraints



Output Format

Output the space separated tuples of the cartesian product.

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
 
 """

import itertools

if __name__ == '__main__':
    #a = [int(x) for x in input().split()]
    #b = [int(x) for x in input().split()]

    a = [1, 2]
    b = [3, 4]

    #print(a, b)
    [print(tup, end=" ") for tup in sorted(itertools.product(a, b))]
