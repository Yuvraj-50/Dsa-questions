# question url : https://leetcode.com/problems/maximum-subarray/

# question instruction :::::::::::::::::::::::::::::::::::::::::::'

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

#  examples ;::::::::::::::::::::::::::::::::::::::::::::::::;;
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1

# solutoiN:::::::::::::::::::::::::::::::::::::::::::::::::::::::

# first try ::::::
class Solution:
    def maxSubArray(self, nums) :
        prevSum = 0
        output = []
        for i in range(len(nums)):
            if prevSum < 0:
                prevSum = 0
            prevSum = prevSum + nums[i]
            output.append(prevSum)
        return max(output) 
