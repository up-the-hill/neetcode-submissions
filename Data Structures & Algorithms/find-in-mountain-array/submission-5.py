class Solution:
    def findInMountainArray(self, target: int, mountainArr: "MountainArray") -> int:
        l, r = 1, mountainArr.length() - 2
        peak = -1
        # find the peak
        while l <= r:
            m = (l + r) // 2
            # get m, and the numbers around it to know where we are.
            if mountainArr.get(m) > mountainArr.get(m - 1) and mountainArr.get(m) > mountainArr.get(
                m + 1
            ):
                peak = m
                break
            elif mountainArr.get(m - 1) < mountainArr.get(m) and mountainArr.get(
                m
            ) < mountainArr.get(m + 1):
                # in left half
                l = m + 1
            elif mountainArr.get(m - 1) > mountainArr.get(m) and mountainArr.get(
                m
            ) > mountainArr.get(m + 1):
                r = m - 1

        # with the peak, now run 2 binary searches
        l1, r1 = 0, peak
        l2, r2 = peak, mountainArr.length() - 1
        while l1 <= r1:
            m = (l1 + r1) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) < target:
                l1 = m + 1
            elif mountainArr.get(m) > target:
                r1 = m - 1
        # not found, search 2nd half

        while l2 <= r2:
            m = (l2 + r2) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                l2 = m + 1
            elif mountainArr.get(m) < target:
                r2 = m - 1

        # not found, return -1
        return -1
