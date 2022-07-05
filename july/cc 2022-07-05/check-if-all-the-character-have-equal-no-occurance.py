# quesiton url :: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

# quesiton instruction :::::::::::::::::::::::::::::::::::::::::::::::::::;

# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;
# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for i, el in enumerate(s):
            if el in dic:
                dic[el] += 1
            else:
                dic[el] = 1
        return all(x == (list(dic.items())[0][1]) for x in dic.values());