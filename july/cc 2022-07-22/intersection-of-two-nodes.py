# question url :: https://leetcode.com/problems/intersection-of-two-linked-lists/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:

# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:

# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

# example s;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        while headA:
            s.add(id(headA))
            headA = headA.next
        while headB:
            if id(headB) in s:
                return headB
            headB = headB.next
        return None
            