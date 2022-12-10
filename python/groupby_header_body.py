#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:07:35 2022

@author: smartlab
"""

import itertools

multi_line_str = """Node: HomePod (2).local.
    Interface: en0
    Interface: awdl0
Node: HomePod.local.
    Interface: en0
    Interface: anpi0
    Interface: awdl0
    Interface: lo0"""

lst = multi_line_str.splitlines()
itr = itertools.groupby(lst, lambda s: s.startswith('Node: '))

res = []
for idx, elem in enumerate(itr):
    #print(idx, elem[0])     # , list(elem[-1]))
    if elem[0]:
        k, v = next(elem[-1]).split(' ', 1)[:]
        dct = {k[:-1]: v}
        #print(f"k='{k}', v=<{v}>, dct=<{dct}>")
    else:
        for intf in elem[1]:
            k, v = intf.strip().split(' ', 1)[:]
            k = k[:-1]
            if k in dct:
                dct[k].append(v)
            else:
                dct.update({k: [v]})
        res.append(dct)
    #print(f"{idx}: dct={dct}")

print(res)