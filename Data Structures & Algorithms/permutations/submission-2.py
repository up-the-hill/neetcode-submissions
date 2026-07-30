class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            temp = []
            for r in res:
                for i in range(len(r) + 1):
                    temp.append(r[:i] + [n] + r[i:])
            res = temp
        return res