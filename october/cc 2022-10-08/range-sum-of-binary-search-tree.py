# question url :: https://leetcode.com/problems/range-sum-of-bst/description/
# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::


# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, low , high):
        if not root:
            return 0
        if root.val >= low and root.val <= high:
            return root.val + self.dfs(root.left, low, high) + self.dfs(root.right, low, high)
        return self.dfs(root.left, low, high) + self.dfs(root.right, low, high)
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)