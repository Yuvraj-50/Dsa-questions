# quesito url  https://leetcode.com/problems/contains-duplicate/

# question insturnciton 

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
#  example ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


class Solution:
    def containsDuplicate(self, nums):
        newValue = set(nums)
        if len(newValue) == len(nums):
            return False
        else: 
            return True
        