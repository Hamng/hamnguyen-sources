# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:55:11 2021

@author: Ham

HackerRank > Practice > Algorithms > Strings
Super Reduced String

Problem
Reduce a string of lowercase characters in range ascii[‘a’..’z’]
by doing a series of operations.
In each operation, select a pair of adjacent letters that match,
and delete them.

Delete as many characters as possible using this method
and return the resulting string.
If the final string is empty, return Empty String

Example.

s = "aab"

"aab" shortens to "b" in one operation: remove the adjacent "a" characters.

Function Description

Complete the superReducedString function in the editor below.

superReducedString has the following parameter(s):

string s: a string to reduce
Returns

string: the reduced string or Empty String
Input Format

A single string, s.

Constraints

Sample Input 0

aaabccddd
Sample Output 0

abd
Explanation 0

Perform the following sequence of operations to get the final string:

aaabccddd → abccddd → abddd → abd
Sample Input 1

aa
Sample Output 1

Empty String
Explanation 1

aa → Empty String
Sample Input 2

baab
Sample Output 2

Empty String
Explanation 2

baab → bb → Empty String

"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

import io

# Test case 11: Expected Output: acdqgacdqj
STDIN_SIO = io.StringIO("""
acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj
abd <- aaabccddd
empty <- ggppppuurrjjooddwwyyllmmvvffddmmppxxaabbddddooppxxgghhhhvvnneeqqyyttbbffvvjjiiaammmmddddhhyywwqqiijj
""".strip())


def reduce1(s):
    # This function does a 1-pass to reduce the string.
    # NOT working for identical pairs starting at an odd index;
    # e.g. "aab" reduces to "b", but "baa" stays "baa"
    # process pairs of adjacent chars in step of 2
    # for odd len(), last access would be out-of-bound so need to -1
    res = "".join([s[i] + s[i+1]
                   for i in range(0, len(s)-1, 2) if s[i] != s[i+1]])
    if len(s) & 1:
        # for odd len(), append the last char as-is
        res += s[-1]
    #print(s, len(s), len(res), "<" + res + ">")
    return res

# Complete the superReducedString function below.
def superReducedString(s):
    while True:
        s_new = reduce1(s)
        if len(s_new) < 2:
            # if len() is 0 or 1, done
            return s_new if len(s_new) else "Empty String"
        if s_new == s:
            # if after == before, reduce again starting at index 1
            s_new = s_new[0] + reduce1(s_new[1:])
            if s_new == s:
                # done if after == before
                return s_new if len(s_new) else "Empty String"
        s = s_new

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    s = STDIN_SIO.readline()

    result = superReducedString(s)

    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
