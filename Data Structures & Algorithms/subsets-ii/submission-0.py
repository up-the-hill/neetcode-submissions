class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(i, stack):
            if i >= len(nums):
                res.append(stack.copy())
                return 
            stack.append(nums[i])
            bt(i + 1, stack)
            stack.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i = i + 1
            bt(i + 1, stack)

        bt(0, [])

        return res