# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:59:07 2021

@author: Ham

HackerRank > Practice > Algorithms > Strings
Caesar Cipher

Problem

Julius Caesar protected his confidential information by encrypting it
using a cipher.
Caesar's cipher shifts each letter by a number of letters.
If the shift takes you past the end of the alphabet,
just rotate back to the front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
Example


The alphabet is rotated by , matching the mapping above.
The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string
Input Format

The first line contains the integer, n, the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.

Constraints



 is a valid ASCII string without any spaces.

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
Explanation

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b

"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys
import string

import io

STDIN_SIO = io.StringIO("""
38 test case 11, expected: Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj
Always-Look-on-the-Bright-Side-of-Life
5
11 test case 5, expected: okffng-Qwvb
middle-Outz
2
""".strip())


encoder = string.ascii_lowercase \
        + string.ascii_lowercase \
        + string.ascii_uppercase \
        + string.ascii_uppercase


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    res = ""
    k %= len(string.ascii_lowercase)
    for c in s:
        idx = encoder.find(c)
        res += (c if idx < 0 else encoder[idx + k])

    return res


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #n = int(input())
    #s = input()
    #k = int(input())

    n = int(STDIN_SIO.readline().strip().split()[0])
    s = STDIN_SIO.readline()
    k = int(STDIN_SIO.readline())

    result = caesarCipher(s, k)

    print(result)

    #fptr.write(result + '\n')
    #fptr.close()
