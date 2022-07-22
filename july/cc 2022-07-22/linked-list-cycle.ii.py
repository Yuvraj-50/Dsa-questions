# question url :: https://leetcode.com/problems/linked-list-cycle-ii/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

# example s;;;;;;;;:::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow  = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None