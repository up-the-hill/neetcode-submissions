class Solution:
    def isHappy(self, n: int) -> bool:
        def getHappy(num: int) -> int:
            res = 0
            while num:
                res += ((num % 10) ** 2)
                num //= 10
            return res

        seen = set()
        while True:
            if n in seen:
                return False
            seen.add(n)
            if n == 1:
                return True
            else:
                n = getHappy(n)

        
        