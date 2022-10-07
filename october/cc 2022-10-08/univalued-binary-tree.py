# question url :: https://leetcode.com/problems/univalued-binary-tree/description/

# question instruction ::::::::::::::::::::::::::::::::::::::::


# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

# Example 1:


# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:


# Input: root = [2,2,2,5,2]
# Output: false


# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, val):
        if not root:
            return True
        if root.val != val:
            return False
        return self.dfs(root.left , val) and self.dfs(root.right, val)
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        return self.dfs(root, val)