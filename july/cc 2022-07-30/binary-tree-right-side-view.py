# question url :: https://leetcode.com/problems/binary-tree-right-side-view/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::;

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100 

# solution ;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRightSide(self, root, m , level):
        if root:
            m[level] = root.val
            self.getRightSide(root.left, m , level+1)
            self.getRightSide(root.right, m , level+1)
            
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        m = {}
        self.getRightSide(root,m , 0)
        res = []
        for i in range(len(m)):
            res.append(m[i])
        return res