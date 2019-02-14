# One-liner to count UPPERCASE letters in a file
# VERY IMPORTANT on Windows: **MUST** use double-quotations to quote the Python codes:

python -c "import sys; print(sum(1 for lines in open(sys.argv[1]).readlines() for c in lines if c.isupper()))" filename

# Fancier using regex
python -c "import sys; import re; print(sum(len(re.split('[A-Z]',lines))-1 for lines in open(sys.argv[1]).readlines()))" filename

# Even fancier, doing so for many files
python -c "import fileinput; import re; print(sum(len(re.split('[A-Z]',lines))-1 for lines in fileinput.input()))" file(s)...
