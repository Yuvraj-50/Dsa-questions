# quesiton url :: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

#  examples ;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;

# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) != 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        