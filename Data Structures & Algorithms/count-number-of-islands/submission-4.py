class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(i,j):
            if (0<=i<ROWS) and (0<=j<COLS) and grid[i][j] == '1':
                grid[i][j] = '0'
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = i + dr, j + dc
                    dfs(nr,nc)
            else:
                return

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        
        return count