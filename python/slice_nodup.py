# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:04:19 2019

@author: Ham

HackerRanch Challenge: Merge The Tools

Consider the following:

A string, s, of length n.
An integer, k, where k is a factor of n.
We can split s into n/k subsegments
where each subsegment, t, consists of a contiguous block of k characters in s.
Then, use each t to create string u such that:

The characters in u are a subsequence of the characters in t.
Any repeat occurrence of a character is removed from the string
such that each character in u occurs exactly once.
In other words, if the character at some index j in t
occurs at a previous index < j in t,
then do not include the character in string u.

Given s and k, print n/k lines where each line i denotes string u.

Input Format

The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.

Constraints

n, where n is the length of s
It is guaranteed that n is a multiple of k.

Output Format

Print n/k lines where each line i contains string u.

Sample Input

AABCAAADA
3

Sample Output

AB
CA
AD

Explanation

String s is split into n/k = 9/3 = 3 equal parts of length k=3.
We convert each t to u by removing any subsequent occurrences
non-distinct characters in t:

We then print each u on a new line.

"""

import collections

def merge_the_tools(string, k):
    """doc"""
    f = "%." + str(k) + "s"
    l = [f % string[i:] for i in range(0, len(string), k)]
    #print(l)
    res = ["".join(collections.OrderedDict.fromkeys(e).keys()) for e in l]
    #print(res)
    [print(e) for e in res]

if __name__ == '__main__':
    #string, k = input(), int(input())
    merge_the_tools(input(), int(input()))
