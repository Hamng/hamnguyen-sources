# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:19:40 2019

@author: Ham

This program displays the DRs and BDRs in a network per an algorithm
specified in an Arrcus interview (for employment).
    1.  With my insufficient understanding of DR and BDR in network
        routing, I'm simplifying this assignment to become a problem
        of multi-key sorting of a (complicated) structure.
    2.  I'm focused on getting it to work in a simple way,
        so didn't optimize it for performance.
    3.  The selection of fields or criteria to be sorted might be fuzzy;
        however, it's flexible enough to change easily.
    4.  Same goes for the sorting order as well as asc/descending.


Assumptions about the 'network' object:
    0.  It should simply be a dict instead of a list of dicts,
        but I'm staying true to the original assignment.
    1.  All keys and values are valid.
    2.  Keys for id are unique.
    3.  No missing or dangling connections.
    4.  Link-state are consistent.
    5.  No missing keys; i.e. 'type' and 'connections' must exist for all,
        and 'loopback' and 'priority' must also exist for 'router'

"""

import sys
import json
from operator import itemgetter


def get_nodes_by_id(ntwrk, nodeid):
    """
    Return a dictionary of nodes (in ntwrk) whose key matches the
    given 'nodeid'. (Ideally, we shouldn't even need this function;
    if ntwrk is a simple dict, then simply return {nodeid: ntwrk[nodeid]}.)
    """
    return {k: v for el in ntwrk
                  for k, v in el.items() if k == nodeid}

def get_nodes_by_type(ntwrk, typ='switch'):
    """
    Return a dictionary of nodes (in ntwrk) whose 'type' matches 'typ'.
    """
    return {k: v for el in ntwrk
                  for k, v in el.items() if v['type'] == typ}

def get_nodes_by_id_type_connect_to(ntwrk, swtch, nodeid, typ='router'):
    """
    Locate a node matching 'nodeid', verify that its type is 'typ',
    then locate a connection to 'swtch',
    then return a tuple of attributes that will be used for sorting.
    If not found, return an empty tuple.
    """
    for k, v in get_nodes_by_id(ntwrk, nodeid).items():
        if v['type'] == typ:
            for conn in v['connections']:
                if conn['to'] == swtch:
                    return (v['priority'], k,
                            v['loopback'], conn['other-port'])
    return ()

def get_dr_bdr(ntwrk, swtch, val):
    """
    Return a tuple of (DR, BDR) (Designated Router, and Backup)
    for the given 'swtch' in the 'ntwrk'
    """
    # For all connections from 'swtch' whose link-state are 'up',
    # form a list of tuples of routers connecting to 'swtch'
    # with appropriate attributes for sorting next.
    lst = [get_nodes_by_id_type_connect_to(ntwrk, swtch, c['to'])
           for c in val['connections'] if c['link-state'] == 'up']
    # Filter out empty elements
    lst = [e for e in lst if e]
    #print(lst)

    # Per Python doc on multi-key sorting, we'd 1st sort the list
    # by the most minor key, then finally by the primary key
    # ("Sorting HOW TO", "Sort Stability and Complex Sorts")
    lst.sort(key=itemgetter(3))                 # ascending by 'port'
    #print(lst)
    lst.sort(key=itemgetter(2))                 # ascending by 'loopback'
    #print(lst)
    lst.sort(key=itemgetter(1), reverse=True)   # descending by 'id'
    #print(lst)
    lst.sort(key=itemgetter(0))                 # ascending by 'priority'
    #print(lst)
    return (lst[0][1], lst[1][1])

def select_dr_bdr(ntwrk):
    """
    In the given 'ntwrk', return a dictionary of switches and their
    corresponding DR and BDR.
    """
    res = {}
    for swtch, val in get_nodes_by_type(ntwrk).items():
        #print(swtch)
        #print(val)
        res.update({swtch: get_dr_bdr(ntwrk, swtch, val)})
    return res

if __name__ == '__main__':
    network = json.load(sys.stdin)
    for swch, dr_bdr in select_dr_bdr(network).items():
        print("Switch: '%s': DR is '%s', BDR is '%s'"
              % (swch, dr_bdr[0], dr_bdr[1]))
