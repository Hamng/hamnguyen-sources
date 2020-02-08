# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 08:34:48 2020

@author: Ham

Self Challenge: Generator of Non-Blank Lines

Given a text file (or stdin), provide a generator that for each iteration,
produces a group of consecutive non-blank lines.
Side-effect: each line is stripped (of leading/trailing whitespaces).

Scoring: a solution needs to be a 1-liner;
i.e. NO point if implementing with a traditional 'for' loop!

Sample Input: self; i.e. this module

"""

import sys
import itertools


def non_blanks(infile=sys.stdin):

    """Explanation from the innermost:
        .readlines()    Read in *all* lines
        map(...)        Strip each line
        groupby()       Group consecutive lines based on emptiness:
            [[False, [list of empty lines]],
             [True , [list of non-empty lines]],
             [False, [list of empty lines]],
             [True , [list of non-empty lines]],
                     ...
             [False, [list of empty lines]]]
        Next, iterate thru the tuples returned by itertools.groupby(),
        if 1st elem of a tuple is True, then return its 2nd elem.
        Caveat: return each as a list(), else caller would need to do so.
    """

    return (list(t[1])
            for t in itertools.groupby(map(str.strip, infile.readlines()),
                                       lambda l: bool(len(l)))
            if t[0])



if __name__ == '__main__':

    for g, lines in enumerate(non_blanks(infile=open(__file__, 'r'))):
        print(g + 1, lines)

    print("\nTotal of", g + 1, "groups of non-blanks")
