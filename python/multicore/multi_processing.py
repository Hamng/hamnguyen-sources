#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://urban-institute.medium.com/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba
Using Multiprocessing to Make Python Code Faster
"""
import time
import multiprocessing

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    y = x*x
    time.sleep(100)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(100):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print('That took {} seconds'.format(time.time() - starttime))
