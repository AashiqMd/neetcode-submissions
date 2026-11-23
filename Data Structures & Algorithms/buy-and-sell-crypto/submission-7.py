class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = prices[0]

        for p in prices[1:]:
            if p < min_p:
                min_p = p
            else:
                profit = max(profit, p - min_p)
        return profit