class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest = [amount+1] * (amount+1)
        fewest[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0: 
                    fewest[i] = min(fewest[i], 1+fewest[i-coin])
        return fewest[-1] if fewest[-1] <= amount else -1

        