from typing import List

# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class DisjointSet:
    def __init__(self, n):
        self.data = [i for i in range(n)]
        self.numConnectedComponents = n

    def find(self, x):
        if self.data[x] == x:
            return x
        self.data[x] = self.find(self.data[x])
        return self.data[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.data[rootX] = rootY
            self.numConnectedComponents -= 1

    def singleConnectedComponent(self):
        return self.numConnectedComponents == 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        disjointSet = DisjointSet(n)
        for timestamp, x, y in logs:
            disjointSet.union(x, y)
            if disjointSet.singleConnectedComponent():
                return timestamp
        return -1
