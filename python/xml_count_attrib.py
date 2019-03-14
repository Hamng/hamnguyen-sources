# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:26:30 2019

@author: Ham

HackerRanch Challenge: XML 1 - Find the Score

You are given a valid XML document, and you have to print its score.
The score is calculated by the sum of the score of each element.
For any element, the score is equal to the number of attributes it has.

Input Format

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format

Output a single line, the integer score of the given XML document.

Sample Input (also see STDIN_SIO below)

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output

5

Explanation

The feed and subtitle tag have one attribute each - lang.
The title and updated tags have no attributes.
The link tag has three attributes - rel, type and href.

So, the total score is 1 + 0 + 1 + 3 + 0 == 5.

There may be any level of nesting in the XML document. To learn about XML parsing, refer here.

NOTE: In order to parse and generate an XML element tree, use the following code:

>> import xml.etree.ElementTree as etree
>> tree = etree.ElementTree(etree.fromstring(xml))
Here, XML is the variable containing the string.
Also, to find the number of keys in a dictionary, use the len function:

>> dicti = {'0': 'This is zero', '1': 'This is one'}
>> print (len(dicti))

2

"""

#import io
import xml.etree.ElementTree as etree

STDIN_SIO = """
15
<feed xml:lang='en'>
  <entry>
    <author gender='male'>Harsh</author>
    <question type='medium' language='python'>XML 2</question>
    <description type='text'>This is related to XML parsing</description>
  </entry><entry>
    <author gender='male'>Harsh</author>
    <question type='medium'>XML 2</question>
    <description type='text'>This is related to XML parsing</description>
  </entry><entry>
    <author gender='male'>Harsh</author>
    <question type='medium'>XML 2</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>
""".strip()

def get_attr_number(node):
    "doc"
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    STDIN_SIO = STDIN_SIO.split("\n", 1)[1:]            # discard 1st line
    #print(len(STDIN_SIO), "<" + STDIN_SIO[0] + ">")
    tree = etree.ElementTree(etree.fromstring(STDIN_SIO[0]))
    print(get_attr_number(tree.getroot()))
