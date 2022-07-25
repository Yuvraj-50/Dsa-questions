# question url :: https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/
# question instruction :::::::::::::::::::::

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]


# solution :::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root , result):
        if root:
            self.helper(root.left, result)
            self.helper(root.right, result)
            result.append(root.val)
        return result
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = self.helper(root, [])
        return res
        