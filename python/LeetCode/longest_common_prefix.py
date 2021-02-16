# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:32:23 2021

@author: Ham

LeetCode #14. Longest Common Prefix

Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""
from typing import List

import io

# 2 lines for each testcase. 2nd line is the expected result
STDIN_SIO = io.StringIO("""
["flower","flow","flight"]
"fl"
["dog","racecar","car"]
""
""".strip())


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for tup in zip(*strs):
            #print(tup)
            t0 = tup[0]

            for t in tup[1:]:
                if t != t0:
                    return prefix
            prefix += t0

            # Alternately, can use a list comprehension as:
            #if all([t == t0 for t in tup[1:]]):
            #    prefix += t0
            #else:
            #    return prefix
            # But it'd iterate thru ALL elements of tup() regardless
            # whereas the simple for loop would shortcut on a mismatch

            # Yet another alternative, which also iterates all tup():
            #if len(set(tup)) == 1:
            #    prefix += tup[0]
            #else:
            #    return prefix

        return prefix


if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break
        exec("strs=" + line)
        result = Solution().longestCommonPrefix(strs)
        print('longestCommonPrefix(', strs, ') returned "' + result + '"')

        if not (line := STDIN_SIO.readline().strip()):
            break
        exec("strs=" + line)
        if strs != result:
            print('Expected="' + strs + '"')
