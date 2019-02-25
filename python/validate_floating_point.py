# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:42:27 2019

@author: Ham

HackerRanch Challenge: Detect Floating Point Number

Task

You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy
all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖-+4.5

 Number must contain at least  decimal value.
For example:
✖ 12.
✔12.0

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using float(x).

Input Format

The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Constraints

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 0

False
True
True
False

Explanation 0

4.0O0: O is not a digit.
-1.00: is valid.
+4.54: is valid.
SomeRandomStuff: is not a number.

"""

stdin_sim = """
4
4.0O0
-1.00
+4.54
SomeRandomStuff
""".strip().splitlines()

if __name__ == '__main__':
    #for _ in range(int(input())):
    for _ in range(int(stdin_sim.pop(0))):
        try:
            #l = input()
            l = stdin_sim.pop(0)
            f = float(l)
            print(l.count('.') == 1)
        except ValueError:
            print(bool(False))
