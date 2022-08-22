# https://leetcode.com/problems/number-of-provinces/

class DisjointSet:
    def __init__(self, size):
        self.representatives = [i for i in range(size)]
        self.connectedComponents = size
        self.ranks = [1 for i in range(size)]

    def addConnection(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.connectedComponents -= 1
            if self.ranks[rootX] > self.ranks[rootY]:
                self.representatives[rootY] = rootX
            elif self.ranks[rootX] < self.ranks[rootY]:
                self.representatives[rootX] = rootY
            else:
                self.representatives[rootX] = rootY
                self.ranks[rootY] += 1

    def find(self, x):
        if self.representatives[x] == x: return x
        self.representatives[x] = self.find(self.representatives[x])
        return self.representatives[x]

    def numberOfConnectedComponents(self):
        return self.connectedComponents


class Solution(object):
    def __init__(self):
        self.representatives = []

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        dset = DisjointSet(len(isConnected))
        for x in range(len(isConnected)):
            for y in range(len(isConnected[x])):
                if x != y and isConnected[x][y] == 1:
                    dset.addConnection(x, y)
        return dset.numberOfConnectedComponents()


solution = Solution()
result = solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
assert result == 2