class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            else:
                res = max(res, profit)
        
        return res
            

        