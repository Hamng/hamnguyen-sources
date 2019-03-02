# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:03:24 2019

@author: Ham

HackerRanch Challenge: Set .intersection() Operation

Task
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English,
some have subscribed to only French
and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper,
and the other set is subscribed to the French newspaper.
The same student could be in both sets.
Your task is to find the total number of students
who have subscribed to at least one newspaper.

Input Format

The first line contains an integer, E,
the number of students who have subscribed to the English newspaper.
The second line contains E space separated roll numbers of those students.
The third line contains F,
the number of students who have subscribed to the French newspaper.
The fourth line contains F space separated roll numbers of those students.

Constraints


Output Format

Output the total number of students who have subscriptions
to both English and French newspapers.

Sample Input (see STDIN_SIO)


Sample Output

13

"""

import io

STDIN_SIO = io.StringIO("""
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
""".strip())

if __name__ == '__main__':
    #input()                             # discarded, not needed
    #e = set(map(int, input().split()))
    #input()                             # discarded, not needed
    #f = set(map(int, input().split()))
    STDIN_SIO.readline().strip()                            # discarded, not needed
    e = set(map(int, STDIN_SIO.readline().strip().split()))
    STDIN_SIO.readline().strip()                            # discarded, not needed
    f = set(map(int, STDIN_SIO.readline().strip().split()))
    print(len(e.intersection(f)))
