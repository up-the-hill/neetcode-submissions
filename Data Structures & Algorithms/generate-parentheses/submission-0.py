class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def bt(o:int, c:int) -> str:
            if c == n:
                res.append("".join(stack))
                return
            if o < n:
                stack.append("(")
                bt(o + 1, c)
                stack.pop()
            if o > c:
                stack.append(")")
                bt(o, c + 1)
                stack.pop()
        bt(0, 0)
        return res

        