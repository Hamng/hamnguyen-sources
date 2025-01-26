# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:47:27 2020

@author: Ham

HackerRank > Practice > Interview Preparation Kit > Warm-up Challenges
Repeated String

Problem
Lilah has a string, s,
of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's
in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10,
the substring we consider is 'abcacabcac',
the first 10 characters of her infinite string.
There are 4 occurrences of 'a' in the substring.

Function Description

Complete the repeatedString function in the editor below.
It should return an integer representing the number of occurrences
of 'a' in the prefix of length n in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider

Input Format

The first line contains a single string, s.
The second line contains an integer, n.

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter 'a's in the first n
letters of the infinite string created by repeating s infinitely many times.

Sample Input 0

aba
10

Sample Output 0

7

Explanation 0
The first 10 letters of the infinite string are 'abaabaabaa'
Because there are 7 a's, we print 7 on a new line.

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first 1000000000000 letters of the infinite string are 'a',
we print 1000000000000 on a new line.

"""


#import math
#import os
#import random
#import re
#import sys


import io

STDIN_SIO = io.StringIO("""
afcfffaged
962645758455
""".strip())


# Complete the repeatedString function below.
def repeatedString(s, n):
    c = s.count('a')
    if c == 0:
        # 'a' not in s[] so immediately return 0
        return 0
    #print('n=', n, 'len=', len(s), "s='" + s + "'")
    n, r = divmod(n, len(s))
    #print('n=', n, '* c=', c, "+ s.count('a',0,", r, ')=', s.count('a', 0, r))
    return n * c + s.count('a', 0, r)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    #n = int(input())

    # VERY CRUCIAL to rstrip() to remove the invisible '\n' at the end of s
    s = STDIN_SIO.readline().rstrip()

    n = int(STDIN_SIO.readline())

    result = repeatedString(s, n)

    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
