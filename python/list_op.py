# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:01:05 2019

@author: Ham

HackerRanch Challenge: Lists

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines
of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding
operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""

stdin_sim = """
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    #N = int(input())

    lst = []
    #for _ in range(N):
    #    command, *args = input().split()
    stdin_sim.pop(0)
    while stdin_sim:
        command, *args = stdin_sim.pop(0).split()
        tup = tuple((int(e) for e in args))
        #print("comm=<" + command + ">", tup)
        if command == 'print':
            print(lst)
        else:
            command = "lst." + command + str(tup)
            #print("exec(" + command + ")")
            exec(command)
