class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Optimize the lower solution with a 1D DP
        m = len(grid)
        n = len(grid[0])

        dp = [float("inf")] * (n+1)

        # I intially made dp[n]=0. But dp[n] will never get recalculated. 
        # It assumes the right path is always free since the value is 0. 
        dp[n-1] = 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[j] = grid[i][j] + min(dp[j], dp[j+1])
        return dp[0]

        # # Flip the problem. Try to go from bottom right to top left. 
        # # This is because it is easy to add an extra row and column to the bottom and right. 
        # m = len(grid)
        # n = len(grid[0])

        # dp = [[float("inf")] * (n+1) for _ in range(m+1)]
        # dp[m][n-1] = 0 
        
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        
        # return dp[0][0]


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