# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:40:13 2019

@author: Ham

HackerRanch Challenge: collections.Counter()

Task

O is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay M amount of money
only if they get the shoe of their desired size.

Your task is to compute how much money O earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated
list of all the shoe sizes in the shop, might be duplicated.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size
desired by the customer and M, the price of the shoe.

Constraints


Output Format

Print the amount of money earned by O.

Sample Input (see stdin_sim below)

Sample Output

200

"""

from collections import Counter

stdin_sim = """
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
"""

stdin_sim = stdin_sim.strip().splitlines()

if __name__ == '__main__':
    sold = 0
    #input()                # discarded, don't really need number of shoes
    #shoes = Counter(input().split())
    #for _ in range(int(input())):
    #    shoe, cost = input().split()
    stdin_sim.pop(0)        # discarded, don't really need number of shoes
    shoes = Counter(stdin_sim.pop(0).split())
    stdin_sim.pop(0)        # discarded, don't really need number of customers
    while stdin_sim:
        shoe, cost = stdin_sim.pop(0).split()
        #print(cost, shoe)
        if shoe in shoes:
            remain = shoes[shoe]
            if remain > 0:
                sold += int(cost)
                shoes[shoe] = remain - 1

    print(sold)
