# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:29:19 2019

@author: Ham

Task from HackerRank
Given a string , which is the company name in lowercase letters,
your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line
and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.
"""

if __name__ == '__main__':
    s = "szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgba"\
        "kpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukc"\
        "vyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni"
    #s = input()
    occ = {}
    [occ.update({c: occ.get(c, 0)+1}) for c in s]
    #for c in s:
    #    occ.update({c: occ.get(c, 0) + 1})
    print(s)
    print(occ)
    occ_sorted = sorted(occ.items(), key=lambda x: x[1] * 1000 - ord(x[0]),
                        reverse=True)
    print(occ_sorted)
    [print(x[0], x[1]) for x in occ_sorted[:3]]
