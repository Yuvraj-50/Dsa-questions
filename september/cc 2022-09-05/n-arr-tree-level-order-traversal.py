# question url :: https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

#  solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


    """
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        q = deque([root])
        res = []
        while q:
            temp = []
            for i in range(len(q)):
                el = q.pop()
                if el:
                    temp.append(el.val)
                if el.children:
                    x = el.children
                    for  i in x:
                        q.appendleft(i)
            res.append(temp)
        return res