# quesiton url :: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solution/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# examples; ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;
 
#  Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]


# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev = dummy 
        l , r  = head , head
        
        while r:
            if r.val == l.val:
                r = r.next
            elif l.next == r:
                prev.next = l
                prev = l
                l = r
            else:
                prev.next = r
                l = r
        if l.next:
            prev.next = None
        return dummy.next