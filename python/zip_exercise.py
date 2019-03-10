# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:46:21 2019

@author: Ham

HackerRanch Challenge: Zipped!

zip([iterable, ...])

This function returns a list of tuples.
The i-th tuple contains the i-th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list
is truncated to the length of the shortest argument sequence.

Sample Code

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>>
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>>
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>>
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]

Task

The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5

Input Format

The first line contains N and X separated by a space.
The next N lines contains the space separated marks obtained by students in a particular subject.

Constraints



Output Format

Print the averages of all students on separate lines.

The averages must be correct up to 1 decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

Sample Output

90.0
91.0
82.0
90.0
85.5

"""

import io
import numpy

STDIN_SIO = io.StringIO("""
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
""".strip())

if __name__ == '__main__':
    _, x = map(int, STDIN_SIO.readline().strip().split())
    #grades_subject_student = [tuple(map(float, STDIN_SIO.readline().strip().split()))
    #                          for _ in range(x)]
    #_, x = map(int, input().strip().split())
    #grades_subject_student = [tuple(map(float, input().strip().split()))
    #                          for _ in range(x)]
    #print(grades_subject_student)
    #print(list(zip(*grades_subject_student)))
    #print(*[sum(s)/x for s in zip(*grades_subject_student)], sep="\n")

    # Above use zip().
    # Below use numpy but too bad, HackerChallenge seems to disable import numpy

    g = numpy.array([STDIN_SIO.readline().strip().split() for _ in range(x)],
                    float)
    print(g)
    print(*numpy.average(g, axis=0), sep="\n")
