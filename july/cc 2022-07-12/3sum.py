# question url  :: https://leetcode.com/problems/3sum/submissions/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 
#  examples; :::::::::::::::::::::::::::::::::::::::::::::::::::::;;;

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i,a in enumerate(nums):
            if i == 0 or i > 0 and a != nums[i - 1]:
                left , right =  i + 1 , len(nums)-1
                while left < right:
                    threeSum = a + nums[left] + nums[right]
                    if threeSum > 0:
                        right -= 1
                    elif threeSum < 0:
                        left += 1
                    else:
                        result.append( [a , nums[left] , nums[right]] )
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left -1]:
                            left += 1
                        while left < right and nums[right] == nums[right +1]:
                            right -= 1
        return result