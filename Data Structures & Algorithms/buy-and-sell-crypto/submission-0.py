class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxSoFar = [prices[n-1]] * n
        bestProfit = 0

        for i in range(n-2,-1,-1):
            maxSoFar[i] = max(prices[i], maxSoFar[i+1])
        
        # Cannot calculate a profit after buying on last day
        for i in range(n-1):
            bestProfit = max(bestProfit, maxSoFar[i+1] - prices[i])
        return bestProfit
