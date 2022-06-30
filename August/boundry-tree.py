# Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order:

# Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree over the right subtree.
# Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
# Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.
# Note: If the root doesn’t have a left subtree or right subtree, then the root itself is the left or right boundary.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format :
# First Parameter - root , root of the tree

# Output Format :
# Return the array of boundary nodes in clock-wise direction.

# Example 1:
# Input:
#     1 2 3 4 5 6 7 null null 8 9
# Output:
#     1 2 4 8 9 6 7 3
# Explanation:
# img

# Example 2:
# Input:
#     1 2 null 4 9 6 5 null 3 null null null null 7 8
# Output:
#     1 2 4 6 5 7 8
# Constraints :
# n == Number of nodes.
# 1 <= n <= 105
# 1 <= node.val <= 105.
# Expected Time Complexity : O(n).
# Expected Space Complexity : O(Height of the tree).


# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;

def traverseLeft(root, ans):
    if not root:
        return 
    if not root.left and not root.right:
        return 
    ans.append(root.val)
    if root.left:
        traverseLeft(root.left, ans)
    else:
        traverseLeft(root.right, ans)

def traverseLeaf(root, ans):
    if not root:
        return 
    if not root.left and not root.right:
        ans.append(root.val)
    traverseLeaf(root.left , ans)
    traverseLeaf(root.right, ans)

def traverseRight(root, res):
    if not root:
        return  
    if not root.left and not root.right:
        return 
    traverseRight(root.left , res)
    traverseRight(root.right, res)
    res.append(root.val)

def solve(root):
    ans = []
    if not root:
        return None
    ans.append(root.val)
    traverseLeft(root.left, ans)
    traverseLeaf(root.left, ans)
    traverseLeaf(root.right, ans)
    traverseRight(root.right, ans)
    return ans 