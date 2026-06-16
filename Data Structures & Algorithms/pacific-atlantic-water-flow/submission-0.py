class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac = set()
        atl = set()
        

        def dfs(s, r, c):
            s.add((r, c))
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in s:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    dfs(s, nr, nc)
                    
        for r in range(ROWS):
            dfs(pac, r, 0)
            dfs(atl, r, COLS-1)
        for c in range(COLS):
            dfs(pac, 0, c)
            dfs(atl, ROWS-1, c)
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
            