class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0

        # We assume that i is the day we sell and calculate the best profit possible.
        # Either sell or don't sell
        for price in prices:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)
        return profit
        
        # n = len(prices)
        # maxSoFar = [prices[n-1]] * n
        # bestProfit = 0

        # for i in range(n-2,-1,-1):
        #     maxSoFar[i] = max(prices[i], maxSoFar[i+1])
        
        # # Cannot calculate a profit after buying on last day
        # for i in range(n-1):
        #     bestProfit = max(bestProfit, maxSoFar[i+1] - prices[i])
        # return bestProfit
