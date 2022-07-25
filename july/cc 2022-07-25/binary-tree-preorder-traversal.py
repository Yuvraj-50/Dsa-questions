# question url :: https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
# question instruction :::::::::::::::::::::::::::::::::::::::::::::::

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, result=[]):
        if root:
            result.append(root.val)
            self.helper(root.left, result)
            self.helper(root.right, result)
        return result
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = self.helper(root, [])
        return res
        