#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:10:44 2025

@author: Ham Nguyen

This is an example of how to use groupby() to group consecutive lines based
on the number of words (or tokens) in each line. (All blank lines are ignored.)

Problem:
Convert input to dict-of-dict

Input to parse:
Device: soc
        Ta000
            Instant: 29.17 deg C
            Max    : 45.76 deg C
        Ta001
            Instant: 28.59 deg C
            Max    : 44.96 deg C
Device: pmu
        TDIE_BUCK0
            Instant: 28.17 deg C
        TDIE_BUCK1
            Instant: 27.53 deg C
Device: pmu2
        TDEV7
            Instant: 24.91 deg C
        TDEV8
            Instant: 24.62 deg C
Device: clvr
        temp_a0_buck0
            Instant: 28.93 deg C
        temp_a1_buck0
            Instant: 26.88 deg C

Output:
{
    "clvr": {
        "temp_a0_buck0": {
            "Instant": "28.93"
        },
        "temp_a1_buck0": {
            "Instant": "26.88"
        },
    },
    "pmu": {
        "TDIE_BUCK0": {
            "Instant": "28.17"
        },
        "TDIE_BUCK1": {
            "Instant": "27.53"
        },
    },
    "pmu2": {
        "TDEV7": {
            "Instant": "24.91"
        },
        "TDEV8": {
            "Instant": "24.62"
        },
    },
    "soc": {
        "Ta000": {
            "Instant": "29.17",
            "Max": "45.76"
        },
        "Ta001": {
            "Instant": "28.59",
            "Max": "44.96"
        },
    }
}
"""

from typing import Dict, Iterator, List
import itertools
import re
import json

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


# 1.Before grouping, split a multiline string s into list of lines:
#   s.strip().splitlines(): strip leading+trailing spaces, then split to lines[]
#   if l.strip(): remove empty in-between lines
#   l.strip().split(): tokenize each line to list of tokens
#   lst = [['Device:', 'soc'], ['Ta000'], ['Instant:', '29.17', 'deg', 'C'], ...]
# 2.The outer groupby_list_len() groups consecutive sublists based on their lengths.
#   Since only the "outer header" in each group has its len(['Device:', 'blah'])==2,
#   the "for outer_k" loop would receive the following outer-tuples in sequence:
#     ('soc',  [['Ta000'],          ['Instant:', ...], ['Max', ...], ...,
#               ['Ts014'],          ['Instant:', ...], ['Max', ...]
#              ])
#     ('pmu',  [['TDIE_BUCK0'],     ['Instant:', ...], ...,
#               ['TDEV8'],          ['Instant:', ...]
#              ])
#     ('pmu2', [['TDIE_BUCK0'],     ['Instant:', ...], ...,
#               ['TDEV8'],          ['Instant:', ...]
#              ])
#     ('clvr', [['temp_a0_buck0'],  ['Instant:', ...], ...,
#               ['temp_b2_buck0'],  ['Instant:', ...]
#              ])
# 3.For each outer-tuple above, the inner groupby_list_len() groups
#   the 2nd element of each outer-tuple based on their lengths.
#   Since only the "inner header" in each group has its len(['Ta000']) == 1,
#   the "for inner_k" loop would receive the following inner-tuples in sequence:
#     outer_k='soc':
#       ('Ta000',           [['Instant:', ...], ['Max', ...]])
#       ...
#       ('Ts014',           [['Instant:', ...], ['Max', ...]])
#     outer_k='pmu':
#       ('TDIE_BUCK0',      [['Instant:', ...]])
#       ...
#       ('TDEV8',           [['Instant:', ...]])
#     outer_k='pmu2':
#       ('TDIE_BUCK0',      [['Instant:', ...]])
#       ...
#       ('TDEV8',           [['Instant:', ...]])
#     outer_k='clvr':
#       ('temp_a0_buck0',   [['Instant:', ...]])
#       ...
#       ('temp_b2_buck0',   [['Instant:', ...]])
# 4.From the 2nd element of each inner-tuple; e.g. [['Instant:', ...], ['Max', ...]],
#   then from the 1st (or only) sublist; e.g. ['Instant:', '51.28', 'deg', 'C'],
#   form a dictionary with:
#  4a.  Key is the 1st element (with the ending ':' stripped off) = 'Instant'
#  4b.  Value is the 2nd element (temperature) = '51.28'
#  4c.  New dictionary: dct = {'Instant': '51.28'}
# 5.And if the inner-tuple's 2nd-element has more than 1 sublists,
#   then from the 2nd sublist; e.g. ['Max', ':', '45.76', 'deg', 'C'],
#   form a {key: value} pair:
#  5a.  Key is the 1st element = 'Max'
#  5b.  Value is the 3rd element (temperature) = '45.76'
#  5c.  Add/update the dictionary in step #4 with: {'Max': '45.76'}
# 6.For each outer_k, and inner_ iteration, yield a tuple to the caller as:
#       ('soc',  'Ta000',           {'Instant': '29.17', 'Max': '45.76'})
#       ...           
#       ('soc',  'Ts014',           {'Instant': '27.59', 'Max': '34.93'})
#       ('pmu',  'TDIE_BUCK0',      {'Instant': '28.17'})
#       ...           
#       ('pmu',  'TDEV8',           {'Instant': '-20.19'})
#       ...           
#       ('clvr', 'temp_b2_buck0',   {'Instant': '28.01'})
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


# Re-implement groupby_list_len() but NOT using itertools.groupby()
def groupby_list_len_alt(lst: List, list_len: int) -> Iterator[Dict]:
    left_elem  = None
    right_list = []
    for l in lst:
        if len(l) == list_len:
            if left_elem or right_list:
                yield (left_elem, right_list)

            left_elem  = l[-1]
            right_list = []

        else:
            right_list.append(l)

    if left_elem or right_list:
        yield (left_elem, right_list)


def groupby_groupby_alt(s: str, outer_header_len, inner_header_len: int) -> Iterator[Dict]:
    lst = [l.strip().split() for l in s.strip().splitlines() if l.strip()]
    #print(*lst, sep='\n')
    for outer_k, itr in groupby_list_len_alt(lst, outer_header_len):
        #print(f'outer_k="{outer_k}", itr={list(itr)}')
        for inner_k, itr2 in groupby_list_len_alt(itr, inner_header_len):
            lst = list(itr2)
            #print(f'\t\tinner_k="{inner_k}", lst={len(lst)}#{lst}')
            dct = {lst[0][0][:-1]: lst[0][1]}
            if len(lst) > 1:
                dct.update({lst[1][0]: lst[1][2]})
            #print(f'outer_k="{outer_k}",\tinner_k="{inner_k}", dct={len(dct)}#{dct}')
            yield (outer_k, inner_k, dct)

def dict2_of_group_alt(s, outer_header_len, inner_header_len: int):
    dct = {}
    for outer_k, inner_k, entry in groupby_groupby_alt(s, outer_header_len, inner_header_len):
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
    #print(json.dumps(dct1, sort_keys=True, indent=4))

    dct2 = dict2_of_group(multiline_str, 2, 1)
    #print(json.dumps(dct2, sort_keys=True, indent=4))

    dct2_alt = dict2_of_group_alt(multiline_str, 2, 1)
    print(json.dumps(dct2_alt, sort_keys=True, indent=4))
    #print(dct2_alt)
