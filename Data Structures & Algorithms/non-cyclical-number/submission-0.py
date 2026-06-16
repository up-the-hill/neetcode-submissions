class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            res = 0
            while n != 0:
                lastDigit = n % 10
                res += lastDigit ** 2
                n = n // 10
            return res
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumOfSquares(n)

        return True
            