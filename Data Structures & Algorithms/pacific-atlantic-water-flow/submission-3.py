class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        pac = set()
        atl = set()
        for i in range(ROWS):
            pac.add((i, 0))
            atl.add((i, COLS-1))

        for j in range(COLS):
            pac.add((0, j))
            atl.add((ROWS - 1, j))
        
        def dfs(cell, st):
            r, c = cell
            for dr, dc in directions:
                tr, tc = r + dr, c + dc
                if (
                    tr in range(ROWS) and
                    tc in range(COLS) and
                    not (tr, tc) in st and
                    heights[r][c] <= heights[tr][tc]
                ): 
                    st.add((tr, tc))
                    dfs((tr, tc), st)

        for p in list(pac):
            dfs(p, pac)
        
        for a in list(atl):
            dfs(a, atl)

        res = []
        for r, c in pac.intersection(atl):
            res.append([r, c])
        return res
