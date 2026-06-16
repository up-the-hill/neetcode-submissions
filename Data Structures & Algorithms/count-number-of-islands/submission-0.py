class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        def dfs(row, col):
            if (
                row < 0 
                or col < 0 
                or row >= len(grid) 
                or col >= len(grid[0])
                ):
                return

            if grid[row][col] == "1":
                grid[row][col] = "0"
                for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    dfs(row+direction[0], col+direction[1])
        
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        print(grid)

        return islands
