# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:29:10 2020

@author: Ham
"""

def locate(ar, target):
    lft = 0
    rgt = len(ar) - 1
    while lft <= rgt:
        mid = (lft + rgt) // 2
        if ar[mid] == target:
            return mid
        if target < ar[mid]:
            rgt = mid - 1
        else:
            lft = mid + 1
    return -1

    #for i,e in enumerate(ar):
    #    if e == target:
    #        return i
    return -1

ar = range(11, 34)
print('locate([],', 20, 'found at', locate(ar, 20))
print('locate([],', 10, 'found at', locate(ar, 10))
print('locate([],', 50, 'found at', locate(ar, 50))
print('locate([],', 11, 'found at', locate(ar, 11))
print('locate([],', 33, 'found at', locate(ar, 33))
print('locate([],', 21, 'found at', locate(ar, 21))
print('locate([],', 22, 'found at', locate(ar, 22))
print('locate([],', 23, 'found at', locate(ar, 23))
print('locate([],', 24, 'found at', locate(ar, 24))

