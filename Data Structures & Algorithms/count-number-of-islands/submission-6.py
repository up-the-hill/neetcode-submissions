class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            while q:
                r, c = q.popleft()
                if (
                    r >= ROWS or 
                    r < 0 or
                    c >= COLS or
                    c < 0 or
                    grid[r][c] == '0'
                ): continue
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    q.append((r+dx, c+dy))
                grid[r][c] = '0'
                    
            
        count = 0
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == '1':
                    count += 1
                    bfs(x, y)
        
        return count
            
