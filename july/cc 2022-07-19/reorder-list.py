# question url :: https://leetcode.com/problems/reorder-list/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev , curr = None , head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev , curr = curr , nxt
        return prev
        
    def cutinhalf(self, head):
        if head == None or head.next == None:
            return None
        slow  = head
        fast = head.next
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            slow = slow.next
        t = slow.next
        slow.next = None
        return t
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        second = self.cutinhalf(head)
        second = self.reverse(second)
        first = head
        
        while second:
            temp = second.next
            second.next = first.next
            first.next = second
            first = first.next.next
            second = temp
        return head
        
            