# question url :: https://leetcode.com/problems/recover-binary-search-tree/submissions/
# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

# Example 1:


# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:


# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

#  solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, lis):
        if not root:
            return lis
        self.inorder(root.left, lis);
        lis.append(root)
        self.inorder(root.right, lis)
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        lis = []
        
        self.inorder(root , lis)
        first = 0
        second = 0
        
        for i in range(1,len(lis)):
            first = i;
            if lis[i-1].val > lis[i].val:
                break
        node1 = lis[first-1];
        for i in range(len(lis)-1, -1, -1):
            second = i
            if lis[i-1].val > lis[i].val:
                break
        node2 = lis[second]
        
        node1.val , node2.val = node2.val , node1.val
        return root;
    