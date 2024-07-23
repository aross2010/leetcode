# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    
    l, h = 0, len(matrix) - 1
    m = h // 2
    row = 0
    # Search for the correct row
    while l <= h:
        # Target is in middle row
        if target >= matrix[m][0] and target <= matrix[m][len(matrix[m]) - 1]:
            row = m
            break
        # Target is in lower half
        elif target < matrix[m][0]:
            h = m - 1
        # Target is in upper half
        else:
            l = m + 1
        m = (l+h) // 2

    # Search for element in row
    l, h = 0, len(matrix[row]) - 1
    m = h // 2
    while l <= h:
        if target == matrix[row][m]:
            return True
        elif target < matrix[row][m]:
            h = m - 1
        else:
            l = m + 1
        m = (l+h) // 2

    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))