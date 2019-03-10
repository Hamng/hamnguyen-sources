# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:24:17 2019

@author: Ham

HackerRanch Challenge: Input()

input()
In Python 2, the expression input() is equivalent to eval(raw_input(prompt)).

Code

>>> input()
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'

Task

You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) == k.

Constraints
All coefficients of polynomial P are integers.
x and k are also integers.

Input Format

The first line contains the space separated values of x and k.
The second line contains the polynomial P.

Output Format

Print True if P(x) == k. Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1

Sample Output

True

Explanation

P(1) = 1^3 + 1*2 + 1 + 1 = 4 == k

Hence, the output is True.

"""

if __name__ == '__main__':
    x, k = map(int, input().strip().split())
    #print(x, k)
    print(k == eval(input()))
