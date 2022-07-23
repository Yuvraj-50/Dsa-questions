# question url :: https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# example s;::::::::::::::::::::::::::::::::::::::::::::::
# 1
# Input: head = [1,1,2]
# Output: [1,2]

# 2
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head