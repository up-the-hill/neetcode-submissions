class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * (numRows)
        rowPos = 0
        reversing = False
        for i, c in enumerate(s):
            print(rowPos)
            rows[rowPos] += c
            if reversing:
                if rowPos == 0:
                    rowPos += 1
                    reversing = False
                else:
                    rowPos -= 1
            else:
                if rowPos == numRows - 1:
                    rowPos -= 1
                    reversing = True
                else:
                    rowPos += 1
        return ''.join(rows)


