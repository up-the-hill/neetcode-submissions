class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ROWS = n
        req = n**3
        res = [[0] * ROWS for _ in range(ROWS)]
        t, b, l, r = 0, ROWS-1, 0, ROWS-1
        num = 1
        while t <= b:
            for i in range(l, r+1):
                res[t][i] = num
                num += 1
            t += 1

            for i in range(t, b+1):
                res[i][r] = num
                num += 1
            r -= 1

            for i in range(r, l-1, -1):
                res[b][i] = num
                num += 1
            b -= 1

            for i in range(b, t-1, -1):
                res[i][l] = num
                num += 1
            l += 1

        return res