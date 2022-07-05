# quesiton url :: https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# question instruciton::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 
#  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
 
#  solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for i in sentence:
            if i not in dic:
                dic[i] = 0
        return len(dic) == 26