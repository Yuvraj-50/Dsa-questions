# question url :: https://leetcode.com/problems/remove-duplicate-letters/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# question examples :::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:
# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occurance = {}
        present = set()
        
        for i , el in enumerate(s):
            last_occurance[el] = i
        
        for i , el in enumerate(s):
            if el not in present:
                while stack and stack[-1] > el and last_occurance[stack[-1]] > i:
                    temp = stack.pop()
                    present.remove(temp)
                stack.append(el)
                present.add(el)
        return "".join(stack)
        