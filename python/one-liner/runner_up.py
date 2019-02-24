# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:18:55 2019

@author: Ham

HackerRanch Challenge: Find the Runner-Up Score!

Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given N scores.
Store them in a list and find the score of the runner-up.

Input Format

The first line contains N.
The second line contains an array A of N integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
"""

if __name__ == '__main__':
    #n = int(input())
    #arr = map(int, input().split())
    arr = '2 3 6 6 5'.split()

    print(sorted(list(set(arr)), reverse=True)[1])
