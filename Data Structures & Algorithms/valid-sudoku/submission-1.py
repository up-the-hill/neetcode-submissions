class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                cell = board[r][c]
                if cell == ".": continue
                if (
                    cell in row_set[r] or
                    cell in col_set[c] or
                    cell in box_set[(r // 3)*3 + c//3]
                ):
                    return False
                row_set[r].add(cell)
                col_set[c].add(cell)
                box_set[(r//3) * 3 + c//3].add(cell)
                
        
        return True
