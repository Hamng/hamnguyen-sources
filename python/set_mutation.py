# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:03:24 2019

@author: Ham

HackerRanch Challenge: Set Mutations

You are given a set A and N number of other sets.
These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

Input Format

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2*N lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries
of the operation name and the length of the other set.
The second line of each part contains space-separated
list of elements in the other set.

 len(set(A))
 len(otherSets)

Output Format

Output the sum of elements in set A.

Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

Sample Output

38

"""

import io

STDIN_SIO = io.StringIO("""
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
""".strip())

if __name__ == '__main__':
    #input()                             # discarded, not needed
    #a = set(map(int, input().split()))
    #for _ in range(int(input())):
    #    op, _ = input().strip().split()
    #    b = set(map(int, input().split()))

    STDIN_SIO.readline().strip()                             # discarded, not needed
    a = set(map(int, STDIN_SIO.readline().strip().split()))
    for _ in range(int(STDIN_SIO.readline().strip())):
        op, _ = STDIN_SIO.readline().strip().split()
        b = set(map(int, STDIN_SIO.readline().strip().split()))
        #print(op, b)
        #print("exec('a." + op + "(" + str(b) + ")')")
        exec("a." + op + "(b)")
        #print("a=", a)

    print(sum(a))
