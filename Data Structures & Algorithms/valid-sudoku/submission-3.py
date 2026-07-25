class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        rowSet = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in rowSet:
                    return False
                if board[i][j] != "." and board[i][j] not in rowSet:
                    rowSet.add(board[i][j])
            rowSet.clear()
        
        colSet = set()
        for j in range(cols):
            for i in range(rows):
                if board[i][j] in colSet:
                    return False
                if board[i][j] != "." and board[i][j] not in colSet:
                    colSet.add(board[i][j])
            colSet.clear()
        
        boxSet = set()
        # for k in range(9):
        for boxRow in range(3):
            for boxCol in range(3):
                for i in range(boxRow*3, boxRow*3 + 3):
                    for j in range(boxCol*3, boxCol*3 + 3):
                        if board[i][j] in boxSet:
                            return False
                        if board[i][j] != "." and board[i][j] not in boxSet:
                            boxSet.add(board[i][j])
                boxSet.clear()

        return True