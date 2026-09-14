class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        for _ in range(k):
            tmp = []
            for item in res:
                start = item[-1]+1 if item else 1
                for i in range(start, n+1):
                    tmp.append(item+[i])
            res = tmp
        return res
        