# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:59:25 2020

@author: Ham

Facebook Coding Exercises: [Greedy Algorithms] Slow Sums

Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the worst possible penalty for a given input.
Signature:
int getTotalTime(int[] arr)
Input:
An array arr containing N integers, denoting the numbers in the list.
Output format:
An int representing the worst possible total penalty.
Constraints:
1 ≤ N ≤ 10^6
1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array.
The sum of values of N over all test cases will not exceed 5 * 10^6.
Example
arr = [4, 2, 1, 3]
output = 26
First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
Add 9 + 1 for a penalty of 10. The penalties sum to 26.

Algorithm:
    Assuming arr[] contains all non-negative values.
    To maximize the overall penalty, we need to maximize the sum of individual pairs.
    Hence, for each iteration, we sum up the highest 2 values.
    Then after replacing the 2 highests with their sum, that sum becomes the new highest.
    So for the next iteration, the new sum will be the previous sum plus the next highest.
    So for the example, the pair-penalty would be:
          4+3            7 penalty
         (4+3)+2         9
        ((4+3)+2)+1     10
    Sum up all penalties together, and factoring: (4+3)*3 + (2)*2 + (1)*1
    Still the same penalty if reverting the order: (1)*1 + (2)*2 + (3+4)*3
    That means if we sort arr[] in ascending order, the total penalty would be:
        a0*1 + a1*2 + a2*3 + ... + (a[-2] + a_last)*(n-1)
    The last term could be expanded to be:
        + ... + a[-2]*(n-1) + a_last*(n-1)
    That means we could iterate upto (and including) the 2nd-from-last,
    then add in the final adjustment: + a_last*(n-1)
    Expanding the new last term again:
        + ... + a[-2]*(n-1) + a_last*n - a_last
    So, the final algorithm is iterating thru the entire arr[],
    then subtract the last adjustment: - a_last
"""

def getTotalTime(arr):
    # Complexity: O(sorting(arr[]) + N)
    arr.sort()
    #print(arr)
    #sum = 0
    #for i, v in enumerate(arr):
    #    # i is 0-based so need to +1
    #    sum += (v * (i + 1))
    #    #print(i, v, sum)
    #return sum - arr[-1]
    #return sum([v * (i + 1) for i, v in enumerate(arr[:-1])]) + (arr[-1]*(len(arr)-1))
    return sum([v * (i + 1) for i, v in enumerate(arr)]) - arr[-1]
  









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
