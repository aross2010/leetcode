# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

# from typing import List


def dailyTemperatures(temperatures: List[int]) -> List:
    stack = []
    res = [0 for _ in temperatures]
    stack.append(0)

    for i in range(1, len(temperatures)):

        if not stack:
            stack.append(i)
            continue
        
        # traverse down the stack, finding the differences between the next greatest index (day)
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index

        stack.append(i)

    # the days with no greater temp in the future will remain zero

    return res


print(dailyTemperatures([73,74,75,71,69,72,76,73]))