# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:04:55 2019

@author: Ham

HackerRanch Challenge: Reduce Function

Task

Given a list of rational numbers, find their product.

Concept
The reduce() function applies a function of two arguments cumulatively on a
list of objects in succession from left to right to reduce it to one value.
Say you have a list, say [1,2,3] and you have to find its sum.

>>> reduce(lambda x, y : x + y,[1,2,3])
6

You can also define an initial value.
If it is specified, the function will assume initial value as the value given,
and then reduce.
It is equivalent to adding the initial value at the beginning of the list.

For example:

>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1

Input Format

First line contains n, the number of rational numbers.
The i-th of next n lines contain two integers each,
the numerator (Ni) and denominator (Di) of the i-th rational number in the list.

Constraints

Output Format

Print only one line containing the numerator and denominator
of the product of the numbers in the list in its simplest form,
i.e. numerator and denominator have no common divisor other than 1.

Sample Input (see STDIN_SIO)

3
1 2
3 4
10 6

Sample Output 0

5 8
(3375671233756712072330395738417580...  3705837503712819180280939360...)

Explanation 0

Required product is 1/2 * 3/4 * 10/16 = 5/8

"""

from fractions import Fraction
from functools import reduce
import io

STDIN_SIO = io.StringIO("""
14
52737478 34003691
62363113 957799033
190929719 615218615
992985647 807326870
734000922 406264
971585263 760842031
354380779 898578100
90099574 913526239
67885048 68658688
747850777 53706795
145445334 663338252
138389787 985338986
345935685 695803944
121407471 971857603
""".strip())

def product(fracs):
    """doc"""
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    #for _ in range(int(input())):
    #    fracs.append(Fraction(*map(int, input().split())))
    for _ in range(int(STDIN_SIO.readline().strip())):
        fracs.append(Fraction(*map(int,
                                   STDIN_SIO.readline().strip().split())))
    result = product(fracs)
    print(*result)
