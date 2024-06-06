# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# import collections
# from typing import List

# Approach: run dfs to get topological order to find if a cycle exists. scan through vertices in topological order. if a vertex's adj list has a vertex that has not been visited in the topological order scan, then a cycle exists.


import collections
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect if a cycle occurs
        visited = set()
        stack = []
        dict = {}

        # create adjancency lists for vertices
        for i in range(len(prerequisites)):
            edgeFrom = prerequisites[i][0]
            edgeTo = prerequisites[i][1]
            if not dict.get(edgeFrom):
                dict.update({edgeFrom: {edgeTo}})     
            else:
                adjList = dict[edgeFrom]
                adjList.add(edgeTo)
                dict[edgeFrom] = adjList
        
        topOrder = collections.deque()
        
        # run dfs
        for key in dict:
            if key in visited:
                 continue
            visited.add(key)
            stack.append(key)
            while stack:
                current = stack[-1]
                list = dict.get(current)
                isValidNeighbor = False
                if list is not None:
                    for vertex in list:
                          if vertex not in visited:
                               isValidNeighbor = True
                               stack.append(vertex)
                               visited.add(vertex)
                               list.remove(vertex) # remove from list so you dont have to scan duplicate vertices
                               break
                    # all neighbors have already been visited      
                    if not isValidNeighbor: topOrder.appendleft(stack.pop())
                # reached a dead end, no pointers to other vertices    
                else: topOrder.appendleft(stack.pop())

        visited.clear()

        # Scan topo order. If an adj list contains a vertex that has yet to be scan through in the top order, then cycle exists
        for i in range(len(topOrder)):
             visited.add(topOrder[i])
             adjList = dict.get(topOrder[i])
             if adjList is not None:
                for vertex in adjList:
                    if vertex in visited:
                       return False
                    
                     
        
        return True
        
def main():
     print(canFinish(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))

main()
