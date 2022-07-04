# question url https://leetcode.com/problems/search-insert-position/

# question instruciton ::::::::::::::::::::::::::::::::::::::::::::::::::::


# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

#  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end  = len(nums) - 1
        index = 0
        
        while start <= end:
            mid = end + (start  - end ) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                index = start = mid + 1
            else:
                end = mid - 1
        return index
        