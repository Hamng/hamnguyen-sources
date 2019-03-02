# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 05:49:37 2019

@author: Ham

HackerRanch Challenge: Check Strict Superset

You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the n sets.

Print True, if A is a strict superset of each of the n sets.
Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set {1, 3, 4} is a strict superset of set {1, 3}.
Set {1, 3, 4} is not a strict superset of set {1, 3, 4}.
Set {1, 3, 4} is not a strict superset of set {1, 3, 5}.

Input Format

The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets.

Constraints

Output Format

Print True if set A is a strict superset of all other n sets.
Otherwise, print False.

Sample Input 0 (see STDIN_SIO)

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0

False

Explanation 0

Set A is the strict superset of the set {1 2 3 4 5}
but not of the set {100 11 12} because 100 is not in set A.
Hence, the output is False.

"""

import io

STDIN_SIO = io.StringIO("""
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
""".strip())

if __name__ == '__main__':
    result = True
    #a = set(map(int, input().strip().split()))
    #for _ in range(int(input())):
    #    b = set(map(int, input().strip().split()))
    a = set(map(int, STDIN_SIO.readline().strip().split()))
    for _ in range(int(STDIN_SIO.readline().strip())):
        b = set(map(int, STDIN_SIO.readline().strip().split()))
        #result &= ((a.intersection(b) == b) and (a.intersection(b) != a))
        result &= (a > b)
    print(result)
