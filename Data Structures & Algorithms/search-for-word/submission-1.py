class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        found = False

        def dfs(r, c, i):
            # if index is at 4, it passed checks for all 3 letters
            if i >= len(word):
                nonlocal found
                found = True
                return
            
            # check if out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 

            # check if letter matches
            if board[r][c] != word[i]:
                return
            
            board[r][c] = '*'
            dfs(r+1, c, i+1)
            dfs(r-1, c, i+1)
            dfs(r, c+1, i+1)
            dfs(r, c-1, i+1)
            board[r][c] = word[i]

        for r in range(ROWS):
            print(board[r])
            for c in range(COLS):
                dfs(r, c, 0)
        

        return found