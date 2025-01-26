#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:36:18 2025

@author: Gino Ledesma from Apple Slack #help-python

$ time /bin/bash -c "python ./numpy_linalg_inv_dot.py"
done

real	1m44.590s
user	17m11.456s
sys	0m19.627s

$ time /bin/bash -c "OMP_NUM_THREADS=1 python ./numpy_linalg_inv_dot.py"
done

real	12m40.400s
user	12m25.752s
sys	0m12.657s

"""

import numpy as np

# Creating very large arrays
arr1 = np.random.rand(20000, 20000)
arr2 = np.random.rand(20000, 20000)

# Performing lots of math that should utilize multiple cores
result = np.dot(np.linalg.inv(arr1), arr2)

print("done")
