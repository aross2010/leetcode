from typing import List


def lengthOfLIS(nums: List[int]) -> int:
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