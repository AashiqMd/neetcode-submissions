class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDiag = set() # (r+c) is const
        negDiag = set() # (r-c) is const
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                board[r][c] = '.'
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        
        backtrack(0)
        return res