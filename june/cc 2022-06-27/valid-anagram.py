# question url :: https://leetcode.com/problems/valid-anagram/

# question instruction:::::::::::::::::::::::::::::::::::::::::::::::::::::::::;
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
#  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# solutioN::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def isAnagram(self, s, t) :
        first = sorted(list(s))
        second = sorted(list(t))
        return first == second