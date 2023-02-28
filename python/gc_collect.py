#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:49:40 2023

@author: Ham Nguyen

Source: a question from Apple #help-python Slack:

Good Morning/Afternoon. I have an interesting observation with numpy on my M1 Mac.
I have a toy program.

and I am noticing that after gc the memory of arr is not being freed?
The same program works fine on Linux i.e the memory goes down after GC.
Does anyone know why this is happening on Mac or am I looking at the wrong thing here?

# Mac (observed)
❯ python3 test.py
before deletion 176582656
after deletion and gc 177532928

# Linux (expected)
$ python3 test.py
before deletion 37294080
after deletion and gc 29294592

"""

import gc
from time import sleep

import numpy as np
from psutil import Process


def main() -> None:
    arr = np.arange(1_000_000)
    print("before deletion", Process().memory_info().rss)
    del arr
    gc.collect()
    sleep(5)
    print("after deletion and gc", Process().memory_info().rss)


if __name__ == "__main__":
    main()