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

def min_length_substring_exhaustive(s, t):
  # NOT working for long strings: taking too long
  # Complexity: probably min: O(len(t)!)    max: O(len(s)!)
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


def count_chars(s):
    """Return a dict counting how many times each char occurs in s"""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def is_subdict(dict_super, dict_sub):
    """Return True if for each key in dict_sub, dict_super[key] >= dict_sub[key]"""
    for key, value in dict_sub.items():
        # I could use "if dict_super.get(key, 0) < value return False"
        # but that assumes value is a positive numeric.
        # Using the code below, no such assumption, as long as '<' works
        if key not in dict_super:
            return False
        if dict_super[key] < value:
            return False

    # All satisfied
    return True


def min_length_substring(s, t):
    """Algorithm: for any substring s_sub of s
       (1. Each char in t must also occur in s_sub.)
        2. The count of each char in t must be <= count of same char in s_sub.
           This also covers #1 above, so #1 could be used as a quick test.
        3. That guarantees that t is a substring of a permutation of s_sub.
        4. First, test the entire s. Return failure immediately if fail.
        5. Next, squeezing from the right side: eliminate 1 char at a time from
           the right then re-evaluate till fail.
           Mark the position when it fails: that's the end position of s_min
        6. Next, similarly squeezing from the left side.
           That marks the begin position of s_min
        7. Return the final min_length.
        8. Complexity: O(len(t) + len(s) + len(s) + len(s))
        Implementation:
            1i. Build a t_dict that counts each char in t.
            2i. Same for s_sub_dict.
            3i. #1 becomes: set(t_dict.keys()) must be a subset of set(s_sub_dict.keys())
            4i. #2 becomes: for each key in t_dict.keys():
                t_dict[key] <= s_sub_dict[key]
    """
    t_dict = count_chars(t)
    s_dict = count_chars(s)
    print(t, t_dict)
    print(s, s_dict)
    if not is_subdict(s_dict, t_dict):
        # t isn't a substring of any permutation of s
        return -1

    # Squeezing from the right side of s
    for i, c in enumerate(s[::-1]):
        s_dict[c] -= 1
        if not is_subdict(s_dict, t_dict):
            s_dict[c] += 1
            s_min_end = len(s) - i - 1
            # inc back the count of c that was decremented
            # Since i goes backward, the actual pos is len(s)-i-1
            #print(s_min_end, s[:s_min_end+1], s_dict)
            break

    # Squeezing from the left side of s
    for i, c in enumerate(s):
        s_dict[c] -= 1
        if not is_subdict(s_dict, t_dict):
            # s_dict[c] += 1    don't need to readjust anymore
            print(i, s_min_end, s_min_end - i + 1, s[i:s_min_end+1])
            return s_min_end - i + 1

    # is an error if finish the for loop above
    raise RuntimeError('t="%s", s="%s", right_most=%d' % (t, s, s_min_end))




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
  s2 = "bfbea c dbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  #s2 = "bfbeabcbfea"
  #t2 = "cbccfa"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

	# Add your own test cases here
