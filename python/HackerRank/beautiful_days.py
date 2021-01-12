# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:59:28 2020

@author: Ham

HackerRank > Practice > Algorithms > Implementation
Beautiful Days at the Movies

Problem
Lily likes to play games with integers.
She has created a new game where she determines the difference between
a number and its reverse.
For instance, given the number 12, its reverse is 21. Their difference is 9.
The number 120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making.
She will look at a numbered range of days
and will only go to a movie on a beautiful day.

Given a range of numbered days, [i ... j] and a number k,
determine the number of days in the range that are beautiful.
Beautiful numbers are defined as numbers
where |i - reverse(i)| is evenly divisible by k.
If a day's value is a beautiful number, it is a beautiful day.
Print the number of beautiful days in the range.

Function Description

Complete the beautifulDays function in the editor below.
It must return the number of beautiful days in the range.

beautifulDays has the following parameter(s):

i: the starting day number
j: the ending day number
k: the divisor
Input Format

A single line of three space-separated integers
describing the respective values of i, j, and k.

Constraints

Output Format

Print the number of beautiful days in the inclusive range between i and j.

Sample Input

20 23 6
Sample Output

2
Explanation

Lily may go to the movies on days 20, 21, 22, and 23.
We perform the following calculations to determine which days are beautiful:

Day 20 is beautiful because the following evaluates to a whole number:
Day 21 is not beautiful because the following doesn't evaluate to a whole number:
Day 22 is beautiful because the following evaluates to a whole number:
Day 23 is not beautiful because the following doesn't evaluate to a whole number:

Only two days, 20 and 22, in this interval are beautiful.
Thus, we print 2 as our answer.


"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

import io

# Test case 6: Expected Output: 9657
STDIN_SIO = io.StringIO("""
1 123456 13
""".strip())


def backward(i):
    res = 0
    while i != 0:
        res = res*10 + (i % 10)
        i //= 10
    return res

def divisible(i, k):
    return abs(i - backward(i)) % k == 0

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    return len([True for e in range(i, j + 1) if divisible(e, k)])

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ijk = input().split()
    ijk = STDIN_SIO.readline().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
