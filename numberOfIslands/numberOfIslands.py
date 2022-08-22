from typing import List

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def _conquerFoundIsland(self, x, y, grid):
        if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x]):
            if grid[x][y] != '1':
                return
            grid[x][y] = '0'
            for dx, dy in dirs:
                self._conquerFoundIsland(x + dx, y + dy, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    counter += 1
                    self._conquerFoundIsland(i, j, grid)
        return counter


solution = Solution()
result = solution.numIslands([["1", "1", "1"], ["0", "0", "0"], ["1", "0", "1"]])
assert result == 3
