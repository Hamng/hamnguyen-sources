# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:56:48 2019

@author: Ham

HackerRanch Challenge: Validating and Parsing Email Addresses

(Similar to but different from Challenge: Validating Email Addresses With a Filter)

A valid email address meets the following criteria:

It's composed of a username, domain name, and extension
assembled in this format: username@domain.extension
The username starts with an English alphabetical character,
and any subsequent characters consist of one or more of the following:
alphanumeric characters, -, ., and _.
(The other Challenge doesn't allow dot.)
The domain and extension contain only English alphabetical characters.
(The other Challenge allows digits in domain, and doesn't restrict extension.)
The extension is 1, 2, or 3 characters in length.
Given N pairs of names and email addresses as input,
print each name and email address pair having a valid email address on a new line.

Hint: Try using Email.utils() to complete this challenge.
For example, this code:

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))

produces this output:

('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>

Input Format

The first line contains a single integer, N, denoting the number of email address.
(The other Challenge has emails only.)
Each line i of the N subsequent lines contains a name and an email address
as two space-separated values following this format:

name <user@email.com>

Constraints

Output Format

Print the space-separated name and email address pairs
containing valid email addresses only.
Each pair must be printed on a new line in the following format:

name <user@email.com>

You must print each valid email address in the same order as it was received as input.

Sample Input (also see STDIN_SIO)

2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output

DEXTER <dexter@hotmail.com>

Explanation

dexter@hotmail.com is a valid email address,
so we print the name and email address pair received as input on a new line.
virus!@variable.:p is not a valid email address
because the username contains an exclamation point (!)
and the extension contains a colon (:).
As this email is not valid, we print nothing.

"""

import email.utils
import re
import io

STDIN_SIO = io.StringIO("""
33
1 brian-23@hackerrank.com
2 britts_54@hackerrank.com
3 its@gmail.com1
mike13445@yahoomail9.server
rase23@ha_ch.com
daniyal@gmail.coma
thatisit@thatisit
8 <lara@hackerrank.com>
dheeraj <dheeraj-234@gmail.com>
crap <itsallcrap>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
mattp <matt23@@india.in>
harsh <.harsh_1234@rediff.in>
harsh <-harsh_1234@rediff.in>
vineet <vineet.iitg@gmail.com>
vineet <vineet.iitg@gmail.co>
vineet <vineet.iitg@gmail.c>
shashank <shashank@9mail.com>
shashank <shashank@gmail.9om>
shashank <shashank@gma_il.com>
shashank <shashank@mail.moc>
shashank <shashank@company-mail.com>
shashank <shashank@companymail.c_o>
vin <vineet@>
vineet <vineet@gmail.com>
vineet <vineet@gma.il.co.m>
vineet <vineet@gma-il.co-m>
vineet <vineet@gma,il.co@m>
vineet <vineet@gmail,com>
vineet <.vin@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>
""".strip())

def fun(s):
    """doc"""
    #print('=' + s + '=')
    if s.count('@') != 1:
        return False

    user, web = s.split('@')

    if not re.match(r"[a-z][\w\.-]*$", user, flags=re.ASCII | re.IGNORECASE):
        # Also, empty user fails the match, so will go thru here
        return False

    if web.count('.') != 1:
        # Also, empty web fails the match, so will go thru here
        return False

    if re.match(r"[A-Za-z\.]+$", web):
        # ok to include dot in pattern since already verified exactly 1 dot
        pass
    else:
        return False

    _, ext = web.split('.')
    #print("user=<" + user + ">", "site=<" + site + ">", "ext=<" + ext + ">")

    return len(ext) < 4

if __name__ == '__main__':
    #for _ in range(int(input().strip())):
    #    name, emai = email.utils.parseaddr(input().strip())
    for _ in range(int(STDIN_SIO.readline().strip())):
        name, emai = email.utils.parseaddr(STDIN_SIO.readline().strip())
        if name and fun(emai):
            print(email.utils.formataddr((name, emai)))
