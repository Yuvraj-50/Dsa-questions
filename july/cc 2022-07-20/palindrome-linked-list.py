# question url :: https://leetcode.com/problems/palindrome-linked-list/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a singly linked list, return true if it is a palindrome.


# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Input: head = [1,2,2,1]
# Output: true


# solution ::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def divide(self, head):
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = head
        h = self.divide(dummy)
        
        prev = None
        curr = h

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True