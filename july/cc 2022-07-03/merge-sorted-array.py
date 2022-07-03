# question url :: https://devsnest.in/algo-challenges/merge-sorted-array

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# solutIOn :::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;
class Solution:
    def merge(self, arr1, m , arr2, n):
        i = (m-1)
        j = (n-1)
        k = (m+n)-1
        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1
        while i >= 0:
            arr1[k] = arr1[i]
            i -= 1
            k -= 1
        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1
        return arr1