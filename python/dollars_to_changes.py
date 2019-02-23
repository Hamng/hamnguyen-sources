# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK

def dollars_to_changes(dollars, dollar_vals):
    """Given a dollars amount (e.g. $8.74), and a list of dollar_values
    in descending values (e.g. [5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]),
    return a list of tuples of changes.
    E.g. [(5, 1), (1, 3), (0.5, 1), (0.1, 2), (0.01, 4)]
    """
    cents = int(dollars * 100)
    res = []
    for value in dollar_vals:
        cval = int(value * 100)
        n, cents = divmod(cents, cval)
        if n != 0:
            res += [(value, n)]

    return res


# Main program starts here
dollar_values = [5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
changes = dollars_to_changes(8.74, dollar_values)
#print(changes)

coins_to_str = {
        5: '$5 bill',
        1: '$1 bill',
        0.50: 'half-dollar',
        0.25: 'quarter',
        0.10: 'dime',
        0.05: 'nickel',
        0.01: 'penny'}

for coins in changes:
    coin_str = coins_to_str[coins[0]]
    if coins[1] > 1:
        coin_str = coin_str + "s" if coins[0] != 0.01 else "pennies"
    print(coins[1], coin_str, end=", ")
