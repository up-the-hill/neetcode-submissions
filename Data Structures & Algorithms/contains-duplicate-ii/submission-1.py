class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        st = set()
        for r in range(len(nums)):
            if r - l > k:
                st.remove(nums[l])
                l += 1
            if nums[r] in st:
                return True
            st.add(nums[r])


        return False