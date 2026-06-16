class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        # set treasures as starting point
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        distance = 0
        def addCell(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >=len(grid[0]):
                return
            if grid[r][c] == 2147483647:
                grid[r][c] = distance + 1
                q.append((r, c))

        # run multi-source bfs
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            distance += 1
        
        for row in grid:
            print(row)
