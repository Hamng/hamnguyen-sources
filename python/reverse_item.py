# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:53:52 2020

@author: Ham
Source: programming question from HCL Technologies interview

Given the stand-alone fun1() below, what's the output?
"""

class MyDict(object):
    @staticmethod
    def fun1(k,v):
        return {k, v}


def fun1(cls, d, prefix=""): 
    values = {}
    for k, v in d.items():
        if isinstance(v, list):
            values.update(cls.fun1(v[0], prefix))
            print('list', 'k:', k, 'v:', v, 'values:', values)
        elif isinstance(v, dict):
            if prefix:
                _prefix = "%s%s_" % (prefix, k)
            else:
                _prefix = "%s_" % (k)
            values.update(cls.fun1(v, _prefix))
            print('dict', 'k:', k, 'v:', v, 'values:', values)
        else:
            values["%s%s" % (prefix, k)] = v
            print('neither', 'k:', k, 'v:', v, 'values:', values)
    return values

if __name__ == '__main__':
    Dict = {1: 'loop', 2: 'For', 3: {'A' : 'while', 'B' : 'To', 'C' : 'loop'}}
    res = fun1(MyDict, Dict)
    print(res)
