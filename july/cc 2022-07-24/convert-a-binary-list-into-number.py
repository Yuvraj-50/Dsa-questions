# question url :: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;

# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next :
            num = num*2 + head.next.val
            head = head.next
        return num