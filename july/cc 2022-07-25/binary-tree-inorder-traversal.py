# question url :: https://leetcode.com/problems/binary-tree-inorder-traversal/

# questoin instruction :::::::::::::::::::::::::::::::::::::::::::::

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# examples; ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::
# 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
        return res
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = self.helper(root, [])
        return result 