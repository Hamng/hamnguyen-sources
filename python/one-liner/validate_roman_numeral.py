# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:24:16 2019

@author: Ham

HackerRanch Challenge: Validating Roman Numerals

You are given a string, and you have to validate whether it's a valid Roman numeral.
If it is valid, print True.
Otherwise, print False.
Try to create a regular expression for a valid Roman numeral.

Input Format

A single line of input containing a string of Roman characters.

Output Format

Output a single line containing True or False according to the instructions above.

Constraints

The number will be between 1 and 3999 (both included).

Sample Input

CDXXI

Sample Output

True

References

Regular expressions are a key concept in any programming language.
A quick explanation with Python examples is available here.
You could also go through the link below
to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

"""

import re

regex_pattern = r"M{,3}((D?C{,3})|(C[DM]))?((L?X{,3})|(X[LC]))?((V?I{,3})|(I[VX]))?$"

print(bool(re.match(regex_pattern, input().strip(), flags=re.IGNORECASE)))

# Above was mine.
# Below is copied from Discussion, but
# ModuleNotFoundError: No module named 'roman'

#from roman import fromRoman
#try:
#    print(0 < fromRoman(input().strip()) < 4000)
#except:
#    print(False)
