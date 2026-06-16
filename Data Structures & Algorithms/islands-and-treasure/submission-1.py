class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        # layer bfs
        distance = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (
                        0 <= r+d[0] < ROWS and
                        0 <= c+d[1] < COLS and
                        grid[r+d[0]][c+d[1]] == 2147483647
                    ):
                        grid[r+d[0]][c+d[1]] = distance
                        q.append((r+d[0], c+d[1]))
            distance += 1
        



