#https://leetcode.com/problems/min-cost-to-connect-all-points/

class DisjointSet:
    def __init__(self, points):
        self.data = [i for i in range(len(points))]
        self.connectedComponnets = len(points)
        self.ranks = [1 for _ in range(len(points))]

    def find(self, x):
        if self.data[x] == x:
            return self.data[x]
        self.data[x] = self.find(self.data[x])
        return self.data[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.connectedComponnets -= 1
            if self.ranks[rootX] > self.ranks[rootY]:
                self.data[rootY] = rootX
            elif self.ranks[rootY] > self.ranks[rootX]:
                self.data[rootX] = rootY
            else:
                self.data[rootX] = rootY
                self.ranks[rootY] += 1
            return True
        else:
            return False


class Solution:
    def calculateWeight(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def createEdges(self, points):
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((i, j, self.calculateWeight(points[i], points[j])))
        return edges

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = self.createEdges(points)
        edges.sort(key=lambda x: x[2])
        djSet = DisjointSet(points)
        cost = 0
        for start, end, weight in edges:
            if djSet.union(start, end):
                cost += weight
            if djSet.connectedComponnets == 1:
                return cost
        return 0