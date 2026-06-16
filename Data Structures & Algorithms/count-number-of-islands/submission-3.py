class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                    continue
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    for d in directions:
                        q.append((row + d[0], col + d[1]))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        
        return count

        