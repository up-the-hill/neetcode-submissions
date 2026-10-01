class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sort = sorted(nums)
        rev = list(reversed(sort))

        return nums == sort or nums == rev