#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:20:45 2022

@author: Ham Nguyen

Problem:
Hi all, I have a command line tool that outputs a multi-line string
and I’d like to parse it into a dict. Anyone have a nice way of doing so?
Input to parse:
Node: HomePod (2).local.
    Interface: en0
    Interface: awdl0
Node: HomePod.local.
    Interface: en0
    Interface: anpi0
    Interface: awdl0
    Interface: lo0
Output:
[{"node": "HomePod (2).local.", "Interfaces": ["en0", "awdl0"]},
 {"node": "HomePod.local.", "Interfaces": ["en0", "anpi0", "awdl0", "lo0"]}]

"""

from typing import List, Dict
import itertools

#
# 1. Before grouping, split a multiline string into list of lines:
#    .strip().splitlines(): strip leading and trailing spaces
#    if l.strip(): remove empty inner lines
# 2. groupby() groups consecutive lines based on matched/unmatched such that:
#    [[True , [list of consecutive   matched lines]],
#     [False. [list of consecutive unmatched lines]],
#           ...
#     [True , [list of consecutive   matched lines]],
#     [False, [list of consecutive unmatched lines]]]
# 3. Iterate thru elem yielded by groupby()
# 4. If matched (e.g. elem[0]==True): use only the 1st matched line, split at the
#    1st space, then yield as a list ['header_prefix', 'remainder of 1st matched line']
# 5. If not matched (e.g. elem[0]==False):
#    a. Split each unmatched lines at the 1st space to produce a list-of-lists
#       l2 = [['Interface:', 'en0'], ['Interface:', 'anpi0'], ['Interface:', 'awdl0']]
#    b. Assuming the 1st element of each inner list are the same, so use l2[0][0]
#    c. And compose a list of all 2nd elements of the inner list => ['en0', 'anpi0', 'awdl0']
#    d. Yield a list from b and c: ['Interface:', ['en0', 'anpi0', 'awdl0']]
def list_of_header_or_body(multiline_str, header_prefix: str) -> List:
    lst = [l.strip() for l in multiline_str.strip().splitlines() if l.strip()]
    #print(*lst, sep='\n')
    itr = itertools.groupby(lst, lambda s: s.startswith(header_prefix))
    for elem in itr:
        #print(i, elem[0])
        if elem[0]:
            yield next(elem[-1]).split(' ', 1)
        else:
            l2 = [s.split(' ', 1) for s in elem[-1]]
            yield [l2[0][0], [e[-1] for e in l2]]


def dict_of_group(multiline_str, header_prefix: str) -> Dict:
    # Init dct() to handle malformed body lines that aren't preceded by a header line
    dct = {}
    for k, v in list_of_header_or_body(multiline_str, header_prefix):
        #k, v = elem
        #print(i, k, elem)
        if k == header_prefix:
            # Strip ':' at the end of k, then convert it lowercase. Then create a new dct
            dct = {k[:-1].lower(): v}
        else:
            # Strip ':' at the end of k, then convert it lowercase. then append "s"
            # Then update to the existing dct.
            # Then yield dct
            dct.update({k[:-1].lower() + "s": v})
            yield dct


if __name__ == '__main__':
    multiline_str = """

    Interface: malformed,
        Interface: NOT preceded by
      Interface: a Node: line

  Node: HomePod (2).local.
   Interface: en0
      Interface: awdl0
    
Node: HomePod.local.
Node: bug, these lines will be ignored
Node:      since being fold into the 'header'
     Node:   whatever

    Interface: en0
       Interface: anpi0
    Interface: awdl0
  Interface: lo0

  Node: malformed, NOT followed by an Interface: line

"""

    res = [d for d in dict_of_group(multiline_str, "Node:")]
    print(*res, sep='\n')
