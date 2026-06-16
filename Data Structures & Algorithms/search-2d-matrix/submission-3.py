class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        def iToPos(i: int):
            return (i // len(matrix[0]), i % len(matrix[0]))

        while l <= r:
            m = l + (r-l)//2
            row, col = iToPos(m)
            print(row, col)
            if target < matrix[row][col]:
                r = r - 1
            if target > matrix[row][col]:
                l = l + 1
            if target == matrix[row][col]:
                return True
        return False