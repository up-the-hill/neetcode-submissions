class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(profit, res)
            if prices[l] > prices[r]:
                l = r
            r += 1
        return res