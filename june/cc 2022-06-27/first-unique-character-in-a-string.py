# question url :: https://leetcode.com/problems/first-unique-character-in-a-string/

# question intruction:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# examples;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# solution;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] == 1:
                return s.index(i)
        return -1