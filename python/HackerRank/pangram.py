# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:38:07 2021

@author: Ham

HackerRank > Practice > Algorithms > Strings
Pangrams

Problem

A pangram is a string that contains every letter of the alphabet.
Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case.
Return either "pangram" or "not pangram" as appropriate.

Example

The string contains all letters in the English alphabet, so return "pangram".

Function Description

Complete the function pangrams in the editor below.
It should return the string "pangram" if the input string is a pangram.
Otherwise, it should return "not pangram".

pangrams has the following parameter(s):

string s: a string to test
Returns

string: either "pangram" or "not pangram"
Input Format

A single line with string .

Constraints


Each character of ,

Sample Input

Sample Input 0

We promptly judged antique ivory buckles for the next prize

Sample Output 0

pangram

Sample Explanation 0

All of the letters of the alphabet are present in the string.

Sample Input 1

We promptly judged antique ivory buckles for the prize

Sample Output 1

not pangram

Sample Explanation 0

The string lacks an x.

"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys
import string

import io

# Test case 8: Expected Output: pangram
STDIN_SIO = io.StringIO("""
WwmdRukNYPMFBxYFPVtZrzs FAktokrLtdPyVRWCyqSHaqjttuhYNXpwnzwoXDC AdKRP AWwEamzQlOT EweNHXGkYrgJJwzErXvkiYIGOK goZXDYecGz oPHaxcZZC Z ktcXTnPFeuPQgQqoJS LZtk nOA zXc QyDseEIHVueKlgZVcQhgc hNHCQJS NXqvz EIOrqfPcBaXHDmWCHKMufyLXBQPVROdnlWDICRO qUNaVNP I fJAoEK saAnGbE pXvQW nd bitUAdJoIkbhPkwiKVUxpgV NsDCpwztiCXliMHrOEicnEsVc uIiai hLRqwFVeeHQzXXqVgUmNcqc TdHCztGUXwnzFGIPdYNZhfFKPQuUI ynSWARRzzwlRlzL JxsljNx YGfagQnP g VMImbbBNiOjNqtFb ODtQK DxNIfqggIzXgP eGMS kcnelJ kOTAG tSwcSlyMp xVjLZigPdsR yilXJyDa SKGOj yWEROeKfnPE iSFZwHPj ZPwKdllGxEdtpKwTMcB Yuus JgyWdYHj snl HrFqRgVDgVPAh X PBRAkR EwpdMYrlgI QKUnRBfKLwV yXKKGbMkIRIYN dqzaYvIQM vt yvuaGntYHEgEJb TNoPvslu htYlZXayqTlcNclvSOoMyfiTWehzhs W wanyMaAYijgxubvDINMlqHblbjLSJCvCpfvqaWHy qwG lLciwkkuu o NoSTWbytadyGuTRznISvCQhFMtrdqveTmcc mcKNPGowUGBLPmONplkUwZeu N p apQLbHLFSIt vkOcFlSMYZdaZy PzfbRPLTHy gAFo PLRItTAOfuWITfyIzUBc F GEXzyMZHXRpnpxQ NV Cl PIBRgkNNKQTVgGkTNbojQqm VvomeAxXDppIWm I KqyX CTA nt JTSsOH M mKzfGwsT LjXPVYzcJFdVWqkFRNm
We promptly judged antique ivory buckles for the next prize
""".strip())


# Complete the pangrams function below.
def pangrams(s):
    return "pangram" if len({c.lower() for c in s if c.isalpha()}) == len(string.ascii_lowercase) else "not pangram"

    # Above is a 1-liner solution
    # Below uses the old-fashioned "for" loop which might return prematurely
    st = set(string.ascii_lowercase)
    for c in s:
        c = c.lower()
        if c in st:
            st.remove(c)
            if not len(st):
                return "pangram"
    return "not pangram"


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #s = input()

    s = STDIN_SIO.readline()

    result = pangrams(s)

    print(result)

    #fptr.write(result + '\n')
    #fptr.close()
