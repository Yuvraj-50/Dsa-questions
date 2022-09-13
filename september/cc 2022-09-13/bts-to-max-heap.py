# question url ::: https://practice.geeksforgeeks.org/problems/bst-to-max-heap/1

# question instructioN ::::::::::::::::::::::::::::::::::::::::::::::::::::


# Given a Binary Search Tree. Convert a given BST into a Special Max Heap with the condition that all the values in the left subtree of a node should be less than all the values in the right subtree of the node. This condition is applied on all the nodes in the so converted Max Heap.

# Example 1:

# Input :
#                  4
#                /   \
#               2     6
#             /  \   /  \
#            1   3  5    7  

# Output : 1 2 3 4 5 6 7 
# Exaplanation :
#                7
#              /   \
#             3     6
#           /   \  /   \
#          1    2 4     5
# The given BST has been transformed into a
# Max Heap and it's postorder traversal is
# 1 2 3 4 5 6 7.
# Example 2:

# Input :
#                  3
#                /   \
#               1     5
#                \   /  \
#                 2 4    6
#                         \
#                          7
# Output : 1 2 3 4 5 6 7 
# Exaplanation :
#                7
#              /   \
#             3     6
#           /   \  /   \
#          1    2 4     5
# The given BST has been transformed into a
# Max Heap and it's postorder traversal is
# 1 2 3 4 5 6 7.


# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
   
#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''
class Solution:
    def convertToMaxHeapUtil(self, root):
        arr  = []
        i = 0
        def inorder(root, arr):
            if root==None:
                return 
            inorder(root.left , arr)
            arr.append(root.data)
            inorder(root.right, arr)
        inorder(root, arr)
        
        def postorder(root): 
            nonlocal i
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            root.data = arr[i]
            i+=1
        postorder(root)