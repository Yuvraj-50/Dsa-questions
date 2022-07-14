# question url :: https://leetcode.com/problems/flood-fill/

# question instruciton ::::::::::::::::::::::::::::::::::::::::

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

#  examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        og_color = image[sr][sc]
        if og_color == color :
            return image
        image[sr][sc] = color
        
#       left side 
        if sr > 0 and image[sr-1][sc] == og_color:
            self.floodFill(image , sr-1 , sc , color)
            
# up side
        if sc>0 and image[sr][sc-1] == og_color:
            self.floodFill(image, sr , sc-1 , color)
# right side
        if sr<len(image)-1 and image[sr+1][sc] == og_color:
            self.floodFill(image , sr+1 , sc, color)
# down side
        if sc<len(image[0])-1 and image[sr][sc+1] == og_color:
            self.floodFill(image , sr , sc+1, color)
        return image

        