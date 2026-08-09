class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToSet = set()
        colsToSet = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsToSet.add(i)
                    colsToSet.add(j)
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowsToSet or j in colsToSet:
                    matrix[i][j] = 0
        
