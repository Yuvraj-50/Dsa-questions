# question url :: https://leetcode.com/problems/trapping-rain-water/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::;

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

#  examples ::::::::::::::::::::::::::::::::::::::::::::::::;;;


# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def trap(self, height: list[int]) -> int:
        left = []
        right = []
        curr_max_left = height[0]
        curr_max_right = height[len(height)-1]
        
        for next_max in height: 
            curr_max_left = max(next_max, curr_max_left)
            left.append(curr_max_left)
            
        for i in range(len(height)-1, -1, -1):
            next_max = height[i]
            curr_max_right = max(next_max , curr_max_right)
            right.insert(0, curr_max_right)
        
        result = 0
        for i in range(len(height)):
            result += min(left[i] , right[i]) - height[i]
        return result
            