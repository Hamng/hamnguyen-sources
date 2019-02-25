# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 02:04:33 2019

@author: Ham

HackerRanch Challenge: Named Tuple

Task

Dr. John Wesley has a spreadsheet containing a list of student's ID,
MARKS, CLASS and NAME.

Your task is to help Dr. Wesley calculate the average marks of the students.


Note:
1. Columns can be in any order.
   IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME.
   (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the ID, MARKS, CLASS and NAME
under their respective column names.

Constraints


Output Format

Print the average marks of the list corrected to 2 decimal places.

Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

TESTCASE 02 (see stdin_sim below)

Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00

"""

import collections

stdin_sim = """
5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    #n = int(input())
    #Grade = collections.namedtuple('Grade', " ".join(input().split()))
    n = int(stdin_sim.pop(0))
    Grade = collections.namedtuple('Grade', " ".join(stdin_sim.pop(0).split()))

    #total = 0.0
    #for _ in range(n):
    #    g = Grade(*(input().split()))
    #    #print(g)
    #    total += float(g.MARKS)
    #print("%0.2f" % (total / n))

    # Below is a 1-liner to make this a 4-lines program
    print("%0.2f" % (sum([float(Grade(*(stdin_sim.pop(0).split())).MARKS)
                          for _ in range(n)]) / n))
