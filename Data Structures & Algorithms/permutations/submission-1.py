class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            new = []
            for p in res:
                for pos in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(pos, n)
                    new.append(copy)
            res = new

        return res
