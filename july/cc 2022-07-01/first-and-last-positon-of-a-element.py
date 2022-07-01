# quesiton instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def searchRange(self, nums, target):
        first_occurance = self.find_first_occurance(nums , target)
        last_occurance = self.find_last_occurance(nums , target)
        return [first_occurance, last_occurance]
        
    def find_first_occurance(self, nums, target):
        start = 0
        end = len(nums) - 1
        first_occurance = -1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                first_occurance = mid
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return first_occurance
            
        
    def find_last_occurance(self , nums , target):
        start = 0
        end = len(nums) - 1
        last_occurance = -1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                last_occurance = mid
                start = mid + 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid = 1
        return last_occurance