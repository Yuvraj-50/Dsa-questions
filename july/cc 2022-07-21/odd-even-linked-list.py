# question url :: https://leetcode.com/problems/odd-even-linked-list/

# question instruciotn :::::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# examples ;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]



# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        even = head.next
        
        while even and even.next:
            temp = even.next
            
            even.next = even.next.next
            temp.next = odd.next
            odd.next = temp
            
            odd = odd.next
            even = even.next
        return head
            
            