# https://leetcode.com/problems/graph-valid-tree/

class DisjointSet:
    def __init__(self, size):
        self.data = [i for i in range(size)]
        self.numConnectedComponents = size
        self.hasCycles = False

    def find(self, x):
        if self.data[x] == x:
            return x
        self.data[x] = self.find(self.data[x])
        return self.data[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            self.hasCycles = True
        else:
            self.data[rootX] = rootY
            self.numConnectedComponents -= 1


class Solution:
    def getSizeOfVerticies(self, edges):
        verticies = set()
        for start, end in edges:
            verticies.add(start)
            verticies.add(end)
        return len(verticies)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        disjointSet = DisjointSet(n)
        for start, end in edges:
            disjointSet.union(start, end)
        return disjointSet.numConnectedComponents == 1 and not disjointSet.hasCycles