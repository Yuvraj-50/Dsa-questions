# question url :: https://leetcode.com/problems/missing-number/

# quesiton instructioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

#  question examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum_we_have = sum(nums)
        actual_sum = 0
        for i in range(len(nums) + 1):
            actual_sum += i
        return actual_sum - sum_we_have