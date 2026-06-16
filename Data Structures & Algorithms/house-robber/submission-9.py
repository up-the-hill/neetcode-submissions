class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for h in nums:
            temp = max(rob2, rob1+h)
            rob1 = rob2
            rob2 = temp
        return rob2
        