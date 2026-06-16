class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def bt(i, s):
            if s == target:
                res.append(comb.copy())
                return
            if s > target or i >= len(nums):
                return
            
            comb.append(nums[i])
            bt(i, s + nums[i])
            comb.pop()
            bt(i + 1, s)

            
        bt(0, 0)
        
        return res