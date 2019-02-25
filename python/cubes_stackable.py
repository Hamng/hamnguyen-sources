# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:30:28 2019

@author: Ham

HackerRanch Challenge: Piling Up!

There is a horizontal row of N cubes.
The length of each cube is given.
You need to create a new vertical pile of cubes.
The new pile should follow these directions:
if cube_i is on top of cube_j then sidelength_i <= sidelength_j.

When stacking the cubes,
you can only pick up either the leftmost or the rightmost cube each time.
Print "Yes" if it is possible to stack the cubes. Otherwise, print "No".
Do not print the quotation marks.

Input Format

The first line contains a single integer t, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains N, the number of cubes.
The second line contains N space separated integers,
denoting the sideLengths of each cube in that order.

Constraints



Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No

"""

stdin_sim = """
2
6
4 3 2 1 3 4
3
1 3 2
"""

stdin_sim = stdin_sim.strip().splitlines()

def pop_highest(l):
    """doc"""
    # warning, pass-by-ref so WILL modify input arg
    return l.pop() if l[-1] >= l[0] else l.pop(0)

def are_cubes_stackable(cubes):
    """doc"""
    #print(len(cubes), cubes)
    bottom = pop_highest(cubes)
    #print(cur, cubes)
    while cubes:
        v = pop_highest(cubes)
        if v > bottom:
            return False

    return True

def run_test_case():
    """doc"""
    #input()            # discarded, not needed
    #cubes = [int(e) for e in input().split()]
    stdin_sim.pop(0)    # discarded, not needed
    cubes = [int(e) for e in stdin_sim.pop(0).split()]
    #print(n, cubes)
    print("Yes" if are_cubes_stackable(cubes) else "No")

if __name__ == '__main__':
    #for _ in range(int(input())):
    for _ in range(int(stdin_sim.pop(0))):
        run_test_case()
