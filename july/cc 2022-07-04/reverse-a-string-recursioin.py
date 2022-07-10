# question url :: https://leetcode.com/problems/reverse-string/
# question instruction ::::::::::::::::::::::::::::::::::::::::::::::

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

#  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::;;

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::;

class Solution:
    def reverseString(self, s):
        self.helper(s , 0 , len(s)-1)
        
    def helper(self, s , start ,end):
        if start >= end:
            return
        s[start] , s[end] = s[end] , s[start]
        self.helper(s, start+1 , end-1)
        