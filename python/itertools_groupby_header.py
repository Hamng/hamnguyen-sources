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
Device: subsy1
        X_sensor_0
            Instant: 29.17 deg C
            Max    : 45.76 deg C
        X_sensor_1
            Instant: 28.59 deg C
            Max    : 44.96 deg C
Device: s_sys6
        tdb_0
            Instant: 28.17 deg C
        tdb_1
            Instant: 27.53 deg C
Device: s_sys1
        tv7
            Instant: 24.91 deg C
        tv8
            Instant: 24.62 deg C
Device: subsys2
        x_temp0
            Instant: 28.93 deg C
        x_temp1
            Instant: 26.88 deg C

Output:
{
    "subsys2": {
        "x_temp0": {
            "Instant": "28.93"
        },
        "x_temp1": {
            "Instant": "26.88"
        },
    },
    "s_sys6": {
        "tdb_0": {
            "Instant": "28.17"
        },
        "tdb_1": {
            "Instant": "27.53"
        },
    },
    "s_sys1": {
        "tv7": {
            "Instant": "24.91"
        },
        "tv8": {
            "Instant": "24.62"
        },
    },
    "subsy1": {
        "X_sensor_0": {
            "Instant": "29.17",
            "Max": "45.76"
        },
        "X_sensor_1": {
            "Instant": "28.59",
            "Max": "44.96"
        },
    }
}
"""

from typing import Dict, Iterator, List, Tuple
import itertools
import re
import json
#from shell import run


def groupby_list_len(lst: List, list_len: int) -> Tuple[str, List]:
    """
    From the given list-of-lists lst, and list_len, group consecutive
    sublists based on their length, then yield a tuple on succesive calls.

    Parameters
    ----------
    lst : List
        The list-of-lists to be grouped based on list_len.
    list_len : int
        Length to group the sublists

    Yields
    ------
    Tuple[str, List]
        [0]: last element of the last sublist whose len(l) == list_len
        [1]: iterator to the remaining sublists whose length doesn't match

    Examples
    --------
    list_len==1 for all examples
    1. Normal: lst = [[a], [b, c], [d, e, f], [g, h], [i], [j, k]]
        (a, [[b, c], [d, e, f], [g, h]])
        (i, [[j, k]])
    2. Ok: lst = [[a], [b], [c], [d, e, f], [g, h], [i], [j, k]]
        (c, [[d, e, f], [g, h]])
        (i, [[j, k]])
    3. Ok list_len==2: lst = [[a, b], [c, d], [e], [f, g, h], [i, j, k]]
        (d, [[e], [f, g, h], [i, j, k]])
    4. ERROR: lst = [[a, b, c], [d, e, f], [g, h], [i], [j, k]]
        (None, [[a, b, c], [d, e, f], [g, h]])
        (i, [[j, k]])
    5. Dropped: lst = [[a], [b, c], [d, e, f], [g, h], [i], [j], [k]]
        (a, [[b, c], [d, e, f], [g, h]])
        Dropped: [i], [j], [k]

    """
    # Must init outer_k=None here to handle the case when there're some
    # unmatched lists before the very 1st list whose len(l) == list_len
    # In that case, the 1st yield will yield (None, iterator)
    outer_k = None
    itr = itertools.groupby(lst, lambda l: len(l) == list_len)
    for k, grp in itr:
        #print(f"['{k}', <", *list(grp), "> ]")
        if k:
            #l = next(grp)
            #print(f' {k}: {len(l)}#{l}')
            # There could be many consecutive matches;
            # e.g. [["Device:", "subsy1"], ["Device:", "subsys2"]], or [["X_sensor_1"], ["V_sensr_14"]]
            # So pick the last element of the last list; e.g. "subsys2", or "V_sensr_14"
            #outer_k = next(grp)[-1]
            outer_k = list(grp)[-1][-1]
        else:
            #l = list(grp)
            #print(f'{list_len}#{outer_k}: {l}')
            #yield (outer_k, l)
            yield (outer_k, grp)

    # An alternative to Example #5:
    # 1.Before the "for" loop, init: k = False
    # 2.Here, end of "for" loop:
    #if k:
    #    yield (outer_k, [])
    # 3.That changes example #5 to:
    # 5.ERROR: lst = [[a], [b, c], [d, e, f], [g, h], [i], [j], [k]]
    #       (a, [[b, c], [d, e, f], [g, h]])
    #       (k, [])


def split_by_outer_header(a_str: str, pattern: str) -> Tuple[str, str]:
    """
    Split a multiline string then yield each substring as a tuple

    Parameters
    ----------
    a_str : str
        A string to be splitted
    pattern : str
        Pattern to split a_str

    Yields
    ------
    Tuple[str, str]
        [0]: 1st token of each substring
        [1]: remainder of a substring

    Examples
    --------
    1. a_str="Dev: subsy1 1 2 3\nDev: s_sys6 4 5\nDev: subsys2 6 7 8 9"
    2. re.split("Dev:", a_str) -> [" subsy1 1 2 3\n", " s_sys6 4 5\n", " subsys2 6 7 8 9"]
    3. In the "for" loop: e = e.strip() -> e = "subsy1 1 2 3"
    4. e.split(' ', 1) -> l = ["subsy1", "1 2 3"]
    5. Successive calls will yield:
        ("subsy1", "1 2 3")
        ("s_sys6", "4 5")
        ("subsys2", "6 7 8 9")

    """
    for e in re.split(pattern, a_str, re.MULTILINE):
        e = e.strip()
        if e:
            l = e.split(' ', 1)
            #print(l)
            #yield (l[0].strip(), [e1.strip() for e1 in l[1].strip().splitlines()])
            yield (l[0].strip(), l[1].strip())
        else:
            # Handle the corner cases:
            # a. pattern is at the begin of a_str, with 0 or more whitespaces
            #    preceding it; e.g. a_str="Dev: ...", or a_str="   Dev: ..."
            # b. pattern is at the end   of a_str, with 0 or more whitespaces
            #    following it; e.g. a_str="... Dev:", or a_str="... Dev:  "
            continue


def parse_level2_value(list_of_lists: Iterator) -> Dict:
    """
    Parse the given list-of-lists to return a Dict

    Parameters
    ----------
    list_of_lists : Iterator
        A list-of-list to parse

    Returns
    -------
    Dict: which could be either:
        {'ERROR': '...'}
        {'WARN*': '...'}
        {'Instant': 'value'}
        {'Instant': 'value', 'Max': 'value'}

    Steps:
     1. E.g. list_of_list = [['Instant:', '29.17', 'deg', 'C'], ['Max', ':', '45.76', ...]]
     2. From the 1st sublist of itr, extract its 1st word; i.e. 'Instant:'
     3. If it starts with either 'ERROR' or 'WARN', form a new dict with an entry:
            Key: 1st word in all CAPS, stripped off ':' ==> 'ERROR' or 'WARN*'
            Value: joining the remaining words of the 1st sublist
     4. Else, form a new dict with an entry:
            Key: 1st sublist, 1st word;     e.g. {'Instant':    (stripped off ':')
            Value: 1st sublist, 2nd word;   e.g.            '29.17'}
     5. If >1 sublists, update the newly formed dict in #4 with an entry:
            Key: 2nd sublist, 1st word;     e.g. {'Max':
            Value: 2nd sublist, 3rd word;   e.g.       '45.76'}
     6. Return the formed dict

    """
    #for l1_key, l1_value in ...:
    #   for l2_key, l2_value in ...:
    #       yield l1_key, l2_key, parse_level2_value(l2_value)
    lst = list(list_of_lists)
    word0 = lst[0][0]
    #print(f'word0="{word0}", lst={len(lst)}#{lst}')
    if word0.upper().startswith('ERROR') or word0.upper().startswith('WARN'):
        dct = {word0.upper().strip(':'): ' '.join(lst[0][1:])}
    else:
        dct = {word0.strip(':'): lst[0][1]}
        if len(lst) > 1:
            dct.update({lst[1][0]: lst[1][2]})
    #print(f'word0="{word0}", dct={len(dct)}#{dct}')
    return dct


def split_groupby(s: str, outer_header: str, inner_header_len: int) -> Tuple[str, str, Dict]:
    for outer_k, v in split_by_outer_header(s, outer_header):
        itr = (l.strip().split() for l in v.splitlines())
        #print(f'outer_k="{outer_k}", itr={list(itr)}')
        #itr = (l.strip().split() for l in v.splitlines())
        for inner_k, inner_v in groupby_list_len(itr, inner_header_len):
            yield outer_k, inner_k, parse_level2_value(inner_v)


def dict1_of_group(s, outer_header: str, inner_header_len: int) -> Dict:
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
#   lst = [['Device:', 'subsy1'], ['X_sensor_0'], ['Instant:', '29.17', 'deg', 'C'], ...]
# 2.The outer groupby_list_len() groups consecutive sublists based on their lengths.
#   Since only the "outer header" in each group has its len(['Device:', 'blah'])==2,
#   the "for outer_k" loop would receive the following outer-tuples in sequence:
#     ('subsy1',  [['X_sensor_0'],  ['Instant:', ...], ['Max', ...], ...,
#                  ['V_sensr_14'],  ['Instant:', ...], ['Max', ...]
#                 ])
#     ('s_sys6',  [['tdb_0'],       ['Instant:', ...], ...,
#                  ['tv8'],         ['Instant:', ...]
#                 ])
#     ('s_sys1',  [['tdb_0'],       ['Instant:', ...], ...,
#                  ['tv8'],         ['Instant:', ...]
#                 ])
#     ('subsys2', [['x_temp0'],     ['Instant:', ...], ...,
#                  ['s_temp2'],     ['Instant:', ...]
#                 ])
# 3.For each outer-tuple above, the inner groupby_list_len() groups
#   the 2nd element of each outer-tuple based on their lengths.
#   Since only the "inner header" in each group has its len(['X_sensor_0']) == 1,
#   the "for inner_k" loop would receive the following inner-tuples in sequence:
#     outer_k='subsy1':
#       ('X_sensor_0',  [['Instant:', ...], ['Max', ...]])
#       ...
#       ('V_sensr_14',  [['Instant:', ...], ['Max', ...]])
#     outer_k='s_sys6':
#       ('tdb_0',       [['Instant:', ...]])
#       ...
#       ('tv8',         [['Instant:', ...]])
#     outer_k='s_sys1':
#       ('tdb_0',       [['Instant:', ...]])
#       ...
#       ('tv8',         [['Instant:', ...]])
#     outer_k='subsys2':
#       ('x_temp0',     [['Instant:', ...]])
#       ...
#       ('s_temp2',     [['Instant:', ...]])
# 4.Parse the inner values; e.g. [['Instant:', ...], ['Max', ...]]
# 5.Successively, yield:
#       ('subsy1',  'X_sensor_0',   {'Instant': '29.17', 'Max': '45.76'})
#       ...           
#       ('subsy1',  'V_sensr_14',   {'Instant': '27.59', 'Max': '34.93'})
#       ('s_sys6',  'tdb_0',        {'Instant': '28.17'})
#       ...           
#       ('s_sys6',  'tv8',          {'Instant': '-20.19'})
#       ...           
#       ('subsys2', 's_temp2',      {'Instant': '28.01'})
def groupby_groupby(s: str, outer_header_len, inner_header_len: int) -> Tuple[str, str, Dict]:
    lst = [l.strip().split() for l in s.strip().splitlines() if l.strip()]
    #print(*lst, sep='\n')
    for outer_k, itr in groupby_list_len(lst, outer_header_len):
        #print(f'outer_k="{outer_k}", itr={list(itr)}')
        for inner_k, inner_v in groupby_list_len(itr, inner_header_len):
            yield outer_k, inner_k, parse_level2_value(inner_v)


def dict2_of_group(s, outer_header_len, inner_header_len: int) -> Dict:
    dct = {}
    for outer_k, inner_k, entry in groupby_groupby(s, outer_header_len, inner_header_len):
        if outer_k in dct:
            dct[outer_k].update({inner_k: entry})
        else:
            dct[outer_k] =      {inner_k: entry}

    return dct


# Same as groupby_list_len() but NOT using itertools.groupby()
# Except for example #5:
#   5. ERROR: lst = [[a], [b, c], [d, e, f], [g, h], [i], [j], [k]]
#       (a, [[b, c], [d, e, f], [g, h]])
#       (k, [])
def groupby_list_len_alt(lst: List, list_len: int) -> Tuple[str, List]:
    # Must init left_elem=None here to handle the case when there're some
    # unmatched lists before the very 1st list whose len(l) == list_len
    # In that case, the 1st yield will yield (None, iterator)
    left_elem  = None
    right_list = []
    for l in lst:
        if len(l) == list_len:
            if right_list:
                # If in the middle of multiple consecutive matches,
                # don't yield anything since right_list was set to []
                # after the 1st match of a series of consecutive matches.
                # e.g. unmatched, match1, yield, match2, match3
                # Also, see note below
                yield (left_elem, right_list)

            left_elem = l[-1]

            # Since right_list=[] on each match, effectively, only the last
            # element of the LAST match (before the 1st unmatched) is kept
            # e.g. [["Device:", "subsy1"], ["Device:", "subsys2"]], or [["X_sensor_1"], ["V_sensr_14"]]
            # Only "subsys2", or "V_sensr_14" is kept for the next yield
            right_list = []

        else:
            # Accumulate the list of unmatches
            right_list.append(l)

    if left_elem or right_list:
        # a.If both are boolean True: yield the last match(es), together with
        #   the ending accumulation of unmatches => normal case.
        # b.If only left_elem is boolean True: no unmatched following the last match(es).
        #   Most likely an error case.
        # c.If only right_list is boolean True: entire lst unmatched => error
        yield (left_elem, right_list)


def groupby_groupby_alt(s: str, outer_header_len, inner_header_len: int) -> Tuple[str, str, Dict]:
    lst = [l.strip().split() for l in s.strip().splitlines() if l.strip()]
    #print(*lst, sep='\n')
    for outer_k, itr in groupby_list_len_alt(lst, outer_header_len):
        #print(f'outer_k="{outer_k}", itr={list(itr)}')
        for inner_k, inner_v in groupby_list_len_alt(itr, inner_header_len):
            yield outer_k, inner_k, parse_level2_value(inner_v)


def dict2_of_group_alt(s, outer_header_len, inner_header_len: int) -> Dict:
    dct = {}
    for outer_k, inner_k, entry in groupby_groupby_alt(s, outer_header_len, inner_header_len):
        if outer_k in dct:
            dct[outer_k].update({inner_k: entry})
        else:
            dct[outer_k] =      {inner_k: entry}

    return dct


def out_of_range_check(dct: Dict, key: str, minval: float, maxval: float, bad_keys: Tuple = []):
    """
    Iterate thru the given dict-of-dict dct, yield a tuple if there's a bad
    keyname (iff bad_keys is given), or if the specified key is out-of-range

    Parameters
    ----------
    dct : Dict
        A dict-of-dict to be iterated.
    key : str
        Key containing a float value.
    minval: float
        Minimum value to compare against.
    maxval: float
        Maximum value to compare against.
    bad_keys : Tuple, optional
        A tuple of bad keys

    Yields
    ------
    Tuple: if bad_key, or out-of-range:
        [0]: level-1 key
        [1]: level-2 key
        [2]: key that's in-error
        [3]: if out-of-range, will be a float value; else, a string

    """
    for l1_key, l1_value in dct.items():
        #print(f"l1_key={l1_key}, l1_value={l1_value}")
        for l2_key, l2_value in l1_value.items():
            #print(f'l2_key="{l2_key}"')
            for b_key in bad_keys:
                if b_key in l2_value:
                    yield (l1_key, l2_key, b_key, l2_value[b_key])
                    break
            else:
                # Got here if completing the "for" loop normally;
                # i.e. did NOT "break", hence NOT finding a bad_key
                value = l2_value.get(key)
                if value:
                    value = float(value)
                    if (value < minval) or (value > maxval):
                        yield (l1_key, l2_key, key, value)


if __name__ == '__main__':
    multiline_str = """Device: subsy1
        X_sensor_0
            Instant: 29.17 deg C
            Max    : -45.76 deg C
        X_sensor_1
            Instant: 28.59 deg C
            Max    : 44.96 deg C
        V_sensr_10
            Instant: 28.14 deg C
            Max    : 36.85 deg C
        V_sensr_11
            Instant: 28.56 deg C
            Max    : 35.17 deg C
        V_sensr_12
            Instant: 28.32 deg C
            Max    : 38.93 deg C
        V_sensr_13
            Instant: 27.98 deg C
            Max    : 10036.93 deg C
        V_sensr_14
            Instant: 27.59 deg C
            Max    : 34.93 deg C
Device: s_sys6
        tdb_0
            Instant: 28.17 deg C
        tdb_1
            Instant: 27.53 deg C
        tdb_2
            Instant: 27.85 deg C
        tdb_3
            Instant: 28.01 deg C
        tdb_4
            Instant: 28.73 deg C
        tv2
            Instant: -20.15 deg C
        tv3
            Instant: 26.88 deg C
        tv4
            Instant: -20.16 deg C
        tv5
            Instant: -20.16 deg C
        tv6
            Instant: -20.19 deg C
        tv7
            Instant: -20.21 deg C
        tv8
            Instant: -20.19 deg C
Device: s_sys1
        tdb_0
            Instant: 25.97 deg C
        tdb_1
            Instant: 25.81 deg C
        Tdl_DO16_20
            Instant: 27.65 deg C
        Tds_W1
            Instant: 27.09 deg C
        Tds_W3
            Instant: 26.65 deg C
        Tcl
            Instant: 51.28 deg C
        tv1
            Instant: 24.46 deg C
Device: wrn_dev
        wrn_sensor
WARNING: Can't initialize the Gas Gauge HAL.
?
Error getting value from the sensor: Device Error^^malformed: missing <CR>^^Device: next_device
        tv7
            Instant: 24.91 deg C
        tv8
            Instant: 24.62 deg C
Device: subsys2
        x_temp0
            Instant: 28.93 deg C
        x_temp1
            Instant: 26.88 deg C
        err_temp1
ERROR: Timed out updating Thermal Sensor xx
ERROR: Time out: Failed to get Temperature SnapShot
ERROR: Failed to get sensor data for err_temp1

        s_temp1
            Instant: 28.33 deg C
        x_temp2
            Instant: 28.01 deg C
        s_temp2
            Instant: 28.01 deg C"""

    dct1 = dict1_of_group(multiline_str, "Device:", 1)
    #print('dct1 =', json.dumps(dct1, sort_keys=True, indent=4))

    dct2 = dict2_of_group(multiline_str, 2, 1)
    #print('dct2 =', json.dumps(dct2, sort_keys=True, indent=4))

    #multiline_str = run("temperature --all", True)
    dct2_alt = dict2_of_group_alt(multiline_str, 2, 1)
    print('dct2_alt =', json.dumps(dct2_alt, sort_keys=True, indent=4))
    # MicroPython json.dumps() doesn't do much, so use print()
    #print('dct2_alt =', dct2_alt)

    # Detect error only
    #for tupl in out_of_range_check(dct2_alt, None, None, None, ['ERROR', 'WARNING']):
    #    if not isinstance(tupl[-1], float):
    #        print(f"\n{tupl[0]}::{tupl[1]}: " + ' '.join(tupl[2:]))

    temp_min = 0.0
    temp_max = 120.0
    for tupl in out_of_range_check(dct2_alt, 'Instant', temp_min, temp_max, ['ERROR', 'WARNING']):
        #print(tupl)
        if isinstance(tupl[-1], float):
            print(f"{tupl[0]}::{tupl[1]}.{tupl[2]}={tupl[-1]:.2f} out-of-range [{temp_min:.1f}, {temp_max:.1f}]")
        else:
            print(f"\n{tupl[0]}::{tupl[1]}: " + ' '.join(tupl[2:]))

    print('\n')
    for tupl in out_of_range_check(dct2_alt, 'Max', temp_min, temp_max):
        #print(tupl)
        if isinstance(tupl[-1], float):
            print(f"{tupl[0]}::{tupl[1]}.{tupl[2]}={tupl[-1]:.2f} out-of-range [{temp_min:.1f}, {temp_max:.1f}]")
