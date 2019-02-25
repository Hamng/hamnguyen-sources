# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:04:36 2019

@author: Ham

HackerRanch Challenge: Designer Door Mat

Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of N and M.

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""

if __name__ == '__main__':
    w = 'WELCOME'
    #n, m = [int(i) for i in input().split()]
    n, m = 11, 33
    for i in range(int(n / 2)):
        #print(i)
        center = '.|' + '..|' * i * 2 + '.'
        outside = '-' * int((m - len(center)) / 2)
        print(outside + center + outside)

    outside = '-' * int((m - len(w)) / 2)
    print(outside + w + outside)

    for i in range(int(n / 2) - 1, -1, -1):
        #print(i)
        center = '.|' + '..|' * i * 2 + '.'
        outside = '-' * int((m - len(center)) / 2)
        print(outside + center + outside)
