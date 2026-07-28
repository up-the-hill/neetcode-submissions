class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
            res = 0
            if j == len(t):
                res += 1
                return 1 
            if i >= len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            res += dfs(i+1, j)
            cache[(i, j)] = res
            return res

        return dfs(0, 0)