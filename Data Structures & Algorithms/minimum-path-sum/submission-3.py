class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[float("inf")] * (n+1) for _ in range(m+1)]
        dp[m-1][n] = 0

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])

        return dp[0][0]

        # for i in range(m):
        #     for j in range(n):
        #         if i == j == 0:
        #             dp[i][j] = grid[i][j]
        #         elif i == 0:
        #             dp[i][j] = dp[i][j-1] + grid[i][j]
        #         elif j == 0:
        #             dp[i][j] = dp[i-1][j] + grid[i][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        # return dp[m-1][n-1]