class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = number of distinct ways to climb to i
        dp_1, dp_2 = 1,2
        if n == 1:
            return dp_1

        for i in range(3,n+1):
            dp_1, dp_2 = dp_2, dp_1 + dp_2

        return dp_2
