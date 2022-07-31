# question url : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 
#  solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque([None,root])
        res = []
        ans = []
        while True:
            node = q.pop()
            if node:
                ans.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            else:
                res.append(ans)
                ans = []
                if q:
                    q.appendleft(None)
                else:
                    break
        for i in range(len(res)):
            if i%2==1:
                res[i].reverse()
        return res