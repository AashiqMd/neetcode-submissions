class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[0] * cols for _ in range(rows)]

        def dfs_helper(i,j,idx) -> bool:
            # Base
            if (
                i<0 or i>=rows or
                j<0 or j>=cols or
                visited[i][j] == 1 or
                word[idx] != board[i][j]
            ):
                return False
            if idx == len(word)-1:
                return True

            # Logic
            visited[i][j] = 1
            exists = (
                dfs_helper(i-1,j,idx+1) or
                dfs_helper(i+1,j,idx+1) or
                dfs_helper(i,j-1,idx+1) or
                dfs_helper(i,j+1,idx+1) 
            )
            visited[i][j] = 0

            # Return
            return exists
        
        for r in range(rows):
            for c in range(cols):
                if dfs_helper(r,c,0):
                    return True
        return False