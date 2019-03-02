# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:55:30 2019

@author: Ham

HackerRanch Challenge: Set .add()

If we want to add a single element to an existing set,
we can use the .add() operation.
It adds the element to the set and returns 'None'.

Example

>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps.
She decided to count the total number of distinct country stamps in her collection.
She asked for your help.
You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

Constraints


Output Format

Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France

Sample Output

5

"""

import io

STDIN_SIO = io.StringIO("""
7
UK
China
USA
France
New Zealand
UK
France
""".strip())

if __name__ == '__main__':
    #print(len({input().strip() for _ in range(int(input()))}))
    print(len({STDIN_SIO.readline().strip().strip()
               for _ in range(int(STDIN_SIO.readline().strip()))}))
    #print(stamps)
    #print(len(stamps))
