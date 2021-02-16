# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 07:16:00 2021

@author: Ham

HackerRank > Practice > Algorithms > Strings
Alternating Characters

Problem
You are given a string containing characters A and B only.
Your task is to change it into a string such that
there are no matching adjacent characters.
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

Example

s ="AABAAB"

Remove an A at positions 0 and 3 to make ABAB in 2 deletions.

Function Description

Complete the alternatingCharacters function in the editor below.

alternatingCharacters has the following parameter(s):

string s: a string
Returns

int: the minimum number of deletions required
Input Format

The first line contains an integer , the number of queries.
The next  lines each contain a string  to analyze.

Constraints

Each string  will consist only of characters  and .
Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Sample Output

3
4
0
0
4
Explanation

The characters marked red are the ones that can be deleted so that the string does not have matching adjacent characters.

image

"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys
#import itertools

import io

# After the 1st line, 2 lines per testcase, 2nd of each is the expected output
STDIN_SIO = io.StringIO("""
15
AAAA
3
BBBBB
4
ABABABAB
0
BABABA
0
AAABBB
4
AABBABABBBBBABBABABBBBABBABABABBABBABBBBAAABBBBBBBBBBBABBBBBBBABBBBBBBBBBBBABBABBBBAABBBBBAAAABBBBBB
62 Testcase #3 +10
ABBBABBBBBABBBBBBBABAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAABBBBBABBBBBBBBABAAABBBBBBBBBBBBBBBBBBAABBBBABB
78
BBBBBABBBBBABABAABBBBBBBBBABBBBBBBBBBBBBBBBBBBBBBBABBABBBBBBABBBBAABBBBBBABBBBAABBBABBBAABBABABABBBA
66
BABBAABBBBABBABBBBBBBBBBABBBBBBBBBABBBBBBBABBBAABBBBBBABBBBBABBBBBBBBBBABABABBABABABBBBABBBABBBBBBAB
61
BABBABBBBBBBABBBBBABBBABBBABBABAABBBBBBBBABAABBBBBBBBBABAAABABBAABABBBBBBBBBBABBBBBABBBBBBBBBBBAABBB
63
BBBBBBBBBBBBBABBBBBAABBAAABBBBBBABBBBBBBBBBBBBBBBBBBABBBBBBBBABBAABBBBABABBBABABBBBBBABABBBBABBBBABA
68
BABBBBBBBAABBBABBBBBBBBBBBBBBBBAABABBABBABBBBBBBBBBABABBBBBBBBBBBBBBBAABBBBBBBBBBBBABBBBBABBBBBBBBBB
75
ABBBBABBBBBBBABABBBAABABBBBAABBAABBABBBBBBABABBBBABABBBBBBBBBBBBBBBBBBBBBBBBAABBBABBBBBBBBAABBBBBBBB
68
BBBBBBBBBBABBBBBBBBBBBBBBBBBBBBBBBBBABBBBBBBABBBBBBABBABAABBBBBABBBBBABBBBBBBABBBBBABBBBBBBABBAABBAB
73
BABBBBBBBBBBABBBBBBBBABBBBBAABBBABBBBAABBBBBBABBBBBBBBBABBBBBBBBBBBBBABBBBBBBAABBBBBBABBBBBBABBABBBB
73
""".strip())


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    if not s:
        return 0

    # Credit to itcreativetechn1's 1/16/21 comment, probably the fastest
    dup = 0
    for i, v in enumerate(s[1:], 1):
        if v == s[i-1]:
            dup += 1
    return dup

    # Or the same as a 1-liner:
    return len([1 for i in range(1, len(s)) if s[i]==s[i-1]])

    # The cool 1-liner is:
    #   return len(s) - len(list(itertools.groupby(s)))
    # but is much slower than the loop below (since having to create groups)

    # But amazingly, the seemingly cheating 1-liner below runs the fastest!
    # Algorithm: if 1st=='A', then after removing dups,
    # the resulting alternate string would be res = "AB" * N
    # where N is how many times "AB" occur in s.
    # Vice versa, if 1st=='B', res = "BA" * count("BA")
    # E.g. s=AAABBAABBBAAA, res = "AB" * 2 + "A"
    # Then the num of removals is: len(s) - len(res)
    # But knowing that len("AB")==2, we don't need to form res,
    # and can calculate its length as: len(res) = 2 * N + int(1st == last)
    # Hence:

    return len(s) - 2 * s.count("AB" if s[0]=='A' else "BA") - int(s[0] == s[-1])

    if len(set(s)) == 1:
        return len(s) - 1

    drop = 0
    prev = s[0]
    for c in s[1:]:
        if c == prev:
            drop += 1
        else:
            prev = c
    return drop


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #q = int(input())

    q = int(STDIN_SIO.readline())

    for q_itr in range(q):
        #s = input()

        s = STDIN_SIO.readline().strip()

        result = alternatingCharacters(s)

        expected = int(STDIN_SIO.readline().split()[0])

        print(result,
              "" if result == expected
              else ("!= " + str(expected) + ' "' + s + '"'))

        #fptr.write(str(result) + '\n')

    #fptr.close()
