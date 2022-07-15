# question url :: https://leetcode.com/problems/rotting-oranges/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# 
# Example 1:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 2:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        fresh_orange = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_orange += 1
                if grid[i][j] == 2:
                    q.appendleft((i, j , 0))
        
        if fresh_orange == 0:
            return 0
        
        directions = {(1,0) , (-1, 0) , (0 , 1) , (0 , -1)}
        
        
        while q:
            o_i , o_j , time = q.pop()
            for i, j in directions:
                new_i , new_j = o_i + i , o_j + j 
                
                if -1<new_i<rows and -1<new_j<cols :
                    if  grid[new_i][new_j] == 1:
                        fresh_orange -= 1
                        grid[new_i][new_j] = 2
                    
                        if fresh_orange == 0:
                            return time + 1
                        q.appendleft((new_i, new_j , time+1))
        return -1