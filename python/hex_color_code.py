# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:15:08 2019

@author: Ham

HackerRanch Challenge: Hex Color Code

CSS colors are defined using a hexadecimal (HEX) notation
for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F.
■ A-F letters can be lower case. (a-f are also valid digits).

Examples

Valid Hex Color Codes
#FFF
#025
#F0A1FB

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff

You are given N lines of CSS code.
Your task is to print all valid Hex Color Codes,
in order of their occurrence from top to bottom.

CSS Code Pattern

Selector
{
	Property: Value;
}

Input Format

The first line contains N, the number of code lines.
The next N lines contains CSS Codes.

Constraints



Output Format

Output the color codes with '#' symbols on separate lines.

Sample Input (see STDIN_SIO below)

Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

Explanation

#BED and #Cab satisfy the Hex Color Code criteria,
but they are used as selectors and not as color codes in the given CSS.

Hence, the valid color codes are:

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

Note: There are no comments ( // or /* */) in CSS Code.

"""

import re
import io

STDIN_SIO = io.StringIO("""
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
""".strip())


if __name__ == '__main__':
    #for _ in range(int(input())):
    #    l = map(lambda x: x[0], re.findall(r"[^#]+(#([\da-f]{6}|[\da-f]{3}))",
    #                                       input(), flags=re.I))
    for _ in range(int(STDIN_SIO.readline().strip())):
        l = map(lambda x: x[0], re.findall(r"[^#]+(#([\da-f]{6}|[\da-f]{3}))",
                                           STDIN_SIO.readline().strip(), flags=re.I))
        [print(e) for e in l]
