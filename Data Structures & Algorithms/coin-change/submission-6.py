class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [99999] * (amount + 1)
        res[0] = 0
        for i in range(1, len(res)):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i], res[i - coin] + 1)
        return res[-1] if res[-1] < amount + 1 else -1


