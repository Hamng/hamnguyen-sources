# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 10:21:58 2021

@author: Ham

HackerRank > Practice > Data Structures > Arrays
2D Array - DS

Given a 6x6 2D Array, arr[][]:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in arr[][] is a subset of values with indices
falling in this pattern in arr[][]'s graphical representation:

a b c
  d
e f g

There are 6 hourglasses in arr[][].
An hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in arr[][],
then print the maximum hourglass sum.
The array will always be 6x6.

Example


-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

The  hourglass sums are:

-63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18

The highest hourglass sum is 28
from the hourglass beginning at row 1, column 2:

0 4 3
  1
8 6 6

Note: If you have already solved the Java domain's Java 2D Array challenge,
you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers
Returns

int: the maximum hourglass sum
Input Format

Each of the 6 lines of inputs arr[i]
contains 6 space-separated integers arr[i][j].

Constraints

Output Format

Print the largest (maximum) hourglass sum found in arr[][].

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

arr[][] contains the following hourglasses:

image

The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

import io

# Test case 6: expected=25
STDIN_SIO = io.StringIO("""
0 6 -7 1 6 3
-8 2 8 3 -2 7
-3 3 -6 -3 0 -6
5 0 5 -1 -5 2
6 2 8 1 3 0
8 5 0 4 -7 4

Test case 0, expected=19
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Test case 1, expected=13
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 9 2 -4 -4 0
0 0 0 -2 0 0
0 0 -1 -2 -4 0

Test case 8, expected=28
-9 -9 -9 1 1 1
0 -9 0 4 3 2
-9 -9 -9 1 2 3
0 0 8 6 6 0
0 0 0 -2 0 0
0 0 1 2 4 0
""".strip())


def sumHourglassAt(arr: list, row: int, col: int):
    sm = sum([arr[row+i][col+j] for i in range(3) for j in range(3)]) - arr[row+1][col] - arr[row+1][col+2]
    #print('[', row, ',', col,']=', arr[row][col], ', sum=', sm)
    return sm

# Complete the hourglassSum function below.
def hourglassSum(arr):
    mx = -99999
    for row in range(len(arr)-2):
        #print(arr[row:row+3])
        for col in range(len(arr[0])-2):
            sm = sumHourglassAt(arr, row, col)
            if sm > mx:
                mx = sm
    return mx


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        #arr.append(list(map(int, input().rstrip().split())))
        arr.append(list(map(int, STDIN_SIO.readline().rstrip().split())))

    result = hourglassSum(arr)

    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
