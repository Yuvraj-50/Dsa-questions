# question url :: https://leetcode.com/problems/rotate-image/

# quesiton instruction ::::::::::::::::::::::::::::::::::::::::::;;;;;;;;
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 
#  examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;
# Example 2:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


# solution ;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        for i in matrix:
            i.reverse()
