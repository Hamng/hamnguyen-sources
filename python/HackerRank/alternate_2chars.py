# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:21:03 2021

@author: Ham

HackerRank > Practice > Algorithms > Strings
Two Characters

Problem

In this challenge, you will be given a string.
You must remove characters until the string
is made up of any two alternating characters.
When you choose a character to remove,
all instances of that character must be removed.
Your goal is to create the longest string possible
that contains just two alternating letters.

As an example, consider the string abaacdabd.
If you delete the character a, you will be left with the string bcdbd.
Now, removing the character c leaves you with
a valid string bdbd having a length of 4.
Removing either b or d at any point would not result in a valid string.

Given a string s, convert it to the longest possible
string t made up only of alternating characters.
Print the length of string t on a new line.
If no string t can be formed, print 0 instead.

Function Description

Complete the alternate function in the editor below.
It should return an integer that denotes the longest string that can be formed,
or 0 if it cannot be done.

alternate has the following parameter(s):

s: a string
Input Format

The first line contains a single integer denoting the length of s.
The second line contains string s.

Constraints

Output Format

Print a single integer denoting the maximum length of  for the given s;
if it is not possible to form string t, print 0 instead.

Sample Input

10
beabeefeab
Sample Output

5
Explanation

The characters present in s are a, b, e, and f.
This means that t must consist of two of those characters
and we must delete two others.
Our choices for characters to leave are
[a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].

If we delete e and f, the resulting string is babab.
This is a valid t as there are only two distinct characters (a and b),
and they are alternating within the string.

If we delete a and f, the resulting string is bebeeeb.
This is not a valid string t because there are consecutive e's present.
Removing them would leave consecutive b's,
so this fails to produce a valid string .

Other cases are solved similarly.

babab is the longest string we can create.

"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys
import itertools

import io

STDIN_SIO = io.StringIO("""
141 test case 8, expected: 8
cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc
1000 test case 30, expected: 0
ucwtvajqreigbqszaukfieswtlhdvwhvlzsxswzbfcropnxlektloohamginpsxeooqsnlbaglmhiyednqibglmodhylweshcquhvxtqclqbvmptqglungavqccwlmhhogdlrzufeccpdmwnnrmgcxqlwdvtqqbicqbfgldxgdkkyvpzvlsncotyhwqeilzmguhpyrazsbsfvkzjzabcvrqwqndoqgztxtlpbfjcvbsplvbwlmmuyyqhiknybizxjzmrjvrtrsshgbiidrrcbapdwsxzlzlmcwrtvngokdvywjglorficgxqvatsbnvplqinopcrttpseweeekbypkvdanbcofvziojhpzhzaltgqvpstrrxfrjhdsdhrtwqzcqneicivppiquubsrvvbrtmwyhhqailyaaypfeusuefgqmbxmfadxtznfxfdtqggxeorjpvtmixlykezahzhxjbovglxggwxfcyrfxpefzolryernhmebhvcidocnknucdldlqtfvcoecygvejdrjnfrfrbqagcbellxnodvlzieerarmzrzfrdgxuhcfuwxvjlqmlflciotcylyyeywgtqgmbwghxaqesjgisuarjhqldcvxgyqzkwpecbapxxhevazufbgkrrzgxcnuuqdzzizbethncfhuvfjgccikzkqnksexzdvbhabdbrdspuygmhvmlbsptzejjtqnbdjpnhzamqvwliukpxxvkspgqxkedqcaaqwhglfiteiqnweyyfwswrkitadrayaqpllnnfatktsdlwtggzvjpefjglqbvpkpgtwarolbmsfbqxjsznmlmdohxwuxlasppsmqfcmfggxvimymnyqqoxdljdcyqlleuhfbemkwyysykdnjcazwrjhqpsclzhezqzghsmuzrapkxccniagkzfkntzrufvgqhbkfgyajwczsihigazrwvkdzequtqabdqqixjqudvdkvydknuamcxr
28 test case 31, expected: 8
asdcbsdcagfsdbgdfanfghbsfdab
10 test case 0, expected: 5
beabeefeab
""".strip())

def keepOnly2(s, keep):
    # keep only chars in s that are in keep
    lst = [c for c in s if c in keep]
    if (l := len(lst)) < 2:
        return 0

    prev = lst[0]
    for c in lst[1:]:
        if c == prev:
            # not alternating, so return 0
            return 0
        prev = c
    #print("removing", tup, len(lst), lst)
    return l

    # alternatively, can do the 1-liner list comprehension below:
    #   return l if all([lst[i] != lst[i+1] for i in range(l-1)]) else 0
    # but it generates a new list of length len(lst)-1 which could be long
    # whereas the for loop above would terminate permaturely if not alternating


# Complete the alternate function below.
def alternate(s):
    # uniq: set of unique chars in s
    uniq = set(s)
    if len(uniq) < 2:
        return 0

    # Iterating thru all combos of 2-chars from the uniq set
    # could shorten to a list comprehension as:
    #   return max([keepOnly2(s, tup) for tup in ...])
    # but the list could be long, and we don't need to keep all elements
    # so doing the usual for loop instead
    mx = 0
    for tup in itertools.combinations(uniq, 2):
        ln = keepOnly2(s, tup)
        if ln > mx:
            mx = ln
    return mx


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #l = int(input().strip())
    #s = input()

    l = int(STDIN_SIO.readline().strip().split()[0])
    s = STDIN_SIO.readline()

    result = alternate(s)

    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
