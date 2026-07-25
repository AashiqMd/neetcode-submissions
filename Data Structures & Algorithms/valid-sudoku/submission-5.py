class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            rowSet = set()
            for j in range(cols):
                if board[i][j] in rowSet:
                    return False
                if board[i][j] != "." and board[i][j] not in rowSet:
                    rowSet.add(board[i][j])
        
        for j in range(cols):
            colSet = set()
            for i in range(rows):
                if board[i][j] in colSet:
                    return False
                if board[i][j] != "." and board[i][j] not in colSet:
                    colSet.add(board[i][j])
        
        # for k in range(9):
        for boxRow in range(3):
            for boxCol in range(3):
                boxSet = set()
                for i in range(boxRow*3, boxRow*3 + 3):
                    for j in range(boxCol*3, boxCol*3 + 3):
                        if board[i][j] in boxSet:
                            return False
                        if board[i][j] != "." and board[i][j] not in boxSet:
                            boxSet.add(board[i][j])

        # Alternate method
        # for k in range(9):
        #     for i in range((k//3)*3, (k//3)*3 + 3):
        #         for j in range(3*k % 9, 3*k % 9 + 3):
        #             if board[i][j] in boxSet:
        #                 return False
        #             if board[i][j] != "." and board[i][j] not in boxSet:
        #                 boxSet.add(board[i][j])
        #     boxSet.clear()

        return True