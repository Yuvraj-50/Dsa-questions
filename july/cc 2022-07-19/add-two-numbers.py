# question url :: https://leetcode.com/problems/add-two-numbers/
# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# examples; ::::::::::::::::::::::::::::::::::::::::::::::::


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer =  dummy
        carry = 0
        
        while l1 or l2:
            l1Val  , l2Val = l1.val if l1 else 0 , l2.val if l2 else 0
            som = l1Val + l2Val + carry 
            carry = som//10
            pointer.next = ListNode(som%10)
            pointer = pointer.next
            l1 = l1.next if l1 else l1 
            l2 = l2.next if l2 else l2
        if carry :
            pointer.next = ListNode(carry)
        return dummy.next