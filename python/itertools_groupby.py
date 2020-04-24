#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:06:17 2020

@author: ham.nguyen

An iterator to return sublists from a list based on a condition.

My son's homework: given a (flat) list of names and their integer grades,
print the non-lastnames as a string, and the corresponding grade.
Each 'name' consists of a firstname, then a lastname as 2 individual
string elements. Then, between first and last, there could be 0-to-N
middle names also as individual string elements.

Input Format

The first line contains an N representing how many lines follow.
The next N lines each contains portions of names, then ends with an integer for grade.

Constraints
Input format is properly formed. Except the 1st line, each other line contains:
    .  At least 2 elements.
    .  Only the last element is an integer (representing a grade).
    .  No other element is an integer.

Here's providing 2 implementations using and not using itertools.groupby

"""

import itertools
import io

STDIN_SIO = io.StringIO("""
6
f11 f12 f13 l1 1
f2 l2 2
f31 f32 l3 3
f41 f42 f43 f44 l4 4
f51 f52 l5 5
f6 6
""".strip())


def sublist_iterator_groupby(lst, pred):
    """
    Partition a list into sublists with each sublist ends and contains
    the element whose predicate(element) == True. (This is almost like
    itertools.takewhile(lst, not pred), but appending the matched elem.)
    Each sublist is yielded as succesive calls to the returned iterator.
    This function implements using itertools.groupby()

    Parameters
    ----------
    lst : list
        The list to be partitioned.
    pred : function
        To apply to each elem of a sublist, then end a sublist when
        this predicate returns True.

    Yields
    ------
    list
        A sublist (from list) such that pred(all_except_last) == False,
        followed by pred(last) == True

    Notes
    -----
    .groupby() groups consecutive elems in lst based on pred(elem):
    [(False, iterator_to_list_of_elems_where_pred_returns_False),
     (True , iterator_to_list_of_elems_where_pred_returns_True ),
                 ...
     (False, iterator_to_list_of_elems_where_pred_returns_False),
     (True , iterator_to_list_of_elems_where_pred_returns_True )
     ]
    We pop 2 consecutive tupples from the .groupby() iterator at a time.
    Basicly, we concatenate the 2nd elem in both tupples then yield the
    concatenation. But since both 2nd elems are iterators, we need to
    convert both to lists before concatenating then yielding.
    Why the 'if not tupl[0]'?
    To ensure we'd start out with pred(elem) == False;
    i.e. skipping over initial consecutive elems whose pred(elem) == True.
    Why the complicated 2nd term in the yield expression?
    next(itr)[1] is iterator-to-list of trailing elems whose pred(elem)==True.
    If >1, we only want to return the first, hence next(next(itr)[1]) to pop
    it out, then [next(next())] to make it a single-elem list before appending.
    This is done to match the behavior of sublist_iterator() below.

    """
    itr = itertools.groupby(lst, pred)
    for tupl in itr:
        if not tupl[0]:
            #yield list(tupl[1]) + list(next(itr)[1])
            #flst = list(tupl[1])
            # VERY IMPORTANT: must process tupl *BEFORE* next(itr)
            #tlst = list(next(itr)[1])
            #print('flst:', flst, type(flst))
            #print('tlst:', tlst, type(tlst), ', [0]:', tlst[0])
            #yield flst + [tlst[0]]
            yield list(tupl[1]) + [next(next(itr)[1])]


def sublist_iterator(lst, pred):
    """
    Partition a list into sublists with each sublist ends and contains
    the element whose predicate(element) == True.
    Each sublist is yielded as succesive calls to the returned iterator.
    This function is an alternate implementation WITHOUT using itertools.

    Parameters
    ----------
    lst : list
        The list to be partitioned.
    pred : function
        To apply to each elem of a sublist, then end a sublist when
        this predicate returns True.

    Yields
    ------
    list
        A sublist (from list) such that pred(all_except_last) == False,
        followed by pred(last) == True

    Notes
    -----
    Init the sublist_to_be_yielded to empty.
    Copy elems one at at time from the input list to the yield sublist.
    till and including pred(elem) == True.
    Then yield the sublist.
    Once coming back for the next iteration, re-init the yield sublist to empty.
    What's the skip_matched stuff?
    To ensure we'd start out with pred(elem) == False;
    i.e. skipping over initial consecutive elems whose pred(elem) == True.
    Also, for consecutive elems whose pred(elem) == True, keep only the 1st.

    """
    ylst = []
    skip_matched = True
    for elem in lst:
        if skip_matched:
            if pred(elem):
                continue
            else:
                skip_matched = False
        if type(elem) is list:
            ylst.extend(elem)
        else:
            ylst.append(elem)
        if pred(elem):
            yield ylst
            ylst = []
            skip_matched = True


def process(fname, lst):
    """
    Process a list of names and grades per the problem statement

    Parameters
    ----------
    fname : funcname
        Name of a function to return an iterator.
    lst : list
        The list to be processed.

    Returns
    -------
    None.

    """
    for sublist in fname(lst, lambda e: type(e) is int):
        #print(sublist)
        # Strip off lastname which is 2nd from last,
        # then join the non-lastname to 1 string with spaces.
        # Making it a list in case needing to process further, or return
        # Alternately, can simply do: del(sublist[-2])
        # len(sublist) < 3 means no lastname, so returning as-is
        if len(sublist) < 3:
            l2 = sublist
        else:
            l2 = [' '.join(sublist[:-2]), sublist[-1]]
        print(l2)


if __name__ == '__main__':
    lst = []
    #inlist = [input().split() for i in range(int(input()))]
    for _ in range(int(STDIN_SIO.readline().strip())):
        *names, grade = STDIN_SIO.readline().strip().split()
        # so names[] sucks up all elems except the last one; which grade claims
        #print(names, int(grade))
        # Sigh, we could complete the hw here if wanting to by:
        #lst.append([' '.join(names[:-1]), int(grade)])
        lst.extend(names)
        lst.append(int(grade))

    # Malformed lists to verify error handling
    #lst = []                                           # empty list
    #lst = [11, 12, 13] + lst                           # initial elems are ints
    #lst = ['f1', 'l1', 1, 2, 3, 'f2', 'l2', 2]         # consecutive ints
    #print(lst)

    #process(sublist_iterator, lst)
    process(sublist_iterator_groupby, lst)
