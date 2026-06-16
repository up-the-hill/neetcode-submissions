class Solution:
    def rob(self, nums: List[int]) -> int:
        sub1, sub2 = nums[1:], nums[:-1]

        def rob(houses):
            rob1, rob2 = 0, 0
            for h in houses:
                temp = max(rob2, rob1+h)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(rob(sub1), rob(sub2)) if len(nums) > 1 else nums[0]