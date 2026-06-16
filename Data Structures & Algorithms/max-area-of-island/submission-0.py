class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs
        R, C = len(grid), len(grid[0])
        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or grid[r][c] == 0
            ): return 0

            grid[r][c] = 0

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        maxArea = 0

        for ri in range(R):
            for ci in range(C):
                if grid[ri][ci] == 1:
                    maxArea = max(dfs(ri,ci), maxArea)
        
        return maxArea
