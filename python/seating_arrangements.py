# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:29:51 2020

@author: Ham

Facebook Coding Exercises: [Greedy Algorithms] Seating Arrangements

There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible overall awkwardness of any seating arrangement.
Signature
int minOverallAwkwardness(int[] arr)
Input
n is in the range [3, 1000].
Each height arr[i] is in the range [1, 1000].
Output
Return the minimum achievable overall awkwardness of any seating arrangement.
Example
n = 4
arr = [5, 10, 6, 8]
output = 4
If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table (having heights [6, 5, 8, 10], in that order), then the four awkwardnesses between pairs of adjacent guests will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4, yielding an overall awkwardness of 4. It's impossible to achieve a smaller overall awkwardness.

Solution:
    [Unsure]
    Sort the heights
    The answer is probably the highest subtracted by the median-highest.
    So after sorting the heights in descending order: arr[0] - arr[n/2]
    NOT working for sample case [14, 13, 10, 6]

"""

#import math
# Add any extra import statements you may need here
import itertools
import random

# Add any helper functions you may need here


def minOverallAwkwardness(arr):
  # Write your code here
  arr.sort(reverse=True)
  print(len(arr), arr)
  return arr[0] - arr[(len(arr) + 1) // 2]


def exhaustive_minOverallAwkwardness(arr):
    n = len(arr)
    #print(n, arr)
    minAwk = 100000
    for p in itertools.permutations(arr):
        maxAwk = max([abs(p[i]-p[i+1]) for i in range(n-1)]+ [abs(p[0]-p[-1])])
        print(p, maxAwk)
        if maxAwk < minAwk:
            minAwk = maxAwk
    print(minAwk, n, arr)
    return minAwk
    #return min([max([abs(p[i]-p[i+1]) for i in range(n-1)] + [abs(p[0]-p[-1])])
    #            for p in itertools.permutations(arr)])







# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 10, 6, 8]
  #expected_1 = 4
  expected_1 = exhaustive_minOverallAwkwardness(arr_1)
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  #expected_2 = 4
  expected_2 = exhaustive_minOverallAwkwardness(arr_2)
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  random.seed()
  #arr_3 = random.sample(range(1, 18), 4)
  #arr_3 = [17, 12, 7, 3]
  arr_3 = [14, 13, 10, 6]
  expected_3 = exhaustive_minOverallAwkwardness(arr_3)
  output_3 = minOverallAwkwardness(arr_3)
  check(expected_3, output_3)
