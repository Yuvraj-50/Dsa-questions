# question url :: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# questoin instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.


# # examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        row = len(grid)-1
        col = 0
        
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                count += (len(grid[0]) - col)
                row -= 1
            else:
                col += 1
        return count
            