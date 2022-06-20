# question url :: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.

#  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Example 1:
# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6

# Example 2:
# Input: sentences = ["please wait", "continue to fight", "continue to win"]
# Output: 3


# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def mostWordsFound(self, sentences):
        maxNum = 0;
        for i in sentences:
            maxNum = max(maxNum , len(i.split(' ')))
        return maxNum
