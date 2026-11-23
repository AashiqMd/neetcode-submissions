class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1

        dp_1, dp_2 = 1,2
        for i in range(3,n+1):
            dp_1, dp_2 = dp_2, dp_1 + dp_2
        return dp_2
        # dp = [0]*(n+1)
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]