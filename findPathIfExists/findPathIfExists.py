
import collections

# https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3893/


class Solution(object):
    def edgesToAdjList(self, edges, n):
        res = [[] for _ in range(n)]
        for start, end in edges:
            res[start].append(end)
            res[end].append(start)
        return res

    # O(E+V)
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        # O(E)
        neighbours = self.edgesToAdjList(edges, n)
        visited = {source}
        stack = [source]
        # O(V)
        while stack:
            element = stack.pop(0)
            if element == destination:
                return True
            for neighbour in neighbours[element]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
        return False