class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def bt(i, s, stack):
            if s == target:
                res.append(stack.copy())
                return 
            if i >= len(candidates) or s > target:
                return
            stack.append(candidates[i])
            bt(i+1, s+candidates[i], stack)
            stack.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bt(i+1, s, stack)
        
        bt(0, 0, [])

        return res