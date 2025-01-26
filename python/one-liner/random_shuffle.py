# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:13:20 2020

@author: Ham

A one-liner to generate a random list of (unique) items.
print(*l) prints all items without the square brackets.
list() could be anything.
shuffle() requires a list so it can modify in-place;
i.e. NOT generating/returning a new list.
Better yet, use random.sample()

"""

python -c "import random; l=list(range(1,9)); random.shuffle(l); print(*l)"
python -c "import random; print(random.sample(range(1,53), 52))"

# Or, to get a list of N random integers between [min_int, max_int]
python -c "import random; print(random.sample(range(min_int, max_int + 1), N))"
