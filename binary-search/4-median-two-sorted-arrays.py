# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1, i2, mid1, mid2 = 0, 0, 0, 0
        n = len(nums1) + len(nums2)

        # Traverse until the median point of the combined array
        for i in range(n//2 + 1):
            # Keep track of prev element incase median is the average of the middle two
            mid1 = mid2
            if i1 == len(nums1):
                mid2 = nums2[i2]
                i2 += 1
            elif i2 == len(nums2):
                mid2 = nums1[i1]
                i1 += 1
            elif nums2[i2] > nums1[i1]:
                mid2 = nums1[i1]
                i1 += 1
            else:
                mid2 = nums2[i2]
                i2 += 1
        if n % 2 == 0: return (mid1+mid2) / 2
        else: return mid2