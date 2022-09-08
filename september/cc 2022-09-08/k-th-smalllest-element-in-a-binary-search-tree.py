// question url ::: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

// question instruction ::::::::::::::::::::::::::::::::::::::::::::::

// Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

// Example 1:
// Input: root = [3,1,4,null,2], k = 1
// Output: 1
// Example 2:

// Input: root = [5,3,6,2,4,null,null,1], k = 3
// Output: 3

# solutioN: :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, arr):
        if not root:
            return 
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 
        arr = []
        self.inorder(root, arr)
        return arr[k-1]