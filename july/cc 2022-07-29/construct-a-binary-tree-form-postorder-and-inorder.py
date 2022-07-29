# question url :: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        has = {el:i for i, el in enumerate(inorder) }
        
        def get_tree(ps, pe, ins, ine):
            
            has_idx = has[postorder[ps]]
            l = has_idx - ins
            r = ine - has_idx
            
            root = TreeNode(postorder[ps])
            root.left = get_tree(ps-1-r, pe, ins, has_idx-1) if l else None
            root.right = get_tree(ps-1, ps-r, has_idx+1, ine) if r else None
            return root
            
        return get_tree(len(postorder)-1, 0, 0, len(inorder)-1)