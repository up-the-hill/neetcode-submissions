class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num, power):
            if num == 0: return 0
            if power == 0: return 1

            res = helper(num, power // 2)
            return res * res if power % 2 == 0 else res * res * num

        res = helper(x, abs(n))

        return res if n >= 0 else 1/res