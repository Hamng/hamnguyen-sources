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
#    l.strip().split(' ', 1): split at the 1st space
#    lst = [['Node:', 'foo'], ['Intf:', 'bar1'], ['Intf:', 'bar2'], ...]
# 2. groupby() groups consecutive inner lists based on the 1st elem of each inner list:
#    [['Node:'     , [list of consecutive inner lists whose 1st element is 'Node:'     ]],
#     ['Interface:', [list of consecutive inner lists whose 1st element is 'Interface:']],
#           ...
#     ['Node:'     , [list of consecutive inner lists whose 1st element is 'Node:'     ]],
#     ['Interface:', [list of consecutive inner lists whose 1st element is 'Interface:']]]
# 3. Iterate thru the elements yielded by groupby()
# 4. If the 1st element (k) matches; i.e. k == header_prefix:
#    a. next(grp): use only the 1st of the inner lists
#    b. next(grp)[1]: and only the 2nd element of that inner list.
#    c. Form a new dct from k, and 4b => dct = {'node': 'HomePod.local.'}
# 5. Else, if not matched:
#    a. For all inner lists (in grp)
#    b. (Assuming the 1st elements are all the same,)
#       Form a list of all 2nd elements => ['en0', 'anpi0', 'awdl0', 'lo0']
#    c. Update dct with a dict entry formed by k, and 5b
#    d. Yield dct: {'node': 'HomePod.local.', 'interfaces': ['en0', 'anpi0', 'awdl0', 'lo0']}
# 6. Caveat: header lines (at the end) NOT followed by body lines will be ignored.
#
def dict_of_group(multiline_str, header_prefix: str) -> Dict:
    lst = [l.strip().split(' ', 1) for l in multiline_str.strip().splitlines() if l.strip()]
    #print(*lst, sep='\n')
    itr = itertools.groupby(lst, lambda e: e[0])
    # Init dct() to handle malformed body lines that aren't preceded by a header line
    dct = {}
    for k, grp in itr:
        #print(f"['{k}', <", *list(grp), "> ]")
        if k == header_prefix:
            # Strip ':' at the end of k, then convert it lowercase. Then create a new dct
            dct = {k[:-1].lower(): next(grp)[1]}
        else:
            # Strip ':' at the end of k, then convert it lowercase. then append "s"
            # Then update to the existing dct.
            # Then yield dct
            dct.update({k[:-1].lower() + "s": [e[1] for e in grp]})
            yield dct


if __name__ == '__main__':
    multiline_str = """

    Interface: malformed,
        Interface: NOT preceded by
      Interface: a Node: line,
       Interface: but still form a dict

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

  Node: malformed, NOT followed by an Interface: line, will be ignored

"""

    res = [d for d in dict_of_group(multiline_str, "Node:")]
    print(*res, sep='\n')
