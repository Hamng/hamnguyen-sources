#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:20:45 2022

@author: Ham Nguyen

This is an example of how to use groupby() to group consecutive lines based
on the 1st token in each line. (All blank lines are ignored.)

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

from typing import Dict, Iterator, List
import itertools
import re
import json

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
#
def groupby_list_len(lst: List, list_len: int) -> Iterator[Dict]:
    itr = itertools.groupby(lst, lambda l: len(l) == list_len)
    for k, grp in itr:
        #print(f"['{k}', <", *list(grp), "> ]")
        if k:
            #l = next(grp)
            #print(f' {k}: {len(l)}#{l}')
            outer_k = next(grp)[-1]
        else:
            #print(f'{outer_k}: {list(grp)}')
            yield (outer_k, grp)

def split_by_outer_header(a_str, header: str) -> Iterator[Dict]:
    for e in re.split(header, a_str, re.MULTILINE):
        if e:
            l = e.strip().split(' ', 1)
            #print(l)
            #yield (l[0].strip(), [e1.strip() for e1 in l[1].strip().splitlines()])
            yield (l[0].strip(), l[1].strip())
        else:
            continue

def split_groupby(s, outer_header: str, inner_header_len: int) -> Iterator[Dict]:
    for outer_k, v in split_by_outer_header(s, outer_header):
        itr = (l.strip().split() for l in v.splitlines())
        #print(f'outer_k="{outer_k}", itr={list(itr)}')
        #itr = (l.strip().split() for l in v.splitlines())
        for inner_k, itr2 in groupby_list_len(itr, inner_header_len):
            lst = list(itr2)
            #print(f'\t\tinner_k="{inner_k}", lst={len(lst)}#{lst}')
            dct = {lst[0][0][:-1]: lst[0][1]}
            if len(lst) > 1:
                dct.update({lst[1][0]: lst[1][2]})
            #print(f'outer_k="{outer_k}",\tinner_k="{inner_k}", dct={len(dct)}#{dct}')
            yield (outer_k, inner_k, dct)

def dict1_of_group(s, outer_header: str, inner_header_len: int):
    dct = {}
    for outer_k, inner_k, entry in split_groupby(s, outer_header, inner_header_len):
        if outer_k in dct:
            dct[outer_k].update({inner_k: entry})
        else:
            dct[outer_k] =      {inner_k: entry}

    return dct


def groupby_groupby(s: str, outer_header_len, inner_header_len: int) -> Iterator[Dict]:
    lst = [l.strip().split() for l in s.strip().splitlines() if l.strip()]
    #print(*lst, sep='\n')
    for outer_k, itr in groupby_list_len(lst, outer_header_len):
        #print(f'outer_k="{outer_k}", itr={list(itr)}')
        for inner_k, itr2 in groupby_list_len(itr, inner_header_len):
            lst = list(itr2)
            #print(f'\t\tinner_k="{inner_k}", lst={len(lst)}#{lst}')
            dct = {lst[0][0][:-1]: lst[0][1]}
            if len(lst) > 1:
                dct.update({lst[1][0]: lst[1][2]})
            #print(f'outer_k="{outer_k}",\tinner_k="{inner_k}", dct={len(dct)}#{dct}')
            yield (outer_k, inner_k, dct)

def dict2_of_group(s, outer_header_len, inner_header_len: int):
    dct = {}
    for outer_k, inner_k, entry in groupby_groupby(s, outer_header_len, inner_header_len):
        if outer_k in dct:
            dct[outer_k].update({inner_k: entry})
        else:
            dct[outer_k] =      {inner_k: entry}

    return dct



if __name__ == '__main__':
    multiline_str = """Device: soc
        Ta000
            Instant: 29.17 deg C
            Max    : 45.76 deg C
        Ta001
            Instant: 28.59 deg C
            Max    : 44.96 deg C
        Ts010
            Instant: 28.14 deg C
            Max    : 36.85 deg C
        Ts011
            Instant: 28.56 deg C
            Max    : 35.17 deg C
        Ts012
            Instant: 28.32 deg C
            Max    : 38.93 deg C
        Ts013
            Instant: 27.98 deg C
            Max    : 36.93 deg C
        Ts014
            Instant: 27.59 deg C
            Max    : 34.93 deg C
Device: pmu
        TDIE_BUCK0
            Instant: 28.17 deg C
        TDIE_BUCK1
            Instant: 27.53 deg C
        TDIE_BUCK2
            Instant: 27.85 deg C
        TDIE_BUCK3
            Instant: 28.01 deg C
        TDIE_BUCK4
            Instant: 28.73 deg C
        TDEV2
            Instant: -20.15 deg C
        TDEV3
            Instant: 26.88 deg C
        TDEV4
            Instant: -20.16 deg C
        TDEV5
            Instant: -20.16 deg C
        TDEV6
            Instant: -20.19 deg C
        TDEV7
            Instant: -20.21 deg C
        TDEV8
            Instant: -20.19 deg C
Device: pmu2
        TDIE_BUCK0
            Instant: 25.97 deg C
        TDIE_BUCK1
            Instant: 25.81 deg C
        TDIE_LDO16_20
            Instant: 27.65 deg C
        TDIE_SW1
            Instant: 27.09 deg C
        TDIE_SW3
            Instant: 26.65 deg C
        TCAL
            Instant: 51.28 deg C
        TDEV1
            Instant: 24.46 deg C
        TDEV7
            Instant: 24.91 deg C
        TDEV8
            Instant: 24.62 deg C
Device: clvr
        temp_a0_buck0
            Instant: 28.93 deg C
        temp_a1_buck0
            Instant: 26.88 deg C
        temp_b1_buck0
            Instant: 28.33 deg C
        temp_a2_buck0
            Instant: 28.01 deg C
        temp_b2_buck0
            Instant: 28.01 deg C"""

    dct1 = dict1_of_group(multiline_str, "Device:", 1)
    #print(dct1)
    print(json.dumps(dct1, sort_keys=True, indent=4))

    dct2 = dict2_of_group(multiline_str,  2, 1)
    #print(json.dumps(dct2, sort_keys=True, indent=4))
