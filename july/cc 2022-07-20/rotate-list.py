# question url ::https://leetcode.com/problems/rotate-list/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Given the head of a linked list, rotate the list to the right by k places.


# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]


# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def cutinhalf(self, head , k):
        ans = head
        slow = head
        fast = head

        for i in range(k+1):
            fast = fast.next
            ans = ans.next

        while fast:
            slow = slow.next
            fast = fast.next
            ans = ans.next

        t = slow.next
        slow.next = None
        return t
    
    def lenght(self,head):
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 and not head:
            return None
        if k == 0 and head:
            return head
        if not head or not head.next:
            return head
        
        leng = self.lenght(head)
        k = k % leng

        lastElements = self.cutinhalf(head , k)
        ans = dummy = ListNode(123)

        while lastElements:
            dummy.next = lastElements
            lastElements = lastElements.next
            dummy = dummy.next

        dummy.next = head
        return ans.next