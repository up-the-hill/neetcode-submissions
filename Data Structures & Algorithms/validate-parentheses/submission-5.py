class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c not in d:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != d[c]:
                    return False
                else:
                    stack.pop()

        return True if len(stack) == 0 else False
            
        