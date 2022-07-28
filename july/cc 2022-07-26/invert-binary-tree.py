# question url :: https://leetcode.com/problems/invert-binary-tree/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::

# Given the root of a binary tree, invert the tree, and return its root.

# .examples ::::::::::::::::::::::::::::::::::::::::::::::
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]


# Input: root = [2,1,3]
# Output: [2,3,1]

# solution ::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left , root.right = root.right , root.left
            return root