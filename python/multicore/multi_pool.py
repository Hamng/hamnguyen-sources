#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Ham Nguyen

"""

import sys
import os
import argparse
import logging
import time
import random
from multiprocessing import Pool

__VERSION__ = "0.2"

_secs_to_sleep = random.sample(range(1, 6), 1)[0]

def parse_command_line(description: str=None):
    """
    Parse command-line options.

    Args:
        description: self-explanatory

    Returns:
        The populated namespace args (from argparse.ArgumentParser().parse_args())
        so caller can access the command-line options as attributes of the namespace;
        e.g. as args.optname

    Notes:
     1. Use type= to validate argument (seems not required in non-darwin),
        so need to provide a valid type
     2. To capture ALL positional args that aren't preceded by an --optX:
            parser.add_argument("remainder", nargs='*', help="unparsed positional args")
            e.g. if sys.argv="--optX x a b --optY y c --optZ z d e f g"
                 args.remainder=(a, b, c, d, e, f, g)
        2b. If no unparsed positional args, here's a slight difference:
                nargs='*': args.remainder = []
                nargs='+': args.remainder = None
        2c. If there're many possible catchall --optX, then prefix each with '--' as usual,
            but on command-line, user MUST explicitly specify --optX before the list
     3. sys.argv[] remains intact after calling parser.parse_args()
    """
    global _secs_to_sleep

    parser = argparse.ArgumentParser(description = description)

    num_workers = Pool()._processes
    cnt = random.sample(range(15, 30), 1)[0]

    # --debug and --verbose are aliases
    parser.add_argument("--debug", "--verbose", action="store_true", default=False,
                        help=f"              If specified, set the loglevel to DEBUG to show more messages")
    parser.add_argument("--version", action="store_true", default=False,
                        help=f"              Show this script version='{__VERSION__}', then exit")
    parser.add_argument("--count", type=int, default=cnt,
                        help=f"              Number of elements in an iterable when calling map, default={cnt}")
    parser.add_argument("--workers", type=int, default=num_workers,
                        help=f"              Number of workers/processes (1: no parallel), default={num_workers}")
    parser.add_argument("--sleep", type=int, default=_secs_to_sleep,
                        help=f"              Seconds to sleep within each process, default={_secs_to_sleep}")
    parser.add_argument("--map", action="store_true", default=False,
                        help=f"              If specified, run the Map test, default=True")
    parser.add_argument("--starmap", action="store_true", default=False,
                        help=f"              If specified, run the Starmap test, default=False")

    # Let's parse it
    args = parser.parse_args()

    #if len(sys.argv) < 2:
    #    logging.error(f"{parser.prog}: Need at least 1 command-line arg")
    #    parser.print_help()
    #    sys.exit(0)

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        #logging.debug(f"args={args}")
        #logging.debug(f"parser={parser}")

    if args.version:
        logging.info(f" Version: '{__VERSION__}'")
        sys.exit(0)

    _secs_to_sleep = args.sleep

    logging.debug(f"Workers: spawn Pool(processes={args.workers})")
    logging.debug(f"  Count: {args.count} elements to map")
    logging.debug(f"  Sleep: {_secs_to_sleep} secs in each worker function\n")

    return args

def zip_len(cnt: int, *iterables):
    """Return an iterator for cnt items from zip(*iterables)
        (This is equivalent to list(zip(*iterables))[:cnt]
        but WON'T waste time zipping ALL items, then toss away from [cnt:])
        This iterator zip(*iterables) but STOPs when cnt exhausts
    """
    itr = zip(*iterables)
    for _ in range(cnt):
        yield itr.__next__()


def square(x: int) -> int:
    """Calculates the square of a number."""
    global _secs_to_sleep

    time.sleep(_secs_to_sleep)          # Sleep a while to simulate some work
                                        # to be done within each process
    return x * x

def multiply2(arg1, arg2):
    """Multiplies two numbers."""
    global _secs_to_sleep

    time.sleep(_secs_to_sleep)          # Sleep a while to simulate some work
                                        # to be done within each process
    return arg1 * arg2


def test_map(num_workers: int=None, num_elements: int=None, min_int: int=5, scale: int=4):
    """
        Sample output:
% python ./multi_pool.py --sleep 2 --map --d --count 11
DEBUG: Workers: spawn Pool(processes=10)
DEBUG:   Count: 11 elements to map
DEBUG:   Sleep: 2 secs in each worker function

INFO: ==============================    Map Test    ==============================
INFO:  Numbers: 11#[18, 30, 40, 27, 19, 25, 17, 36, 47, 34, 5]
INFO:  Squares: 11#[324, 900, 1600, 729, 361, 625, 289, 1296, 2209, 1156, 25]
INFO:  Runtime: 5.3 seconds
    """
    # To make the list non-consecutive and non-repeating random values,
    # shuffle() a much longer list of Nx values, then keep only the first 1x values
    #numbers = list(range(min_int, min_int + (4 * num_elements)))
    #random.shuffle(numbers)
    #numbers = numbers[:num_elements]
    # Best: 1-liner below
    #numbers = random.sample(range(min_int, max_int + 1), num_elements)
    # Cons of using 'max_int': if num_elements too large, .sample() will fail,
    # so would need to increase 'max_int' to accomodate.
    # So using >1 'scale' to control how wide the spread from 'min_int'
    numbers = random.sample(range(min_int, min_int + (scale * num_elements)), num_elements)
    logging.info(('=' * 30) + "    Map Test    " + ('=' * 30))
    logging.info(f" Numbers: {len(numbers)}#{numbers}")
    start_time = time.time()
    with Pool(processes=num_workers) as pool:
        results = pool.map(square, numbers)
        logging.info(f" Squares: {len(results)}#{results}")
    logging.info(f" Runtime: {time.time() - start_time:.1f} seconds\n")

def test_starmap(num_workers: int=None, num_elements: int=None, min_int: int=5, scale: int=4):
    """
% python ./multi_pool.py --sleep 2 --starmap --d --count 11
DEBUG: Workers: spawn Pool(processes=10)
DEBUG:   Count: 11 elements to map
DEBUG:   Sleep: 2 secs in each worker function

INFO: ==============================    Starmap Test    ==============================
INFO:    Pairs: 11#[(5, 39), (39, 15), (13, 27), (36, 46), (46, 43), (15, 29), (27, 30), (29, 31), (43, 13), (31, 5), (30, 36)]
INFO: Multiply: 11#[195, 585, 351, 1656, 1978, 435, 810, 899, 559, 155, 1080]
INFO:  Runtime: 5.3 seconds
    """
    left_nums = random.sample(range(min_int, min_int + (scale * num_elements)), num_elements)
    right_nums = left_nums[:]
    random.shuffle(right_nums)
    #pairs = list(zip(left_nums, right_nums))[:num_elements]
    # Above wastes time zipping the entire lists, then keep only the first num_elements
    # whereas zip_len() STOPs zipping at num_elements
    pairs = list(zip_len(num_elements, left_nums, right_nums))
    logging.info(('=' * 30) + "    Starmap Test    " + ('=' * 30))
    logging.info(f"   Pairs: {len(pairs)}#{pairs}")
    start_time = time.time()
    with Pool(processes=num_workers) as pool:
        results = pool.starmap(multiply2, pairs)
        logging.info(f"Multiply: {len(results)}#{results}")
    logging.info(f" Runtime: {time.time() - start_time:.1f} seconds\n")


if __name__ == '__main__':
    # VERY IMPORTANT: MUST call .basicConfig(level=logging.INFO) else no log messages!
    # Because the default is level=logging.WARNING hence *NO* INFO/DEBUG messages!
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    args = parse_command_line(description="A sample script to try out the Pool class from Python multiprocessing module")

    #start_time = time.time()

    if args.map or (len(sys.argv) < 2):
        test_map(num_workers=args.workers, num_elements=args.count)
    elif args.starmap:
        test_starmap(num_workers=args.workers, num_elements=args.count)

    #logging.info(f" Runtime: {time.time() - start_time:.1f} seconds")
