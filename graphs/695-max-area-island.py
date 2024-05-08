# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Approach: Run BFS when approached with water. For every neighboring water cell in the BFS add to area. Return max area.


import collections
from typing import List


def main():
        grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        print(maxAreaOfIsland(grid1))
        grid2 = [[1]]
        print(maxAreaOfIsland(grid2))

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    def bfs(i, j):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q.appendleft((i, j))
        area = 0
        # if an island is solo, this will remain false
        isNeighbors = False
        while q:
            indices = q.popleft()
            i, j = indices
            # scan neighboring cells
            for x, y in directions:
                nx, ny = i + x, j + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
                    isNeighbors = True   
                    area += 1 

        if not isNeighbors:
                area += 1      
        return area

    q = collections.deque()
    maxArea = 0
    visited = set()
    if not grid:
        return 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])): 
            # found a new island
            if grid[i][j] == 1 and not (i, j) in visited:
                area = bfs(i, j)
                if area > maxArea:
                    maxArea = area
         
    return maxArea

main()
