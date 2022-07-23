# questionn url .:: https://leetcode.com/problems/maximum-product-subarray/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::

# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)
        max_prod = 1
        min_prod = 1
        
        for i in nums:
            tmp = max_prod*i
            max_prod = max(i*min_prod , i*max_prod , i)
            min_prod = min(i*min_prod , tmp , i)
            result = max(max_prod, min_prod , result)
        return result
        