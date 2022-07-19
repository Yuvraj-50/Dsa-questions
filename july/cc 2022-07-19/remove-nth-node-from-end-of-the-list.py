# question url :: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# question insturction ::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        fast = dummy
        slow = dummy
        
        for i in range(n+1):
            if fast:
                fast = fast.next
            else:
                return head.next
            
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return dummy