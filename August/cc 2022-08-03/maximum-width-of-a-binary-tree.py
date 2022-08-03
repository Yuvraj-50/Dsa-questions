# question url :: https://devsnest.in/algo-challenges/maximum-width-of-binary-tree?tab=question

# question instruction :::::::::::::::::::::::::::::::::::::::::  Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format:
# First Parameter - TreeNode root

# Output Format:
# Return the number

# Example 1:
# img

# Input:
#     root = [2 4 6 5 9 null 3]
# Output:
#     4
# Example 2:
# img

# Input:
#     root = [2 4 6 5 null null 3 9 null 8]
# Output:
#     7
# Example 3:
# img

# Input:
#     root = [3 11 9 5]
# Output:
#     2

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

def solve(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    curr_level = [[root, 0]]
    width = 0
    while curr_level:
        nxt_level = []

        for i in range(len(curr_level)):
            if curr_level[i][0].left:
                nxt_level.append([curr_level[i][0].left, 2*curr_level[i][1]+1 ])
            if curr_level[i][0].right:
                nxt_level.append([curr_level[i][0].right , 2*curr_level[i][1]+2])

        if nxt_level:
            width = max(nxt_level[-1][1]-nxt_level[0][1]+1, width)
        curr_level = nxt_level
    return width