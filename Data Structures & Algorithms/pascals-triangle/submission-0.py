class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp = [0] * (i+1)
            for j, n in enumerate(temp):
                l = res[i-1][j - 1] if j-1 >= 0 else 0
                r = res[i-1][j] if j < len(res[i-1]) else 0
                temp[j] = l + r
            res.append(temp)
        return res