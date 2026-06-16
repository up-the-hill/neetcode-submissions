class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow2


