# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# approach: use dfs to find adjacent neighbors that for an island. Mark as visited so no duplicate cells are visited.

import collections
from typing import List


def main():
        grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
        print(numIslands(grid))



def numIslands(grid: List[List[str]]) -> int:
    q = collections.deque()
    count = 0
    visited = set()
    if not grid:
         return 0
    
    def bfs(i, j):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q.appendleft((i, j))
        while q:
            indices = q.popleft()
            i, j = indices
            # scan neighboring cells
            for x, y in directions:
                nx, ny = i + x, j + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1" and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])): 
            # found a new island
            if grid[i][j] == "1" and not (i, j) in visited:
                 bfs(i, j)
                 count += 1

                    
                 
    return count


main()
