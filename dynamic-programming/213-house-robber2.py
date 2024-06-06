# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3

from typing import List


def rob(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]
    
    # take the max of house robber 1 from [0] to [-2] and [1] to [-1] since first and last el are neighbors
    
    def rob_linear(nums: List[int]):
        nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            prev = nums[i-1]
            curr = nums[i] + nums[i-2]
            nums[i] = max(prev, curr)
        return nums[-1]

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

print(rob([1,2,3,4,5,1,2,3,4,5]))