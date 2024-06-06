# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1    

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    mins = [0]*(amount+1)
    coins.sort()

    if not amount: 
        return 0
    
    for i in range(1, amount+1):
        options = set()
        for coin in coins:
            diff = i - coin
            if diff == 0:
                options.add(1)
            elif diff < 0 or mins[diff] < 0: 
                continue
            else:
               options.add(mins[diff] + mins[coin])
        
        if not options:
            mins[i] = -1
        else:
            mins[i] = min(options)
        
        options.clear()

    return mins[amount]

print(coinChange([1,2,5], 11))