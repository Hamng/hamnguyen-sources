# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:15:35 2020

@author: Ham

HackerRank > Practice > Algorithms > Implementation
Angry Professor

Problem
A Discrete Mathematics professor has a class of students.
Frustrated with their lack of discipline, he decides to cancel class
if fewer than some number of students are present when class starts.
Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).

Given the arrival time of each student and a threshhold number of attendees,
determine if the class is canceled.

Input Format

The first line of input contains t, the number of test cases.

Each test case consists of two lines.

The first line has two space-separated integers, n and k,
the number of students (size of a[]) and the cancellation threshold.
The second line contains n space-separated integers (a[1 ... n])
describing the arrival times for each student.

Note: Non-positive arrival times (a[i] <= 0) indicate the student arrived early or on time;
positive arrival times (a[i] > 0) indicate the student arrived a[i] minutes late.

For example, there are  students who arrive at times . Four are there on time, and two arrive late. If there must be  for class to go on, in this case the class will continue. If there must be , then class is cancelled.

Function Description

Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):

k: the threshold number of students
a: an array of integers representing arrival times
Constraints

Output Format

For each test case, print the word YES if the class is canceled or NO if it is not.

Note
If a student arrives exactly on time , the student is considered to have entered before the class started.

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Sample Output

YES
NO
Explanation

For the first test case, . The professor wants at least  students in attendance, but only  have arrived on time ( and ) so the class is cancelled.

For the second test case, . The professor wants at least  students in attendance, and there are  who have arrived on time ( and ) so the class is not cancelled.
"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

import io

# Test case 9: Expected Output: YES YES NO YES YES YES NO NO NO YES
STDIN_SIO = io.StringIO("""
10
800 542
-54 60 -68 -33 -32 -95 20 -95 74 0 10 81 -93 -28 78 -23 77 -66 -89 -48 -59 -68 -5 -76 -26 61 -98 24 -61 30 -95 -71 -89 -70 41 -51 66 -31 -34 -50 -87 -2 5 29 31 -57 13 -99 18 32 -45 -11 -55 -83 -2 -54 97 28 35 -73 17 92 11 36 18 93 -3 -26 0 0 95 96 63 50 34 -16 -6 37 -4 -51 93 -89 54 59 25 -12 17 -16 37 -30 -90 78 7 -18 -40 -38 -70 -34 95 -82 -56 -45 -8 54 -29 21 -83 -20 19 5 -11 -97 75 -10 76 -95 92 -57 3 -49 0 55 -26 -77 -65 56 -82 -63 -36 -31 70 -48 20 66 -69 7 -42 56 90 -65 -20 36 27 -11 77 32 -21 -14 -91 16 52 -34 -90 63 76 -87 3 50 27 -50 7 -8 -20 22 -6 -75 -66 -6 52 -88 2 28 -4 92 -43 40 29 31 -74 12 97 91 -49 -24 -71 85 -40 -31 43 -28 69 89 -20 52 26 -26 -57 91 71 -12 79 -68 63 -16 74 97 -16 94 58 -82 -16 -12 -83 -31 22 -49 93 -26 68 14 91 -37 -1 48 83 49 -95 -72 21 -85 -99 49 3 0 -22 65 -78 76 -38 43 -59 72 58 33 0 74 -56 43 -3 -82 -9 -94 -1 -71 47 65 59 61 -34 48 16 37 50 83 75 -31 -12 76 -49 -57 62 -3 -13 90 -10 86 64 -50 -56 -69 -50 20 30 -79 -96 -28 64 -31 -47 -80 -63 35 42 -43 70 85 68 86 -55 -82 -6 62 93 -3 19 1 50 10 73 -46 -69 67 38 -41 -71 -96 -38 4 -56 -76 -91 -57 14 90 -25 -87 -69 85 -60 4 -53 64 -63 75 -28 -94 -28 -17 23 34 -97 -96 27 -77 -11 -74 37 -8 11 -71 -34 -11 21 9 40 -97 -68 -55 -78 87 -69 -58 -56 59 49 -7 -48 49 -3 18 -53 -81 -13 69 -73 85 73 -1 61 -98 92 -97 28 14 -5 74 3 -32 96 -60 -61 -15 40 -64 -78 63 20 14 6 83 -16 -74 69 36 -59 38 45 -6 -22 -38 85 -74 -65 -57 21 87 2 -10 -19 88 47 50 83 -30 80 10 -74 -23 -26 63 -25 -89 -64 -2 46 14 -72 -37 -74 -13 36 71 61 1 -79 -38 16 35 27 -68 -31 -18 -52 10 75 84 -48 -25 -2 -48 -92 37 14 44 13 -67 48 99 98 -30 -85 37 -21 46 -41 8 -33 -45 -21 93 3 -30 -3 -55 -91 -74 51 -14 26 52 -7 53 58 91 -88 -66 -50 46 -78 -6 -90 1 -96 -70 28 41 -34 79 45 24 -11 81 -38 -66 33 41 -5 -69 -10 -75 13 77 -15 40 31 49 58 56 62 69 -99 74 57 -9 34 58 -4 95 -44 -83 -3 -22 -67 13 -4 80 -45 -59 98 22 -4 -32 -21 -32 -14 97 -53 -82 49 6 -30 57 -41 82 37 77 -89 -54 89 -80 -7 -25 48 -36 -7 50 29 -65 28 -66 -56 -10 -5 -60 4 1 -21 27 -38 -66 -6 35 -28 -61 52 73 23 -58 0 26 14 71 -6 56 62 42 42 -59 30 78 0 -95 39 -4 -27 -48 -11 -28 -18 66 10 52 -37 -27 83 7 13 12 12 92 -51 85 11 -84 -2 61 62 -69 -28 -23 7 52 37 73 -32 -40 9 -50 91 2 -88 -57 81 -6 -24 -25 -12 -51 -41 98 93 62 16 23 -51 0 -40 -46 -36 83 81 43 -38 -94 -23 57 -35 -19 -36 58 -71 82 19 85 32 68 81 11 -11 50 2 3 -79 -92 -69 54 -64 -57 17 40 67 16 24 -67 -37 -70 77 -81 0 24 28 -15 -20 77 -18 -39 -81 -85 87 41 74 -16 -89 60 -76 -11 68 49 2 25 -99 -10 -24 87 -52 88 44 82 -54 22 31 39 -16 87 -67 -96 34 99 6 22 -67 89 -66 -44 -70 55 -56 53 -83 96 57 20 -50 2 -58 68 -86 -88 85 25 -55 -8 -75 -36 54 12 -76 -55 -5 -36 -33 93 -17 -23 70 -9 -82 88 -79 -20 -61 97 69 17 13 -42 9 -17 20 81
800 591
-75 56 -40 -5 -98 -74 63 57 -43 83 -71 58 91 -83 -44 -1 86 -5 46 3 55 85 8 60 5 -45 14 30 -59 -42 -39 -75 -4 3 46 47 36 72 -74 49 -76 60 50 51 -4 -65 -37 20 -25 -44 -81 -77 23 15 -82 81 62 -4 -31 -26 -49 -82 36 31 -29 -36 -18 33 -16 43 68 61 17 -47 73 88 17 12 -77 -18 71 -21 -73 35 -6 91 6 57 -22 75 -78 -69 38 -53 -76 25 -31 -89 53 45 6 38 41 -87 0 10 82 -78 64 39 60 92 -63 -47 -9 33 -32 -27 -67 88 -32 49 81 38 -16 -90 94 67 -15 30 10 -39 87 68 84 73 11 83 6 -42 51 98 -14 -58 -35 -5 -4 92 -62 45 20 66 -97 -76 -23 26 2 75 46 -49 -22 31 -50 -70 35 10 -38 39 -78 -91 -37 -31 -97 59 -91 77 14 93 83 -28 31 73 66 9 79 1 69 7 -90 62 26 0 99 -56 8 0 74 14 -38 -41 76 -38 -27 64 64 -56 -18 83 49 4 -76 -1 -83 -96 -43 -43 -84 64 80 -34 60 87 46 0 -63 -8 -62 94 -29 18 32 91 96 80 41 20 -8 31 31 5 37 37 -76 96 -26 30 28 -79 33 0 78 -75 85 -93 91 14 64 -31 39 -50 93 28 57 -46 -19 -65 -24 -35 -4 77 -79 -27 -98 88 89 56 22 56 -44 -70 -54 64 33 -91 -80 84 -63 -6 -73 99 36 -96 92 -38 8 3 0 -44 -66 -22 7 9 21 83 66 -60 -42 -61 62 -74 64 -36 44 50 -19 61 83 0 91 -3 -70 -12 -72 99 77 56 -3 10 76 11 -36 73 -47 -28 61 -48 -46 96 -86 5 74 9 -58 -25 -83 34 13 91 85 -3 2 -78 -63 20 74 -70 91 -26 51 -89 92 -6 -83 69 -21 15 75 -25 -24 -45 22 -99 46 -68 -80 -36 32 81 44 -89 27 90 -2 -46 64 -76 58 -4 52 6 -33 57 88 -38 -46 -99 -31 -28 -8 63 69 10 -67 -36 91 5 -36 95 5 -57 -60 77 -49 -81 -84 81 -36 33 11 -28 63 -79 -99 75 -11 -60 -93 -67 -47 4 -96 36 -82 -41 -90 -47 -6 -56 -5 14 -69 -92 16 -57 -11 46 52 -93 4 79 -7 52 -57 -22 -41 -84 68 24 40 0 -48 11 81 38 42 -33 -99 -66 -94 -24 -78 49 36 82 12 80 33 -64 0 52 23 -44 23 31 -51 -9 -15 27 36 32 96 60 -8 96 30 2 -86 80 -9 -30 71 -42 2 -42 83 -39 43 -61 -80 -63 58 68 64 57 -63 -38 31 73 -1 -75 -46 17 70 45 88 -12 27 94 -80 -69 94 -78 -39 -62 71 77 -56 59 73 -28 -14 -11 -73 -36 60 -50 64 84 -84 96 -88 -24 -68 75 -41 6 -45 0 26 24 46 44 59 66 -79 2 -35 16 -14 48 -96 62 -75 63 -51 39 -66 59 -64 -72 -39 63 -53 -34 -71 -75 -89 -12 -52 18 -16 4 94 -12 93 54 11 -11 48 35 81 91 0 39 32 59 68 -86 78 72 -35 56 47 -14 17 -72 12 -25 19 16 -26 -3 90 60 40 -44 -11 25 -23 -59 -93 -43 -46 21 89 -21 -16 -14 67 78 -59 87 -74 34 56 -43 -28 58 59 -44 20 67 43 -94 8 21 -95 42 -73 71 -25 82 -53 32 23 64 -94 -31 -17 -51 -97 -96 33 -18 19 -39 -56 -50 -17 77 11 -35 -76 43 -43 70 -19 -37 -58 -63 -49 -74 -28 -18 11 -86 40 28 44 -62 69 81 -51 94 -78 -87 -12 -84 -90 87 53 -24 -51 61 75 -84 -8 -86 -39 69 -41 96 21 47 38 14 -11 36 -43 11 25 -67 -16 -97 -89 25 -78 -89 -58 63 74 -92 -68 52 -30 -33 62 -93 58 86 60 -31 36 90 56 -43 83 -19 -15 66 87 -6 52 -32 -42 11 81 45 62 -64 88 -52 -46 -26 95 12 -44 89 69 -11 -92 18 -64 -95 98 48 23 62 24 36 -33 58 -66 -77 -69 -99 -11 -38 32 54
800 183
69 -34 -31 -27 -60 -13 -93 -66 -82 -32 -19 -33 -85 -1 -17 39 -64 30 -1 50 -37 2 -77 16 -76 6 -53 -42 63 -57 4 19 22 15 -12 88 -34 84 -63 74 -52 86 -23 95 27 19 -1 51 -44 -51 89 -10 -34 38 -51 88 -44 61 -6 58 -61 -17 19 37 91 24 32 55 33 -67 57 -39 -81 25 -9 -20 64 -84 -58 -51 -14 82 62 -16 -35 -83 90 -98 -75 -58 58 58 68 9 68 -79 89 -32 -51 51 83 82 -9 96 -55 21 -84 39 74 -82 62 28 -23 54 60 -16 -92 -20 -31 38 -22 56 -44 11 97 65 -56 -10 -6 10 74 62 25 71 -51 48 -74 80 52 40 -38 -8 3 77 -87 -75 -66 -31 -24 52 -16 0 57 -12 -77 -11 -14 -61 -42 26 -78 46 95 -87 -83 46 92 -94 -80 -63 -64 24 97 -48 -75 24 -80 97 99 -47 -77 35 -41 -23 -88 82 12 83 -95 -53 9 -24 0 -18 -58 -86 -59 -57 3 77 -18 -48 69 -95 66 35 -30 -17 84 -33 -53 82 93 -17 23 92 -58 75 -27 -92 -71 -72 -90 83 77 -69 89 47 43 83 -62 -60 71 48 59 95 71 -84 -9 -35 -36 -21 -61 60 84 -75 -22 67 -24 -43 -59 17 57 -43 -21 -6 -88 -35 -48 -57 42 -83 69 -61 -70 80 94 -12 -3 18 87 33 -56 76 15 -40 -18 25 -79 84 -90 31 66 88 -4 93 -87 18 -47 51 31 -72 19 -89 84 52 42 -63 31 -29 -13 78 1 95 46 14 42 80 -88 -64 47 50 51 -98 -20 70 2 -34 -49 7 28 26 60 36 79 24 -16 -17 -92 -2 -47 -47 26 -57 -63 -23 39 -66 -7 52 -54 66 3 -42 2 13 73 52 -45 -27 -78 5 0 -69 -78 -98 49 55 -51 -5 45 8 -30 70 -73 -88 48 -21 21 59 -15 31 -74 22 39 -32 -97 8 -4 6 -76 -33 44 -76 -49 -64 -45 34 38 98 87 15 74 -15 1 -7 -20 -57 -48 -82 -21 -66 47 90 -60 63 -74 83 1 30 -24 36 31 61 -27 80 95 -71 99 -27 54 -59 21 -81 -93 -30 -1 14 12 -15 23 92 95 -12 29 6 -35 15 9 83 12 -24 -84 98 69 -88 -13 -15 48 55 -20 -64 -79 63 80 -95 64 -58 61 45 73 -75 -18 -47 -71 48 -68 -50 -97 -88 -64 -74 -58 29 -40 1 -12 -52 72 53 -6 38 19 74 5 97 49 -51 -55 78 -7 -61 -60 -53 17 -79 13 -50 9 52 -38 -85 -25 46 68 28 -8 -46 6 5 11 0 54 8 -27 78 -61 -57 3 -19 32 -51 88 60 2 -70 -50 41 73 -19 61 17 65 13 -82 97 79 6 -98 13 84 69 6 42 -59 -79 63 -47 -75 54 -92 -23 -99 -94 48 -54 43 18 34 81 25 -18 -62 -22 -77 99 -27 96 4 80 50 -36 -59 47 -70 -91 -42 36 79 45 -86 82 -67 -96 -21 75 -11 -69 21 16 -45 -86 -69 -95 -85 -10 37 89 23 -79 -62 68 -69 -96 54 81 -71 91 -95 94 31 4 -48 25 79 -69 -11 -67 -75 -23 -27 -84 25 -91 66 0 -41 -18 51 66 53 -76 24 -97 -58 -84 -26 -35 -96 -23 64 -64 32 0 -30 18 -5 0 -89 -85 -18 -84 90 -99 -98 53 -2 -73 52 -22 95 18 34 33 -67 74 92 86 81 73 12 -99 96 1 1 -35 15 -48 -75 -76 56 32 64 -82 -57 29 -87 36 -4 -84 -64 -53 -76 -80 -87 97 -62 43 49 -23 85 -27 33 -8 4 95 63 -99 -2 -94 -91 -84 -21 -79 57 -80 8 67 -23 -83 67 -48 80 25 31 -24 -62 28 88 58 -63 -39 -99 16 81 54 31 -34 -55 -45 30 -13 -82 81 54 -67 -30 92 -17 4 12 51 -65 -58 97 11 -77 24 -18 -81 97 41 -59 -9 46 -26 75 -6 -67 61 20 95 49 57 -77 -92 91 -54 19 -30 -80 -27 -90 -96 -98 25 34 -68 -45 3 69 -1 80 -15 -70 -20 58 57 -33 58
800 484
50 -22 54 41 69 81 20 49 10 44 57 22 78 68 -44 15 13 32 -38 0 13 -94 74 -6 93 49 95 -12 -99 -34 -85 89 -40 18 47 90 -4 47 31 -14 -7 -79 38 27 -73 32 16 9 48 86 -98 -60 13 -32 -12 -74 14 -74 -97 42 68 -33 1 92 -22 48 -7 -75 -68 70 -7 5 -49 -74 -85 -73 -44 89 -1 -46 -12 96 -55 92 84 9 -58 16 45 -11 -60 36 95 53 11 -23 -45 95 -96 -77 2 75 52 -24 -34 -80 24 -54 -99 -67 58 86 14 -57 20 94 20 -87 65 -21 -99 50 -75 42 64 -36 3 78 55 -32 69 -50 0 -65 -1 -69 45 -75 75 -98 -30 14 -61 3 80 44 -15 -95 -84 37 -3 37 77 72 81 96 -57 97 6 86 88 -92 -78 -75 51 52 -18 -55 -54 51 -50 -51 -61 77 0 6 -47 96 -37 -91 -35 -96 -85 -52 -83 78 55 -93 -77 -37 87 -71 94 -11 -91 24 46 84 -76 74 -44 45 82 -69 -62 41 -53 35 -84 83 0 -5 80 -81 26 -67 60 -74 4 -5 53 -19 -63 6 -56 -74 97 7 -69 85 -48 70 17 2 -92 -91 -58 52 20 -69 0 85 -76 78 -36 -45 20 -44 -63 11 -58 1 17 -90 -16 66 -8 -18 99 -33 -64 20 45 22 -15 -64 -87 -41 23 46 -48 8 67 -44 76 -1 60 -25 -90 -66 -84 -30 0 -28 -59 67 -38 -15 -6 -23 93 27 -50 58 3 -97 -60 -10 2 40 64 -21 38 -11 -52 31 -63 98 -14 -5 -86 8 33 -62 -9 1 61 -80 12 97 30 62 -91 58 -21 -27 -17 -9 6 90 74 -94 66 40 70 -47 -69 -46 73 -70 -20 -58 36 92 -92 63 26 -6 35 23 35 11 -31 -17 66 -3 -88 77 -82 -20 4 -92 44 -22 -97 -89 -15 42 62 -3 99 15 -20 64 14 76 71 -48 -72 47 -68 6 -89 82 -60 -31 -95 -50 43 -18 -3 -79 -68 -42 50 -61 26 5 -68 -70 76 -39 4 40 9 9 57 -39 -68 17 71 -40 -99 16 -37 48 92 -90 81 96 40 55 99 27 -76 -90 28 97 -80 98 52 84 38 93 -4 -62 51 -98 63 22 23 40 -46 -30 -3 45 79 -4 -55 -40 -91 7 23 97 -84 -79 -83 -10 -8 56 72 -72 -34 72 -78 -48 -19 15 -14 82 31 -57 32 -96 11 56 -6 39 57 -30 -28 56 90 -95 36 -6 -90 -34 34 66 -34 -85 3 85 39 -99 97 -20 31 -96 -44 -86 18 60 -54 2 -1 -33 -15 17 -85 -75 -76 -75 -10 -26 26 -92 -89 2 30 37 44 89 -41 66 27 -65 88 15 64 56 59 87 52 -44 -46 -19 4 53 -18 75 65 -6 33 -56 -63 -92 65 -23 73 -57 -53 13 -36 6 38 -56 26 62 84 13 -35 -74 -89 -75 68 33 -8 30 64 54 -22 -11 73 -12 -43 61 -83 -36 88 -34 95 -30 -17 51 53 -89 -68 27 25 55 18 3 -55 -26 -2 52 -32 4 -98 -35 -13 78 -28 27 -98 -26 51 -21 -69 -2 -12 21 40 -97 -33 -42 9 -31 79 -43 -46 -45 -51 56 18 -43 17 26 94 -1 -8 -29 64 8 -23 -72 -73 -71 88 -96 90 -88 8 70 89 -85 14 68 -26 26 27 -23 72 76 74 70 64 24 24 78 17 -64 77 67 -8 -57 -48 -40 -27 85 -41 18 -66 81 -41 -5 74 -46 -53 -58 -11 52 -1 32 13 34 74 11 46 83 -3 50 -61 32 62 79 -10 84 -28 -44 -87 47 -82 5 2 -20 -29 34 -70 9 61 -57 -25 87 -11 -95 61 11 -53 23 -57 -65 -17 -82 22 -72 -84 6 -24 -63 -76 85 -52 32 -64 17 3 61 -37 -61 -86 -42 -67 -80 -94 -78 -53 -60 11 -67 1 98 70 -77 54 67 76 11 -11 39 -39 -80 -85 -3 86 24 -59 95 -33 -37 -67 -80 -19 -91 39 39 -51 24 13 -85 -1 -90 36 -90 -62 -61 36 -77 -36 37 2 -55 49 -42 10 -13 -41 -72
800 730
7 -11 -30 18 -41 -75 -41 76 -5 -42 -17 -84 14 0 -83 46 8 -31 14 75 -41 28 58 82 -11 34 97 8 57 -59 -27 -83 -67 -25 -17 -92 55 44 76 81 -50 19 34 -64 92 -37 33 59 87 -85 90 -18 -49 -63 -89 -16 13 -92 -14 43 -83 31 53 68 27 -1 -34 -67 -82 12 27 68 15 40 20 -41 -16 24 -62 61 98 59 34 20 9 92 61 81 72 -58 56 0 23 41 68 -28 69 -3 -18 -72 -55 67 77 97 -21 -46 59 50 22 72 99 61 92 72 39 89 12 15 -57 91 19 -8 35 -65 -3 -99 90 22 76 44 -42 -62 -93 -44 89 -33 24 -91 -52 20 -45 61 -32 69 -30 -76 -98 80 67 94 12 -69 21 0 -72 81 -92 5 -26 38 -92 34 57 34 90 -33 8 43 -18 -55 67 59 30 41 -91 -18 -97 25 66 31 93 63 -70 83 53 78 26 -84 54 -65 -8 -32 87 -12 -69 -14 59 -16 -35 -17 41 -12 -85 -27 -26 -36 -80 41 77 -77 -49 -13 20 -38 -84 -99 -3 96 13 31 -21 -26 -39 -73 25 -67 94 -34 -14 26 -80 76 -38 -27 -1 42 77 -27 40 -84 -4 91 37 17 -50 50 22 -69 4 15 -6 -79 -30 3 -59 88 -96 14 -58 -84 27 -95 -14 61 65 75 -38 59 12 39 6 87 60 -35 85 82 59 -66 -94 -43 -8 34 76 -14 60 60 86 73 1 20 32 3 -80 -16 48 -37 81 -54 -17 -46 -27 99 -58 15 33 -98 -37 -9 -74 -95 -37 31 56 76 -59 6 32 -3 -30 3 -5 -32 59 -64 -19 -8 96 26 30 81 -76 -27 -96 4 52 -45 -64 3 -71 -9 31 -98 -9 -83 -79 80 55 -69 -41 -82 -84 -54 9 24 -29 -23 2 91 51 3 42 38 -43 -1 -84 -30 66 -21 47 -9 82 89 58 48 -7 92 -40 47 -90 72 87 -47 -92 81 -65 15 -27 83 -37 99 40 -45 25 67 -96 94 -95 -41 -9 78 17 -73 2 33 -92 87 27 64 -29 20 -24 61 -7 10 28 94 -85 -41 -76 -30 11 -53 -54 -44 -53 60 -83 -48 27 11 50 -53 73 -75 -74 21 -79 28 -96 68 -93 -31 6 -18 42 -42 35 -28 46 13 14 10 -13 79 -15 -62 80 -36 -77 73 -36 -11 -66 35 -48 85 34 -7 -86 60 -38 -61 20 -57 -3 68 -49 66 24 -29 1 86 10 -35 84 49 75 92 -11 45 32 -58 45 98 -78 -93 -93 -15 -29 -51 -3 87 14 -77 -33 92 40 0 -26 59 29 36 36 -78 -58 -30 -34 -91 0 -78 95 4 -72 25 6 7 -88 -61 46 -93 -73 -18 -44 11 -83 -31 59 -66 -43 -34 -27 -88 -36 -44 93 -39 13 77 -72 54 -30 -85 -24 -25 -94 -68 -4 89 58 -74 -22 69 -24 45 38 -51 89 62 -92 -33 50 -60 10 -46 86 71 34 48 38 -54 96 -97 -46 -3 98 76 89 54 -37 71 -20 36 -86 65 29 53 -29 63 -13 13 -6 11 -78 -99 17 43 -17 -96 -63 80 86 -22 -39 -91 55 15 -98 8 -95 -97 82 53 -20 54 -68 32 23 69 91 14 21 -59 -7 -48 27 -18 -38 12 26 97 57 0 83 -43 34 -72 -39 -78 51 -53 76 -91 95 -76 -25 67 3 -15 -41 65 -19 34 21 61 43 2 37 -86 -52 -6 89 64 45 -83 41 -13 -39 -23 64 85 -50 -31 85 73 -85 -19 57 70 -67 41 -55 -22 58 -6 34 -34 83 -24 35 -9 29 -98 65 -93 75 -93 94 -76 65 27 -78 -35 -78 81 9 38 71 -29 58 73 -9 15 -34 -8 -77 -50 -48 -68 97 -92 -44 -49 -20 4 53 -63 95 18 -73 80 61 10 -68 87 -84 28 15 43 -60 -17 -28 76 62 57 -72 89 -72 -46 82 -10 17 94 20 -19 -89 94 -68 45 68 -17 45 -77 -10 -62 9 10 14 11 -46 16 -71 56 -85 74 -9 -98 2 -75 -3 -57 61 42 24 -11 88 -9 -41 2 24 36
800 434
-74 -66 -16 97 65 -23 -41 4 16 -73 -77 -30 -67 43 30 -43 -43 44 -14 -92 -58 -73 95 -64 13 -43 33 -49 84 -53 22 71 -6 29 61 -52 40 -20 -6 99 -25 -61 20 -11 56 71 12 0 -62 -91 54 -96 72 29 -4 -50 -76 40 27 -53 -19 17 -22 -2 -98 61 93 -46 25 49 -9 -10 -15 85 57 29 18 -60 -16 78 -60 -19 48 24 -46 -6 -24 96 71 -86 24 57 67 -35 -31 -50 4 50 40 81 99 -97 -56 -67 -26 7 74 97 -81 76 -98 -9 53 -11 -37 83 32 63 25 -19 -89 54 -95 -56 87 93 -63 92 65 -61 99 90 -76 23 -89 5 73 -93 14 -96 -33 39 -96 -17 38 -64 -27 -21 65 9 39 84 77 -32 -78 97 -22 12 -71 81 -13 -98 56 -96 -16 27 -24 -71 40 -97 35 82 86 29 -76 18 -11 -82 88 41 88 -63 -32 19 -41 43 -15 -39 -72 11 34 -90 -50 17 -54 -95 -32 -60 45 -89 -47 -16 10 -68 27 -35 -60 -58 -1 2 -87 -2 -8 35 93 -41 -62 -7 64 -7 -6 52 -71 30 38 31 -81 96 48 96 61 -35 -94 47 22 49 0 -99 -15 -95 65 -79 -13 41 -60 -55 -26 96 89 -30 -50 -43 36 -74 -76 -5 0 -93 -65 79 -23 50 -29 21 41 -33 -34 94 23 73 89 -94 68 -55 -25 14 21 49 62 24 -25 -47 -37 -33 -61 13 37 -44 -46 90 -38 71 -20 65 46 -90 -98 -34 30 -1 -73 45 -73 68 -42 -42 15 -92 89 -22 -99 6 -1 37 -59 74 4 95 -62 48 27 36 7 82 38 -83 -21 -86 -81 6 14 -77 -5 96 -40 -23 -87 -62 -88 95 1 -15 -20 -98 77 46 89 -11 48 -13 4 8 96 43 14 66 17 -91 34 -44 45 8 -66 -81 30 -54 -35 31 -84 19 -64 -67 18 72 -51 69 58 -35 48 -90 16 -17 -59 35 74 95 -92 25 24 -67 -65 75 -17 0 -80 96 87 -99 -14 43 41 31 -4 99 5 -59 7 98 -97 42 -40 77 56 -27 63 62 64 41 2 -52 12 -82 -97 96 -82 -24 -33 3 -31 63 4 51 24 40 37 38 -55 -21 57 -99 12 15 30 87 0 -7 29 76 -55 83 12 94 -47 -71 88 -96 -99 -51 -29 42 -41 -37 60 -27 -85 -59 -85 -16 72 88 -11 -66 96 -91 59 -59 -34 -75 14 -9 66 -49 -26 35 -6 -64 -12 31 -51 87 59 63 -47 -40 46 -14 22 -15 -33 52 -29 8 50 -51 -65 15 88 -70 22 2 63 32 83 -39 -1 -56 59 -24 -8 -66 69 -50 64 98 82 6 68 36 -37 -20 18 -25 -46 -90 29 28 41 -8 51 44 6 -84 41 78 -99 73 -27 46 -48 80 -96 27 -91 43 -94 81 -91 -79 89 -63 60 -57 -35 -65 -43 -64 -57 80 -80 96 64 -79 -94 -39 -68 -23 44 68 -87 -19 30 -25 -79 -40 -81 38 -65 -4 -76 46 -51 -25 -53 -78 30 -74 33 -52 5 24 33 36 31 14 88 57 -82 38 -80 -28 66 23 -54 -64 -71 1 54 -59 -30 -45 33 62 -89 55 -21 -31 89 39 -33 -58 -43 13 -49 35 -97 2 -35 50 68 -97 92 30 35 -29 25 25 0 -18 -15 -33 -33 -96 3 48 -56 -13 26 -82 -65 33 4 -10 2 5 -81 82 -25 39 29 52 -33 -37 -65 24 88 72 21 96 -63 -44 44 -15 -9 -50 95 27 71 -92 41 18 -26 21 -77 -74 22 -88 98 88 -11 50 44 -86 -46 56 -47 68 -69 -77 58 -90 -22 51 86 -32 -33 7 -63 45 24 -49 -79 1 59 98 81 3 71 28 -50 11 -94 13 64 20 -11 -16 91 -91 -47 -21 -30 37 -34 -62 26 -20 44 -82 43 1 28 48 -87 -70 -29 -68 -19 -64 22 42 4 73 47 -12 62 48 84 -61 -88 62 -27 80 -39 5 75 -62 -62 -83 -95 -4 -61 51 -1 21 96 -59 18 75 -88 19 -27 46 -21 -51 77 -25 11 88 -41 -55
800 190
-66 40 95 47 0 -9 -3 44 -19 -49 63 -50 70 -83 59 -77 56 54 -42 -65 35 88 65 61 36 46 -40 31 59 74 -63 1 -74 -26 60 63 -66 -37 -35 -20 -13 74 -67 -68 71 49 -46 10 9 -89 81 69 -3 -83 10 -62 -73 81 46 -19 -43 4 23 -10 4 -6 -3 84 35 -97 -74 -24 99 -88 -58 -15 32 -44 -38 91 58 79 -26 20 -35 -10 80 10 -44 29 10 56 15 49 59 48 -90 30 96 81 -19 -93 -30 -31 54 80 56 -10 -41 -29 3 21 10 14 2 41 39 -73 -42 95 16 64 17 48 85 -63 -59 87 -36 -79 -97 -13 -60 58 43 51 -34 -84 -42 61 -13 68 -61 -94 -9 88 99 -47 -40 65 -64 94 84 53 14 5 43 53 33 -1 25 5 95 87 -62 -18 21 -28 -95 -31 0 -90 -15 -47 94 95 42 96 4 73 -89 97 61 68 11 -18 -40 54 -3 -8 54 -70 55 86 -54 30 -8 6 -58 25 -25 33 4 -25 93 -10 -36 47 -98 55 -98 -48 69 27 -32 1 48 28 -25 -17 87 -21 -59 -19 -55 62 -15 -11 -69 64 42 -64 -3 48 -97 -3 44 -12 -46 -12 -61 -54 90 -13 -55 65 -47 -40 -25 84 -5 -11 -64 -4 6 -63 -96 -96 86 -97 -91 -39 -96 -42 20 97 -17 79 84 -96 56 62 29 38 19 9 -55 2 -80 77 26 29 -35 29 -48 13 38 -57 -37 -35 -87 -20 45 46 -22 -77 50 -43 -19 -8 -51 -24 -53 -8 80 99 41 -62 45 16 -84 -67 4 -23 36 -43 -56 -28 -52 0 -84 -53 -71 -16 76 88 77 -46 18 -58 52 -93 73 -70 -62 62 73 -76 83 17 -76 -71 -12 -87 -38 -37 51 -50 8 5 46 69 35 -20 41 -81 -94 74 -73 42 -11 -53 14 42 -80 45 -16 51 -63 -74 61 -73 -12 66 -14 1 -92 92 62 81 -34 -70 45 -54 -44 65 -35 -65 -43 -85 -44 86 92 94 -65 98 -7 54 93 13 -40 -47 -74 75 -47 26 -50 79 43 1 54 -11 -71 -65 25 -6 -14 -93 69 57 84 -12 99 -80 17 2 -85 84 -83 73 -33 -26 -84 -87 -43 74 -31 65 29 25 -32 -70 -45 -26 -5 90 31 37 92 25 -20 -15 -37 81 -30 14 86 32 -91 64 10 38 75 -14 -51 -6 -91 -74 6 95 14 -51 98 -88 -45 42 59 2 8 5 -7 -83 85 -79 -65 79 36 36 17 27 -77 -23 2 -22 93 -73 90 3 -66 18 -8 15 84 82 76 69 -83 41 -69 -99 94 -66 -29 -60 -55 -31 81 12 -50 -71 -9 32 32 30 -41 -15 2 21 55 -83 -64 79 -13 -15 -38 42 -27 -92 -53 13 3 82 14 -94 89 -37 -44 3 -7 72 8 -45 -42 -99 -11 41 -44 25 -79 -85 48 74 38 -1 -99 43 -41 -95 -78 30 10 -57 95 69 -53 95 -28 -98 50 -16 -25 -9 52 53 -2 -21 55 70 12 29 -46 -70 -94 93 -20 -98 -73 -16 -15 -8 -5 -85 59 62 -48 40 69 -21 -31 -12 -28 -1 -70 -31 90 -59 -21 -55 53 8 -14 99 -63 -50 -40 -2 26 -74 24 -86 -48 62 -43 6 92 1 66 41 73 -29 -6 -86 87 81 -69 -78 -65 -91 63 -60 -63 -13 -14 11 -49 57 24 -40 -55 -26 41 -45 50 19 -37 -68 93 -82 -39 -50 38 -96 2 -77 -10 -85 -12 -62 71 -79 -64 -9 -32 -20 -89 -60 -30 41 -45 42 73 11 63 -52 10 43 -83 -36 48 -39 -32 -16 60 -99 -27 65 -22 -91 -54 -71 -79 -44 -72 83 41 62 -74 40 40 -91 -33 -72 -86 -92 11 57 83 -57 -86 79 -15 -5 -76 -75 36 35 23 29 -23 54 90 -77 -17 80 -27 -82 57 -83 -36 49 -76 95 44 13 50 -54 31 -65 70 -3 -9 -43 77 99 -88 86 88 -20 -62 5 5 -5 95 88 -68 -66 -29 -95 91 19 -98 47 43 71 -6 70 -88 0 -97 0 -32 46 -79 -71 91 53 -52 28 20 -53
800 79
20 90 0 7 -14 -68 -56 -98 5 -83 45 -26 -56 99 62 76 77 41 -49 98 -25 43 -80 -63 -86 83 81 77 -44 76 51 92 71 -57 33 -87 74 95 76 91 56 98 -40 31 4 -42 -11 35 19 58 52 62 80 -32 67 -23 -1 -17 1 78 7 -13 59 -53 -45 -31 -9 75 3 -50 -82 -98 99 -78 15 6 29 41 -73 20 9 -68 -49 -13 -51 -80 -89 69 46 -88 -4 -36 -19 -26 27 62 2 7 -74 60 -36 10 -71 13 -79 -30 -52 73 -47 -15 50 63 60 7 95 11 -60 8 -6 0 -26 -25 -1 54 -49 27 0 55 13 -47 83 91 -84 -27 24 -32 62 -33 55 69 10 8 87 -74 78 -12 -32 -9 6 63 67 -84 52 50 -10 -15 15 -86 39 6 -34 83 25 86 -80 -65 -96 81 24 -59 50 -10 50 72 -8 -59 49 12 -86 -10 0 65 -82 -97 30 -44 -84 51 2 -28 54 -57 33 -83 -20 -37 -25 22 -53 -65 80 -69 67 51 -43 -84 70 -54 -62 -22 -34 -8 13 19 -53 -55 98 98 96 -39 -32 -41 16 -5 -36 -14 -38 83 4 23 -91 91 6 60 43 -93 23 -30 -34 70 -15 94 58 -62 83 -72 -67 -69 -57 -75 -28 29 -59 -95 47 -17 -2 -73 44 -75 -72 -6 -14 -64 56 -25 -63 40 -17 -17 -53 32 -49 -19 -92 72 93 -7 6 -32 -14 0 -15 0 80 -1 -55 -92 42 -49 58 2 -5 -63 -84 -26 56 28 -23 8 -50 -40 -47 14 -47 -28 -41 61 96 10 24 31 67 -56 39 45 -77 -51 21 -18 32 78 32 -72 15 61 -71 72 3 80 96 -36 -66 -50 -4 59 70 -62 28 -83 17 35 88 -78 -39 85 -39 -61 -60 -44 83 1 -41 -7 50 66 38 -60 13 -21 53 -40 -80 -50 -16 -5 -51 4 26 -66 6 48 38 -75 -52 55 -55 -50 0 -81 48 67 -49 -43 -39 3 -94 93 13 35 -17 -22 90 -64 -74 -11 36 -73 -6 60 -30 -42 -67 61 8 -49 -40 54 97 25 -16 -97 20 37 90 -24 -64 2 6 -16 -60 96 90 87 -69 10 -53 -89 -29 52 -27 96 -46 75 -62 72 10 79 19 87 82 -29 56 61 -96 -60 -93 -66 7 45 -86 -96 37 -96 45 -48 -84 -15 47 -29 -94 -70 46 -80 83 -27 -94 -17 -2 -40 0 27 70 76 -71 -65 46 -6 -76 51 -63 80 -54 -88 14 8 73 -54 -29 12 -39 -71 17 -83 -15 5 64 -87 87 -79 -8 -72 -74 76 -9 8 70 -86 -60 -32 -55 -57 27 90 24 -71 8 -65 74 -38 -33 35 -30 42 95 -70 -16 -23 -76 -13 87 -84 -32 -78 94 41 -66 -83 51 -39 4 -49 -92 68 90 20 -19 24 -57 58 -70 -35 -76 85 -47 78 37 -25 4 -50 27 -75 79 -50 -54 44 59 -13 97 -67 -27 -49 -25 99 -67 -27 -24 93 1 -93 -3 -32 -69 -51 48 15 16 93 -38 74 93 -5 3 74 46 -64 -8 12 -45 -96 86 -70 76 -47 7 -76 74 -22 -84 85 67 -79 49 5 -11 -89 -65 -51 -78 59 -23 89 -69 78 -60 83 17 -8 -11 -62 67 -20 66 -25 26 81 -20 3 34 -95 -49 -79 -46 -86 0 79 -55 -51 -27 69 -61 6 -72 -75 -43 -58 2 -11 76 -57 1 96 40 -81 -76 20 -52 22 -88 36 -21 23 -31 -75 -88 35 72 -50 83 79 -86 0 -30 16 72 1 -98 20 -63 -40 31 -46 11 68 84 9 -51 -62 -83 3 34 53 81 65 73 0 -32 61 -47 -93 -29 54 -63 18 -50 55 78 20 -86 -8 42 17 -7 22 59 89 -70 74 16 33 -66 3 0 8 -61 51 77 31 50 -94 -21 -2 31 30 73 -15 -55 88 -46 -46 17 -64 69 -34 0 33 12 -18 -16 43 -63 32 81 -77 -22 87 -25 -38 -98 66 -1 -77 -87 -60 -47 44 14 32 -49 -23 -85 15 -14 -58 25 67 76 95 -91 70 12 0 94 74 94 -67 -11 94 -87 42
800 66
-57 91 1 -94 11 44 -6 -15 23 70 28 49 -44 -99 -34 -4 -19 -15 94 -64 -21 -99 90 82 -31 19 -61 16 -26 14 77 52 66 -20 29 -70 98 -82 87 -1 21 29 93 87 -14 -31 -24 -91 3 -54 0 38 97 -38 -90 -55 -64 -46 -83 -80 -39 -40 -47 -57 46 -86 -88 49 -49 70 -79 3 -15 -4 86 99 -48 -92 -74 -97 13 -23 -59 -38 -65 0 39 -92 56 56 -85 -72 -46 -80 66 -96 -60 80 -97 -80 32 -58 -36 77 -51 -40 88 21 29 -10 78 75 30 9 -79 41 -23 34 -6 -56 -44 45 61 22 19 38 -90 87 -74 0 -91 16 46 77 61 62 -82 -93 -26 -38 -99 95 -42 62 35 -21 57 -44 -87 59 8 -9 81 38 -69 4 4 -58 -34 15 -35 0 26 99 18 -18 32 21 -82 -72 87 -72 -28 90 55 36 47 87 -80 91 -97 77 42 47 9 80 49 -40 -87 44 92 85 -16 17 10 99 22 -90 27 -41 -9 -85 74 -88 12 56 64 -96 65 -80 73 36 61 60 67 -77 -75 -39 -92 -63 63 13 -65 -59 -26 11 -24 -47 -77 25 65 -25 18 -42 96 -71 29 39 -97 -30 -43 -74 -40 56 -86 -65 -36 -92 8 69 91 64 -76 72 -55 48 95 21 -48 -56 58 -38 -64 1 68 77 -14 -84 49 67 10 -6 -42 -44 56 77 -22 -62 49 -11 -38 28 33 -47 -21 39 34 89 77 66 86 -49 62 -99 -26 28 50 -21 -22 66 -86 79 56 -96 -7 -67 -62 54 -31 -88 15 -26 -26 -48 67 -47 25 -26 -48 -14 -90 0 2 29 11 48 87 43 -26 17 -11 99 91 17 -53 -98 -17 -99 9 -10 -99 99 84 -3 87 56 84 -86 85 -19 38 85 21 -80 14 3 -48 -51 98 95 -26 -87 10 -90 28 38 80 22 -9 83 -44 -40 90 -77 49 77 -75 89 -89 85 -42 35 0 75 -64 84 -97 1 -19 31 2 95 -24 15 -16 82 76 32 80 -37 70 -53 -49 -59 85 36 51 -17 -20 93 37 -95 -97 -42 -39 -22 -53 -80 82 -71 82 -8 -95 -12 -62 -51 -85 12 78 64 -86 82 -65 93 54 20 28 73 -57 -38 -95 -18 40 -18 41 39 -20 -18 35 86 -80 29 86 83 -92 -63 -63 -23 -68 -25 24 89 37 82 24 66 26 -17 2 56 74 -85 -56 92 -49 -87 -33 22 36 46 25 17 -12 64 86 60 95 -49 -5 -76 62 -32 -92 69 10 89 -84 39 44 -62 27 43 71 25 90 35 69 0 -25 -90 -41 -23 89 74 -69 -15 11 70 -55 -63 -49 49 -21 -32 23 34 5 -94 71 -79 6 -88 -5 4 57 57 -70 -30 8 90 -85 0 33 37 63 48 -63 43 -98 -81 19 -67 46 -86 59 38 53 39 32 47 44 -69 36 29 12 42 -1 -73 -6 -2 40 14 -30 -83 33 62 30 38 44 0 81 -40 -4 -82 -77 81 -28 -62 53 -25 80 -16 19 76 25 24 -23 42 82 43 -13 76 -75 52 87 -67 -64 -77 90 -52 -34 78 -93 89 -49 34 12 3 52 -68 -84 -59 -19 37 -94 -80 65 -89 31 -33 15 -42 81 68 -5 25 72 43 -24 56 69 50 47 45 -23 11 50 70 -4 69 -27 3 -30 94 78 77 -38 -86 71 -65 13 37 -82 -99 98 0 -14 -76 54 2 72 -84 59 96 5 -29 90 86 73 -63 -57 -48 -18 67 94 -9 53 -29 15 -46 39 -42 -41 5 -69 90 83 -49 63 30 90 -28 -84 -7 -35 -23 81 7 50 41 85 46 75 26 64 0 96 -49 -42 84 -10 55 -78 17 31 -48 95 -36 43 -12 -20 -66 46 -1 72 70 46 -77 92 52 -57 -91 0 -26 -94 -54 4 35 88 42 74 46 90 -96 21 -9 -54 35 31 49 1 -92 -28 -59 68 -76 14 19 49 -90 68 -1 51 -76 99 -60 33 -9 -36 29 21 -51 -31 95 37 -50 36 80 -41 -74 86 96 -43 -84 77 -36 22 -38 -9 -33
800 500
-59 37 -81 25 -85 -21 7 45 -55 75 -33 -95 76 -72 -52 84 0 62 -20 -58 -3 -18 9 -1 73 73 43 -45 2 -47 77 17 -58 62 19 88 3 36 21 -32 66 -53 -78 81 67 -86 65 25 -84 -53 -63 -30 51 82 8 19 71 87 22 -34 -2 -37 -25 42 -5 -16 93 86 17 69 -34 3 -60 59 63 75 -67 36 30 5 -78 -55 -72 -15 -9 18 -24 -52 63 70 -10 -44 -61 -21 -11 78 -51 -60 -26 16 -12 82 -7 -73 -51 50 -93 90 -79 -50 -41 -80 14 -20 -21 80 -75 -74 2 57 -96 -66 -58 48 -67 -28 80 -4 54 87 -17 12 35 -78 -39 42 -99 28 -16 -95 -28 -95 84 -54 76 17 -14 89 -21 -90 7 99 -44 -64 8 -95 35 96 -41 -62 -97 -14 -61 -16 23 46 42 -89 29 98 -65 -78 87 24 29 2 17 41 -24 -17 -15 29 -13 -47 73 -32 42 43 -88 -62 5 48 84 57 51 -55 -91 -28 56 47 -73 -71 93 97 -85 -55 27 69 98 20 -53 20 65 -1 -77 2 83 -18 44 61 -31 -72 -73 -23 -19 -24 -23 -21 98 61 -74 -29 -93 85 -68 -66 -16 10 -83 -64 -29 80 89 -93 -76 66 70 60 -96 0 96 67 61 5 63 -51 62 -45 -37 91 -44 -15 53 -29 -77 -17 -52 -38 -15 -61 65 -23 -48 30 -10 -50 31 21 45 38 84 -48 44 1 -29 42 27 -73 37 61 -77 53 82 97 -29 -2 -94 1 -88 2 -16 16 61 -24 97 -49 -1 -87 -33 63 23 -27 19 9 -34 -28 -56 51 -38 -72 -12 -14 28 49 90 76 81 32 36 -59 -4 78 36 -34 4 62 79 82 30 22 -96 87 6 -30 -64 18 82 85 29 -97 -25 -53 39 64 20 95 89 46 -5 -90 -19 41 -8 23 -97 22 83 79 -64 -45 34 4 -74 -70 -80 -52 -21 -4 72 -71 0 44 -74 -58 22 -26 95 31 -33 52 -15 16 50 70 0 95 40 -87 66 56 -49 97 -64 -18 35 -15 27 38 -4 -51 7 -56 -38 65 -90 -98 -55 -40 -28 -21 -82 -65 -21 87 -17 82 89 75 34 37 13 -20 82 91 -19 -78 -2 63 -52 52 -92 97 25 62 -64 -36 -34 97 68 83 1 93 -10 82 58 -87 -21 85 8 -6 98 1 54 52 38 62 2 47 64 30 -17 -78 53 -37 -14 -89 41 96 -40 17 88 70 40 6 52 83 -57 -59 76 75 91 2 6 27 3 -77 -81 -86 -69 81 -33 -42 26 53 -2 45 97 78 -2 54 -7 -49 82 -13 31 77 59 59 26 93 44 74 -90 -49 -63 -50 38 -10 90 -76 17 90 -78 -15 65 84 50 -55 -64 38 -59 1 -44 -22 86 8 -56 -32 0 -42 59 -28 38 -55 40 -85 -85 1 -49 -64 -77 90 71 -72 26 -90 46 0 53 -42 0 -97 -65 15 77 -49 3 -40 -66 -51 -32 -83 63 -66 90 14 35 -27 13 14 73 -44 -58 -56 -54 -22 52 -16 -40 83 90 -72 -12 -29 -46 -15 -10 0 1 45 -15 -93 -24 -34 43 98 -67 62 74 -57 86 -91 89 68 0 97 85 35 51 26 40 -31 -47 -91 -88 -93 26 -74 -29 57 -60 97 96 -8 -7 45 -11 58 -73 32 -3 87 -63 -96 59 -25 11 -18 -60 6 -12 -66 79 35 78 -13 -97 62 17 56 63 96 57 33 -92 -88 -42 33 -82 25 -39 42 -42 -1 -15 36 -92 57 -51 -70 -82 52 -16 -98 5 11 -14 86 -63 -68 45 61 -41 -90 10 39 74 69 29 93 -44 84 62 19 -57 8 -96 -44 -88 -81 51 -95 65 68 36 -33 18 -95 87 10 -54 52 -87 40 35 30 -47 -65 94 -62 99 15 -65 1 -76 -50 -29 34 -50 97 52 -77 -5 67 -79 33 26 99 -62 -96 -12 22 0 11 -86 41 -87 90 64 47 -88 -26 81 -9 78 35 -56 -37 -17 60 -60 -42 -23 -96 -95 -82 -24 1 38 54 20 -63 -50 86 0 22 51 -12 2 61
""".strip())


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    ontime = len([1 for t in a if t <= 0])
    return 'NO' if ontime >= k else 'YES'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #t = int(input())
    t = int(STDIN_SIO.readline())

    for t_itr in range(t):
        #nk = input().split()
        #a = list(map(int, input().rstrip().split()))

        nk = STDIN_SIO.readline().split()
        a = list(map(int, STDIN_SIO.readline().rstrip().split()))

        n = int(nk[0])

        k = int(nk[1])


        result = angryProfessor(k, a)

        #fptr.write(result + '\n')
        print(result)

    #fptr.close()
