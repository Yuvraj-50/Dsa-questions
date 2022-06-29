# quesiton url :: https://devsnest.in/algo-challenges/binary-search

# quesiton instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Given an array of integers nums which are sorted in ascending order, and an integer target, write a function to search target in nums. If the target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input:
#     6
#     -1 0 3 5 9 12
#     9
# Output:
#     4
# Explanation:
#     Explanation: 9 exists in nums and its index is 4

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def solve(n, nums, target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1