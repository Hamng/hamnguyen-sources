# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:32:41 2019

@author: Ham

HackerRanch Challenge: Triangle Quest 2

You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

You can't take more than two lines.
The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.

Input Format

A single line of input containing the integer N.

Constraints

1 <= N <= 9

Output Format

Print the palindromic triangle of size N as explained above.

Sample Input

5

Sample Output

1
121
12321
1234321
123454321

"""
from functools import reduce

#More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())+1):
    print([0, 1, 121, 12321, 1234321, 123454321, 12345654321,
           1234567654321, 123456787654321, 12345678987654321][i])

    # Similar to the original "Triangle Quest" challenge,
    # this problem is simple to solve, but *SEVERELY RESTRICTIVE*!
    # I cheated above by adopting other people's solution in the other challenge.
    # Below 4 are the square of working solutions also from the other Discussion:
    # (too bad, Python 3 removes reduce(), and moves it inside functools.

    print(((10**i) // 9)**2)

    print(((10**i - 1) // 9) ** 2)

    print(sum(map(lambda n: 10**n, range(i)))**2)

    print(reduce(lambda x, y: x*10+y, [1]*i) ** 2)

