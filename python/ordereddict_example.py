# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:40:54 2019

@author: Ham

HackerRanch Challenge: OrderedDict

Task

You are the manager of a supermarket.
You have a list of N items together with their prices
that consumers bought on a particular day.
Your task is to print each item_name and net_price
in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Constraints


Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input (see stdin_sim below)

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

"""

import collections

stdin_sim = """
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    sold = collections.OrderedDict()
    #for _ in range(int(input())):
    #    *items, amt = input().split()
    for _ in range(int(stdin_sim.pop(0))):
        *items, amt = stdin_sim.pop(0).split()
        k = " ".join(items)
        if k in sold:
            sold[k] += int(amt)
        else:
            sold[k] = int(amt)

    [print(k, v) for k, v in sold.items()]
