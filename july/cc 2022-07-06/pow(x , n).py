# question url :: https://leetcode.com/problems/powx-n/
# question instruction ;;;;;;;;::::::::::::::::::::::::::::::::::::::::::;;;;;

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def myPow(self, x: float, n: int) -> float:
        isnneg , isxneg = n < 0 , x < 0
        x , n = abs(x) , abs(n)
        if n == 0:
            return 1.0
        half_ans = self.myPow(x , n // 2)
        if n % 2 == 1:
            ans = half_ans * half_ans * x
        else:
            ans = half_ans * half_ans
        if isxneg and x % 2 == 1:
             ans = -ans
        if isxneg :
            ans = 1/ans
        return ans