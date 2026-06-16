class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            m_el = matrix[m//COLS][m%COLS]
            if target == m_el:
                return True
            elif target > m_el:
                l = m + 1
            elif target < m_el:
                r = m - 1
            
        return False
            
        