class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        # dp[i] = minimum number of coins to get i.

        for i in range(1, amount+1):
            for coin in coins:
                if amount - coin >= 0 and dp[i-coin] >-1:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
            if dp[i] == amount+1:
                dp[i] = -1

        print(dp)
        return dp[amount]