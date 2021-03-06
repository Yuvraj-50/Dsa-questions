# question url :: https://leetcode.com/problems/two-sum/

# question instruction::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#  examples ;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# solutioN:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return i , j


# approch 2 with hash hap ::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def twoSum(self, nums, target) :
        dic = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in dic:
                 return i , dic[remaining]
            else:
                dic[nums[i]] = i