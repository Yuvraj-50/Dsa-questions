# quesiton url :: https://leetcode.com/problems/container-with-most-water/submissions/

# quesiotn instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# examples ;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


# solution ;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height)-1
        max_water = 0
        while start < end:
            curr_water = min(height[start] , height[end]) * (end - start)
            max_water = max(curr_water , max_water)
            
            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                end -=1
                start +=1
                
        return max_water
                
        