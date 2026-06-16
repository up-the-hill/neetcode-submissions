class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return ( 
                dfs(r, c+1)+
                dfs(r, c-1)+
                dfs(r+1, c)+
                dfs(r-1, c)+
                1
            )
        
        max_area = 0

        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(dfs(r, c), max_area)

        return max_area
