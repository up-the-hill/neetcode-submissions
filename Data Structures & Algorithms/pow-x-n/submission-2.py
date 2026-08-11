class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num, pow):
            if num == 0: return 0
            if pow == 0: return 1
            if pow % 2 == 1:
                return num * helper(num, pow - 1)
            else:
                l = helper(num, pow // 2)
                return l * l

        res = helper(x, abs(n))

        return res if n >= 0 else 1/res