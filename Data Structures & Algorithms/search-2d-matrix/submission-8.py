class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = (l + r) // 2
            m_n = matrix[m // COLS][m % COLS]
            if target < m_n:
                r = m - 1
            elif target > m_n:
                l = m + 1
            else: 
                return True
        return False
