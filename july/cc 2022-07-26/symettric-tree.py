# quesiton url :: https://leetcode.com/problems/symmetric-tree/

# /question instruciton ;::::::::::::::::::::::::::::::::::::::::

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def match(self, p, q):
        if (not p and q) or (p and not q):
            return 0
        if not p and not q:
            return 1
        if p.val == q.val and self.match(p.left , q.right) and self.match(p.right , q.left):
            return 1
        else:
            return 0
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1
        return self.match(root.left, root.right)