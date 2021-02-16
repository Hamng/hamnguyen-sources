# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:37:54 2021

@author: Ham
"""

import more_itertools as mit

import io

STDIN_SIO = io.StringIO("""
abcd
""".strip())

def partition_mit(s: str) -> list:
    # Copied from: https://stackoverflow.com/questions/4904430/find-all-list-permutations-of-splitting-a-string-in-python
    if s:
        for lst in mit.partitions(s):
            yield ["".join(sublst) for sublst in lst]
    else:
        yield []

def partition_recursive(s: str) -> list:
    # Ham's own: NOT working
    if s:
        res = []
        for i in range(1,len(s)+1):
            lft = [s[:i]]
            res += [lft + rest for rest in partition_recursive(s[i:])]
        return res
    else:
        return []

def partition_generator(s: str) -> list:
    # Copied from: https://stackoverflow.com/questions/52167339/get-all-possible-str-partitions-of-any-length
    if s:
        for i in range(1, len(s)+1):
            lft = s[:i]
            for p in partition_generator(s[i:]):
                yield [lft] + p
    else:
        yield []

def splitter(str):
    # Copied from: https://stackoverflow.com/questions/4904430/find-all-list-permutations-of-splitting-a-string-in-python
    # Bug: missing the 1-element list containing the entire str: [str]
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield [start, end]
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break
        print('Partitioning "' + line + '":')
        #print(*list(partition_generator(line)), sep='\n')
        #print(*list(splitter(line)), sep='\n')
        print(*list(partition_mit(line)), sep='\n')
        #print(*list(partition_recursive(line)), sep='\n')
