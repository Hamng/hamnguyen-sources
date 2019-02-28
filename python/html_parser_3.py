# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:53:34 2019

@author: Ham

HackerRanch Challenge: Detect HTML Tags, Attributes and Attribute Values

You are given an HTML code snippet of  lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute.
It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value
inside the HTML comment tags (<!-- Comments -->).
Comments can be multiline.
All attributes have an attribute value.

Input Format

The first line contains an integer , the number of lines in the HTML code snippet.
The next  lines contain HTML code.

Constraints


Output Format

Print the HTML tags, attributes and attribute values
in order of their occurrence from top to bottom in the snippet.

Format your answers as explained in the problem statement.

Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high

"""

from html.parser import HTMLParser
import io

STDIN_SIO = io.StringIO("""
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
""".strip())

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    "doc"
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print("->", a, ">", v) for a, v in attrs]

    #def handle_endtag(self, tag):
    #    print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        [print("->", a, ">", v) for a, v in attrs]

    #def handle_comment(self, data):
    #    comment = data.splitlines()
    #    if len(comment) > 1:
    #        print(">>> Multi-line Comment")
    #        [print(c) for c in comment]
    #    else:
    #        print(">>> Single-line Comment\n" + comment[0])

    #def handle_data(self, data):
    #    if data != "\n":
    #        print(">>> Data\n" + data)

if __name__ == '__main__':
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    #for _ in range(int(input())):
    #    parser.feed(input())
    for _ in range(int(STDIN_SIO.readline().strip())):
        parser.feed(STDIN_SIO.readline())
    parser.close()
