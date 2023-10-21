#Course Schedule II

from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        self.inDegrees = [0] * n

        for (dest, src) in edges:
            self.adjList[src].append(dest)
            self.inDegrees[dest] += 1


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = Graph(prerequisites, numCourses)
        q = deque()
        order = []

        for i in range(numCourses):
            if graph.inDegrees[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            order.append(course)

            for neighbor in graph.adjList[course]:
                graph.inDegrees[neighbor] -= 1
                if graph.inDegrees[neighbor] == 0:
                    q.append(neighbor)

        if len(order) == numCourses:
            return order
        else:
            return []

