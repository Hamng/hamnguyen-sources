# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:46:42 2019

@author: Ham

HackerRanch Challenge: Triangle Quest

You are given a positive integer N.
Print a numerical triangle of height N-1 like the one below:

1
22
333
4444
55555
......

Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines.
The first line (the for statement) is already written for you.
You have to complete the print statement.

Note: Using anything related to strings will give a score of 0.

Input Format

A single line containing integer, N.

Constraints

1 <= N <= 9

Output Format

Print N-1 lines as explained above.

Sample Input

5

Sample Output

1
22
333
4444

"""

#More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())):
    print(*([i]*i), sep=chr(0))

    # This problem is *SEVERELY RESTRICTIVE*!
    # Above is my best attempt but still doesn't work since I tried to
    # add a NUL between the digits, but print() displays a NUL as a space.
    # Below are 5 best & working answers from the Discussion forum:
    # (too bad, Python 3 removes reduce(), and moves it inside functools.

    print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])

    print(((10**i) // 9)*i)
    print(((10**i - 1) // 9) * i)

    print(sum(map(lambda x: i * 10**x, range(i))))

    #print(reduce(lambda x,y: x*10+y, [i]*i))
