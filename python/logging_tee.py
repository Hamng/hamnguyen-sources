#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:14:38 2020

@author: ham.nguyen

Experiment with logging and 'tee'

VERY IMPORTANT:
    Spyder/IPython messes up logging (e.g. messages not shown in desired format)
    Woraround: import+reload logging before everything else.
    Sigh, reload isn't a builtin for Python 3, so need to import from importlib

"""

import logging
from importlib import reload
reload(logging)
#logger = logging.getLogger(__name__)

import sys
import os
#from IPython.utils.io import Tee
from contextlib import closing


if __name__ == '__main__':

    # Problem: for each run within Spyder/IPython, a log entry would be
    #   dup'ed; e.g. 1st run, it shows up once; 2nd: it shows up twice;
    #   Nth run: N times; till restarting the kernel.
    #   No such problem when running stand-alone outside Spyder.
    # Cause: in Spyder, there're lots of log handlers pre-added, then for
    #   each run, our handler here will be addHandler()'ed again, hence dup
    # Fix: clear logging.Logger.manager.loggerDict
    #print(logging.Logger.manager.loggerDict.keys())
    #logging.Logger.manager.loggerDict = {}

    #logging.getLogger('some').setLevel(level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG,
                        stream=sys.stdout,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('[%s %s] %s: %s', 'nvme0n1', 'randwrite', 'RUN_x',
                 'just an info')
    logging.debug('and this is a debug')
    logging.warning('how about this warning')

    #print('This is not in the output file.')        

    #with closing(Tee("outputfile.log", "w", channel="stdout")) as outputstream:
    #    print('a std print')
    #    logging.info('logging to both stdout and logfile')

    # raise Exception('The file "outputfile.log" is closed anyway.')
    logging.warning('warning to stdout only')
