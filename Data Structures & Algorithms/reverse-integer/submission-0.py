class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 4294967295, -4294967296
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            if res >= MAX // 10:
                return 0
            last = x % 10
            res = res * 10 + last
            x = x // 10
        return res * sign

        