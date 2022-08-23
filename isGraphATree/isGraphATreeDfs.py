from typing import List


class Solution:
    def hasCycles(self, adjList):
        stack = [(0, 0)]
        visited = set()
        while stack:
            element, parent = stack.pop()
            visited.add(element)
            neighbours = adjList[element]
            for n in neighbours:
                if n not in visited:
                    stack.append((n, element))
                else:
                    if n != parent:
                        return True
        return False

    def isOneConnectedComponent(self, adjList, m):
        stack = [(0, 0)]
        visited = set()
        while stack:
            element, parent = stack.pop()
            visited.add(element)
            neighbours = adjList[element]
            for n in neighbours:
                if n not in visited:
                    stack.append((n, element))
        return len(visited) == m

    def edgesToAdjList(self, edges, n):
        adjList = [[] for i in range(n)]
        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)
        return adjList

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = self.edgesToAdjList(edges, n)
        hasCycle = self.hasCycles(adjList)
        oneConnectedComponent = self.isOneConnectedComponent(adjList, n)
        return not hasCycle and oneConnectedComponent