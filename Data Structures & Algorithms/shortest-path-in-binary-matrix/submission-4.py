class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1))
        ROWS, COLS = len(grid), len(grid[0]) 
        end = (ROWS - 1, COLS - 1)
        if grid[end[0]][end[1]] == 1 or grid[0][0] == 1:
            return -1

        q = deque() # distance, cell
        q.append((1,(0,0)))
        seen = {(0,0)}

        while q:
            d, (x, y) = q.popleft()
            if (x,y) == end:
                return d
            for dx, dy in dirs:
                i, j = x+dx, y+dy
                if (
                    i >= 0 and i < ROWS and 
                    j >= 0 and j < COLS and
                    grid[i][j] == 0 and
                    (i, j) not in seen
                ):
                    seen.add((i,j))
                    q.append((d+1,(i,j)))

        return -1