# question url :: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# question instruciton ::::::::::::::::::::::::;

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        ans = head.next
        curr = head
        nxt = head.next

        while nxt and nxt.next:
            nextPair = nxt.next
            nxt.next  = curr
            curr.next = nextPair.next if nextPair.next else nextPair

            curr = nextPair
            nxt = nextPair.next
        
        if nxt:
            nxt.next = curr
            curr.next = None
        return ans