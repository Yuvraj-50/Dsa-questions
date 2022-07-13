# question url :: https://leetcode.com/problems/merge-intervals/submissions/

# quesiotn instruction :::::::::::::::::::::::::::::::::::::::::::::::::::
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        interval = sorted(intervals , key = lambda elem : elem[0] )
        current_interval = interval[0]
        result = []
        
        for next_interval in interval:
            if next_interval[0] <= current_interval[1]:
                if next_interval[1] > current_interval[1]:
                    current_interval[1] = next_interval[1]
            else:
                result.append(current_interval)
                current_interval = next_interval
        result.append(current_interval)
        return result
    