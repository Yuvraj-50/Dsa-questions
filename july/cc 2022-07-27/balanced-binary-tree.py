# question url ::: https://leetcode.com/problems/balanced-binary-tree/submissions/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# #  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightOfBinaryTree(self, root, s):
        if not root:
            return s
        lh = self.heightOfBinaryTree(root.left, s+1)
        if lh == -1:
            return -1
        rh = self.heightOfBinaryTree(root.right, s+1)
        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x = self.heightOfBinaryTree(root, 0)
        if x == -1:
            return False
        else:
            return True