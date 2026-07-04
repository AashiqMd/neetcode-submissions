class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = number of distinct ways to climb to i
        dp = [0] * (n+1)
        for i in range(1,n+1):
            if i <= 2:
                dp[i] = i
            else:
                dp[i] = dp[i-1] + dp[i-2]
        
        print(dp)
        return dp[n]
