#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:07:51 2020

@author: ham.nguyen

This script parses output from an 'mpstat-P ALL' command such that for each
time tick, it counts entries in a specific column (e.g. '%sys' or '%idle'),
that don't match an excluded_value (e.g. 0 for '%sys', 100 for '%idle'),
then if the count is non-0, print the count, sum, and average.
Each time tick is reported as consecutive non-blank line,
and is separated from the previous and the following
time tick by blank lines.

Usage:  mpstat_%sys_not_0.py  <  mpstat.log

REQUIREMENTS: must invoke 'mpstat' with option '-P ALL' because:
    a.  The 2nd line (i.e. CPU=='all') in each time tick is skipped.
    b.  The number_of_cpus is calculated as number_of_lines in
        each time tick - 2 (header and CPU=='all')

Notes:
    1.  Don't really need Python3. It's just that Python3 print()
        as desired, whereas Python2 print() as a tuple.
    2.  For plotting, we probably only care about the last field
        (i.e. num of CPUs used), so 'awk' it out to the clipboard as:
            mpstat_%sys_not_0.py < mpstat.log | awk '{print $NF}' | xclip -i
        Alternately, simplify this script to output only the desired field.
    3.  Naming convention: the name of this script is tokenized such that:
         a. 3rd_from_last: name of the column to be examined.
         b. Last token: the excluded_value (i.e. to not match)
         c. To parse a different column, just create a new symlink to this
            module; e.g. mpstat_%idle_not_100.py -> mpstat_%sys_not.0.py
         d. If above is too hacky, just hardwire the needed vars.
    4.  In a way, this script _condenses_ an mpstat output by
        printing a 1-liner for each "relevant" time ticks.
    5.  Typically, this script is used to print the "number of CPUs used"
        (or "CPU utilization/saturation", or "how many CPUs to saturate").
        That's calculated as:
         a. '%sys': avg_%sys_per_cpu = sum / non_0_count
                    avg_%sys_total   = avg_%sys_per_cpu * non_0_count
                                     = sum (in % unit)
                    num_cpus_used    = sum / 100 

         b. '%idle': avg_%idle_per_cpu = sum / non_100_count
                     avg_%idle_total   = avg_%idle_per_cpu * non_100_count
                                       = sum
                     avg_%busy         = non_100_count * 100 - sum  (in % unit)
                     num_cpus_used     = above / 100
                                       = non_100_count - sum / 100

"""

import sys
import os
import itertools

# A generator to yield a list of non-blank lines.
# Explanation from innermost:
#   infile.readlines()  read *all* lines into a list
#   map(str.strip, *)   strip leading and trailing whitespaces in each line
#   itertools.groupby() group consecutive lines based on blank/not_blank. E.g.
#       [[False, ['', '']],
#        [True, ['line 1', 'a line', 'still more', 'and']],
#        [False, ['']],
#        [True, ['finally']]]
#   (t[1] for if t[0])  for each elem in the list, if elem[0]==True,
#                       return list(elem[1]) as a list of non-blank lines. E.g.
#       [['line 1', 'a line', 'still more', 'and'],
#        ['finally']]
def non_blank_lines(infile=sys.stdin):
    return (list(tupl[1]) for tupl in itertools.groupby(map(str.strip,
                                                        infile.readlines()),
                                                        lambda l: len(l) != 0)
            if tupl[0])


# A generator to yield a tuple of (time_tick, count, sum, num_cpus)
# for each time_tick whose column_name doesn't match the excluded_value
def count_sum_not_matched(column_name, excluded_value, infile=sys.stdin):
    where = None
    excluded_value = float(excluded_value)
    for lines_list in non_blank_lines(infile=infile):
        lines_list_len = len(lines_list)
        #print('Got:', lines_list_len, lines_list)
        #if lines_list_len < 3:
        #    # Each lines_list must have 2+ lines, representing >=1 cpus
        #    # This also skips the sign-on line since having only 1 line.
        #    continue

        # Examine the 1st line (in the list): skip if 1st char isn't a digit.
        # This skips the ending "Average:" summaries since 1st col not numeric.
        # This also skips the sign-on line since its 1st char isn't numeric.
        line = lines_list[0]
        if not line[0].isdigit():
            continue

        # mpstat-specific parsing of each list_of_lines by:
        # split the 1st line to column headings, and ignore lines 1 and 2.
        # Then find index of the column headings that matches column_name.
        # Hack alert: set "where" only once since it should always be the same.
        # Caveat: on CentOS, each time_tick line has an "AM/PM" as the
        # 2nd column, whereas the ending "Average:" summaries don't,
        # so "where" would be off-by-1, but we skipped "Average:" already.
        if where is None:
            headings = line.split()
            where = headings.index(column_name)
            time_tick = headings[0]
            #print(time_tick, column_name, 'is @ index', where)
        else:
            time_tick = line.split(None, 1)[0]

        # Inner list comprehension:
        #   for each line starting from the 3rd:
        #	split(None, where+1): split just enough to examine line[where]
        #	float(line[where]):	  keep only value in where column as float
        # Outer list comprehension:	keep only elem NOT == excluded_value
        lst = [e for e in [float(line.split(None, where + 1)[where])
                           for line in lines_list[2:]]
               if e != excluded_value]

        count = len(lst)
        if count:
            # Ok, yielding a tuple of: (time tick, count, sum, num_cpus)
            #print('Yielding non-0 at:', time_tick, count, sum(lst), lines_list_len - 2, lst)
            yield (time_tick, count, sum(lst), lines_list_len - 2)


if __name__ == '__main__':
    # Set vars based on script name:
    # excluded_value: last token
    # column_name: 3rd from last
    # If that seems too hacky, forget about tokens[], just hardwire the 2
    # From innermost:
    # __file__:      '/path/to/mpstat_%sys_not_0.py'
    # .basename():   'mpstat_%sys_not_0.py'
    # .splitext():  ['mpstat_%sys_not_0', '.py']
    # [0]:           'mpstat_%sys_not_0'
    # .rsplit(,3):  ['mpstat', '%sys', 'not', '0']
    tokens = os.path.splitext(os.path.basename(__file__))[0].rsplit('_', 3)
    column_name = tokens[-3]
    excluded_value = int(tokens[-1])
    #print(tokens, column_name, excluded_value)

    for tup in count_sum_not_matched(column_name, excluded_value):
        cpu_used = tup[2] / 100
        if excluded_value != 0:
            cpu_used = tup[1] - cpu_used
        print(tup[0] + ':',
              tup[1], 'cpus whose', column_name, '!=', str(excluded_value) + ',',
              tup[2], 'total', column_name + ',',
              tup[2] / tup[1], 'avg', column_name + ',',
              'num of cpus used', cpu_used)
