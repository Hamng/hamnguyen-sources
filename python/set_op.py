# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:28:19 2019

@author: Ham

HackerRanch Challenge: Set .discard(), .remove() & .pop()

Task
You have a non-empty set S,
and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer Q, the number of elements in the set S.
The second line contains Q space separated elements of set S.
All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove
and/or discard commands followed by their associated value.

Constraints



Output Format

Print the sum of the elements of set S on a single line.

Sample Input (see STDIN_SIO)

Sample Output

4

"""

import io

STDIN_SIO = io.StringIO("""
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
""".strip())

if __name__ == '__main__':
    #input()                             # discarded, not needed
    #s = set(map(int, input().split()))
    #for _ in range(int(input())):
    #    command, *args = input().strip().split()
    STDIN_SIO.readline().strip()                             # discarded, not needed
    s = set(map(int, STDIN_SIO.readline().strip().split()))
    for _ in range(int(STDIN_SIO.readline().strip())):
        command, *args = STDIN_SIO.readline().strip().split()
        args = tuple(map(int, args))
        #print("comm=<" + command + ">", args, args)
        command = "s." + command + str(args)
        # Caveat, for 1-arg op, it always shows a comma after the arg!!
        # That's bc Python always shows a 1-element tuple with an
        # ending command likes (x,) to disambiguate from an expr (x).
        # I.e. type((1,)) == 'tuple'  whereas   type((1)) == 'int'
        #      str((1,))  == '(1,)'             str((1))  == '1'
        #print("exec('" + command + "')")
        exec(command)

    print(sum(s))
