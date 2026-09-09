class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        for _ in range(k):
            temp = []
            for item in res:
                start = item[-1]+1 if item else 1
                for i in range(start, n+1):
                    temp.append(item + [i])
            res = temp

        return res