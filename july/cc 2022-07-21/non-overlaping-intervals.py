# question url :: https://leetcode.com/problems/non-overlapping-intervals/

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;
# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        result = 0
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                result += 1
                prevEnd = min(prevEnd , end)
        return result