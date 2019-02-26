# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:10:08 2019

@author: Ham

HackerRanch Challenge: Validating UID

Task

ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID)
for each of its employees.
The company has assigned you the task of validating
all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (A - Z, a - z & 0 - 9).
No character should repeat.
There must be exactly  characters in a valid UID.

Input Format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid.
Otherwise, print 'Invalid', on separate lines.
Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354

Sample Output

Invalid
Valid

"""

import string
import collections
import io

STDIN_SIO = io.StringIO("""
2
B1CD102354
B1CDEF2354
""".strip())


def is_valid_uid(s):
    """doc"""
    #print(s)
    if len(s) != 10:
        return False

    c = collections.Counter(s)
    upp = 0
    dig = 0
    ld = string.ascii_letters + string.digits
    for k, v in c.items():
        if v > 1:
            return False                # repeating chars => False
        if k in string.digits:
            dig += 1
        elif k in string.ascii_uppercase:
            upp += 1
        elif k not in ld:
            return False                # neither digit nor letter => False

    return (upp > 1) and (dig > 2)      # >=2 UPPERCASE and >=3 digits

if __name__ == '__main__':
    for _ in range(int(STDIN_SIO.readline().strip())):
        print("Valid" if is_valid_uid(STDIN_SIO.readline().strip())
              else "Invalid")
