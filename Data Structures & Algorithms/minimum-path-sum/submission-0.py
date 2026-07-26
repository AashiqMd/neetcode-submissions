class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j] + grid[i-1][j], dp[i][j-1] + grid[i][j-1])

        return dp[m-1][n-1] + grid[m-1][n-1]