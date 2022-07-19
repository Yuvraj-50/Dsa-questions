# question url :: https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# example s;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;s;;;;;;;;;;;;;;

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode()
        temp = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy.next