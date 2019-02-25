# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 00:54:42 2019

@author: Ham

HackerRanch Challenge: DefaultDict Tutorial

In this challenge, you will be given 2 integers, N and M.
There are N words, which might repeat, in word group A.
There are words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A.
If it does not appear, print .

Constraints



Input Format

The first line contains integers, N and M separated by a space.
The next N lines contains the words belonging to group A (might repeat).
The next M lines contains the words belonging to group B.

Output Format

Output M lines.
The i_th line should contain the 1-indexed positions of
the occurrences of the i_th word separated by spaces.

Sample Input (see stdin_sim below)

Sample Output

1 2 4
3 5

"""

from collections import defaultdict

stdin_sim = """
5 2
a
a
b
a
b
a
b
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    #n, m = map(int, input().split())
    n, m = map(int, stdin_sim.pop(0).split())
    occ = defaultdict(list)
    for i in range(1, n + 1):
        occ[stdin_sim.pop(0)].append(str(i))
        #occ[input()].append(str(i))
    #print(occ)

    for _ in range(m):
        #w = input()
        w = stdin_sim.pop(0)
        if w in occ:
            print(" ".join(list(occ[w])))
        else:
            print(-1)
