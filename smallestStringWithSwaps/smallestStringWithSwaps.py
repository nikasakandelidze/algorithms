# https://leetcode.com/problems/smallest-string-with-swaps/
from collections import defaultdict


class DisjointSet:

    def __init__(self, string):
        self.data = [i for i in range(len(string))]
        self.rank = [1 for i in range(len(string))]

    def join(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.data[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.data[rootX] = rootY
            else:
                self.rank[rootX] += 1
                self.data[rootY] = rootX

    def find(self, x):
        if self.data[x] == x:
            return x
        self.data[x] = self.find(self.data[x])
        return self.data[x]


class Solution(object):
    # [[0, 3], [1, 2]] dcab 3 2 2 3
    # if N characters are in same connected component we can sort them by alphabet and that would be
    # the smallest lexicographic result
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        djSet = DisjointSet(s)
        res = [x for x in s]
        for start, end in pairs:
            djSet.join(start, end)
        mappings = defaultdict(list)
        for i in range(len(s)):
            root = djSet.find(i)
            mappings[root].append(i)
        for k in mappings:
            vals = mappings[k]
            resCopy = res[:]
            valsCopy = vals[:]
            valsCopy.sort(key=lambda x: res[x])
            for i in range(len(vals)):
                resCopy[vals[i]] = res[valsCopy[i]]
            res = resCopy
        return ''.join(res)


