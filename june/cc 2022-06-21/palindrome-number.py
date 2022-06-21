# question url :: https://leetcode.com/problems/palindrome-number/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
 
#  question examples ::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr =  list(str(x))
        reverseArr = arr[::-1]
        return True  if arr == reverseArr else False
        