# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:05:26 2019

@author: Ham

HackerRanch Challenge: No Idea!

There is an array of n integers.
There are also 2 disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0.
For each i in the array, if i in A, you add +1 to your happiness.
If i in B, you add -1 to your happiness.
Otherwise, your happiness does not change.
Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements.
However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, for the sets A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

Explanation

You gain +1 unit of happiness for elements 1 and 3 in set A.
You lose -1 unit for 5 in set B.
The element 7 in set B does not exist in the array
so it is not included in the calculation.

Hence, the total happiness is 1 + 1 - 1 = 1.

"""

import io

STDIN_SIO = io.StringIO("""
3 2
1 5 3
3 1
5 7
""".strip())

if __name__ == '__main__':
    #input()                             # discarded, not needed
    #l = list(map(int, input().split())) # must be a list() so can iterate [for i in l]
    #a = set(map(int, input().split()))
    #b = set(map(int, input().split()))
    STDIN_SIO.readline().strip()        # discarded, not needed
    l = list(map(int, STDIN_SIO.readline().strip().split()))
                                        # must be a list() so can iterate [for i in l]
    a = set(map(int, STDIN_SIO.readline().strip().split()))
    b = set(map(int, STDIN_SIO.readline().strip().split()))
    #print(l)
    #print("+1", a)
    #print("-1", b)
    #print(sum([1 for i in l if i in a]) - sum([1 for i in l if i in b]))
    # casting to int() not needed, but doing so for clarity
    # Also, can simply do sum(expr gen) instead of sum([list comp])
    print(sum(int(i in a) - int(i in b) for i in l))
