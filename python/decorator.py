# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:28:39 2019

@author: Ham

HackerRanch Challenge: Standardize Mobile Number Using Decorators

Let's dive into decorators!
You are given N mobile numbers.
Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number.
Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer N, the number of mobile phone numbers.
N lines follow each containing a mobile number.

Output Format

Print N mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230

Concept

Like most other programming languages, Python has the concept of closures.
Extending these closures gives us decorators, which are an invaluable asset.
You can learn about decorators in 12 easy steps here.
To solve the above question,
make a list of the mobile numbers and pass it to a function
that sorts the array in ascending order.
Make a decorator that standardizes the mobile numbers
and apply it to the function.

"""

import io

STDIN_SIO = io.StringIO("""
3
07895462130
919875641230
9195969878
""".strip())

def wrapper(f):
    def fun(l):
        #print(l)
        res = []
        for x in l:
            if x.startswith('+'):
                x = x[1:]           # remove the "+" prefix
            xint = int(x)
            if xint < 10000000000:
                x = str(xint + 910000000000)    # if less than 10 digits
            res.append("+" + x[:2] + " " + x[-10:-5] + " " + x[-5:])
        #print(res)
        return f(res)
        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    #l = [input() for _ in range(int(input()))]
    l = [STDIN_SIO.readline().strip()
         for _ in range(int(STDIN_SIO.readline().strip()))]
    sort_phone(l)
