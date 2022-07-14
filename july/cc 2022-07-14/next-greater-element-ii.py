# question url :: https://leetcode.com/problems/next-greater-element-ii/

# question instruciton ::::::::::::::::::::::::::::::::::::::::::::::::

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 
#  examples ;::::::::::::::::::::::::::::::::::::::::::::::::::::::::/::

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.

# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::;;


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stack = []
        result = [-1] * n
        for i in range(2*n):
            current = nums[i % n]
            if len(stack) == 0 :
                stack.append(i % n )
            else:
                if nums[stack[-1]] > current:
                    stack.append(i % n )
                while len(stack) > 0 and nums[stack[-1]] < current:
                    index = stack.pop()
                    result[index] = current
                stack.append(i % n)
        return result
                    