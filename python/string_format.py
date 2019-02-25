# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:56:18 2019

@author: Ham

HackerRanch Challenge: String Formatting

Given an integer, N, print the following values for each integer i from 1 to N:

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line
in the order specified above for each i from 1 to N.
Each value should be space-padded to match the width of the binary value of N.

Input Format

A single integer denoting .

Constraints

Output Format

Print N lines where each line i (in the range 1 <= i <= N)
contains the respective decimal, octal, capitalized hexadecimal,
and binary values of i.
Each printed value must be formatted to the width of the binary value of N.

Sample Input

17
Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

"""

def print_formatted(number):
    """Print from 1 to number in all bases."""
    w = number.bit_length()
    for i in range(1, number + 1):
        print("{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(i, w=w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
