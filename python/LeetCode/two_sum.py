# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:00:29 2021

@author: Ham

Leet Code #1. Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

from typing import List

import io

STDIN_SIO = io.StringIO("""
[2,7,11,15]
9
[3,2,4]
6
[3,3]
6
""".strip())

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            expected = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == expected:
                    return [i, j]

if __name__ == '__main__':
    while True:
        line = STDIN_SIO.readline().strip()
        if not line:
            break
        nums = list(map(int, line[1:-1].split(',')))
        target = int(STDIN_SIO.readline().strip())
        print("twoSum(", nums, target, ") returned",
              Solution().twoSum(nums, target))
