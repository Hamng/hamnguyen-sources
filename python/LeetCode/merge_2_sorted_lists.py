# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:11:34 2021

@author: Ham

LeetCode #21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

"""

from typing import List

import io

# 3 lines for each testcase. 1st 2 lines are the 2 sorted array.
# 3rd line is the expected merged result.
STDIN_SIO = io.StringIO("""
[1,2,4]
[1,3,4]
[1, 1, 2, 3, 4, 4]
[]
[]
[]
[]
[0]
[0]
[13,23,47,50,68,71,82,95]
[13,24,45,49,49,68,70]
[13, 13, 23, 24, 45, 47, 49, 49, 50, 68, 68, 70, 71, 82, 95]
""".strip())


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next if next else None

    @staticmethod
    def from_list(lst: List = None):
        # can't declare return type as '-> ListNode' yet???
        if lst:
            # bad, .pop() destroys lst[] (by popping out all elements)
            #val = lst.pop(0)
            #return ListNode(val=val, next=ListNode.create_list(lst) if lst else None)
            return ListNode(val=lst[0], next=ListNode.from_list(lst[1:]))
        else:
            return None

    def to_list(self) -> List:
        if not self:
            return None
        else:
            nxt = self.next
            return [self.val] + ([] if not nxt else nxt.to_list())

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2) if l1.next else l2
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next) if l2.next else l1
            return l2


class Solution_list:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # Convert both links to lists[], append them together,
        # sort the combined, then return the link from the sorted list
        lst = l1.to_list() + l2.to_list()
        lst.sort()
        return ListNode.from_list(lst)


if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break
        exec("lst=" + line)
        lnk1 = ListNode.from_list(lst)
        #print(lst, lnk1)
        print('1:', lnk1.to_list() if lnk1 else None)

        if not (line := STDIN_SIO.readline().strip()):
            break
        exec("lst=" + line)
        lnk2 = ListNode.from_list(lst)
        print('2:', lnk2.to_list() if lnk2 else None)

        merged = Solution_list().mergeTwoLists(lnk1, lnk2)
        merged = merged.to_list() if merged else None
        print('M:', merged)

        if not (line := STDIN_SIO.readline().strip()):
            break
        exec("lst=" + line)
        if not lst:
            lst = None
        if merged != lst:
            print('F:', lst)
