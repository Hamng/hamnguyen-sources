# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:08:00 2019

@author: Ham

HackerRanch Challenge: Text Wrap

You are given a string S and width N.
Your task is to wrap the string into a paragraph of width N.

Input Format

The first line contains a string, S.
The second line contains the width, N.

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
    #result = wrap(string, max_width)
    print("\n".join([string[max_width*i:max_width*(i + 1)]
                     for i in range(int(len(string)/max_width) + 1)]))
