import collections

# https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3893/


class Solution(object):
    def edgesToAdjList(self, edges, n):
        res = [[] for _ in range(n)]
        for start, end in edges:
            res[start].append(end)
            res[end].append(start)
        return res

    def dfs(self, source, dest, adjList, visited):
        if source == dest:
            return True
        for n in adjList[source]:
            if n not in visited:
                visited.add(n)
                if self.dfs(n, dest, adjList, visited):
                    return True
        return False

    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        neighbours = self.edgesToAdjList(edges, n)
        visited = set([source])
        return self.dfs(source, destination, neighbours, visited)