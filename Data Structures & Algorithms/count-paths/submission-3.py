class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Version 3 - DP but space optimized
        dp = [1] * (n+1)
        dp[n] = 0

        for i in range(m-2,-1,-1):
            for j in range(n-1,-1,-1):
                dp[j] += dp[j+1]
        
        return dp[0]

        