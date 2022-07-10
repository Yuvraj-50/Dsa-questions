# question url :: https://leetcode.com/problems/product-of-array-except-self/
# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# examples:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# solutioN:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        result = [1] * len(nums)
        
        for i, el in enumerate(nums):
            result[i] = prefix
            prefix *= el
            
        postfix = 1
        for i in range(len(nums) - 1 , -1 , -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result
            
        