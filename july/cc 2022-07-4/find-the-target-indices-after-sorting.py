# question url :: https://leetcode.com/problems/find-target-indices-after-sorting-array/

# question instruciton ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.


# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def targetIndices(self, nums, target):
        result = []
        self.merge_sort(nums)
        left_occurance = self.find_occurance(nums, target, True)
        right_occurance = self.find_occurance(nums, target, False)
        
        for x in range(left_occurance , right_occurance + 1):
            if x == -1:
                return []
            result.append(x)
        return result
        
    def find_occurance(self, nums, target, flag):
        start = 0
        end = len(nums)-1
        occurance = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                occurance = mid
                if flag:
                    end = mid-1
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return occurance
                    
                
        
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right  = nums[mid:]
        self.merge_sort(left)
        self.merge_sort(right)
        
        self.merge(left , right, nums)
        
    def merge(self , left , right , nums):
        i = 0
        j = 0
        k = 0
        
        while  i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1