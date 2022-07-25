# question url :: https://leetcode.com/problems/binary-tree-level-order-traversal/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# examples ::::::::::::::::::::::::::::::::::::::::::::::::::;;
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque([None, root])
        temp = []
        res = []
        while True:
            n = q.pop()
            if n:
                temp.append(n.val)
                if n.left:
                    q.appendleft(n.left)
                if n.right:
                    q.appendleft(n.right)
            else:
                res.append(temp)
                temp = []
                if q:
                    q.appendleft(None)
                else:
                    break
        return res