# question url :: https://leetcode.com/problems/remove-linked-list-elements/submissions/

# quesiton instrucition :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# solutoiN using recursive :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from xml.dom.minicompat import NodeList


class Solution:
    def removeElements(self, head: Optional[NodeList], val: int) -> Optional[NodeList]:
        if not head:
            return head
        
        if head.val == val:
            return self.removeElements(head.next , val)
        else:
            newHead = self.removeElements(head.next, val)
            head.next = newHead
        return  head


# using iterative method;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[NodeList], val: int) -> Optional[NodeList]:
        curr = head
        prev = None
        
        while curr:
            if prev == None and curr.val == val:
                head = head.next
            elif curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head