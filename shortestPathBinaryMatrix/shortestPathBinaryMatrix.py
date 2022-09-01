from typing import List

ways = [(0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (1, 0), (-1, 0), (-1, 1)]


class Solution:
    def inBounds(self, x, y, grid):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid)

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        queue = [((0, 0), 1)]
        visited = {(0, 0)}
        while queue:
            point, length = queue.pop(0)
            x, y = point
            if point == (len(grid) - 1, len(grid) - 1):
                return length
            for dx, dy in ways:
                newx = x + dx
                newy = y + dy
                if self.inBounds(newx, newy, grid) and grid[newx][newy] == 0 and (newx, newy) not in visited:
                    queue.append(((newx, newy), length + 1))
                    visited.add((newx, newy))
        return -1
