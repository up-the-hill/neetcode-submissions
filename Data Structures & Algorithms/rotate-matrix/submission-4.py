class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        t, b = 0, len(matrix) - 1

        while t < b:
            for i in range(b-t):
                l, r = t, b
                temp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = temp

            print(matrix)
            t += 1
            b -= 1