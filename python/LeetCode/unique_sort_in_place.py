# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 08:53:27 2021

@author: Ham

LeetCode #26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that
each element appears only once and returns the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference,
which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.


Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.

"""

from typing import List

import io

# 2 lines for each testcase; 2nd line is the expected result.
STDIN_SIO = io.StringIO("""
[1,1,2]
[1,2]
[0,0,1,1,1,2,2,3,3,4]
[0, 1, 2, 3, 4]
""".strip())


class Solution:
    # speed: fast because doing only 1 "del" operation.
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # A most trivial solution could be:
        #   nums = sorted(list(set(nums)))
        #   return len(nums)
        # But this is where the pass-by-reference comes to play.
        # In C/C++, this function would be removeDuplicates(int *nums).
        # So callee can definitely change the content pointed to by nums.
        # However, if callee points nums to a new area as nums=malloc(100),
        # that has *NO* impact on caller's original nums[]
        # So that's a WRONG solution!

        l = len(nums)
        if l < 2:
            return l

        # Convert nums[] to a set, which removes duplications.
        # If lens of both are the same, no work needed, just return len
        st = set(nums)
        #print(st)
        len_set = len(st)
        if l == len_set:
            return l

        # Else, sort the set, then copy 1 element at a time to nums[]
        # then return the new len
        for i, v in enumerate(sorted(st)):
            nums[i] = v
        del nums[len_set:]
        return len_set


class Solution_forward:
    # speed: slow because doing the "del" operation 1 item at a time
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 1
        ahead = nums[0]
        while i < len(nums):
            cur = nums[i]
            if ahead == cur:
                del nums[i]
                #nums.pop(i)
            else:
                ahead = cur
                i += 1
        return len(nums)

class Solution_backward:
    # speed: slow because doing the "del" operation 1 item at a time
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = len(nums)
        ahead = None
        while i:
            cur, ahead = ahead, nums[i-1]
            i -= 1
            if ahead == cur:
                nums.pop(i)
        return len(nums)


if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break
        exec("lst=" + line)
        Solution().removeDuplicates(lst)
        print(len(lst), lst)

        if not (line := STDIN_SIO.readline().strip()):
            break
        exec("expected=" + line)
        if expected != lst:
            print('F:', len(expected), expected)
