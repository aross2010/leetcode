# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# import collections
# from typing import List

# Approach: Run dfs and return a list of vertices in post order. Scan through the list. if an adj list of a vertex contains a vertex that has not been visited, then it is impossible. Else means all required pre-reqs have been taken.


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        
        postorder = collections.deque()
        
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
                    if not isValidNeighbor: postorder.append(stack.pop())
                # reached a dead end, no pointers to other vertices    
                else: postorder.append(stack.pop())

        visited.clear()

        # scan through post order. all adj lists of vertices should have already been visited when viewed. 
        # this means the courses have alerady been taken to take new course. 
        # if a course in the adj list has yet to been visited (taken), then it is impossible
        for i in range(len(postorder)):
             visited.add(postorder[i])
             adjList = dict.get(postorder[i])
             if adjList is not None:
                for vertex in adjList:
                    if vertex not in visited:
                       # post order not valid
                       return []
        i = numCourses
        while len(postorder) < i:
            if numCourses-1 not in visited:
                postorder.appendleft(numCourses-1)
            numCourses -=1
             
        
        return postorder
        
def main():
     print(findOrder(4, [[3,0],[0,1]]))

main()
