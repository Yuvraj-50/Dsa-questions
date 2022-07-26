# question url :: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
        return res
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        self.helper(root1 , res)
        self.helper(root2, res)
        return sorted(res)