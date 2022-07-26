# quesiton url :: https://leetcode.com/problems/same-tree/

# quesiton instruction ::::::::::::::::::::::::::::::::::::::::::::::

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Input: p = [1,2], q = [1,null,2]
# Output: false

# solutoin ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return 0
        if not p and not q:
            return 1
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right , q.right):
            return 1
        else:
            return 0