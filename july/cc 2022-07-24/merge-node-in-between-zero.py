# question url :: https://leetcode.com/problems/merge-nodes-in-between-zeros/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

# Return the head of the modified linked list.

# question examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head.next
        s = 0
        dummy = ListNode(0)
        res = dummy
        while pointer:
            s += pointer.val
            if pointer.val == 0:
                dummy.next = ListNode(s)
                s = 0
                dummy = dummy.next
            pointer = pointer.next
        return res.next