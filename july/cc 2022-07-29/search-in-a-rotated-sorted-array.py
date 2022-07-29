# quesiton url :: https://leetcode.com/problems/search-in-rotated-sorted-array/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# # examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        
        while s<=e:
            m = (s + e)//2
            if nums[m] == target:
                return m
            elif nums[s] <= nums[m]:
                if target >= nums[s] and target <= nums[m]:
                    e = m-1
                else:
                    s = m+1
            else:
                if target >= nums[m] and target <= nums[e]:
                    s = m+1
                else:
                    e = m-1
        return -1
    