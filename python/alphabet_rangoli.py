# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:59:24 2019

@author: Ham

HackerRanch Challenge: Alphabet Rangoli

You are given an integer, N.
Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter 'a',
and the boundary has the Nth alphabet letter (in alphabetical order).

Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Output Format

Print the alphabet rangoli in the format explained above.

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""

def print_rangoli(size):
    """doc"""
    a = ord('a')
    for i in range(size):
        ln = size - 1 - i
        dash = '-' * (2 * ln)
        center = [chr(a + ln + j) for j in range(i + 1)]
        right = list(center)        # must copy to a new list
        center.reverse()
        center += right[1:]
        print(dash + "-".join(center) + dash)

    for i in range(size - 2, -1, -1):
        l = size - 1 - i
        dash = '-' * (2 * l)
        center = [chr(a + l + j) for j in range(i + 1)]
        right = list(center)        # *MUST* copy to a new list
        center.reverse()
        center += right[1:]
        print(dash + "-".join(center) + dash)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
