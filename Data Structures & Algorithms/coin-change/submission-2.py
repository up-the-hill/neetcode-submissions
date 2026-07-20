class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        req = [amount + 1] * (amount + 1)
        req[0] = 0
        for i in range(1, len(req)):
            for c in coins: 
                if i - c >= 0:
                    req[i] = min(req[i], req[i - c] + 1)
        
        if req[-1] == amount + 1:
            return -1
        else: return req[-1]