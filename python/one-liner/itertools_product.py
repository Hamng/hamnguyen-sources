# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:38:08 2019

@author: Ham

HackerRanch Challenge: Maximize It!

You are given a function f(x) = x^2.
You are also given K lists.
The i-th list consists of Ni elements.

You have to pick one element from each list to maximize the equation below:

    S = (f(x1) + f(x2) + ... + f(xk)) % M

xi denotes the element picked from the i-th list .
Find the maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list,
not necessarily the largest element.
You add the squares of the chosen elements and perform the modulo operation.
The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers K and M.
The next K lines each contains an integer N, denoting the number of elements in the  list,
followed by N space separated integers denoting the elements in the list.

Constraints





Output Format

Output a single integer denoting the value Smax.

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output

206

Explanation

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list
gives the maximum Smax value equal to (5^2 + 9^2 + 10^2) % 1000 = 206.

"""

import itertools

if __name__ == '__main__':
    k, m = map(int, input().strip().split())
    l = [tuple(map(int, input().strip().split()[1:])) for _ in range(k)]
    # listcomp above splits, then discard the 1st int from each line.
    # Each line becomes an inner list, then l is the outer lists of all.
    #print(l)   => [(5, 4), (7, 8, 9), (5, 7, 8, 9, 10)]
    #mx = 0
    #for t in itertools.product(*l):
    #    #print(t)
    #    mx = max(mx, sum([i*i for i in t]) % m)
    # Above was straightforward. Below is mind-boggling
    mx = max([sum([i*i for i in t]) % m for t in itertools.product(*l)])
    print(mx)
