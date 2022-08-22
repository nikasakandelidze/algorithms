from typing import List

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:

    def _dfs(self, matrix, boolMatrix, x, y):
        if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[x]) and matrix[x][y] == 'O' and boolMatrix[x][
            y] == True:
            boolMatrix[x][y] = False
            for dx, dy in dirs:
                self._dfs(matrix, boolMatrix, x + dx, y + dy)

    def _buildFlippableMatrix(self, board):
        result = [[True for _ in board[row]] for row in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[x])):
                if x == 0 or y == 0 or x == len(board) - 1 or y == len(board[x]) - 1:
                    if board[x][y] == 'O':
                        self._dfs(board, result, x, y)
        return result

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        flippable = self._buildFlippableMatrix(board)
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 'O' and flippable[x][y]:
                    board[x][y] = 'X'


input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solution = Solution()
solution.solve(input)
assert input == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]