# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:09:41 2020

@author: Ham

Facebook Coding Practice: [Strings] Minimum Length Substrings

You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
Signature
int minLengthSubstring(String s, String t)
Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"'
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.

"""

#import math
# Add any extra import statements you may need here
import itertools

# Add any helper functions you may need here
def substring_n(s, n):
  for i in range(len(s)-n+1):
    yield s[i:i+n]

def min_length_substring(s, t):
  # Write your code here
  for pos in range(len(s)-len(t)+1):
    print(s, t)
    for l in range(len(t), len(s)-pos+1):
      sub_n = s[pos:pos+l]
      print(pos, l, sub_n)
      for p in itertools.permutations(sub_n):
        if ''.join(p).find(t) >= 0:
          print(l, sub_n)
          return l
  return -1











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  #s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  #t2 = "cbccfafebccdccebdd"
  s2 = "bfbeabcbfea"
  t2 = "cbccfa"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

	# Add your own test cases here
  