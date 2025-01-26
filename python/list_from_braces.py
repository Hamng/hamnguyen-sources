#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Ham Nguyen

"""

import sys
import os
import re

if __name__ == '__main__':
    all_lines = open(sys.argv[1], 'r').read()
    #print('"' + all_lines.strip() + '"')

    m = re.search(r'.*\{([^}]+)\}', all_lines, re.MULTILINE)
    if m:
        print('matched={' + m.group(1) + '}')
        ret_list = [int(e, 0) for e in m.group(1).split(',')]
        print([f'{v:#08x}' for v in ret_list])
    sys.exit(0)


    # Rev 1.0
    for line in open(sys.argv[1], 'r').readlines():
        left_brace = line.find('{')
        if left_brace < 0:
            continue
        line = line.rstrip()[left_brace + 1:-1]
        print('"' + line.strip() + '"')
        print(line.split(','))
