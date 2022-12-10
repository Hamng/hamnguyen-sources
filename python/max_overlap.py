#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:04:00 2021

@author: Ham

Splunk Interview Question

Giving a list-of-lists:
    lst = [[s0,e0], [s1,e1], [s2,e2], ..., [sN,eN]]
Each inner list has 2 elements representing a time interval,
such that sX <= eX.
The time intervals are in random order, and could overlap.
Problem: find the maximum number of overlaps


"""

def process_1_interval(dct, start, end):
    for time in range(start, end+1):
        if time in dct:
            dct[time] += 1
        else:
            dct[time] = 1

if __name__ == '__main__':
    # obtain lst[] somehow
    dct = dict()
    for start, end in lst:
        process_1_interval(dct, start, end)

    print(max(dct.values()))
