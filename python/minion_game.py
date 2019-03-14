# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:18:13 2019

@author: thomas_nystrand in Discussion

HackerRanch Challenge: The Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string S.
Note: The string S will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA

Sample Output

Stuart 12

Note :
Vowels are only defined a 'AEIOU'
In this problem, 'Y' is not considered a vowel.

"""

if __name__ == '__main__':
    st = input().strip()

    vowels = 'AEIOU'.upper()
    l = len(st)
    kevin = sum(l-i for i, c in enumerate(st) if c in vowels)
    stuart = sum(l-i for i, c in enumerate(st) if c not in vowels)
    #stuart = int(l*(l + 1)/2 - kevin)

    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Stuart', stuart)
