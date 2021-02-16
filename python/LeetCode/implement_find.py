# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:00:55 2021

@author: Ham

LeetCode #28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string?
This is a great question to ask during an interview.

For the purpose of this problem,
we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf() and Python's find().


Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0


Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.

"""

import io

# 2 lines for each testcase; 2nd line is the expected result.
STDIN_SIO = io.StringIO("""
"hello"
"ll"
2
"aaaaa"
"bba"
-1
""
""
0
mississippi
issip
4
""".strip())


class Solution_find:
    # speed: fastest, simplest but pointless since purpose is implement find()
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return -1 if len(needle) > len(haystack) else haystack.find(needle)

class Solution_slice:
    # speed: very slightly slower than using the builtin find()
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len_n = len(needle)
        last_h = len(haystack) - len_n + 1
        #if last_h < 1:
        #    return -1
        for found in range(last_h):
            if needle == haystack[found:found+len_n]:
                return found
        return -1

class Solution_loop:
    # speed: very slightly slower than using the builtin find()
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        last_h = len(haystack) - len(needle) + 1
        #if last_h < 1:
        #    return -1
        for found in range(last_h):
            #for ofs, chr_n in enumerate(needle):
            #    if chr_n != haystack[found + ofs]:
            #        break
            for chr_n, chr_h in zip(needle, haystack[found:]):
                if chr_n != chr_h:
                    break
            else:
                return found
        return -1


if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break

        line = line.strip('"')
        needle = STDIN_SIO.readline().strip().strip('"')
        found = Solution_loop().strStr(line, needle)
        expected = int(STDIN_SIO.readline().strip())
        print('@' + str(found) + ': found needle "' + needle
              + '" in haystack "' + line + '"',
              "" if found == expected else ("!= @" + str(expected)))
