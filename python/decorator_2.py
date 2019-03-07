# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:08:27 2019

@author: Ham

HackerRanch Challenge: Decorators 2 - Name Directory

Let's use decorators to build a name directory!
You are given some information about people.
Each person has a first name, last name, age and sex.
Print their names in a specific format sorted by their age in ascending order
i.e. the youngest person's name should be printed first.
For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:

Mr. Henry Davids

For Mary George, the output should be:

Ms. Mary George

Input Format

The first line contains the integer N, the number of people.
N lines follow each containing the space separated values of the first name,
last name, age and sex, respectively.

Constraints


Output Format

Output  names on separate lines in the format described above in ascending order of age.

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle

Concept

For sorting a nested list based on some parameter, you can use the itemgetter library.
You can read more about it here.

"""

import io

STDIN_SIO = io.StringIO("""
10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M
""".strip())

def person_lister(f):
    def inner(people):
        #print(*people)
        people.sort(key=lambda x: int(x[2]))
        #print(*people)
        # complete the function
        return (f(p) for p in people)
    return inner

# Caveat: this is a BAD example of using decorator!
# The original name_format() belows expects a simple tuple(first, last, age, sex),
# then return 1 string.
# But after being decorated per above,
# the new name_format() expects a tuple-of-tuples: ((f1,l1,a1,s1), (f2,l2,a2,s2)),
# then returns a sorted tuple-of-strings: ("str1", "str2", ..., "strn")

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    #people = [input().split() for i in range(int(input()))]
    people = [STDIN_SIO.readline().strip().split()
              for i in range(int(STDIN_SIO.readline().strip()))]
    print(*name_format(people), sep='\n')
