# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:33:30 2019

@author: wizard2non2 in Discussion

HackerRanch Challenge: XML2 - Find the Maximum Depth

You are given a valid XML document, and you have to
print the maximum level of nesting in it.
Take the depth of the root as 0.

Input Format

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format

Output a single line,
the integer value of the maximum level of nesting in the XML document.

Sample Input (also see STDIN_SIO below)

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output

1

Explanation

Here, the root is a feed tag, which has depth of 0.
The tags title, subtitle, link and updated all have a depth of 1.
Thus, the maximum depth is 1.

Hamie's Notes:

I didn't solve the challenge, so cheated by reading thru the Discussion,
then adopted wizard2none's excellent solution. Also, I fixed main()
to not needing any globalvar, and starting from level==0.

"""

#import io
import xml.etree.ElementTree as etree

STDIN_SIO = """
12
<entry>
  <author>Harsh</author>
  <question>XML 2</question>
  <type>
  	<subtype>
    	<supersubtype>
        	Nesting
        </supersubtype>
    </subtype>
  </type>
  <description>This is related to XML parsing</description>
</entry>
""".strip()

def depth(elem, level):
    "doc"
    return max([level] + [depth(child, level + 1) for child in elem])


if __name__ == '__main__':
    STDIN_SIO = STDIN_SIO.split("\n", 1)[1:]            # discard 1st line
    #print(len(STDIN_SIO), "<" + STDIN_SIO[0] + ">")
    tree = etree.ElementTree(etree.fromstring(STDIN_SIO[0]))
    print(depth(tree.getroot(), 0))
