# quesiton url  :: https://leetcode.com/problems/shuffle-string/submissions/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# solutOIN ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def restoreString(self, s, indices) :
        string = ''
        for i in range(len(s)):
             string += s[indices.index(i)]
        return string
            