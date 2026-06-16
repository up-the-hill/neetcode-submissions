class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1] * (n + 1)
        arr[0] = 1

        def dfs(num):
            if arr[num] != -1:
                return arr[num]
            if num == 1:
                arr[num] = 1
            else:
                arr[num] = dfs(num-1)+dfs(num-2)

            return arr[num]
        
        return dfs(n);
                