class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Version 3 - DP but space optimized
        dp = [1] * (n+1)
        dp[n] = 0

        for i in range(m-2,-1,-1):
            for j in range(n-1,-1,-1):
                dp[j] += dp[j+1]
        
        return dp[0]

        # Version 2 = TLE
        # def dfs(i,j) -> int:
        #     if i>=m or j>=n:
        #         return 0
        #     if i==m-1 and j==n-1:
        #         return 1
        #     return dfs(i+1,j) + dfs(i,j+1)

        # return dfs(0,0)


        # Version 1
        # dp = [[0] * n for _ in range(m)]

        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if (i,j) == (m-1,n-1):
        #             dp[i][j] = 1
        #         elif i==m-1:
        #             dp[i][j] = dp[i][j+1]
        #         elif j==n-1:
        #             dp[i][j] = dp[i+1][j]
        #         else:
        #             dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        # return dp[0][0]