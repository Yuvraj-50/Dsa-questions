# question url https://leetcode.com/problems/next-permutation/


# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return 
        while nums[j] <= nums[i - 1]:
            j -= 1
            
        nums[i - 1] , nums[j] = nums[j] , nums[i - 1]
        
        nums[i:] = nums[len(nums)-1:i-1:-1]