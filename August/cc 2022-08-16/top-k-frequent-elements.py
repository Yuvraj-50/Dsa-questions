# question url ::  https://leetcode.com/problems/top-k-frequent-elements/
# 
# # question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::
# # 
# # Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
  
#   solution:::::::::::::::::::::::::::::::::::::::::::::::

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        
        heap = []
        for i in frequency:
            if len(heap) < k:
                heapq.heappush(heap, (frequency[i] , i))
            else:
                if heap[0][0] < frequency[i]:
                    heapq.heappush(heap, (frequency[i] , i))
                    heapq.heappop(heap)
        
        return [x[1] for x in heap]