class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min cost to reach the top step from i
        n = len(cost)
        dp = [0] * (n+1)
        dp[n], dp[n-1] = 0, cost[n-1]

        for i in range(n-2, -1,-1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])
        
        # # dp[i] = min cost to reach ith step
        # # Need to return dp[n]
        # dp = [0] * (len(cost)+1)
        # dp[0], dp[1] = 0, 0

        # for i in range(2, len(cost)+1):
        #     dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])

        # return dp[-1] 
