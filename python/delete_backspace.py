# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:44:22 2019

@author: Ham

(Java) Interview question from Samsung (from HackerRank)

Given an array of chars (of keys pressed), remove r"\b" and the preceding char.
Notes:
    1.  This is NOT the single backspace char ('\b'), but 2 consecutive
        chars: a backslash char ('\') followed by a 'b'
    2.  Must handle multiple occurrences of r"\b", might be adjacent.
    3.  Must handle (possibly multiple) r"\b" at the beginning of the array.
    4.  Must handle _excessive_ r"\b"; i.e. more r"\b" than avail chars.
    5.  No special treatment for other backslash-combo;
        i.e. treat them normally as 2 consecutive chars.
        e.g. r"\1\b2" => r"\2" (deleting "1")
             r"\\bA"  => r"A"  (deleting the first '\')

Input:
    1 line representing the keypress array
    (might contain leading and trailing spaces)

Output:
    The original input line
    Then the resulting line after processing r"\b"
"""

import re

def delete_backspace(s):
    print("%s" % s)
    leading_bs = re.compile(r"""^       # at begin of string
                                (       # group \1
                                 \\     # a literal backslash
                                 b      # then 'b'
                                )+      # 1-or-more occurences
                            """, re.VERBOSE)    # to document pattern
    #print("leading_bs<%s>" % leading_backspaces)
    s = re.sub(leading_bs, "", s)
    #print("-lead_bs<%s>" % s)

    non_lead_bs = re.compile(r"""
                                 .      # any single char
                                 \\     # a literal backslash
                                 b      # then 'b'
                             """, re.VERBOSE)   # to document pattern
    s, nsubs = re.subn(non_lead_bs, "", s, count=1)  # do only 1 sub
    #print("-char+bs<%s>" % s)
    while nsubs > 0:
        s = re.sub(leading_bs, "", s)
        #print("-lead_bs<%s>" % s)
        s, nsubs = re.subn(non_lead_bs, "", s, count=1)  # do only 1 sub
        #print("-char+bs<%s>" % s)
    print("%s" % s)

if __name__ == '__main__':
    #delete_backspace(input())
    delete_backspace(r"\1\b2: '1' removed")
    delete_backspace(r"\\bA: first '\' removed")
    delete_backspace(r"123\b\bABC: '23' removed bc consecutive bs")
    delete_backspace(r"\b\b\b  with lead\bDing bs A\bB and em\bMbedde\bEd some\b\b\bOMEwhere")
    delete_backspace(r"\b\b\b\b123456\b\b\b\b\b\b\b\b\b\bExtra bs removed")
