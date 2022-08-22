from typing import List

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


class Solution:
    #   looks like a BFS problem
    #   since 2 neihgbouring orange to a rotten orange both become rotten on the same minute.

    def inBounds(self, x, y, grid):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x])

    def letTheTimeTick(self, grid, rottens):
        time = 0
        queue = []
        for x, y in rottens:
            queue.append((x, y, 0))
        while queue:
            temporary_queue = []
            time += 1
            while queue:
                x, y, time = queue.pop(0)
                for dx, dy in dirs:
                    new_x = x + dx
                    new_y = y + dy
                    if self.inBounds(new_x, new_y, grid) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        temporary_queue.append((new_x, new_y, time + 1))
            queue += temporary_queue
        return time

    def getCoordinatesOfOranges(self, grid, value):
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == value:
                    result.append((i, j))
        return result

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = self.getCoordinatesOfOranges(grid, 2)
        result = self.letTheTimeTick(grid, rottens)
        healthy = self.getCoordinatesOfOranges(grid, 1)
        return result if len(healthy) == 0 else -1


solution = Solution()
result = solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
assert result == 4