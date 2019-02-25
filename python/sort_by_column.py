# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:25:10 2019

@author: Ham

HackerRanch Challenge: Athele Sort

Task

You are given a spreadsheet that contains a list of N athletes and their details
(such as age, height, weight and so on).
You are required to sort the data based on the K-th attribute and print the
final resulting table. Follow the example given below for better understanding.

image

Note that K is indexed from 0 to M - 1, where M is the number of attributes.

Note: If two attributes are the same for different rows,
for example, if two atheletes are of the same age,
print the row that appeared first in the input.

Input Format

The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.

Constraints



Each element

Output Format

Print the  lines of the sorted table.
Each line should contain the space separated elements.
Check the sample below for clarity.

Sample Input 0 (see stdin_sim below)

Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

"""

from operator import itemgetter

stdin_sim = """
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    #n, m = map(int, input().split())
    n, m = map(int, stdin_sim.pop(0).split())

    #arr = [map(int, input().rstrip().split()) for _ in range(n)]
    arr = [list(map(int, stdin_sim.pop(0).rstrip().split())) for _ in range(n)]

    #k = int(input())
    k = int(stdin_sim.pop(0))

    [print(" ".join([str(e) for e in l])) for l in sorted(arr, key=itemgetter(k))]
