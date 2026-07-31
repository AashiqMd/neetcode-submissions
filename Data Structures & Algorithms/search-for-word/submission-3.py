class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i,j,idx):
            if (i<0 or j<0 or i>=ROWS or j>=COLS or 
                idx>=len(word) or word[idx] != board[i][j]):
                return False
            if idx == (len(word)-1):
                return True
            visited.add((i,j))
            
            for dr, dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                nr, nc = i+dr, j+dc
                if (nr,nc) not in visited and dfs(nr,nc,idx+1):
                    return True
            
            visited.remove((i,j))

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        
        return False