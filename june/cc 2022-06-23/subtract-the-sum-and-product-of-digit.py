# question url ::https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:

# Input: n = 234
# Output: 15 


# Input: n = 4421
# Output: 21

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::
import math
class Solution:
    def subtractProductAndSum(self, n) :
        s = 0
        p = 1
        while n:
            s += n % 10
            p *= n % 10
            n = math.floor(n / 10)
        return p - s