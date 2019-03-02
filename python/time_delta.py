# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:40:37 2019

@author: Ham

HackerRanch Challenge: Time Delta

When users post an update on social media, such as a URL, image, status update etc.,
other users in their network are able to view this new post on their news feed.
Users can also see exactly when the post was published,
i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones,
this can be confusing.
You are given two timestamps of one such post that
a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone.
Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.

Constraints

Input contains only valid timestamps

Output Format

Print the absolute difference (t1 - t2) in seconds.

Sample Input 0 (also see STDIN_SIO)

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output 0

25200
88200

Explanation 0

In the first query, when we compare the time in UTC for both the time stamps,
we see a difference of 7 hours.
which is 7x3600 seconds or 25200 seconds.

Similarly, in the second query,
time difference is 5 hours and 30 minutes for time zone adjusting
for that we have a difference of 1 day and 30 minutes.
Or 24x3600 + 30x60 = 88200

"""

import io
from dateutil import parser

STDIN_SIO = io.StringIO("""
11
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Fri 11 Feb 2078 00:05:21 +0400
Mon 29 Dec 2064 03:33:48 -1100
Wed 12 May 2269 23:22:15 -0500
Tue 05 Oct 2269 02:12:07 -0200
Sat 14 Sep 2126 00:36:44 +1400
Wed 22 Jun 2050 23:18:57 -0100
Sat 17 Sep 2107 18:52:42 +0530
Wed 24 Apr 2199 15:00:11 -0900
Sat 24 Aug 2080 00:35:31 +1030
Mon 12 Jan 1998 01:22:02 -0700
Thu 16 Jul 2026 06:28:56 -0930
Sun 20 Apr 2149 00:02:39 -0400
Sat 09 Jun 1979 12:33:03 +0200
Sat 28 Dec 2120 16:55:13 +0500
Thu 19 Sep 2199 10:47:49 +0330
Sun 15 May 2016 02:21:14 +0630
Sun 23 Nov 2110 22:33:19 -1100
Sun 22 Oct 2141 05:14:53 +1100
""".strip())

# Complete the time_delta function below.
def time_delta(t1, t2):
    d1 = parser.parse(t1)
    #print(d1)
    d2 = parser.parse(t2)
    #print(d2)
    return str(abs(int((d1 - d2).total_seconds())))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #t = int(input())
    #for t_itr in range(t):
    #    t1 = input()
    #    t2 = input()
    #    delta = time_delta(t1, t2)
    #    fptr.write(delta + '\n')
    #fptr.close()

    for _ in range(int(STDIN_SIO.readline().strip())):
        print(time_delta(STDIN_SIO.readline().strip(),
                         STDIN_SIO.readline().strip()))
