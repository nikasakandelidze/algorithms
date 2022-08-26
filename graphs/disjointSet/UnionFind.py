class QuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    # In quick find structure finding whether or not two components are connectd is O(1)
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # In quick find structure finding union operation is O(N)
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootX:
                    self.root[i] = rootY


class QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # In Quick Union structure find function takes O(N) time
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # In Quick Union structure union function takes O(N) time
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[x] = rootY


class UnionByRankAndFindByPathCompression:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.rank[rootY] += 1
                self.root[rootX] = rootY

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)
