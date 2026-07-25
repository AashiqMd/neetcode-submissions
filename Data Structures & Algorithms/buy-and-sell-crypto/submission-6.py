class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Can do forwards or backwards by storing minTillHere or maxTillHere
        maxProfit = 0
        minTillHere = prices[0]

        for price in prices:
            maxProfit = max(maxProfit, price - minTillHere)
            minTillHere = min(minTillHere, price)
        
        return maxProfit