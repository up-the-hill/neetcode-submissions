class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            dirs = ( (1,0), (-1,0),(0,1), (0,-1))

            res = 1
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < ROWS and 0 <= y < COLS and matrix[x][y] > matrix[i][j]:
                    res = max(res, 1+dfs(x, y))
            dp[i][j] = res
            return res
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                temp = dfs(i, j)
                res = max(res, temp)
        
        return res