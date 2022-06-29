# question url  :: https://leetcode.com/problems/fibonacci-number/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::


# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,


# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::;Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def fib(self, n):
        if n == 0 or n == 1:
            return n 
        return self.fib(n - 1) + self.fib(n - 2)