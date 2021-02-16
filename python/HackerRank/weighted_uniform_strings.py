# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:19:26 2021

@author: Ham

HackerRank > Practice > Algorithms > Strings
Weighted Uniform Strings

Problem

A weighted string is a string of lowercase English letters
where each letter has a weight.
Character weights are 1 to 26 from 'a' to 'z' as shown below:

Its order in the (English) alphabets

We define the following terms:

The weight of a string is the sum of the weights of all the string's characters.
For example:

image

A uniform string consists of a single character repeated zero or more times.
For example, ccc and a are uniform strings, but bcb and cd are not.
Given a string, s, let U be the
set of weights for all possible uniform contiguous substrings of string s.
You have to answer n queries, where each query i consists of a single integer, x[i].
For each query, print "Yes" on a new line if x[i] in U;
otherwise, print "No" instead.

Note: The  symbol denotes that  is an element of set .

Function Description

Complete the weightedUniformStrings function in the editor below.
It should return an array of strings, either "Yes" or "No", one for each query.

weightedUniformStrings has the following parameter(s):

s: a string
queries: an array of integers
Input Format

The first line contains a string s, the original string.
The second line contains an integer n, the number of queries.
Each of the next n lines contains an integer x[i],
the weight of a uniform subtring of s that may or may not exist.

Constraints

 will only contain lowercase English letters, ascii[a-z].
Output Format

Print n lines.
For each query, print "Yes" on a new line if x[i] in U.
Otherwise, print "No".

Sample Input 0

abccddde
6
1
3
12
5
9
10
Sample Output 0

Yes
Yes
Yes
Yes
No
No
Explanation 0

The weights of every possible uniform substring in the string abccddde are shown below:

image

We print Yes on the first four lines because the first four queries match weights of uniform substrings of . We print No for the last two queries because there are no uniform substrings in  that have those weights.

Note that while de is a substring of  that would have a weight of , it is not a uniform substring.

Note that we are only dealing with contiguous substrings. So ccc is not a substring of the string ccxxc.

Sample Input 1

aaabbbbcccddd
5
9
7
8
12
5
Sample Output 1

Yes
No
Yes
Yes
No

"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

import io

# Test case 31: Expected Output: [Yes, No, Yes, Yes, No]
STDIN_SIO = io.StringIO("""
aaabbbbcccddd
5
9
7
8
12
5
""".strip())



# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    w = set()
    prev = None
    count = 0
    for c in s:
        if c == prev:
            count += 1
        else:
            prev = c
            count = 1
        w.add(count * (ord(c) - ord('a') + 1))
    return ['Yes' if q in w else 'No' for q in queries]


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #s = input()
    #queries_count = int(input())

    s = STDIN_SIO.readline()

    queries_count = int(STDIN_SIO.readline())

    queries = []

    for _ in range(queries_count):
        #queries_item = int(input())
        queries_item = int(STDIN_SIO.readline())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    print("\n".join(result))

    #fptr.write('\n'.join(result))
    #fptr.write('\n')
    #fptr.close()
