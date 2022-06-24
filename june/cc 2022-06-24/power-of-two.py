# question url :: https://leetcode.com/problems/power-of-two

# question instruction ::::::::::::::::::::::::::::::::::::::::::;

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16

# solutioN ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def isPowerOfTwo(self, n):
        if n == 0 or n < 0: return False
        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True