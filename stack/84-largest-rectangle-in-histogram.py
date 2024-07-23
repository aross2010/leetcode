# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Example 2:
# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

def largestRectangleArea(heights: list[int]) -> int:
    stack = [] # store (index, height of rectangle)
    max_area = 0

    for i, h in enumerate(heights):
        start = i # how far back the height can go before a lower height
        while stack and h < stack[-1][1]:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index)) 
            start = index # where that height can start from 
        stack.append((start, h))

    # traverse tuple
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
 
    return max_area

print(largestRectangleArea([5,4,4,6,3,2,9,5,4,8,1,0,0,4,7,2]))