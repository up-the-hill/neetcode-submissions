class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        seen = set()

        def bt():
            if len(stack) == len(nums):
                res.append(stack.copy())
                return
            
            for n in nums:
                if n in seen:
                    continue
                
                stack.append(n)
                seen.add(n)
                bt()
                stack.pop()
                seen.remove(n)

        
        bt()

        return res
        