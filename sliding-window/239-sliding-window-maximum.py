# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


import collections
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    q = collections.deque()
    l = 0

    for r in range(len(nums)):

        # remove elements less than current
        while q and q[-1] < nums[r]:
            q.pop()

        q.append(nums[r])

        # valid window
        if r >= k-1:
            res.append(q[0])
            # max num in deque out of bounds, remove
            if q[0] == nums[l]:
                q.popleft()
            l+=1
            
            
    return res

print(maxSlidingWindow([1,3,1,2,0,5], 3))