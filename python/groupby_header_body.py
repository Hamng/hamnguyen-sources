#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:20:45 2022

@author: smartlab
"""

from typing import List, Dict
import itertools

def list_of_header_or_body(multiline_str, header_prefix: str) -> List:
    lst = [l.strip() for l in multiline_str.strip().splitlines() if l.strip()]
    #print(lst)
    itr = itertools.groupby(lst, lambda s: s.startswith(header_prefix))
    for elem in itr:
        #print(i, elem[0])
        if elem[0]:
            yield next(elem[-1]).split(' ', 1)
        else:
            l2 = [s.split(' ', 1) for s in elem[-1]]
            yield [l2[0][0], [e[-1] for e in l2]]

def dict_of_group(multiline_str, header_prefix: str) -> Dict:
    for i, elem in enumerate(list_of_header_or_body(multiline_str, header_prefix)):
        k, v = elem
        #print(i, k, elem)
        if k == header_prefix:
            dct = {k[:-1].lower(): v}
        else:
            dct.update({k[:-1].lower() + "s": v})
            yield dct


if __name__ == '__main__':
    multiline_str = """



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


"""

    res = [d for d in dict_of_group(multiline_str, "Node:")]
    print(res)
