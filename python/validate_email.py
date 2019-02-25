# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:36:13 2019

@author: Ham

HackerRanch Challenge: Validating Email Addresses With a Filter

Task

You are given an integer N followed by N email addresses.
Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3.

Input Format

The first line of input is the integer N, the number of email addresses.
N lines follow, each containing a string.

Constraints

Each line is a non-empty string.

Output Format

Output a list containing the valid email addresses in lexicographical order.
If the list is empty, just output an empty list, [].

Sample Input

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

import io
#import string
import re

STDIN_SIO = io.StringIO("""
8
brian-23@hackerrank.com
britts_54@hackerrank.com
its@gmail.com1
mike13445@yahoomail9.server
rase23@ha_ch.com
daniyal@gmail.coma
thatisit@thatisit
lara@hackerrank.com
""".strip())


def fun(s):
    """doc"""
    if s.count('@') != 1:
        return False

    user, web = s.split('@')

    if not user or re.search(r"[^A-Za-z0-9_\-]", user):
        return False

    if web.count('.') != 1:
        return False

    site, ext = web.split('.')
    #print("user=<" + user + ">", "site=<" + site + ">", "ext=<" + ext + ">")

    return not bool(re.search(r"[^A-Za-z0-9]", site)) and (len(ext) < 4)

def filter_mail(emails):
    """doc"""
    return list(filter(fun, emails))

if __name__ == '__main__':
    #emails = [input() for _ in range(int(input()))]
    emails = [STDIN_SIO.readline().strip()
              for _ in range(int(STDIN_SIO.readline().strip()))]
    #print(emails)
    print(sorted(filter_mail(emails)))
