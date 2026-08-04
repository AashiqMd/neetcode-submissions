class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m,n = len(grid),len(grid[0])
        
        def dfs(i,j):
            if (i<0 or j<0 or i>=m or j>=n or 
                grid[i][j]==0 or (i,j) in visited):
                return 0
            visited.add((i,j))

            return (1 + 
                dfs(i+1,j) +
                dfs(i-1,j) +
                dfs(i,j+1) +
                dfs(i,j-1)
            )

        maxCount = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    maxCount = max(dfs(i,j), maxCount)
        
        return maxCount