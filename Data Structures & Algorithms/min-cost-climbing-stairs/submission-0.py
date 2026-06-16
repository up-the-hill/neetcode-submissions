class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)

        def dfs(n):
            if n == 1 or n == 0:
                return 0
            return min((cost[n-1] + dfs(n-1)), (cost[n-2] + dfs(n-2)))
        
        return dfs(top)
        