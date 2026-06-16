class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i, n in enumerate(nums):
            if n in hm:
                return [hm[n], i]
            hm[target - n] = i
        

