class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        
        def bt(i):
            if i == len(nums):
                res.append(stack.copy())
                return
            
            stack.append(nums[i])
            bt(i + 1)

            stack.pop()
            bt(i + 1)
        
        bt(0)
        
        return res
        