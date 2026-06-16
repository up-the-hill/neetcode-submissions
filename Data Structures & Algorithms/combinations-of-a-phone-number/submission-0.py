class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        res = []

        def dfs(i, stack):
            if i >= len(digits):
                res.append(''.join(stack))
                return 
            for c in digitToChar[digits[i]]:
                stack.append(c)
                dfs(i+1, stack)
                stack.pop()
        
        dfs(0, [])

        return res