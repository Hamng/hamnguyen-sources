# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:50:30 2019

@author: Ham

HackerRanch Challenge: Nested Lists

Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having
the second lowest grade.

Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines;
the first line contains a student's name,
and the second line contains their grade.

Constraints
2 <= N <= 5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students, order their names alphabetically
and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
"""

stdin_sim = """
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    lst = []
    #for _ in range(int(input())):
    #    name = input()
    #    score = float(input())
    stdin_sim.pop(0)                                    # ignored
    while stdin_sim:
        name = stdin_sim.pop(0)
        score = float(stdin_sim.pop(0))
        lst.append((score, name))

    lst.sort()
    lowest = lst.pop(0)[0]
    #print(lowest)
    #lst = [tup for tup in lst if tup[0] != lowest]      # remove lowest score student(s)
    lst = list(filter(lambda t: t[0] != lowest, lst))
    lowest = lst[0][0]                                  # now 2nd lowest
    lst = [tup[1] for tup in lst if tup[0] == lowest]   # only names of lowest student(s)
    [print(n) for n in sorted(lst)]
