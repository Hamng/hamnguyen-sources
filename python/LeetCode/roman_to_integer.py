# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:46:00 2021

@author: Ham

LeetCode #13: Roman to Integer

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

import io

STDIN_SIO = io.StringIO("""
"III"
"IV"
"IX"
"LVIII"
"MCMXCIV"
""".strip())


double = {"II": 2, "IV": 4, "IX": 9, "XX": 20, "XL": 40, "XC": 90, "CC": 200, "CD": 400, "CM": 900}
#single = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
single = [0] * 26
ord_A = ord('A')
single[ord('I') - ord_A] = 1
single[ord('V') - ord_A] = 5
single[ord('X') - ord_A] = 10
single[ord('L') - ord_A] = 50
single[ord('C') - ord_A] = 100
single[ord('D') - ord_A] = 500
single[ord('M') - ord_A] = 1000

class Solution:
    def romanToInt(self, s: str, idx: int = 0) -> int:
        l = len(s)
        if idx >= l:
            #print()
            return 0
        roman = s[idx]
        if (l - idx) >= 2:
            if (prefix := double.get(roman + s[idx + 1], 0)):
                return prefix + self.romanToInt(s, idx + 2)
        #return single[roman] + self.romanToInt(s[1:])
        return single[ord(roman) - ord_A] + self.romanToInt(s, idx + 1)

class Solution_nonlookup:
    def romanToInt(self, s: str) -> int:
        # Amazingly, I thought the _lookup version would be way faster
        # but actually this _nonlookup version is slightly faster
        # than the all-dictionary _lookup version
        if not (l := len(s)):
            #print()
            return 0
        roman = s[0]
        if roman == 'M':
            #print(1000, '+', s[1:])
            return 1000 + self.romanToInt(s[1:])
        if roman == 'D':
            #print(500, '+', s[1:])
            return 500 + self.romanToInt(s[1:])
        if roman == 'C':
            if l == 1:
                #print(100)
                return 100
            #print(-100 if s[1] in ['M','D'] else 100)
            return (-100 if s[1] in ['M','D'] else 100) + self.romanToInt(s[1:])
        if roman == 'L':
            #print(50, '+', s[1:])
            return 50 + self.romanToInt(s[1:])
        if roman == 'X':
            if l == 1:
                #print(10)
                return 10
            #print(-10 if s[1] in ['C','L'] else 10)
            return (-10 if s[1] in ['C','L'] else 10) + self.romanToInt(s[1:])
        if roman == 'V':
            #print(5, '+', s[1:])
            return 5 + self.romanToInt(s[1:])
        if s == "IV":
            #print(4)
            return 4
        elif s == "IX":
            #print(9)
            return 9
        else:
            #print(l)
            return l

if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip().strip('"')):
            break
        print('romanToInt("' + line + '") returned',
              Solution_nonlookup().romanToInt(line))
