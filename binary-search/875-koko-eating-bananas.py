# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)
    min_speed = r

    while l <= r:
        m = (l + r) // 2
        # Calculate if k is valid
        hours_to_finish = 0
        for pile in piles:
            hours_to_finish += math.ceil(pile / m) # Hours to finish pile at k rate
            if hours_to_finish > h: break
        
        # Valid k, shift left to find lower k
        if hours_to_finish <= h:
            min_speed = m
            r = m - 1
        else: l = m + 1


    return min_speed

print(minEatingSpeed([30,11,23,4,20], 5))