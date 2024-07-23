# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

def lengthOfLIS(nums: list[int]) -> int:
    dp = [1] * len(nums)
    max_len = 0

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                # update dp, an increasing sequence detected
                dp[i] = max(dp[j]+1, dp[i])
                if dp[i] >= max_len:
                    max_len = dp[i]
    # return largest sequence detected
    return max(dp)
    


print(lengthOfLIS([7,7,7,7,7,7,7]))