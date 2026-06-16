class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs
        R, C = len(grid), len(grid[0])
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
            while q:
                row, col = q.popleft()
                if (
                    row < 0
                    or col < 0
                    or row >= R
                    or col >= C
                    or grid[row][col] == "0"
                ): continue

                grid[row][col] = "0"

                for d in ds:
                    q.append((row + d[0], col + d[1]))
            
        islands = 0
        for ri in range(R):
            for ci in range(C):
                if grid[ri][ci] == "1":
                    islands += 1
                    bfs(ri, ci)
                    
        return islands
