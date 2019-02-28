# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:38:50 2019

@author: Ham

HackerRanch Challenge: Matrix Script

Task

Neo has a complex matrix script. The matrix script is a N X M grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

Capture.JPG

To decode the script, Neo needs to read each column
and select only the alphanumeric characters and connect them.
Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script,
then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.

Constraints


Note: A 0 score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script.

Sample Input 0

7 3
Tsi
h%x
i #
sM
$a
#t%
ir!

Sample Output 0

This is Matrix#  %!

Explanation 0

The decoded script is:

This$#is% Matrix#  %!

Neo replaces the symbols or spaces between two alphanumeric characters
with a single space   ' ' for better readability.

So, the final decoded script is:

This is Matrix#  %!

"""

import re
import io

STDIN_SIO = io.StringIO("""
7 3
Tsi
h%x
i #
sM
$a
#t%
ir!
""".strip())

if __name__ == '__main__':
    #n, m = map(int, input().split())
    n, m = map(int, STDIN_SIO.readline().strip().split())

    #matrix =[input() for _ in range(n)]
    matrix = []
    for _ in range(n):
        # Sigh, only if using _SIO: the original input line might contain
        # trailing spaces, but I append trailing spaces to lines in _SIO,
        # they'll be _automatically removed_ when this *.py is saved!
        matrix_item = STDIN_SIO.readline().strip()
        matrix_item += (" " * (m - len(matrix_item)))
        matrix.append(matrix_item)

    #decoded = "".join([matrix[r][c] for c in range(m) for r in range(n)])
    # The above nested-for is mine, but the nested-join and zip below
    # is copied from user NYJ1qCr in the discussion
    #decoded = "".join([e for col in zip(*matrix) for e in col])
    decoded = "".join(["".join(col) for col in zip(*matrix)])
    #print('decode="' + decoded + '"')

    _, head, decoded, tail, _ = re.split(r"^(\W*)(.*?)(\W*)$", decoded)
    #print('head=' + str(len(head)) + '"' + head + '",',
    #      'decode="' + decoded + '",',
    #      'tail=' + str(len(tail)) + '"' + tail + '"')

    decoded = re.sub(r"\W+", " ", decoded)
    #print('decode="' + decoded + '"')
    print(head + decoded + tail)
