# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:12:29 2019

@author: Ham

HackerRanch Challenge: Word Order

You are given N words. Some words may repeat.
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, N.
The next N lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word
according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

"""

stdin_sim = """
4
bcdef
abcdefg
bcde
bcdef
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    lst = []
    occ = {}
    #n = int(input())
    n = int(stdin_sim.pop(0))
    for _ in range(n):
        #word = input()
        word = stdin_sim.pop(0)
        if word in occ:
            occ[word] += 1
        else:
            lst += [word]
            occ[word] = 1

    print(len(lst))
    [print(occ[word], end=" ") for word in lst]

    # Alternately, can do a 1-liner below, but the resulting
    # dictionary might NOT be printed in the order of appearance
    #
    #from collections import Counter
    #print(Counter(stdin_sim).items())
