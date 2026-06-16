class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        arr = [-1] * (top + 1)

        def dfs(n):
            if n == 1 or n == 0:
                return 0
            if arr[n] != -1:
                return arr[n]
            else:
                arr[n] = min((cost[n-1] + dfs(n-1)), (cost[n-2] + dfs(n-2)))

            return arr[n]
        
        return dfs(top)
        