# question url :: https://leetcode.com/problems/3sum-closest/description/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        minDiff = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            low = i+1
            high = len(nums)-1
            while low < high:
                threesum = nums[i] + nums[low] + nums[high]
                if target == threesum:
                    closest = threesum
                    return closest
                if target < threesum:
                    high -= 1
                else:
                    low += 1
                temp = abs(threesum-target)
                if temp < minDiff:
                    minDiff = temp
                    closest = threesum
        return closest
git add 