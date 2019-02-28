# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:53:34 2019

@author: Ham

HackerRanch Challenge: HTML Parser - Part 2

*This section assumes that you understand the basics
discussed in HTML Parser - Part 1

.handle_comment(data)
This method is called when a comment is encountered (e.g. <!--comment-->).
The data argument is the content inside the comment tag:

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          print "Comment  :", data


.handle_data(data)
This method is called to process arbitrary data
(e.g. text nodes and the content of <script>...</script> and <style>...</style>).
The data argument is the text content of HTML.

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print "Data     :", data

Task

You are given an HTML code snippet of N lines.
Your task is to print the single-line comments,
multi-line comments and the data.

Print the result in the following format:

>>> Single-line Comment
Comment
>>> Data
My Data
>>> Multi-line Comment
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:

Note: Do not print data if data == '\n'.

Input Format

The first line contains integer N, the number of lines in the HTML code snippet.
The next N lines contains HTML code.

Constraints


Output Format

Print the single-line comments, multi-line comments and the data
in order of their occurrence from top to bottom in the snippet.

Format the answers as explained in the problem statement.

Sample Input (also see STDIN_SIO below)

4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

Sample Output

>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]

"""

from html.parser import HTMLParser
import io

STDIN_SIO = io.StringIO("""
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
2
<div>Zabardasti Ka Testcase</div>
<br/>
""".strip())

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    "doc"
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        [print("->", a, ">", v) for a, v in attrs]

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        [print("->", a, ">", v) for a, v in attrs]

    def handle_comment(self, data):
        comment = data.splitlines()
        if len(comment) > 1:
            print(">>> Multi-line Comment")
            [print(c) for c in comment]
        else:
            print(">>> Single-line Comment\n" + comment[0])

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data\n" + data)

if __name__ == '__main__':
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    #for _ in range(int(input())):
    #    parser.feed(input())
    for _ in range(int(STDIN_SIO.readline().strip())):
        parser.feed(STDIN_SIO.readline())
    parser.close()
