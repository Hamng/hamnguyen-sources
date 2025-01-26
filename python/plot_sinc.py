# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:20:23 2020

@author: Ham

A trivial sample plot using NumPy and Matplotlib.
If running inside Jupyter, and to show the plot inline,
prepend at the beginning:
    
%matplotlib inline

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 100)
y = np.sinc(x)
plt.plot(x, y)