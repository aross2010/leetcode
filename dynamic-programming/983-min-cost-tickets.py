# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

# Train tickets are sold in three different ways:

# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

 

# Example 1:

# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.
# Example 2:

# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total, you spent $17 and covered all the days of your travel.

import math
from typing import List


def mincostTickets(days: List[int], costs: List[int]) -> int:
    
    max_day = days[-1]
    min_costs = [0] * (max_day + 1)

    days_set = set(days)

    for i in range(1, max_day + 1):
        if i not in days_set:
            min_costs[i] = min_costs[i-1]
        else: 
            min_costs[i] = min(
                min_costs[i-1] + costs[0], # add one extra day to the previous cost
                min_costs[i-7] + costs[1] if i - 7 >= 0 else costs[1], # add a 7-day pass to the cost of 7 days ago OR just the cost of a 7-day pass will cover all the days
                min_costs[i-30] + costs[2] if i - 30 >= 0 else costs[2] # add a 30-day pass to the cost of 30 days ago OR just the cost of a 30-day pass will cover all the days
            )


    return min_costs[-1]

print(mincostTickets([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28], [3,13,45])) # 11
