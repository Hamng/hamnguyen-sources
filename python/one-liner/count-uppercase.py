# One-liner to count UPPERCASE letters in a file
# VERY IMPORTANT on Windows: **MUST** use double-quotations to quote the Python codes:

python -c "import sys; print(sum(1 for lines in open(sys.argv[1]).readlines() for c in lines if c.isupper()))" filename

# Fancier using regex
python -c "import sys; import re; print(sum(len(re.split('[A-Z]',lines))-1 for lines in open(sys.argv[1]).readlines()))" filename

# Even fancier, doing so for many files
# why the -1?  The number of elements in the post-split list is always 1 more than num of matches
# E.g. no matches => not splitted => len=1, count=0
# single matched: lines='   A  wha ' => [before_match, after_match] => count=len-1=1
# This works even if matched at begin of string (e.g. lines='A   ' => before_match='')
# or matched at end (lines='   A' => after_match='')
# or both (lines='A' => before_ and after_ are both '')
python -c "import fileinput; import re; print(sum(len(re.split('[A-Z]',lines))-1 for lines in fileinput.input()))" file(s)...

# Geez, not sure why I used re.split???  Better version (don't need weird -1):
python -c "import fileinput; import re; print(sum(len(re.findall('[A-Z]',lines)) for lines in fileinput.input()))" file(s)...
