#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:17:35 2020

@author: ham.nguyen

Burger King promo: calculate the promo code below for some meal deals:
    -sum( (-1)^n * sqrt( 5! * 5 / 4!) ) for i = 1..461

Don't really need to use Python but just for showing off list comprehension.
Inside the sqrt() is always 25, so that results in 5 after sqrt'ing.
The -1^n flip-flops between -1 and +1
So the series is always [-5 5 -5 5 ...]
For an even number of terms, the sum is 0, since pairs of terms cancel each other.
So for an odd number of terms, the sum is always -5 as the left-over.

"""

import math
print(-sum([(-1)**i * int(math.sqrt((math.factorial(5) * 5)/math.factorial(4)))
            for i in range(1, 462)]))