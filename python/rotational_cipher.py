# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:01:10 2020

@author: Ham

Facebook Coding Practice: Rotational Cipher

One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678

"""

#import math
# Add any extra import statements you may need here
import string


# Add any helper functions you may need here


def rotChar(ch, fact):
    ordi = ord(ch)
    if ch.isdigit():
      return string.digits[(ordi - ord('0') + fact) % len(string.digits)]
    elif ch.isupper():
      return string.ascii_uppercase[(ordi - ord('A') + fact)
                                 % len(string.ascii_uppercase)]
    elif ch.islower():
      return string.ascii_lowercase[(ordi - ord('a') + fact)
                                 % len(string.ascii_lowercase)]
    return ch

def rotationalCipher(input, rotation_factor):
  # Write your code here
  #upper = string.ascii_uppercase + string.ascii_uppercase
  #rot_alpha = rotation_factor % len(string.ascii_uppercase)
  #digit = string.digits + string.digits
  #rot_digit = rotation_factor % len(string.digits)
  #res = ''
  #for v in input:
  #  o = ord(v)
  #  if v.isdigit():
  #    v = string.digits[(o - ord('0') + rotation_factor) % len(string.digits)]
  #  elif v.isupper():
  #    #v = upper[o - ord('A') + rot_alpha]
  #    v = string.ascii_uppercase[(o - ord('A') + rotation_factor)
  #                               % len(string.ascii_uppercase)]
  #  elif v.islower():
  #    #v = upper[o - ord('a') + rot_alpha].lower()
  #    v = string.ascii_lowercase[(o - ord('a') + rotation_factor)
  #                               % len(string.ascii_lowercase)]
  #  res += v
  return ''.join([rotChar(ch, rotation_factor) for ch in input])











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  