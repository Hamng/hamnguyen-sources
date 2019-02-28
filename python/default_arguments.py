# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:42:22 2019

@author: Ham

HackerRanch Challenge: Default Arguments

In this challenge, the task is to debug the existing code
to successfully execute all provided test files.

Python supports a useful concept of default argument values.
For each keyword argument of a function,
we can assign a default value which is going to be used
as the value of said argument if the function is called without it.
For example, consider the following increment function:

def increment_by(n, increment=1):
    return n + increment
The functions works like this:

>>> increment_by(5, 2)
7
>>> increment_by(4)
5


Debug the given function print_from_stream using the default value of one of its arguments.

The function has the following signature:

def print_from_stream(n, stream)

This function should print the first n values returned by
get_next() method of stream object provided as an argument.
Each of these values should be printed in a separate line.

Whenever the function is called without the stream argument,
it should use an instance of EvenStream class defined
in the code stubs below as the value of stream.

Your function will be tested on several cases by the locked template code.

Input Format

The input is read by the provided locked code template.
In the first line, there is a single integer Q denoting the number of queries.
Each of the following Q lines contains a stream_name followed by integer n,
and it corresponds to a single test for your function.

Constraints

Output Format

The output is produced by the provided and locked code template.
For each of the queries (stream_name, n),
if the stream_name is even then print_from_stream(n) is called.
Otherwise, if the stream_name is odd, then print_from_stream(n, OddStream()) is called.

Sample Input 0

3
odd 2
even 3
odd 5

Sample Output 0

1
3
0
2
4
1
3
5
7
9

Explanation 0

There are  queries in the sample.

In the first query, the function print_from_stream(2, OddStream()) is executed,
which leads to printing values 1 and 3 in separated lines
as the first two non-negative odd numbers.

In the second query, the function print_from_stream(3) is executed,
which leads to printing values 0, 2 and 4 in separated lines
as the first three non-negative even numbers.

In the third query, the function print_from_stream(5, OddStream()) is executed,
which leads to printing values 1,3,5,7 and 9 in separated lines
as the first five non-negative odd numbers.

"""

import io

STDIN_SIO = io.StringIO("""
5
odd 2
even 3
odd 5
even 4
even 2
""".strip())

class EvenStream(object):
    "doc"
    def __init__(self):
        self.current = 0

    def get_next(self):
        "doc"
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    "doc"
    def __init__(self):
        self.current = 1

    def get_next(self):
        "doc"
        to_return = self.current
        self.current += 2
        return to_return

# The broken prototype was print_from_stream(n, stream=EvenClass()).
# When the 1st time it's invoked without stream,
# it'll instantiate an EvenClass object, then *REMEMBER* it.
# Then when the next time it's invoked without stream,
# it will *NOT* instantiate a brand-new EvenClass object,
# but instead, *REUSE* the first-time-created EvenClass object;
# hence, as a result, it'll *CONTINUE* to count from where it left off last
# (instead of restart counting from 0).
# So for STDIN_SIO, the "even 4" (incorrectly) displays [6,8,10,12],
# then "even 2" (incorrectly) displays [14, 16].
# To fix, default stream=None,
# then it'll correctly instantatiate a brand-new EvenClass object
# (whenever stream is not specified).
# Also, when testing stream, should test specificly as "if stream == None"
# instead of "if not stream"
def print_from_stream(n, stream=None):
    "doc"
    if stream == None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


#for _ in range(int(input())):
#    stream_name, n = input().split()
for _ in range(int(STDIN_SIO.readline().strip())):
    stream_name, n = STDIN_SIO.readline().strip().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
