# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 01:26:12 2020

@author: Ham

HackerRank > Practice > Interview Preparation Kit > Warm-up Challenges
Sales by Match

Problem
Alex works at a clothing store. There is a large pile of socks that must be
paired by color for sale.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2].
There is one pair of color 1 and one of color 2.
There are three odd socks left, one of each color. The number of pairs is 2.

Function Description

Complete the sockMerchant function in the editor below.
It must return an integer representing
the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer n, the number of socks represented in ar[].
The second line contains n space-separated integers
describing the colors ar[i] of the socks in the pile.

Constraints

 where

Output Format

Return the total number of matching pairs of socks that Alex can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20

Sample Output

3

Explanation


Alex can match three pairs of socks.

"""

#!/bin/python

#import math
import os
#import random
#import re
#import sys
#import itertools

import io

STDIN_SIO = io.StringIO("""
100
50 49 38 49 78 36 25 96 10 67 \
78 58 98 8 53 1 4 7 29 6 \
59 93 74 3 67 47 12 85 84 40 \
81 85 89 70 33 66 6 9 13 67 \
75 42 24 73 49 28 25 5 86 53 \
10 44 45 35 47 11 81 10 47 16 \
49 79 52 89 100 36 6 57 96 18 \
23 71 11 99 95 12 78 19 16 64 \
23 77 7 19 11 5 81 43 14 27 \
11 63 57 62 3 56 50 9 13 45
""".strip())

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #print(ar)
    m = 0
    for i,v in enumerate(ar):
        if v is None:
            continue
        try:
            found = ar.index(v, i+1)
            # if not found, will jump to the 'except' section
            m += 1
            #print('match #', m, '[', i, ']=', v, '== [', found, ']=', ar[found])
            ar[found] = None
        except:
            # jump here if not found
            pass
    return m

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    #ar = map(int, input().rstrip().split())

    n = int(STDIN_SIO.readline().strip())
    ar = list(map(int, STDIN_SIO.readline().rstrip().split()))
    #print(n, ar)

    result = sockMerchant(n, ar)

    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
