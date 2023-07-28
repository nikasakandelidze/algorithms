from functools import cache

class Solution:
    #   moves: (1,2), (1,-2), (-1, 2), (2,1), (-2,1), (2,-1), (-1,-2), (-2,-1)
    #
    #   We need to either:
    #       - Find some kind of formula that'll give us an answer
    #       - Get the answer by trying every possible answer and calculating a probability
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        deltas = [(1,2), (1,-2), (-1, 2), (2,1), (-2,1), (2,-1), (-1,-2), (-2,-1)]
        def in_bounds(x,y):
            return x >= 0 and y >=0 and x < n and y < n
        @cache
        def recursive(x,y,k):
            if not in_bounds(x,y):
                return 0
            if k == 0:
                return 1
            res = 0
            for dx,dy in deltas:
                temp = recursive(x+dx, y+dy, k-1)
                res += temp * (1/8)
            return res
        return recursive(row, column, k)



