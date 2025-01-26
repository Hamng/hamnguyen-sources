# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 08:19:21 2021

@author: Ham

LeetCode #35. Search Insert Position

Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""

from typing import List

import io

# 2 lines for each testcase; 2nd line is the expected result.
STDIN_SIO = io.StringIO("""
[1,3,5,6]
5
2
[1,3,5,6]
2
1
[1,3,5,6]
7
4
[1,3,5,6]
0
0
[1]
0
0
""".strip())


class Solution_linear:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v >= target:
                return i
        return i+1

class Solution:
    # Hmm, this binary search isn't much faster than linear
    def searchInsert(self, nums: List[int], target: int) -> int:
        lft = 0
        rgt = len(nums) - 1
        while lft <= rgt:
            mid = (lft + rgt) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                lft = mid + 1
            else:
                rgt = mid - 1
        return lft


if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break

        exec("lst=" + line)
        target = int(STDIN_SIO.readline().strip())
        found = Solution().searchInsert(lst, target)
        expected = int(STDIN_SIO.readline().strip())
        print('@' + str(found) + ':', lst[:found], target, lst[found:])
        if found != expected:
            print("!= @" + str(expected))
