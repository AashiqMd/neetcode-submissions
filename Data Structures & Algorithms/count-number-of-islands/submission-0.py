class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 0 = water, 1=land, 2=visited land
        rows, cols = len(grid), len(grid[0])
        numIslands = 0

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] != "1":
                return
            grid[i][j] = "2"

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    numIslands +=1

        return numIslands