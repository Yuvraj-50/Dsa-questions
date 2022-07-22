# question url :: https://leetcode.com/problems/intersection-of-two-linked-lists/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]


# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def make_ll_equal(self, l1, l2):
        p1 , p2 = l1, l2
        while p1 or p2:
            if p1:
                p1 = p1.next
            else:
                n = ListNode(0)
                n.next = l1
                l1 = n 
            if p2:
                p2 = p2.next
            else:
                n = ListNode(0)
                n.next = l2
                l2 = n
        return l1 , l2
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1.val and not l2.val:
            return l1 if l1.val else l2
        
        l1 , l2 = self.make_ll_equal(l1 , l2)
        any_l2 = True
        
        while any_l2:
            any_l2 = False
            
            l1_p , l2_p = l1, l2
            prev = None
            
            while l1_p:
                som = l1_p.val + l2_p.val
                l1_p.val = som%10
                l2_p.val = som//10
                any_l2 = any_l2 or bool(l2_p.val)
                prev = l2_p
                l1_p , l2_p = l1_p.next , l2_p.next
                
            prev.next = ListNode(0)
            if l2.val:
                n = ListNode(0)
                n.next = l1
                l1 = n
            else:
                l2 = l2.next
        return l1
            