class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [101] * (len(cost))
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2, len(res)):
            res[i] = min(res[i - 1] + cost[i], res[i - 2] + cost[i])
        print(res)
        return min(res[-1], res[-2])