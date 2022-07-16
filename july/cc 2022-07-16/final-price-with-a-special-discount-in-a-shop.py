# question url:: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# 
# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

#   examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Example 1:

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]

# ṣolutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        next_smallest = [0] * len(prices)
        stack = []
        result = []
        for i in range(len(prices)-1 , -1, -1):
            while len(stack)!=0 and stack[-1] > prices[i]:
                stack.pop()
            if len(stack)!= 0 and stack[-1] <= prices[i]:
                next_smallest[i] = stack[-1]
            stack.append(prices[i])
        for i in range(len(prices)):
            result.append(prices[i] - next_smallest[i])
        return result