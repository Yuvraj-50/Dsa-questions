# question url :: https://leetcode.com/problems/middle-of-the-linked-list/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# # examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

#  solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            return slow.next
        else:
            return slow
            