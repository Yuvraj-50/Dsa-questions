# question url :: https://leetcode.com/problems/valid-parentheses/submissions/
# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 
#  examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {'(' : ')' , '[' : ']' , '{' : '}'}
        
        for el in s:
            if el in m:
                stack.append(el)
            else:
                if len(stack) == 0:
                    return False
                elif m[stack[-1]] == el:
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False