# question url ::: https://leetcode.com/problems/insert-interval/

# question instruction :::::::::::::::::::::::::::::::::::::::::::

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# examples; :::::::::::::::::::::::::::::::::::::::::::::::::::::;;

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if len(intervals) <= 0:
            return [newInterval]
        
        if intervals[len(intervals)-1][0] <= newInterval[0]:
            intervals.append(newInterval)
        else:
            for i in range(len(intervals)):
                if intervals[i][0] > newInterval[0]:
                    intervals.insert(i, newInterval)
                    break
                           
        current_interval = intervals[0]
        result = []
        for i in range(len(intervals)):
            if intervals[i][0] <= current_interval[1]:
                if intervals[i][1] > current_interval[1]:
                    current_interval[1] = intervals[i][1]
            else:
                result.append(current_interval)
                current_interval = intervals[i]
        result.append(current_interval)
        return result;
                    
                    