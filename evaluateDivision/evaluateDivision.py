class Solution(object):
    def buildAdjMap(self, equations, values):
        mapping = {}
        for i in range(len(equations)):
            e = equations[i]
            first = e[0]
            second = e[1]
            if first not in mapping:
                mapping[first] = [(second, values[i])]
            else:
                mapping[first].append((second, values[i]))
            if second not in mapping:
                mapping[second] = [(first, 1 / values[i])]
            else:
                mapping[second].append((first, 1 / values[i]))
        return mapping

    def dfs(self, adjMap, start, end, visited, res):
        if start == end:
            return res
        else:
            neighbours = adjMap[start]
            for n in neighbours:
                if n[0] not in visited:
                    v = set(visited)
                    v.add(n[0])
                    r = self.dfs(adjMap, n[0], end, v, res * n[1])
                    if r != -1:
                        return r
        return -1

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adjMap = self.buildAdjMap(equations, values)
        print(adjMap)
        res = []
        for q in queries:
            start = q[0]
            end = q[1]
            if start not in adjMap or end not in adjMap:
                res.append(-1.0)
            else:
                res.append(self.dfs(adjMap, start, end, set(), 1.0))
        return res