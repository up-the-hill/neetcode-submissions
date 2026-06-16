class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(x, y):
            if (
                x >= ROWS or 
                x < 0 or
                y >= COLS or
                y < 0 or
                grid[x][y] == '0'
            ): return
            grid[x][y]= '0'
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(x+d[0], y+d[1])
            
        count = 0
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x, y)
        
        return count
            
