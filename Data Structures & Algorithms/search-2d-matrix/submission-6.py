class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r: 
            m = (l + r) // 2
            x = m // COLS
            y = m % COLS
            if matrix[x][y] > target: 
                r = m - 1 
            elif matrix[x][y] < target: 
                l = m + 1 
            else:
                return True
        return False
            