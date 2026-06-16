class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # layer dfs
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: fresh += 1
                if grid[r][c] == 2: q.append((r, c))

        layer = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    rx, ry = x + dx, y + dy
                    if (
                        rx < 0 or
                        rx >= ROWS or
                        ry < 0 or
                        ry >= COLS or
                        grid[rx][ry] == 2 or
                        grid[rx][ry] == 0
                    ): continue
                    grid[rx][ry] = 2
                    fresh -= 1
                    q.append((rx, ry))
            layer += 1
        
        return layer if fresh == 0 else -1