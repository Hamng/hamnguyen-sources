# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:40:20 2020

@author: Ham

HackerRank > Practice > Interview Preparation Kit > Warm-up Challenges
Jumping on the Clouds

Problem
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to
the number of the current cloud plus 1 or 2.
She must avoid the thunderheads.
Determine the minimum number of jumps it will take
Emma to jump from her starting postion to the last cloud.
It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe
or 1 if they must be avoided.
For example, c=[0,1,0,0,0,1,0] indexed from 0...6
The number on each cloud is its index in the list
so she must avoid the clouds at indexes 1 and 5.
She could follow the following two paths: 0-2-4-6 or 0-2-3-4-6.
The first path takes 3 jumps while the second takes 4.

Function Description

Complete the jumpingOnClouds function in the editor below.
It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

c: an array of binary integers

Input Format

The first line contains an integer n, the total number of clouds.
The second line contains n space-separated binary integers
describing clouds c[i] where 0 <= c[i] < n.

Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0
Sample Output 0

4
Explanation 0:
Emma must avoid 2 and 5. She can win the game with a minimum of 4 jumps:


Sample Input 1

6
0 0 0 0 1 0
Sample Output 1

3
Explanation 1:
The only thundercloud to avoid is 4. Emma can win the game in 3 jumps:

"""

#import math
#import os
#import random
#import re
#import sys

import io

STDIN_SIO = io.StringIO("""
85
0 1 0 1 0 1 0 0 0 0 0 0 0 0 1 0 1 0 0 0 \
0 1 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 \
1 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 1 \
0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 1 0 \
0 1 0 1 0
""".strip())


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c) < 2:
        # at the last one, can't jump anymore
        return 0
    if len(c) == 2:
        # at next-to-last: if can't jump to last, return 0
        # else return 1 since can make 1 last jump
        return 1 - c[-1]
    if len(c) == 3:
        # at 2nd-to-last: if can't jump to neither last, nor next-to-last ==> 0
        # else return 1 since can make 1 last jump to either
        return (0 if ((c[-1] + c[-2]) > 1) else 1)

    if c[2] == 0:
        # if able to, jump to the next-next then recursive from there
        return 1 + jumpingOnClouds(c[2:])
    elif c[1] == 0:
        # if able to, jump to the next then recursive from there
        return 1 + jumpingOnClouds(c[1:])
    else:
        throw(RuntimeError, "Can't jump anywhere")

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    #c = list(map(int, input().rstrip().split()))

    n = int(STDIN_SIO.readline())
    c = list(map(int, STDIN_SIO.readline().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
