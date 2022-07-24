# question url :: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# questoin instruciton ::::::::::::::::::::::::::
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# examples ::::::::::::::::::::::::::::::::::::::::::::::::
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# solution ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKthNode(self, head, k):
        fast = head
        slow = head
        
        for i in range(k):
            fast = head.next
            head = head.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
            
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_from_right = self.findKthNode(head, k)
        k_from_left = head
        
        for i in range(k-1):
            k_from_left = k_from_left.next
            
        tmp = k_from_right.val
        k_from_right.val = k_from_left.val
        k_from_left.val = tmp
        
        return head
            