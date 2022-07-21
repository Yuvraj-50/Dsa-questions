# question url :: https://leetcode.com/problems/reverse-linked-list-ii/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# example 1
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPair = dummy
        
        for i in range(left-1):
            leftPair = leftPair.next
        
        prev = None
        curr = leftPair.next
        for i in range(right-left+1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        
        leftPair.next.next = curr
        leftPair.next = prev
    
        return dummy.next