class DisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.rank = [1 for i in range(size + 1)]
        self.connectedComponents = size

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.connectedComponents -= 1
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.rank[rootY] += 1
                self.root[rootX] = rootY
            return True
        else:
            return False

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        unified_edges = []
        for idx, weight in enumerate(wells):
            unified_edges.append((weight, 0, idx + 1))
        for start, end, weight in pipes:
            unified_edges.append((weight, start, end))
        unified_edges.sort(key=lambda x: x[0])
        djSet = DisjointSet(n)
        total_cost = 0
        for weight, start, end in unified_edges:
            if djSet.union(start, end):
                total_cost += weight
        return total_cost

