class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        R, C = len(grid), len(grid[0])
        # bfs, keep count of breadths searched
        depth = 0
        fresh = 0
        q = collections.deque()

        def addCell(r, c):
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or grid[r][c] == 0
                or grid[r][c] == 2
            ): return
            seen.add((r, c))
            q.append((r, c))

        for ri in range(R):
            for ci in range(C):
                if grid[ri][ci] == 2:
                    seen.add((ri, ci))
                    q.append((ri, ci))
                elif grid[ri][ci] == 1:
                    fresh += 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == 1: fresh -= 1
                grid[r][c] = 2

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            depth += 1
        
        depth = depth - 1 if depth else 0

        return depth if fresh == 0 else -1
        
        
