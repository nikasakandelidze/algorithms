# problem: https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution(object):
    # Let's use graphs to solve this problem
    # The idea is two nodes: a and b are neighbouring if a == b
    # and there is a path between two nodes a and c if a == middle man b and == c
    # each node will have constrained list of nodes where path shouldn't exist
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        def dfs(neighbours, start, target):
            visited = {start}
            stack = [start]
            while stack:
                element = stack.pop()
                if element == target:
                    return True
                for n in neighbours[element]:
                    if n not in visited:
                        stack.append(n)
                        visited.add(n)
            return False

        neighbours = {}
        for eq in equations:
            var1 = eq[0]
            var2 = eq[3]
            equals = eq[1:3] == "=="
            if equals:
                if var1 not in neighbours:
                    neighbours[var1] = [var2]
                else:
                    neighbours[var1].append(var2)
                if var2 not in neighbours:
                    neighbours[var2] = [var1]
                else:
                    neighbours[var2].append(var1)
        for eq in equations:
            var1 = eq[0]
            var2 = eq[3]
            equals = eq[1:3] == "=="
            if not equals:
                if var1 == var2:
                    return False
                if var1 in neighbours and var2 in neighbours:
                    if dfs(neighbours, var1, var2):
                        return False
        return True



