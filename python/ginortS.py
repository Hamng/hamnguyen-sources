# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:23:31 2019

@author: Ham

HackerRanch Challenge: ginortS

Task

You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string S.

Constraints

Output Format

Output the sorted string S.

Sample Input

Sorting1234

Sample Output

ginortS1324

"""

import string

if __name__ == '__main__':
    s = input()
    lower = sorted([e for e in s if e in string.ascii_lowercase])
    #print(lower)
    upper = sorted([e for e in s if e in string.ascii_uppercase])
    #print(upper)
    odd = sorted([e for e in s if e.isdigit() and (int(e) & 1)])
    #print(odd)
    even = sorted([e for e in s if e.isdigit() and int(e) & 1 == 0])
    #print(even)
    print("".join(lower + upper + odd + even))
