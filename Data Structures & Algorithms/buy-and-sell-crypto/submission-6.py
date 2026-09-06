class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for i, price in enumerate(prices):
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        
        return profit

