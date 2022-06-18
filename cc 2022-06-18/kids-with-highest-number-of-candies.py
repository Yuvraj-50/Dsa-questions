# question url :: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# Example 2:

# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.


# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_num  = max(candies);
        res = []
        for elem in candies:
            if ((elem + extraCandies) >= max_num):
                res.append(True)
            else:
                res.append(False)
        return res
        