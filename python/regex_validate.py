# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:40:19 2019

@author: Ham

HackerRanch Challenge: Invalid Regex

You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format

The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+

Sample Output

True
False

Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.

"""

#import sys
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        pattern = input()
        #print("pattern='" + pattern + "'")
        try:
            print(bool(re.compile(pattern)))
        except re.error:
            #exc_type, value, traceback = sys.exc_info()
            #print("Failed with exception [%s]" % exc_type.__name__)
            print(False)
