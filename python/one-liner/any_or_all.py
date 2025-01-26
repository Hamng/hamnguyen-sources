# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:57:47 2019

@author: Ham

HackerRanch Challenge: Any or All

Task

You are given a space separated list of integers.
If all the integers are positive,
then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer N.
N is the total number of integers in the list.
The second line contains the space separated list of  integers.

Constraints


Output Format

Print True if all the conditions of the problem statement are satisfied.
Otherwise, print False.

Sample Input

5
12 9 61 5 14

Sample Output

True

Explanation

Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.

Hence, the output is True.

Can you solve this challenge in 3 lines of code or less?
There is no penalty for solutions that are correct but have more than 3 lines.

"""

stdin_sim = """
5
12 9 61 5 14
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    stdin_sim.pop(0)                # discarded, don't need number of ints
    arr = stdin_sim.pop(0).split()
    #input()
    #arr = input().split()
    print(arr)
    print([int(e) > 0 for e in arr])
    print(all([int(e) > 0 for e in arr]))
    print([e == e[::-1] for e in arr])
    print(any([e == e[::-1] for e in arr]))
    # To keep this program 3 lines or less
    print(all([int(e) > 0 for e in arr]) and any([e == e[::-1] for e in arr]))
