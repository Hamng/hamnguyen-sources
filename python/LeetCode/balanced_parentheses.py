# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 00:08:46 2021

@author: Ham

LeetCode #20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

from typing import List

import io

STDIN_SIO = io.StringIO("""
"()"
"()[]{}"
"(]"
"([)]"
"{[]}"
""".strip())


class Solution:
    def isValid(self, s: str, ofs: int=0, need: List[str]=None) -> bool:
        if ofs >= len(s):
            return not need
        if need is None:
            need = []
        c = s[ofs]
        ofs += 1
        while True:
            if c == '(':
                need.append(')')
                break

            if c == '{':
                need.append('}')
                break

            if c == '[':
                need.append(']')
                break

            if c == ')':
                if not need or need.pop() != ')':
                    return False
                break

            if c == '}':
                if not need or need.pop() != '}':
                    return False
                break

            if c == ']':
                if not need or need.pop() != ']':
                    return False

            break

        return self.isValid(s, ofs, need)



class Solution_iterative:
    def isValid(self, s: str) -> bool:
        # NOT working!!
        paren = 0
        brace = 0
        bracket = 0
        for c in s:
            if c == '(':
                paren += 1
            elif c == ')':
                if (paren := paren - 1) < 0 or bool(brace + bracket):
                    return False
            elif c == '{':
                brace += 1
            elif c == '}':
                if (brace := brace - 1) < 0 or bool(paren + bracket):
                    return False
            elif c == '[':
                bracket += 1
            elif c == ']':
                if (bracket := bracket - 1) < 0 or bool(paren + brace):
                    return False
        return (paren + brace + bracket) == 0


if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip().strip('"')):
            break
        print('isValid("' + line + '") returned',
              Solution().isValid(line))
