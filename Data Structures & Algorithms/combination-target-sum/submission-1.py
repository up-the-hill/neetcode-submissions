class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []

        def dfs(s, i):
            if s > target:
                return
            if s == target:
                res.append(stack.copy())
                return
            for n in range(i, len(nums)):
                stack.append(nums[n])
                dfs(s + nums[n], n)
                stack.pop()
            
        dfs(0, 0)

        return res
        