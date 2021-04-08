# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:00:03 2021

@author: Ham
Facebook Interview Question

Given a list of (lowercase only) words, see if they're "in order"
according to a given ordering of (lowercase) alphabets.

Assumption: all chars are in the ordering.

But bonus: if a char isn't in the ordering, return out-of-order immediately

"""

import random
import string
import io

STDIN_SIO = io.StringIO("""
abcd
abdeg
whatever
you
said
""".strip())

def in_order_2(a: str, b: str, order: str) -> bool:
    for ca, cb in zip(a, b):
        if ca == cb:
            continue
        if (cai := order.find(ca)) < 0:
            return False
        if (cbi := order.find(cb)) < 0:
            return False
        return cai < cbi
    return len(a) <= len(b)

def in_order(words: list, order: str) -> bool:
    for cur, nxt in zip(words, words[1:]):
        #print(cur, nxt)
        if not in_order_2(cur, nxt, order):
            print('"' + cur + '"', 'and "' + nxt + '"', "are not in order")
            return False
    return True

if __name__ == '__main__':
    order = list(string.ascii_lowercase)
    random.shuffle(order)
    order = ''.join(order)
    order = 'acwys'
    print(order)

    words = list(map(str.strip, STDIN_SIO.readlines()))
    print(words)
    print(in_order(words, order))