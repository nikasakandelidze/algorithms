def isValidSudoku(board):
    boxSets = [[set() for _ in range(0, 3)] for _ in range(0, 3)]
    columnSets = [set() for _ in board]
    for row in range(len(board)):
        rowSet = set()
        for column in range(len(board[row])):
            element = board[row][column]
            if not element.isnumeric():
                continue
            if element in rowSet:
                return False
            else:
                rowSet.add(element)
            columnSet = columnSets[column]
            if element in columnSet:
                return False
            else:
                columnSet.add(element)
            boxColumn = column // 3
            boxRow = row // 3
            boxSet = boxSets[boxRow][boxColumn]
            if element in boxSet:
                return False
            else:
                boxSet.add(element)
    return True


assert True == isValidSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
