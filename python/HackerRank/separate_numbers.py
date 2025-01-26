# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:29:00 2021

@author: Ham

HackerRank > Practice > Algorithms > Strings
Separate the Numbers

Problem
A numeric string, x, is beautiful if it can be split into a sequence of two or
more positive integers, a[1],a[2],...,a[n], satisfying the following conditions:

1. a[i]- a[i-1] = 1 for any 1 < i <= n
   (i.e., each element in the sequence is 1 more than the previous element).
2. No a[i] contains a leading zero.
   For example, we can split s = "10203" into the sequence {1, 02, 03},
   but it is not beautiful because "02" and "03" have leading zeroes.
3. The contents of the sequence cannot be rearranged.
   For example, we can split s = "312" into the sequence {3, 1, 2},
   but it is not beautiful because it breaks our first constraint
   (i.e., 1 - 3 != 1).
The diagram below depicts some beautiful strings:

image

You must perform q queries where each query consists of some integer string s.
For each query, print whether or not the string is beautiful on a new line.
If it's beautiful, print YES x, where x is the first number of the increasing sequence.
If there are multiple such values of x, choose the smallest.
Otherwise, print NO.

Function Description

Complete the separateNumbers function in the editor below.
It should print a string as described above.

separateNumbers has the following parameter:

s: an integer value represented as a string
Input Format

The first line contains an integer q, the number of strings to evaluate.
Each of the next q lines contains an integer string s to query.

Constraints

Output Format

For each query, print its answer on a new line
(i.e., either YES x where x is the smallest first number
 of the increasing sequence, or NO).

Sample Input 0

7
1234
91011
99100
101103
010203
13
1
Sample Output 0

YES 1
YES 9
YES 99
NO
NO
NO
NO
Explanation 0

The first three numbers are beautiful (see the diagram above).
The remaining numbers are not beautiful:

For "101103", all possible splits violate the first and/or second conditions.
For "010203" it starts with a zero so all possible splits violate the 2nd condition.
For "13", the only possible split is {1,3}, which violates the first condition.
For s = "1", there are no possible splits because s only has one digit.
Sample Input 1

4
99910001001
7891011
9899100
999100010001
Sample Output 1

YES 999
YES 7
YES 98
NO

"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

import io

# After the 1st line, 2 lines per testcase, 2nd of each is the expected output
STDIN_SIO = io.StringIO("""
21
1234
yes 1
91011
yes 9
99100
yes 99
101103
no
010203
no
13
no
1
no
99910001001
yes 999
7891011
yes 7
9899100
yes 98
999100010001
no
90071992547409929007199254740993
yes 9007199254740992, 10 lines from Testcase #4
45035996273704964503599627370497
yes 4503599627370496
22517998136852482251799813685249
yes 2251799813685248
11258999068426241125899906842625
yes 1125899906842624
562949953421312562949953421313
yes 562949953421312
90071992547409928007199254740993
no
45035996273704963503599627370497
no
22517998136852481251799813685249
no
11258999068426240125899906842625
no
562949953421312462949953421313
no
""".strip())


def found(s, val, loop=1):
    if not s:
        return True
    if s[0] == '0':
        return False
    val_str = str(val)
    if len(s) < len(val_str):
        return False
    #print("#" + str(loop) + ":", '"' + s + '".startswith("' + val_str + '")')
    return False if not s.startswith(val_str) \
        else found(s[len(val_str):], val + 1, loop+1)

# Complete the separateNumbers function below.
def separateNumbers(s):
    if (not s) or (len(s) < 2) or (s[0] == '0'):
        print("NO")
        return
    for l in range(1, min(16, len(s) // 2) + 1):
        #if (2 * l) > len(s):
        #    # can't fit 2 substrings of len l
        #    break
        start = int(s[:l])
        #print("<" + s + ">", l, start)
        if found(s[l:], start + 1):
            print("YES", start)
            return
    print("NO")

if __name__ == '__main__':
    #q = int(input())
    #for q_itr in range(q):
    #    s = input()

    q = int(STDIN_SIO.readline())

    for q_itr in range(q):
        s = STDIN_SIO.readline().strip()

        separateNumbers(s)
        print(STDIN_SIO.readline().strip(), '"' + s + '"')
