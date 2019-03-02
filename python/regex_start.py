# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:23:20 2019

@author: Ham

HackerRanch Challenge: Re.start() and Re.end()

start() & end()
These expressions return the indices of the start and end
of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.

Constraints



Output Format

Print the tuple in this format: (start_index, end_index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa

Sample Output

(0, 1)
(1, 2)
(4, 5)

"""

import re

if __name__ == '__main__':
    s = "aaadaa" if True else input().strip()
    p = "aa"     if True else input().strip()
    #p = re.compile(p)
    #pos = 0
    #m = p.search(s, pos)
    #if m:
    #    while m:
    #        pos = m.start()
    #        print((pos, m.end() - 1))
    #        m = p.search(s, pos + 1)
    #else:
    #
    # The simpler code above is mine.
    # Otoh, the terribly complicated listcomp with nested-for
    # code below was copied from others in the Discussion forum
    #
    p = re.compile(r"(?=(" + p + "))")
    if not [print(e) for e in [(m.start(1), m.end(1)-1)
                               for m in p.finditer(s)]]:
        print((-1, -1))
