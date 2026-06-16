class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                for d in directions:
                    if (
                        0 <= r + d[0] < ROWS and
                        0 <= c + d[1] < COLS
                    ):
                        dfs(r + d[0], c + d[1])
        

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        
        return count

        