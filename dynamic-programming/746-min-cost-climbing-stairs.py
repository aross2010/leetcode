from typing import List


def minCostClimbingStairs( cost: List[int]) -> int:

    dp = [cost[-2], cost[-1]]

    for i in range(len(cost) - 3, -1, -1):
        temp = dp[0]
        dp[0] = cost[i] + min(dp[0], dp[1])
        dp[1] = temp


    
    return min(dp[0], dp[1])

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))