# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 20:26:02 2019

@author: Ham

HackerRanch Challenge: Finding the percentage (average)

You have a record of N students.
Each record contains the student's name, and their percent marks in Maths,
Physics and Chemistry.
The marks can be floating values.
The user enters some integer N followed by the names and marks for students.
You are required to save the record in a dictionary data type.
The user then enters a student's name.
Output the average percentage marks obtained by that student,
correct to two decimal places.

Input Format

The first line contains the integer N, the number of students.
The next N lines contains the name and marks obtained by that student separated by a space.
The final line contains the name of a particular student previously listed.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student
correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00

"""

stdin_sim = """
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""

stdin_sim = stdin_sim.strip().splitlines()

import statistics

if __name__ == '__main__':
    student_marks = {}
    #n = int(input())
    #for _ in range(n):
    #    name, *line = input().split()
    for _ in range(int(stdin_sim.pop(0))):
        name, *line = stdin_sim.pop(0).split()
        student_marks[name] = [float(e) for e in line]
    #    #scores = list(map(float, line))
    #    #student_marks[name] = scores
    #query_name = input()
    query_name = stdin_sim.pop(0)

    #print(query_name, student_marks[query_name], sum(student_marks[query_name]))
    print("%0.2f" % statistics.mean(student_marks[query_name]))
