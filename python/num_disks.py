# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:31:29 2020

@author: Ham
Source: programming question from HCL Technologies interview

Write a NumDisk class with constructor and member function

"""

class NumDisks(object):
    def __init__(self, num_disks):
        if num_disks in [2,4,8]:
            self.num_disks = num_disks
        else:
            raise Exception("invalid constructor arg: " + str(num_disks))

    def get_num_disks(self):
        return self.num_disks

if __name__ == '__main__':
    # Valid cases
    print(NumDisks(2).get_num_disks())
    print(NumDisks(4).get_num_disks())
    print(NumDisks(8).get_num_disks())

    # invalid cases
    try:
        inv1 = NumDisks(5)
        print(inv1.get_num_disks())
    except Exception as e:
        print(e)

    try:
        inv2 = NumDisks('abc')
        print(inv2.get_num_disks())
    except Exception as e:
        print(e)
