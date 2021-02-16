# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:52:52 2021

@author: Ham

HackerRank > Practice > Algorithms > Recursion
The Power Sum

Problem
Find the number of ways that a given integer, X,
can be expressed as the sum of the N-th powers of unique, natural numbers.

For example, if X=13 and N=2,
we have to find all combinations of unique squares adding up to 13.
The only solution is 2^2 + 3^2.

Function Description

Complete the powerSum function in the editor below.
It should return an integer that represents the number of possible combinations.

powerSum has the following parameter(s):

X: the integer to sum to
N: the integer power to raise numbers to
Input Format

The first line contains an integer X.
The second line contains an integer N.

Constraints

Output Format

Output a single integer, the number of possible combinations caclulated.

Sample Input 0

10
2
Sample Output 0

1
Explanation 0

If X=10 and N=2, we need to find the number of ways
that 10 can be represented as the sum of squares of unique numbers.

10 = 1^2 + 3^2
This is the only way in which 10 can be expressed as the sum of unique squares.

Sample Input 1

100
2
Sample Output 1

3
Explanation 1

100 = 10^2 = 6^2 + 8^2 = 1^2 + 3^2 + 4^2 + 5^2 + 7^2

Sample Input 2

100
3
Sample Output 2

1
Explanation 2

100 can be expressed as the sum of the cubes of 1, 2, 3, 4.
(1^3 + 2^3 + 3^3 + 4^3 = 100).
There is no other way to express 100 as the sum of cubes.

"""

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

import io

# 3rd line == expected result
STDIN_SIO = io.StringIO("""
49
2
2 = 7^2 = 6^2 + 3^2 + 2^2
8
3
1 = 2^3
400
2
55 Testcase #5
100
3
1
100
2
3
10
2
1
800
2
561 Testcase #3
""".strip())


def countCombosSumEqual(sm: int, nums: list) -> int:
    """
    Count all possible combos of elements in nums[] such that sum(combo) == sm

    Args:
        sm (int): the sum to match.
        nums (list): list of positive integers.

    Returns:
        int: resulting count.

    If nums[0] == sm, start with count=1, then pop nums[0]
    For r from 2 to len(nums), iterate thru all combos C(len(nums), r),
    then count all such that sum(combo) == sm
    """
    count = 0
    if nums[0] == sm:
        count += 1
        nums.pop(0)
    return count + len([1 for r in range(2, len(nums) + 1)
                        for combo in itertools.combinations(nums, r)
                        if sum(combo) == sm])

# Complete the powerSum function below.
def powerSum(X: int, N: int) -> int:
    # Starting from i=1, generate a list of i^N in ascending order
    # [2^N, 3^N, ..., (M-1)^N, M^N] such that the last nums[-1]=M^N <= X
    # Reverse nums[] to be in descending order, then append [1]
    nums = []
    i = 1
    while True:
        i += 1
        v = i ** N
        if v > X:
            break
        nums.append(v)
    nums.reverse()
    nums += [1]
    #nums = list(range(int(X ** (1.0/N)), 0, -1))
    #nums = [y for v in nums[:-1] if (y := v ** N) <= X] + [1]
    #print(X, len(nums), nums)

    # Iterate thru all except the last elements.
    # If an element nums[i] == X, increment count by 1
    # else, discounting nums[i], count all combos of sublist nums[i+1:]
    # such that sum(combo) == X - nums[i].
    # Shorten the sublist further by eliminating nums[j] > (X - nums[i])
    count = 0
    for i, v in enumerate(nums[:-1]):
        if v == X:
            delta = 1
        else:
            delta = countCombosSumEqual(X - v,
                                        [e for e in nums[i+1:] if e <= X - v])
        count += delta

    return count


def wrong_powerSum(X, N, seq=None):
    if X < 1 or N < 0:
        return 0

    if not N:
        # only 1 way X == sum(1^0 + 2^0 + 3^0 + ... X^0)
        return 1

    if seq is None:
        seq = list(range(int(X ** (1.0/N)), 0, -1))

    term0 = int(seq[0] ** N)

    if len(seq) == 1:
        return term0 == X

    if term0 == X:
        return 1 + powerSum(X, N, seq[1:])
    else:
        count = 0
        for i in range(0, len(seq)):
            seq_new = list(seq)
            term0 = int(seq_new.pop(i) ** N)
            count += powerSum(X, N, seq_new)
            if X != term0:
                count += powerSum(X - term0, N, seq_new)
        return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #X = int(input())
    #N = int(input())

    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break

        X = int(line)
        N = int(STDIN_SIO.readline())

        result = powerSum(X, N)

        expected = int(STDIN_SIO.readline().split()[0])

        print("sum="+str(X), "power="+str(N), "combos="+str(result),
              "" if result == expected else (" != expected=" + str(expected)))

        #break

    #fptr.write(str(result) + '\n')
    #fptr.close()
