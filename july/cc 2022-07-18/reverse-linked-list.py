# question url :: https://leetcode.com/problems/reverse-linked-list/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# examples ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        return prev